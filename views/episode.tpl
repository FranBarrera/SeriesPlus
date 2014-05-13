%if data_raw['data']['error']<1:
	%if data_raw['online']:
		<h1 class="title">Ver online</h1>
		<ul class="table">
		%for server in data_raw['data']['streaming']:

			<li><a class="open_link" target="_blank" href="/go/{{server['idv']}}">
				{{server['host']}}  <span class="{{server['quality']}}">{{server['quality']}}</span></a></li>

		%end
		</ul>
	%end
	%if data_raw['direct']:
		<h1 class="title">Descargar</h1>
		<ul class="table">
		%for server in data_raw['data']['direct_download']:
			<li><a class="open_link" target="_blank" href="/go/{{server['idv']}}">
				{{server['host']}}  <span class="{{server['quality']}}">{{server['quality']}}</span></a></li>
		%end
		</ul>
	%end
%else:
	<h1>ERROR</h1>
%end
