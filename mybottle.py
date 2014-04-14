from bottle import route, run, template, get, post, request, response, redirect
from user_token import fuser_token
from user_token import fseriesfollowing


@get('/main') # or @route('/login')
def le_main():
    return template('template.tpl',data_raw=fseriesfollowing(request.get_cookie("user_token")))

@get('/serie/:idm')
def le_serie(idm):
    return template('serie.tpl',data_raw=full_info(request.get_cookie("user_token"),idm,mediaType))
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
    user_token = fuser_token(username,password)
    if len(user_token) > 0:
        response.set_header('Set-Cookie', 'user='+username)
        response.set_header('Set-Cookie', 'user_token='+user_token)
        return redirect('/main')
    else:
        return "<p>Login failed.</p>"
run(host='localhost', port=8080)



