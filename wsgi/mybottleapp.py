import requests
import json
import os
from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH
from funciones import fuser_token
from funciones import fseriesfollowing,full_info,fbusqueda,fusermedia_all,episode,get_link

@get('/auth')
def auth_reload():
    fichero = open(os.path.join(os.path.dirname(__file__),"auth.txt"),'w')
    fclave = open(os.path.join(os.path.dirname(__file__),"clave.txt"),'r')
    clave = fclave.readline()
    q = {"id_api":'2132',"secret":clave}
    r = requests.get('http://api.series.ly/v2/auth_token',params=q)
    jtemp = json.loads(r.text)
    auth = jtemp["auth_token"]
    fichero.write(auth)
  
@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static')

@get('/series')
def le_series():
    return template('header.tpl',username=request.get_cookie("user")),template('tseries.tpl',data_raw=fusermedia_all(request.get_cookie("user_token")))

@post('/series')
def le_series():
    return template('tseries.tpl',data_raw=fusermedia_all(request.get_cookie("user_token")))

@get('/pelis')
def le_series():
    return template('header.tpl',username=request.get_cookie("user")),template('tpelis.tpl',data_raw=fusermedia_all(request.get_cookie("user_token")))

@post('/pelis')
def le_series():
    return template('tpelis.tpl',data_raw=fusermedia_all(request.get_cookie("user_token")))

@post('/busqueda')
def le_busqueda():
    v_busqueda = request.forms.get('busqueda')
    return template('header.tpl'),template('busqueda.tpl',data_raw=fbusqueda(v_busqueda)),template('footer.tpl')

@get('/ep/:idm')
def le_episode(idm):
    mediaType = 5
    return template('episode.tpl',data_raw=episode(request.get_cookie("user_token"),idm,mediaType))

@get('/go/:idv')
def le_link(idv):
    return template('golink.tpl',data_raw=get_link(request.get_cookie("user_token"),idv))  

@get('/tv/:idm')
def le_pelicula(idm):
    mediaType = 4
    return template('header.tpl'),template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl')

@post('/tv/:idm')
def le_pelicula(idm):
    mediaType = 4
    return template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl')


@get('/docus/:idm')
def le_pelicula(idm):
    mediaType = 3
    return template('header.tpl',username=request.get_cookie("user")),template('pelicula.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('episode.tpl',data_raw=episode(request.get_cookie("user_token"),idm,mediaType))

@post('/docus/:idm')
def le_pelicula(idm):
    mediaType = 3
    return template('pelicula.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('episode.tpl',data_raw=episode(request.get_cookie("user_token"),idm,mediaType))

@get('/peli/:idm')
def le_pelicula(idm):
    mediaType = 2
    return template('header.tpl'),template('pelicula.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl'),template('episode.tpl',data_raw=episode(request.get_cookie("user_token"),idm,mediaType))

@post('/peli/:idm')
def le_pelicula(idm):
    mediaType = 2
    return template('pelicula.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl'),template('episode.tpl',data_raw=episode(request.get_cookie("user_token"),idm,mediaType))

@get('/main') # or @route('/login')
def le_main():
    return template('header.tpl',username=request.get_cookie("user")),template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token"))),template('footer.tpl')

@post('/main')
def le_main():
    return template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token")))

@get('/serie/:idm')
def le_serie(idm):
    mediaType = 1
    return template('header.tpl'),template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType)),template('footer.tpl')

@post('/serie/:idm')
def le_serie(idm):
    mediaType = 1
    return template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType))


@route('/salir')
def basic_liad():
    response.set_header('Set-Cookie', 'user=')
    response.set_header('Set-Cookie', 'user_token=')
    return redirect('/')


@get('/') # or @route('/')
def login():
    if request.get_cookie("user_token"):
        return template('header.tpl',username=request.get_cookie("user")),template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token")))
    else:
        return template('login.tpl')


@post('/') # or @route('/', method='POST')
def do_login():
    if request.get_cookie("user_token"):
        return template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token")))
    else:
        username = request.forms.get('username')
        password = request.forms.get('password')
        user_token = fuser_token(username,password)
        if len(user_token) > 0:
            response.set_header('Set-Cookie', 'user='+username)
            response.set_header('Set-Cookie', 'user_token='+user_token)
            response.set_header('Set-Cookie', 'user='+username)
            response.set_header('Set-Cookie', 'user_token='+user_token)
            return redirect('/main')
        else:
            return "<p>Login Incorrecto.<a href=\"/\">Intentar de nuevo </a</p>"



ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
                                      'app-root/repo/wsgi/views/'))
    
    application=default_app()
else:
    run(host='localhost', port=8080)



