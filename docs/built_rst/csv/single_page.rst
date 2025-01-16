.. This file is auto-generated.  Do not edit it by hand!

.. _single-csv:

CSV Elements & Enumerations (Single Page)
=========================================

.. contents::
   :local:


.. _single-csv-elements:

Elements
--------


.. _single-csv-ballot-measure-contest:

ballot_measure_contest
~~~~~~~~~~~~~~~~~~~~~~

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends :ref:`single-csv-contest-base`.

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| con_statement     | ``xs:string`` | Optional     | Single       | Specifies a statement in opposition to   |                                          |
|                   |               |              |              | the referendum. It does not necessarily  |                                          |
|                   |               |              |              | appear on the ballot.                    |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| effect_of_abstain | ``xs:string`` | Optional     | Single       | Specifies what effect abstaining (i.e.   |                                          |
|                   |               |              |              | not voting) on this proposition will     |                                          |
|                   |               |              |              | have (i.e. whether abstaining is         |                                          |
|                   |               |              |              | considered a vote against it).           |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_text         | ``xs:string`` | Optional     | Single       | Specifies the full text of the           |                                          |
|                   |               |              |              | referendum as it appears on the ballot.  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| info_uri          | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that links to additional |                                          |
|                   |               |              |              | information about the referendum.        |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| passage_threshold | ``xs:string`` | Optional     | Single       | Specifies the threshold of votes that    |                                          |
|                   |               |              |              | the referendum needs in order to pass.   |                                          |
|                   |               |              |              | The default is a simple majority (i.e.   |                                          |
|                   |               |              |              | 50% plus one vote). Other common         |                                          |
|                   |               |              |              | thresholds are "three-fifths" and        |                                          |
|                   |               |              |              | "two-thirds". If there are `competing    |                                          |
|                   |               |              |              | initiatives`_, information about their   |                                          |
|                   |               |              |              | effect on the passage of the             |                                          |
|                   |               |              |              | BallotMeasureContest would go here.      |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pro_statement     | ``xs:string`` | Optional     | Single       | Specifies a statement in favor of the    |                                          |
|                   |               |              |              | referendum. It does not necessarily      |                                          |
|                   |               |              |              | appear on the ballot.                    |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| summary_text      | ``xs:string`` | Optional     | Single       | Specifies a short summary of the         |                                          |
|                   |               |              |              | referendum that is on the ballot, below  |                                          |
|                   |               |              |              | the title, but above the text.           |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type              | ``xs:string`` | Optional     | Single       | Specifies the particular type of ballot  |                                          |
|                   |               |              |              | measure. Must be one of the valid        |                                          |
|                   |               |              |              | :ref:`single-csv-ballot-measure-type`    |                                          |
|                   |               |              |              | options.                                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type        | ``xs:string`` | Optional     | Single       | Allows for cataloging a new              |                                          |
|                   |               |              |              | :ref:`single-csv-ballot-measure-type`    |                                          |
|                   |               |              |              | option, when Type is specified as        |                                          |
|                   |               |              |              | "other."                                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,elecoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation,con_statement,effect_of_abstain,full_text,info_uri,passage_threshold,pro_statement,summary_text,type,other_type
    bmc0001,HB2,bs001 bs002 bs003,Raising levy for School Bond,School Bond Issue,ed001,all registered voters,,54,false,School Bond,42,majority,,This is no good.,No effect,A measure to do raise funds for etc etc,www.ballotmeasure.com,two-thirds,Everything will be great.,It’s a referendum about school funding,referendum,


.. _single-csv-contest-base:

contest_base
^^^^^^^^^^^^

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`,
:ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`,
and :ref:`single-csv-retention-contest` (NB: the latter because it extends
:ref:`single-csv-ballot-measure-contest`).

+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                    | Optional     | Single       | An abbreviation for the contest.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                    | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                          |                                  |              |              | which could be of any selection type     |                                          |
|                          |                                  |              |              | that extends                             |                                          |
|                          |                                  |              |              | :ref:`single-csv-ballot-selection-base`. |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                    | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                    | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                     | **Required** | Single       | References an                            |                                          |
|                          |                                  |              |              | :ref:`single-csv-electoral-district`     |                                          |
|                          |                                  |              |              | element that represents the geographical |                                          |
|                          |                                  |              |              | scope of the contest.                    |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                    | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                          |                                  |              |              | electorate for this contest past the     |                                          |
|                          |                                  |              |              | usual, "all registered voters"           |                                          |
|                          |                                  |              |              | electorate. This subtag will most often  |                                          |
|                          |                                  |              |              | be used for primaries and local          |                                          |
|                          |                                  |              |              | elections. In primaries, voters may have |                                          |
|                          |                                  |              |              | to be registered as a specific party to  |                                          |
|                          |                                  |              |              | vote, or there may be special rules for  |                                          |
|                          |                                  |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                  |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                    | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                          |                                  |              |              | links to another source of information.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                   | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                          |                                  |              |              | contest are rotated.                     |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                    | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                          |                                  |              |              | it appears on the ballot (NB:            |                                          |
|                          |                                  |              |              | BallotTitle should be used for this      |                                          |
|                          |                                  |              |              | purpose).                                |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                   | Optional     | Single       | Order in which the contests are listed   |                                          |
|                          |                                  |              |              | on the ballot. This is the default       |                                          |
|                          |                                  |              |              | ordering, and can be overrides by data   |                                          |
|                          |                                  |              |              | in a :ref:`single-csv-ballot-style`      |                                          |
|                          |                                  |              |              | element.                                 |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       |                                          |
|                          |                                  |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``         | Optional     | Single       | If "other" is selected as the            |                                          |
|                          |                                  |              |              | **VoteVariation**, the name of the       |                                          |
|                          |                                  |              |              | variation can be specified here.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-ballot-measure-selection:

ballot_measure_selection
~~~~~~~~~~~~~~~~~~~~~~~~

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:ref:`single-csv-ballot-measure-contest` that would appear on the ballot.
BallotMeasureSelection extends :ref:`single-csv-ballot-selection-base`.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| selection    | ``xs:string`` | **Required** | Single       | Selection text for a                     |                                          |
|              |               |              |              | :ref:`single-csv-ballot-measure-contest` |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,sequence_order,selection
    bms001,1,Proposition A
    bms002,2,Proposition B


.. _single-csv-ballot-selection-base:

ballot_selection_base
^^^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-csv-ballot-measure-selection`,
:ref:`single-csv-candidate-selection`, and :ref:`single-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    |                                          |
|                |                |              |              | listed on the ballot or in results. This |                                          |
|                |                |              |              | is the default ordering, and can be      |                                          |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`single-csv-ordered-contest`.    |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-ballot-selection-base:

ballot_selection_base
~~~~~~~~~~~~~~~~~~~~~

A base model for all ballot selection types:
:ref:`single-csv-ballot-measure-selection`,
:ref:`single-csv-candidate-selection`, and :ref:`single-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    |                                          |
|                |                |              |              | listed on the ballot or in results. This |                                          |
|                |                |              |              | is the default ordering, and can be      |                                          |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`single-csv-ordered-contest`.    |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-ballot-style:

ballot_style
~~~~~~~~~~~~

A container for the contests/measures on the ballot.

+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===============+==============+==============+==========================================+==========================================+
| image_uri            | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that returns an image of |                                          |
|                      |               |              |              | the sample ballot.                       |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ordered_contests_ids | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    |                                          |
|                      |               |              |              | :ref:`single-csv-ordered-contest`        |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_ids            | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    |                                          |
|                      |               |              |              | :ref:`single-csv-party`s.                |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,image_uri,ordered_contest_ids,party_ids
    bs00010,http://i.giphy.com/26BoCh3PgT8ai45ji.gif,oc2025,par02
    bs00011,http://i.giphy.com/3oEjHYDWEICgEpAOjK.gif,oc3000 oc2025,par01


.. _single-csv-candidate:

candidate
~~~~~~~~~

The Candidate object represents a candidate in a contest. If a candidate is
running in multiple contests, each contest **must** have its own Candidate
object. Candidate objects may **not** be reused between Contests.

+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+==================================================+==============+==============+==========================================+==========================================+
| ballot_name          | ``xs:string``                                    | **Required** | Single       | The candidate's name as it will be       |                                          |
|                      |                                                  |              |              | displayed on the official ballot (e.g.   |                                          |
|                      |                                                  |              |              | "Ken T. Cuccinelli II").                 |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`single-csv-external-identifiers`           | Optional     | Single       | Another identifier for a candidate that  |                                          |
|                      |                                                  |              |              | links to another source of information   |                                          |
|                      |                                                  |              |              | (e.g. a campaign committee ID that links |                                          |
|                      |                                                  |              |              | to a campaign finance system).           |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_date            | ``xs:date``                                      | Optional     | Single       | Date when the candidate filed for the    |                                          |
|                      |                                                  |              |              | contest.                                 |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_incumbent         | ``xs:boolean``                                   | Optional     | Single       | Indicates whether the candidate is the   |                                          |
|                      |                                                  |              |              | incumbent for the office associated with |                                          |
|                      |                                                  |              |              | the contest.                             |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_top_ticket        | ``xs:boolean``                                   | Optional     | Single       | Indicates whether the candidate is the   |                                          |
|                      |                                                  |              |              | top of a ticket that includes multiple   |                                          |
|                      |                                                  |              |              | candidates.                              |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id             | ``xs:IDREF``                                     | Optional     | Single       | Reference to a :ref:`single-csv-party`   |                                          |
|                      |                                                  |              |              | element with additional information      |                                          |
|                      |                                                  |              |              | about the candidate's affiliated party.  |                                          |
|                      |                                                  |              |              | This is the party affiliation that is    |                                          |
|                      |                                                  |              |              | intended to be presented as part of      |                                          |
|                      |                                                  |              |              | ballot information.                      |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| person_id            | ``xs:IDREF``                                     | Optional     | Single       | Reference to a :ref:`single-csv-person`  |                                          |
|                      |                                                  |              |              | element with additional information      |                                          |
|                      |                                                  |              |              | about the candidate.                     |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| post_election_status | :ref:`single-csv-candidate-post-election-status` | Optional     | Single       | Final status of the candidate (e.g.      |                                          |
|                      |                                                  |              |              | winner, withdrawn, etc...).              |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pre_election_status  | :ref:`single-csv-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate     |                                          |
|                      |                                                  |              |              | (e.g. filed, qualified, etc...).         |                                          |
+----------------------+--------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_name,external_identifier_type,external_identifier_othertype,external_identifier_value,file_date,is_incumbent,is_top_ticket,party_id,person_id,post_election_status,pre_election_status
    can001,Jude Fawley,,,,2016-12-01,true,false,par01,per50001,,filed
    can002,Arabella Donn,,,,2016-12-01,false,false,par02,per50002,,qualified
    can003,John Coltrane,,,,2016-09-23,false,false,par02,per50003,,qualified
    can004,Miles Davis,,,,2016-05-26,false,false,par01,per50004,,qualified


.. _single-csv-candidate-contest:

candidate_contest
~~~~~~~~~~~~~~~~~

CandidateContest extends :ref:`single-csv-contest-base` and represents a contest among
candidates.

