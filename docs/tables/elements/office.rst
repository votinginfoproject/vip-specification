.. This file is auto-generated.  Do not edit it by hand!

+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=============================+==============+==============+==========================================+==========================================+
| ContactInformation   | :doc:`ContactInformation    | Optional     | Repeats      | Specifies the contact information for    | If the element is invalid or not         |
|                      | <contact_information>`      |              |              | the office and/or individual holding the | present, then the implementation is      |
|                      |                             |              |              | office.                                  | required to ignore it.                   |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId  | xs:IDREF                    | **Required** | Single       | Links to the :doc:`ElectoralDistrict     | If the field is invalid, then the        |
|                      |                             |              |              | <electoral_district>` element associated | implementation is required to ignore the |
|                      |                             |              |              | with the office.                         | Office element containing it.            |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :doc:`ExternalIdentifiers   | Optional     | Single       | Other identifiers that link this office  | If the element is invalid or not         |
|                      | <external_identifiers>`     |              |              | to other related datasets (e.g. campaign | present, then the implementation is      |
|                      |                             |              |              | finance systems, OCD IDs, et al.).       | required to ignore it.                   |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline       | xs:date                     | Optional     | Single       | Specifies the date and time when a       | If the field is invalid or not present,  |
|                      |                             |              |              | candidate must have filed for the        | then the implementation is required to   |
|                      |                             |              |              | contest for the office.                  | ignore it.                               |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan           | xs:boolean                  | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                      |                             |              |              | partisan.                                | then the implementation is required to   |
|                      |                             |              |              |                                          | ignore it.                               |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | :doc:`InternationalizedText | **Required** | Single       | The name of the office.                  | If the element is invalid, then the      |
|                      | <internationalized_text>`   |              |              |                                          | implementation is required to ignore the |
|                      |                             |              |              |                                          | Office element containing it.            |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonId | xs:IDREF                    | Optional     | Repeats      | Links to the :doc:`Person <person>`      | If the field is invalid or not present,  |
|                      |                             |              |              | element(s) that hold additional          | then the implementation is required to   |
|                      |                             |              |              | information about the current office     | ignore it.                               |
|                      |                             |              |              | holder(s).                               |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                 | `Term`_                     | Optional     | Single       | Defines the term the office can be held. | If the element is invalid or not         |
|                      |                             |              |              |                                          | present, then the implementation is      |
|                      |                             |              |              |                                          | required to ignore it.                   |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
