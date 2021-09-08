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
| spatial_boundary_id    | ``xs:IDREF``                          | Optional     | Single       | Defines the spatial boundary of the      | If the element is invalid or not         |
|                        |                                       |              |              | precinct. All voter addresses contained  | present, then the implementation is      |
|                        |                                       |              |              | within this boundary are assigned to the | required to ignore it.                   |
|                        |                                       |              |              | precinct. If a voter address also maps   |                                          |
|                        |                                       |              |              | to a :doc:`StreetSegment                 |                                          |
|                        |                                       |              |              | <street_segment>`, then the precinct     |                                          |
|                        |                                       |              |              | assignment from the StreetSegment will   |                                          |
|                        |                                       |              |              | be preferred over the assignment from    |                                          |
|                        |                                       |              |              | the spatial boundary.                    |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ward                   | ``xs:string``                         | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                        |                                       |              |              | contained within.                        | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_style_id,electoral_district_ids,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,locality_id,name,number,polling_location_ids,precinct_split_name,spatial_boundary_id,ward
    pre90111,bs00010,ed001,ocd-id,,ocd-division/country:us,false,loc001,203 - GEORGETOWN,0203,poll001 poll002,split13,sb1,,5
    pre90112,bs00011,ed002,fips,,42,false,loc001,203 - GEORGETOWN,0203,poll003,split26,,6
    pre90113,bs00010,ed003,,,,false,loc002,203 - GEORGETOWN,0203,poll004,split54,sb1,7


.. _multi-csv-spatial-boundary:

spatial_boundary
----------------

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+--------------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                            | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+================================+==============+==============+==============+==========================================+==========================================+
| external_geospatial_feature_id | ``xs:IDREF`` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                                |              |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                                |              |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                                |              |              |              |                                          | it.                                      |
+--------------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,external_geospatial_feature_id
    sb1,egf1


.. _multi-csv-external-geospatial-feature:

external_geospatial_feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+---------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+====================================+==============+==============+==========================================+==========================================+
| external_file_id    | ``xs:IDREF``                       | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                     |                                    |              |              | :ref:`multi-csv-external-file`           | implementation is required to ignore the |
|                     |                                    |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                     |                                    |              |              | define the feature's boundary.           | containing it.                           |
+---------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_format         | :ref:`multi-csv-geospatial-format` | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                     |                                    |              |              |                                          | implementation is required to ignore the |
|                     |                                    |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                     |                                    |              |              |                                          | containing it.                           |
+---------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feature_identifiers | ``xs:string``                      | **Required** | Single       | Identifing attributes indicating which   | If the element is invalid, then the      |
|                     |                                    |              |              | specific shape(s) to use from the        | implementation is required to ignore the |
|                     |                                    |              |              | geospatial file. These refer to          | ``ExternalGeospatialFeature`` element    |
|                     |                                    |              |              | identifiers within the referenced        | containing it.                           |
|                     |                                    |              |              | external file.                           |                                          |
+---------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,external_file_id,file_format,shape_identifiers
    egf1,ef1,shp,0 7 9


.. _multi-csv-feature-attribute:

feature_attribute
^^^^^^^^^^^^^^^^^

The description for FeatureAttribute

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| name         | ``xs:string`` | **Required** | Repeats      | This field should list the appropriate   | If the field is invalid, then the        |
|              |               |              |              | column header from the geospatial        | implementation is required to ignore the |
|              |               |              |              | attribute table.                         | ``FeatureAttribute`` element containing  |
|              |               |              |              |                                          | it.                                      |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string`` | **Required** | Repeats      | This field should list the appropriate   | If the field is invalid, then the        |
|              |               |              |              | value from the geospatial attribute      | implementation is required to ignore the |
|              |               |              |              | table, per the column header name.       | ``FeatureAttribute`` element containing  |
|              |               |              |              |                                          | it.                                      |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
