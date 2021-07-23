.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===========================+==============+==============+==========================================+==========================================+
| Filename     | ``xs:string``             | **Required** | Single       | The name of the external file.           | If the field is invalid, then the        |
|              |                           |              |              |                                          | implementation is required to ignore the |
|              |                           |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Checksum     | :ref:`multi-xml-checksum` | **Required** | Single       | The cryptographic checksum of the        | If the element is invalid, then the      |
|              |                           |              |              | referenced external file.                | implementation is required to ignore the |
|              |                           |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
