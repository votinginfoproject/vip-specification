.. This file is auto-generated.  Do not edit it by hand!

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`multi-xml-internationalized-text` | **Required** | Single       | The last minute or emergency             | If the element is invalid, then the      |
|              |                                         |              |              | notification text should be placed here. | implementation is required to ignore the |
|              |                                         |              |              |                                          | ``ElectionNotice`` element containing    |
|              |                                         |              |              |                                          | it.                                      |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | ``xs:anyURI``                           | Optional     | Single       | Optional URL for additional information  | If the field is invalid or not present,  |
|              |                                         |              |              | related to the last minute or emergency  | then the implementation is required to   |
|              |                                         |              |              | notification.                            | ignore it.                               |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
