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

Voters can be assigned to a precinct in two ways. A voter location modeled by :doc:`StreetSegment <street_segment>`
is assigned to a precinct by :doc:`StreetSegment.PrecinctId <street_segment>`.
Alternatively, a precinct's spatial boundary can be modeled with :doc:`Precinct.SpatialBoundary  <precinct>`.
Any registered voter address contained within the spatial boundary of the precinct
is assigned to that precinct.

+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=======================================+==============+==============+==========================================+==========================================+
| ballot_style_id        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             |                                          |
|                        |                                       |              |              | :ref:`multi-csv-ballot-style`, which a   |                                          |
|                        |                                       |              |              | person who lives in this precinct will   |                                          |
|                        |                                       |              |              | vote.                                    |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_ids | ``xs:IDREFS``                         | Optional     | Single       | Links to the                             |                                          |
|                        |                                       |              |              | :ref:`multi-csv-electoral-district`s     |                                          |
|                        |                                       |              |              | (e.g., congressional district, state     |                                          |
|                        |                                       |              |              | house district, school board district)   |                                          |
|                        |                                       |              |              | to which the entire precinct/precinct    |                                          |
|                        |                                       |              |              | split belongs. **Highly Recommended** if |                                          |
|                        |                                       |              |              | candidate information is to be provided. |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers   | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Other identifier for the precinct that   |                                          |
|                        |                                       |              |              | relates to another dataset (e.g.         |                                          |
|                        |                                       |              |              | `OCD-ID`_).                              |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only           | ``xs:boolean``                        | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                        |                                       |              |              | mail-only elections.                     | implementation is required to assume     |
|                        |                                       |              |              |                                          | `IsMailOnly` is false.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| locality_id            | ``xs:IDREF``                          | **Required** | Single       | Links to the :ref:`multi-csv-locality`   |                                          |
|                        |                                       |              |              | that comprises the precinct.             |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                   | ``xs:string``                         | **Required** | Single       | Specifies the precinct's name (or number |                                          |
|                        |                                       |              |              | if no name exists).                      |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number                 | ``xs:string``                         | Optional     | Single       | Specifies the precinct's number (e.g.,   |                                          |
|                        |                                       |              |              | 32 or 32A -- alpha characters are        |                                          |
|                        |                                       |              |              | legal). Should be used if the `Name`     |                                          |
|                        |                                       |              |              | field is populated by a name and not a   |                                          |
|                        |                                       |              |              | number.                                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids   | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the precinct's       |                                          |
|                        |                                       |              |              | :ref:`multi-csv-polling-location`        |                                          |
|                        |                                       |              |              | object(s).                               |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_split_name    | ``xs:string``                         | Optional     | Single       | If this field is empty, then this        |                                          |
|                        |                                       |              |              | `Precinct` object represents a full      |                                          |
|                        |                                       |              |              | precinct. If this field is present, then |                                          |
|                        |                                       |              |              | this `Precinct` object represents one    |                                          |
|                        |                                       |              |              | portion of a split precinct. Each        |                                          |
|                        |                                       |              |              | `Precinct` object that represents one    |                                          |
|                        |                                       |              |              | portion of a split precinct **must**     |                                          |
|                        |                                       |              |              | have the same `Name` value, but          |                                          |
|                        |                                       |              |              | different `PrecinctSplitName` values.    |                                          |
|                        |                                       |              |              | See the `sample_feed.xml` file for       |                                          |
|                        |                                       |              |              | examples.                                |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| spatial_boundary_id    | ``xs:IDREF``                          | Optional     | Single       | Defines the spatial boundary of the      |                                          |
|                        |                                       |              |              | precinct. All voter addresses contained  |                                          |
|                        |                                       |              |              | within this boundary are assigned to the |                                          |
|                        |                                       |              |              | precinct. If a voter address also maps   |                                          |
|                        |                                       |              |              | to a :doc:`StreetSegment                 |                                          |
|                        |                                       |              |              | <street_segment>`, then the precinct     |                                          |
|                        |                                       |              |              | assignment from the StreetSegment will   |                                          |
|                        |                                       |              |              | be preferred over the assignment from    |                                          |
|                        |                                       |              |              | the spatial boundary.                    |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ward                   | ``xs:string``                         | Optional     | Single       | Specifies the ward the precinct is       |                                          |
|                        |                                       |              |              | contained within.                        |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_style_id,electoral_district_ids,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,locality_id,name,number,polling_location_ids,precinct_split_name,spatial_boundary_id,ward
    pre90111,bs00010,ed001,ocd-id,,ocd-division/country:us,false,loc001,203 - GEORGETOWN,0203,poll001 poll002,split13,sb1,,5
    pre90112,bs00011,ed002,fips,,42,false,loc001,203 - GEORGETOWN,0203,poll003,split26,,6
    pre90113,bs00010,ed003,,,,false,loc002,203 - GEORGETOWN,0203,poll004,split54,sb1,7
