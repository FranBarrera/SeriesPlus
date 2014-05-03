%if data_raw['error']<1:
	<h1> {{data_raw['name']}} </h1>
	<h3> Nota: {{data_raw['rating']}} </h3>
	<h3> Año: {{data_raw['year']}} </h3>
	<p> {{data_raw['plot']}}</p>
	%for i in range(1,data_raw['seasons']):
		%if i < 10:
			%season_number = '0'+str(i)
		%else:
			%season_number = str(i)
		%end
		%season_variable = 'season_'+season_number
		%if data_raw['seasons_episodes'][season_variable]:
			<h3>Temporada {{i}}</h3>
			<ul>
			%for episodes in data_raw['seasons_episodes'][season_variable]:
				<li>{{episodes['name']}}</li>
			%end
			</ul>
		%end
	%end
%else:
	<h1>ERROR</h1>
%end
