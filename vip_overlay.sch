<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        queryBinding="xslt2"
        defaultPhase="strict">

  <title>VIP 7.0 Core Schematron Validation Specification</title>

  <ns prefix="xs" uri="http://www.w3.org/2001/XMLSchema"/>
  <ns prefix="xsi" uri="http://www.w3.org/2001/XMLSchema-instance"/>

  <!-- Populated at build time from iana_timezones.xml by the Schematron XSLTs -->
  <let name="ianaCanonicalZones"
        value="('Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Ciudad_Juarez', 'America/Costa_Rica', 'America/Coyhaique', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Fort_Nelson', 'America/Fortaleza', 'America/Glace_Bay', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Chita', 'Asia/Colombo', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kathmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Riyadh', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ulaanbaatar', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faroe', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/Perth', 'Australia/Sydney', 'Etc/GMT', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/UTC', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kirov', 'Europe/Kyiv', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Ulyanovsk', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zurich', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Kanton', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Wake', 'Pacific/Wallis')"/>
  <let name="ianaAliasZones"
        value="('Africa/Asmera', 'Africa/Timbuktu', 'America/Argentina/ComodRivadavia', 'America/Atka', 'America/Buenos_Aires', 'America/Catamarca', 'America/Coral_Harbour', 'America/Cordoba', 'America/Ensenada', 'America/Fort_Wayne', 'America/Godthab', 'America/Indianapolis', 'America/Jujuy', 'America/Knox_IN', 'America/Louisville', 'America/Mendoza', 'America/Montreal', 'America/Nipigon', 'America/Pangnirtung', 'America/Porto_Acre', 'America/Rainy_River', 'America/Rosario', 'America/Santa_Isabel', 'America/Shiprock', 'America/Thunder_Bay', 'America/Virgin', 'America/Yellowknife', 'Antarctica/South_Pole', 'Asia/Ashkhabad', 'Asia/Calcutta', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Dacca', 'Asia/Harbin', 'Asia/Istanbul', 'Asia/Kashgar', 'Asia/Katmandu', 'Asia/Macao', 'Asia/Rangoon', 'Asia/Saigon', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Ujung_Pandang', 'Asia/Ulan_Bator', 'Atlantic/Faeroe', 'Atlantic/Jan_Mayen', 'Australia/ACT', 'Australia/Canberra', 'Australia/Currie', 'Australia/LHI', 'Australia/NSW', 'Australia/North', 'Australia/Queensland', 'Australia/South', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Etc/GMT+0', 'Etc/GMT-0', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/Universal', 'Etc/Zulu', 'Europe/Belfast', 'Europe/Kiev', 'Europe/Nicosia', 'Europe/Tiraspol', 'Europe/Uzhgorod', 'Europe/Zaporozhye', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'Pacific/Enderbury', 'Pacific/Johnston', 'Pacific/Ponape', 'Pacific/Samoa', 'Pacific/Truk', 'Pacific/Yap', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Samoa')"/>
  <let name="ianaAliasTargets"
        value="('Africa/Asmara', 'Africa/Bamako', 'America/Argentina/Catamarca', 'America/Adak', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Atikokan', 'America/Argentina/Cordoba', 'America/Tijuana', 'America/Indiana/Indianapolis', 'America/Nuuk', 'America/Indiana/Indianapolis', 'America/Argentina/Jujuy', 'America/Indiana/Knox', 'America/Kentucky/Louisville', 'America/Argentina/Mendoza', 'America/Toronto', 'America/Toronto', 'America/Iqaluit', 'America/Rio_Branco', 'America/Winnipeg', 'America/Argentina/Cordoba', 'America/Tijuana', 'America/Denver', 'America/Toronto', 'America/St_Thomas', 'America/Edmonton', 'Antarctica/McMurdo', 'Asia/Ashgabat', 'Asia/Kolkata', 'Asia/Ulaanbaatar', 'Asia/Shanghai', 'Asia/Shanghai', 'Asia/Dhaka', 'Asia/Shanghai', 'Europe/Istanbul', 'Asia/Urumqi', 'Asia/Kathmandu', 'Asia/Macau', 'Asia/Yangon', 'Asia/Ho_Chi_Minh', 'Asia/Jerusalem', 'Asia/Thimphu', 'Asia/Makassar', 'Asia/Ulaanbaatar', 'Atlantic/Faroe', 'Europe/Oslo', 'Australia/Sydney', 'Australia/Sydney', 'Australia/Hobart', 'Australia/Lord_Howe', 'Australia/Sydney', 'Australia/Darwin', 'Australia/Brisbane', 'Australia/Adelaide', 'Australia/Hobart', 'Australia/Melbourne', 'Australia/Perth', 'Australia/Broken_Hill', 'America/Rio_Branco', 'America/Noronha', 'America/Sao_Paulo', 'America/Manaus', 'America/Halifax', 'America/Winnipeg', 'America/Toronto', 'America/Edmonton', 'America/St_Johns', 'America/Vancouver', 'America/Regina', 'America/Whitehorse', 'America/Santiago', 'Pacific/Easter', 'Etc/GMT', 'Etc/GMT', 'Etc/GMT', 'Etc/GMT', 'Etc/UTC', 'Etc/UTC', 'Etc/UTC', 'Europe/London', 'Europe/Kyiv', 'Asia/Nicosia', 'Europe/Chisinau', 'Europe/Kyiv', 'Europe/Kyiv', 'America/Tijuana', 'America/Mazatlan', 'America/Mexico_City', 'Pacific/Kanton', 'Pacific/Honolulu', 'Pacific/Pohnpei', 'Pacific/Pago_Pago', 'Pacific/Chuuk', 'Pacific/Chuuk', 'America/Anchorage', 'America/Adak', 'America/Phoenix', 'America/Chicago', 'America/Indiana/Indianapolis', 'America/New_York', 'Pacific/Honolulu', 'America/Indiana/Knox', 'America/Detroit', 'America/Denver', 'America/Los_Angeles', 'Pacific/Pago_Pago')"/>

  <!-- Official ISO 639-1 two-letter language codes -->
  <let name="iso639_1"
        value="('aa','ab','ae','af','ak','am','an','ar','as','av','ay','az','ba','be','bg','bi','bm','bn','bo','br','bs','ca','ce','ch','co','cr','cs','cu','cv','cy','da','de','dv','dz','ee','el','en','eo','es','et','eu','fa','ff','fi','fj','fo','fr','fy','ga','gd','gl','gn','gu','gv','ha','he','hi','ho','hr','ht','hu','hy','hz','ia','id','ie','ig','ii','ik','io','is','it','iu','ja','jv','ka','kg','ki','kj','kk','kl','km','kn','ko','kr','ks','ku','kv','kw','ky','la','lb','lg','li','ln','lo','lt','lu','lv','mg','mh','mi','mk','ml','mn','mr','ms','mt','my','na','nb','nd','ne','ng','nl','nn','no','nr','nv','ny','oc','oj','om','or','os','pa','pi','pl','ps','pt','qu','rm','rn','ro','ru','rw','sa','sc','sd','se','sg','si','sk','sl','sm','sn','so','sq','sr','ss','st','su','sv','sw','ta','te','tg','th','ti','tk','tl','tn','to','tr','ts','tt','tw','ty','ug','uk','ur','uz','ve','vi','vo','wa','wo','xh','yi','yo','za','zh','zu')"/>

  <!-- US states, DC, and US territories for postal code hygiene checks -->
  <let name="usStatesAndTerritories"
        value="('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC','AS','GU','MP','PR','VI')"/>

  <!-- Regex patterns stored in variables to avoid XSLT AVT interpretation of curly braces in compiled Schematron -->
  <let name="bcp47PrivRe" value="'^x(-[a-z0-9]{1,8})+$'"/>
  <let name="bcp47Re"
        value="'^([a-zA-Z]{2,3})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-([a-zA-Z0-9]{5,8}|[0-9][a-zA-Z0-9]{3}))*(-[0-9A-WY-Za-wy-z](-[a-zA-Z0-9]{2,8})+)*(-x(-[a-zA-Z0-9]{1,8})+)?$'"/>
  <let name="dateNoTzRe" value="'^-?\d{4,}-\d{2}-\d{2}$'"/>
  <let name="dateTimeTzRe" value="'(Z|[+-]\d{2}:\d{2})$'"/>
  <let name="latLongRe" value="'^[+-]?\d+(\.\d+)?\s*,\s*[+-]?\d+(\.\d+)?$'"/>
  <let name="plusCodeFullRe"
        value="'^([23456789CFGHJMPQRVWXcfghjmpqrvwx]{8}|[23456789CFGHJMPQRVWXcfghjmpqrvwx]{4}0000|[23456789CFGHJMPQRVWXcfghjmpqrvwx]{6}00)\+([23456789CFGHJMPQRVWXcfghjmpqrvwx]{2,7})?$'"/>
  <let name="plusCodeShortRe"
        value="'^[23456789CFGHJMPQRVWXcfghjmpqrvwx]{4,6}\+[23456789CFGHJMPQRVWXcfghjmpqrvwx]{2,7}(\s+\S.*)?$'"/>
  <let name="ocdIdRe"
        value="'^ocd-division/country:[a-z]{2}(/[\p{Ll}_-]+:[\p{Ll}0-9_~.-]+)*$'"/>
  <let name="fipsRe" value="'^\d{2,10}$'"/>
  <let name="sha256Re" value="'^[0-9a-fA-F]{64}$'"/>
  <let name="sha512Re" value="'^[0-9a-fA-F]{128}$'"/>
  <let name="usZipRe" value="'^\d{5}(-\d{4})?$'"/>

  <!-- SSRF-safe base feed loader for cross-document overlay validation -->
  <let name="rawBaseFeedPi"
        value="if (/processing-instruction('vip-base-feed')) then normalize-space(string((/processing-instruction('vip-base-feed'))[1])) else ''"/>
  <let name="baseFeedUri"
        value="if (matches($rawBaseFeedPi, '(^|\s)href\s*=\s*(&#34;[^&#34;]+&#34;|''[^'']+'')')) then replace($rawBaseFeedPi, '^.*?(^|\s)href\s*=\s*(&#34;([^&#34;]+)&#34;|''([^'']+)'').*$', '$3$4') else ''"/>
  <let name="resolvedBaseUri"
        value="if ($baseFeedUri != '') then string(resolve-uri($baseFeedUri, base-uri(/))) else ''"/>
  <let name="baseDoc"
        value="if (starts-with($resolvedBaseUri, 'file:') and doc-available($resolvedBaseUri)) then doc($resolvedBaseUri)[exists(VipObject)] else ()"/>

  <xsl:key name="entity-by-id" match="/*/*[@id]" use="@id"/>

  <phase id="strict">
      <active pattern="i18n-errors"/>
      <active pattern="i18n-language-tags"/>
      <active pattern="timezone-errors"/>
      <active pattern="time-errors"/>
      <active pattern="overlay-errors"/>
      <active pattern="overlay-polling-location-errors"/>
      <active pattern="overlay-spatial-boundary-errors"/>
      <active pattern="overlay-crossdoc-ref-errors"/>
      <active pattern="ref-target-type-errors"/>
      <active pattern="ref-idrefs-errors"/>
      <active pattern="ref-selection-subtype-errors"/>
      <active pattern="ref-ordered-contest-errors"/>
      <active pattern="ref-locality-hierarchy-errors"/>
      <active pattern="ref-cardinality-errors"/>
      <active pattern="enum-errors"/>
    
      <active pattern="geo-errors"/>
      <active pattern="hygiene-errors"/>
  </phase>

  <phase id="full">
      <active pattern="i18n-errors"/>
      <active pattern="i18n-language-tags"/>
      <active pattern="i18n-warnings"/>
      <active pattern="timezone-errors"/>
      <active pattern="timezone-warnings"/>
      <active pattern="time-errors"/>
      <active pattern="time-warnings"/>
      <active pattern="overlay-errors"/>
      <active pattern="overlay-polling-location-errors"/>
      <active pattern="overlay-spatial-boundary-errors"/>
      <active pattern="overlay-crossdoc-ref-errors"/>
      <active pattern="overlay-warnings"/>
      <active pattern="ref-target-type-errors"/>
      <active pattern="ref-idrefs-errors"/>
      <active pattern="ref-selection-subtype-errors"/>
      <active pattern="ref-ordered-contest-errors"/>
      <active pattern="ref-locality-hierarchy-errors"/>
      <active pattern="ref-cardinality-errors"/>
      <active pattern="ref-warnings"/>
      <active pattern="enum-errors"/>
    
    
      <active pattern="geo-errors"/>
      <active pattern="geo-warnings"/>
      <active pattern="hygiene-errors"/>
      <active pattern="hygiene-warnings-elements"/>
      <active pattern="hygiene-warnings-postalcode"/>
      <active pattern="hygiene-warnings-attrs"/>
  </phase>

  <!-- ================================================================ -->
  <!-- Internationalization (I18N-01 .. I18N-07)                         -->
  <!-- ================================================================ -->
  <pattern id="i18n-errors">
      <rule context="BallotMeasureContest/ConStatement | Contest/ConStatement | RetentionContest/ConStatement | BallotMeasureContest/EffectOfAbstain | Contest/EffectOfAbstain | RetentionContest/EffectOfAbstain | BallotMeasureContest/FullText | Contest/FullText | RetentionContest/FullText | BallotMeasureContest/InfoUri | Contest/InfoUri | RetentionContest/InfoUri | BallotMeasureContest/PassageThreshold | Contest/PassageThreshold | RetentionContest/PassageThreshold | BallotMeasureContest/ProStatement | Contest/ProStatement | RetentionContest/ProStatement | BallotMeasureContest/SummaryText | Contest/SummaryText | RetentionContest/SummaryText | BallotMeasureSelection/Selection | BallotSelection/Selection | BallotStyle/ImageUri | Candidate/BallotName | ContactInformation/Directions | ContactInformation/Email | ContactInformation/Fax | ContactInformation/Hours | ContactInformation/Name | ContactInformation/Phone | ContactInformation/Uri | Contest/BallotSubTitle | BallotMeasureContest/BallotSubTitle | RetentionContest/BallotSubTitle | CandidateContest/BallotSubTitle | PartyContest/BallotSubTitle | Contest/BallotTitle | BallotMeasureContest/BallotTitle | RetentionContest/BallotTitle | CandidateContest/BallotTitle | PartyContest/BallotTitle | Contest/ElectorateSpecification | BallotMeasureContest/ElectorateSpecification | RetentionContest/ElectorateSpecification | CandidateContest/ElectorateSpecification | PartyContest/ElectorateSpecification | EmergencyNotice/NoticeText | EmergencyNotice/NoticeUri | VoterService/Description | ElectionAdministration/AbsenteeUri | ElectionAdministration/AmIRegisteredUri | ElectionAdministration/BallotTrackingUri | ElectionAdministration/BallotProvisionalTrackingUri | ElectionAdministration/ElectionsUri | ElectionAdministration/RegistrationUri | ElectionAdministration/RulesUri | ElectionAdministration/WhatIsOnMyBallotUri | ElectionAdministration/WhereDoIVoteUri | ElectoralDistrict/Name | Office/Description | Office/Name | Party/LogoUri | Party/Name | Person/FullName | Person/Profession | Person/Title | PollingLocation/Directions | PollingLocation/Hours | PollingLocation/PhotoUri | Election/AbsenteeBallotInfo | Election/ElectionType | Election/Name | Election/RegistrationInfo | Election/ResultsUri">
         <assert id="I18N-01"
                 test="not(exists(Text | Uri) and exists(text()[normalize-space(.) != '']))">
        [I18N-01] <name/> must not mix non-whitespace direct text with &lt;Text&gt; or &lt;Uri&gt; sub-elements.
      </assert>
         <assert id="I18N-02a"
                 test="exists(Text | Uri) or exists(text()[normalize-space(.) != ''])">
        [I18N-02] <name/> must contain non-whitespace direct text or at least one &lt;Text&gt;/&lt;Uri&gt; child.
      </assert>
         <assert id="I18N-02b"
                 test="every $child in (Text | Uri) satisfies normalize-space($child) != ''">
        [I18N-02] Every &lt;Text&gt; or &lt;Uri&gt; child of <name/> must contain non-whitespace content.
      </assert>
         <assert id="I18N-03"
                 test="not(exists(Text | Uri)) or (some $c in (Text | Uri) satisfies lower-case(normalize-space($c/@language)) = 'i-default')">
        [I18N-03] When &lt;Text&gt; or &lt;Uri&gt; sub-elements are used in <name/>, one must have language="i-default".
      </assert>
         <assert id="I18N-04"
                 test="not(exists(Text | Uri)) or count(Text | Uri) eq count(distinct-values((Text | Uri)/lower-case(normalize-space(@language))))">
        [I18N-04] Sub-elements of <name/> must have distinct case-insensitive @language values.
      </assert>
      </rule>

      <rule context="PollingLocation[exists(AddressStructured)]">
         <let name="langs"
              value="for $a in AddressStructured return (if ($a/@language) then lower-case(normalize-space($a/@language)) else 'i-default')"/>
         <assert id="I18N-05-pl"
                 test="'i-default' = $langs and count($langs) eq count(distinct-values($langs))">
        [I18N-05] PollingLocation AddressStructured elements must include an 'i-default' fallback and have unique case-insensitive @language values.
      </assert>
      </rule>

      <rule context="Candidate/ContactInformation | VoterService/ContactInformation | ElectionAdministration/ContactInformation | Office/ContactInformation | Person/ContactInformation">
         <let name="mailLangs"
              value="for $a in MailingAddress return (if ($a/@language) then lower-case(normalize-space($a/@language)) else 'i-default')"/>
         <let name="physLangs"
              value="for $a in PhysicalAddress return (if ($a/@language) then lower-case(normalize-space($a/@language)) else 'i-default')"/>
         <assert id="I18N-05-mail"
                 test="not(exists(MailingAddress)) or ('i-default' = $mailLangs and count($mailLangs) eq count(distinct-values($mailLangs)))">
        [I18N-05] MailingAddress elements in <name/> must include an 'i-default' fallback and have unique case-insensitive @language values.
      </assert>
         <assert id="I18N-05-phys"
                 test="not(exists(PhysicalAddress)) or ('i-default' = $physLangs and count($physLangs) eq count(distinct-values($physLangs)))">
        [I18N-05] PhysicalAddress elements in <name/> must include an 'i-default' fallback and have unique case-insensitive @language values.
      </assert>
      </rule>

      <rule context="ContactInformation/MailingAddress | ContactInformation/PhysicalAddress | PollingLocation/AddressStructured">
         <assert id="I18N-07-addr" test="exists(AddressLine[normalize-space(.) != ''])">
        [I18N-07] <name/> must contain at least one non-whitespace AddressLine.
      </assert>
      </rule>
  </pattern>

  <pattern id="i18n-language-tags">
      <rule context="*/Text[@language] | *[not(self::ContactInformation or self::FeedContactInformation)]/Uri[@language] | AddressStructured[@language] | MailingAddress[@language] | PhysicalAddress[@language]">
         <let name="tag" value="normalize-space(@language)"/>
         <let name="lower" value="lower-case($tag)"/>
         <let name="primary" value="tokenize($lower, '-')[1]"/>
         <assert id="I18N-06"
                 test="$lower eq 'i-default'                     or matches($lower, $bcp47PrivRe)                     or (matches($tag, $bcp47Re) and (string-length($primary) ne 2 or $primary = $iso639_1))">
        [I18N-06] Invalid BCP-47 language tag '<value-of select="@language"/>' on <name/>. Use 'i-default' or a valid BCP-47 tag (e.g. 'en', 'es', 'zh-Hans').
      </assert>
      </rule>
  </pattern>

  <pattern id="i18n-warnings">
      <rule context="PollingLocation/AddressStructured">
         <assert id="I18N-07-us" role="warning"
                 test="if (not(Country) or upper-case(normalize-space(Country)) = ('US', 'USA', 'UNITED STATES'))                     then (exists(City[normalize-space(.) != '']) and exists(Region[normalize-space(.) != '']) and exists(PostalCode[normalize-space(.) != '']))                     else true()">
        [I18N-07] US PollingLocation/AddressStructured should provide non-empty City, Region, and PostalCode.
      </assert>
      </rule>
  </pattern>

  <!-- ================================================================ -->
  <!-- Time Zones (TZ-01 .. TZ-02)                                       -->
  <!-- ================================================================ -->
  <pattern id="timezone-errors">
      <rule context="*/TimeZone">
         <assert id="TZ-01" test="normalize-space(.) = ($ianaCanonicalZones, $ianaAliasZones)">
        [TZ-01] TimeZone '<value-of select="normalize-space(.)"/>' is not a recognized IANA time zone identifier.
      </assert>
      </rule>
  </pattern>

  <pattern id="timezone-warnings">
      <rule context="*/TimeZone[normalize-space(.) = $ianaAliasZones]">
         <let name="tz" value="normalize-space(.)"/>
         <report id="TZ-02" role="warning" test="true()">
        [TZ-02] TimeZone '<value-of select="$tz"/>' is a backward-compatible IANA alias; prefer canonical zone '<value-of select="$ianaAliasTargets[index-of($ianaAliasZones, $tz)[1]]"/>'.
      </report>
      </rule>
  </pattern>

  <!-- ================================================================ -->
  <!-- Schedules, Dates, and Times (TIME-01 .. TIME-08)                  -->
  <!-- ================================================================ -->
  <pattern id="time-errors">
      <rule context="Schedule/Hours | DefaultPollingHours/Hours | OverriddenPollingHours/Hours | DefaultEarlyVoteHours/Hours | OverriddenEarlyVoteHours/Hours | DefaultDropoffHours/Hours | OverriddenDropoffHours/Hours">
         <assert id="TIME-01" test="normalize-space(StartTime) lt normalize-space(EndTime)">
        [TIME-01] Hours StartTime (<value-of select="normalize-space(StartTime)"/>) must be strictly earlier than EndTime (<value-of select="normalize-space(EndTime)"/>).
      </assert>
      </rule>

      <rule context="ContactInformation/Schedule | Locality/DefaultPollingHours | Locality/OverriddenPollingHours | Locality/DefaultEarlyVoteHours | Locality/OverriddenEarlyVoteHours | Locality/DefaultDropoffHours | Locality/OverriddenDropoffHours | PollingLocation/Schedule | Election/Schedule">
         <assert id="TIME-02"
                 test="not(some $h1 in Hours, $h2 in $h1/following-sibling::Hours                         satisfies normalize-space($h1/StartTime) lt normalize-space($h2/EndTime)                               and normalize-space($h2/StartTime) lt normalize-space($h1/EndTime))">
        [TIME-02] <name/> contains overlapping Hours intervals.
      </assert>
         <assert id="TIME-03-sched"
                 test="not(exists(StartDate) and exists(EndDate)                         and (normalize-space(StartDate) castable as xs:date)                         and (normalize-space(EndDate) castable as xs:date))                     or xs:date(normalize-space(StartDate)) le xs:date(normalize-space(EndDate))">
        [TIME-03] <name/> StartDate (<value-of select="normalize-space(StartDate)"/>) must not be later than EndDate (<value-of select="normalize-space(EndDate)"/>).
      </assert>
         <assert id="TIME-05a"
                 test="not(exists(IsOpen24Hours) and (normalize-space(IsOpen24Hours) castable as xs:boolean) and xs:boolean(normalize-space(IsOpen24Hours)) and exists(Hours))">
        [TIME-05] <name/> cannot specify Hours when IsOpen24Hours is true.
      </assert>
         <assert id="TIME-05b"
                 test="not(exists(IsOnlyByAppointment[normalize-space(.) = ('true', '1')]) and exists(IsOrByAppointment[normalize-space(.) = ('true', '1')]))">
        [TIME-05] <name/> cannot set both IsOnlyByAppointment and IsOrByAppointment to true.
      </assert>
         <assert id="TIME-05c"
                 test="exists(Hours)                     or exists(IsOpen24Hours[normalize-space(.) = ('true', '1')])                     or exists(IsOnlyByAppointment[normalize-space(.) = ('true', '1')])                     or exists(IsOrByAppointment[normalize-space(.) = ('true', '1')])">
        [TIME-05] <name/> must specify at least one Hours interval or set IsOpen24Hours, IsOnlyByAppointment, or IsOrByAppointment to true.
      </assert>
      </rule>

      <rule context="Office/Term">
         <assert id="TIME-03-term"
                 test="not(exists(StartDate) and exists(EndDate)                         and (normalize-space(StartDate) castable as xs:date)                         and (normalize-space(EndDate) castable as xs:date))                     or xs:date(normalize-space(StartDate)) le xs:date(normalize-space(EndDate))">
        [TIME-03] Term StartDate (<value-of select="normalize-space(StartDate)"/>) must not be later than EndDate (<value-of select="normalize-space(EndDate)"/>).
      </assert>
      </rule>

      <rule context="Candidate/FileDate | Schedule/StartDate | DefaultPollingHours/StartDate | OverriddenPollingHours/StartDate | DefaultEarlyVoteHours/StartDate | OverriddenEarlyVoteHours/StartDate | DefaultDropoffHours/StartDate | OverriddenDropoffHours/StartDate | Schedule/EndDate | DefaultPollingHours/EndDate | OverriddenPollingHours/EndDate | DefaultEarlyVoteHours/EndDate | OverriddenEarlyVoteHours/EndDate | DefaultDropoffHours/EndDate | OverriddenDropoffHours/EndDate | Term/StartDate | Term/EndDate | Office/FilingDeadline | Person/DateOfBirth | Election/AbsenteeRequestDeadline | Election/Date | Election/RegistrationDeadline">
         <assert id="TIME-04" test="matches(normalize-space(.), $dateNoTzRe)">
        [TIME-04] Date element <name/> ('<value-of select="normalize-space(.)"/>') must not include a timezone suffix.
      </assert>
      </rule>
  </pattern>

  <pattern id="time-warnings">
    

      <rule context="Election">
         <assert id="TIME-07-reg" role="warning"
                 test="not(exists(RegistrationDeadline) and exists(Date)                         and (normalize-space(RegistrationDeadline) castable as xs:date)                         and (normalize-space(Date) castable as xs:date))                     or xs:date(normalize-space(RegistrationDeadline)) le xs:date(normalize-space(Date))">
        [TIME-07] Election RegistrationDeadline (<value-of select="normalize-space(RegistrationDeadline)"/>) should not be later than Election Date (<value-of select="normalize-space(Date)"/>).
      </assert>
         <assert id="TIME-07-abs" role="warning"
                 test="not(exists(AbsenteeRequestDeadline) and exists(Date)                         and (normalize-space(AbsenteeRequestDeadline) castable as xs:date)                         and (normalize-space(Date) castable as xs:date))                     or xs:date(normalize-space(AbsenteeRequestDeadline)) le xs:date(normalize-space(Date))">
        [TIME-07] Election AbsenteeRequestDeadline (<value-of select="normalize-space(AbsenteeRequestDeadline)"/>) should not be later than Election Date (<value-of select="normalize-space(Date)"/>).
      </assert>
      </rule>

    

      <rule context="PollingLocation/Hours | ContactInformation/Hours | FeedContactInformation/Hours">
         <report id="TIME-08" role="warning" test="true()">
        [TIME-08] Free-text &lt;Hours&gt; on <value-of select="local-name(..)"/> is deprecated; prefer structured &lt;Schedule&gt;.
      </report>
      </rule>
  </pattern>

  <!-- ================================================================ -->
  <!-- Overlay Rules (OVR-01..03, OVR-06..08, OVR-10..11)                -->
  <!-- ================================================================ -->
  <pattern id="overlay-errors">
      <rule context="/VipOverlay">
         <assert id="OVR-01a" test="count(*) ge 1">
        [OVR-01] VipOverlay must contain at least one entity update or new PollingLocation.
      </assert>
         <assert id="OVR-01b" test="count(Election) le 1">
        [OVR-01] VipOverlay may contain at most one Election element.
      </assert>
         <assert id="OVR-10-base"
                 test="not(starts-with($resolvedBaseUri, 'file:')) or exists($baseDoc)">
        [OVR-10] Base feed '<value-of select="$baseFeedUri"/>' declared in &lt;?vip-base-feed?&gt; could not be loaded.
      </assert>
      </rule>

      <rule context="/VipOverlay/*">
         <assert id="OVR-02" test="exists(*)">
        [OVR-02] Overlay entity <name/> (id="<value-of select="@id"/>") must contain at least one field update, Clear* element, or EmergencyNotice.
      </assert>
         <assert id="OVR-10"
                 test="not(exists($baseDoc))                     or (if (self::PollingLocation[normalize-space(@isNew) = ('true', '1')])                         then not(exists(key('entity-by-id', @id, $baseDoc)))                         else exists(key('entity-by-id', @id, $baseDoc)[(if (@xsi:type) then normalize-space(@xsi:type) else local-name()) = (if (current()/@xsi:type) then normalize-space(current()/@xsi:type) else local-name(current()))]))">
        [OVR-10] Overlay entity <name/> (id="<value-of select="@id"/>") fails base-feed identity matching (isNew IDs must not exist in base feed; update IDs must exist in base feed with matching entity type).
      </assert>
      </rule>

      <rule context="EmergencyNotice">
         <assert id="OVR-07a" test="exists(NoticeText | NoticeUri)">
        [OVR-07] EmergencyNotice must contain NoticeText or NoticeUri.
      </assert>
         <assert id="OVR-07b" test="count(NoticeText) le 1">
        [OVR-07] EmergencyNotice may contain at most one NoticeText element.
      </assert>
         <assert id="OVR-07c" test="every $a in AppliesTo satisfies normalize-space($a) != ''">
        [OVR-07] EmergencyNotice AppliesTo values must not be empty or whitespace-only.
      </assert>
         <assert id="OVR-07d"
                 test="count(AppliesTo) eq count(distinct-values(AppliesTo/lower-case(normalize-space(.))))">
        [OVR-07] EmergencyNotice AppliesTo values must be unique (case-insensitive).
      </assert>
      </rule>
  </pattern>

  <pattern id="overlay-polling-location-errors">
      <rule context="/VipOverlay/PollingLocation[normalize-space(@isNew) = ('true', '1')]">
         <assert id="OVR-03-req" test="exists(AddressStructured) and exists(LocationType)">
        [OVR-03] New PollingLocation (id="<value-of select="@id"/>", isNew="true") must provide both AddressStructured and LocationType.
      </assert>
      </rule>
  </pattern>

  <pattern id="overlay-spatial-boundary-errors">
      <rule context="/VipOverlay/Precinct/SpatialBoundary[exists($baseDoc)]">
         <let name="fid" value="normalize-space(ExternalGeospatialFeature/ExternalFileId)"/>
         <let name="fmt" value="normalize-space(ExternalGeospatialFeature/FileFormat)"/>
         <let name="idxs"
              value="distinct-values(ExternalGeospatialFeature/FeatureIdentifier/normalize-space(Index))"/>
         <assert id="OVR-06"
                 test="some $bf in $baseDoc/VipObject/Precinct/SpatialBoundary/ExternalGeospatialFeature                     satisfies (                       normalize-space($bf/ExternalFileId) eq $fid                       and normalize-space($bf/FileFormat) eq $fmt                       and count($idxs) eq count(distinct-values($bf/FeatureIdentifier/normalize-space(Index)))                       and (every $x in $idxs satisfies $x = distinct-values($bf/FeatureIdentifier/normalize-space(Index)))                     )">
        [OVR-06] Overlay Precinct SpatialBoundary must match an existing ExternalGeospatialFeature in the base feed (same ExternalFileId, FileFormat, and set of FeatureIdentifier/Index values).
      </assert>
      </rule>
  </pattern>

  <pattern id="overlay-crossdoc-ref-errors">
      <rule context="/VipOverlay//Candidate/PartyId | /VipOverlay//Person/PartyId | /VipOverlay//BallotStyle/PartyIds | /VipOverlay//CandidateContest/PrimaryPartyIds | /VipOverlay//Contest/PrimaryPartyIds | /VipOverlay//CandidateSelection/EndorsementPartyIds | /VipOverlay//BallotSelection/EndorsementPartyIds | /VipOverlay//PartySelection/PartyIds | /VipOverlay//BallotSelection/PartyIds | /VipOverlay//PollingLocation/PartyIds">
         <assert id="OVR-11-party"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::Party]))">
        [OVR-11] Reference in <name/> must resolve to a Party in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//Candidate/PersonId | /VipOverlay//VoterService/ElectionOfficialPersonId | /VipOverlay//Office/OfficeHolderPersonIds | /VipOverlay//Party/LeaderPersonIds">
         <assert id="OVR-11-person"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::Person]))">
        [OVR-11] Reference in <name/> must resolve to a Person in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//ElectoralDistrictId | /VipOverlay//Precinct/ElectoralDistrictIds">
         <assert id="OVR-11-ed"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::ElectoralDistrict]))">
        [OVR-11] Reference in <name/> must resolve to an ElectoralDistrict in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//ExternalGeospatialFeature/ExternalFileId">
         <assert id="OVR-11-ef"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::ExternalFile]))">
        [OVR-11] ExternalFileId must resolve to an ExternalFile in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//Locality/ParentLocalityId | /VipOverlay//Precinct/LocalityId | /VipOverlay//Election/TopLevelLocalityId">
         <assert id="OVR-11-loc"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::Locality]))">
        [OVR-11] Reference in <name/> must resolve to a Locality in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//OrderedContest/ContestId">
         <assert id="OVR-11-contest"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::Contest or self::BallotMeasureContest or self::CandidateContest or self::PartyContest or self::RetentionContest]))">
        [OVR-11] ContestId must resolve to a Contest in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//Precinct/BallotStyleId">
         <assert id="OVR-11-bs"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::BallotStyle]))">
        [OVR-11] BallotStyleId must resolve to a BallotStyle in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//RetentionContest/CandidateId | /VipOverlay//Contest/CandidateId | /VipOverlay//CandidateSelection/CandidateIds | /VipOverlay//BallotSelection/CandidateIds">
         <assert id="OVR-11-cand"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::Candidate]))">
        [OVR-11] Reference in <name/> must resolve to a Candidate in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//RetentionContest/OfficeId | /VipOverlay//Contest/OfficeId | /VipOverlay//CandidateContest/OfficeIds | /VipOverlay//Contest/OfficeIds">
         <assert id="OVR-11-office"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::Office]))">
        [OVR-11] Reference in <name/> must resolve to an Office in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//BallotStyle/OrderedContestIds">
         <assert id="OVR-11-oc"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::OrderedContest]))">
        [OVR-11] OrderedContestIds must resolve to OrderedContest entities in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//BallotSelectionIds | /VipOverlay//OrderedContest/OrderedBallotSelectionIds">
         <assert id="OVR-11-sel"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies exists(key('entity-by-id', $t, $baseDoc)[self::BallotSelection or self::BallotMeasureSelection or self::CandidateSelection or self::PartySelection]))">
        [OVR-11] Reference in <name/> must resolve to BallotSelection entities in the base feed.
      </assert>
      </rule>
      <rule context="/VipOverlay//Locality/PollingLocationIds | /VipOverlay//Precinct/PollingLocationIds">
         <assert id="OVR-11-pl"
                 test="not(exists($baseDoc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (exists(key('entity-by-id', $t, $baseDoc)[self::PollingLocation]) or exists(/VipOverlay/PollingLocation[normalize-space(@isNew) = ('true', '1') and @id = $t])))">
        [OVR-11] PollingLocationIds must resolve to PollingLocation entities in the base feed or new PollingLocations (@isNew="true") in this overlay.
      </assert>
      </rule>
  </pattern>

  <pattern id="overlay-warnings">
      <rule context="/VipOverlay/PollingLocation[normalize-space(@isNew) = ('true', '1')]">
         <assert id="OVR-03-clear" role="warning"
                 test="not(exists(*[starts-with(local-name(), 'Clear')]))">
        [OVR-03] New PollingLocation (id="<value-of select="@id"/>", isNew="true") should not contain Clear* elements.
      </assert>
      </rule>

      <rule context="/VipOverlay/Locality">
         <assert id="OVR-08-polling" role="warning"
                 test="not(exists(DefaultPollingHours) and exists(OverriddenPollingHours))">
        [OVR-08] Locality overlay should not set both DefaultPollingHours and OverriddenPollingHours simultaneously.
      </assert>
         <assert id="OVR-08-early" role="warning"
                 test="not(exists(DefaultEarlyVoteHours) and exists(OverriddenEarlyVoteHours))">
        [OVR-08] Locality overlay should not set both DefaultEarlyVoteHours and OverriddenEarlyVoteHours simultaneously.
      </assert>
         <assert id="OVR-08-dropoff" role="warning"
                 test="not(exists(DefaultDropoffHours) and exists(OverriddenDropoffHours))">
        [OVR-08] Locality overlay should not set both DefaultDropoffHours and OverriddenDropoffHours simultaneously.
      </assert>
      </rule>
  </pattern>

  <!-- ================================================================ -->
  <!-- Referential Integrity & Subtypes (REF-01 .. REF-08)               -->
  <!-- ================================================================ -->
  <pattern id="ref-target-type-errors">
    <!-- Main Feed: strict resolution in /VipObject -->
    
    
    
    
    
    
    
    
    
    
    
    
    

    <!-- Overlay standalone: if an ID exists inside /VipOverlay, it must match expected target type -->
    <rule context="Candidate/PartyId | Person/PartyId | BallotStyle/PartyIds | CandidateContest/PrimaryPartyIds | Contest/PrimaryPartyIds | CandidateSelection/EndorsementPartyIds | BallotSelection/EndorsementPartyIds | PartySelection/PartyIds | BallotSelection/PartyIds | PollingLocation/PartyIds">
         <assert id="REF-01-ov-party"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::Party]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to a Party entity.
      </assert>
      </rule>
      <rule context="Candidate/PersonId | VoterService/ElectionOfficialPersonId | Office/OfficeHolderPersonIds | Party/LeaderPersonIds">
         <assert id="REF-01-ov-person"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::Person]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to a Person entity.
      </assert>
      </rule>
      <rule context="ElectoralDistrictId | Precinct/ElectoralDistrictIds">
         <assert id="REF-01-ov-ed"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::ElectoralDistrict]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to an ElectoralDistrict entity.
      </assert>
      </rule>
      <rule context="ExternalGeospatialFeature/ExternalFileId">
         <assert id="REF-01-ov-ef"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::ExternalFile]))">
        [REF-01] ExternalFileId resolving inside VipOverlay must point to an ExternalFile entity.
      </assert>
      </rule>
      <rule context="Locality/ParentLocalityId | Precinct/LocalityId | Election/TopLevelLocalityId">
         <assert id="REF-01-ov-loc"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::Locality]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to a Locality entity.
      </assert>
      </rule>
      <rule context="OrderedContest/ContestId">
         <assert id="REF-01-ov-contest"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::Contest or self::BallotMeasureContest or self::CandidateContest or self::PartyContest or self::RetentionContest]))">
        [REF-01] ContestId resolving inside VipOverlay must point to a Contest entity.
      </assert>
      </rule>
      <rule context="Precinct/BallotStyleId">
         <assert id="REF-01-ov-bs"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::BallotStyle]))">
        [REF-01] BallotStyleId resolving inside VipOverlay must point to a BallotStyle entity.
      </assert>
      </rule>
      <rule context="RetentionContest/CandidateId | Contest/CandidateId | CandidateSelection/CandidateIds | BallotSelection/CandidateIds">
         <assert id="REF-01-ov-cand"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::Candidate]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to a Candidate entity.
      </assert>
      </rule>
      <rule context="RetentionContest/OfficeId | Contest/OfficeId | CandidateContest/OfficeIds | Contest/OfficeIds">
         <assert id="REF-01-ov-office"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::Office]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to an Office entity.
      </assert>
      </rule>
      <rule context="BallotStyle/OrderedContestIds">
         <assert id="REF-01-ov-oc"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::OrderedContest]))">
        [REF-01] OrderedContestIds resolving inside VipOverlay must point to OrderedContest entities.
      </assert>
      </rule>
      <rule context="BallotSelectionIds | OrderedContest/OrderedBallotSelectionIds">
         <assert id="REF-01-ov-sel"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::BallotSelection or self::BallotMeasureSelection or self::CandidateSelection or self::PartySelection]))">
        [REF-01] <name/> reference resolving inside VipOverlay must point to BallotSelection entities.
      </assert>
      </rule>
      <rule context="Locality/PollingLocationIds | Precinct/PollingLocationIds">
         <assert id="REF-01-ov-pl"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies (not(exists(key('entity-by-id', $t))) or exists(key('entity-by-id', $t)[self::PollingLocation]))">
        [REF-01] PollingLocationIds resolving inside VipOverlay must point to PollingLocation entities.
      </assert>
      </rule>
  </pattern>

  <pattern id="ref-idrefs-errors">
      <rule context="BallotStyle/OrderedContestIds | BallotStyle/PartyIds | CandidateContest/OfficeIds | Contest/OfficeIds | CandidateContest/PrimaryPartyIds | Contest/PrimaryPartyIds | CandidateSelection/CandidateIds | BallotSelection/CandidateIds | CandidateSelection/EndorsementPartyIds | BallotSelection/EndorsementPartyIds | Contest/BallotSelectionIds | BallotMeasureContest/BallotSelectionIds | RetentionContest/BallotSelectionIds | CandidateContest/BallotSelectionIds | PartyContest/BallotSelectionIds | Locality/PollingLocationIds | Office/OfficeHolderPersonIds | OrderedContest/OrderedBallotSelectionIds | Party/LeaderPersonIds | PartySelection/PartyIds | BallotSelection/PartyIds | PollingLocation/PartyIds | Precinct/ElectoralDistrictIds | Precinct/PollingLocationIds">
         <let name="tokens" value="tokenize(normalize-space(.), '\s+')[. != '']"/>
         <assert id="REF-02"
                 test="count($tokens) ge 1 and count($tokens) eq count(distinct-values($tokens))">
        [REF-02] <name/> must contain at least one ID reference and no duplicate IDs.
      </assert>
      </rule>
  </pattern>

  <pattern id="ref-selection-subtype-errors">
    
    
    

      <rule context="BallotMeasureContest/BallotSelectionIds | RetentionContest/BallotSelectionIds | Contest[normalize-space(@xsi:type) = ('BallotMeasureContest', 'RetentionContest')]/BallotSelectionIds">
         <assert id="REF-03-ov-bm"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != '']                     satisfies (if (exists(key('entity-by-id', $t)))                                then exists(key('entity-by-id', $t)[self::BallotMeasureSelection or self::BallotSelection[normalize-space(@xsi:type) = 'BallotMeasureSelection']])                                else if (exists($baseDoc) and exists(key('entity-by-id', $t, $baseDoc)))                                then exists(key('entity-by-id', $t, $baseDoc)[self::BallotMeasureSelection or self::BallotSelection[normalize-space(@xsi:type) = 'BallotMeasureSelection']])                                else true())">
        [REF-03] BallotMeasureContest/RetentionContest BallotSelectionIds must reference BallotMeasureSelection entities.
      </assert>
      </rule>
      <rule context="CandidateContest/BallotSelectionIds | Contest[normalize-space(@xsi:type) = 'CandidateContest']/BallotSelectionIds">
         <assert id="REF-03-ov-cand"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != '']                     satisfies (if (exists(key('entity-by-id', $t)))                                then exists(key('entity-by-id', $t)[self::CandidateSelection or self::BallotSelection[normalize-space(@xsi:type) = 'CandidateSelection']])                                else if (exists($baseDoc) and exists(key('entity-by-id', $t, $baseDoc)))                                then exists(key('entity-by-id', $t, $baseDoc)[self::CandidateSelection or self::BallotSelection[normalize-space(@xsi:type) = 'CandidateSelection']])                                else true())">
        [REF-03] CandidateContest BallotSelectionIds must reference CandidateSelection entities.
      </assert>
      </rule>
      <rule context="PartyContest/BallotSelectionIds | Contest[normalize-space(@xsi:type) = 'PartyContest']/BallotSelectionIds">
         <assert id="REF-03-ov-party"
                 test="every $t in tokenize(normalize-space(.), '\s+')[. != '']                     satisfies (if (exists(key('entity-by-id', $t)))                                then exists(key('entity-by-id', $t)[self::PartySelection or self::BallotSelection[normalize-space(@xsi:type) = 'PartySelection']])                                else if (exists($baseDoc) and exists(key('entity-by-id', $t, $baseDoc)))                                then exists(key('entity-by-id', $t, $baseDoc)[self::PartySelection or self::BallotSelection[normalize-space(@xsi:type) = 'PartySelection']])                                else true())">
        [REF-03] PartyContest BallotSelectionIds must reference PartySelection entities.
      </assert>
      </rule>
  </pattern>

  <pattern id="ref-ordered-contest-errors">
    

      <rule context="OrderedContest/OrderedBallotSelectionIds">
         <let name="cid"
              value="if (exists(../ContestId)) then normalize-space(../ContestId) else if (exists($baseDoc)) then normalize-space(key('entity-by-id', ../@id, $baseDoc)[self::OrderedContest]/ContestId) else ''"/>
         <let name="oc"
              value="key('entity-by-id', $cid)[self::Contest or self::BallotMeasureContest or self::CandidateContest or self::PartyContest or self::RetentionContest]"/>
         <let name="bc"
              value="if (exists($baseDoc)) then key('entity-by-id', $cid, $baseDoc)[self::Contest or self::BallotMeasureContest or self::CandidateContest or self::PartyContest or self::RetentionContest] else ()"/>
         <let name="effBs"
              value="if (exists($oc/BallotSelectionIds)) then $oc/BallotSelectionIds                   else if (exists($oc/ClearBallotSelectionIds)) then ()                   else $bc/BallotSelectionIds"/>
         <let name="allowed"
              value="if (exists($effBs)) then tokenize(normalize-space($effBs), '\s+')[. != ''] else ()"/>
         <assert id="REF-04-ov"
                 test="not(exists($oc) or exists($bc)) or (every $t in tokenize(normalize-space(.), '\s+')[. != ''] satisfies $t = $allowed)">
        [REF-04] OrderedContest OrderedBallotSelectionIds must all appear in the referenced Contest's effective BallotSelectionIds.
      </assert>
      </rule>
  </pattern>

  <pattern id="ref-locality-hierarchy-errors">
    

      <rule context="Locality">
         <let name="selfId" value="normalize-space(@id)"/>
         <let name="p1"
              value="if (exists(ParentLocalityId)) then normalize-space(ParentLocalityId)                   else if (exists(ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $selfId, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p2"
              value="if ($p1 = '') then ''                   else if (exists(key('entity-by-id', $p1)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p1)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p1)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p1, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p3"
              value="if ($p2 = '') then ''                   else if (exists(key('entity-by-id', $p2)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p2)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p2)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p2, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p4"
              value="if ($p3 = '') then ''                   else if (exists(key('entity-by-id', $p3)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p3)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p3)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p3, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p5"
              value="if ($p4 = '') then ''                   else if (exists(key('entity-by-id', $p4)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p4)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p4)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p4, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p6"
              value="if ($p5 = '') then ''                   else if (exists(key('entity-by-id', $p5)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p5)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p5)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p5, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p7"
              value="if ($p6 = '') then ''                   else if (exists(key('entity-by-id', $p6)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p6)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p6)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p6, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <let name="p8"
              value="if ($p7 = '') then ''                   else if (exists(key('entity-by-id', $p7)[self::Locality]/ParentLocalityId)) then normalize-space(key('entity-by-id', $p7)[self::Locality]/ParentLocalityId)                   else if (exists(key('entity-by-id', $p7)[self::Locality]/ClearParentLocalityId)) then ''                   else if (exists($baseDoc)) then normalize-space(key('entity-by-id', $p7, $baseDoc)[self::Locality]/ParentLocalityId)                   else ''"/>
         <assert id="REF-05-ov-self"
                 test="not(ParentLocalityId) or normalize-space(ParentLocalityId) != $selfId">
        [REF-05] Locality (id="<value-of select="$selfId"/>") cannot reference itself as ParentLocalityId.
      </assert>
         <assert id="REF-05-ov-nocycle"
                 test="not($selfId = ($p1, $p2, $p3, $p4, $p5, $p6, $p7, $p8))">
        [REF-05] Locality (id="<value-of select="$selfId"/>") creates a ParentLocalityId cycle.
      </assert>
      </rule>
  </pattern>

  <pattern id="ref-cardinality-errors">
      <rule context="CandidateContest/NumberElected | Contest/NumberElected">
         <assert id="REF-08-elected"
                 test="(normalize-space(.) castable as xs:integer) and xs:integer(normalize-space(.)) ge 1">
        [REF-08] NumberElected must be &gt;= 1.
      </assert>
      </rule>
      <rule context="CandidateContest/VotesAllowed | Contest/VotesAllowed">
         <assert id="REF-08-votes"
                 test="(normalize-space(.) castable as xs:integer) and xs:integer(normalize-space(.)) ge 1">
        [REF-08] VotesAllowed must be &gt;= 1.
      </assert>
         <assert id="REF-08-1ofm"
                 test="not(normalize-space(../VoteVariation) = '1-of-m') or ((normalize-space(.) castable as xs:integer) and xs:integer(normalize-space(.)) eq 1)">
        [REF-08] VotesAllowed must equal 1 when VoteVariation is '1-of-m'.
      </assert>
      </rule>
      <rule context="ElectoralDistrict/Number">
         <assert id="REF-08-ednum"
                 test="(normalize-space(.) castable as xs:integer) and xs:integer(normalize-space(.)) ge 0">
        [REF-08] ElectoralDistrict Number must be &gt;= 0.
      </assert>
      </rule>
      <rule context="*/SequenceOrder">
         <assert id="REF-08-seq"
                 test="(normalize-space(.) castable as xs:integer) and xs:integer(normalize-space(.)) ge 0">
        [REF-08] SequenceOrder must be &gt;= 0.
      </assert>
      </rule>
  </pattern>

  <pattern id="ref-warnings">
      <rule context="PollingLocation[normalize-space(LocationType) = 'DropOff']">
         <assert id="REF-06" role="warning" test="not(exists(PartyIds))">
        [REF-06] DropOff PollingLocation (id="<value-of select="@id"/>") should not specify PartyIds.
      </assert>
      </rule>

    
  </pattern>

  <!-- ================================================================ -->
  <!-- Enum 'other' <-> Other* Pairing (ENUM-01, ENUM-02)                -->
  <!-- ================================================================ -->
  <pattern id="enum-errors">
    <!-- Wholesale value objects (both Main & Overlay) -->
    <rule context="VoterService | ExternalIdentifier | LocationIdentifier">
         <assert id="ENUM-01-val-pair"
                 test="(normalize-space(Type) = 'other') eq exists(OtherType)">
        [ENUM-01] <name/> must specify OtherType if and only if Type is 'other'.
      </assert>
         <assert id="ENUM-01-val-nonempty"
                 test="not(exists(OtherType)) or normalize-space(OtherType) != ''">
        [ENUM-01] <name/>/OtherType must not be empty or whitespace-only.
      </assert>
      </rule>

      <!-- Main Feed patchable entities -->
    

    

    

    <!-- Overlay patchable entities (clear-then-set + cross-doc merge semantics) -->
    <rule context="BallotMeasureContest | RetentionContest | Contest[normalize-space(@xsi:type) = ('BallotMeasureContest', 'RetentionContest')]">
         <let name="baseEntity"
              value="if (exists($baseDoc)) then key('entity-by-id', @id, $baseDoc) else ()"/>
         <let name="effType"
              value="if (exists(Type)) then normalize-space(Type) else if (exists(ClearType)) then '' else normalize-space($baseEntity/Type)"/>
         <let name="effOtherType"
              value="if (exists(OtherType)) then normalize-space(OtherType) else if (exists(ClearOtherType)) then '' else normalize-space($baseEntity/OtherType)"/>
         <let name="effVv"
              value="if (exists(VoteVariation)) then normalize-space(VoteVariation) else if (exists(ClearVoteVariation)) then '' else normalize-space($baseEntity/VoteVariation)"/>
         <let name="effOtherVv"
              value="if (exists(OtherVoteVariation)) then normalize-space(OtherVoteVariation) else if (exists(ClearOtherVoteVariation)) then '' else normalize-space($baseEntity/OtherVoteVariation)"/>
         <assert id="ENUM-02-bmc-type-notother"
                 test="not(exists(Type) and normalize-space(Type) != 'other') or not(exists(OtherType))">
        [ENUM-02] <name/> cannot specify OtherType when Type is not 'other'.
      </assert>
         <assert id="ENUM-02-bmc-type-cleartype"
                 test="not(not(exists(Type)) and exists(ClearType)) or not(exists(OtherType))">
        [ENUM-02] <name/> cannot specify OtherType when clearing Type without setting Type='other'.
      </assert>
         <assert id="ENUM-02-bmc-type-standalone"
                 test="not(exists(Type) and normalize-space(Type) = 'other' and empty($baseDoc)) or (exists(OtherType) and normalize-space(OtherType) != '')">
        [ENUM-02] <name/> must provide a non-empty OtherType when Type is 'other'.
      </assert>
         <assert id="ENUM-02-bmc-type-crossdoc"
                 test="empty($baseEntity) or (($effType = 'other') eq ($effOtherType != ''))">
        [ENUM-02] Merged <name/> (id="<value-of select="@id"/>") must have OtherType if and only if Type is 'other'.
      </assert>
         <assert id="ENUM-02-bmc-vv-notother"
                 test="not(exists(VoteVariation) and normalize-space(VoteVariation) != 'other') or not(exists(OtherVoteVariation))">
        [ENUM-02] <name/> cannot specify OtherVoteVariation when VoteVariation is not 'other'.
      </assert>
         <assert id="ENUM-02-bmc-vv-clear"
                 test="not(not(exists(VoteVariation)) and exists(ClearVoteVariation)) or not(exists(OtherVoteVariation))">
        [ENUM-02] <name/> cannot specify OtherVoteVariation when clearing VoteVariation without setting VoteVariation='other'.
      </assert>
         <assert id="ENUM-02-bmc-vv-standalone"
                 test="not(exists(VoteVariation) and normalize-space(VoteVariation) = 'other' and empty($baseDoc)) or (exists(OtherVoteVariation) and normalize-space(OtherVoteVariation) != '')">
        [ENUM-02] <name/> must provide a non-empty OtherVoteVariation when VoteVariation is 'other'.
      </assert>
         <assert id="ENUM-02-bmc-vv-crossdoc"
                 test="empty($baseEntity) or (($effVv = 'other') eq ($effOtherVv != ''))">
        [ENUM-02] Merged <name/> (id="<value-of select="@id"/>") must have OtherVoteVariation if and only if VoteVariation is 'other'.
      </assert>
      </rule>

      <rule context="CandidateContest | PartyContest | Contest[not(normalize-space(@xsi:type) = ('BallotMeasureContest', 'RetentionContest'))]">
         <let name="baseEntity"
              value="if (exists($baseDoc)) then key('entity-by-id', @id, $baseDoc) else ()"/>
         <let name="effVv"
              value="if (exists(VoteVariation)) then normalize-space(VoteVariation) else if (exists(ClearVoteVariation)) then '' else normalize-space($baseEntity/VoteVariation)"/>
         <let name="effOtherVv"
              value="if (exists(OtherVoteVariation)) then normalize-space(OtherVoteVariation) else if (exists(ClearOtherVoteVariation)) then '' else normalize-space($baseEntity/OtherVoteVariation)"/>
         <assert id="ENUM-02-cb-vv-notother"
                 test="not(exists(VoteVariation) and normalize-space(VoteVariation) != 'other') or not(exists(OtherVoteVariation))">
        [ENUM-02] <name/> cannot specify OtherVoteVariation when VoteVariation is not 'other'.
      </assert>
         <assert id="ENUM-02-cb-vv-clear"
                 test="not(not(exists(VoteVariation)) and exists(ClearVoteVariation)) or not(exists(OtherVoteVariation))">
        [ENUM-02] <name/> cannot specify OtherVoteVariation when clearing VoteVariation without setting VoteVariation='other'.
      </assert>
         <assert id="ENUM-02-cb-vv-standalone"
                 test="not(exists(VoteVariation) and normalize-space(VoteVariation) = 'other' and empty($baseDoc)) or (exists(OtherVoteVariation) and normalize-space(OtherVoteVariation) != '')">
        [ENUM-02] <name/> must provide a non-empty OtherVoteVariation when VoteVariation is 'other'.
      </assert>
         <assert id="ENUM-02-cb-vv-crossdoc"
                 test="empty($baseEntity) or (($effVv = 'other') eq ($effOtherVv != ''))">
        [ENUM-02] Merged <name/> (id="<value-of select="@id"/>") must have OtherVoteVariation if and only if VoteVariation is 'other'.
      </assert>
      </rule>

      <rule context="ElectoralDistrict | Locality">
         <let name="baseEntity"
              value="if (exists($baseDoc)) then key('entity-by-id', @id, $baseDoc) else ()"/>
         <let name="effType"
              value="if (exists(Type)) then normalize-space(Type) else if (exists(ClearType)) then '' else normalize-space($baseEntity/Type)"/>
         <let name="effOtherType"
              value="if (exists(OtherType)) then normalize-space(OtherType) else if (exists(ClearOtherType)) then '' else normalize-space($baseEntity/OtherType)"/>
         <assert id="ENUM-02-edloc-type-notother"
                 test="not(exists(Type) and normalize-space(Type) != 'other') or not(exists(OtherType))">
        [ENUM-02] <name/> cannot specify OtherType when Type is not 'other'.
      </assert>
         <assert id="ENUM-02-edloc-type-clear"
                 test="not(not(exists(Type)) and exists(ClearType)) or not(exists(OtherType))">
        [ENUM-02] <name/> cannot specify OtherType when clearing Type without setting Type='other'.
      </assert>
         <assert id="ENUM-02-edloc-type-standalone"
                 test="not(exists(Type) and normalize-space(Type) = 'other' and empty($baseDoc)) or (exists(OtherType) and normalize-space(OtherType) != '')">
        [ENUM-02] <name/> must provide a non-empty OtherType when Type is 'other'.
      </assert>
         <assert id="ENUM-02-edloc-type-crossdoc"
                 test="empty($baseEntity) or (($effType = 'other') eq ($effOtherType != ''))">
        [ENUM-02] Merged <name/> (id="<value-of select="@id"/>") must have OtherType if and only if Type is 'other'.
      </assert>
      </rule>
  </pattern>

  <!-- ================================================================ -->
  <!-- Street Segments (SS-01 .. SS-04, Main Feed Only)                  -->
  <!-- ================================================================ -->
  

  

  <!-- ================================================================ -->
  <!-- Geospatial, Identifiers, Checksums (GEO-01 .. GEO-05)             -->
  <!-- ================================================================ -->
  <pattern id="geo-errors">
      <rule context="LatLng">
         <assert id="GEO-01-err"
                 test="(normalize-space(Latitude) castable as xs:double)                     and (normalize-space(Longitude) castable as xs:double)                     and not(normalize-space(Latitude) = ('NaN', 'INF', '-INF', '+INF'))                     and not(normalize-space(Longitude) = ('NaN', 'INF', '-INF', '+INF'))                     and xs:double(normalize-space(Latitude)) ge -90                     and xs:double(normalize-space(Latitude)) le 90                     and xs:double(normalize-space(Longitude)) ge -180                     and xs:double(normalize-space(Longitude)) le 180">
        [GEO-01] LatLng coordinates must be finite numbers with Latitude in [-90, 90] and Longitude in [-180, 180].
      </assert>
      </rule>

      <rule context="LocationIdentifier">
         <assert id="GEO-02-latlong"
                 test="if (normalize-space(Type) = 'latlong')                     then (if (matches(normalize-space(Value), $latLongRe))                           then (for $lat in xs:double(tokenize(normalize-space(Value), '\s*,\s*')[1]),                                     $lon in xs:double(tokenize(normalize-space(Value), '\s*,\s*')[2])                                 return $lat ge -90 and $lat le 90 and $lon ge -180 and $lon le 180)                           else false())                     else true()">
        [GEO-02] LocationIdentifier with Type='latlong' must have valid 'lat,lon' Value within [-90,90], [-180,180].
      </assert>
         <assert id="GEO-02-pluscode"
                 test="if (normalize-space(Type) = 'pluscode')                     then (matches(normalize-space(Value), $plusCodeFullRe) or matches(normalize-space(Value), $plusCodeShortRe))                     else true()">
        [GEO-02] LocationIdentifier with Type='pluscode' must contain a valid Open Location Code Value.
      </assert>
      </rule>

      <rule context="ExternalIdentifier">
         <assert id="GEO-03-ocdid"
                 test="if (normalize-space(Type) = 'ocd-id')                     then matches(normalize-space(Value), $ocdIdRe)                     else true()">
        [GEO-03] ExternalIdentifier with Type='ocd-id' must match '^ocd-division/country:[a-z]{2}(/[\p{Ll}_-]+:[\p{Ll}0-9_~.-]+)*$'.
      </assert>
      </rule>

    

      <rule context="ExternalGeospatialFeature[normalize-space(FileFormat) = 'shp']">
         <assert id="GEO-05"
                 test="exists(FeatureIdentifier)                     and (every $idx in FeatureIdentifier/normalize-space(Index)                          satisfies (matches($idx, '^\d+$') and xs:integer($idx) le 2147483647))                     and (count(FeatureIdentifier) eq count(distinct-values(FeatureIdentifier[matches(normalize-space(Index), '^\d+$')]/xs:integer(normalize-space(Index)))))">
        [GEO-05] Shapefile ExternalGeospatialFeature FeatureIdentifier/Index values must be unique 32-bit non-negative integers (&lt;= 2147483647).
      </assert>
      </rule>
  </pattern>

  <pattern id="geo-warnings">
      <rule context="LatLng">
         <assert id="GEO-01-warn" role="warning"
                 test="not((normalize-space(Latitude) castable as xs:double)                         and (normalize-space(Longitude) castable as xs:double)                         and not(normalize-space(Latitude) = ('NaN', 'INF', '-INF', '+INF'))                         and not(normalize-space(Longitude) = ('NaN', 'INF', '-INF', '+INF'))                         and xs:double(normalize-space(Latitude)) eq 0                         and xs:double(normalize-space(Longitude)) eq 0)">
        [GEO-01] LatLng (0, 0) appears to be a Null Island placeholder coordinate.
      </assert>
      </rule>

      <rule context="LocationIdentifier[normalize-space(Type) = 'geocoder-id']">
         <assert id="GEO-02-geocoder" role="warning"
                 test="exists(@provider) and normalize-space(@provider) != ''">
        [GEO-02] LocationIdentifier with Type='geocoder-id' should specify a non-empty @provider attribute.
      </assert>
      </rule>

      <rule context="ExternalIdentifier[normalize-space(Type) = 'fips']">
         <assert id="GEO-03-fips" role="warning" test="matches(normalize-space(Value), $fipsRe)">
        [GEO-03] ExternalIdentifier with Type='fips' should be 2 to 10 digits ('<value-of select="normalize-space(Value)"/>').
      </assert>
      </rule>

    
  </pattern>

  <!-- ================================================================ -->
  <!-- URI & Data Hygiene (HYG-01 .. HYG-04)                             -->
  <!-- ================================================================ -->
  <pattern id="hygiene-errors">
      <rule context="BallotMeasureContest/InfoUri | Contest/InfoUri | RetentionContest/InfoUri | BallotStyle/ImageUri | ContactInformation/Uri | EmergencyNotice/NoticeUri | ElectionAdministration/AbsenteeUri | ElectionAdministration/AmIRegisteredUri | ElectionAdministration/BallotTrackingUri | ElectionAdministration/BallotProvisionalTrackingUri | ElectionAdministration/ElectionsUri | ElectionAdministration/RegistrationUri | ElectionAdministration/RulesUri | ElectionAdministration/WhatIsOnMyBallotUri | ElectionAdministration/WhereDoIVoteUri | Party/LogoUri | PollingLocation/PhotoUri | Election/ResultsUri">
         <assert id="HYG-01"
                 test="if (exists(Uri))                     then (every $u in Uri satisfies matches(normalize-space($u), '^https?://\S+$'))                     else matches(normalize-space(.), '^https?://\S+$')">
        [HYG-01] URI value in <name/> must be a valid HTTP or HTTPS URL (starting with http:// or https://).
      </assert>
      </rule>

      <rule context="ContactInformation | FeedContactInformation | ElectionAdministration | VoterService | Term">
         <assert id="HYG-02-container" test="exists(*)">
        [HYG-02] <name/> must not be an empty container element.
      </assert>
      </rule>

    

      <rule context="BallotMeasureContest/Name | CandidateContest/Name | PartyContest/Name | RetentionContest/Name | Contest/Name | Locality/Name | Precinct/Name | Source/Name | City | Region | Source/VipId | Checksum/Value | ExternalIdentifier/Value | LocationIdentifier/Value | IsInactive | OtherType | OtherVoteVariation">
         <assert id="HYG-03-err" test="normalize-space(.) != ''">
        [HYG-03] <name/> must not be empty or whitespace-only.
      </assert>
      </rule>
  </pattern>

  <pattern id="hygiene-warnings-elements">
    

      <rule context="Abbreviation | County | Country | WorldRegion | PostalCode | LocationName | FirstName | LastName | MiddleName | Nickname | Gender | Prefix | Suffix | Precinct/Number | PrecinctSplitName | Ward | LatLng/Source | AddressDirection | HouseNumberPrefix | HouseNumberSuffix | StreetDirection | StreetName | StreetSuffix | UnitNumber">
         <assert id="HYG-03-warn-elem" role="warning" test="normalize-space(.) != ''">
        [HYG-03] Optional string element <name/> should not be empty or whitespace-only when present.
      </assert>
      </rule>
  </pattern>

  <pattern id="hygiene-warnings-postalcode">
      <rule context="MailingAddress/PostalCode | PhysicalAddress/PostalCode | AddressStructured/PostalCode | StreetSegment/PostalCode">
         <let name="hasUS"
              value="upper-case(normalize-space(../Country)) = ('US', 'USA', 'UNITED STATES')"/>
         <let name="noCountryUSState"
              value="not(exists(../Country)) and upper-case(normalize-space(../Region)) = $usStatesAndTerritories"/>
         <assert id="HYG-04" role="warning"
                 test="if ($hasUS or $noCountryUSState)                     then matches(normalize-space(.), $usZipRe)                     else true()">
        [HYG-04] US PostalCode ('<value-of select="normalize-space(.)"/>') should be 5 digits or ZIP+4 (12345 or 12345-6789).
      </assert>
      </rule>
  </pattern>

  <pattern id="hygiene-warnings-attrs">
      <rule context="*[@label or @provider]">
         <assert id="HYG-03-warn-label" role="warning"
                 test="not(exists(@label)) or normalize-space(@label) != ''">
        [HYG-03] @label attribute on <name/> should not be empty or whitespace-only.
      </assert>
         <assert id="HYG-03-warn-provider" role="warning"
                 test="not(exists(@provider)) or normalize-space(@provider) != ''">
        [HYG-03] @provider attribute on <name/> should not be empty or whitespace-only.
      </assert>
      </rule>
  </pattern>

</schema>