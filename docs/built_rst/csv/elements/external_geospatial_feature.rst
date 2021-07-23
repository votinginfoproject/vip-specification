.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-external-geospatial-feature:

external_geospatial_feature
===========================

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+====================================+==============+==============+==========================================+==========================================+
| external_file_id  | ``xs:IDREF``                       | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                    |              |              | :ref:`multi-csv-external-file`           | implementation is required to ignore the |
|                   |                                    |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                    |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_format       | :ref:`multi-csv-geospatial-format` | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                    |              |              |                                          | implementation is required to ignore the |
|                   |                                    |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                    |              |              |                                          | containing it.                           |
+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| shape_identifiers | ``xs:string``                      | **Required** | Repeats      | Identifiers indicating which specific    | If the field is invalid, then the        |
|                   |                                    |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                   |                                    |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                   |                                    |              |              | the referenced external file. This is a  | containing it.                           |
|                   |                                    |              |              | repeated field in the XML specification, |                                          |
|                   |                                    |              |              | but a scalar field in the CSV            |                                          |
|                   |                                    |              |              | specification. If more than one          |                                          |
|                   |                                    |              |              | identifier is required with the CSV      |                                          |
|                   |                                    |              |              | specifiation, multiple values can be     |                                          |
|                   |                                    |              |              | provided by delimited by the pipe symbol |                                          |
|                   |                                    |              |              | (|).                                     |                                          |
+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,external_file_id,file_format,shape_identifiers
    egf1,ef1,shp,0|7|9
