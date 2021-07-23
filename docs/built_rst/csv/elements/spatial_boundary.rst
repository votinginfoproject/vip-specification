.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-spatial-boundary:

spatial_boundary
================

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
