%if data_raw['error']<1:
	%for i in data_raw['response']['results']:
		%if i['type'] <= 4:
			<div class="col-md-2 poster">
				<img src="{{i['object']['img']}}">
			</div>
		 <div class="col-md-10">
	 		<h1 class="title">{{i['object']['name']}}</h1>
	 		<h3>Nota: {{i['object']['rating']}} - Año: {{i['object']['year']}}</h3>
	 		<h3>Sinopsis:</h3>
	 		<p class="detail">{{i['object']['plot']}}</p>
	 	</div>
	 	%end
	%end
%end
