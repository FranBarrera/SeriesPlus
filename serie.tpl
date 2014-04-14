<html>
	<head>
	</head>
	<body>
		<h1> {{data_raw['name']}} </h1>
		%for i in data_raw['seasons_episodes']:
			<h3>{{i}}</h3>
	</body>
</html>