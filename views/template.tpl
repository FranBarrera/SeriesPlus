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
				<div class="col-md-12 show_caratulas">
				%for media in data_raw[data]:
					<a href="/{{tipo}}/{{media['idm']}}" class="col-md-2">
						<div class="caratula">
							<span class="leyenda">
								<div class="info">{{media['name']}}<br>{{media['year']}}</div>
							</span>
							<img src="{{media['img']}}"/>
						</div>
					</a>
				%end
			</ul>
		%end
	%end
%end


