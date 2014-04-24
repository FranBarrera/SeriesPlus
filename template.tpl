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
						%tipo = ''
						%for media in data_raw[data]:
						%if media['mediaType'] == 1:
							%tipo = 'serie'
						%elif media['mediaType'] == 2:
							%tipo = 'peliculas'
						%elif media['mediaType'] == 3:
							%tipo = 'docus'
						%elif media['mediaType'] == 4:
							%tipo = 'tv'
						%end
							<li><a href="{{tipo}}/{{media['idm']}}">{{media['name']}}</a></li>
						%end
					</ul>
				%end
		%end

	</body>
</html>


