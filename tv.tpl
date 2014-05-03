%if data_raw['error']<1:
	<h1>{{data_raw['name']}}</h1>
	<h3>Nota: {{data_raw['rating']}}</h3>
	<h3>Año: {{data_raw['year']}}</h3>
	<p>{{data_raw['plot']}}</p>
%end
