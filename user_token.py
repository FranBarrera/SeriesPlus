import requests
from getpass import getpass
import json

fichero = open('auth.txt','r')
auth_token = fichero.readline()
username = raw_input('Username')
password = getpass('Password')


q = {'auth_token':auth_token,'username':username,'password':password,'remember':'0'}
r = requests.get('http://api.series.ly/v2/user/user_token',params=q)

jresp = json.loads(r.text)

user_token = jresp['user_token']

def seriesfollowing():
	q_sf = {'auth_token':auth_token,'user_token':user_token}
	r_sf = requests.get('http://api.series.ly/v2/user/media/series',params=q_sf)
	jresp = json.loads(r_sf.text)
	return jresp