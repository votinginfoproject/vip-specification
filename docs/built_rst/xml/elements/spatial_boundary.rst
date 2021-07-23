.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-spatial-boundary:

SpatialBoundary
===============

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                       | Data Type                                    | Required?    | Repeats?     | Description                              | Error Handling                           |
+===========================+==============================================+==============+==============+==========================================+==========================================+
| ExternalGeospatialFeature | :ref:`multi-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                           |                                              |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                           |                                              |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                           |                                              |              |              |                                          | it.                                      |
+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <ShapeIdentifier>3</ShapeIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>
