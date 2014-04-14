import requests
import json

fichero = open('auth.txt','r')
auth_token = fichero.readline()

def fuser_token(username, password):
	q = {'auth_token':auth_token,'username':username,'password':password,'remember':'1'}
	r = requests.get('http://api.series.ly/v2/user/user_token',params=q)
	if r.text == '{"errorMessage":"User not found.","error":31}':
		return ''
	else:
		jresp = json.loads(r.text)
		token = jresp['user_token']
		return token


def fseriesfollowing(user_token):
 	q_sf = {'auth_token':auth_token,'user_token':user_token}
 	r_sf = requests.get('http://api.series.ly/v2/user/media/series',params=q_sf)
 	jresp = json.loads(r_sf.text)
 	return jresp

 #seriesfollow = fseriesfollowing()
 #nombres = []
 #for i in seriesfollow['series']:
# 	nombres.append(i['name'])

# def fseriesmostseen():
# 	q = {'auth_token':auth_token}
# 	r = requests.get('http://api.series.ly/v2/media/most_seen',params=q)
# 	jresp = json.loads(r.text)
# 	return jresp

# seriesmost = fseriesmostseen()
# nombres_mostseen = []
# for i in seriesmost['series']:
# 	nombres_mostseen.append(i['name'])



#@route('/template')
#def test():
#	return template('template.tpl',nombres=nombres,nombres_mostseen=nombres_mostseen)




fichero.close()

