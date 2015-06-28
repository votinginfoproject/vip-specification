.. This file is auto-generated.  Do not edit it by hand!

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| Latitude     | xs:float     | **Required** | Single       | The latitude of the polling location.    | If field is invalid or not present, the  |
|              |              |              |              |                                          | implementation is required to ignore the |
|              |              |              |              |                                          | element containing it.                   |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Longitude    | xs:float     | **Required** | Single       | The longitude of the polling location.   | If the field is invalid or not present,  |
|              |              |              |              |                                          | the implementation is required to ignore |
|              |              |              |              |                                          | the element containing it.               |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Source       | xs:string    | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|              |              |              |              | from location name to lat/lng. For       | the implementation is required to ignore |
|              |              |              |              | example, this could be the name of a     | it.                                      |
|              |              |              |              | geocoding service.                       |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
