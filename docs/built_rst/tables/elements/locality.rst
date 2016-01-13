.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                               | Error Handling                           |
+==========================+=======================================+==============+==============+===========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                   | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`single-xml-election-administration` | then the implementation is required to   |
|                          |                                       |              |              | object.                                   | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Another identifier for a locality that    | If the element is invalid or not         |
|                          |                                       |              |              | links to another dataset (e.g. `OCD-ID`_) | present, then the implementation is      |
|                          |                                       |              |              |                                           | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.         | If the field is not present or invalid,  |
|                          |                                       |              |              |                                           | the implementation is required to ignore |
|                          |                                       |              |              |                                           | the Locality element containing it.      |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| PollingLocationId        | ``xs:IDREF``                          | Optional     | Repeats      | Specifies a link to the locality's        | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`polling locations                   | the implementation is required to ignore |
|                          |                                       |              |              | <single-xml-polling-location>`. If early  | it. However, the implementation should   |
|                          |                                       |              |              | vote centers or ballot drop locations are | still check to see if there are any      |
|                          |                                       |              |              | locality-wide, they should be specified   | polling locations associated with this   |
|                          |                                       |              |              | here.                                     | locality's state.                        |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| StateId                  | ``xs:IDREF``                          | **Required** | Single       | References the locality's                 | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`single-xml-state`.                  | the implementation is required to ignore |
|                          |                                       |              |              |                                           | the Locality element containing.         |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.        | If the field is invalid or not present,  |
|                          |                                       |              |              | county, town, et al.), which is one of    | then the implementation is required to   |
|                          |                                       |              |              | the various :ref:`DistrictType            | ignore it.                               |
|                          |                                       |              |              | enumerations <single-xml-district-type>`. |                                          |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality    | If the field is invalid or not present,  |
|                          |                                       |              |              | that falls outside the options listed in  | then the implementation is required to   |
|                          |                                       |              |              | :ref:`DistrictType                        | ignore it.                               |
|                          |                                       |              |              | <single-xml-district-type>`.              |                                          |
+--------------------------+---------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
