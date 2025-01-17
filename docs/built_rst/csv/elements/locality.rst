.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-locality:

locality
========

The Locality object represents the jurisdiction below the :ref:`multi-csv-state` (e.g. county).

+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=======================================+==============+==============+==========================================+==========================================+
| election_administration_id | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                  |                                          |
|                            |                                       |              |              | :ref:`multi-csv-election-administration` |                                          |
|                            |                                       |              |              | object.                                  |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers       | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Another identifier for a locality that   |                                          |
|                            |                                       |              |              | links to another dataset (e.g.           |                                          |
|                            |                                       |              |              | `OCD-ID`_)                               |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only               | ``xs:boolean``                        | Optional     | Single       | Determines if the locality runs          | If the field is missing or invalid, the  |
|                            |                                       |              |              | mail-only elections. If this is true,    | implementation is required to assume     |
|                            |                                       |              |              | then all precincts a part of the         | `IsMailOnly` is false.                   |
|                            |                                       |              |              | locality will also run mail-only         |                                          |
|                            |                                       |              |              | elections. Drop boxes may be used in     |                                          |
|                            |                                       |              |              | addition to this flag using a            |                                          |
|                            |                                       |              |              | :ref:`polling location                   |                                          |
|                            |                                       |              |              | <multi-csv-polling-location>` record     |                                          |
|                            |                                       |              |              | configured as a Drop Box.                |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                       | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to a set of the         |                                          |
|                            |                                       |              |              | locality's :ref:`polling locations       |                                          |
|                            |                                       |              |              | <multi-csv-polling-location>`s. If early |                                          |
|                            |                                       |              |              | vote centers or ballot drop locations    |                                          |
|                            |                                       |              |              | are locality-wide, they should be        |                                          |
|                            |                                       |              |              | specified here.                          |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state_id                   | ``xs:IDREF``                          | **Required** | Single       | References the locality's                |                                          |
|                            |                                       |              |              | :ref:`multi-csv-state`.                  |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                       | :ref:`multi-csv-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.       |                                          |
|                            |                                       |              |              | county, town, et al.), which is one of   |                                          |
|                            |                                       |              |              | the various :ref:`DistrictType           |                                          |
|                            |                                       |              |              | enumerations <multi-csv-district-type>`. |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                 | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality   |                                          |
|                            |                                       |              |              | that falls outside the options listed in |                                          |
|                            |                                       |              |              | :ref:`DistrictType                       |                                          |
|                            |                                       |              |              | <multi-csv-district-type>`.              |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_administration_id,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,name,polling_location_ids,state_id,type,other_type
    loc001,ea123,ocd-id,,ocd-division/country:us/state:co/county:denver,true,Locality #1,poll001 poll002,st51,city,
    loc002,ea345,,,,,Locality #2,,st51,other,unique type
