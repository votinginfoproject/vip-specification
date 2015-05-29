Precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:doc:`Source.VipId <source>`, :doc:`Locality.Name <locality>`, :doc:`Precinct.Ward <precinct>`,
:doc:`Precinct.Name <precinct>`, and :doc:`Precinct.Number <precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| Tag                 | Data Type               | Required?    | Repeats?   | Description               | Error Handling              |
+=====================+=========================+==============+============+===========================+=============================+
| BallotStyleId       | xs:IDREF                | Optional     | Single     |Links to the :doc:`ballot  |If the field is missing or   |
|                     |                         |              |            |style <ballot_style>`,     |invalid, the implementation  |
|                     |                         |              |            |which a person who lives in|is required to ignore it.    |
|                     |                         |              |            |this precinct will vote.   |                             |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| ElectoralDistrictId | xs:IDREF                | Optional     | Repeats    |Links to an :doc:`electoral|If the field is invalid or   |
|                     |                         |              |            |district                   |not present, the             |
|                     |                         |              |            |<electoral_district>`      |implementation is required to|
|                     |                         |              |            |(e.g., congressional       |ignore it.                   |
|                     |                         |              |            |district, state house      |                             |
|                     |                         |              |            |district, school board     |                             |
|                     |                         |              |            |district) to which the     |                             |
|                     |                         |              |            |precinct belongs. **Highly |                             |
|                     |                         |              |            |Recommended** if candidate |                             |
|                     |                         |              |            |information is to be       |                             |
|                     |                         |              |            |provided. Multiple allowed |                             |
|                     |                         |              |            |and recommended to specify |                             |
|                     |                         |              |            |the geography of multiple  |                             |
|                     |                         |              |            |electoral districts. If an |                             |
|                     |                         |              |            |electoral district splits a|                             |
|                     |                         |              |            |precinct, use the          |                             |
|                     |                         |              |            |**PrecinctSplitName**      |                             |
|                     |                         |              |            |object and do not specify  |                             |
|                     |                         |              |            |that particular electoral  |                             |
|                     |                         |              |            |district in this object.   |                             |
|                     |                         |              |            |                           |                             |
|                     |                         |              |            |                           |                             |
|                     |                         |              |            |                           |                             |
|                     |                         |              |            |                           |                             |
|                     |                         |              |            |                           |                             |
|                     |                         |              |            |                           |                             |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| ExternalIdentifiers |:doc:`ExternalIdentifiers| Optional     | Single     |Other identifier for the   |If the element is invalid or |
|                     |<external_identifiers>`  |              |            |precinct that relates to   |not present, the             |
|                     |                         |              |            |another dataset            |implementation is required to|
|                     |                         |              |            |(e.g. `OCD-ID`_).          |ignore it.                   |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| IsMailOnly          | xs:boolean              | Optional     | Single     |Determines if the precinct |If the field is missing or   |
|                     |                         |              |            |runs mail-only elections.  |invalid, the implementation  |
|                     |                         |              |            |                           |is required to assume        |
|                     |                         |              |            |                           |**IsMailOnly** is false.     |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| LocalityId          | xs:IDREF                | **Required** | Single     |Links to the :doc:`locality|If the field is invalid or   |
|                     |                         |              |            |<locality>` that comprises |not present, the             |
|                     |                         |              |            |the precinct.              |implementation is required to|
|                     |                         |              |            |                           |ignore the precinct element  |
|                     |                         |              |            |                           |containing it.               |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| Name                | xs:string               | **Required** | Single     |Specifies the precinct's   |If the field is invalid or   |
|                     |                         |              |            |name (or number if no name |not present, the             |
|                     |                         |              |            |exists).                   |implementation is required to|
|                     |                         |              |            |                           |ignore the precinct element  |
|                     |                         |              |            |                           |containing it.               |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| Number              | xs:string               | Optional     | Single     |Specifies the precinct's   |If the field is invalid or   |
|                     |                         |              |            |number (e.g., 32 or 32A -- |not present, the             |
|                     |                         |              |            |alpha characters are       |implementation is required to|
|                     |                         |              |            |legal). Should be used if  |ignore it.                   |
|                     |                         |              |            |the **Name** field is      |                             |
|                     |                         |              |            |populated by a name and not|                             |
|                     |                         |              |            |a number.                  |                             |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| PollingLocationId   | xs:IDREF                | Optional     | Repeats    |Specifies a link to the    |If the field is invalid or   |
|                     |                         |              |            |precinct's :doc:`polling   |not present, the             |
|                     |                         |              |            |location                   |implementation is required to|
|                     |                         |              |            |<polling_location>`        |ignore it.                   |
|                     |                         |              |            |object(s). Multiple        |                             |
|                     |                         |              |            |**PollingLocationId** tags |                             |
|                     |                         |              |            |may be specified, but this |                             |
|                     |                         |              |            |use should be reserved for |                             |
|                     |                         |              |            |when multiple              |                             |
|                     |                         |              |            |Election-Day-only vote     |                             |
|                     |                         |              |            |locations serve specific   |                             |
|                     |                         |              |            |precincts.                 |                             |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| PrecinctSplitName   | xs:string               | Optional     | Single     |Refers to name of the      |If the field is invalid or   |
|                     |                         |              |            |associated precinct split. |not present, the             |
|                     |                         |              |            |                           |implementation is required to|
|                     |                         |              |            |                           |ignore it.                   |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+
| Ward                | xs:string               | Optional     | Single     |Specifies the ward the     |If the field is missing or   |
|                     |                         |              |            |precinct is contained      |invalid, the implementation  |
|                     |                         |              |            |within.                    |is required to ignore it.    |
|                     |                         |              |            |                           |                             |
+---------------------+-------------------------+--------------+------------+---------------------------+-----------------------------+

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
