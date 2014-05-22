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
					%tipo = 'peli'
					%tipo2 = 'Peliculas pendientes'
				%elif media['mediaType'] == 3:
					%tipo = 'docus'
					%tipo2 = 'Documentales'
				%elif media['mediaType'] == 4:
					%tipo = 'tv'
					%tipo2 = 'Programas de televisión'
				%end
			%end
			<h1> {{tipo2}} </h1>
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
				</div>
		%end
	%end
%end
<script>
	$(document).on('ready', function(){
		$('title').html('SeriesPlus - Inicio');
		$('.m_main').addClass('active');
	});
</script>
