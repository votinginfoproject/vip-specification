.. This file is auto-generated.  Do not edit it by hand!

ContestBase
===========

A base model for all Contest types: :doc:`BallotMeasureContest <ballot_measure_contest>`,
:doc:`CandidateContest <candidate_contest>`, :doc:`PartyContest <party_contest>`,
and :doc:`RetentionContest <retention_contest>` (NB: the latter because it extends
:doc:`BallotMeasureContest <ballot_measure_contest>`).

+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+=======================================+==============+==============+==========================================+==========================================+
| Abbreviation            | xs:string                             | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                       |              |              |                                          | then the implementation should ignore    |
|                         |                                       |              |              |                                          | it.                                      |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | xs:IDREFS                             | Optional     | Single       | References a set of BallotSelections,    | If the field is invalid or not present,  |
|                         |                                       |              |              | which could be of any selection type     | then the implementation should ignore    |
|                         |                                       |              |              | that extends :doc:`BallotSelectionBase   | it.                                      |
|                         |                                       |              |              | </xml/elements/ballot_selection_base>`.  |                                          |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :doc:`InternationalizedText           | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         | <internationalized_text>`             |              |              | the ballot.                              | present, then the implementation should  |
|                         |                                       |              |              |                                          | ignore it.                               |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :doc:`InternationalizedText           | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         | <internationalized_text>`             |              |              | the ballot.                              | present, then the implementation should  |
|                         |                                       |              |              |                                          | ignore it.                               |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | xs:IDREF                              | Optional     | Single       | References an :doc:`ElectoralDistrict    | If the field is invalid or not present,  |
|                         |                                       |              |              | <electoral_district>` element that       | then the implementation should ignore    |
|                         |                                       |              |              | represents the geographical scope of the | it.                                      |
|                         |                                       |              |              | contest.                                 |                                          |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :doc:`InternationalizedText           | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                         | <internationalized_text>`             |              |              | electorate for this contest past the     | present, then the implementation should  |
|                         |                                       |              |              | usual, "all registered voters"           | ignore it.                               |
|                         |                                       |              |              | electorate. This subtag will most often  |                                          |
|                         |                                       |              |              | be used for primaries and local          |                                          |
|                         |                                       |              |              | elections. In primaries, voters may have |                                          |
|                         |                                       |              |              | to be registered as a specific party to  |                                          |
|                         |                                       |              |              | vote, or there may be special rules for  |                                          |
|                         |                                       |              |              | which ballot a voter can pull. In some   |                                          |
|                         |                                       |              |              | local elections, non-citizens can vote.  |                                          |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :doc:`ExternalIdentifiers             | Optional     | Single       | Other identifiers for a contest that     | If the element is invalid or not         |
|                         | </xml/elements/external_identifiers>` |              |              | links to another source of information.  | present, then the implementation should  |
|                         |                                       |              |              |                                          | ignore it.                               |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | xs:boolean                            | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                       |              |              | contest are rotated.                     | then the implementation should ignore    |
|                         |                                       |              |              |                                          | it.                                      |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | xs:string                             | Optional     | Single       | Name of the contest, not necessarily how | If the field is invalid or not present,  |
|                         |                                       |              |              | it appears on the ballot (NB:            | then the implementation should ignore    |
|                         |                                       |              |              | BallotTitle should be used for this      | it.                                      |
|                         |                                       |              |              | purpose).                                |                                          |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | xs:integer                            | Optional     | Single       | Order in which the candidates are listed | If the field is invalid or not present,  |
|                         |                                       |              |              | on the ballot.                           | then the implementation should ignore    |
|                         |                                       |              |              |                                          | it.                                      |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :doc:`VoteVariation                   | Optional     | Single       | Vote variation associated with the       | If the field is invalid or not present,  |
|                         | <../enumerations/vote_variation>`     |              |              | contest (e.g. n-of-m, majority, et al).  | then the implementation should ignore    |
|                         |                                       |              |              |                                          | it.                                      |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | xs:string                             | Optional     | Single       | If "other" is selected as the            | If the field is invalid or not present,  |
|                         |                                       |              |              | **VoteVariation**, the name of the       | then the implementation should ignore    |
|                         |                                       |              |              | variation can be specified here.         | it.                                      |
+-------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
