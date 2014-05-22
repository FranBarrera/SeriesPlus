	%if data_raw['error']<1:
		<div class="col-md-2 poster">
			<img src="{{data_raw['poster']['large']}}">
		</div>
		<div class="col-md-10">
			<h1 class="title">{{data_raw['name']}}</h1>
			<h3>Nota: {{data_raw['rating']}} - Año: {{data_raw['year']}}</h3>
			<h3>Sinopsis:</h3>
			<p class="detail">{{data_raw['plot']}}</p>
		</div>
	%end