+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+================+==============+==============+==========================================+==========================================+
| number_elected    | ``xs:integer`` | Optional     | Single       | Number of candidates that are elected in |                                          |
|                   |                |              |              | the contest (i.e. "N" of N-of-M).        |                                          |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_ids        | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                   |                |              |              | :ref:`single-csv-office` elements, if    |                                          |
|                   |                |              |              | available, which give additional         |                                          |
|                   |                |              |              | information about the offices. **Note:** |                                          |
|                   |                |              |              | the order of the office IDs **must** be  |                                          |
|                   |                |              |              | in the same order as the candidates      |                                          |
|                   |                |              |              | listed in `BallotSelectionIds`. E.g., if |                                          |
|                   |                |              |              | the various `BallotSelectionIds`         |                                          |
|                   |                |              |              | reference                                |                                          |
|                   |                |              |              | :ref:`single-csv-candidate-selection`    |                                          |
|                   |                |              |              | elements which reference the candidate   |                                          |
|                   |                |              |              | for President first and Vice-President   |                                          |
|                   |                |              |              | second, the `OfficeIds` should reference |                                          |
|                   |                |              |              | the office of President first and the    |                                          |
|                   |                |              |              | office of Vice-President second.         |                                          |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| primary_party_ids | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-csv-party`       |                                          |
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


.. _single-csv-contest-base:

contest_base
^^^^^^^^^^^^

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`,
:ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`,
and :ref:`single-csv-retention-contest` (NB: the latter because it extends
:ref:`single-csv-ballot-measure-contest`).

+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                    | Optional     | Single       | An abbreviation for the contest.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                    | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                          |                                  |              |              | which could be of any selection type     |                                          |
|                          |                                  |              |              | that extends                             |                                          |
|                          |                                  |              |              | :ref:`single-csv-ballot-selection-base`. |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                    | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                    | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                     | **Required** | Single       | References an                            |                                          |
|                          |                                  |              |              | :ref:`single-csv-electoral-district`     |                                          |
|                          |                                  |              |              | element that represents the geographical |                                          |
|                          |                                  |              |              | scope of the contest.                    |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                    | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                          |                                  |              |              | electorate for this contest past the     |                                          |
|                          |                                  |              |              | usual, "all registered voters"           |                                          |
|                          |                                  |              |              | electorate. This subtag will most often  |                                          |
|                          |                                  |              |              | be used for primaries and local          |                                          |
|                          |                                  |              |              | elections. In primaries, voters may have |                                          |
|                          |                                  |              |              | to be registered as a specific party to  |                                          |
|                          |                                  |              |              | vote, or there may be special rules for  |                                          |
|                          |                                  |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                  |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                    | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                          |                                  |              |              | links to another source of information.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                   | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                          |                                  |              |              | contest are rotated.                     |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                    | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                          |                                  |              |              | it appears on the ballot (NB:            |                                          |
|                          |                                  |              |              | BallotTitle should be used for this      |                                          |
|                          |                                  |              |              | purpose).                                |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                   | Optional     | Single       | Order in which the contests are listed   |                                          |
|                          |                                  |              |              | on the ballot. This is the default       |                                          |
|                          |                                  |              |              | ordering, and can be overrides by data   |                                          |
|                          |                                  |              |              | in a :ref:`single-csv-ballot-style`      |                                          |
|                          |                                  |              |              | element.                                 |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       |                                          |
|                          |                                  |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``         | Optional     | Single       | If "other" is selected as the            |                                          |
|                          |                                  |              |              | **VoteVariation**, the name of the       |                                          |
|                          |                                  |              |              | variation can be specified here.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-candidate-selection:

candidate_selection
~~~~~~~~~~~~~~~~~~~

CandidateSelection extends :ref:`single-csv-ballot-selection-base` and represents a
ballot selection for a candidate contest.

+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+================+==============+==============+==========================================+==========================================+
| candidate_ids         | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                       |                |              |              | :ref:`single-csv-candidate` elements.    |                                          |
|                       |                |              |              | The number of candidates that can be     |                                          |
|                       |                |              |              | references is unbounded in cases where   |                                          |
|                       |                |              |              | the ballot selection is for a ticket     |                                          |
|                       |                |              |              | (e.g. "President/Vice President",        |                                          |
|                       |                |              |              | "Governor/Lt Governor").                 |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| endorsement_party_ids | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                       |                |              |              | :ref:`single-csv-party` elements, which  |                                          |
|                       |                |              |              | signifies one or more endorsing parties  |                                          |
|                       |                |              |              | for the candidate(s).                    |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in           | ``xs:boolean`` | Optional     | Single       | Signifies if the particular ballot       |                                          |
|                       |                |              |              | selection allows for write-in            |                                          |
|                       |                |              |              | candidates. If true, one or more         |                                          |
|                       |                |              |              | write-in candidates are allowed for this |                                          |
|                       |                |              |              | contest.                                 |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,sequence_order,candidate_ids,endorsement_party_ids,is_write_in
    cs001,3,can004,par01,false
    cs002,2,can001 can002,par03 par02,false
    cs003,1,can003,par02 par03,true


.. _single-csv-ballot-selection-base:

ballot_selection_base
^^^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-csv-ballot-measure-selection`,
:ref:`single-csv-candidate-selection`, and :ref:`single-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    |                                          |
|                |                |              |              | listed on the ballot or in results. This |                                          |
|                |                |              |              | is the default ordering, and can be      |                                          |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`single-csv-ordered-contest`.    |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-checksum:

checksum
~~~~~~~~

The ``Checksum`` object contains information about a cryptographic checksum, including
the raw checksum value and the cryptographic hash algorithm used to compute it.

+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+======================================+==============+==============+==========================================+==========================================+
| algorithm    | :ref:`single-csv-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to |                                          |
|              |                                      |              |              | compute the checksum value.              |                                          |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``                        | **Required** | Single       | The raw cryptographic checksum value     |                                          |
|              |                                      |              |              | encoded as a non-delimited, lowercase    |                                          |
|              |                                      |              |              | hexadecimal string.                      |                                          |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,algorithm,value
    ch1,sha-256,65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e


.. _single-csv-contact-information:

