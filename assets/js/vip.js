var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

$( document ).ready(function() {


	// SHRINK NAV
	$('body').waypoint(function(direction) {
		if(direction == "down")
  			$(".desktop .nav-wrap").stop().animate({paddingTop:"15px", paddingBottom: "10px"},200);
  		else
  			$(".desktop .nav-wrap").stop().animate({paddingTop:"30px", paddingBottom: "30px"},200);
	}, { offset: -300 });

	// EXPAND SEARCH
	var active = Boolean(false);
	var timeout;

	function activateSearch() {
		if (!active) {
			$(".nav .search input[type='text']").animate({width:'167px'});
			active = Boolean(true);
		}
	};
	function suppressSearch() {
		if (active) {
			if(!$(".nav .search input[type='text']").is( ":focus" )){
				clearInterval(timeout);
				$(".nav .search input[type='text']").stop().animate({width:'14px'});
				active = Boolean(false);
			}
		}
	};
	$(".nav .search input[type='text']").hover(function() {clearInterval(timeout); activateSearch(); }, function () { timeout = setInterval(suppressSearch, 2000); });


	// DETECT MOBILE
	// Optimalisation: Store the references outside the event handler:
    var $window = $(window);

    function checkWidth() {
        var windowsize = $window.width();
        if (windowsize < 480) {
        	$("body").removeClass("desktop");
      		$("body").addClass("mobile");
        }
        else{
        	$("body").removeClass("mobile");
        	$("body").addClass("desktop");
        }
    }
    // Execute on load
    checkWidth();
    // Bind event listener
    $(window).resize(checkWidth);

    // Form watermark
    if( $('.comments input[type="text"]').length != 0 ){
    	$('.comments input[type="text"]').watermark();
    }
});

}
/*
     FILE ARCHIVED ON 23:29:18 May 25, 2018 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 15:02:00 Mar 25, 2021.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  CDXLines.iter: 47.12 (3)
  esindex: 0.011
  load_resource: 116.326 (2)
  exclusion.robots: 0.147
  captures_list: 257.979
  exclusion.robots.policy: 0.137
  RedisCDXSource: 1.658
  PetaboxLoader3.datanode: 90.569 (5)
  LoadShardBlock: 181.636 (3)
  PetaboxLoader3.resolve: 53.163 (2)
*/