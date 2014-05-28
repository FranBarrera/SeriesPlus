# -*- coding: utf-8 -*-
import requests
import json
import os
from collections import OrderedDict

fichero = open(os.path.join(os.path.dirname(__file__),"auth.txt"),'r')
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

def get_link(user_token,idv):
	r_sf = ('http://api.series.ly/v2/media/link/go/'+idv+'/?auth_token='+auth_token+'&user_token='+user_token)
	return r_sf

def fseriesfollowing(user_token):
 	q_sf = {'auth_token':auth_token,'user_token':user_token}
 	r_sf = requests.get('http://api.series.ly/v2/user/media/pending',params=q_sf)
 	jresp = json.loads(r_sf.text,object_pairs_hook=OrderedDict)
 	return jresp

def full_info(user_token,idm,mediaType):
	q_sf = {'auth_token':auth_token,'user_token':user_token,'idm':idm,'mediaType':mediaType}
	r_sf = requests.get('http://api.series.ly/v2/media/full_info',params=q_sf)
	jresp = json.loads(r_sf.text,object_pairs_hook=OrderedDict)
	return jresp

def episode(user_token,idm,mediaType):
	q_sf = {'auth_token':auth_token,'user_token':user_token,'idm':idm,'mediaType':mediaType}
	r_sf = requests.get('http://api.series.ly/v2/media/episode/links',params=q_sf)
	jresp = json.loads(r_sf.text, object_pairs_hook=OrderedDict)
	try:
		direct = len(jresp['direct_download'])
	except KeyError:
		direct = 0
	try:
		online = len(jresp['streaming'])
	except KeyError:
		online = 0
		
	servers = {'online':online, 'direct':direct,'data':jresp}
	
	return servers

def fbusqueda(v_busqueda):
	q_sf = {'auth_token':auth_token,'q':v_busqueda}
	r_sf = requests.get('http://api.series.ly/v2/search',params=q_sf)
	jresp = json.loads(r_sf.text)
	print jresp
	return jresp

def fusermedia_all(user_token):
	q_sf = {'auth_token':auth_token,'user_token':user_token}
 	r_sf = requests.get('http://api.series.ly/v2/user/media/',params=q_sf)
 	jresp = json.loads(r_sf.text, object_pairs_hook=OrderedDict)
 	return jresp

def fmostseen():
	q_sf = {'auth_token':auth_token}
 	r_sf = requests.get('http://api.series.ly/v2/media/most_seen/',params=q_sf)
 	jresp = json.loads(r_sf.text, object_pairs_hook=OrderedDict)
 	return jresp

fichero.close()

