.. This file is auto-generated.  Do not edit it by hand!

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-office-term-type` | Optional     | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              |                                   |              |              | :ref:`multi-xml-office-term-type` for    | the implementation is required to ignore |
|              |                                   |              |              | valid values).                           | the ``Office`` element containing it.    |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | ``xs:date``                       | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                   |              |              | term of the office.                      | then the implementation is required to   |
|              |                                   |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | ``xs:date``                       | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                   |              |              | term of the office.                      | then the implementation is required to   |
|              |                                   |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
