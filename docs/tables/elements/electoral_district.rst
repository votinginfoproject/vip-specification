.. This file is auto-generated.  Do not edit it by hand!

+---------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==================================+==============+==============+==========================================+==========================================+
| ExternalIdentifiers | :doc:`ExternalIdentifiers        | Optional     | Single       | Other identifiers that link to external  | If the element is invalid or not         |
|                     | <external_identifiers>`          |              |              | datasets (e.g. `OCD-IDs`_)               | present, then the implementation is      |
|                     |                                  |              |              |                                          | required to ignore it.                   |
+---------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | xs:string                        | **Required** | Single       | Specifies the electoral area's name.     | If the field is invalid, then the        |
|                     |                                  |              |              |                                          | implementation is required to ignore the |
|                     |                                  |              |              |                                          | ``ElectoralDistrict`` element containing |
|                     |                                  |              |              |                                          | it.                                      |
+---------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number              | xs:integer                       | Optional     | Single       | Specifies the district number of the     | If the field is invalid or not present,  |
|                     |                                  |              |              | district (e.g. 34, in the case of the    | then the implementation is required to   |
|                     |                                  |              |              | 34th State Senate District). If a number | ignore it.                               |
|                     |                                  |              |              | is not applicable, instead of leaving    |                                          |
|                     |                                  |              |              | the field blank, leave this field out of |                                          |
|                     |                                  |              |              | the object; empty strings are not valid  |                                          |
|                     |                                  |              |              | for xs:integer fields.                   |                                          |
+---------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                | :doc:`DistrictType               | **Required** | Single       | Specifies the type of electoral area.    | If the field is invalid, then the        |
|                     | <../enumerations/district_type>` |              |              |                                          | implementation is required to ignore the |
|                     |                                  |              |              |                                          | ``ElectoralDistrict`` element containing |
|                     |                                  |              |              |                                          | it.                                      |
+---------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType           | xs:string                        | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                     |                                  |              |              | :doc:`DistrictType                       | then the implementation is required to   |
|                     |                                  |              |              | <../enumerations/district_type>` option  | ignore it.                               |
|                     |                                  |              |              | when ``Type`` is specified as "other".   |                                          |
+---------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
