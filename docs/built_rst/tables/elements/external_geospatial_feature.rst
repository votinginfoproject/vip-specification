.. This file is auto-generated.  Do not edit it by hand!

+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+====================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                       | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                    |              |              | :ref:`multi-xml-external-file`           | implementation is required to ignore the |
|                   |                                    |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                    |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`multi-xml-geospatial-format` | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                    |              |              |                                          | implementation is required to ignore the |
|                   |                                    |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                    |              |              |                                          | containing it.                           |
+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`multi-xml-feature-attribute` | **Required** | Single       | Identifing attributes indicating which   | If the element is invalid, then the      |
|                   |                                    |              |              | specific shape(s) to use from the        | implementation is required to ignore the |
|                   |                                    |              |              | geospatial file. These refer to          | ``ExternalGeospatialFeature`` element    |
|                   |                                    |              |              | identifiers within the referenced        | containing it.                           |
|                   |                                    |              |              | external file.                           |                                          |
+-------------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
