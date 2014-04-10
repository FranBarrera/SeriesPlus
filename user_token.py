import requests
from getpass import getpass
import json

fichero = open('auth.txt','r')
auth_token = fichero.readline()


def fuser_token():
	username = raw_input('Username: ')
	password = getpass('Password: ')
	q = {'auth_token':auth_token,'username':username,'password':password,'remember':'0'}
	r = requests.get('http://api.series.ly/v2/user/user_token',params=q)
	jresp = json.loads(r.text)
	return jresp['user_token']


def fseriesfollowing():
	user_token = fuser_token()
	q_sf = {'auth_token':auth_token,'user_token':user_token}
	r_sf = requests.get('http://api.series.ly/v2/user/media/series',params=q_sf)
	jresp = json.loads(r_sf.text)
	for i in jresp['series']:
		print i['name']

prueba = fseriesfollowing()

fichero.close()

