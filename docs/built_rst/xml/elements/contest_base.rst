.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-contest-base:

ContestBase
===========

A base model for all Contest types: :ref:`multi-xml-ballot-measure-contest`,
:ref:`multi-xml-candidate-contest`, :ref:`multi-xml-party-contest`,
and :ref:`multi-xml-retention-contest` (NB: the latter because it extends
:ref:`multi-xml-ballot-measure-contest`).

+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                           | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                         |              |              |                                          | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                           | Optional     | Single       | References a set of BallotSelections,    | If the field is invalid or not present,  |
|                         |                                         |              |              | which could be of any selection type     | then the implementation should ignore    |
|                         |                                         |              |              | that extends                             | it.                                      |
|                         |                                         |              |              | :ref:`multi-xml-ballot-selection-base`.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         |                                         |              |              | the ballot.                              | present, then the implementation should  |
|                         |                                         |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         |                                         |              |              | the ballot.                              | present, then the implementation should  |
|                         |                                         |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                            | **Required** | Single       | References an                            | If the field is invalid, then the        |
|                         |                                         |              |              | :ref:`multi-xml-electoral-district`      | implementation should ignore it.         |
|                         |                                         |              |              | element that represents the geographical |                                          |
|                         |                                         |              |              | scope of the contest.                    |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                         |                                         |              |              | electorate for this contest past the     | present, then the implementation should  |
|                         |                                         |              |              | usual, "all registered voters"           | ignore it.                               |
|                         |                                         |              |              | electorate. This subtag will most often  |                                          |
|                         |                                         |              |              | be used for primaries and local          |                                          |
|                         |                                         |              |              | elections. In primaries, voters may have |                                          |
|                         |                                         |              |              | to be registered as a specific party to  |                                          |
|                         |                                         |              |              | vote, or there may be special rules for  |                                          |
|                         |                                         |              |              | which ballot a voter can pull. In some   |                                          |
|                         |                                         |              |              | local elections, non-citizens can vote.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers for a contest that     | If the element is invalid or not         |
|                         |                                         |              |              | links to another source of information.  | present, then the implementation should  |
|                         |                                         |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                          | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                         |              |              | contest are rotated.                     | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                           | Optional     | Single       | Name of the contest, not necessarily how | If the field is invalid or not present,  |
|                         |                                         |              |              | it appears on the ballot (NB:            | then the implementation should ignore    |
|                         |                                         |              |              | BallotTitle should be used for this      | it.                                      |
|                         |                                         |              |              | purpose).                                |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                          | Optional     | Single       | Order in which the contests are listed   | If the field is invalid or not present,  |
|                         |                                         |              |              | on the ballot. This is the default       | then the implementation should ignore    |
|                         |                                         |              |              | ordering, and can be overrides by data   | it.                                      |
|                         |                                         |              |              | in a :ref:`multi-xml-ballot-style`       |                                          |
|                         |                                         |              |              | element.                                 |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`multi-xml-vote-variation`         | Optional     | Single       | Vote variation associated with the       | If the field is invalid or not present,  |
|                         |                                         |              |              | contest (e.g. n-of-m, majority, et al).  | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                           | Optional     | Single       | If "other" is selected as the            | If the field is invalid or not present,  |
|                         |                                         |              |              | **VoteVariation**, the name of the       | then the implementation should ignore    |
|                         |                                         |              |              | variation can be specified here.         | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
