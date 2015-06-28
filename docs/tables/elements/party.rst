.. This file is auto-generated.  Do not edit it by hand!

+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=============================+==============+==============+==========================================+==========================================+
| Abbreviation        | xs:string                   | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                     |                             |              |              |                                          | then the implementation is required to   |
|                     |                             |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color               | `HtmlColorString`_          | Optional     | Single       | The preferred display color for the      | If the field is invalid or not present,  |
|                     |                             |              |              | party, for use in maps and other         | then the implementation is required to   |
|                     |                             |              |              | displays.                                | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers   | Optional     | Single       | Other identifiers that link this party   | If the field is invalid or not present,  |
|                     | <external_identifiers>`     |              |              | to other related data sets (e.g. a       | then the implementation is required to   |
|                     |                             |              |              | campaign finance system, etc).           | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri             | xs:anyURI                   | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                     |                             |              |              | displays.                                | then the implementation is required to   |
|                     |                             |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | :doc:`InternationalizedText | Optional     | Single       | The name of the party.                   | If the element is invalid or not         |
|                     | <internationalized_text>`   |              |              |                                          | present, then the implementation is      |
|                     |                             |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
