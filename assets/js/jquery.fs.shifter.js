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

/* 
 * Shifter v3.0.3 - 2014-02-19 
 * A jQuery plugin for simple slide-out mobile navigation. Part of the Formstone Library. 
 * http://formstone.it/shifter/ 
 * 
 * Copyright 2014 Ben Plum; MIT Licensed 
 */ 

;(function ($, window) {
	"use strict";

	var initialized = false,
		data = {};

	/**
	 * @options
	 * @param maxWidth [string] <'980px'> "Width at which to auto-disable plugin"
	 */
	var options = {
		maxWidth: "980px"
	};

	var pub = {

		/**
		 * @method
		 * @name close
		 * @description Closes navigation if open
		 * @example $.shifter("close");
		 */
		close: function() {
			if (initialized) {
				data.$body.removeClass("shifter-open");
				data.$page.off(".shifter");
				// Close mobile keyboard if open
				data.$nav.find("input").trigger("blur");
			}
		},

		/**
		 * @method
		 * @name enable
		 * @description Enables navigation system
		 * @example $.shifter("enable");
		 */
		enable: function() {
			if (initialized) {
				data.$body.addClass("shifter-active");
			}
		},

		/**
		 * @method
		 * @name defaults
		 * @description Sets default plugin options
		 * @param opts [object] <{}> "Options object"
		 * @example $.shifter("defaults", opts);
		 */
		defaults: function(opts) {
			options = $.extend(options, opts || {});
		},

		/**
		 * @method
		 * @name destroy
		 * @description Removes instance of plugin
		 * @example $.shifter("destroy");
		 */
		destroy: function() {
			if (initialized) {
				data.$body.removeClass("shifter shifter-active shifter-open")
					      .off("touchstart.shifter click.shifter");

				// Navtive MQ Support
				if (window.matchMedia !== undefined) {
					data.mediaQuery.removeListener(_onRespond);
				}

				data = {};
			}
		},

		/**
		 * @method
		 * @name disable
		 * @description Disables navigation system
		 * @example $.shifter("disable");
		 */
		disable: function() {
			if (initialized) {
				data.$body.removeClass("shifter-active");
			}
		},

		/**
		 * @method
		 * @name open
		 * @description Opens navigation if closed
		 * @example $.shifter("open");
		 */
		open: function() {
			if (initialized) {
				data.$body.addClass("shifter-open");
				data.$page.one("touchstart.shifter click.shifter", _onClick);
			}
		}
	};

	/**
	 * @method private
	 * @name _init
	 * @description Initializes plugin
	 * @param opts [object] "Initialization options"
	 */
	function _init(opts) {
		// Local options
		options = $.extend(options, opts || {});

		data.$body = $("body");
		data.$page = $(".shifter-page");
		data.$nav  = $(".shifter-navigation");

		if (data.$page.length > 0 && data.$nav.length > 0) {
			initialized = true;

			data.$body.addClass("shifter")
					  .on("touchstart.shifter click.shifter", ".shifter-handle", _onClick);

			// Navtive MQ Support
			if (window.matchMedia !== undefined) {
				data.mediaQuery = window.matchMedia("(max-width:" + (options.maxWidth === Infinity ? "100000px" : options.maxWidth) + ")");
				data.mediaQuery.addListener(_onRespond);
				_onRespond();
			}
		}
	}

	/**
	 * @method private
	 * @name _onRespond
	 * @description Handles media query match change
	 */
	function _onRespond() {
		if (data.mediaQuery.matches) {
			pub.enable();
		} else {
			pub.disable();
		}
	}

	/**
	 * @method private
	 * @name _onClick
	 * @description Determines proper click / touch action
	 * @param e [object] "Event data"
	 */
	function _onClick(e) {
		e.preventDefault();
		e.stopPropagation();

		if (data.$body.hasClass("shifter-open")) {
			pub.close();
		} else {
			pub.open();
		}
	}

	$.shifter = function(method) {
		if (pub[method]) {
			return pub[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return _init.apply(this, arguments);
		}
		return this;
	};
})(jQuery, window);

}
/*
     FILE ARCHIVED ON 23:29:20 May 25, 2018 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 15:02:00 Mar 25, 2021.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 122.895
  exclusion.robots: 0.088
  exclusion.robots.policy: 0.08
  RedisCDXSource: 1.001
  esindex: 0.008
  LoadShardBlock: 75.59 (3)
  PetaboxLoader3.datanode: 103.559 (5)
  CDXLines.iter: 26.564 (3)
  load_resource: 250.026 (2)
  PetaboxLoader3.resolve: 214.545 (2)
*/