.. This file is auto-generated.  Do not edit it by hand!

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                                  |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                  |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                  |              |              | outside the options listed in            | ignore it.                               |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
|              |                                  |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                  |              |              | using this field.                        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
