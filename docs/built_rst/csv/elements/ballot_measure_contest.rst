.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ballot-measure-contest:

ballot_measure_contest
======================

BallotMeasureContest extends :ref:`multi-csv-contest-base` and provides information about a ballot measure or referendum before the voters.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearConStatement/>``, ``<ClearProStatement/>``, ``<ClearFullText/>``).

+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=========================================+==============+==============+==========================================+==========================================+
| con_statement     | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Statement in opposition to the measure.  | If the element is invalid or not         |
|                   |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| effect_of_abstain | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the element is invalid or not         |
|                   |                                         |              |              | not voting) on this proposition will     | present, then the implementation is      |
|                   |                                         |              |              | have (i.e. whether abstaining is         | required to ignore it.                   |
|                   |                                         |              |              | considered a vote against it). Clearable |                                          |
|                   |                                         |              |              | in overlays.                             |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_text         | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Full legal text of the ballot measure.   | If the element is invalid or not         |
|                   |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| info_uri          | :ref:`multi-csv-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|                   |                                         |              |              | about the measure. Clearable in          | present, then the implementation is      |
|                   |                                         |              |              | overlays.                                | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| passage_threshold | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                   |                                         |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                   |                                         |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                   |                                         |              |              | 50% plus one vote). Other common         |                                          |
|                   |                                         |              |              | thresholds are "three-fifths" and        |                                          |
|                   |                                         |              |              | "two-thirds". Clearable in overlays.     |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pro_statement     | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Statement in support of the measure.     | If the element is invalid or not         |
|                   |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| summary_text      | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Summary explanation of the measure.      | If the element is invalid or not         |
|                   |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type              | :ref:`multi-csv-ballot-measure-type`    | Optional     | Single       | Specifies the particular type of ballot  | If the field is invalid or not present,  |
|                   |                                         |              |              | measure from                             | then the implementation is required to   |
|                   |                                         |              |              | :ref:`multi-csv-ballot-measure-type`     | ignore it.                               |
|                   |                                         |              |              | (e.g. initiative, referendum,            |                                          |
|                   |                                         |              |              | constitutional amendment). Clearable in  |                                          |
|                   |                                         |              |              | overlays.                                |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type        | ``xs:string``                           | Optional     | Single       | Custom measure type if Type is "other".  | If the field is invalid or not present,  |
|                   |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,abbreviation,ballot_selection_ids,ballot_title,electoral_district_id,name,passage_threshold,type
    bmc0001,HB2,bs001 bs002,School Bond Issue,ed001,School Bond Issue,majority,referendum


.. _multi-csv-contest-base:

contest_base
------------

A base model for all Contest types: :ref:`multi-csv-ballot-measure-contest`, :ref:`multi-csv-candidate-contest`, :ref:`multi-csv-party-contest`, and :ref:`multi-csv-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=========================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                           | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                         |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                         |              |              |                                          | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                           | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                          |                                         |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                          |                                         |              |              |                                          | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                         |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                         |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                            | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                          |                                         |              |              | :ref:`multi-csv-electoral-district`      | implementation is required to ignore the |
|                          |                                         |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                          |                                         |              |              | the contest. Required in main feed;      |                                          |
|                          |                                         |              |              | optional in overlays.                    |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                          |                                         |              |              | electorate for this contest past the     | present, then the implementation should  |
|                          |                                         |              |              | usual "all registered voters"            | ignore it.                               |
|                          |                                         |              |              | electorate. This subtag will most often  |                                          |
|                          |                                         |              |              | be used for primaries and local          |                                          |
|                          |                                         |              |              | elections (e.g. in closed primaries,     |                                          |
|                          |                                         |              |              | voters may have to be registered as a    |                                          |
|                          |                                         |              |              | specific party to vote, or in some local |                                          |
|                          |                                         |              |              | elections, non-citizens can vote).       |                                          |
|                          |                                         |              |              | Clearable in overlays.                   |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`multi-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                         |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                          |                                         |              |              | overlays.                                | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                          | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                         |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                          |                                         |              |              | in overlays.                             | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                           | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                          |                                         |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                         |              |              |                                          | ``ContestBase`` element containing it.   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                          | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                          |                                         |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                         |              |              |                                          | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`multi-csv-vote-variation`         | Optional     | Single       | Vote variation associated with the       | If the field is invalid or not present,  |
|                          |                                         |              |              | contest from                             | then the implementation should ignore    |
|                          |                                         |              |              | :ref:`multi-csv-vote-variation` (e.g.    | it.                                      |
|                          |                                         |              |              | n-of-m, majority, plurality, ranked      |                                          |
|                          |                                         |              |              | choice, et al). Clearable in overlays.   |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``xs:string``                           | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                          |                                         |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                          |                                         |              |              |                                          | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive              | ``xs:string``                           | Optional     | Single       | If specified, the element is treated as  | If the field is invalid or not present,  |
|                          |                                         |              |              | inactive, and the value describes the    | then the implementation should ignore    |
|                          |                                         |              |              | reason (e.g. "Contest cancelled due to   | it.                                      |
|                          |                                         |              |              | unopposed candidate", "Backup polling    |                                          |
|                          |                                         |              |              | location"). Clearable in overlays.       |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
