%if data_raw['error']<1:
	<h1>{{data_raw['name']}}</h1>
	<h3>Nota: {{data_raw['rating']}}</h3>
	<h3>Año: {{data_raw['year']}}</h3>
	<p>{{data_raw['plot']}}</p>
	%tmp_num = 1
	%for seasons in data_raw['seasons_episodes']:
		%if seasons!='season_00':
			<h1>Temporada {{tmp_num}}</h1>
			<ul>
			%for episodes in data_raw['seasons_episodes'][seasons]:
				<li>{{episodes['episode']}} - {{episodes['name']}}</li>
			%end
			</ul>
			%tmp_num = tmp_num+1
		%end
	%end
%else:
	<h1>ERROR</h1>
%end