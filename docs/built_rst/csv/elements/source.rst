.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-source:

source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=================+==============+==============+==========================================+==========================================+
| name                        | ``xs:string``   | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                             |                 |              |              | that is providing the information.       | implementation is required to ignore the |
|                             |                 |              |              |                                          | ``Source`` element containing it.        |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vip_id                      | ``xs:string``   | **Required** | Single       | Specifies the ID of the organization.    | If the field is invalid, then the        |
|                             |                 |              |              | VIP uses FIPS_ codes for this ID.        | implementation is required to ignore the |
|                             |                 |              |              |                                          | ``Source`` element containing it.        |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_time                   | ``xs:dateTime`` | **Required** | Single       | Specifies the date and time of the feed  | If the field is invalid, then the        |
|                             |                 |              |              | production. The date/time is considered  | implementation is required to ignore the |
|                             |                 |              |              | to be in the timezone local to the       | ``Source`` element containing it.        |
|                             |                 |              |              | organization.                            |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description                 | ``xs:string``   | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                             |                 |              |              | organization providing the data and what | present, then the implementation is      |
|                             |                 |              |              | data is in the feed.                     | required to ignore it.                   |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| organization_uri            | ``xs:string``   | Optional     | Single       | Specifies a URI to the home page of the  | If the field is invalid or not present,  |
|                             |                 |              |              | organization publishing the data.        | then the implementation is required to   |
|                             |                 |              |              |                                          | ignore it.                               |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feed_contact_information_id | ``xs:IDREF``    | Optional     | Single       | Reference to the :ref:`multi-csv-person` | If the element is invalid or not         |
|                             |                 |              |              | who will respond to inquiries about the  | present, then the implementation is      |
|                             |                 |              |              | information contained within the file.   | required to ignore it.                   |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| terms_of_use_uri            | ``xs:anyURI``   | Optional     | Single       | Specifies the website where the Terms of | If the field is invalid or not present,  |
|                             |                 |              |              | Use for the information in this file can | then the implementation is required to   |
|                             |                 |              |              | be found.                                | ignore it.                               |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| version                     | ``xs:string``   | Optional     | Single       | Specifies the version of the data        | If the field is invalid or not present,  |
|                             |                 |              |              |                                          | then the implementation is required to   |
|                             |                 |              |              |                                          | ignore it.                               |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date_time,description,name,organization_uri,terms_of_use_uri,vip_id,version
    source01,2016-06-02T10:24:08,SBE is the official source for Virginia data,"State Board of Elections, Commonwealth of Virginia",http://www.sbe.virginia.gov/,http://example.com/terms,51,5.1
