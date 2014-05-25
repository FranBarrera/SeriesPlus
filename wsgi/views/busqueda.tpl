
<h1>Resultados de la búsqueda:</h1>
<div class="col-md-12 show_caratulas">
	%lista = [1,2,3,4]
	%for media in data_raw['response']['results']:
		%if media['type'] <= 4:
			%if media['type'] == 1:
				%tipo = 'serie'
			%elif media['type'] == 2:
				%tipo = 'peli'
			%elif media['type'] == 3:
				%tipo = 'doc'
			%elif media['type'] == 4:
				%tipo = 'tv'
			%end
			<div class="col-md-2">
				<a href="/{{tipo}}/{{media['object']['idm']}}">
					<div class="caratula">
						<div class="leyenda">
							<div class="rate">
								<div class="rate_star"></div>
								<div class="rate_real">{{media['object']['rating']}}</div>
							</div>
							<div class="info">{{media['object']['name']}}<br>{{media['object']['year']}}</div>
						</div>
						<img width="175" height="260" src="{{media['object']['img']}}"/>
					</div>
				</a>
			</div>
		%end
	%end
</div>