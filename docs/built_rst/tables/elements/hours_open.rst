.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===========================+==============+==============+==========================================+==========================================+
| Schedule     | :ref:`multi-xml-schedule` | **Required** | Repeats      | Defines a block of days and hours that a | At least one valid `Schedule`_ must be   |
|              |                           |              |              | place will be open.                      | present for ``HoursOpen`` to be valid.   |
|              |                           |              |              |                                          | If no valid `Schedule`_ is present, the  |
|              |                           |              |              |                                          | implementation is required to ignore the |
|              |                           |              |              |                                          | ``HoursOpen`` element.                   |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
