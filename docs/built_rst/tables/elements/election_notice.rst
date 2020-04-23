.. This file is auto-generated.  Do not edit it by hand!

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`multi-xml-internationalized-text` | **Required** | Single       | Text for the Election Notice.            | If the element is invalid, then the      |
|              |                                         |              |              |                                          | implementation is required to ignore the |
|              |                                         |              |              |                                          | ``ElectionNotice`` element containing    |
|              |                                         |              |              |                                          | it.                                      |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | ``xs:anyURI``                           | Optional     | Single       | Optional URL for additional information  | If the field is invalid or not present,  |
|              |                                         |              |              | related to the Election Notice.          | then the implementation is required to   |
|              |                                         |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
