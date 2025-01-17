.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate-contest:

CandidateContest
================

CandidateContest extends :ref:`multi-xml-contest-base` and represents a contest among
candidates.

+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+================+==============+==============+==========================================+==========================================+
| NumberElected   | ``xs:integer`` | Optional     | Single       | Number of candidates that are elected in |                                          |
|                 |                |              |              | the contest (i.e. "N" of N-of-M).        |                                          |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeIds       | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                 |                |              |              | :ref:`multi-xml-office` elements, if     |                                          |
|                 |                |              |              | available, which give additional         |                                          |
|                 |                |              |              | information about the offices. **Note:** |                                          |
|                 |                |              |              | the order of the office IDs **must** be  |                                          |
|                 |                |              |              | in the same order as the candidates      |                                          |
|                 |                |              |              | listed in `BallotSelectionIds`. E.g., if |                                          |
|                 |                |              |              | the various `BallotSelectionIds`         |                                          |
|                 |                |              |              | reference                                |                                          |
|                 |                |              |              | :ref:`multi-xml-candidate-selection`     |                                          |
|                 |                |              |              | elements which reference the candidate   |                                          |
|                 |                |              |              | for President first and Vice-President   |                                          |
|                 |                |              |              | second, the `OfficeIds` should reference |                                          |
|                 |                |              |              | the office of President first and the    |                                          |
|                 |                |              |              | office of Vice-President second.         |                                          |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrimaryPartyIds | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-xml-party`        |                                          |
|                 |                |              |              | elements, if the contest is related to a |                                          |
|                 |                |              |              | particular party.                        |                                          |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VotesAllowed    | ``xs:integer`` | Optional     | Single       | Maximum number of votes/write-ins per    |                                          |
|                 |                |              |              | voter in this contest.                   |                                          |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateContest id="cc20003">
      <BallotSelectionIds>cs10961 cs10962 cs10963</BallotSelectionIds>
      <BallotTitle>
        <Text language="en">Governor of Virginia</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Governor</Name>
      <NumberElected>1</NumberElected>
      <OfficeId>off0000</OfficeId>
      <VotesAllowed>1</VotesAllowed>
   </CandidateContest>


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
