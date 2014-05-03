<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="shortcut icon" href="">
        <title>SeriesPlus - Login</title>

        <!-- Bootstrap core CSS -->
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css" rel="stylesheet">
        <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css" rel="stylesheet">
		<script src="//use.edgefonts.net/lato:n1,i1,n3,i3,n4,i4,n7,i7,n9,i9.js"></script>
            <style>
/* line 14, ../sass/login.scss */
body {
  font-family: lato;
  font-weight: 300;
  background: #16a085;
  color: white;
  -webkit-font-smoothing: antialiased;
  -moz-font-smoothing: antialiased;
  -o-font-smoothing: antialiased;
  -ms-font-smoothing: antialiased;
  font-smoothing: antialiased;
}
/* line 24, ../sass/login.scss */
body .header {
  margin: 60px 0 10px;
  text-align: center;
  font-size: 40px;
  font-weight: 300;
}
/* line 30, ../sass/login.scss */
body form {
  text-align: left;
  padding: 30px;
  background: rgba(255, 255, 255, 0.2);
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  border-radius: 5px;
  text-align: center;
}
/* line 36, ../sass/login.scss */
body form span {
  display: block;
  color: white;
  font-size: 20px;
  margin-bottom: 10px;
  text-align: left;
  font-weight: 400;
}
/* line 45, ../sass/login.scss */
body form input[type=submit] {
  margin-top: 15px;
  border: none;
  box-shadow: none;
  background: white;
  color: #1abc9c;
  text-shadow: none;
  outline: none;
}
/* line 53, ../sass/login.scss */
body form input[type=submit]:hover, body form input[type=submit]:active {
  background: #16a085;
  color: white;
}
/* line 59, ../sass/login.scss */
body form input[type=text], body form input[type=password] {
  width: 100%;
  margin-bottom: 10px;
  border: none;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  -ms-border-radius: 5px;
  border-radius: 5px;
  padding: 5px 10px;
  outline: none;
  color: grey;
  font-weight: 300;
}


            </style>


     </head>

    <body>
        <div class="col-md-12 header">SeriesPlus</div>
        <div class="row">
          <div class="col-md-4 col-md-offset-4">
                <form action="/" method="post">
                    <div><span>Username:</span><input name="username" placeholder="Usuario" type="text" /></div>
                    <div><span>Password:</span><input name="password" placeholder="Contraseña" type="password" /></div>
                    <input value="Iniciar sesión" class="btn btn-success" type="submit" />
                </form>
            </div>
    </body>
</html>