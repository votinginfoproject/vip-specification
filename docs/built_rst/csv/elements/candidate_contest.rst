.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-candidate-contest:

candidate_contest
=================

CandidateContest extends :ref:`multi-csv-contest-base` and represents a contest among
candidates.

+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+================+==============+==============+==========================================+==========================================+
| number_elected    | ``xs:integer`` | Optional     | Single       | Number of candidates that are elected in |                                          |
|                   |                |              |              | the contest (i.e. "N" of N-of-M).        |                                          |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_ids        | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                   |                |              |              | :ref:`multi-csv-office` elements, if     |                                          |
|                   |                |              |              | available, which give additional         |                                          |
|                   |                |              |              | information about the offices. **Note:** |                                          |
|                   |                |              |              | the order of the office IDs **must** be  |                                          |
|                   |                |              |              | in the same order as the candidates      |                                          |
|                   |                |              |              | listed in `BallotSelectionIds`. E.g., if |                                          |
|                   |                |              |              | the various `BallotSelectionIds`         |                                          |
|                   |                |              |              | reference                                |                                          |
|                   |                |              |              | :ref:`multi-csv-candidate-selection`     |                                          |
|                   |                |              |              | elements which reference the candidate   |                                          |
|                   |                |              |              | for President first and Vice-President   |                                          |
|                   |                |              |              | second, the `OfficeIds` should reference |                                          |
|                   |                |              |              | the office of President first and the    |                                          |
|                   |                |              |              | office of Vice-President second.         |                                          |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| primary_party_ids | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-csv-party`        |                                          |
|                   |                |              |              | elements, if the contest is related to a |                                          |
|                   |                |              |              | particular party.                        |                                          |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| votes_allowed     | ``xs:integer`` | Optional     | Single       | Maximum number of votes/write-ins per    |                                          |
|                   |                |              |              | voter in this contest.                   |                                          |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,electoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation,number_elected,office_ids,primary_party_ids,votes_allowed
    cancon001,SE-1,bs001 bs002,,Governor of Virginia,ed001,all registered voters,fips,,49,true,Governor,1,,,1,off001,par01,1
    cancon002,SE-2,bs003 bs004,,Lieutenant Governor of Virginia,ed001,all registered voters,fips,,49,true,Lt Governor,2,,,1,off002,par01,1


.. _multi-csv-contest-base:

contest_base
------------

A base model for all Contest types: :ref:`multi-csv-ballot-measure-contest`,
:ref:`multi-csv-candidate-contest`, :ref:`multi-csv-party-contest`,
and :ref:`multi-csv-retention-contest` (NB: the latter because it extends
:ref:`multi-csv-ballot-measure-contest`).

+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                   | Optional     | Single       | An abbreviation for the contest.         |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                   | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                          |                                 |              |              | which could be of any selection type     |                                          |
|                          |                                 |              |              | that extends                             |                                          |
|                          |                                 |              |              | :ref:`multi-csv-ballot-selection-base`.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                   | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                          |                                 |              |              | the ballot.                              |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                   | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                          |                                 |              |              | the ballot.                              |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                    | **Required** | Single       | References an                            |                                          |
|                          |                                 |              |              | :ref:`multi-csv-electoral-district`      |                                          |
|                          |                                 |              |              | element that represents the geographical |                                          |
|                          |                                 |              |              | scope of the contest.                    |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                   | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                          |                                 |              |              | electorate for this contest past the     |                                          |
|                          |                                 |              |              | usual, "all registered voters"           |                                          |
|                          |                                 |              |              | electorate. This subtag will most often  |                                          |
|                          |                                 |              |              | be used for primaries and local          |                                          |
|                          |                                 |              |              | elections. In primaries, voters may have |                                          |
|                          |                                 |              |              | to be registered as a specific party to  |                                          |
|                          |                                 |              |              | vote, or there may be special rules for  |                                          |
|                          |                                 |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                 |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                   | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                          |                                 |              |              | links to another source of information.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                  | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                          |                                 |              |              | contest are rotated.                     |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                   | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                          |                                 |              |              | it appears on the ballot (NB:            |                                          |
|                          |                                 |              |              | BallotTitle should be used for this      |                                          |
|                          |                                 |              |              | purpose).                                |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                  | Optional     | Single       | Order in which the contests are listed   |                                          |
|                          |                                 |              |              | on the ballot. This is the default       |                                          |
|                          |                                 |              |              | ordering, and can be overrides by data   |                                          |
|                          |                                 |              |              | in a :ref:`multi-csv-ballot-style`       |                                          |
|                          |                                 |              |              | element.                                 |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`multi-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       |                                          |
|                          |                                 |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``        | Optional     | Single       | If "other" is selected as the            |                                          |
|                          |                                 |              |              | **VoteVariation**, the name of the       |                                          |
|                          |                                 |              |              | variation can be specified here.         |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
