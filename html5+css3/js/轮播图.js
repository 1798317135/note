		var i=0;
		var t;
		$(function() {
			$('menu>li').mouseenter(function(event) {
				$(this).addClass('l1').siblings().removeClass('l1');
				i=$(this).index()
				$('ul li').eq(i).stop(true).fadeIn(500).siblings().fadeOut(500);
			});
			$('span.right').on('click',active);
			 $(window).one('load',out_fun);
			$('img').hover(in_fun,out_fun);
			function active(){
				if (i==3) {
					i=-1;
				}
				$('menu>li').eq(i+1).trigger('mouseenter');
				//
			}
			function out_fun(){
				t = setInterval(active,5000);
			}
			function in_fun(){
				clearInterval(t);
			}
			$('span.left').click(function(event) {
				$('menu>li').eq(i-1).trigger('mouseenter');
			});
		});