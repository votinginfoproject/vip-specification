.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-precinct:

precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:ref:`Source.VipId <multi-csv-source>`, :ref:`Locality.Name <multi-csv-locality>`, :ref:`Precinct.Ward <multi-csv-precinct>`,
:ref:`Precinct.Name <multi-csv-precinct>`, and :ref:`Precinct.Number <multi-csv-precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=======================================+==============+==============+==========================================+==========================================+
| ballot_style_id        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                        |                                       |              |              | :ref:`multi-csv-ballot-style`, which a   | then the implementation is required to   |
|                        |                                       |              |              | person who lives in this precinct will   | ignore it.                               |
|                        |                                       |              |              | vote.                                    |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_ids | ``xs:IDREFS``                         | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                        |                                       |              |              | :ref:`multi-csv-electoral-district`s     | then the implementation is required to   |
|                        |                                       |              |              | (e.g., congressional district, state     | ignore it.                               |
|                        |                                       |              |              | house district, school board district)   |                                          |
|                        |                                       |              |              | to which the entire precinct/precinct    |                                          |
|                        |                                       |              |              | split belongs. **Highly Recommended** if |                                          |
|                        |                                       |              |              | candidate information is to be provided. |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers   | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Other identifier for the precinct that   | If the element is invalid or not         |
|                        |                                       |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                        |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only           | ``xs:boolean``                        | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                        |                                       |              |              | mail-only elections.                     | implementation is required to assume     |
|                        |                                       |              |              |                                          | `IsMailOnly` is false.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| locality_id            | ``xs:IDREF``                          | **Required** | Single       | Links to the :ref:`multi-csv-locality`   | If the field is invalid, then the        |
|                        |                                       |              |              | that comprises the precinct.             | implementation is required to ignore the |
|                        |                                       |              |              |                                          | ``Precinct`` element containing it.      |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                   | ``xs:string``                         | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid, then the        |
|                        |                                       |              |              | if no name exists).                      | implementation is required to ignore the |
|                        |                                       |              |              |                                          | ``Precinct`` element containing it.      |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number                 | ``xs:string``                         | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                        |                                       |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                        |                                       |              |              | legal). Should be used if the `Name`     | ignore it.                               |
|                        |                                       |              |              | field is populated by a name and not a   |                                          |
|                        |                                       |              |              | number.                                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids   | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the precinct's       | If the field is invalid or not present,  |
|                        |                                       |              |              | :ref:`multi-csv-polling-location`        | then the implementation is required to   |
|                        |                                       |              |              | object(s).                               | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_split_name    | ``xs:string``                         | Optional     | Single       | If this field is empty, then this        | If the field is invalid or not present,  |
|                        |                                       |              |              | `Precinct` object represents a full      | then the implementation is required to   |
|                        |                                       |              |              | precinct. If this field is present, then | ignore it.                               |
|                        |                                       |              |              | this `Precinct` object represents one    |                                          |
|                        |                                       |              |              | portion of a split precinct. Each        |                                          |
|                        |                                       |              |              | `Precinct` object that represents one    |                                          |
|                        |                                       |              |              | portion of a split precinct **must**     |                                          |
|                        |                                       |              |              | have the same `Name` value, but          |                                          |
|                        |                                       |              |              | different `PrecinctSplitName` values.    |                                          |
|                        |                                       |              |              | See the `sample_feed.xml` file for       |                                          |
|                        |                                       |              |              | examples.                                |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ward                   | ``xs:string``                         | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                        |                                       |              |              | contained within.                        | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_style_id,electoral_district_ids,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,locality_id,name,number,polling_location_ids,precinct_split_name,ward
    pre90111,bs00010,ed001,ocd-id,,ocd-division/country:us,false,loc001,203 - GEORGETOWN,0203,poll001 poll002,split13,5
    pre90112,bs00011,ed002,fips,,42,false,loc001,203 - GEORGETOWN,0203,poll003,split26,6
    pre90113,bs00010,ed003,,,,false,loc002,203 - GEORGETOWN,0203,poll004,split54,7
