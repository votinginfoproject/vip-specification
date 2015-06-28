.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+===========================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | xs:IDREF                  | Optional     | Single       | Links to the state's election            | If the field is invalid or not present,  |
|                          |                           |              |              | administration object.                   | the implementation is required to ignore |
|                          |                           |              |              |                                          | it.                                      |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :doc:`ExternalIdentifiers | Optional     | Single       | Other identifier for the state that      | If the field is invalid or not present,  |
|                          | <external_identifiers>`   |              |              | relates to another dataset (e.g.         | the implementation is required to ignore |
|                          |                           |              |              | `OCD-ID`_).                              | it.                                      |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | xs:string                 | Optional     | Single       | Specifiers the name of a state, such as  | If the field is not present or invalid,  |
|                          |                           |              |              | Alabama.                                 | the implementation is required to ignore |
|                          |                           |              |              |                                          | the element containing it.               |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId        | xs:IDREF                  | Optional     | Repeats      | Specifies a link to the state's          | If the field is missing or invalid, the  |
|                          |                           |              |              | :doc:`polling locations                  | implementation is required to ignore it. |
|                          |                           |              |              | <polling_location>`. If early vote       |                                          |
|                          |                           |              |              | centers or ballot drop locations are     |                                          |
|                          |                           |              |              | state-wide (e.g., anyone in the state    |                                          |
|                          |                           |              |              | can use them), they can be specified     |                                          |
|                          |                           |              |              | here, but are encouraged to only use the |                                          |
|                          |                           |              |              | :doc:`Precinct <precinct>` element.      |                                          |
+--------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
