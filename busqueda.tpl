<html>
	<head>
	</head>
	<body>
		%lista = [1,2,3,4]
		%for i in data_raw['response']['results']:
			 %if i['type'] <= 4:
			 	<p>{{i['object']['name']}}</p>
			 %end
		%end
	</body>
</html>
