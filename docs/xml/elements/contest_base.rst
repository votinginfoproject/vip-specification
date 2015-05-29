ContestBase
===========

A base model for all Contest types: :doc:`BallotMeasureContest <ballot_measure_contest>`,
:doc:`CandidateContest <candidate_contest>`, :doc:`PartyContest <party_contest>`,
and :doc:`RetentionContest <retention_contest>` (NB: the latter because it extends
:doc:`BallotMeasureContest <ballot_measure_contest>`).

+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| Tag                     | Data Type                       | Required? | Repeats? | Description              | Error Handling       |
|                         |                                 |           |          |                          |                      |
+=========================+=================================+===========+==========+==========================+======================+
| Abbreviation            | xs:string                       | Optional  | Single   |An abbreviation for the   |If the field is       |
|                         |                                 |           |          |contest.                  |invalid or not        |
|                         |                                 |           |          |                          |present, the          |
|                         |                                 |           |          |                          |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| BallotSelectionId       | xs:IDREF                        | Optional  | Repeats  |References a particular   |If the field is       |
|                         |                                 |           |          |BallotSelection, which    |invalid or not        |
|                         |                                 |           |          |could be of any selection |present, the          |
|                         |                                 |           |          |type that extends         |implementation should |
|                         |                                 |           |          |:doc:`BallotSelectionBase |ignore it.            |
|                         |                                 |           |          |<ballot_selection_base>`. |                      |
|                         |                                 |           |          |                          |                      |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| BallotSubTitle          |:doc:`InternationalizedText      | Optional  | Single   |Subtitle of the contest as|If the element is     |
|                         |<internationalized_text>`        |           |          |it appears on the ballot. |invalid or not        |
|                         |                                 |           |          |                          |present, the          |
|                         |                                 |           |          |                          |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| BallotTitle             |:doc:`InternationalizedText      | Optional  | Single   |Title of the contest as it|If the element is     |
|                         |<internationalized_text>`        |           |          |appears on the ballot.    |invalid or not        |
|                         |                                 |           |          |                          |present, the          |
|                         |                                 |           |          |                          |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| ElectoralDistrictId     | xs:IDREF                        | Optional  | Single   |References an             |If the field is       |
|                         |                                 |           |          |:doc:`ElectoralDistrict   |invalid or not        |
|                         |                                 |           |          |<electoral_district>`     |present, the          |
|                         |                                 |           |          |element that represents   |implementation should |
|                         |                                 |           |          |the geographical scope of |ignore it.            |
|                         |                                 |           |          |the contest.              |                      |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| ElectorateSpecification |:doc:`InternationalizedText      | Optional  | Single   |Specifies any changes to  |If the element is     |
|                         |<internationalized_text>`        |           |          |the eligible electorate   |invalid or not        |
|                         |                                 |           |          |for this contest past the |present, the          |
|                         |                                 |           |          |usual, "all registered    |implementation should |
|                         |                                 |           |          |voters" electorate. This  |ignore it.            |
|                         |                                 |           |          |subtag will most often be |                      |
|                         |                                 |           |          |used for primaries and    |                      |
|                         |                                 |           |          |local elections. In       |                      |
|                         |                                 |           |          |primaries, voters may have|                      |
|                         |                                 |           |          |to be registered as a     |                      |
|                         |                                 |           |          |specific party to vote, or|                      |
|                         |                                 |           |          |there may be special rules|                      |
|                         |                                 |           |          |for which ballot a voter  |                      |
|                         |                                 |           |          |can pull. In some local   |                      |
|                         |                                 |           |          |elections, non-citizens   |                      |
|                         |                                 |           |          |can vote.                 |                      |
|                         |                                 |           |          |                          |                      |
|                         |                                 |           |          |                          |                      |
|                         |                                 |           |          |                          |                      |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| ExternalIdentifiers     |:doc:`ExternalIdentifiers        | Optional  | Single   |Other identifiers for a   |If the element is     |
|                         |<external_identifiers>`          |           |          |contest that links to     |invalid or not        |
|                         |                                 |           |          |another source of         |present, the          |
|                         |                                 |           |          |information.              |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
|                         |                                 |           |          |                          |                      |
|                         |                                 |           |          |                          |                      |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| HasRotation             | xs:boolean                      | Optional  | Single   |Indicates whether the     |If the field is       |
|                         |                                 |           |          |selections in the contest |invalid or not        |
|                         |                                 |           |          |are rotated.              |present, the          |
|                         |                                 |           |          |                          |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| Name                    | xs:string                       | Optional  | Single   |Name of the contest, not  |If the field is       |
|                         |                                 |           |          |necessarily how it appears|invalid or not        |
|                         |                                 |           |          |on the ballot (NB:        |present, the          |
|                         |                                 |           |          |BallotTitle should be used|implementation should |
|                         |                                 |           |          |for this purpose).        |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| SequenceOrder           | xs:integer                      | Optional  | Single   |Order in which the        |If the field is       |
|                         |                                 |           |          |candidates are listed on  |invalid or not        |
|                         |                                 |           |          |the ballot.               |present, the          |
|                         |                                 |           |          |                          |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| VoteVariation           |:doc:`VoteVariation              | Optional  | Single   |Vote variation associated |If the element is     |
|                         |<../enumerations/vote_variation>`|           |          |with the contest          |invalid or not        |
|                         |                                 |           |          |(e.g. n-of-m, majority, et|present, the          |
|                         |                                 |           |          |al).                      |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
| OtherVoteVariation      | xs:string                       | Optional  | Single   |If "other" is selected as |If the field is       |
|                         |                                 |           |          |the **VoteVariation**, the|invalid or not        |
|                         |                                 |           |          |name of the variation can |present, the          |
|                         |                                 |           |          |be specified here.        |implementation should |
|                         |                                 |           |          |                          |ignore it.            |
+-------------------------+---------------------------------+-----------+----------+--------------------------+----------------------+
