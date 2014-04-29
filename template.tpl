<html>

	<head>
	</head>
	<body>
		
		<h1> Siguiendo </h1>
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
							<td><a href="{{tipo}}/{{media['idm']}}"><img src="{{media['img']}}"/></a></td>
						%end
					</ul>
				%end
		%end

	</body>
</html>


