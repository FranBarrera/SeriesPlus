import requests
import json
from lxml import etree
import webbrowser

fichero = open('auth.txt','r')
respuesta = open('most_seen.txt','w')
auth_token = fichero.readline()
q = {'auth_token':auth_token}
r = requests.get('http://api.series.ly/v2/media/most_seen',params=q)
jresp = json.loads(r.text)

#print jresp['series'][0]
#respuesta.write(json.dumps(jresp['series'][0]))

for i in jresp['series']:
	print i['name']
