Precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:doc:`Source.VipId <source>`, :doc:`Locality.Name <locality>`, :doc:`Precinct.Ward <precinct>`,
:doc:`Precinct.Name <precinct>`, and :doc:`Precinct.Number <precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

.. todo::

   Complete description for ExternalIdentifiers
   
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| Tag                 | Data Type          | Required?    | Repeats?   | Description               | Error Handling              |
+=====================+====================+==============+============+===========================+=============================+
| BallotStyleId       | xs:IDREF           | Optional     | Single     |The **BallotStyleId** links|If the **BallotStyleId**     |
|                     |                    |              |            |to the ballot element,     |field is missing or invalid, |
|                     |                    |              |            |which a person who lives in|the implementation is        |
|                     |                    |              |            |this precinct will vote.   |required to ignore it.       |
|                     |                    |              |            |                           |                             |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| ElectoralDistrictId | xs:IDREF           | Optional     | Repeats    |The **ElectoralDistrictId**|If the                       |
|                     |                    |              |            |links to an :doc:`electoral|**ElectoralDistrictId** field|
|                     |                    |              |            |district                   |is invalid or not present,   |
|                     |                    |              |            |<electoral_district>`      |the implementation is        |
|                     |                    |              |            |(e.g., congressional       |required to ignore it.       |
|                     |                    |              |            |district, state house      |                             |
|                     |                    |              |            |district, school board     |                             |
|                     |                    |              |            |district) to which the     |                             |
|                     |                    |              |            |precinct belongs. ***Highly|                             |
|                     |                    |              |            |Recommended*** if candidate|                             |
|                     |                    |              |            |information is to be       |                             |
|                     |                    |              |            |provided. Multiple allowed |                             |
|                     |                    |              |            |and recommended to specify |                             |
|                     |                    |              |            |the geography of multiple  |                             |
|                     |                    |              |            |electoral districts. If an |                             |
|                     |                    |              |            |electoral district splits a|                             |
|                     |                    |              |            |precinct, use the          |                             |
|                     |                    |              |            |**PrecinctSplitName**      |                             |
|                     |                    |              |            |object and do not specify  |                             |
|                     |                    |              |            |that particular electoral  |                             |
|                     |                    |              |            |district in this object.   |                             |
|                     |                    |              |            |                           |                             |
|                     |                    |              |            |                           |                             |
|                     |                    |              |            |                           |                             |
|                     |                    |              |            |                           |                             |
|                     |                    |              |            |                           |                             |
|                     |                    |              |            |                           |                             |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| ExternalIdentifiers | ExternalIdentifiers| Optional     | Single     |**ExternalIdentifiers**    |If **ExternalIdentifiers** is|
|                     |                    |              |            |                           |invalid or not present, the  |
|                     |                    |              |            |                           |implementation is required to|
|                     |                    |              |            |                           |ignore it.                   |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| IsMailOnly          | xs:boolean         | Optional     | Single     |**IsMailOnly** determines  |If **IsMailOnly** is missing |
|                     |                    |              |            |if the **Precinct** runs   |or invalid, the              |
|                     |                    |              |            |mail-only elections.       |implementation is required to|
|                     |                    |              |            |                           |assume **IsMailOnly** is     |
|                     |                    |              |            |                           |false.                       |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| LocalityId          | xs:IDREF           | **Required** | Single     |The **LocalityId** links to|If the **LocalityId** field  |
|                     |                    |              |            |the :doc:`locality         |is invalid or not present,   |
|                     |                    |              |            |<locality>` that comprises |the implementation is        |
|                     |                    |              |            |the precinct.              |required to ignore the       |
|                     |                    |              |            |                           |precinct element containing  |
|                     |                    |              |            |                           |it.                          |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| Name                | xs:string          | **Required** | Single     |The **Name** specifies the |If the **Name** field is     |
|                     |                    |              |            |precinct's name (or number |invalid or not present, the  |
|                     |                    |              |            |if no name exists).        |implementation is required to|
|                     |                    |              |            |                           |ignore the precinct element  |
|                     |                    |              |            |                           |containing it.               |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| Number              | xs:string          | Optional     | Single     |The **Number** specifies   |If the **Number** field is   |
|                     |                    |              |            |the precinct's number      |invalid or not present, the  |
|                     |                    |              |            |(e.g., 32 or 32A -- alpha  |implementation is required to|
|                     |                    |              |            |characters are             |ignore it.                   |
|                     |                    |              |            |legal). Should be used if  |                             |
|                     |                    |              |            |the **name** field is      |                             |
|                     |                    |              |            |populated by a name and not|                             |
|                     |                    |              |            |a number.                  |                             |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| PollingLocationId   | xs:IDREF           | Optional     | Repeats    |The **PollingLocationId**  |If the **PollingLocationId** |
|                     |                    |              |            |specifies a link to the    |field is invalid or not      |
|                     |                    |              |            |precinct's :doc:`polling   |present, the implementation  |
|                     |                    |              |            |location                   |is required to ignore it.    |
|                     |                    |              |            |<polling_location>`        |                             |
|                     |                    |              |            |object(s). Multiple        |                             |
|                     |                    |              |            |**PollingLocationId** tags |                             |
|                     |                    |              |            |may be specified, but this |                             |
|                     |                    |              |            |use should be reserved for |                             |
|                     |                    |              |            |when multiple              |                             |
|                     |                    |              |            |Election-Day-only vote     |                             |
|                     |                    |              |            |locations serve specific   |                             |
|                     |                    |              |            |precincts.                 |                             |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| PrecinctSplitName   | xs:string          | Optional     | Single     |The **PrecinctSplitName**  |If **PrecinctSplitName** is  |
|                     |                    |              |            |refers to name of the      |invalid or not present, the  |
|                     |                    |              |            |associated precinct split. |implementation is required to|
|                     |                    |              |            |                           |ignore it.                   |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+
| Ward                | xs:string          | Optional     | Single     |The **Ward** specifies the |If the **Ward** field is     |
|                     |                    |              |            |ward the precinct is       |missing or invalid, the      |
|                     |                    |              |            |contained within.          |implementation is required to|
|                     |                    |              |            |                           |ignore it.                   |
+---------------------+--------------------+--------------+------------+---------------------------+-----------------------------+

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
