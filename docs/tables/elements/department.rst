.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          | <contact_information>`   |              |              | for the election administration body     | present, then the implementation is      |
|                          |                          |              |              | (see :doc:`ContactInformation            | required to ignore it.                   |
|                          |                          |              |              | <contact_information>`).                 |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                 | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                          |              |              | election administration office. The      | then the implementation is required to   |
|                          |                          |              |              | specified person should be the           | ignore it.                               |
|                          |                          |              |              | :doc:`election official <person>`.       |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`VoterService       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          | <ea-dep-voter-service>`  |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                          |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
