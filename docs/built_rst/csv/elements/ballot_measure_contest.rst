.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ballot-measure-contest:

ballot_measure_contest
======================

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends :ref:`multi-csv-contest-base`.

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
|                   |               |              |              | :ref:`multi-csv-ballot-measure-type`     |                                          |
|                   |               |              |              | options.                                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type        | ``xs:string`` | Optional     | Single       | Allows for cataloging a new              |                                          |
|                   |               |              |              | :ref:`multi-csv-ballot-measure-type`     |                                          |
|                   |               |              |              | option, when Type is specified as        |                                          |
|                   |               |              |              | "other."                                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,elecoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation,con_statement,effect_of_abstain,full_text,info_uri,passage_threshold,pro_statement,summary_text,type,other_type
    bmc0001,HB2,bs001 bs002 bs003,Raising levy for School Bond,School Bond Issue,ed001,all registered voters,,54,false,School Bond,42,majority,,This is no good.,No effect,A measure to do raise funds for etc etc,www.ballotmeasure.com,two-thirds,Everything will be great.,It’s a referendum about school funding,referendum,


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
