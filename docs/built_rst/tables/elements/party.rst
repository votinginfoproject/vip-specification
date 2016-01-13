.. This file is auto-generated.  Do not edit it by hand!

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation        | ``xs:string``                           | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color               | :ref:`multi-xml-html-color-string`      | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                     |                                         |              |              | party, for use in maps and other         | present, then the implementation is      |
|                     |                                         |              |              | displays.                                | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers that link this party   | If the element is invalid or not         |
|                     |                                         |              |              | to other related data sets (e.g. a       | present, then the implementation is      |
|                     |                                         |              |              | campaign finance system, etc).           | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri             | ``xs:anyURI``                           | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                     |                                         |              |              | displays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | :ref:`multi-xml-internationalized-text` | Optional     | Single       | The name of the party.                   | If the element is invalid or not         |
|                     |                                         |              |              |                                          | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
