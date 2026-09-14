.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-source:

source
======

The Source object represents the organization publishing the information. In a VIP 7.0 main feed file, exactly one Source object must be present. Source is excluded from feed overlays.

+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=========================================+==============+==============+==========================================+==========================================+
| date_time                   | ``xs:dateTime``                         | **Required** | Single       | Specifies the date and time of feed      | If the field is invalid, then the        |
|                             |                                         |              |              | production (e.g. "2024-11-05T08:30:00"). | implementation is required to ignore the |
|                             |                                         |              |              | Considered to be in the timezone local   | ``Source`` element containing it.        |
|                             |                                         |              |              | to the organization.                     |                                          |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description                 | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                             |                                         |              |              | organization providing the data and what | present, then the implementation is      |
|                             |                                         |              |              | data is in the feed (e.g. "Virginia      | required to ignore it.                   |
|                             |                                         |              |              | Department of Elections official         |                                          |
|                             |                                         |              |              | candidate and polling location feed for  |                                          |
|                             |                                         |              |              | the 2024 General Election").             |                                          |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feed_contact_information_id | :ref:`multi-csv-contact-information`    | Optional     | Single       | Contact information for inquiries about  | If the element is invalid or not         |
|                             |                                         |              |              | the feed data.                           | present, then the implementation is      |
|                             |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                        | ``xs:string``                           | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                             |                                         |              |              | publishing the feed.                     | implementation is required to ignore the |
|                             |                                         |              |              |                                          | ``Source`` element containing it.        |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| organization_uri            | :ref:`multi-csv-internationalized-uri`  | Optional     | Single       | Web address of the organization          | If the element is invalid or not         |
|                             |                                         |              |              | publishing the feed.                     | present, then the implementation is      |
|                             |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| terms_of_use_uri            | :ref:`multi-csv-internationalized-uri`  | Optional     | Single       | Web address where Terms of Use for the   | If the element is invalid or not         |
|                             |                                         |              |              | feed data can be found.                  | present, then the implementation is      |
|                             |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vip_id                      | ``xs:string``                           | **Required** | Single       | Specifies the ID of the organization     | If the field is invalid, then the        |
|                             |                                         |              |              | publishing the feed. VIP uses FIPS codes | implementation is required to ignore the |
|                             |                                         |              |              | for this ID (e.g. "51" for Virginia).    | ``Source`` element containing it.        |
+-----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,date_time,description,name,organization_uri,terms_of_use_uri,vip_id
    source01,2024-10-24T14:25:28,SBE is official source,"State Board of Elections",http://www.sbe.virginia.gov/,http://example.com/terms,51
