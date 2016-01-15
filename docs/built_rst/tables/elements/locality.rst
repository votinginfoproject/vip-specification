.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                  | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`multi-xml-election-administration` | then the implementation is required to   |
|                          |                                       |              |              | object.                                  | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Another identifier for a locality that   | If the element is invalid or not         |
|                          |                                       |              |              | links to another dataset (e.g.           | present, then the implementation is      |
|                          |                                       |              |              | `OCD-ID`_)                               | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        | If the field is not present or invalid,  |
|                          |                                       |              |              |                                          | the implementation is required to ignore |
|                          |                                       |              |              |                                          | the Locality element containing it.      |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to a set of the         | If the field is invalid or not present,  |
|                          |                                       |              |              | locality's :ref:`polling locations       | the implementation is required to ignore |
|                          |                                       |              |              | <multi-xml-polling-location>`s. If early | it. However, the implementation should   |
|                          |                                       |              |              | vote centers or ballot drop locations    | still check to see if there are any      |
|                          |                                       |              |              | are locality-wide, they should be        | polling locations associated with this   |
|                          |                                       |              |              | specified here.                          | locality's state.                        |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                  | ``xs:IDREF``                          | **Required** | Single       | References the locality's                | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`multi-xml-state`.                  | the implementation is required to ignore |
|                          |                                       |              |              |                                          | the Locality element containing.         |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                          |                                       |              |              | county, town, et al.), which is one of   | then the implementation is required to   |
|                          |                                       |              |              | the various :ref:`DistrictType           | ignore it.                               |
|                          |                                       |              |              | enumerations <multi-xml-district-type>`. |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality   | If the field is invalid or not present,  |
|                          |                                       |              |              | that falls outside the options listed in | then the implementation is required to   |
|                          |                                       |              |              | :ref:`DistrictType                       | ignore it.                               |
|                          |                                       |              |              | <multi-xml-district-type>`.              |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
