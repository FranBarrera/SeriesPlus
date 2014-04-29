<html>

	<head>
	</head>
	<body>
		
		<h1> Mi SeriesPlus </h1>
		%for data in data_raw:
			%if data!= 'error':
				%if len(data_raw[data]) > 0:
					%tipo = ''
					%tipo2 =''
					%for media in data_raw[data]:
						%if media['mediaType'] == 1:
							%tipo = 'serie'
							%tipo2 = 'Series'
						%elif media['mediaType'] == 2:
							%tipo = 'peliculas'
							%tipo2 = 'Peliculas pendientes'
						%elif media['mediaType'] == 3:
							%tipo = 'docus'
							%tipo2 = 'Documentales'
						%elif media['mediaType'] == 4:
							%tipo = 'tv'
							%tipo2 = 'Programas de televisión'
						%end
					%end
					<h2> {{tipo2}} </h2>
					<ul>
						%for media in data_raw[data]:
							<td><a href="{{tipo}}/{{media['idm']}}"><img src="{{media['img']}}"/></a></td>
						%end
					</ul>
				%end
			%end
		%end

	</body>
</html>


