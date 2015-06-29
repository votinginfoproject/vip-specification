.. This file is auto-generated.  Do not edit it by hand!

+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+===========================+==============+==============+==========================================+==========================================+
| BallotStyleId       | xs:IDREF                  | Optional     | Single       | Links to the :doc:`ballot style          | If the field is invalid or not present,  |
|                     |                           |              |              | <ballot_style>`, which a person who      | then the implementation is required to   |
|                     |                           |              |              | lives in this precinct will vote.        | ignore it.                               |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId | xs:IDREF                  | Optional     | Repeats      | Links to an :doc:`electoral district     | If the field is invalid or not present,  |
|                     |                           |              |              | <electoral_district>` (e.g.,             | then the implementation is required to   |
|                     |                           |              |              | congressional district, state house      | ignore it.                               |
|                     |                           |              |              | district, school board district) to      |                                          |
|                     |                           |              |              | which the precinct belongs. **Highly     |                                          |
|                     |                           |              |              | Recommended** if candidate information   |                                          |
|                     |                           |              |              | is to be provided. Multiple allowed and  |                                          |
|                     |                           |              |              | recommended to specify the geography of  |                                          |
|                     |                           |              |              | multiple electoral districts. If an      |                                          |
|                     |                           |              |              | electoral district splits a precinct,    |                                          |
|                     |                           |              |              | use the **PrecinctSplitName** object and |                                          |
|                     |                           |              |              | do not specify that particular electoral |                                          |
|                     |                           |              |              | district in this object.                 |                                          |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers | Optional     | Single       | Other identifier for the precinct that   | If the element is invalid or not         |
|                     | <external_identifiers>`   |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                     |                           |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly          | xs:boolean                | Optional     | Single       | Determines if the precinct runs          | If the field is invalid or not present,  |
|                     |                           |              |              | mail-only elections.                     | then the implementation is required to   |
|                     |                           |              |              |                                          | assume **IsMailOnly** is false.          |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId          | xs:IDREF                  | **Required** | Single       | Links to the :doc:`locality <locality>`  | If the field is invalid, then the        |
|                     |                           |              |              | that comprises the precinct.             | implementation is required to ignore the |
|                     |                           |              |              |                                          | ``Precinct`` element containing it.      |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | xs:string                 | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid, then the        |
|                     |                           |              |              | if no name exists).                      | implementation is required to ignore the |
|                     |                           |              |              |                                          | ``Precinct`` element containing it.      |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number              | xs:string                 | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                     |                           |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                     |                           |              |              | legal). Should be used if the **Name**   | ignore it.                               |
|                     |                           |              |              | field is populated by a name and not a   |                                          |
|                     |                           |              |              | number.                                  |                                          |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId   | xs:IDREF                  | Optional     | Repeats      | Specifies a link to the precinct's       | If the field is invalid or not present,  |
|                     |                           |              |              | :doc:`polling location                   | then the implementation is required to   |
|                     |                           |              |              | <polling_location>` object(s). Multiple  | ignore it.                               |
|                     |                           |              |              | **PollingLocationId** tags may be        |                                          |
|                     |                           |              |              | specified, but this use should be        |                                          |
|                     |                           |              |              | reserved for when multiple               |                                          |
|                     |                           |              |              | Election-Day-only vote locations serve   |                                          |
|                     |                           |              |              | specific precincts.                      |                                          |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName   | xs:string                 | Optional     | Single       | Refers to name of the associated         | If the field is invalid or not present,  |
|                     |                           |              |              | precinct split.                          | then the implementation is required to   |
|                     |                           |              |              |                                          | ignore it.                               |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                | xs:string                 | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                     |                           |              |              | contained within.                        | then the implementation is required to   |
|                     |                           |              |              |                                          | ignore it.                               |
+---------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