contact_information
~~~~~~~~~~~~~~~~~~~

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`single-csv-election-administration`, :ref:`single-csv-office`,
:ref:`single-csv-person`, :ref:`single-csv-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===========================+==============+==============+==========================================+==========================================+
| address_line  | ``xs:string``             | Optional     | Repeats      | The "location" portion of a mailing      |                                          |
|               |                           |              |              | address. :ref:`See usage note.           |                                          |
|               |                           |              |              | <single-csv-name-address-line-usage>`    |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions    | ``xs:string``             | Optional     | Single       | Specifies further instructions for       |                                          |
|               |                           |              |              | locating this entity.                    |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| email         | ``xs:string``             | Optional     | Repeats      | An email address for the contact.        |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| fax           | ``xs:string``             | Optional     | Repeats      | A fax line for the contact.              |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours         | ``xs:string``             | Optional     | Single       | Contains the hours (in local time) that  |                                          |
|               |                           |              |              | the location is open *(NB: this element  |                                          |
|               |                           |              |              | is deprecated in favor of the more       |                                          |
|               |                           |              |              | structured :ref:`single-csv-hours-open`  |                                          |
|               |                           |              |              | element. It is strongly encouraged that  |                                          |
|               |                           |              |              | data providers move toward contributing  |                                          |
|               |                           |              |              | hours in this format)*.                  |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id | ``xs:IDREF``              | Optional     | Single       | References an                            |                                          |
|               |                           |              |              | :ref:`single-csv-hours-open` element,    |                                          |
|               |                           |              |              | which lists the hours of operation for a |                                          |
|               |                           |              |              | location.                                |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| lat_long      | :ref:`single-csv-lat-lng` | Optional     | Single       | Specifies the latitude and longitude of  |                                          |
|               |                           |              |              | this entity.                             |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name          | ``xs:string``             | Optional     | Single       | The name of the location or contact.     |                                          |
|               |                           |              |              | :ref:`See usage note.                    |                                          |
|               |                           |              |              | <single-csv-name-address-line-usage>`    |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| phone         | ``xs:string``             | Optional     | Repeats      | A phone number for the contact.          |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| uri           | ``xs:anyURI``             | Optional     | Repeats      | An informational URI for the contact or  |                                          |
|               |                           |              |              | location.                                |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| parent_id     | ``xs:IDREF``              | Optional     | Repeats      | A reference to a record in source,       |                                          |
|               |                           |              |              | department, voter_service, candidate,    |                                          |
|               |                           |              |              | person, or office.                       |                                          |
+---------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,address_line_1,address_line_2,address_line_3,directions,email,fax,hours,hours_open_id,latitude,longitude,latlng_source,name,phone,uri,parent_id
    ci0827,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,off001
    ci0828,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,vs01


.. _single-csv-contest-base:

contest_base
~~~~~~~~~~~~

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`,
:ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`,
and :ref:`single-csv-retention-contest` (NB: the latter because it extends
:ref:`single-csv-ballot-measure-contest`).

+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                    | Optional     | Single       | An abbreviation for the contest.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                    | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                          |                                  |              |              | which could be of any selection type     |                                          |
|                          |                                  |              |              | that extends                             |                                          |
|                          |                                  |              |              | :ref:`single-csv-ballot-selection-base`. |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                    | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                    | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                     | **Required** | Single       | References an                            |                                          |
|                          |                                  |              |              | :ref:`single-csv-electoral-district`     |                                          |
|                          |                                  |              |              | element that represents the geographical |                                          |
|                          |                                  |              |              | scope of the contest.                    |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                    | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                          |                                  |              |              | electorate for this contest past the     |                                          |
|                          |                                  |              |              | usual, "all registered voters"           |                                          |
|                          |                                  |              |              | electorate. This subtag will most often  |                                          |
|                          |                                  |              |              | be used for primaries and local          |                                          |
|                          |                                  |              |              | elections. In primaries, voters may have |                                          |
|                          |                                  |              |              | to be registered as a specific party to  |                                          |
|                          |                                  |              |              | vote, or there may be special rules for  |                                          |
|                          |                                  |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                  |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                    | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                          |                                  |              |              | links to another source of information.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                   | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                          |                                  |              |              | contest are rotated.                     |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                    | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                          |                                  |              |              | it appears on the ballot (NB:            |                                          |
|                          |                                  |              |              | BallotTitle should be used for this      |                                          |
|                          |                                  |              |              | purpose).                                |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                   | Optional     | Single       | Order in which the contests are listed   |                                          |
|                          |                                  |              |              | on the ballot. This is the default       |                                          |
|                          |                                  |              |              | ordering, and can be overrides by data   |                                          |
|                          |                                  |              |              | in a :ref:`single-csv-ballot-style`      |                                          |
|                          |                                  |              |              | element.                                 |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       |                                          |
|                          |                                  |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``         | Optional     | Single       | If "other" is selected as the            |                                          |
|                          |                                  |              |              | **VoteVariation**, the name of the       |                                          |
|                          |                                  |              |              | variation can be specified here.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-department:

department
~~~~~~~~~~

+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=======================================+==============+==============+==========================================+==========================================+
| election_official_person_id | ``xs:IDREF``                          | Optional     | Single       | The individual to contact at the         |                                          |
|                             |                                       |              |              | election administration office. The      |                                          |
|                             |                                       |              |              | specified person should be the           |                                          |
|                             |                                       |              |              | :ref:`election official                  |                                          |
|                             |                                       |              |              | <single-csv-person>`.                    |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| voter_service               | :ref:`single-csv-voter-service`       | Optional     | Repeats      | The types of services and appropriate    |                                          |
|                             |                                       |              |              | contact individual available to voters.  |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_administration_id  | ``xs:IDREF``                          | Optional     | Single       | The election administration that the     |                                          |
|                             |                                       |              |              | department is a part of.                 |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_official_person_id,election_administration_id
    dep01,per50002,ea123
    dep02,per50002,ea345
    dep03,per50002,ea625
    dep04,per50002,ea625


.. _single-csv-election:

election
~~~~~~~~

The Election object represents an Election Day, which usually consists of many individual contests
and/or referenda. A feed must contain **exactly one** Election object. All relationships in the
feed (e.g., street segment to precinct to polling location) are assumed to relate only to
the Election specified by this object. It is permissible, and recommended, to combine unrelated
contests (e.g., a special election and a general election) that occur on the same day into one feed
with one Election object.

+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============================+================+==============+==============+==========================================+==========================================+
| date                          | ``xs:date``    | **Required** | Single       | Specifies when the election is being     |                                          |
|                               |                |              |              | held. The `Date` is considered to be in  |                                          |
|                               |                |              |              | the timezone local to the state holding  |                                          |
|                               |                |              |              | the election.                            |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_type                 | ``xs:string``  | Optional     | Single       | Specifies the highest controlling        |                                          |
|                               |                |              |              | authority for election (e.g., federal,   |                                          |
|                               |                |              |              | state, county, city, town, etc.)         |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state_id                      | ``xs:IDREF``   | **Required** | Single       | Specifies a link to the `State` element  |                                          |
|                               |                |              |              | where the election is being held.        |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_statewide                  | ``xs:boolean`` | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                               |                |              |              | statewide.                               | the implementation is required to        |
|                               |                |              |              |                                          | default to "yes".                        |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                          | ``xs:string``  | Optional     | Single       | The name for the election (**NB:** while |                                          |
|                               |                |              |              | optional, this element is highly         |                                          |
|                               |                |              |              | recommended).                            |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_info             | ``xs:string``  | Optional     | Single       | Specifies information about registration |                                          |
|                               |                |              |              | for this election either as text or a    |                                          |
|                               |                |              |              | URI.                                     |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_ballot_info          | ``xs:string``  | Optional     | Single       | Specifies information about requesting   |                                          |
|                               |                |              |              | absentee ballots either as text or a URI |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| results_uri                   | ``xs:anyURI``  | Optional     | Single       | Contains a URI where results for the     |                                          |
|                               |                |              |              | election may be found                    |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_hours                 | ``xs:string``  | Optional     | Single       | Contains the hours (in local time) that  |                                          |
|                               |                |              |              | Election Day polling locations are open. |                                          |
|                               |                |              |              | If polling hours differ in specific      |                                          |
|                               |                |              |              | polling locations, alternative hours may |                                          |
|                               |                |              |              | be specified in the                      |                                          |
|                               |                |              |              | :ref:`single-csv-polling-location`       |                                          |
|                               |                |              |              | object *(NB: this element is deprecated  |                                          |
|                               |                |              |              | in favor of the more structured          |                                          |
|                               |                |              |              | :ref:`single-csv-hours-open` element. It |                                          |
|                               |                |              |              | is strongly encouraged that data         |                                          |
|                               |                |              |              | providers move toward contributing hours |                                          |
|                               |                |              |              | in this format)*.                        |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_ids                | ``xs:IDREF``   | Optional     | Single       | References the                           |                                          |
|                               |                |              |              | :ref:`single-csv-hours-open` element,    |                                          |
|                               |                |              |              | which lists the hours of operation for   |                                          |
|                               |                |              |              | polling locations.                       |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_election_day_registration | ``xs:boolean`` | Optional     | Single       | Specifies if a voter can register on the |                                          |
|                               |                |              |              | same day of the election (i.e., the last |                                          |
|                               |                |              |              | day of the election). Valid items are    |                                          |
|                               |                |              |              | "yes" and "no".                          |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_deadline         | ``xs:date``    | Optional     | Single       | Specifies the last day to register for   |                                          |
|                               |                |              |              | the election with the possible exception |                                          |
|                               |                |              |              | of Election Day registration.            |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_request_deadline     | ``xs:date``    | Optional     | Single       | Specifies the last day to request an     |                                          |
|                               |                |              |              | absentee ballot.                         |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date,name,election_type,state_id,is_statewide,registration_info,absentee_ballot_info,results_uri,polling_hours,has_election_day_registration,registration_deadline,absentee_request_deadline,hours_open_id
    e001,10-08-2016,Best Hot Dog,State,st51,true,www.registrationinfo.com,You can vote absentee,http://hotdogcontest.gov/results,Noon to 3p.m.,true,10/08/2016,,ho002


.. _single-csv-election-administration:

election_administration
~~~~~~~~~~~~~~~~~~~~~~~

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Tag                             | Data Type                         | Required?    | Repeats?     | Description                                                 | Error Handling                           |
+=================================+===================================+==============+==============+=============================================================+==========================================+
| absentee_uri                    | ``xs:anyURI``                     | Optional     | Single       | Specifies the web address for information on absentee       |                                          |
|                                 |                                   |              |              | voting.                                                     |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| am_i_registered_uri             | ``xs:anyURI``                     | Optional     | Single       | Specifies the web address for information on whether an     |                                          |
|                                 |                                   |              |              | individual is registered.                                   |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ballot_tracking_uri             | ``xs:anyURI``                     | Optional     | Single       | Specifies the web address for tracking information for a    |                                          |
|                                 |                                   |              |              | ballot cast by mail                                         |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ballot_tracking_provisional_uri | ``xs:anyURI``                     | Optional     | Single       | Specifies the web address for tracking information for a    |                                          |
|                                 |                                   |              |              | provisional ballot. To support EAC guidelines for           |                                          |
|                                 |                                   |              |              | "Processing Provisional Ballots"                            |                                          |
|                                 |                                   |              |              | (https://www.eac.gov/research-and-data/provisional-voting/) |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| election_notice                 | :ref:`single-csv-election-notice` | Optional     | Single       | A place for election administrators to post last minute and |                                          |
|                                 |                                   |              |              | emergency notifications pertaining to the election.         |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| elections_uri                   | ``xs:anyURI``                     | Optional     | Single       | Specifies web address the administration's website.         |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| registration_uri                | ``xs:anyURI``                     | Optional     | Single       | Specifies web address for information on registering to     |                                          |
|                                 |                                   |              |              | vote.                                                       |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| rules_uri                       | ``xs:anyURI``                     | Optional     | Single       | Specifies a URI for the election rules and laws (if any)    |                                          |
|                                 |                                   |              |              | for the jurisdiction of the administration.                 |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| what_is_on_my_ballot_uri        | ``xs:anyURI``                     | Optional     | Single       | Specifies web address for information on what is on an      |                                          |
|                                 |                                   |              |              | individual's ballot.                                        |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| where_do_i_vote_uri             | ``xs:anyURI``                     | Optional     | Single       | The Specifies web address for information on where an       |                                          |
|                                 |                                   |              |              | individual votes based on their address.                    |                                          |
+---------------------------------+-----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,absentee_uri,am_i_registered_uri,ballot_tracking_uri,ballot_tracking_provisional_uri,election_notice_text,election_notice_uri,elections_uri,registration_uri,rules_uri,what_is_on_my_ballot_uri,where_do_i_vote_uri
    ea123,https://example.com/absentee,https://example.com/am-i-registered,https://www.vote.virginia.gov/,https://www.vote.virginia.gov/,This is an emergency notification for this election.,https://www.yadayada.gov,https://example.com/elections,https://example.com/registration,https://example.com/rules,https://example.com/what-is-on-my-ballot,https://example.com/where-do-i-vote
    ea345,https://example.com/absentee2,https://example.com/am-i-registered2,https://example.com/elections2,https://example.com/registration2,,,https://example.com/rules2,https://example.com/what-is-on-my-ballot2,https://example.com/where-do-i-vote2
    ea625,https://example.com/absentee3,https://example.com/am-i-registered3,https://example.com/elections3,https://example.com/registration3,This is an emergency notification for this election.,,https://example.com/rules3,https://example.com/what-is-on-my-ballot3,https://example.com/where-do-i-vote3


.. _single-csv-election-notice:

election_notice
~~~~~~~~~~~~~~~

+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===============+==============+==============+==========================================+==========================================+
| election_notice_text | ``xs:string`` | **Required** | Single       | The last minute or emergency             |                                          |
|                      |               |              |              | notification text should be placed here. |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_notice_uri  | ``xs:string`` | Optional     | Single       | Optional URL for additional information  |                                          |
|                      |               |              |              | related to the last minute or emergency  |                                          |
|                      |               |              |              | notification.                            |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-electoral-district:

electoral_district
~~~~~~~~~~~~~~~~~~

The ``ElectoralDistrict`` object represents the geographic area in which contests are held. Examples
of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District",
or "Union School District". The geographic area that comprises a ``ElectoralDistrict`` is defined by
which precincts link to the ``ElectoralDistrict``.

+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+========================================+==============+==============+==========================================+==========================================+
| external_identifiers | :ref:`single-csv-external-identifiers` | Optional     | Single       | Other identifiers that link to external  |                                          |
|                      |                                        |              |              | datasets (e.g. `OCD-IDs`_)               |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                 | ``xs:string``                          | **Required** | Single       | Specifies the electoral area's name.     |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number               | ``xs:integer``                         | Optional     | Single       | Specifies the district number of the     |                                          |
|                      |                                        |              |              | district (e.g. 34, in the case of the    |                                          |
|                      |                                        |              |              | 34th State Senate District). If a number |                                          |
|                      |                                        |              |              | is not applicable, instead of leaving    |                                          |
|                      |                                        |              |              | the field blank, leave this field out of |                                          |
|                      |                                        |              |              | the object; empty strings are not valid  |                                          |
|                      |                                        |              |              | for xs:integer fields.                   |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                 | :ref:`single-csv-district-type`        | **Required** | Single       | Specifies the type of electoral area.    |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type           | ``xs:string``                          | Optional     | Single       | Allows for cataloging a new              |                                          |
|                      |                                        |              |              | :ref:`single-csv-district-type` option   |                                          |
|                      |                                        |              |              | when ``Type`` is specified as "other".   |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,external_identifier_type,external_identifier_othertype,external_identifier_value,name,number,type,other_type
    ed001,ocd-id,,ocd-division/country:us/state:ny/borough:brooklyn,Brooklyn,1,borough,
    ed002,other,community-board,4,CB 4,2,other,community-board


.. _single-csv-external-file:

external_file
~~~~~~~~~~~~~

The ``ExternalFile`` object holds a reference to a file external to the feed itself. 
External files are packaged along with the VIP feed into a single, archived file. 

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| file_uri     | ``xs:anyURI`` | **Required** | Single       | The URI of the external file.            |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| checksum_id  | ``xs:IDREF``  | **Required** | Single       | The cryptographic checksum of the        |                                          |
|              |               |              |              | referenced external file.                |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,file_uri,checksum_id
    ef1,precinct_shapes.zip,ch1


.. _single-csv-external-geospatial-feature:

external_geospatial_feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+======================================+==============+==============+==========================================+==========================================+
| external_file_id   | ``xs:IDREF``                         | **Required** | Single       | Links to the                             |                                          |
|                    |                                      |              |              | :ref:`single-csv-external-file`          |                                          |
|                    |                                      |              |              | containing the geospatial shape(s) that  |                                          |
|                    |                                      |              |              | define the feature's boundary.           |                                          |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_format        | :ref:`single-csv-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       |                                          |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feature_identifier | :ref:`single-csv-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    |                                          |
|                    |                                      |              |              | shape(s) to use from the geospatial      |                                          |
|                    |                                      |              |              | file. These refer to identifiers within  |                                          |
|                    |                                      |              |              | the referenced external file. This is a  |                                          |
|                    |                                      |              |              | repeated field in the XML specification, |                                          |
|                    |                                      |              |              | but a scalar field in the CSV            |                                          |
|                    |                                      |              |              | specification. If more than one          |                                          |
|                    |                                      |              |              | identifier is required with the CSV      |                                          |
|                    |                                      |              |              | specifiation, multiple values can be     |                                          |
|                    |                                      |              |              | provided by delimited by space.          |                                          |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,external_file_id,file_format,shape_identifiers
    egf1,ef1,shp,0 7 9


.. _single-csv-external-identifier:

external_identifier
~~~~~~~~~~~~~~~~~~~

+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================+==============+==============+==========================================+==========================================+
| type         | ``identifier_type`` | **Required** | Single       | Specifies the type of identifier. Must   |                                          |
|              |                     |              |              | be one of the valid types as defined by  |                                          |
|              |                     |              |              | :ref:`single-csv-identifier-type`.       |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``       | Optional     | Single       | Allows for cataloging an                 |                                          |
|              |                     |              |              | ``ExternalIdentifier`` type that falls   |                                          |
|              |                     |              |              | outside the options listed in            |                                          |
|              |                     |              |              | :ref:`single-csv-identifier-type`.       |                                          |
|              |                     |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                     |              |              | using this field.                        |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``       | **Required** | Single       | Specifies the identifier.                |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-external-identifiers:

external_identifiers
~~~~~~~~~~~~~~~~~~~~

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`single-csv-candidate`

* Any element that extends :ref:`single-csv-contest-base`

* :ref:`single-csv-electoral-district`

* :ref:`single-csv-locality`

* :ref:`single-csv-office`

* :ref:`single-csv-party`

* :ref:`single-csv-precinct`

* :ref:`single-csv-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=======================================+==============+==============+==========================================+==========================================+
| external_identifier | :ref:`single-csv-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                     |                                       |              |              | identifier it is (see                    | must be present for                      |
|                     |                                       |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                     |                                       |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                     |                                       |              |              |                                          | present, the implementation is required  |
|                     |                                       |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                     |                                       |              |              |                                          | element.                                 |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-feature-identifier:

feature_identifier
~~~~~~~~~~~~~~~~~~

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| index        | ``xs:int``   | Optional     | Single       | The index value for the shapefile        |                                          |
|              |              |              |              | feature.                                 |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-html-color-string:

html_color_string
~~~~~~~~~~~~~~~~~

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``


.. _single-csv-lat-lng:

lat_long
~~~~~~~~

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| latitude      | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    |                                          |
|               |               |              |              | from location name to lat/lng. For       |                                          |
|               |               |              |              | example, this could be the name of a     |                                          |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-locality:

locality
~~~~~~~~

The Locality object represents the jurisdiction below the :ref:`single-csv-state` (e.g. county).

+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| Tag                        | Data Type                              | Required?    | Repeats?     | Description                               | Error Handling                           |
+============================+========================================+==============+==============+===========================================+==========================================+
| election_administration_id | ``xs:IDREF``                           | Optional     | Single       | Links to the locality's                   |                                          |
|                            |                                        |              |              | :ref:`single-csv-election-administration` |                                          |
|                            |                                        |              |              | object.                                   |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| external_identifiers       | :ref:`single-csv-external-identifiers` | Optional     | Single       | Another identifier for a locality that    |                                          |
|                            |                                        |              |              | links to another dataset (e.g. `OCD-ID`_) |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| is_mail_only               | ``xs:boolean``                         | Optional     | Single       | Determines if the locality runs mail-only | If the field is missing or invalid, the  |
|                            |                                        |              |              | elections. If this is true, then all      | implementation is required to assume     |
|                            |                                        |              |              | precincts a part of the locality will     | `IsMailOnly` is false.                   |
|                            |                                        |              |              | also run mail-only elections. Drop boxes  |                                          |
|                            |                                        |              |              | may be used in addition to this flag      |                                          |
|                            |                                        |              |              | using a :ref:`polling location            |                                          |
|                            |                                        |              |              | <single-csv-polling-location>` record     |                                          |
|                            |                                        |              |              | configured as a Drop Box.                 |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| name                       | ``xs:string``                          | **Required** | Single       | Specifies the name of a locality.         |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| polling_location_ids       | ``xs:IDREFS``                          | Optional     | Single       | Specifies a link to a set of the          |                                          |
|                            |                                        |              |              | locality's :ref:`polling locations        |                                          |
|                            |                                        |              |              | <single-csv-polling-location>`s. If early |                                          |
|                            |                                        |              |              | vote centers or ballot drop locations are |                                          |
|                            |                                        |              |              | locality-wide, they should be specified   |                                          |
|                            |                                        |              |              | here.                                     |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| state_id                   | ``xs:IDREF``                           | **Required** | Single       | References the locality's                 |                                          |
|                            |                                        |              |              | :ref:`single-csv-state`.                  |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| type                       | :ref:`single-csv-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.        |                                          |
|                            |                                        |              |              | county, town, et al.), which is one of    |                                          |
|                            |                                        |              |              | the various :ref:`DistrictType            |                                          |
|                            |                                        |              |              | enumerations <single-csv-district-type>`. |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+
| other_type                 | ``xs:string``                          | Optional     | Single       | Allows for defining a type of locality    |                                          |
|                            |                                        |              |              | that falls outside the options listed in  |                                          |
|                            |                                        |              |              | :ref:`DistrictType                        |                                          |
|                            |                                        |              |              | <single-csv-district-type>`.              |                                          |
+----------------------------+----------------------------------------+--------------+--------------+-------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_administration_id,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,name,polling_location_ids,state_id,type,other_type
    loc001,ea123,ocd-id,,ocd-division/country:us/state:co/county:denver,true,Locality #1,poll001 poll002,st51,city,
    loc002,ea345,,,,,Locality #2,,st51,other,unique type


