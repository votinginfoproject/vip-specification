.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-locality:

locality
========

The Locality object represents the jurisdiction below the :ref:`multi-csv-state` (e.g. county).

+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=======================================+==============+==============+==========================================+==========================================+
| election_administration_id | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                  | If the field is invalid or not present,  |
|                            |                                       |              |              | :ref:`multi-csv-election-administration` | then the implementation is required to   |
|                            |                                       |              |              | object.                                  | ignore it.                               |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers       | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Another identifier for a locality that   | If the element is invalid or not         |
|                            |                                       |              |              | links to another dataset (e.g.           | present, then the implementation is      |
|                            |                                       |              |              | `OCD-ID`_)                               | required to ignore it.                   |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
<<<<<<< HEAD
| name                       | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        | If the field is invalid, then the        |
|                            |                                       |              |              |                                          | implementation is required to ignore the |
|                            |                                       |              |              |                                          | ``Locality`` element containing it.      |
=======
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
| name                       | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        | If the field is not present or invalid,  |
|                            |                                       |              |              |                                          | the implementation is required to ignore |
|                            |                                       |              |              |                                          | the Locality element containing it.      |
>>>>>>> 191cfa7... Updating RST files, adding IsMailOnly field to Locality
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to a set of the         | If the field is invalid or not present,  |
|                            |                                       |              |              | locality's :ref:`polling locations       | the implementation is required to ignore |
|                            |                                       |              |              | <multi-csv-polling-location>`s. If early | it. However, the implementation should   |
|                            |                                       |              |              | vote centers or ballot drop locations    | still check to see if there are any      |
|                            |                                       |              |              | are locality-wide, they should be        | polling locations associated with this   |
|                            |                                       |              |              | specified here.                          | locality's state.                        |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state_id                   | ``xs:IDREF``                          | **Required** | Single       | References the locality's                | If the field is invalid, then the        |
|                            |                                       |              |              | :ref:`multi-csv-state`.                  | implementation is required to ignore the |
|                            |                                       |              |              |                                          | ``Locality`` element containing it.      |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                       | :ref:`multi-csv-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                            |                                       |              |              | county, town, et al.), which is one of   | then the implementation is required to   |
|                            |                                       |              |              | the various :ref:`DistrictType           | ignore it.                               |
|                            |                                       |              |              | enumerations <multi-csv-district-type>`. |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                 | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality   | If the field is invalid or not present,  |
|                            |                                       |              |              | that falls outside the options listed in | then the implementation is required to   |
|                            |                                       |              |              | :ref:`DistrictType                       | ignore it.                               |
|                            |                                       |              |              | <multi-csv-district-type>`.              |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_administration_id,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,name,polling_location_ids,state_id,type,other_type
    loc001,ea123,ocd-id,,ocd-division/country:us/state:co/county:denver,true,Locality #1,poll001 poll002,st51,city,
    loc002,ea345,,,,,Locality #2,,st51,other,unique type
