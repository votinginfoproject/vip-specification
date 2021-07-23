.. This file is auto-generated.  Do not edit it by hand!

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| Algorithm    | :ref:`multi-xml-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to | If the field is invalid, then the        |
|              |                                     |              |              | compute the checksum value.              | implementation is required to ignore the |
|              |                                     |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                       | **Required** | Single       | The raw cryptographic checksum value.    | If the field is invalid, then the        |
|              |                                     |              |              |                                          | implementation is required to ignore the |
|              |                                     |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