.. _single-csv-office:

office
~~~~~~

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type              | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+========================+==============+==============+==========================================+==========================================+
| description              | ``xs:string``          | Optional     | Single       | A brief description of the office and    |                                          |
|                          |                        |              |              | its purpose.                             |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``           | **Required** | Single       | Links to the                             |                                          |
|                          |                        |              |              | :ref:`single-csv-electoral-district`     |                                          |
|                          |                        |              |              | element associated with the office.      |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:IDREF``           | Optional     | Single       | Other identifiers that link this office  |                                          |
|                          |                        |              |              | to other related datasets (e.g. campaign |                                          |
|                          |                        |              |              | finance systems, OCD IDs, et al.).       |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| filing_deadline          | ``xs:date``            | Optional     | Single       | Specifies the date and time when a       |                                          |
|                          |                        |              |              | candidate must have filed for the        |                                          |
|                          |                        |              |              | contest for the office.                  |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_partisan              | ``xs:boolean``         | Optional     | Single       | Indicates whether the office is          |                                          |
|                          |                        |              |              | partisan.                                |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``          | **Required** | Single       | The name of the office.                  |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_holder_person_ids | ``xs:IDREFS``          | Optional     | Single       | Links to the :ref:`single-csv-person`    |                                          |
|                          |                        |              |              | element(s) that hold additional          |                                          |
|                          |                        |              |              | information about the current office     |                                          |
|                          |                        |              |              | holder(s).                               |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term                     | :ref:`single-csv-term` | Optional     | Single       | Defines the term the office can be held. |                                          |
+--------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,electoral_district_id,external_identifier_type,external_identifier_othertype,external_identifier_value,filing_deadline,is_partisan,name,office_holder_person_ids,term_type,term_start_date,term_end_date
    off001,ed001,,,,,true,Deputy Chief of Staff,per50003,full-term,2002-01-21,
    off002,ed001,,,,,true,Deputy Deputy Chief of Staff,per50001,unexpired-term,2002-01-21,
    off003,ed001,,,,,false,General Secretary of Secretaries,per50004,full-term,2002-01-21,


.. _single-csv-ordered-contest:

ordered_contest
~~~~~~~~~~~~~~~

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:ref:`single-csv-ballot-style` to accurate depict exactly what will show up on a particular
ballot in the proper order.

+------------------------------+--------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
| Tag                          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                                   |
+==============================+==============+==============+==============+==========================================+==================================================+
| contest_id                   | ``xs:IDREF`` | **Required** | Single       | Links to elements that extend            |                                                  |
|                              |              |              |              | :ref:`single-csv-contest-base`.          |                                                  |
+------------------------------+--------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
| ordered_ballot_selection_ids | ``IDREFS``   | Optional     | Single       | Links to elements that extend            | If the field is invalid or not present, the      |
|                              |              |              |              | :ref:`single-csv-ballot-selection-base`. | implementation is required to ignore it. If an   |
|                              |              |              |              |                                          | ``OrderedBallotSelectionIds`` element is not     |
|                              |              |              |              |                                          | present, the presumed order of the selection     |
|                              |              |              |              |                                          | will be the order of                             |
|                              |              |              |              |                                          | :ref:`single-csv-ballot-selection-base`-extended |
|                              |              |              |              |                                          | elements referenced by the underlying            |
|                              |              |              |              |                                          | :ref:`single-csv-contest-base`-extended          |
|                              |              |              |              |                                          | elements.                                        |
+------------------------------+--------------+--------------+--------------+------------------------------------------+--------------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,contest_id,ordered_ballot_selection_ids
    oc2025,con001,bs001 bs002 bs003
    oc3000,con002,bs001


.. _single-csv-party:

party
~~~~~

This element describes a political party and the metadata associated with them. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated :ref:`single-csv-candidate-contest` can use the **PrimaryPartyIds** field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+========================================+==============+==============+==========================================+==========================================+
| abbreviation         | ``xs:string``                          | Optional     | Single       | An abbreviation for the party name.      |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| color                | :ref:`single-csv-html-color-string`    | Optional     | Single       | The preferred display color for the      |                                          |
|                      |                                        |              |              | party, for use in maps and other         |                                          |
|                      |                                        |              |              | displays.                                |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`single-csv-external-identifiers` | Optional     | Single       | Other identifiers that link this party   |                                          |
|                      |                                        |              |              | to other related data sets (e.g. a       |                                          |
|                      |                                        |              |              | campaign finance system, etc).           |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in          | ``xs:boolean``                         | Optional     | Single       | Signals if this political party is one   |                                          |
|                      |                                        |              |              | that is officially recognized by a       |                                          |
|                      |                                        |              |              | local, state, or federal organization,   |                                          |
|                      |                                        |              |              | or is a "write-in" in jurisdictions      |                                          |
|                      |                                        |              |              | which allow candidates to free-form      |                                          |
|                      |                                        |              |              | enter their political affiliation. If    |                                          |
|                      |                                        |              |              | this field is not present then it is     |                                          |
|                      |                                        |              |              | assumed to be false.                     |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| leader_person_ids    | ``xs:IDREFS``                          | Optional     | Single       | A reference of :ref:`single-csv-person`  |                                          |
|                      |                                        |              |              | elements which are leaders of the        |                                          |
|                      |                                        |              |              | `Party`.                                 |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| logo_uri             | ``xs:anyURI``                          | Optional     | Single       | Web address of a logo to use in          |                                          |
|                      |                                        |              |              | displays.                                |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                 | ``xs:string``                          | **Required** | Single       | The name of the party.                   |                                          |
+----------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,color,external_identifier_type,external_identifier_othertype,external_identifier_value,is_write_in,leader_person_ids,logo_uri,name
    par01,REP,ff0000,,,,true,,http://example.com/elephant.png,Republican
    par02,DEM,0000ff,,,,false,per01,http://example.com/donkey.png,Democrat
    par03,GRN,efefef,,,,,,http://example.com/tree.png,Green
    par04,WFP,ee99aa,,,,,,http://example.com/worker.png,Working Families Party


