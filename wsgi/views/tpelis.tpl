%for data in data_raw:
	%if data!= 'error':
		%if len(data_raw[data]) > 0:
			%tipo = ''
			%tipo2 =''
			%for media in data_raw[data]:
				%if media['mediaType'] == 2:
					%tipo = 'peli'
					%tipo2 = 'Películas'
				%elif media['mediaType'] == 3:
					%tipo = 'doc'
					%tipo2 = 'Documentales'
				%end
			%end
			%if tipo2:
				<h1> {{tipo2}} </h1>
				<div class="col-md-12 show_caratulas">
				%for media in data_raw[data]:
					%if media['mediaType']==2 or media['mediaType']==3:
						<a href="/{{tipo}}/{{media['idm']}}" class="col-md-2">
							<div class="caratula">
								<span class="leyenda">
									<div class="info">{{media['name']}}<br>{{media['year']}}</div>
								</span>
								<img src="{{media['img']}}"/>
							</div>
						</a>
					%end
				%end
				</div>
			%end
		%end
	%end
%end