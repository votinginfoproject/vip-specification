.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-source:

Source
======

The Source object represents the organization publishing the information. In a VIP 7.0 main feed file, exactly one Source object must be present. Source is excluded from feed overlays.

+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=========================================+==============+==============+==========================================+==========================================+
| DateTime               | ``xs:dateTime``                         | **Required** | Single       | Specifies the date and time of feed      | If the field is invalid, then the        |
|                        |                                         |              |              | production in local time.                | implementation is required to ignore the |
|                        |                                         |              |              |                                          | ``Source`` element containing it.        |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Describes the organization and the data  | If the element is invalid or not         |
|                        |                                         |              |              | contained in the feed.                   | present, then the implementation is      |
|                        |                                         |              |              |                                          | required to ignore it.                   |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactInformation | :ref:`multi-xml-contact-information`    | Optional     | Single       | Contact information for inquiries about  | If the element is invalid or not         |
|                        |                                         |              |              | the feed data.                           | present, then the implementation is      |
|                        |                                         |              |              |                                          | required to ignore it.                   |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                   | ``xs:string``                           | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                        |                                         |              |              | publishing the feed.                     | implementation is required to ignore the |
|                        |                                         |              |              |                                          | ``Source`` element containing it.        |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri        | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Web address of the organization          | If the element is invalid or not         |
|                        |                                         |              |              | publishing the feed.                     | present, then the implementation is      |
|                        |                                         |              |              |                                          | required to ignore it.                   |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TermsOfUseUri          | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Web address where Terms of Use for the   | If the element is invalid or not         |
|                        |                                         |              |              | feed data can be found.                  | present, then the implementation is      |
|                        |                                         |              |              |                                          | required to ignore it.                   |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId                  | ``xs:string``                           | **Required** | Single       | FIPS code identifying the state or       | If the field is invalid, then the        |
|                        |                                         |              |              | jurisdiction.                            | implementation is required to ignore the |
|                        |                                         |              |              |                                          | ``Source`` element containing it.        |
+------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _FIPS: https://www.census.gov/geo/reference/codes/cou.html

.. code-block:: xml
   :linenos:

   <Source id="src1">
      <DateTime>2024-10-24T14:25:28</DateTime>
      <Description>
         <Text language="en">SBE is the official source for Virginia election data.</Text>
      </Description>
      <FeedContactInformation>
         <Name>State Board of Elections Support</Name>
         <Email>elections@sbe.virginia.gov</Email>
      </FeedContactInformation>
      <Name>State Board of Elections, Commonwealth of Virginia</Name>
      <OrganizationUri>http://www.sbe.virginia.gov/</OrganizationUri>
      <TermsOfUseUri>http://www.sbe.virginia.gov/terms</TermsOfUseUri>
      <VipId>51</VipId>
   </Source>
