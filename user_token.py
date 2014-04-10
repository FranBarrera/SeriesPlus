import requests
from getpass import getpass


fichero = open('auth.txt','r')
auth_token = fichero.readline()
username = raw_input('Username')
password = getpass('Password')

q = {'auth_token':auth_token,'username':username,'password':password,'remember':'0'}
r = requests.get('http://api.series.ly/v2/user/user_token',params=q)

print r.text