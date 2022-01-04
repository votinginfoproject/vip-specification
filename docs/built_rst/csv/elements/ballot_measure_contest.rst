.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ballot-measure-contest:

ballot_measure_contest
======================

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends :ref:`multi-csv-contest-base`.

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| con_statement     | ``xs:string`` | Optional     | Single       | Specifies a statement in opposition to   | If the element is invalid or not         |
|                   |               |              |              | the referendum. It does not necessarily  | present, then the implementation is      |
|                   |               |              |              | appear on the ballot.                    | required to ignore it.                   |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| effect_of_abstain | ``xs:string`` | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the element is invalid or not         |
|                   |               |              |              | not voting) on this proposition will     | present, then the implementation is      |
|                   |               |              |              | have (i.e. whether abstaining is         | required to ignore it.                   |
|                   |               |              |              | considered a vote against it).           |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_text         | ``xs:string`` | Optional     | Single       | Specifies the full text of the           | If the element is invalid or not         |
|                   |               |              |              | referendum as it appears on the ballot.  | present, then the implementation is      |
|                   |               |              |              |                                          | required to ignore it.                   |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| info_uri          | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that links to additional | If the field is invalid or not present,  |
|                   |               |              |              | information about the referendum.        | then the implementation is required to   |
|                   |               |              |              |                                          | ignore it.                               |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| passage_threshold | ``xs:string`` | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                   |               |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                   |               |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                   |               |              |              | 50% plus one vote). Other common         |                                          |
|                   |               |              |              | thresholds are "three-fifths" and        |                                          |
|                   |               |              |              | "two-thirds". If there are `competing    |                                          |
|                   |               |              |              | initiatives`_, information about their   |                                          |
|                   |               |              |              | effect on the passage of the             |                                          |
|                   |               |              |              | BallotMeasureContest would go here.      |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pro_statement     | ``xs:string`` | Optional     | Single       | Specifies a statement in favor of the    | If the element is invalid or not         |
|                   |               |              |              | referendum. It does not necessarily      | present, then the implementation is      |
|                   |               |              |              | appear on the ballot.                    | required to ignore it.                   |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| summary_text      | ``xs:string`` | Optional     | Single       | Specifies a short summary of the         | If the element is invalid or not         |
|                   |               |              |              | referendum that is on the ballot, below  | present, then the implementation is      |
|                   |               |              |              | the title, but above the text.           | required to ignore it.                   |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type              | ``xs:string`` | Optional     | Single       | Specifies the particular type of ballot  | If the field is invalid or not present,  |
|                   |               |              |              | measure. Must be one of the valid        | then the implementation is required to   |
|                   |               |              |              | :ref:`multi-csv-ballot-measure-type`     | ignore it.                               |
|                   |               |              |              | options.                                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type        | ``xs:string`` | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                   |               |              |              | :ref:`multi-csv-ballot-measure-type`     | then the implementation is required to   |
|                   |               |              |              | option, when Type is specified as        | ignore it.                               |
|                   |               |              |              | "other."                                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,elecoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation,con_statement,effect_of_abstain,full_text,info_uri,passage_threshold,pro_statement,summary_text,type,other_type
    bmc0001,HB2,bs001 bs002 bs003,Raising levy for School Bond,School Bond Issue,ed001,all registered voters,,54,false,School Bond,42,majority,,This is no good.,No effect,A measure to do raise funds for etc etc,www.ballotmeasure.com,two-thirds,Everything will be great.,It’s a referendum about school funding,referendum,
.. _competing initiatives: http://ballotpedia.org/Laws_governing_the_initiative_process_in_California#Competing_initiatives


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
| abbreviation             | ``xs:string``                   | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                 |              |              |                                          | then the implementation should ignore    |
|                          |                                 |              |              |                                          | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                   | Optional     | Single       | References a set of BallotSelections,    | If the field is invalid or not present,  |
|                          |                                 |              |              | which could be of any selection type     | then the implementation should ignore    |
|                          |                                 |              |              | that extends                             | it.                                      |
|                          |                                 |              |              | :ref:`multi-csv-ballot-selection-base`.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                   | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                 |              |              | the ballot.                              | present, then the implementation should  |
|                          |                                 |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                   | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                 |              |              | the ballot.                              | present, then the implementation should  |
|                          |                                 |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                    | **Required** | Single       | References an                            | If the field is invalid, then the        |
|                          |                                 |              |              | :ref:`multi-csv-electoral-district`      | implementation is required to ignore the |
|                          |                                 |              |              | element that represents the geographical | ``ContestBase`` element containing it.   |
|                          |                                 |              |              | scope of the contest.                    |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                   | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                          |                                 |              |              | electorate for this contest past the     | present, then the implementation should  |
|                          |                                 |              |              | usual, "all registered voters"           | ignore it.                               |
|                          |                                 |              |              | electorate. This subtag will most often  |                                          |
|                          |                                 |              |              | be used for primaries and local          |                                          |
|                          |                                 |              |              | elections. In primaries, voters may have |                                          |
|                          |                                 |              |              | to be registered as a specific party to  |                                          |
|                          |                                 |              |              | vote, or there may be special rules for  |                                          |
|                          |                                 |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                 |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                   | Optional     | Single       | Other identifiers for a contest that     | If the element is invalid or not         |
|                          |                                 |              |              | links to another source of information.  | present, then the implementation should  |
|                          |                                 |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                  | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                 |              |              | contest are rotated.                     | then the implementation should ignore    |
|                          |                                 |              |              |                                          | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                   | **Required** | Single       | Name of the contest, not necessarily how | If the field is invalid, then the        |
|                          |                                 |              |              | it appears on the ballot (NB:            | implementation is required to ignore the |
|                          |                                 |              |              | BallotTitle should be used for this      | ``ContestBase`` element containing it.   |
|                          |                                 |              |              | purpose).                                |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                  | Optional     | Single       | Order in which the contests are listed   | If the field is invalid or not present,  |
|                          |                                 |              |              | on the ballot. This is the default       | then the implementation should ignore    |
|                          |                                 |              |              | ordering, and can be overrides by data   | it.                                      |
|                          |                                 |              |              | in a :ref:`multi-csv-ballot-style`       |                                          |
|                          |                                 |              |              | element.                                 |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`multi-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       | If the field is invalid or not present,  |
|                          |                                 |              |              | contest (e.g. n-of-m, majority, et al).  | then the implementation should ignore    |
|                          |                                 |              |              |                                          | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``        | Optional     | Single       | If "other" is selected as the            | If the field is invalid or not present,  |
|                          |                                 |              |              | **VoteVariation**, the name of the       | then the implementation should ignore    |
|                          |                                 |              |              | variation can be specified here.         | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
