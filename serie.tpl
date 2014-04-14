<html>
	<head>
	</head>
	<body>
		%if data_raw['error']<1:
			<h1> {{data_raw['name']}} </h1>
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
	</body>
</html>