.. _single-csv-party-contest:

party_contest
~~~~~~~~~~~~~

An extension of :ref:`single-csv-contest-base` which describes a contest in
which the possible ballot selections are of type :ref:`single-csv-party-selection`. These could include contests in which straight-party
selections are allowed, or party-list contests (although these are more common
outside of the United States).

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,electoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation
    pcon001,PC1071,bs001 bs002,,Party Election,ed001,all registered voters,,,,false,Straight Party Vote,3,,


.. _single-csv-contest-base:

contest_base
^^^^^^^^^^^^

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`,
:ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`,
and :ref:`single-csv-retention-contest` (NB: the latter because it extends
:ref:`single-csv-ballot-measure-contest`).

+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                    | Optional     | Single       | An abbreviation for the contest.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                    | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                          |                                  |              |              | which could be of any selection type     |                                          |
|                          |                                  |              |              | that extends                             |                                          |
|                          |                                  |              |              | :ref:`single-csv-ballot-selection-base`. |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                    | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                    | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                          |                                  |              |              | the ballot.                              |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                     | **Required** | Single       | References an                            |                                          |
|                          |                                  |              |              | :ref:`single-csv-electoral-district`     |                                          |
|                          |                                  |              |              | element that represents the geographical |                                          |
|                          |                                  |              |              | scope of the contest.                    |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                    | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                          |                                  |              |              | electorate for this contest past the     |                                          |
|                          |                                  |              |              | usual, "all registered voters"           |                                          |
|                          |                                  |              |              | electorate. This subtag will most often  |                                          |
|                          |                                  |              |              | be used for primaries and local          |                                          |
|                          |                                  |              |              | elections. In primaries, voters may have |                                          |
|                          |                                  |              |              | to be registered as a specific party to  |                                          |
|                          |                                  |              |              | vote, or there may be special rules for  |                                          |
|                          |                                  |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                  |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                    | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                          |                                  |              |              | links to another source of information.  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                   | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                          |                                  |              |              | contest are rotated.                     |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                    | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                          |                                  |              |              | it appears on the ballot (NB:            |                                          |
|                          |                                  |              |              | BallotTitle should be used for this      |                                          |
|                          |                                  |              |              | purpose).                                |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                   | Optional     | Single       | Order in which the contests are listed   |                                          |
|                          |                                  |              |              | on the ballot. This is the default       |                                          |
|                          |                                  |              |              | ordering, and can be overrides by data   |                                          |
|                          |                                  |              |              | in a :ref:`single-csv-ballot-style`      |                                          |
|                          |                                  |              |              | element.                                 |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       |                                          |
|                          |                                  |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``         | Optional     | Single       | If "other" is selected as the            |                                          |
|                          |                                  |              |              | **VoteVariation**, the name of the       |                                          |
|                          |                                  |              |              | variation can be specified here.         |                                          |
+--------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-party-selection:

party_selection
~~~~~~~~~~~~~~~

This element extends :ref:`single-csv-ballot-selection-base` to
support contests in which the selections can be groups of one or more parties.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| party_ids    | ``xs:IDREFS`` | **Required** | Single       | One or more :ref:`single-csv-party` IDs  | If one or more parties referenced are    |
|              |               |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |               |              |              | selection.                               | implementation is required to ignore the |
|              |               |              |              |                                          | PartySelection containing it.            |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,sequence_order,party_ids
    ps001,1,par01 par04
    ps002,2,par02
    ps003,3,par03


.. _single-csv-ballot-selection-base:

ballot_selection_base
^^^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-csv-ballot-measure-selection`,
:ref:`single-csv-candidate-selection`, and :ref:`single-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    |                                          |
|                |                |              |              | listed on the ballot or in results. This |                                          |
|                |                |              |              | is the default ordering, and can be      |                                          |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`single-csv-ordered-contest`.    |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-person:

person
~~~~~~

``Person`` defines information about a person. The person may be a candidate, election administrator,
or elected official. These elements reference ``Person``:

* :ref:`single-csv-candidate`

* :ref:`single-csv-election-administration`

* :ref:`single-csv-office`

+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+========================================+==============+==============+==========================================+==========================================+
| date_of_birth          | ``xs:date``                            | Optional     | Single       | Represents the individual's date of      |                                          |
|                        |                                        |              |              | birth.                                   |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers   | :ref:`single-csv-external-identifiers` | Optional     | Single       | Identifiers for this person.             |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| first_name             | ``xs:string``                          | Optional     | Single       | Represents an individual's first name.   |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_name              | ``xs:string``                          | Optional     | Single       | Specifies a person's full name (**NB:**  |                                          |
|                        |                                        |              |              | this information is                      |                                          |
|                        |                                        |              |              | :ref:`single-csv-internationalized-text` |                                          |
|                        |                                        |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                        |              |              | in multiple languages).                  |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| gender                 | ``xs:string``                          | Optional     | Single       | Specifies a person's gender.             |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| last_name              | ``xs:string``                          | Optional     | Single       | Represents an individual's last name.    |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| middle_name            | ``xs:string``                          | Optional     | Repeats      | Represents any number of names between   |                                          |
|                        |                                        |              |              | an individual's first and last names     |                                          |
|                        |                                        |              |              | (e.g. John **Ronald Reuel** Tolkien).    |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| nickname               | ``xs:string``                          | Optional     | Single       | Represents an individual's nickname.     |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id               | ``xs:IDREF``                           | Optional     | Single       | Refers to the associated                 |                                          |
|                        |                                        |              |              | :ref:`single-csv-party`. This            |                                          |
|                        |                                        |              |              | information is intended to be used by    |                                          |
|                        |                                        |              |              | feed consumers to help them disambiguate |                                          |
|                        |                                        |              |              | the person's identity, but not to be     |                                          |
|                        |                                        |              |              | presented as part of any ballot          |                                          |
|                        |                                        |              |              | information. For that see                |                                          |
|                        |                                        |              |              | :ref:`single-csv-candidate` **PartyId**. |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| prefix                 | ``xs:string``                          | Optional     | Single       | Specifies a prefix associated with a     |                                          |
|                        |                                        |              |              | person (e.g. Dr.).                       |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| profession             | ``xs:string``                          | Optional     | Single       | Specifies a person's profession (**NB:** |                                          |
|                        |                                        |              |              | this information is                      |                                          |
|                        |                                        |              |              | :ref:`single-csv-internationalized-text` |                                          |
|                        |                                        |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                        |              |              | in multiple languages).                  |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| suffix                 | ``xs:string``                          | Optional     | Single       | Specifies a suffix associated with a     |                                          |
|                        |                                        |              |              | person (e.g. Jr.).                       |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| title                  | ``xs:string``                          | Optional     | Single       | A title associated with a person         |                                          |
|                        |                                        |              |              | (**NB:** this information is             |                                          |
|                        |                                        |              |              | :ref:`single-csv-internationalized-text` |                                          |
|                        |                                        |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                        |              |              | in multiple languages).                  |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date_of_birth,first_name,gender,last_name,middle_name,nickname,party_id,prefix,profession,suffix,title
    per50001,1961-08-04,Barack,male,Obama,Hussein,,par02,,President,II,Mr. President
    per50002,1985-11-21,Carly,female,Jepsen,Rae,,par01,,Recording Artist,,
    per50003,1926-09-23,John,male,Coltrane,William,Trane,par02,,Recording Artist,Saint,
    per50004,1926-05-26,Miles,male,Davis,Dewey,,par01,,Recording Artist,III,


.. _single-csv-polling-location:

polling_location
~~~~~~~~~~~~~~~~

The PollingLocation object represents a site where voters cast or drop off ballots.

+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                                   | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================================+===========================+==============+==============+==========================================+==========================================+
| address_line                          | ``xs:string``             | Optional     | Repeats      | Represents the various parts of an       | One of AddressStructured and AddressLine |
|                                       |                           |              |              | address to a polling location.           | should be present for a given Polling    |
|                                       |                           |              |              |                                          | Location. If none is present, the        |
|                                       |                           |              |              |                                          | implementation is required to ignore the |
|                                       |                           |              |              |                                          | ``PollingLocation`` element containing   |
|                                       |                           |              |              |                                          | it.                                      |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions                            | ``xs:string``             | Optional     | Single       | Specifies further instructions for       |                                          |
|                                       |                           |              |              | locating the polling location.           |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours                                 | ``xs:string``             | Optional     | Single       | Contains the hours (in local time) that  |                                          |
|                                       |                           |              |              | the polling location is open (**NB:**    |                                          |
|                                       |                           |              |              | this element is deprecated in favor of   |                                          |
|                                       |                           |              |              | the more structured                      |                                          |
|                                       |                           |              |              | :ref:`single-csv-hours-open` element. It |                                          |
|                                       |                           |              |              | is strongly encouraged that data         |                                          |
|                                       |                           |              |              | providers move toward contributing hours |                                          |
|                                       |                           |              |              | in this format).                         |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id                         | ``xs:IDREF``              | Optional     | Single       | Links to an :ref:`single-csv-hours-open` |                                          |
|                                       |                           |              |              | element, which is a schedule of dates    |                                          |
|                                       |                           |              |              | and hours during which the polling       |                                          |
|                                       |                           |              |              | location is available.                   |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_drop_box                           | ``xs:boolean``            | Optional     | Single       | Indicates if this polling location is a  |                                          |
|                                       |                           |              |              | drop box.                                |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_early_voting                       | ``xs:boolean``            | Optional     | Single       | Indicates if this polling location is an |                                          |
|                                       |                           |              |              | early vote site.                         |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                                  | ``xs:string``             | Optional     | Single       | Name of the polling location.            |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| photo_uri                             | ``xs:string``             | Optional     | Single       | Contains a link to an image of the       |                                          |
|                                       |                           |              |              | polling location.                        |                                          |
+---------------------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,name,address_line,structured_line_1,structured_city,structured_state,structured_zip,directions,hours,photo_uri,hours_open_id,is_drop_box,is_early_voting,latitude,longitude,latlng_source
    poll001,ALBERMARLE HIGH SCHOOL,,2775 Hydraulic Rd,Charlottesville,VA,22901,Use back door,7am-8pm,www.picture.com,ho001,false,true,38.0754627,78.5014875,Google Maps
    poll002,Public Library,Main St Denver CO,,,,,,next to the checkout counter,7am-8pm,www.picture.com,,false,true,38.0754627,78.5014875,Google Maps


.. _single-csv-lat-lng:

lat_long
^^^^^^^^

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| latitude      | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    |                                          |
|               |               |              |              | from location name to lat/lng. For       |                                          |
|               |               |              |              | example, this could be the name of a     |                                          |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-simple-address-type:

simple_address_type
^^^^^^^^^^^^^^^^^^^

