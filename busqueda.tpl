<html>
	<head>
	</head>
	<body>
		%lista = [1,2,3,4]
		%for i in data_raw['response']['results']:
			 %if i['type'] <= 4:
			 	<h1>{{i['object']['name']}}</h1>
				<p>Nota: {{i['object']['rating']}}</p>
				<p>Año: {{i['object']['year']}}</p>
				<p>{{i['object']['plot']}}</p>
				<img src="{{i['object']['img']}}"/>

			 %end
		%end
	</body>
</html>
