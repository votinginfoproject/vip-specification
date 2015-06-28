.. This file is auto-generated.  Do not edit it by hand!

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`OfficeTermType                | **Required** | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              | <../enumerations/office_term_type>` |              |              | :doc:`OfficeTermType                     | the implementation is required to ignore |
|              |                                     |              |              | <../enumerations/office_term_type>` for  | the ``Office`` element containing it.    |
|              |                                     |              |              | valid values).                           |                                          |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | xs:date                             | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | the implementation is required to ignore |
|              |                                     |              |              |                                          | it.                                      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | xs:date                             | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | the implementation is required to ignore |
|              |                                     |              |              |                                          | it.                                      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
