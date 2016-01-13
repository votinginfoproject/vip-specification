.. This file is auto-generated.  Do not edit it by hand!

+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| Tag                     | Data Type                                       | Required?    | Repeats?     | Description                                       | Error Handling                           |
+=========================+=================================================+==============+==============+===================================================+==========================================+
| Abbreviation            | xs:string                                       | Optional     | Single       | An abbreviation for the contest.                  | If the field is invalid or not present,  |
|                         |                                                 |              |              |                                                   | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| BallotSelectionId       | xs:IDREF                                        | Optional     | Repeats      | References a particular BallotSelection, which    | If the field is invalid or not present,  |
|                         |                                                 |              |              | could be of any selection type that extends       | then the implementation should ignore    |
|                         |                                                 |              |              | :doc:`BallotSelectionBase                         | it.                                      |
|                         |                                                 |              |              | </built_rst/xml/elements/ballot_selection_base>`. |                                          |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| BallotSubTitle          | :doc:`InternationalizedText                     | Optional     | Single       | Subtitle of the contest as it appears on the      | If the element is invalid or not         |
|                         | <internationalized_text>`                       |              |              | ballot.                                           | present, then the implementation should  |
|                         |                                                 |              |              |                                                   | ignore it.                               |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| BallotTitle             | :doc:`InternationalizedText                     | Optional     | Single       | Title of the contest as it appears on the ballot. | If the element is invalid or not         |
|                         | <internationalized_text>`                       |              |              |                                                   | present, then the implementation should  |
|                         |                                                 |              |              |                                                   | ignore it.                               |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | xs:IDREF                                        | Optional     | Single       | References an :doc:`ElectoralDistrict             | If the field is invalid or not present,  |
|                         |                                                 |              |              | <electoral_district>` element that represents the | then the implementation should ignore    |
|                         |                                                 |              |              | geographical scope of the contest.                | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ElectorateSpecification | :doc:`InternationalizedText                     | Optional     | Single       | Specifies any changes to the eligible electorate  | If the element is invalid or not         |
|                         | <internationalized_text>`                       |              |              | for this contest past the usual, "all registered  | present, then the implementation should  |
|                         |                                                 |              |              | voters" electorate. This subtag will most often   | ignore it.                               |
|                         |                                                 |              |              | be used for primaries and local elections. In     |                                          |
|                         |                                                 |              |              | primaries, voters may have to be registered as a  |                                          |
|                         |                                                 |              |              | specific party to vote, or there may be special   |                                          |
|                         |                                                 |              |              | rules for which ballot a voter can pull. In some  |                                          |
|                         |                                                 |              |              | local elections, non-citizens can vote.           |                                          |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers for a contest that links to     | If the element is invalid or not         |
|                         | </built_rst/xml/elements/external_identifiers>` |              |              | another source of information.                    | present, then the implementation should  |
|                         |                                                 |              |              |                                                   | ignore it.                               |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| HasRotation             | xs:boolean                                      | Optional     | Single       | Indicates whether the selections in the contest   | If the field is invalid or not present,  |
|                         |                                                 |              |              | are rotated.                                      | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| Name                    | xs:string                                       | Optional     | Single       | Name of the contest, not necessarily how it       | If the field is invalid or not present,  |
|                         |                                                 |              |              | appears on the ballot (NB: BallotTitle should be  | then the implementation should ignore    |
|                         |                                                 |              |              | used for this purpose).                           | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| SequenceOrder           | xs:integer                                      | Optional     | Single       | Order in which the candidates are listed on the   | If the field is invalid or not present,  |
|                         |                                                 |              |              | ballot.                                           | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| VoteVariation           | :doc:`VoteVariation                             | Optional     | Single       | Vote variation associated with the contest (e.g.  | If the field is invalid or not present,  |
|                         | <../enumerations/vote_variation>`               |              |              | n-of-m, majority, et al).                         | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| OtherVoteVariation      | xs:string                                       | Optional     | Single       | If "other" is selected as the **VoteVariation**,  | If the field is invalid or not present,  |
|                         |                                                 |              |              | the name of the variation can be specified here.  | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
