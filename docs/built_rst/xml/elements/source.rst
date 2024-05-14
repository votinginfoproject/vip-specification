.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-source:

Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=========================================+==============+==============+==========================================+==========================================+
| Name                   | ``xs:string``                           | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                        |                                         |              |              | that is providing the information.       | implementation is required to ignore the |
|                        |                                         |              |              |                                          | ``Source`` element containing it.        |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId                  | ``xs:string``                           | **Required** | Single       | Specifies the ID of the organization.    | If the field is invalid, then the        |
|                        |                                         |              |              | VIP uses FIPS_ codes for this ID.        | implementation is required to ignore the |
|                        |                                         |              |              |                                          | ``Source`` element containing it.        |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateTime               | ``xs:dateTime``                         | **Required** | Single       | Specifies the date and time of the feed  | If the field is invalid, then the        |
|                        |                                         |              |              | production. The date/time is considered  | implementation is required to ignore the |
|                        |                                         |              |              | to be in the timezone local to the       | ``Source`` element containing it.        |
|                        |                                         |              |              | organization.                            |                                          |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                        |                                         |              |              | organization providing the data and what | present, then the implementation is      |
|                        |                                         |              |              | data is in the feed.                     | required to ignore it.                   |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri        | ``xs:string``                           | Optional     | Single       | Specifies a URI to the home page of the  | If the field is invalid or not present,  |
|                        |                                         |              |              | organization publishing the data.        | then the implementation is required to   |
|                        |                                         |              |              |                                          | ignore it.                               |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactInformation | :ref:`multi-xml-contact-information`    | Optional     | Single       | Reference to the :ref:`multi-xml-person` | If the element is invalid or not         |
|                        |                                         |              |              | who will respond to inquiries about the  | present, then the implementation is      |
|                        |                                         |              |              | information contained within the file.   | required to ignore it.                   |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TouUri                 | ``xs:anyURI``                           | Optional     | Single       | Specifies the website where the Terms of | If the field is invalid or not present,  |
|                        |                                         |              |              | Use for the information in this file can | then the implementation is required to   |
|                        |                                         |              |              | be found.                                | ignore it.                               |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Version                | ``xs:string``                           | Optional     | Single       | Specifies the version of the data        | If the field is invalid or not present,  |
|                        |                                         |              |              |                                          | then the implementation is required to   |
|                        |                                         |              |              |                                          | ignore it.                               |
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
