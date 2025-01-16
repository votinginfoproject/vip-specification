.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-source:

source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=================+==============+==============+==========================================+==========================================+
| name                        | ``xs:string``   | **Required** | Single       | Specifies the name of the organization   |                                          |
|                             |                 |              |              | that is providing the information.       |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vip_id                      | ``xs:string``   | **Required** | Single       | Specifies the ID of the organization.    |                                          |
|                             |                 |              |              | VIP uses FIPS_ codes for this ID.        |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_time                   | ``xs:dateTime`` | **Required** | Single       | Specifies the date and time of the feed  |                                          |
|                             |                 |              |              | production. The date/time is considered  |                                          |
|                             |                 |              |              | to be in the timezone local to the       |                                          |
|                             |                 |              |              | organization.                            |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description                 | ``xs:string``   | Optional     | Single       | Specifies both the nature of the         |                                          |
|                             |                 |              |              | organization providing the data and what |                                          |
|                             |                 |              |              | data is in the feed.                     |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| organization_uri            | ``xs:string``   | Optional     | Single       | Specifies a URI to the home page of the  |                                          |
|                             |                 |              |              | organization publishing the data.        |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feed_contact_information_id | ``xs:IDREF``    | Optional     | Single       | Reference to the :ref:`multi-csv-person` |                                          |
|                             |                 |              |              | who will respond to inquiries about the  |                                          |
|                             |                 |              |              | information contained within the file.   |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| terms_of_use_uri            | ``xs:anyURI``   | Optional     | Single       | Specifies the website where the Terms of |                                          |
|                             |                 |              |              | Use for the information in this file can |                                          |
|                             |                 |              |              | be found.                                |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| version                     | ``xs:string``   | Optional     | Single       | Specifies the version of the data        |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date_time,description,name,organization_uri,terms_of_use_uri,vip_id,version
    source01,2016-06-02T10:24:08,SBE is the official source for Virginia data,"State Board of Elections, Commonwealth of Virginia",http://www.sbe.virginia.gov/,http://example.com/terms,51,5.1
