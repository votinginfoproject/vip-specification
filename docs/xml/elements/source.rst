Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

.. include:: ../../tables/elements/source.rst

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
