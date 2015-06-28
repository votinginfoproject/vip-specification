.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation              | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          | <contact_information>`                |              |              | service.                                 | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :doc:`InternationalizedText           | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          | <internationalized_text>`             |              |              | available.                               | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                              | Optional     | Single       | The :doc:`authority <person>` for a      | If the field is invalid or not present,  |
|                          |                                       |              |              | particular voter service.                | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`VoterServiceType                | Optional     | Single       | The type of :doc:`voter service          | If the field is invalid or not present,  |
|                          | <../enumerations/voter_service_type>` |              |              | <../enumerations/voter_service_type>`.   | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                             | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                       |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                       |              |              | service.                                 | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