A ``SimpleAddressType`` represents a structured address.

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| structured_line_1 | ``xs:string`` | **Required** | Single       | The address line for a structured        |                                          |
|                   |               |              |              | address. Should include the street       |                                          |
|                   |               |              |              | number, street name, and any prefix and  |                                          |
|                   |               |              |              | suffix.                                  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_2 | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_3 | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_city   | ``xs:string`` | **Required** | Single       | The City value of a structured address.  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_state  | ``xs:string`` | **Required** | Single       | The State value of a structured address. |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_zip    | ``xs:string`` | Optional     | Single       | The ZIP code of a structured address.    |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-precinct:

precinct
~~~~~~~~

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:ref:`Source.VipId <single-csv-source>`, :ref:`Locality.Name <single-csv-locality>`, :ref:`Precinct.Ward <single-csv-precinct>`,
:ref:`Precinct.Name <single-csv-precinct>`, and :ref:`Precinct.Number <single-csv-precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

Voters can be assigned to a precinct in two ways. A voter location modeled by :doc:`StreetSegment <street_segment>`
is assigned to a precinct by :doc:`StreetSegment.PrecinctId <street_segment>`.
Alternatively, a precinct's spatial boundary can be modeled with :doc:`Precinct.SpatialBoundary  <precinct>`.
Any registered voter address contained within the spatial boundary of the precinct
is assigned to that precinct.

+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+========================================+==============+==============+==========================================+==========================================+
| ballot_style_id        | ``xs:IDREF``                           | Optional     | Single       | Links to the                             |                                          |
|                        |                                        |              |              | :ref:`single-csv-ballot-style`, which a  |                                          |
|                        |                                        |              |              | person who lives in this precinct will   |                                          |
|                        |                                        |              |              | vote.                                    |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_ids | ``xs:IDREFS``                          | Optional     | Single       | Links to the                             |                                          |
|                        |                                        |              |              | :ref:`single-csv-electoral-district`s    |                                          |
|                        |                                        |              |              | (e.g., congressional district, state     |                                          |
|                        |                                        |              |              | house district, school board district)   |                                          |
|                        |                                        |              |              | to which the entire precinct/precinct    |                                          |
|                        |                                        |              |              | split belongs. **Highly Recommended** if |                                          |
|                        |                                        |              |              | candidate information is to be provided. |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers   | :ref:`single-csv-external-identifiers` | Optional     | Single       | Other identifier for the precinct that   |                                          |
|                        |                                        |              |              | relates to another dataset (e.g.         |                                          |
|                        |                                        |              |              | `OCD-ID`_).                              |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only           | ``xs:boolean``                         | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                        |                                        |              |              | mail-only elections.                     | implementation is required to assume     |
|                        |                                        |              |              |                                          | `IsMailOnly` is false.                   |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| locality_id            | ``xs:IDREF``                           | **Required** | Single       | Links to the :ref:`single-csv-locality`  |                                          |
|                        |                                        |              |              | that comprises the precinct.             |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                   | ``xs:string``                          | **Required** | Single       | Specifies the precinct's name (or number |                                          |
|                        |                                        |              |              | if no name exists).                      |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number                 | ``xs:string``                          | Optional     | Single       | Specifies the precinct's number (e.g.,   |                                          |
|                        |                                        |              |              | 32 or 32A -- alpha characters are        |                                          |
|                        |                                        |              |              | legal). Should be used if the `Name`     |                                          |
|                        |                                        |              |              | field is populated by a name and not a   |                                          |
|                        |                                        |              |              | number.                                  |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids   | ``xs:IDREFS``                          | Optional     | Single       | Specifies a link to the precinct's       |                                          |
|                        |                                        |              |              | :ref:`single-csv-polling-location`       |                                          |
|                        |                                        |              |              | object(s).                               |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_split_name    | ``xs:string``                          | Optional     | Single       | If this field is empty, then this        |                                          |
|                        |                                        |              |              | `Precinct` object represents a full      |                                          |
|                        |                                        |              |              | precinct. If this field is present, then |                                          |
|                        |                                        |              |              | this `Precinct` object represents one    |                                          |
|                        |                                        |              |              | portion of a split precinct. Each        |                                          |
|                        |                                        |              |              | `Precinct` object that represents one    |                                          |
|                        |                                        |              |              | portion of a split precinct **must**     |                                          |
|                        |                                        |              |              | have the same `Name` value, but          |                                          |
|                        |                                        |              |              | different `PrecinctSplitName` values.    |                                          |
|                        |                                        |              |              | See the `sample_feed.xml` file for       |                                          |
|                        |                                        |              |              | examples.                                |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| spatial_boundary_id    | ``xs:IDREF``                           | Optional     | Single       | Defines the spatial boundary of the      |                                          |
|                        |                                        |              |              | precinct. All voter addresses contained  |                                          |
|                        |                                        |              |              | within this boundary are assigned to the |                                          |
|                        |                                        |              |              | precinct. If a voter address also maps   |                                          |
|                        |                                        |              |              | to a :doc:`StreetSegment                 |                                          |
|                        |                                        |              |              | <street_segment>`, then the precinct     |                                          |
|                        |                                        |              |              | assignment from the StreetSegment will   |                                          |
|                        |                                        |              |              | be preferred over the assignment from    |                                          |
|                        |                                        |              |              | the spatial boundary.                    |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ward                   | ``xs:string``                          | Optional     | Single       | Specifies the ward the precinct is       |                                          |
|                        |                                        |              |              | contained within.                        |                                          |
+------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_style_id,electoral_district_ids,external_identifier_type,external_identifier_othertype,external_identifier_value,is_mail_only,locality_id,name,number,polling_location_ids,precinct_split_name,spatial_boundary_id,ward
    pre90111,bs00010,ed001,ocd-id,,ocd-division/country:us,false,loc001,203 - GEORGETOWN,0203,poll001 poll002,split13,sb1,,5
    pre90112,bs00011,ed002,fips,,42,false,loc001,203 - GEORGETOWN,0203,poll003,split26,,6
    pre90113,bs00010,ed003,,,,false,loc002,203 - GEORGETOWN,0203,poll004,split54,sb1,7


.. _single-csv-retention-contest:

retention_contest
~~~~~~~~~~~~~~~~~

``RetentionContest`` extends :ref:`single-csv-ballot-measure-contest` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| candidate_id | ``xs:IDREF`` | **Required** | Single       | Links to the :ref:`single-csv-candidate` |                                          |
|              |              |              |              | being retained.                          |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_id    | ``xs:IDREF`` | Optional     | Single       | Links to the information about the       |                                          |
|              |              |              |              | office.                                  |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-schedule:

schedule
~~~~~~~~

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type               | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=========================+==============+==============+==========================================+==========================================+
| is_only_by_appointment | ``xs:boolean``          | Optional     | Single       | If true, the place is only open during   |                                          |
|                        |                         |              |              | the specified time window with an        |                                          |
|                        |                         |              |              | appointment.                             |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_or_by_appointment   | ``xs:boolean``          | Optional     | Single       | If true, the place is open during the    |                                          |
|                        |                         |              |              | hours specified time window and may also |                                          |
|                        |                         |              |              | be open with an appointment.             |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_subject_to_change   | ``xs:boolean``          | Optional     | Single       | If true, the place should be open during |                                          |
|                        |                         |              |              | the specified time window, but may be    |                                          |
|                        |                         |              |              | subject to change. People should contact |                                          |
|                        |                         |              |              | prior to arrival to confirm hours are    |                                          |
|                        |                         |              |              | still accurate.                          |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_date             | ``xs:date``             | Optional     | Single       | The date at which this collection of     |                                          |
|                        |                         |              |              | start and end times and options begin.   |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_date               | ``xs:date``             | Optional     | Single       | The date at which this collection of     |                                          |
|                        |                         |              |              | start and end times and options end.     |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id          | ``xs:IDREF``            | **Required** | Single       | A reference to the associated hours_open |                                          |
|                        |                         |              |              | element.                                 |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,start_time,end_time,is_only_by_appointment,is_or_by_appointment,is_subject_to_change,start_date,end_date,hours_open_id
    sch001,07:00:00-06:00,22:00:00-06:00,,true,,2016-10-10,2016-10-12,ho001
    sch002,09:00:00-06:00,20:00:00-06:00,true,,,2016-10-13,2016-10-15,ho001
    sch003,08:00:00-06:00,14:00:00-06:00,,,true,2016-10-10,2016-10-15,ho002


.. _single-csv-simple-address-type:

simple_address_type
~~~~~~~~~~~~~~~~~~~

A ``SimpleAddressType`` represents a structured address.

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| structured_line_1 | ``xs:string`` | **Required** | Single       | The address line for a structured        |                                          |
|                   |               |              |              | address. Should include the street       |                                          |
|                   |               |              |              | number, street name, and any prefix and  |                                          |
|                   |               |              |              | suffix.                                  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_2 | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_3 | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_city   | ``xs:string`` | **Required** | Single       | The City value of a structured address.  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_state  | ``xs:string`` | **Required** | Single       | The State value of a structured address. |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_zip    | ``xs:string`` | Optional     | Single       | The ZIP code of a structured address.    |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-source:

source
~~~~~~

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=================+==============+==============+==========================================+==========================================+
| name                        | ``xs:string``   | **Required** | Single       | Specifies the name of the organization   |                                          |
|                             |                 |              |              | that is providing the information.       |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vip_id                      | ``xs:string``   | **Required** | Single       | Specifies the ID of the organization.    |                                          |
|                             |                 |              |              | VIP uses FIPS_ codes for this ID.        |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_time                   | ``xs:dateTime`` | **Required** | Single       | Specifies the date and time of the feed  |                                          |
|                             |                 |              |              | production. The date/time is considered  |                                          |
|                             |                 |              |              | to be in the timezone local to the       |                                          |
|                             |                 |              |              | organization.                            |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description                 | ``xs:string``   | Optional     | Single       | Specifies both the nature of the         |                                          |
|                             |                 |              |              | organization providing the data and what |                                          |
|                             |                 |              |              | data is in the feed.                     |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| organization_uri            | ``xs:string``   | Optional     | Single       | Specifies a URI to the home page of the  |                                          |
|                             |                 |              |              | organization publishing the data.        |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feed_contact_information_id | ``xs:IDREF``    | Optional     | Single       | Reference to the                         |                                          |
|                             |                 |              |              | :ref:`single-csv-person` who will        |                                          |
|                             |                 |              |              | respond to inquiries about the           |                                          |
|                             |                 |              |              | information contained within the file.   |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| terms_of_use_uri            | ``xs:anyURI``   | Optional     | Single       | Specifies the website where the Terms of |                                          |
|                             |                 |              |              | Use for the information in this file can |                                          |
|                             |                 |              |              | be found.                                |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| version                     | ``xs:string``   | Optional     | Single       | Specifies the version of the data        |                                          |
+-----------------------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date_time,description,name,organization_uri,terms_of_use_uri,vip_id,version
    source01,2016-06-02T10:24:08,SBE is the official source for Virginia data,"State Board of Elections, Commonwealth of Virginia",http://www.sbe.virginia.gov/,http://example.com/terms,51,5.1


.. _single-csv-spatial-boundary:

spatial_boundary
~~~~~~~~~~~~~~~~

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+--------------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                            | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+================================+==============+==============+==============+==========================================+==========================================+
| external_geospatial_feature_id | ``xs:IDREF`` | **Required** | Single       | The spatial boundary defined by a        |                                          |
|                                |              |              |              | geospatial feature that is external to   |                                          |
|                                |              |              |              | the VIP feed.                            |                                          |
+--------------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,external_geospatial_feature_id
    sb1,egf1


.. _single-csv-state:

state
~~~~~

The State object includes state-wide election information. The ID attribute is
recommended to be the state's FIPS code, along with the prefix "st".

+----------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+========================================+==============+==============+==========================================+==========================================+
| election_administration_id | ``xs:IDREF``                           | Optional     | Single       | Links to the state's election            |                                          |
|                            |                                        |              |              | administration object.                   |                                          |
+----------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers       | :ref:`single-csv-external-identifiers` | Optional     | Single       | Other identifier for the state that      |                                          |
|                            |                                        |              |              | relates to another dataset (e.g.         |                                          |
|                            |                                        |              |              | `OCD-ID`_).                              |                                          |
+----------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                       | ``xs:string``                          | **Required** | Single       | Specifiers the name of a state, such as  |                                          |
|                            |                                        |              |              | Alabama.                                 |                                          |
+----------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids       | ``xs:IDREFS``                          | Optional     | Single       | Specifies a link to the state's          |                                          |
|                            |                                        |              |              | :ref:`polling locations                  |                                          |
|                            |                                        |              |              | <single-csv-polling-location>`. If early |                                          |
|                            |                                        |              |              | vote centers or ballot drop locations    |                                          |
|                            |                                        |              |              | are state-wide (e.g., anyone in the      |                                          |
|                            |                                        |              |              | state can use them), they can be         |                                          |
|                            |                                        |              |              | specified here, but you are encouraged   |                                          |
|                            |                                        |              |              | to only use the                          |                                          |
|                            |                                        |              |              | :ref:`single-csv-precinct` element.      |                                          |
+----------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_administration_id,external_identifier_type,external_identifier_othertype,external_identifier_value,name,polling_location_ids
    st51,ea123,ocd-id,,ocd-division/country:us/state:va,Virginia,


.. _single-csv-street-segment:

street_segment
~~~~~~~~~~~~~~

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address, in which case these values
are equal.

+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                  | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+============================+==============+==============+==========================================+==========================================+
| address_direction      | ``xs:string``              | Optional     | Single       | Specifies the (inter-)cardinal direction |                                          |
|                        |                            |              |              | of the entire address. An example is     |                                          |
|                        |                            |              |              | "NE" for the address "100 E Capitol St   |                                          |
|                        |                            |              |              | NE."                                     |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city                   | ``xs:string``              | **Required** | Single       | The city specifies the city or town of   |                                          |
|                        |                            |              |              | the address.                             |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_addresses | ``xs:boolean``             | Optional     | Single       | Specifies if the segment covers every    |                                          |
|                        |                            |              |              | address on this street. If this is       |                                          |
|                        |                            |              |              | *true*, then the values of               |                                          |
|                        |                            |              |              | **StartHouseNumber** and                 |                                          |
|                        |                            |              |              | **EndHouseNumber** should be ignored.    |                                          |
|                        |                            |              |              | The value of **OddEvenBoth** must be     |                                          |
|                        |                            |              |              | *both*.                                  |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_streets   | ``xs:boolean``             | Optional     | Single       | Specifies if the segment covers every    |                                          |
|                        |                            |              |              | street in this city. If this is *true*,  |                                          |
|                        |                            |              |              | then the values of **OddEvenBoth**,      |                                          |
|                        |                            |              |              | **StartHouseNumber**,                    |                                          |
|                        |                            |              |              | **EndHouseNumber**, **StreetName**, and  |                                          |
|                        |                            |              |              | **Zip** should be ignored.               |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| odd_even_both          | :ref:`single-csv-oeb-enum` | **Required** | Single       | Specifies whether the odd side of the    | If the field is not present or invalid,  |
|                        |                            |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                        |                            |              |              | even side, or both are in included in    | the StreetSegment containing it.         |
|                        |                            |              |              | the street segment.                      |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_id            | ``xs:IDREF``               | **Required** | Single       | References the                           |                                          |
|                        |                            |              |              | :ref:`single-csv-precinct` that contains |                                          |
|                        |                            |              |              | the entire street segment. If a precinct |                                          |
|                        |                            |              |              | has a :ref:`single-csv-spatial-boundary` |                                          |
|                        |                            |              |              | which also contains the entire street    |                                          |
|                        |                            |              |              | segment, then the precinct assignment    |                                          |
|                        |                            |              |              | from the segment will be preferred over  |                                          |
|                        |                            |              |              | the assignment defined by the spatial    |                                          |
|                        |                            |              |              | boundary.                                |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_house_number     | ``xs:integer``             | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** or       |
|                        |                            |              |              | segment starts. This value is necessary  | **IncludesAllStreets** are true, if the  |
|                        |                            |              |              | for the street segment to make any       | field is not present or invalid, the     |
|                        |                            |              |              | sense. Unless **IncludesAllAddresses**   | implementation is required to ignore the |
|                        |                            |              |              | or **IncludesAllStreets** are true, this | StreetSegment element containing it. If  |
|                        |                            |              |              | value must be less than or equal to      | the **StartHouseNumber** is greater than |
|                        |                            |              |              | **EndHouseNumber**. If                   | the **EndHouseNumber**, the              |
|                        |                            |              |              | **IncludesAllAddresses** or              | implementation should ignore the element |
|                        |                            |              |              | **IncludesAllStreets** are true, this    | containing them.                         |
|                        |                            |              |              | value is ignored.                        |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_house_number       | ``xs:integer``             | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** or       |
|                        |                            |              |              | segment ends. This value is necessary    | **IncludesAllStreets** are true, if the  |
|                        |                            |              |              | for the street segment to make any       | field is not present or invalid, the     |
|                        |                            |              |              | sense. Unless **IncludesAllAddresses**   | implementation is required to ignore the |
|                        |                            |              |              | or **IncludesAllStreets** are true, it   | StreetSegment element containing it. If  |
|                        |                            |              |              | must be greater than or equal to         | the **EndHouseNumber** is less than the  |
|                        |                            |              |              | **StartHouseNumber**. If                 | **StartHouseNumber**, the implementation |
|                        |                            |              |              | **IncludesAllAddresses** or              | should ignore the element containing it. |
|                        |                            |              |              | **IncludesAllStreets** are true, this    |                                          |
|                        |                            |              |              | value is ignored.                        |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_prefix    | ``xs:string``              | Optional     | Single       | Part of a street address. It may contain |                                          |
|                        |                            |              |              | letters or slashes (e.g., 'B' in 'B22    |                                          |
|                        |                            |              |              | Main St'). If this value is present then |                                          |
|                        |                            |              |              | **StartHouseNumber** must be equal to    |                                          |
|                        |                            |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                        |                            |              |              | used if **IncludesAllAddresses** or      |                                          |
|                        |                            |              |              | **IncludesAllStreets** are true.         |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_suffix    | ``xs:string``              | Optional     | Single       | Part of a street address. It may contain |                                          |
|                        |                            |              |              | letters or slashes (e.g., 1/2 in '22 1/2 |                                          |
|                        |                            |              |              | Main St'). If this value is present then |                                          |
|                        |                            |              |              | **StartHouseNumber** must be equal to    |                                          |
|                        |                            |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                        |                            |              |              | used if **IncludesAllAddresses** or      |                                          |
|                        |                            |              |              | **IncludesAllStreets** are true.         |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state                  | ``xs:string``              | **Required** | Single       | Specifies the two-letter state           |                                          |
|                        |                            |              |              | abbreviation of the address.             |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_direction       | ``xs:string``              | Optional     | Single       | Specifies the (inter-)cardinal direction |                                          |
|                        |                            |              |              | of the street address (e.g., the "E" in  |                                          |
|                        |                            |              |              | "100 E Capitol St NE").                  |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_name            | ``xs:string``              | Optional     | Single       | Represents the name of the street for    |                                          |
|                        |                            |              |              | the address. A special wildcard, "*",    |                                          |
|                        |                            |              |              | denotes every street in the given        |                                          |
|                        |                            |              |              | city/town. It optionally may contain     |                                          |
|                        |                            |              |              | street direction, street suffix or       |                                          |
|                        |                            |              |              | address direction (e.g., both "Capitol"  |                                          |
|                        |                            |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                        |                            |              |              | the address "100 E Capitol St NE"),      |                                          |
|                        |                            |              |              | however this is not preferred. Preferred |                                          |
|                        |                            |              |              | is street name alone (e.g. "Capitol").   |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_suffix          | ``xs:string``              | Optional     | Single       | Represents the abbreviated,              |                                          |
|                        |                            |              |              | non-directional suffix to the street     |                                          |
|                        |                            |              |              | name. An example is "St" for the address |                                          |
|                        |                            |              |              | "100 E Capitol St NE."                   |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| unit_number            | ``xs:string``              | Optional     | Repeats      | The apartment/unit number for a street   |                                          |
|                        |                            |              |              | segment. If this value is present then   |                                          |
|                        |                            |              |              | **StartHouseNumber** must be equal to    |                                          |
|                        |                            |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                        |                            |              |              | used if **IncludesAllAddresses** or      |                                          |
|                        |                            |              |              | **IncludesAllStreets** are true.         |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| zip                    | ``xs:string``              | Optional     | Single       | Specifies the zip code of the address.   |                                          |
|                        |                            |              |              | It may be 5 or 9 digits, and it may      |                                          |
|                        |                            |              |              | include a hyphen ('-'). It is required   |                                          |
|                        |                            |              |              | as it helps with geocoding, which is     |                                          |
|                        |                            |              |              | crucial for distributors.                |                                          |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,address_direction,city,includes_all_addresses,includes_all_streets,odd_even_both,precinct_id,start_house_number,end_house_number,house_number_prefix,house_number_suffix,state,street_direction,street_name,street_suffix,unit_number,zip
    ss000001,N,Washington,false,false,odd,pre90113,101,199,,,DC,NW,Delaware,St,,20001
    ss000002,S,Washington,true,false,both,pre90112,,,,,DC,SE,Wisconsin,Ave,,20002
    ss000003,N,Washington,false,false,even,pre90113,100,100,A,1/2,DC,NW,Delaware,St,,20001


.. _single-csv-term:

term
~~~~

+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+====================================+==============+==============+==========================================+==========================================+
| term_type       | :ref:`single-csv-office-term-type` | **Required** | Single       | Specifies the type of office term (see   |                                          |
|                 |                                    |              |              | :ref:`single-csv-office-term-type` for   |                                          |
|                 |                                    |              |              | valid values).                           |                                          |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term_start_date | ``xs:date``                        | Optional     | Single       | Specifies the start date for the current |                                          |
|                 |                                    |              |              | term of the office.                      |                                          |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term_end_date   | ``xs:date``                        | Optional     | Single       | Specifies the end date for the current   |                                          |
|                 |                                    |              |              | term of the office.                      |                                          |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-time-with-zone:

time_with_zone
~~~~~~~~~~~~~~

A string pattern restricting the value to a time with an included offset from
UTC. The pattern is

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))(Z|[+-]((0[0-9]|1[0-3]):[0-5][0-9]|14:00))``

.. code-block:: xml
   :linenos:

   <HoursOpen id="hours0001">
     <Schedule>
       <Hours>
         <StartTime>06:00:00-05:00</StartTime>
         <EndTime>12:00:00-05:00</EndTime>
       </Hours>
       <Hours>
         <StartTime>13:00:00-05:00</StartTime>
         <EndTime>19:00:00-05:00</EndTime>
       </Hours>
       <StartDate>2013-11-05</StartDate>
       <EndDate>2013-11-05</EndDate>
     </Schedule>
   </HoursOpen>


.. _single-csv-voter-service:

voter_service
~~~~~~~~~~~~~

+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=======================================+==============+==============+==========================================+==========================================+
| description                 | ``xs:string``                         | Optional     | Single       | Long description of the services         |                                          |
|                             |                                       |              |              | available.                               |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_official_person_id | ``xs:IDREF``                          | Optional     | Single       | The :ref:`authority <single-csv-person>` |                                          |
|                             |                                       |              |              | for a particular voter service.          |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                        | :ref:`single-csv-voter-service-type`  | Optional     | Single       | The type of :ref:`voter service          |                                          |
|                             |                                       |              |              | <single-csv-voter-service-type>`.        |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                  | ``xs:string``                         | Optional     | Single       | If Type is "other", OtherType allows for |                                          |
|                             |                                       |              |              | cataloging another type of voter         |                                          |
|                             |                                       |              |              | service.                                 |                                          |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,description,election_official_person_id,type,other_type,department_id
    vs01,A service we provide,per50002,other,overseas-voting,dep01
    vs00,Elections notifications,per50002,other,voter-registration,dep02
    vs02,Pencil sharpening,per50002,other,office-help,dep03
    vs03,Guided hike to polling place,per50002,other,polling-places,dep03
    vs04,Bike messenger ballot delivery,per50002,other,absentee-ballots,dep03


.. _single-csv-enumerations:

Enumerations
------------


.. _single-csv-ballot-measure-type:

ballot_measure_type
~~~~~~~~~~~~~~~~~~~

A list of the various types of ballot measures. States may have different legal
definitions of each type; Wikipedia_ has more details about each type.  These
values are to help states with multiple types of non-candidate-based contests
distinguish between each type; as such, the definitions in this table are simple
guidelines. Ultimately it is up to the state or local election official to
choose the value which best describes the ballot measure(s) in their
jurisdiction.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| ballot-measure | A catch-all for generic types of                   |
|                | non-candidate-based contests.                      |
+----------------+----------------------------------------------------+
| initiative     | These are usually citizen-driven measures to be    |
|                | placed on the ballot. These could include both     |
|                | statutory changes and constitutional amendments.   |
+----------------+----------------------------------------------------+
| referendum     | These could include measures to repeal existing    |
|                | acts of legislation, legislative referrals, and    |
|                | legislatively-referred state constitutional        |
|                | amendments.                                        |
+----------------+----------------------------------------------------+
| other          | Anything that does not fall into the above         |
|                | categories.                                        |
+----------------+----------------------------------------------------+


.. _single-csv-candidate-post-election-status:

candidate_post_election_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+----------------------------------------------------+
| Tag                | Description                                        |
+====================+====================================================+
| advanced-to-runoff | For contests in which the top *N* candidates       |
|                    | advance to the next round.                         |
+--------------------+----------------------------------------------------+
| projected-winner   | A candidate is expected to win, but official       |
|                    | results are not yet complete.                      |
+--------------------+----------------------------------------------------+
| winner             | The candidate has officially won.                  |
+--------------------+----------------------------------------------------+
| withdrawn          | The candidate has withdrawn from the contest.      |
+--------------------+----------------------------------------------------+


.. _single-csv-candidate-pre-election-status:

candidate_pre_election_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| filed        | The candidate has filed for office but not yet     |
|              | been qualified.                                    |
+--------------+----------------------------------------------------+
| qualified    | The candidate has qualified for the contest.       |
+--------------+----------------------------------------------------+
| withdrawn    | The candidate has withdrawn from the contest (but  |
|              | may still be on the ballot).                       |
+--------------+----------------------------------------------------+
| write-in     |                                                    |
+--------------+----------------------------------------------------+


.. _single-csv-checksum-algorithm:

checksum_algorithm
~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| sha-256      | 256-bit cryptographic hash algorithm of the SHA-2  |
|              | family                                             |
+--------------+----------------------------------------------------+
| sha-512      | 512-bit cryptographic hash algorithm of the SHA-2  |
|              | family                                             |
+--------------+----------------------------------------------------+


.. _single-csv-district-type:

district_type
~~~~~~~~~~~~~

Enumeration describing the set of possible jurisdiction and district types.
Please use the enumeration value which most accurately reflects the type of
district or jurisdiction in your state or county. For example, "town" and
"township" may mean different things -- or not be defined at all -- in your
state, so please use the definition which best matches your local meaning.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| borough        | A borough                                          |
+----------------+----------------------------------------------------+
| city           | A city.                                            |
+----------------+----------------------------------------------------+
| city-council   | A specific seat/jurisdiction for a city, town, or  |
|                | village council.                                   |
+----------------+----------------------------------------------------+
| congressional  | A United States congressional district.            |
+----------------+----------------------------------------------------+
| county         | A county.                                          |
+----------------+----------------------------------------------------+
| county-council | A county council district, either in its entirety  |
|                | or for a specific seat.                            |
+----------------+----------------------------------------------------+
| judicial       | A judicial district.                               |
+----------------+----------------------------------------------------+
| municipality   | A civil division which is not a town, city,        |
|                | village, or county.                                |
+----------------+----------------------------------------------------+
| national       | The United States.                                 |
+----------------+----------------------------------------------------+
| school         | A school district.                                 |
+----------------+----------------------------------------------------+
| special        | A `special-purpose district`_ that exist separate  |
|                | from general-purpose districts.                    |
+----------------+----------------------------------------------------+
| state          | A state, district, commonwealth, or U.S.           |
|                | territory.                                         |
+----------------+----------------------------------------------------+
| state-house    | The lower house of a state legislature.            |
+----------------+----------------------------------------------------+
| state-senate   | The upper house of a state legislature.            |
+----------------+----------------------------------------------------+
| town           | A town_.                                           |
+----------------+----------------------------------------------------+
| township       | A township, which may be different than a town.    |
|                | See the `Wikipedia article`_.                      |
+----------------+----------------------------------------------------+
| utility        | A non-water public or municipal utility district.  |
+----------------+----------------------------------------------------+
| village        | A village district.                                |
+----------------+----------------------------------------------------+
| ward           | A ward.                                            |
+----------------+----------------------------------------------------+
| water          | A water district.                                  |
+----------------+----------------------------------------------------+
| other          | Any district not described above. Use the          |
|                | *OtherType* field to describe it.                  |
+----------------+----------------------------------------------------+


.. _single-csv-geospatial-format:

geospatial_format
~~~~~~~~~~~~~~~~~

Geospatial file formats that are supported by the VIP specification.

+--------------+---------------------------------------------------------------------------+
| Tag          | Description                                                               |
+==============+===========================================================================+
| shp          | ESRI Shapefile (`reference                                                |
|              | <https://www.loc.gov/preservation/digital/formats/fdd/fdd000280.shtml>`_) |
+--------------+---------------------------------------------------------------------------+


