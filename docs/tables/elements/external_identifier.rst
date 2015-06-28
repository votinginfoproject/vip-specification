.. This file is auto-generated.  Do not edit it by hand!

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`IdentifierType               | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid, then the        |
|              | <../enumerations/identifier_type>` |              |              | be one of the valid types as defined by  | implementation is required to ignore the |
|              |                                    |              |              | :doc:`IdentifierType                     | ``ElectionIdentifier`` containing it.    |
|              |                                    |              |              | <../enumerations/identifier_type>`.      |                                          |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | xs:string                          | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                    |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                    |              |              | outside the options listed in            | ignore it.                               |
|              |                                    |              |              | :doc:`IdentifierType                     |                                          |
|              |                                    |              |              | <../enumerations/identifier_type>`.      |                                          |
|              |                                    |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                    |              |              | using this field.                        |                                          |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | xs:string                          | **Required** | Single       | Specifies the identifier.                | If the field is invalid, then the        |
|              |                                    |              |              |                                          | implementation is required to ignore the |
|              |                                    |              |              |                                          | ``ElectionIdentifier`` containing it.    |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
