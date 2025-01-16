.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-party-contest:

PartyContest
============

An extension of :ref:`multi-xml-contest-base` which describes a contest in
which the possible ballot selections are of type :ref:`multi-xml-party-selection`. These could include contests in which straight-party
selections are allowed, or party-list contests (although these are more common
outside of the United States).


.. _multi-xml-contest-base:

ContestBase
-----------

A base model for all Contest types: :ref:`multi-xml-ballot-measure-contest`,
:ref:`multi-xml-candidate-contest`, :ref:`multi-xml-party-contest`,
and :ref:`multi-xml-retention-contest` (NB: the latter because it extends
:ref:`multi-xml-ballot-measure-contest`).

+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                           | Optional     | Single       | An abbreviation for the contest.         |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                           | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                         |                                         |              |              | which could be of any selection type     |                                          |
|                         |                                         |              |              | that extends                             |                                          |
|                         |                                         |              |              | :ref:`multi-xml-ballot-selection-base`.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                         |                                         |              |              | the ballot.                              |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                         |                                         |              |              | the ballot.                              |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                            | **Required** | Single       | References an                            |                                          |
|                         |                                         |              |              | :ref:`multi-xml-electoral-district`      |                                          |
|                         |                                         |              |              | element that represents the geographical |                                          |
|                         |                                         |              |              | scope of the contest.                    |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                         |                                         |              |              | electorate for this contest past the     |                                          |
|                         |                                         |              |              | usual, "all registered voters"           |                                          |
|                         |                                         |              |              | electorate. This subtag will most often  |                                          |
|                         |                                         |              |              | be used for primaries and local          |                                          |
|                         |                                         |              |              | elections. In primaries, voters may have |                                          |
|                         |                                         |              |              | to be registered as a specific party to  |                                          |
|                         |                                         |              |              | vote, or there may be special rules for  |                                          |
|                         |                                         |              |              | which ballot a voter can pull. In some   |                                          |
|                         |                                         |              |              | local elections, non-citizens can vote.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                         |                                         |              |              | links to another source of information.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                          | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                         |                                         |              |              | contest are rotated.                     |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                           | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                         |                                         |              |              | it appears on the ballot (NB:            |                                          |
|                         |                                         |              |              | BallotTitle should be used for this      |                                          |
|                         |                                         |              |              | purpose).                                |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                          | Optional     | Single       | Order in which the contests are listed   |                                          |
|                         |                                         |              |              | on the ballot. This is the default       |                                          |
|                         |                                         |              |              | ordering, and can be overrides by data   |                                          |
|                         |                                         |              |              | in a :ref:`multi-xml-ballot-style`       |                                          |
|                         |                                         |              |              | element.                                 |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`multi-xml-vote-variation`         | Optional     | Single       | Vote variation associated with the       |                                          |
|                         |                                         |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                           | Optional     | Single       | If "other" is selected as the            |                                          |
|                         |                                         |              |              | **VoteVariation**, the name of the       |                                          |
|                         |                                         |              |              | variation can be specified here.         |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
