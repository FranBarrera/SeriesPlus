<html>
	<head>
	</head>
	<body>
		<h1> {{data_raw['name']}} </h1>
		%for i in range(1,data_raw['seasons']):
			%if i < 10:
				%season_number = '0'+str(i)
			%else:
				%season_number = str(i)
		%end
			%season_variable = 'season_'+season_number
			<h3>Temporada {{i}}</h3>
	</body>
</html>