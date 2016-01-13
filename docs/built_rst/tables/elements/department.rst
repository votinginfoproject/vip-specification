.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information` | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          |                                      |              |              | for the election administration body     | present, then the implementation is      |
|                          |                                      |              |              | (see                                     | required to ignore it.                   |
|                          |                                      |              |              | :ref:`multi-xml-contact-information`).   |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                         | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                                      |              |              | election administration office. The      | then the implementation is required to   |
|                          |                                      |              |              | specified person should be the           | ignore it.                               |
|                          |                                      |              |              | :ref:`election official                  |                                          |
|                          |                                      |              |              | <multi-xml-person>`.                     |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`multi-xml-voter-service`       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          |                                      |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                                      |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
