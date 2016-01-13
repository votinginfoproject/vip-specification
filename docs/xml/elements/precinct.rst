.. This file is auto-generated.  Do not edit it by hand!

Precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:doc:`Source.VipId <source>`, :doc:`Locality.Name <locality>`, :doc:`Precinct.Ward <precinct>`,
:doc:`Precinct.Name <precinct>`, and :doc:`Precinct.Number <precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| BallotStyleId        | xs:IDREF                              | Optional     | Single       | Links to the :doc:`ballot style          | If the field is invalid or not present,  |
|                      |                                       |              |              | <ballot_style>`, which a person who      | then the implementation is required to   |
|                      |                                       |              |              | lives in this precinct will vote.        | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictIds | xs:IDREFS                             | Optional     | Single       | Links to an :doc:`electoral district     | If the field is invalid or not present,  |
|                      |                                       |              |              | <electoral_district>` (e.g.,             | then the implementation is required to   |
|                      |                                       |              |              | congressional district, state house      | ignore it.                               |
|                      |                                       |              |              | district, school board district) to      |                                          |
|                      |                                       |              |              | which the precinct belongs. **Highly     |                                          |
|                      |                                       |              |              | Recommended** if candidate information   |                                          |
|                      |                                       |              |              | is to be provided. Multiple allowed and  |                                          |
|                      |                                       |              |              | recommended to specify the geography of  |                                          |
|                      |                                       |              |              | multiple electoral districts. If an      |                                          |
|                      |                                       |              |              | electoral district splits a precinct,    |                                          |
|                      |                                       |              |              | use the `PrecinctSplitName` object and   |                                          |
|                      |                                       |              |              | do not specify that particular electoral |                                          |
|                      |                                       |              |              | district in this object.                 |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :doc:`ExternalIdentifiers             | Optional     | Single       | Other identifier for the precinct that   | If the element is invalid or not         |
|                      | </xml/elements/external_identifiers>` |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                      |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly           | xs:boolean                            | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                      |                                       |              |              | mail-only elections.                     | implementation is required to assume     |
|                      |                                       |              |              |                                          | `IsMailOnly` is false.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId           | xs:IDREF                              | **Required** | Single       | Links to the :doc:`locality <locality>`  | If the field is invalid or not present,  |
|                      |                                       |              |              | that comprises the precinct.             | the implementation is required to ignore |
|                      |                                       |              |              |                                          | the precinct element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | xs:string                             | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid or not present,  |
|                      |                                       |              |              | if no name exists).                      | the implementation is required to ignore |
|                      |                                       |              |              |                                          | the precinct element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number               | xs:string                             | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                      |                                       |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                      |                                       |              |              | legal). Should be used if the `Name`     | ignore it.                               |
|                      |                                       |              |              | field is populated by a name and not a   |                                          |
|                      |                                       |              |              | number.                                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds   | xs:IDREFS                             | Optional     | Single       | Specifies a link to the precinct's       | If the field is invalid or not present,  |
|                      |                                       |              |              | :doc:`polling location                   | then the implementation is required to   |
|                      |                                       |              |              | <polling_location>` object(s).           | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName    | xs:string                             | Optional     | Single       | Refers to name of the associated         | If the field is invalid or not present,  |
|                      |                                       |              |              | precinct split.                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                 | xs:string                             | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                      |                                       |              |              | contained within.                        | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <Precinct id="pre90111">
      <BallotStyleId>bs00010</BallotStyleId>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <ElectoralDistrictId>ed60311</ElectoralDistrictId>
      <ElectoralDistrictId>ed60054</ElectoralDistrictId>
      <IsMailOnly>false</IsMailOnly>
      <LocalityId>loc70001</LocalityId>
      <Name>203 - GEORGETOWN</Name>
      <Number>0203</Number>
      <PollingLocationId>pl81274</PollingLocationId>
   </Precinct>
