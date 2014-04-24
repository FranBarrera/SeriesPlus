# -*- coding: utf-8 -*-
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
 	r_sf = requests.get('http://api.series.ly/v2/user/media/pending',params=q_sf)
 	jresp = json.loads(r_sf.text)
 	return jresp

def full_info(user_token,idm,mediaType):
	q_sf = {'auth_token':auth_token,'user_token':user_token,'idm':idm,'mediaType':mediaType}
	r_sf = requests.get('http://api.series.ly/v2/media/full_info',params=q_sf)
	jresp = json.loads(r_sf.text)
	return jresp

def fbusqueda(v_busqueda):
	q_sf = {'auth_token':auth_token,'q':v_busqueda}
	r_sf = requests.get('http://api.series.ly/v2/search',params=q_sf)
	jresp = json.loads(r_sf.text)
	print jresp
	return jresp

fichero.close()

