<html>

	<head>
	</head>
	<body>
		<h1> Series Following </h1>
		%for nombre in nombres:
		<ul>
			<li> {{nombre}} </li>
		</ul>
		%end
		<h1> Series mas vistas </h1>
		%for mostnombre in nombres_mostseen:
		<ul>
			<li> {{mostnombre}} </li>
		</ul>
		%end
	</body>

</html>