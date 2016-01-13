.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=================================+==============+==============+==========================================+==========================================+
| StartTime    | :ref:`multi-xml-time-with-zone` | Optional     | Single       | The time at which this place opens.      | If the element is invalid or not         |
|              |                                 |              |              |                                          | present, then the implementation is      |
|              |                                 |              |              |                                          | required to ignore it.                   |
+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | :ref:`multi-xml-time-with-zone` | Optional     | Single       | The time at which this place closes.     | If the element is invalid or not         |
|              |                                 |              |              |                                          | present, then the implementation is      |
|              |                                 |              |              |                                          | required to ignore it.                   |
+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
