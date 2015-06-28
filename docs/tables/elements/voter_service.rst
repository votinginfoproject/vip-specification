.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation              | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          | <contact_information>`                |              |              | service.                                 | present, the implementation is required  |
|                          |                                       |              |              |                                          | to ignore it.                            |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :doc:`InternationalizedText           | Optional     | Single       | Long description of the services         | If the field is invalid or not present,  |
|                          | <internationalized_text>`             |              |              | available.                               | the implementation is required to ignore |
|                          |                                       |              |              |                                          | it.                                      |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                              | Optional     | Single       | The :doc:`authority <person>` for a      | If the field is invalid or not present,  |
|                          |                                       |              |              | particular voter service.                | the implementation is required to ignore |
|                          |                                       |              |              |                                          | it.                                      |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`VoterServiceType                | Optional     | Single       | The type of :doc:`voter service          | If the element is invalid or not         |
|                          | <../enumerations/voter_service_type>` |              |              | <../enumerations/voter_service_type>`.   | present, the implementation is required  |
|                          |                                       |              |              |                                          | to ignore it.                            |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                             | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                       |              |              | cataloging another type of voter         | the implementation is required to ignore |
|                          |                                       |              |              | service.                                 | it.                                      |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