.. _single-csv-identifier-type:

identifier_type
~~~~~~~~~~~~~~~

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| fips           | Federal Information Processing Standards codes for |
|                | states_, counties_, and cities_.                   |
+----------------+----------------------------------------------------+
| local-level    | An identifier generated or used by local           |
|                | governments or organizations.                      |
+----------------+----------------------------------------------------+
| national-level | An identifier generated or used by national        |
|                | organizations.                                     |
+----------------+----------------------------------------------------+
| ocd-id         | An `Open Civic Data Division Identifier`_.         |
+----------------+----------------------------------------------------+
| state-level    | An identifier generated or used by state           |
|                | governments or organizations.                      |
+----------------+----------------------------------------------------+
| other          | Any identifier which doesn't fall into any of the  |
|                | above categories.                                  |
+----------------+----------------------------------------------------+


.. _single-csv-oeb-enum:

oeb_enum
~~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| both         | Both even and odd addresses within the range.      |
+--------------+----------------------------------------------------+
| even         | Only even-numbered addresses within the range.     |
+--------------+----------------------------------------------------+
| odd          | Only odd-numbered addresses within the range.      |
+--------------+----------------------------------------------------+


.. _single-csv-office-term-type:

office_term_type
~~~~~~~~~~~~~~~~

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| full-term      | This election is for an office for which the       |
|                | existing term has been completed.                  |
+----------------+----------------------------------------------------+
| unexpired-term | This election is for an office for which the       |
|                | original term is not yet complete.                 |
+----------------+----------------------------------------------------+


