.. This file is auto-generated.  Do not edit it by hand!

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| BallotStyleId        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-xml-ballot-style`, which a   | then the implementation is required to   |
|                      |                                       |              |              | person who lives in this precinct will   | ignore it.                               |
|                      |                                       |              |              | vote.                                    |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictIds | ``xs:IDREFS``                         | Optional     | Single       | Links to an                              | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-xml-electoral-district`      | then the implementation is required to   |
|                      |                                       |              |              | (e.g., congressional district, state     | ignore it.                               |
|                      |                                       |              |              | house district, school board district)   |                                          |
|                      |                                       |              |              | to which the precinct belongs. **Highly  |                                          |
|                      |                                       |              |              | Recommended** if candidate information   |                                          |
|                      |                                       |              |              | is to be provided. Multiple allowed and  |                                          |
|                      |                                       |              |              | recommended to specify the geography of  |                                          |
|                      |                                       |              |              | multiple electoral districts. If an      |                                          |
|                      |                                       |              |              | electoral district splits a precinct,    |                                          |
|                      |                                       |              |              | use the `PrecinctSplitName` object and   |                                          |
|                      |                                       |              |              | do not specify that particular electoral |                                          |
|                      |                                       |              |              | district in this object.                 |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifier for the precinct that   | If the element is invalid or not         |
|                      |                                       |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                      |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly           | ``xs:boolean``                        | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                      |                                       |              |              | mail-only elections.                     | implementation is required to assume     |
|                      |                                       |              |              |                                          | `IsMailOnly` is false.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId           | ``xs:IDREF``                          | **Required** | Single       | Links to the :ref:`multi-xml-locality`   | If the field is invalid or not present,  |
|                      |                                       |              |              | that comprises the precinct.             | the implementation is required to ignore |
|                      |                                       |              |              |                                          | the precinct element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | ``xs:string``                         | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid or not present,  |
|                      |                                       |              |              | if no name exists).                      | the implementation is required to ignore |
|                      |                                       |              |              |                                          | the precinct element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number               | ``xs:string``                         | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                      |                                       |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                      |                                       |              |              | legal). Should be used if the `Name`     | ignore it.                               |
|                      |                                       |              |              | field is populated by a name and not a   |                                          |
|                      |                                       |              |              | number.                                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds   | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the precinct's       | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-xml-polling-location`        | then the implementation is required to   |
|                      |                                       |              |              | object(s).                               | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName    | ``xs:string``                         | Optional     | Single       | Refers to name of the associated         | If the field is invalid or not present,  |
|                      |                                       |              |              | precinct split.                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                 | ``xs:string``                         | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                      |                                       |              |              | contained within.                        | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
