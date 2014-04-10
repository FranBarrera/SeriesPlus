import requests
from getpass import getpass
import json
from bottle import route, run, template


fichero = open('auth.txt','r')
auth_token = fichero.readline()
respuesta = open('most_seen.txt','w')
fi_usertoken = open('user_token.txt','w')


def fuser_token():
	username = raw_input('Username: ')
	password = getpass('Password: ')
	q = {'auth_token':auth_token,'username':username,'password':password,'remember':'0'}
	r = requests.get('http://api.series.ly/v2/user/user_token',params=q)
	jresp = json.loads(r.text)
	token = jresp['user_token']
	fi_usertoken.write(token)
	return jresp['user_token']


def fseriesfollowing():
	user_token = fuser_token()
	q_sf = {'auth_token':auth_token,'user_token':user_token}
	r_sf = requests.get('http://api.series.ly/v2/user/media/series',params=q_sf)
	jresp = json.loads(r_sf.text)
	return jresp

seriesfollow = fseriesfollowing()
nombres = []
for i in seriesfollow['series']:
	nombres.append(i['name'])

def fseriesmostseen():
	q = {'auth_token':auth_token}
	r = requests.get('http://api.series.ly/v2/media/most_seen',params=q)
	jresp = json.loads(r.text)
	return jresp

seriesmost = fseriesmostseen()
nombres_mostseen = []
for i in seriesmost['series']:
	nombres_mostseen.append(i['name'])

@route('/')
def test():
	return template('template.tpl',nombres=nombres,mostnombre=nombres_mostseen)

run(host='localhost', port=8080)

fichero.close()

