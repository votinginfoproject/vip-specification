.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-lat-lng:

lat_long
========

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| latitude      | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|               |               |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|               |               |              |              | example, this could be the name of a     | ignore it.                               |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
