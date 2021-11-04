.. This file is auto-generated.  Do not edit it by hand!

+----------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                                    | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+==============================================+==============+==============+==========================================+==========================================+
| ExternalGeospatialFeatures | :ref:`multi-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                            |                                              |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                            |                                              |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                            |                                              |              |              |                                          | it.                                      |
+----------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
