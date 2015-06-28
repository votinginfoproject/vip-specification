.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | xs:IDREF                         | Optional     | Single       | Links to the locality's :doc:`election   | If the field is invalid or not present,  |
|                          |                                  |              |              | administration                           | then the implementation is required to   |
|                          |                                  |              |              | <election_administration>` object.       | ignore it.                               |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :doc:`ExternalIdentifiers        | Optional     | Single       | Another identifier for a locality that   | If the element is invalid or not         |
|                          | <external_identifiers>`          |              |              | links to another dataset (e.g.           | present, then the implementation is      |
|                          |                                  |              |              | `OCD-ID`_)                               | required to ignore it.                   |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | xs:string                        | **Required** | Single       | Specifies the name of a locality.        | If the field is invalid, then the        |
|                          |                                  |              |              |                                          | implementation is required to ignore the |
|                          |                                  |              |              |                                          | Locality element containing it.          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId        | xs:IDREF                         | Optional     | Repeats      | Specifies a link to the locality's       | If the field is invalid or not present,  |
|                          |                                  |              |              | :doc:`polling locations                  | then the implementation is required to   |
|                          |                                  |              |              | <polling_location>`. If early vote       | ignore it. However, the implementation   |
|                          |                                  |              |              | centers or ballot drop locations are     | should still check to see if there are   |
|                          |                                  |              |              | locality-wide, they should be specified  | any polling locations associated with    |
|                          |                                  |              |              | here.                                    | this locality's state.                   |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                  | xs:IDREF                         | **Required** | Single       | References the locality's :doc:`state    | If the field is invalid, then the        |
|                          |                                  |              |              | <state>`.                                | implementation is required to ignore the |
|                          |                                  |              |              |                                          | locality element containing.             |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`DistrictType               | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                          | <../enumerations/district_type>` |              |              | county, town, et al.), which is one of   | then the implementation is required to   |
|                          |                                  |              |              | the various :doc:`DistrictType           | ignore it.                               |
|                          |                                  |              |              | enumerations                             |                                          |
|                          |                                  |              |              | <../enumerations/district_type>`.        |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                        | Optional     | Single       | Allows for defining a type of locality   | If the field is invalid or not present,  |
|                          |                                  |              |              | that falls outside the options listed in | then the implementation is required to   |
|                          |                                  |              |              | :doc:`DistrictType                       | ignore it.                               |
|                          |                                  |              |              | <../enumerations/district_type>`.        |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
