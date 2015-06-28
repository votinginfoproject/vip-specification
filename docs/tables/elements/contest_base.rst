.. This file is auto-generated.  Do not edit it by hand!

+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+===================================+==============+==============+==========================================+==========================================+
| Abbreviation            | xs:string                         | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                   |              |              |                                          | the implementation should ignore it.     |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionId       | xs:IDREF                          | Optional     | Repeats      | References a particular BallotSelection, | If the field is invalid or not present,  |
|                         |                                   |              |              | which could be of any selection type     | the implementation should ignore it.     |
|                         |                                   |              |              | that extends :doc:`BallotSelectionBase   |                                          |
|                         |                                   |              |              | <ballot_selection_base>`.                |                                          |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :doc:`InternationalizedText       | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         | <internationalized_text>`         |              |              | the ballot.                              | present, the implementation should       |
|                         |                                   |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :doc:`InternationalizedText       | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         | <internationalized_text>`         |              |              | the ballot.                              | present, the implementation should       |
|                         |                                   |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | xs:IDREF                          | Optional     | Single       | References an :doc:`ElectoralDistrict    | If the field is invalid or not present,  |
|                         |                                   |              |              | <electoral_district>` element that       | the implementation should ignore it.     |
|                         |                                   |              |              | represents the geographical scope of the |                                          |
|                         |                                   |              |              | contest.                                 |                                          |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :doc:`InternationalizedText       | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                         | <internationalized_text>`         |              |              | electorate for this contest past the     | present, the implementation should       |
|                         |                                   |              |              | usual, "all registered voters"           | ignore it.                               |
|                         |                                   |              |              | electorate. This subtag will most often  |                                          |
|                         |                                   |              |              | be used for primaries and local          |                                          |
|                         |                                   |              |              | elections. In primaries, voters may have |                                          |
|                         |                                   |              |              | to be registered as a specific party to  |                                          |
|                         |                                   |              |              | vote, or there may be special rules for  |                                          |
|                         |                                   |              |              | which ballot a voter can pull. In some   |                                          |
|                         |                                   |              |              | local elections, non-citizens can vote.  |                                          |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :doc:`ExternalIdentifiers         | Optional     | Single       | Other identifiers for a contest that     | If the element is invalid or not         |
|                         | <external_identifiers>`           |              |              | links to another source of information.  | present, the implementation should       |
|                         |                                   |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | xs:boolean                        | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                   |              |              | contest are rotated.                     | the implementation should ignore it.     |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | xs:string                         | Optional     | Single       | Name of the contest, not necessarily how | If the field is invalid or not present,  |
|                         |                                   |              |              | it appears on the ballot (NB:            | the implementation should ignore it.     |
|                         |                                   |              |              | BallotTitle should be used for this      |                                          |
|                         |                                   |              |              | purpose).                                |                                          |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | xs:integer                        | Optional     | Single       | Order in which the candidates are listed | If the field is invalid or not present,  |
|                         |                                   |              |              | on the ballot.                           | the implementation should ignore it.     |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :doc:`VoteVariation               | Optional     | Single       | Vote variation associated with the       | If the element is invalid or not         |
|                         | <../enumerations/vote_variation>` |              |              | contest (e.g. n-of-m, majority, et al).  | present, the implementation should       |
|                         |                                   |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | xs:string                         | Optional     | Single       | If "other" is selected as the            | If the field is invalid or not present,  |
|                         |                                   |              |              | **VoteVariation**, the name of the       | the implementation should ignore it.     |
|                         |                                   |              |              | variation can be specified here.         |                                          |
+-------------------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
