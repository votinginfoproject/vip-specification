Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|Tag             |Data Type                  |Required?        |Repeats?             |Description          |Error           |
|                |                           |                 |                     |                     |Handling        |
+================+===========================+=================+=====================+=====================+================+
|Name            |xs:string                  |**Required**     |Single               |Specifies the name of|If the field is |
|                |                           |                 |                     |the organization that|invalid, the    |
|                |                           |                 |                     |is providing the     |implementation  |
|                |                           |                 |                     |information.         |is required to  |
|                |                           |                 |                     |                     |ignore the      |
|                |                           |                 |                     |                     |source element  |
|                |                           |                 |                     |                     |containing it.  |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|VipId           |xs:string                  |**Required**     |Single               |Specifies the ID of  |If the field is |
|                |                           |                 |                     |the organization as  |invalid, the    |
|                |                           |                 |                     |assigned by VIP. This|implementation  |
|                |                           |                 |                     |ID is not an         |is required to  |
|                |                           |                 |                     |attribute so as not  |ignore the      |
|                |                           |                 |                     |to interfere with    |source element  |
|                |                           |                 |                     |organizations' own   |containing it.  |
|                |                           |                 |                     |numbering conventions|                |
|                |                           |                 |                     |(since id attributes |                |
|                |                           |                 |                     |must be unique across|                |
|                |                           |                 |                     |the entire file).    |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|DateTime        |xs:dateTime                |**Required**     |Single               |Specifies the date   |If the field is |
|                |                           |                 |                     |and time of the feed |not present or  |
|                |                           |                 |                     |production. The      |invalid, the    |
|                |                           |                 |                     |date/time is         |implementation  |
|                |                           |                 |                     |considered to be in  |is required to  |
|                |                           |                 |                     |the timezone local to|ignore the      |
|                |                           |                 |                     |the                  |element         |
|                |                           |                 |                     |organization. This   |containing it.  |
|                |                           |                 |                     |datetime is required |                |
|                |                           |                 |                     |to match the datetime|                |
|                |                           |                 |                     |specified in the     |                |
|                |                           |                 |                     |feed's filename.     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|Description     |:doc:`InternationalizedText|Optional         |Single               |Specifies both the   |If the field is |
|                |<internationalized_text>`  |                 |                     |nature of the        |invalid, the    |
|                |                           |                 |                     |organization         |implementation  |
|                |                           |                 |                     |providing the data   |is required to  |
|                |                           |                 |                     |and what data is in  |ignore it.      |
|                |                           |                 |                     |the feed.            |                |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|OrganizationUri |xs:string                  |Optional         |Single               |Specifies a URI to   |If the field is |
|                |                           |                 |                     |the home page of the |invalid or not  | 
|                |                           |                 |                     |organization         |present, the    |
|                |                           |                 |                     |publishing the data. |implementation  |
|                |                           |                 |                     |                     |is required to  |
|                |                           |                 |                     |                     |ignore it.      |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|FeedContactId   |xs:IDREF                   |Optional         |Single               |Reference to the     |If the field is |
|                |                           |                 |                     |:doc:`person         |invalid or not  |
|                |                           |                 |                     |<person>` who will   |present, the    |
|                |                           |                 |                     |respond to inquiries |implementation  |
|                |                           |                 |                     |about the information|is required to  |
|                |                           |                 |                     |contained within the |ignore it.      |
|                |                           |                 |                     |file.                |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+
|TouUri          |xs:anyURI                  |Optional         |Single               |Specifies the website|If the field is |
|                |                           |                 |                     |where the Terms of   |invalid, the    |
|                |                           |                 |                     |Use for the          |implementation  |
|                |                           |                 |                     |information in this  |is required to  |
|                |                           |                 |                     |file can be found.   |ignore it.      |
|                |                           |                 |                     |                     |                |
+----------------+---------------------------+-----------------+---------------------+---------------------+----------------+

.. code-block:: xml
   :linenos:
   
   <source id="1">
      <name>State of Alabama</name>
      <vip_id></vip_id>
      <datetime>2008-06-05T15:45:10</datetime>
      <description>The State of Alabama is the official source of election information in Alabama. This feed provides information on election dates, districts, offices, candidates, and precinct boundaries.</description>
      <organization_url>http://www.sos.state.al.us/Elections</organization_url>
      <feed_contact_id>1555122</feed_contact_id>
      <tou_url>http://www.sos.state.al.us/vipFeed/terms_of_use.html</tou_url>
   </source>
