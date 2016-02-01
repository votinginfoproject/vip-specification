.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the state's election            | If the field is invalid or not present,  |
|                          |                                       |              |              | administration object.                   | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifier for the state that      | If the element is invalid or not         |
|                          |                                       |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                          |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifiers the name of a state, such as  | If the field is invalid, then the        |
|                          |                                       |              |              | Alabama.                                 | implementation is required to ignore it. |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the state's          | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`polling locations                  | then the implementation is required to   |
|                          |                                       |              |              | <multi-xml-polling-location>`. If early  | ignore it.                               |
|                          |                                       |              |              | vote centers or ballot drop locations    |                                          |
|                          |                                       |              |              | are state-wide (e.g., anyone in the      |                                          |
|                          |                                       |              |              | state can use them), they can be         |                                          |
|                          |                                       |              |              | specified here, but you are encouraged   |                                          |
|                          |                                       |              |              | to only use the                          |                                          |
|                          |                                       |              |              | :ref:`multi-xml-precinct` element.       |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
