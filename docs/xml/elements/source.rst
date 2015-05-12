Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+----------------+---------------------+-----------------+------------------+----------------+
|Tag             |Data                 |Optional/Required|Description       |Error           |
|                |Type                 |                 |                  |Handling        |
+================+=====================+=================+==================+================+
|Name            |String               |Required         |The name          |If the name     |
|                |                     |                 |field             |field is        |
|                |                     |                 |specifies         |invalid, the    |
|                |                     |                 |the name of       |implementation  |
|                |                     |                 |the               |is required to  |
|                |                     |                 |organization      |ignore the      |
|                |                     |                 |that is           |source element  |
|                |                     |                 |providing         |containing it.  |
|                |                     |                 |the               |                |
|                |                     |                 |information.      |                |
+----------------+---------------------+-----------------+------------------+----------------+
|VipId           |String               |Required         |The VipId         |If the VipId    |
|                |                     |                 |field             |field is        |
|                |                     |                 |specifies the     |invalid, the    |
|                |                     |                 |ID of the         |implementation  |
|                |                     |                 |organization      |is required to  |
|                |                     |                 |as assigned by    |ignore the      |
|                |                     |                 |VIP. This ID      |source element  |
|                |                     |                 |is not an         |containing it.  |
|                |                     |                 |attribute so      |                |
|                |                     |                 |as not to         |                |
|                |                     |                 |interfere with    |                |
|                |                     |                 |organizations'    |                |
|                |                     |                 |own numbering     |                |
|                |                     |                 |conventions       |                |
|                |                     |                 |(since id         |                |
|                |                     |                 |attributes        |                |
|                |                     |                 |must be unique    |                |
|                |                     |                 |across the        |                |
|                |                     |                 |entire file).     |                |
+----------------+---------------------+-----------------+------------------+----------------+
|DateTime        |DateTime             |Required         |The DateTime field|If the          |
|                |                     |                 |specifies the date|DateTime field  |
|                |                     |                 |and time of the   |is not present  |
|                |                     |                 |feed              |or invalid,     |
|                |                     |                 |production. The   |the             |
|                |                     |                 |date/time is      |implementation  |
|                |                     |                 |considered to be  |is required to  |
|                |                     |                 |in the timezone   |ignore the      |
|                |                     |                 |local to the      |source element  |
|                |                     |                 |organization. This|containing it.  |
|                |                     |                 |datetime is       |                |
|                |                     |                 |required to match |                |
|                |                     |                 |the datetime      |                |
|                |                     |                 |specified in the  |                |
|                |                     |                 |feed's filename.  |                |
+----------------+---------------------+-----------------+------------------+----------------+
|Description     |InternationalizedText|Optional         |The Description   |If the          |
|                |                     |                 |specifies both the|description is  |
|                |                     |                 |nature of the     |invalid, the    |
|                |                     |                 |organization      |implementation  |
|                |                     |                 |providing the data|is required to  |
|                |                     |                 |and what data is  |ignore it.      |
|                |                     |                 |in the feed.      |                |
+----------------+---------------------+-----------------+------------------+----------------+
|OrganizationUrl |String               |Optional         |The               |If the          |
|                |                     |                 |OrganizationUrl   |OrganizationUrl | 
|                |                     |                 |field contains a  |field is        |
|                |                     |                 |URL to the home   |invalid, the    |
|                |                     |                 |page of the       |implementation  |
|                |                     |                 |organization      |is required to  |
|                |                     |                 |publishing the    |ignore it.      |
|                |                     |                 |data.             |                |
+----------------+---------------------+-----------------+------------------+----------------+
|FeedContactId   |IDREF                |Optional         |The FeedContactId |If the          |
|                |                     |                 |is a reference to |FeedContactId   |
|                |                     |                 |(an election      |field is        |
|                |                     |                 |official object)  |invalid, the    |
|                |                     |                 |the person who    |implementation  |
|                |                     |                 |will respond to   |is required to  |
|                |                     |                 |inquiries about   |ignore it.      |
|                |                     |                 |the information   |                |
|                |                     |                 |contained within  |                |
|                |                     |                 |the file.         |                |
+----------------+---------------------+-----------------+------------------+----------------+
|TouUrl          |anyURI               |Optional         |The tou_url is the|If the TouUrl   |
|                |                     |                 |website where the |field is        |
|                |                     |                 |Terms of Use for  |invalid, the    |
|                |                     |                 |the information in|implementation  |
|                |                     |                 |this file can be  |is required to  |
|                |                     |                 |found.            |ignore it.      |
+----------------+---------------------+-----------------+------------------+----------------+

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

