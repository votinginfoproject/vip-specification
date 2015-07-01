.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+===========================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | xs:IDREF                  | Optional     | Single       | Links to the state's election            | If the field is invalid or not present,  |
|                          |                           |              |              | administration object.                   | then the implementation is required to   |
|                          |                           |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :doc:`ExternalIdentifiers | Optional     | Single       | Other identifier for the state that      | If the element is invalid or not         |
|                          | <external_identifiers>`   |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                          |                           |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | xs:string                 | **Required** | Single       | Specifiers the name of a state, such as  | If the field is invalid, then the        |
|                          |                           |              |              | Alabama.                                 | implementation is required to ignore the |
|                          |                           |              |              |                                          | ``State`` element containing it.         |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId        | xs:IDREF                  | Optional     | Repeats      | Specifies a link to the state's          | If the field is invalid or not present,  |
|                          |                           |              |              | :doc:`polling locations                  | then the implementation is required to   |
|                          |                           |              |              | <polling_location>`. If early vote       | ignore it.                               |
|                          |                           |              |              | centers or ballot drop locations are     |                                          |
|                          |                           |              |              | state-wide (e.g., anyone in the state    |                                          |
|                          |                           |              |              | can use them), they can be specified     |                                          |
|                          |                           |              |              | here, but are encouraged to only use the |                                          |
|                          |                           |              |              | :doc:`Precinct <precinct>` element.      |                                          |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
