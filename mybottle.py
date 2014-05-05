import requests
import json
from bottle import route, run, template, get, post, request, response, redirect
from user_token import fuser_token
from user_token import fseriesfollowing,full_info,fbusqueda

@get('/auth')
def auth_reload():
    fichero = open('auth.txt','w')
    fclave = open('clave.txt','r')
    clave = fclave.readline()
    q = {"id_api":'2132',"secret":clave}
    r = requests.get('http://api.series.ly/v2/auth_token',params=q)
    jtemp = json.loads(r.text)
    auth = jtemp["auth_token"]
    fichero.write(auth)

@post('/busqueda')
def le_busqueda():
    v_busqueda = request.forms.get('busqueda')
    return template('header.tpl'),template('busqueda.tpl',data_raw=fbusqueda(v_busqueda)),template('footer.tpl')

@get('/tv/:idm')
def le_pelicula(idm):
    mediaType = 4
    return template('header.tpl'),template('tv.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl')

@get('/docus/:idm')
def le_pelicula(idm):
    mediaType = 3
    return template('header.tpl'),template('docus.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl')

@get('/peliculas/:idm')
def le_pelicula(idm):
    mediaType = 2
    return template('header.tpl'),template('pelicula.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl') 

@get('/main') # or @route('/login')
def le_main():
    return template('header.tpl'),template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token"))),template('footer.tpl')

@get('/serie/:idm')
def le_serie(idm):
    mediaType = 1
    return template('header.tpl'),template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl')

@get('/') # or @route('/')
def login():
    return template('login.tpl')

@post('/') # or @route('/', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    user_token = fuser_token(username,password)
    if len(user_token) > 0:
        response.set_header('Set-Cookie', 'user='+username)
        response.set_header('Set-Cookie', 'user_token='+user_token)
        return redirect('/main')
    else:
        return "<p>Login Incorrecto.<a href=\"/\">Intentar de nuevo </a</p>"

run(host='localhost', port=8080)

# This must be added in order to do correct path lookups for the views
# import os
# from bottle import TEMPLATE_PATH

# ON_OPENSHIFT = False
# if os.environ.has_key('OPENSHIFT_REPO_DIR'):
#     ON_OPENSHIFT = True

# if ON_OPENSHIFT:
#     TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
#                                       'app-root/repo/wsgi/views/'))
    
#     application=default_app()
# else:
#   run(host='localhost', port=8080, debug=True)



