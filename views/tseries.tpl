%for data in data_raw:
	%if data!= 'error':
		%if len(data_raw[data]) > 0:
			%tipo = ''
			%tipo2 =''
			%for media in data_raw[data]:
				%if media['mediaType'] == 1:
					%tipo = 'serie'
					%tipo2 = 'Series'
				%elif media['mediaType'] == 4:
					%tipo = 'tv'
					%tipo2 = 'TVShows'
				%end
			%end
			<h1> {{tipo2}} </h1>
				<div class="col-md-12 show_caratulas">
				%for media in data_raw[data]:
					%if media['mediaType']==1 or media['mediaType']==4:
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