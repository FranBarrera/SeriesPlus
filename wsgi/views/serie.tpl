%if data_raw['error']<1:
	<div class="col-md-2 poster">
		<img src="{{data_raw['poster']['large']}}">
	</div>
	<div class="col-md-10">
		<h1 class="title">{{data_raw['name']}}</h1>
		<h3>Nota: {{data_raw['rating']}} - Año: {{data_raw['year']}}</h3>
		<h3>Sinopsis:</h3>
		<p class="detail">{{data_raw['plot']}}</p>
		<hr>
		%tmp_num = 1
		%for seasons in data_raw['seasons_episodes']:
			%if seasons!='season_00':
				<h1 class="title">Temporada {{tmp_num}}</h1>
				<ul class="table">
				%for episodes in data_raw['seasons_episodes'][seasons]:
					<li><a class="open_bar" href="/ep/{{episodes['idm']}}">
						
						{{episodes['episode']}} - {{episodes['name']}}</a></li>
				%end
				</ul>
				%tmp_num = tmp_num+1
			%end
		%end
	</div>
%else:
	<h1>ERROR</h1>
%end
<div class="episode_bar"></div>
<div class="fadeweb"></div>
<script>
	
		$('title').html('SeriesPlus - {{data_raw['name']}}');
		$('.m_serie').addClass('active');
		
		$('.open_bar').on('click', function(e){
			e.preventDefault();
			$('body').css('overflow', 'hidden');
			$('.episode_bar').css('overflow', 'auto').scrollTop(0);
			$('.fadeweb').fadeIn();
			$.get($(this).attr('href'),function(data){
				$('.episode_bar').html(data).css('right',0);
			});
		});
		
        $('nav a').on('click', function(e){
            $('.fadeweb').fadeOut();
            $('.episode_bar').css('right','');
            $('body').css('overflow', '');
        });

        $('.fadeweb').on('click', function(e){
			$(this).fadeOut();
			$('.episode_bar').css('right','');
			$('body').css('overflow', '');
		});
		
</script>