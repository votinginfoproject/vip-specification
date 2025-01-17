.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-source:

Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=========================================+==============+==============+==========================================+==========================================+
| Name                   | ``xs:string``                           | **Required** | Single       | Specifies the name of the organization   |                                          |
|                        |                                         |              |              | that is providing the information.       |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId                  | ``xs:string``                           | **Required** | Single       | Specifies the ID of the organization.    |                                          |
|                        |                                         |              |              | VIP uses FIPS_ codes for this ID.        |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateTime               | ``xs:dateTime``                         | **Required** | Single       | Specifies the date and time of the feed  |                                          |
|                        |                                         |              |              | production. The date/time is considered  |                                          |
|                        |                                         |              |              | to be in the timezone local to the       |                                          |
|                        |                                         |              |              | organization.                            |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies both the nature of the         |                                          |
|                        |                                         |              |              | organization providing the data and what |                                          |
|                        |                                         |              |              | data is in the feed.                     |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri        | ``xs:string``                           | Optional     | Single       | Specifies a URI to the home page of the  |                                          |
|                        |                                         |              |              | organization publishing the data.        |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactInformation | :ref:`multi-xml-contact-information`    | Optional     | Single       | Reference to the :ref:`multi-xml-person` |                                          |
|                        |                                         |              |              | who will respond to inquiries about the  |                                          |
|                        |                                         |              |              | information contained within the file.   |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TouUri                 | ``xs:anyURI``                           | Optional     | Single       | Specifies the website where the Terms of |                                          |
|                        |                                         |              |              | Use for the information in this file can |                                          |
|                        |                                         |              |              | be found.                                |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Version                | ``xs:string``                           | Optional     | Single       | Specifies the version of the data        |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _FIPS: https://www.census.gov/geo/reference/codes/cou.html

.. code-block:: xml
   :linenos:

   <Source id="src1">
      <DateTime>2013-10-24T14:25:28</DateTime>
      <Description>
         <Text language="en">SBE is the official source for Virginia data</Text>
      </Description>
      <Name>State Board of Elections, Commonwealth of Virginia</Name>
      <OrganizationUri>http://www.sbe.virginia.gov/</OrganizationUri>
      <VipId>51</VipId>
      <Version>5.0</Version>
   </Source>
