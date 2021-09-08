.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Name         | ``xs:string`` | **Required** | Repeats      | This field should list the appropriate   | If the field is invalid, then the        |
|              |               |              |              | column header from the geospatial        | implementation is required to ignore the |
|              |               |              |              | attribute table.                         | ``FeatureAttribute`` element containing  |
|              |               |              |              |                                          | it.                                      |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string`` | **Required** | Repeats      | This field should list the appropriate   | If the field is invalid, then the        |
|              |               |              |              | value from the geospatial attribute      | implementation is required to ignore the |
|              |               |              |              | table, per the column header name.       | ``FeatureAttribute`` element containing  |
|              |               |              |              |                                          | it.                                      |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
