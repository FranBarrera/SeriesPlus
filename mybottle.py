import requests
import json
from bottle import route, default_app, run, template, get, post, request, response, redirect
from user_token import fuser_token
from user_token import fseriesfollowing,full_info,fbusqueda

# @get('/auth')
# def auth_reload():
#     fichero = open('auth.txt','w')
#     q = {"id_api":'',"secret":''}
#     r = requests.get('http://api.series.ly/v2/auth_token',params=q)
#     jtemp = json.loads(r.text)
#     auth = jtemp["auth_token"]
#     fichero.write(auth)


@post('/busqueda')
def le_busqueda():
    v_busqueda = request.forms.get('busqueda')
    return template('busqueda.tpl',data_raw=fbusqueda(v_busqueda))

@get('/tv/:idm')
def le_pelicula(idm):
    mediaType = 4
    return template('tv.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType))

@get('/docus/:idm')
def le_pelicula(idm):
    mediaType = 3
    return template('docus.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType))

@get('/peliculas/:idm')
def le_pelicula(idm):
    mediaType = 2
    return template('pelicula.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType))  

@get('/main') # or @route('/login')
def le_main():
    return template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token")))

@get('/serie/:idm')
def le_serie(idm):
    mediaType = 1
    return template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType))

@get('/') # or @route('/')
def login():
    return '''
        <form action="/" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

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
# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
                                      'app-root/repo/wsgi/views/'))
    
    application=default_app()
else:
    run(host='localhost', port=8080, debug=True)



