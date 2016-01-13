.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information`    | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          |                                         |              |              | service.                                 | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          |                                         |              |              | available.                               | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                            | Optional     | Single       | The :ref:`authority <multi-xml-person>`  | If the field is invalid or not present,  |
|                          |                                         |              |              | for a particular voter service.          | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                          |                                         |              |              | <multi-xml-voter-service-type>`.         | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                           | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                         |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                         |              |              | service.                                 | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
