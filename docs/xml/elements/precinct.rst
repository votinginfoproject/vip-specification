Precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of VipId,
Locality.Name, Precinct.Ward, Precinct.Name, and Precinct.Number should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

.. todo::

   Verify documentation is correct.
   
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| Tag                         | Data Type   | Optional/Required  | Description           | Error Handling                 |
+=============================+=============+====================+=======================+================================+
| Name                        | String      | **Required**       | The **Name** specifies| If the **Name** field is       |
|                             |             |                    |the precinct's name (or|invalid or not present, the     |
|                             |             |                    |number if no name      |implementation is required to   |
|                             |             |                    |exists).               |ignore the precinct element     |
|                             |             |                    |                       |containing it.                  |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| Number                      | String      | **Optional**       | The **Number**        | If the **Number** field is     |
|                             |             |                    |specifies the          |invalid or not present, the     |
|                             |             |                    |precinct's number      |implementation is required to   |
|                             |             |                    |(e.g., 32 or 32A --    |ignore it.                      |
|                             |             |                    |alpha characters are   |                                |
|                             |             |                    |legal). Should be used |                                |
|                             |             |                    |if the **name** field  |                                |
|                             |             |                    |is populated by a name |                                |
|                             |             |                    |and not a number.      |                                |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| LocalityId                  | IDREF       | **Required**       | The **LocalityId**    | If the **LocalityId** field is |
|                             |             |                    |links to the locality  |invalid or not present, the     |
|                             |             |                    |that comprises the     |implementation is required to   |
|                             |             |                    |precinct.              |ignore the precinct element     |
|                             |             |                    |                       |containing it.                  |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| ElectoralDistrictId         | IDREF       | Optional;          | The                   | If the **ElectoralDistrictId** |
|                             |             | multiple allowed   |**ElectoralDistrictId**|field is invalid or not present,|
|                             |             |                    |links to an electoral  |the implementation is required  |
|                             |             |                    |district (e.g.,        |to ignore the precinct element  |
|                             |             |                    |congressional district,|containing it.                  |
|                             |             |                    |state house district,  |                                |
|                             |             |                    |school board district) |                                |
|                             |             |                    |to which the precinct  |                                |
|                             |             |                    |belongs. ***Highly     |                                |
|                             |             |                    |Recommended*** if      |                                |
|                             |             |                    |candidate information  |                                |
|                             |             |                    |is to be               |                                |
|                             |             |                    |provided. Multiple     |                                |
|                             |             |                    |allowed and recommended|                                |
|                             |             |                    |to specify the         |                                |
|                             |             |                    |geography of multiple  |                                |
|                             |             |                    |electoral districts. If|                                |
|                             |             |                    |an electoral district  |                                |
|                             |             |                    |splits a precinct, use |                                |
|                             |             |                    |the                    |                                |
|                             |             |                    |**PrecinctSplitName**  |                                |
|                             |             |                    |object and do not      |                                |
|                             |             |                    |specify that particular|                                |
|                             |             |                    |electoral district in  |                                |
|                             |             |                    |this object.           |                                |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| Ward                        | String      | Optional           | The **Ward** specifies| If the **Ward** field is       |
|                             |             |                    |the ward the precinct  |missing or invalid, the         |
|                             |             |                    |is contained within.   |implementation is required to   |
|                             |             |                    |                       |ignore it.                      |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| IsMailOnly                  | Boolean     | Optional           | The **IsMailOnly**    | If the **IsMailOnly** field is |
|                             |             |                    |specifies whether      |missing or invalid, the         |
|                             |             |                    |voters in the precinct |implementation is required to   |
|                             |             |                    |vote only by mailing   |default to "no".                |
|                             |             |                    |their ballots (with the|                                |
|                             |             |                    |possible option of     |                                |
|                             |             |                    |dropping off their     |                                |
|                             |             |                    |ballots as well). Valid|                                |
|                             |             |                    |values are "yes" and   |                                |
|                             |             |                    |"no", with "no" being  |                                |
|                             |             |                    |the default if the tag |                                |
|                             |             |                    |is not present.        |                                |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| PollingLocationId           | IDREF       | Optional;          | The                   | If the **PollingLocationId**   |
|                             |             | multiple allowed   |**PollingLocationId**  |field is missing or invalid, the|
|                             |             |                    |specifies a link to the|implementation is required to   |
|                             |             |                    |precinct's polling     |ignore it.                      |
|                             |             |                    |location               |                                |
|                             |             |                    |object. Multiple       |                                |
|                             |             |                    |**PollingLocationId**  |                                |
|                             |             |                    |tags may be specified, |                                |
|                             |             |                    |but this use should be |                                |
|                             |             |                    |reserved for when      |                                |
|                             |             |                    |multiple               |                                |
|                             |             |                    |Election-Day-only vote |                                |
|                             |             |                    |locations serve        |                                |
|                             |             |                    |specific precincts.    |                                |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+
| BallotStyleId               | IDREF       | Optional           | The **BallotStyleId** | If the **BallotStyleId** field |
|                             |             |                    |links to the ballot on |is missing or invalid, the      |
|                             |             |                    |which a person who     |implementation is required to   |
|                             |             |                    |lives in this precinct |ignore it.                      |
|                             |             |                    |will vote.             |                                |
+-----------------------------+-------------+--------------------+-----------------------+--------------------------------+

.. code-block:: xml
   :linenos:

   <Precinct id="4567">
     <Name>Camelot</Name>
     <LocalityId>568</LocalityId>
     <ElectoralDistrictId>100044</ElectoralDistrictId>
     <ElectoralDistrictId>100055</ElectoralDistrictId>
     <PollingLocationId>3845</PollingLocationId>
   </Precinct>
