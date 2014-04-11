import requests
from getpass import getpass
import json
from bottle import route, run, template, get, post


fichero = open('auth.txt','r')
auth_token = fichero.readline()
respuesta = open('most_seen.txt','w')
fi_usertoken = open('user_token.txt','w')


def fuser_token(username, password):
#	username = raw_input('Username: ')
#	password = getpass('Password: ')
	q = {'auth_token':auth_token,'username':username,'password':password,'remember':'1'}
	r = requests.get('http://api.series.ly/v2/user/user_token',params=q)
	if r.status_code == 200:
		jresp = json.loads(r.text)
		token = jresp['user_token']
		#fi_usertoken.write(token)
		return token
	else:
		return ''	

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


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
	token1 = fuser_token(username,password)
    if len(token1) > 0:
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"



@route('/template')
def test():
	return template('template.tpl',nombres=nombres,nombres_mostseen=nombres_mostseen)
run(host='localhost', port=8080)



fichero.close()
respuesta.close()
fi_usertoken.close()

