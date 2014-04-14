<html>

	<head>
	</head>
	<body>
		<h1> Series Following </h1>
		%for data in data_raw:
			%if data!= 'error':
		<h2> {{data}} </h2>
		<ul>
			%for media in data_raw[data]:
			<li>{{media['name']}}</li>
		</ul>
		%end
			%end
	</body>

</html>