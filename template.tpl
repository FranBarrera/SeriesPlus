<html>

	<head>
	</head>
	<body>
		<h1> Series Following </h1>
		%for data in data_raw:
			%if data!= 'error':
				%if len(data_raw[data]) > 0:
					<h2> {{data}} </h2>
					<ul>
						%for media in data_raw[data]:
							<li><a href="serie/{{media['idm']}}">{{media['name']}}</a></li>
						%end
					</ul>
				%end
		%end
	</body>
</html>