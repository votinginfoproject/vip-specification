.. This file is auto-generated.  Do not edit it by hand!

+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation    | :ref:`multi-xml-contact-information`    | Optional     | Repeats      | Specifies the contact information for    | If the element is invalid or not         |
|                       |                                         |              |              | the office and/or individual holding the | present, then the implementation is      |
|                       |                                         |              |              | office.                                  | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId   | ``xs:IDREF``                            | **Required** | Single       | Links to the                             | If the field is invalid or not present,  |
|                       |                                         |              |              | :ref:`multi-xml-electoral-district`      | the implementation is required to ignore |
|                       |                                         |              |              | element associated with the office.      | the ``Office`` element containing it.    |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers   | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers that link this office  | If the element is invalid or not         |
|                       |                                         |              |              | to other related datasets (e.g. campaign | present, then the implementation is      |
|                       |                                         |              |              | finance systems, OCD IDs, et al.).       | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline        | ``xs:date``                             | Optional     | Single       | Specifies the date and time when a       | If the field is invalid or not present,  |
|                       |                                         |              |              | candidate must have filed for the        | then the implementation is required to   |
|                       |                                         |              |              | contest for the office.                  | ignore it.                               |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan            | ``xs:boolean``                          | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                       |                                         |              |              | partisan.                                | then the implementation is required to   |
|                       |                                         |              |              |                                          | ignore it.                               |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                  | :ref:`multi-xml-internationalized-text` | **Required** | Single       | The name of the office.                  | If the field is invalid or not present,  |
|                       |                                         |              |              |                                          | the implementation is required to ignore |
|                       |                                         |              |              |                                          | the ``Office`` element containing it.    |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonIds | ``xs:IDREFS``                           | Optional     | Single       | Links to the :ref:`multi-xml-person`     | If the field is invalid or not present,  |
|                       |                                         |              |              | element(s) that hold additional          | then the implementation is required to   |
|                       |                                         |              |              | information about the current office     | ignore it.                               |
|                       |                                         |              |              | holder(s).                               |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                  | :ref:`multi-xml-term`                   | Optional     | Single       | Defines the term the office can be held. | If the element is invalid or not         |
|                       |                                         |              |              |                                          | present, then the implementation is      |
|                       |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
