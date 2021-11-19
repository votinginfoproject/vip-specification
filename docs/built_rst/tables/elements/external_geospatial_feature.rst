.. This file is auto-generated.  Do not edit it by hand!

+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=====================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                        | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                     |              |              | :ref:`multi-xml-external-file`           | implementation is required to ignore the |
|                   |                                     |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                     |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`multi-xml-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                     |              |              |                                          | implementation is required to ignore the |
|                   |                                     |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                     |              |              |                                          | containing it.                           |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`multi-xml-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    | If the element is invalid, then the      |
|                   |                                     |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                   |                                     |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                   |                                     |              |              | the referenced external file. This is a  | containing it.                           |
|                   |                                     |              |              | repeated field in the XML specification, |                                          |
|                   |                                     |              |              | but a scalar field in the CSV            |                                          |
|                   |                                     |              |              | specification. If more than one          |                                          |
|                   |                                     |              |              | identifier is required with the CSV      |                                          |
|                   |                                     |              |              | specifiation, multiple values can be     |                                          |
|                   |                                     |              |              | provided by delimited by space.          |                                          |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