.. _single-csv-vote-variation:

vote_variation
~~~~~~~~~~~~~~

Note that the descriptions below describe what the enumeration names
stand for in the context of the VIP spec, rather than provide general
definitions of the election terms that the names correspond to.  For example,
even though there are majority voting methods that are not "1-of-m" (e.g.
ranked choice voting), we constrain "majority" to 1-of-m.  We do this to
eliminate any source of ambiguity when a single enumeration value needs
to be assigned to a contest.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| 1-of-m         | A method where each voter can select up to one     |
|                | option.                                            |
+----------------+----------------------------------------------------+
| approval       | `Approval voting`_, where each voter can select as |
|                | many options as desired.                           |
+----------------+----------------------------------------------------+
| borda          | `Borda count`_, where each voter can rank the      |
|                | options, and the rankings are assigned point       |
|                | values.                                            |
+----------------+----------------------------------------------------+
| cumulative     | `Cumulative voting`_, where each voter can         |
|                | distribute their vote to up to *N* options.        |
+----------------+----------------------------------------------------+
| majority       | A 1-of-m method where the winner needs more than   |
|                | 50% of the vote to be elected.                     |
+----------------+----------------------------------------------------+
| n-of-m         | A method where each voter can select up to *N*     |
|                | options.                                           |
+----------------+----------------------------------------------------+
| plurality      | A 1-of-m method where the option with the most     |
|                | votes is elected, regardless of whether the option |
|                | has more than 50% of the vote.                     |
+----------------+----------------------------------------------------+
| proportional   | A `proportional representation`_ method (other     |
|                | than STV), which is any system that elects winners |
|                | in proportion to the total vote.                   |
+----------------+----------------------------------------------------+
| range          | `Range voting`_, where each voter can select a     |
|                | score for each option.                             |
+----------------+----------------------------------------------------+
| rcv            | `Ranked choice voting`_ (RCV), where each voter    |
|                | can rank the options, and the ballots are counted  |
|                | in rounds.  Also known as instant-runoff voting    |
|                | (IRV) and the single transferable vote (STV).      |
+----------------+----------------------------------------------------+
| super-majority | A 1-of-m method where the winner needs more than   |
|                | some predetermined fraction of the vote to be      |
|                | elected, where the fraction is more than 50% (e.g. |
|                | three-fifths or two-thirds).                       |
+----------------+----------------------------------------------------+
| other          | Used when the vote variation type is not included  |
|                | in this enumeration.                               |
+----------------+----------------------------------------------------+


.. _single-csv-voter-service-type:

voter_service_type
~~~~~~~~~~~~~~~~~~

+--------------------+----------------------------------------------------+
| Tag                | Description                                        |
+====================+====================================================+
| absentee-ballots   | This department handles the dispatch, tracking,    |
|                    | and return of absentee ballots.                    |
+--------------------+----------------------------------------------------+
| overseas-voting    | The department for overseas, military, and other   |
|                    | outside-the-U.S. voters.                           |
+--------------------+----------------------------------------------------+
| polling-places     | This deparment handles the selection and           |
|                    | management of polling places.                      |
+--------------------+----------------------------------------------------+
| voter-registration | The deparment that manages voter registration.     |
+--------------------+----------------------------------------------------+
| other              | Any other service not covered by the above         |
|                    | descriptions.                                      |
+--------------------+----------------------------------------------------+
