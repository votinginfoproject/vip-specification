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

BallotMeasureContest extends :ref:`single-csv-contest-base` and provides information about a ballot measure or referendum before the voters.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearConStatement/>``, ``<ClearProStatement/>``, ``<ClearFullText/>``).

+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+==========================================+==============+==============+==========================================+==========================================+
| con_statement     | :ref:`single-csv-internationalized-text` | Optional     | Single       | Statement in opposition to the measure.  | If the element is invalid or not         |
|                   |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                          |              |              |                                          | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| effect_of_abstain | :ref:`single-csv-internationalized-text` | Optional     | Single       | Describes effect of abstaining on the    | If the element is invalid or not         |
|                   |                                          |              |              | measure. Clearable in overlays.          | present, then the implementation is      |
|                   |                                          |              |              |                                          | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_text         | :ref:`single-csv-internationalized-text` | Optional     | Single       | Full legal text of the ballot measure.   | If the element is invalid or not         |
|                   |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                          |              |              |                                          | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| info_uri          | :ref:`single-csv-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|                   |                                          |              |              | about the measure. Clearable in          | present, then the implementation is      |
|                   |                                          |              |              | overlays.                                | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| passage_threshold | :ref:`single-csv-internationalized-text` | Optional     | Single       | Threshold required for passage (e.g.     | If the element is invalid or not         |
|                   |                                          |              |              | "majority", "two-thirds"). Clearable in  | present, then the implementation is      |
|                   |                                          |              |              | overlays.                                | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pro_statement     | :ref:`single-csv-internationalized-text` | Optional     | Single       | Statement in support of the measure.     | If the element is invalid or not         |
|                   |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                          |              |              |                                          | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| summary_text      | :ref:`single-csv-internationalized-text` | Optional     | Single       | Summary explanation of the measure.      | If the element is invalid or not         |
|                   |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                   |                                          |              |              |                                          | required to ignore it.                   |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type              | :ref:`single-csv-ballot-measure-type`    | Optional     | Single       | Type of measure from                     | If the field is invalid or not present,  |
|                   |                                          |              |              | :ref:`single-csv-ballot-measure-type`.   | then the implementation is required to   |
|                   |                                          |              |              | Clearable in overlays.                   | ignore it.                               |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type        | ``xs:string``                            | Optional     | Single       | Custom measure type if Type is "other".  | If the field is invalid or not present,  |
|                   |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                   |                                          |              |              |                                          | ignore it.                               |
+-------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,abbreviation,ballot_selection_ids,ballot_title,electoral_district_id,name,passage_threshold,type
    bmc0001,HB2,bs001 bs002,School Bond Issue,ed001,School Bond Issue,majority,referendum


.. _single-csv-contest-base:

contest_base
^^^^^^^^^^^^

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`, :ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`, and :ref:`single-csv-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                          |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | :ref:`single-csv-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | :ref:`single-csv-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                          |                                          |              |              | :ref:`single-csv-electoral-district`     | implementation is required to ignore the |
|                          |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                          |                                          |              |              | the contest. Required in main feed;      |                                          |
|                          |                                          |              |              | optional in overlays.                    |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | :ref:`single-csv-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                          |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                          |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                          |                                          |              |              | overlays.                                | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                          |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                          |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                          |                                          |              |              | :ref:`single-csv-vote-variation`.        | it.                                      |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                          |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                          |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-ballot-measure-selection:

ballot_measure_selection
~~~~~~~~~~~~~~~~~~~~~~~~

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:ref:`single-csv-ballot-measure-contest` that would appear on the ballot.
BallotMeasureSelection extends :ref:`single-csv-ballot-selection-base`.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| selection    | ``xs:string`` | **Required** | Single       | Selection text for a                     | If the element is invalid or not         |
|              |               |              |              | :ref:`single-csv-ballot-measure-contest` | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the BallotMeasureSelection     |
|              |               |              |              |                                          | containing it.                           |
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
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|                |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|                |                |              |              | is the default ordering, and can be      | ignore it.                               |
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
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|                |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|                |                |              |              | is the default ordering, and can be      | ignore it.                               |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`single-csv-ordered-contest`.    |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-ballot-style:

ballot_style
~~~~~~~~~~~~

A container for the contests/measures on the ballot.

+----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=========================================+==============+==============+==========================================+==========================================+
| image_uri            | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Specifies a URI that returns an image of | If the element is invalid or not         |
|                      |                                         |              |              | the sample ballot.                       | present, then the implementation is      |
|                      |                                         |              |              |                                          | required to ignore it.                   |
+----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ordered_contests_ids | ``xs:IDREFS``                           | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                      |                                         |              |              | :ref:`single-csv-ordered-contest`        | then the implementation is required to   |
|                      |                                         |              |              |                                          | ignore it.                               |
+----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_ids            | ``xs:IDREFS``                           | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                      |                                         |              |              | :ref:`single-csv-party`s.                | then the implementation is required to   |
|                      |                                         |              |              |                                          | ignore it.                               |
+----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,image_uri!en,ordered_contest_ids,party_ids
    bs00010,http://i.giphy.com/26BoCh3PgT8ai45ji.gif,oc2025,par02
    bs00011,http://i.giphy.com/3oEjHYDWEICgEpAOjK.gif,oc3000 oc2025,par01


.. _single-csv-candidate:

candidate
~~~~~~~~~

The Candidate object represents a candidate in a contest. If a candidate is running in multiple contests, each contest **must** have its own Candidate object.

+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| Tag                  | Data Type                                        | Required?    | Repeats?     | Description                                       | Error Handling                           |
+======================+==================================================+==============+==============+===================================================+==========================================+
| ballot_name          | :ref:`single-csv-internationalized-text`         | **Required** | Single       | The candidate's name as it will appear on the     | If the element is invalid, then the      |
|                      |                                                  |              |              | ballot.                                           | implementation is required to ignore the |
|                      |                                                  |              |              |                                                   | ``Candidate`` element containing it.     |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| contact_information  | :ref:`single-csv-contact-information`            | Optional     | Single       | Campaign or official contact information for the  | If the element is invalid or not         |
|                      |                                                  |              |              | candidate.                                        | present, then the implementation is      |
|                      |                                                  |              |              |                                                   | required to ignore it.                   |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| external_identifier  | :ref:`single-csv-external-identifier`            | Optional     | Repeats      | External identifier(s) linking this candidate to  | If the element is invalid or not         |
|                      |                                                  |              |              | external systems.                                 | present, then the implementation is      |
|                      |                                                  |              |              |                                                   | required to ignore it.                   |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| file_date            | ``xs:date``                                      | Optional     | Single       | Date when the candidate filed for office.         | If the field is invalid or not present,  |
|                      |                                                  |              |              |                                                   | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| is_incumbent         | ``xs:boolean``                                   | Optional     | Single       | Indicates whether the candidate currently holds   | If the field is invalid or not present,  |
|                      |                                                  |              |              | the office.                                       | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| is_top_ticket        | ``xs:boolean``                                   | Optional     | Single       | Indicates whether the candidate is at the top of  | If the field is invalid or not present,  |
|                      |                                                  |              |              | a ticket.                                         | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| party_id             | ``xs:IDREF``                                     | Optional     | Single       | References the candidate's affiliated             | If the field is invalid or not present,  |
|                      |                                                  |              |              | :ref:`single-csv-party`.                          | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| person_id            | ``xs:IDREF``                                     | Optional     | Single       | References the underlying                         | If the field is invalid or not present,  |
|                      |                                                  |              |              | :ref:`single-csv-person` record.                  | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| post_election_status | :ref:`single-csv-candidate-post-election-status` | Optional     | Single       | Post-election outcome status from                 | If the field is invalid or not present,  |
|                      |                                                  |              |              | :ref:`single-csv-candidate-post-election-status`. | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| pre_election_status  | :ref:`single-csv-candidate-pre-election-status`  | Optional     | Single       | Pre-election qualification status from            | If the field is invalid or not present,  |
|                      |                                                  |              |              | :ref:`single-csv-candidate-pre-election-status`.  | then the implementation is required to   |
|                      |                                                  |              |              |                                                   | ignore it.                               |
+----------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,ballot_name,file_date,is_incumbent,is_top_ticket,party_id,person_id,post_election_status,pre_election_status
    can001,Jude Fawley,2024-03-01,true,false,par01,per50001,,qualified


.. _single-csv-candidate-contest:

candidate_contest
~~~~~~~~~~~~~~~~~

CandidateContest extends :ref:`single-csv-contest-base` and represents a contest among candidates.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumberElected/>``, ``<ClearOfficeIds/>``, ``<ClearPrimaryPartyIds/>``, ``<ClearVotesAllowed/>``).

+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+================+==============+==============+==========================================+==========================================+
| number_elected    | ``xs:integer`` | Optional     | Single       | Number of candidates elected in this     | If the field is invalid or not present,  |
|                   |                |              |              | contest (i.e. "N" of N-of-M). Clearable  | then the implementation is required to   |
|                   |                |              |              | in overlays.                             | ignore it.                               |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_ids        | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-csv-office`      | If the field is invalid or not present,  |
|                   |                |              |              | elements associated with the contest.    | then the implementation is required to   |
|                   |                |              |              | Clearable in overlays.                   | ignore it.                               |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| primary_party_ids | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-csv-party`       | If the field is invalid or not present,  |
|                   |                |              |              | elements if the contest is               | then the implementation is required to   |
|                   |                |              |              | party-specific. Clearable in overlays.   | ignore it.                               |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| votes_allowed     | ``xs:integer`` | Optional     | Single       | Maximum number of selections a voter may | If the field is invalid or not present,  |
|                   |                |              |              | make in this contest. Clearable in       | then the implementation is required to   |
|                   |                |              |              | overlays.                                | ignore it.                               |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,ballot_selection_ids,ballot_title,electoral_district_id,name,number_elected,office_ids,primary_party_ids,votes_allowed
    cc001,cs001 cs002,Governor of Virginia,ed001,Governor,1,off001,par01,1


.. _single-csv-contest-base:

contest_base
^^^^^^^^^^^^

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`, :ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`, and :ref:`single-csv-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                          |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | :ref:`single-csv-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | :ref:`single-csv-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                          |                                          |              |              | :ref:`single-csv-electoral-district`     | implementation is required to ignore the |
|                          |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                          |                                          |              |              | the contest. Required in main feed;      |                                          |
|                          |                                          |              |              | optional in overlays.                    |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | :ref:`single-csv-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                          |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                          |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                          |                                          |              |              | overlays.                                | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                          |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                          |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                          |                                          |              |              | :ref:`single-csv-vote-variation`.        | it.                                      |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                          |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                          |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-candidate-selection:

candidate_selection
~~~~~~~~~~~~~~~~~~~

CandidateSelection extends :ref:`single-csv-ballot-selection-base` and represents a ballot selection for one or more candidates in a candidate contest.

+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+================+==============+==============+==========================================+==========================================+
| candidate_ids         | ``xs:IDREFS``  | **Required** | Single       | References :ref:`single-csv-candidate`   | If CandidateIds is invalid or not        |
|                       |                |              |              | elements that comprise this selection    | present, the implementation is required  |
|                       |                |              |              | (e.g. candidate and running mate).       | to ignore the CandidateSelection         |
|                       |                |              |              |                                          | containing it.                           |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| endorsement_party_ids | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-csv-party`       | If the field is invalid or not present,  |
|                       |                |              |              | elements endorsing this candidate        | then the implementation is required to   |
|                       |                |              |              | selection.                               | ignore it.                               |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in           | ``xs:boolean`` | Optional     | Single       | Signifies whether this selection         | If the field is invalid or not present,  |
|                       |                |              |              | represents a write-in line.              | then the implementation is required to   |
|                       |                |              |              |                                          | ignore it.                               |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,sequence_order,candidate_ids,endorsement_party_ids,is_write_in
    cs001,1,can001,par01,false
    cs002,2,can002,par02,false


.. _single-csv-ballot-selection-base:

ballot_selection_base
^^^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-csv-ballot-measure-selection`,
:ref:`single-csv-candidate-selection`, and :ref:`single-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|                |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|                |                |              |              | is the default ordering, and can be      | ignore it.                               |
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
| algorithm    | :ref:`single-csv-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to | If the field is invalid, then the        |
|              |                                      |              |              | compute the checksum value.              | implementation is required to ignore the |
|              |                                      |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``                        | **Required** | Single       | The raw cryptographic checksum value     | If the field is invalid, then the        |
|              |                                      |              |              | encoded as a non-delimited, lowercase    | implementation is required to ignore the |
|              |                                      |              |              | hexadecimal string.                      | ``Checksum`` element containing it.      |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,algorithm,value
    ch1,sha-256,65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e


.. _single-csv-contact-information:

contact_information
~~~~~~~~~~~~~~~~~~~

Defines contact information (addresses, location identifiers, phone numbers, emails, schedules) for persons, election offices, voter services, or polling locations. ContactInformation has an optional attribute ``label``.

+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                | Required?    | Repeats?     | Description                                 | Error Handling                           |
+=====================+==========================================+==============+==============+=============================================+==========================================+
| mailing_address     | :ref:`single-csv-simple-address-type`    | Optional     | Repeats      | Structured mailing address for the contact. | If the element is invalid or not         |
|                     |                                          |              |              | Multiple addresses in different languages   | present, then the implementation is      |
|                     |                                          |              |              | can be specified.                           | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| physical_address    | :ref:`single-csv-simple-address-type`    | Optional     | Repeats      | Structured physical address for the         | If the element is invalid or not         |
|                     |                                          |              |              | contact. Multiple addresses in different    | present, then the implementation is      |
|                     |                                          |              |              | languages can be specified.                 | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| location_identifier | :ref:`single-csv-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus  | If the element is invalid or not         |
|                     |                                          |              |              | Code, coordinates).                         | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| directions          | :ref:`single-csv-internationalized-text` | Optional     | Single       | Directions for finding or reaching the      | If the element is invalid or not         |
|                     |                                          |              |              | contact location.                           | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| email               | :ref:`single-csv-internationalized-text` | Optional     | Repeats      | Email address(es) for the contact.          | If the element is invalid or not         |
|                     |                                          |              |              |                                             | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| fax                 | :ref:`single-csv-internationalized-text` | Optional     | Repeats      | Fax number(s) for the contact.              | If the element is invalid or not         |
|                     |                                          |              |              |                                             | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| hours               | :ref:`single-csv-internationalized-text` | Optional     | Single       | Operating hours as free-form text. *(NB:    | If the element is invalid or not         |
|                     |                                          |              |              | deprecated in favor of                      | present, then the implementation is      |
|                     |                                          |              |              | :ref:`single-csv-schedule-with-timezone`)*. | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| schedule            | :ref:`single-csv-schedule-with-timezone` | Optional     | Repeats      | Structured schedule with dates and          | If the element is invalid or not         |
|                     |                                          |              |              | operating hours.                            | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| lat_lng             | :ref:`single-csv-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.         | If the element is invalid or not         |
|                     |                                          |              |              |                                             | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| name                | :ref:`single-csv-internationalized-text` | Optional     | Single       | Person or place name associated with this   | If the element is invalid or not         |
|                     |                                          |              |              | contact information.                        | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| phone               | :ref:`single-csv-internationalized-text` | Optional     | Repeats      | Telephone number(s) for the contact.        | If the element is invalid or not         |
|                     |                                          |              |              |                                             | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| uri                 | :ref:`single-csv-internationalized-uri`  | Optional     | Repeats      | Web address(es) for the contact.            | If the element is invalid or not         |
|                     |                                          |              |              |                                             | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    label,directions,email,fax,hours,name,phone,uri
    ci001,Use entrance on Main St,info@example.gov,,08:00-17:00,Elections Office,555-0100,https://example.gov


.. _single-csv-contest-base:

contest_base
~~~~~~~~~~~~

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`, :ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`, and :ref:`single-csv-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                          |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | :ref:`single-csv-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | :ref:`single-csv-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                          |                                          |              |              | :ref:`single-csv-electoral-district`     | implementation is required to ignore the |
|                          |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                          |                                          |              |              | the contest. Required in main feed;      |                                          |
|                          |                                          |              |              | optional in overlays.                    |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | :ref:`single-csv-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                          |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                          |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                          |                                          |              |              | overlays.                                | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                          |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                          |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                          |                                          |              |              | :ref:`single-csv-vote-variation`.        | it.                                      |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                          |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                          |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-election:

election
~~~~~~~~

The Election object represents an election event. A feed must contain **exactly one** Election object in the main feed. In feed overlays, Election can appear to update election metadata.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearAbsenteeBallotInfo/>``). Fields that are required in the main feed (Date and TopLevelLocalityId) are optional in overlays.

+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                           | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============================+==========================================+==============+==============+==========================================+==========================================+
| absentee_ballot_info          | :ref:`single-csv-internationalized-text` | Optional     | Single       | Information about requesting absentee    | If the element is invalid or not         |
|                               |                                          |              |              | ballots.                                 | present, then the implementation is      |
|                               |                                          |              |              |                                          | required to ignore it.                   |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_request_deadline     | ``xs:date``                              | Optional     | Single       | Last day to request an absentee ballot.  | If the field is invalid or not present,  |
|                               |                                          |              |              |                                          | then the implementation is required to   |
|                               |                                          |              |              |                                          | ignore it.                               |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date                          | ``xs:date``                              | **Required** | Single       | Date of the election in local time.      | If the field is invalid, then the        |
|                               |                                          |              |              | Required in main feed; optional in       | implementation is required to ignore the |
|                               |                                          |              |              | overlays.                                | ``Election`` element containing it.      |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_type                 | :ref:`single-csv-internationalized-text` | Optional     | Single       | Type of election (e.g. General, Primary, | If the element is invalid or not         |
|                               |                                          |              |              | Special).                                | present, then the implementation is      |
|                               |                                          |              |              |                                          | required to ignore it.                   |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_election_day_registration | ``xs:boolean``                           | Optional     | Single       | Specifies whether voters can register on | If the field is invalid or not present,  |
|                               |                                          |              |              | election day.                            | then the implementation is required to   |
|                               |                                          |              |              |                                          | ignore it.                               |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| schedule                      | :ref:`single-csv-schedule-with-timezone` | Optional     | Repeats      | Schedule of voting dates and hours for   | If the element is invalid or not         |
|                               |                                          |              |              | the election.                            | present, then the implementation is      |
|                               |                                          |              |              |                                          | required to ignore it.                   |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_statewide                  | ``xs:boolean``                           | Optional     | Single       | Indicates whether the election is        | If the field is invalid or not present,  |
|                               |                                          |              |              | statewide.                               | then the implementation is required to   |
|                               |                                          |              |              |                                          | ignore it.                               |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                          | :ref:`single-csv-internationalized-text` | Optional     | Single       | The name of the election.                | If the element is invalid or not         |
|                               |                                          |              |              |                                          | present, then the implementation is      |
|                               |                                          |              |              |                                          | required to ignore it.                   |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_deadline         | ``xs:date``                              | Optional     | Single       | Last day to register to vote for the     | If the field is invalid or not present,  |
|                               |                                          |              |              | election.                                | then the implementation is required to   |
|                               |                                          |              |              |                                          | ignore it.                               |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_info             | :ref:`single-csv-internationalized-text` | Optional     | Single       | Information about voter registration.    | If the element is invalid or not         |
|                               |                                          |              |              |                                          | present, then the implementation is      |
|                               |                                          |              |              |                                          | required to ignore it.                   |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| results_uri                   | :ref:`single-csv-internationalized-uri`  | Optional     | Single       | Web address where election results may   | If the element is invalid or not         |
|                               |                                          |              |              | be found.                                | present, then the implementation is      |
|                               |                                          |              |              |                                          | required to ignore it.                   |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| top_level_locality_id         | ``xs:IDREF``                             | **Required** | Single       | Links to the top-level                   | If the field is invalid or not present,  |
|                               |                                          |              |              | :ref:`single-csv-locality` for the       | the implementation is required to ignore |
|                               |                                          |              |              | election (e.g. the state locality).      | the Election containing it.              |
|                               |                                          |              |              | Required in main feed; optional in       |                                          |
|                               |                                          |              |              | overlays.                                |                                          |
+-------------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,date,name,election_type,top_level_locality_id,is_statewide,registration_info,absentee_ballot_info,results_uri,has_election_day_registration,registration_deadline,absentee_request_deadline
    ele001,2024-11-05,2024 General Election,General,loc51,true,https://vote.va.gov/register,https://vote.va.gov/absentee,https://vote.va.gov/results,false,2024-10-15,2024-10-25


.. _single-csv-election-administration:

election_administration
~~~~~~~~~~~~~~~~~~~~~~~

The ElectionAdministration element represents an administrative body serving a locality's election functions. In VIP 7.0, ElectionAdministration is embedded directly by value inside a :ref:`single-csv-locality` element rather than referenced by an ID.

In overlay feeds, the entire ElectionAdministration element is replaced as a single unit on the locality, or cleared using ``<ClearElectionAdministration/>``.

+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                             | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================================+=========================================+==============+==============+==========================================+==========================================+
| absentee_uri                    | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for absentee voting          | If the element is invalid or not         |
|                                 |                                         |              |              | information.                             | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| am_i_registered_uri             | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for voter registration       | If the element is invalid or not         |
|                                 |                                         |              |              | status verification.                     | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_tracking_uri             | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for tracking mail-in         | If the element is invalid or not         |
|                                 |                                         |              |              | ballots.                                 | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_tracking_provisional_uri | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for provisional ballot       | If the element is invalid or not         |
|                                 |                                         |              |              | tracking.                                | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| contact_information             | :ref:`single-csv-contact-information`   | Optional     | Single       | Primary contact information for the      | If the element is invalid or not         |
|                                 |                                         |              |              | election administration.                 | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| elections_uri                   | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Primary web address for the election     | If the element is invalid or not         |
|                                 |                                         |              |              | administration.                          | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_uri                | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for voter registration.      | If the element is invalid or not         |
|                                 |                                         |              |              |                                          | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| rules_uri                       | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for election rules,          | If the element is invalid or not         |
|                                 |                                         |              |              | regulations, and statutes.               | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| voter_service                   | :ref:`single-csv-voter-service`         | Optional     | Repeats      | Specific voter services provided by the  | If the element is invalid or not         |
|                                 |                                         |              |              | administration (e.g. voter registration, | present, then the implementation is      |
|                                 |                                         |              |              | overseas voting).                        | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| what_is_on_my_ballot_uri        | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address where voters can see sample  | If the element is invalid or not         |
|                                 |                                         |              |              | ballots.                                 | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| where_do_i_vote_uri             | :ref:`single-csv-internationalized-uri` | Optional     | Single       | Web address for official polling place   | If the element is invalid or not         |
|                                 |                                         |              |              | lookup.                                  | present, then the implementation is      |
|                                 |                                         |              |              |                                          | required to ignore it.                   |
+---------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    absentee_uri,am_i_registered_uri,ballot_tracking_uri,ballot_tracking_provisional_uri,elections_uri,registration_uri,rules_uri,what_is_on_my_ballot_uri,where_do_i_vote_uri
    https://example.com/absentee,https://example.com/registered,https://vote.virginia.gov/track,https://vote.virginia.gov/provisional,https://example.com/elections,https://example.com/register,https://example.com/rules,https://example.com/ballot,https://example.com/poll


.. _single-csv-electoral-district:

electoral_district
~~~~~~~~~~~~~~~~~~

An ElectoralDistrict represents a geographic boundary or jurisdiction for representation, contests, and offices.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumber/>``, ``<ClearExternalIdentifier/>``). Name and Type are optional in overlays.

+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==========================================+==============+==============+==========================================+==========================================+
| external_identifier | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                          |              |              | district to other datasets (e.g.         | present, then the implementation is      |
|                     |                                          |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                | :ref:`single-csv-internationalized-text` | **Required** | Single       | Name of the district. Required in main   | If the element is invalid, then the      |
|                     |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                     |                                          |              |              |                                          | ``ElectoralDistrict`` element containing |
|                     |                                          |              |              |                                          | it.                                      |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number              | ``xs:integer``                           | Optional     | Single       | Number of the district (e.g. "57").      | If the field is invalid or not present,  |
|                     |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                | :ref:`single-csv-district-type`          | **Required** | Single       | Type of district from                    | If the field is invalid, then the        |
|                     |                                          |              |              | :ref:`single-csv-district-type`.         | implementation is required to ignore the |
|                     |                                          |              |              | Required in main feed; optional in       | ``ElectoralDistrict`` element containing |
|                     |                                          |              |              | overlays.                                | it.                                      |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type          | ``xs:string``                            | Optional     | Single       | Custom district type if Type is "other". | If the field is invalid or not present,  |
|                     |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,name,number,type,other_type
    ed60129,57th House of Delegates District,57,state-house,


.. _single-csv-external-file:

external_file
~~~~~~~~~~~~~

The ``ExternalFile`` object holds a reference to a file external to the feed itself, such as a shapefile archive. External files are packaged along with the VIP feed into a single archive.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| file_uri     | ``xs:anyURI`` | **Required** | Single       | The URI or filename of the external      | If the field is invalid, then the        |
|              |               |              |              | file.                                    | implementation is required to ignore the |
|              |               |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| checksum_id  | ``xs:IDREF``  | **Required** | Single       | The cryptographic checksum of the        | If the element is invalid, then the      |
|              |               |              |              | external file.                           | implementation is required to ignore the |
|              |               |              |              |                                          | ``ExternalFile`` element containing it.  |
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
| external_file_id   | ``xs:IDREF``                         | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                    |                                      |              |              | :ref:`single-csv-external-file`          | implementation is required to ignore the |
|                    |                                      |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                    |                                      |              |              | define the feature's boundary.           | containing it.                           |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_format        | :ref:`single-csv-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                    |                                      |              |              |                                          | implementation is required to ignore the |
|                    |                                      |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                    |                                      |              |              |                                          | containing it.                           |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feature_identifier | :ref:`single-csv-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    | If the element is invalid, then the      |
|                    |                                      |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                    |                                      |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                    |                                      |              |              | the referenced external file. This is a  | containing it.                           |
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

Specifies an external identifier for an entity, linking it to another dataset or system. ExternalIdentifier has optional attributes ``label`` and ``provider``.

In overlay feeds, this element is clearable using ``<ClearExternalIdentifier/>`` on elements where it is marked clearable.

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| type         | :ref:`single-csv-identifier-type` | **Required** | Single       | Specifies the type of identifier from    | If the field is invalid or not present,  |
|              |                                   |              |              | :ref:`single-csv-identifier-type`.       | the implementation is required to ignore |
|              |                                   |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                   |              |              |                                          | it.                                      |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``                     | Optional     | Single       | Allows defining an identifier type       | If the field is invalid or not present,  |
|              |                                   |              |              | outside                                  | then the implementation is required to   |
|              |                                   |              |              | :ref:`single-csv-identifier-type`. Type  | ignore it.                               |
|              |                                   |              |              | should be set to "other" when using this |                                          |
|              |                                   |              |              | field.                                   |                                          |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``                     | **Required** | Single       | Specifies the identifier value.          | If the field is invalid or not present,  |
|              |                                   |              |              |                                          | the implementation is required to ignore |
|              |                                   |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                   |              |              |                                          | it.                                      |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-feature-identifier:

feature_identifier
~~~~~~~~~~~~~~~~~~

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| index        | ``xs:string`` | **Required** | Single       | The index value for the shapefile        | If the Index field is invalid or not     |
|              |               |              |              | feature.                                 | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the FeatureIdentifier          |
|              |               |              |              |                                          | containing it.                           |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


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
| latitude      | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|               |               |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|               |               |              |              | example, this could be the name of a     | ignore it.                               |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-locality:

locality
~~~~~~~~

The Locality object represents any jurisdictional level—including states, counties, cities, and towns. Localities form a tree hierarchy using ``ParentLocalityId``, with the root locality representing the state (with ``Type="state"``).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearDefaultPollingHours/>``, ``<ClearElectionAdministration/>``, ``<ClearIsInactive/>``). Name is optional in overlays. Emergency notices and overridden hours are only permitted in overlays.

+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+===========================================+==============+==============+==========================================+==========================================+
| election_administration     | :ref:`single-csv-election-administration` | Optional     | Single       | The election administration entity for   | If the element is invalid or not         |
|                             |                                           |              |              | this locality. In overlays, this entity  | present, then the implementation is      |
|                             |                                           |              |              | is replaced as a single unit or cleared  | required to ignore it.                   |
|                             |                                           |              |              | with <ClearElectionAdministration/>.     |                                          |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier         | :ref:`single-csv-external-identifier`     | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                             |                                           |              |              | locality to external datasets (e.g.      | present, then the implementation is      |
|                             |                                           |              |              | OCD-ID, FIPS). Clearable in overlays.    | required to ignore it.                   |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only                | ``xs:boolean``                            | Optional     | Single       | Specifies if the locality runs mail-only | If the field is missing or invalid, the  |
|                             |                                           |              |              | elections. Clearable in overlays.        | implementation is required to assume     |
|                             |                                           |              |              |                                          | IsMailOnly is false.                     |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                        | ``xs:string``                             | **Required** | Single       | Name of the locality. Required in main   | If the field is invalid, then the        |
|                             |                                           |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                             |                                           |              |              |                                          | ``Locality`` element containing it.      |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids        | ``xs:IDREFS``                             | Optional     | Single       | References locality-wide polling         | If the field is invalid or not present,  |
|                             |                                           |              |              | locations (e.g. early vote sites or drop | then the implementation is required to   |
|                             |                                           |              |              | boxes). Clearable in overlays.           | ignore it.                               |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| parent_locality_id          | ``xs:IDREF``                              | Optional     | Single       | References the parent                    | If the field is invalid or not present,  |
|                             |                                           |              |              | :ref:`single-csv-locality` in the        | then the implementation is required to   |
|                             |                                           |              |              | jurisdiction hierarchy (e.g. county      | ignore it.                               |
|                             |                                           |              |              | pointing to state). If omitted, this is  |                                          |
|                             |                                           |              |              | a top-level jurisdiction.                |                                          |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                        | :ref:`single-csv-district-type`           | Optional     | Single       | The kind of jurisdiction (e.g. state,    | If the field is invalid or not present,  |
|                             |                                           |              |              | county, city) from                       | then the implementation is required to   |
|                             |                                           |              |              | :ref:`single-csv-district-type`.         | ignore it.                               |
|                             |                                           |              |              | Clearable in overlays.                   |                                          |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                  | ``xs:string``                             | Optional     | Single       | Allows defining a type of locality       | If the field is invalid or not present,  |
|                             |                                           |              |              | outside :ref:`single-csv-district-type`. | then the implementation is required to   |
|                             |                                           |              |              | Clearable in overlays.                   | ignore it.                               |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| default_polling_hours       | :ref:`single-csv-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for day-of       | If the element is invalid or not         |
|                             |                                           |              |              | polling locations throughout this        | present, then the implementation is      |
|                             |                                           |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| default_early_vote_hours    | :ref:`single-csv-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for in-person    | If the element is invalid or not         |
|                             |                                           |              |              | early voting locations throughout this   | present, then the implementation is      |
|                             |                                           |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| default_dropoff_hours       | :ref:`single-csv-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for ballot       | If the element is invalid or not         |
|                             |                                           |              |              | drop-off locations throughout this       | present, then the implementation is      |
|                             |                                           |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive                 | ``xs:string``                             | Optional     | Single       | If specified, marks the locality as      | If the field is invalid or not present,  |
|                             |                                           |              |              | inactive and explains the reason why.    | then the implementation is required to   |
|                             |                                           |              |              | Clearable in overlays.                   | ignore it.                               |
+-----------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,name,parent_locality_id,type,other_type,is_mail_only,polling_location_ids
    loc51,Virginia,,state,,false,
    loc70001,Albemarle County,loc51,county,,false,pl001 pl002


.. _single-csv-location-identifier:

location_identifier
~~~~~~~~~~~~~~~~~~~

Specifies an external identifier for a physical location (e.g. a polling location or contact address), such as a latitude/longitude pair, Plus Code, or geocoder ID. LocationIdentifier has optional attributes ``label``, ``provider`` (e.g. "Google"), and ``relativePriority`` (a decimal number indicating the relative preference of this identifier when multiple identifiers are provided).

In overlay feeds, this element is clearable using ``<ClearLocationIdentifier/>``.

+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag          | Data Type                                  | Required?    | Repeats?     | Description                                 | Error Handling                           |
+==============+============================================+==============+==============+=============================================+==========================================+
| type         | :ref:`single-csv-location-identifier-type` | **Required** | Single       | Specifies the type of location identifier   | If the field is invalid or not present,  |
|              |                                            |              |              | from                                        | the implementation is required to ignore |
|              |                                            |              |              | :ref:`single-csv-location-identifier-type`. | the ``LocationIdentifier`` containing    |
|              |                                            |              |              |                                             | it.                                      |
+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``                              | Optional     | Single       | Specifies the type of identifier if         | If the field is invalid or not present,  |
|              |                                            |              |              | ``Type`` is set to "other".                 | then the implementation is required to   |
|              |                                            |              |              |                                             | ignore it.                               |
+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| value        | ``xs:string``                              | **Required** | Single       | Specifies the identifier value (e.g. Plus   | If the field is invalid or not present,  |
|              |                                            |              |              | Code, coordinates, Place ID).               | the implementation is required to ignore |
|              |                                            |              |              |                                             | the ``LocationIdentifier`` containing    |
|              |                                            |              |              |                                             | it.                                      |
+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+


.. _single-csv-office:

office
~~~~~~

``Office`` represents an elected or appointed government office associated with an electoral district (e.g. Mayor, Governor, School Board).

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| contact_information      | :ref:`single-csv-contact-information`    | Optional     | Repeats      | Contact information for the office.      | If the element is invalid or not         |
|                          |                                          |              |              |                                          | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description              | :ref:`single-csv-internationalized-text` | Optional     | Single       | Brief description of the office and its  | If the element is invalid or not         |
|                          |                                          |              |              | responsibilities.                        | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                             | **Required** | Single       | Links to the                             | If ElectoralDistrictId is invalid or not |
|                          |                                          |              |              | :ref:`single-csv-electoral-district`     | present, the implementation is required  |
|                          |                                          |              |              | representing the geographical scope of   | to ignore the Office containing it.      |
|                          |                                          |              |              | the office.                              |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                          |              |              | office to external systems (e.g.         | present, then the implementation is      |
|                          |                                          |              |              | OCD-ID).                                 | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| filing_deadline          | ``xs:date``                              | Optional     | Single       | Filing deadline date for candidates      | If the field is invalid or not present,  |
|                          |                                          |              |              | running for this office.                 | then the implementation is required to   |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_partisan              | ``xs:boolean``                           | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                          |                                          |              |              | partisan.                                | then the implementation is required to   |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | :ref:`single-csv-internationalized-text` | **Required** | Single       | Official name of the office.             | If Name is invalid or not present, the   |
|                          |                                          |              |              |                                          | implementation is required to ignore the |
|                          |                                          |              |              |                                          | Office containing it.                    |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_holder_person_ids | ``xs:IDREFS``                            | Optional     | Single       | References to :ref:`single-csv-person`   | If the field is invalid or not present,  |
|                          |                                          |              |              | elements for the current office          | then the implementation is required to   |
|                          |                                          |              |              | holder(s).                               | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term                     | :ref:`single-csv-term`                   | Optional     | Single       | Defines the term length and dates of the | If the element is invalid or not         |
|                          |                                          |              |              | office.                                  | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,electoral_district_id,filing_deadline,is_partisan,name,office_holder_person_ids,term_type,term_start_date,term_end_date
    off001,ed001,2024-06-01,true,Governor,per50001,full-term,2022-01-15,2026-01-15


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
| contest_id                   | ``xs:IDREF`` | **Required** | Single       | Links to elements that extend            | If the field is invalid or not present, the      |
|                              |              |              |              | :ref:`single-csv-contest-base`.          | implementation is required to ignore the         |
|                              |              |              |              |                                          | ``OrderedContest`` element containing it.        |
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

The Party object represents a political party or ballot grouping.

+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==========================================+==============+==============+==========================================+==========================================+
| abbreviation        | ``xs:string``                            | Optional     | Single       | Abbreviation for the party name (e.g.    | If the field is invalid or not present,  |
|                     |                                          |              |              | "DEM", "REP").                           | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| color               | :ref:`single-csv-html-color-string`      | Optional     | Single       | Six-digit hexadecimal HTML color code    | If the element is invalid or not         |
|                     |                                          |              |              | associated with the party.               | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                          |              |              | party to other datasets.                 | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in         | ``xs:boolean``                           | Optional     | Single       | Indicates if the party represents        | If the field is invalid or not present,  |
|                     |                                          |              |              | write-in selections.                     | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| leader_person_ids   | ``xs:IDREFS``                            | Optional     | Single       | References to :ref:`single-csv-person`   | If the field is invalid or not present,  |
|                     |                                          |              |              | elements for party leadership.           | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| logo_uri            | :ref:`single-csv-internationalized-uri`  | Optional     | Single       | URI pointing to the party logo.          | If the element is invalid or not         |
|                     |                                          |              |              |                                          | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                | :ref:`single-csv-internationalized-text` | **Required** | Single       | Official name of the party.              | If the element is invalid, then the      |
|                     |                                          |              |              |                                          | implementation is required to ignore the |
|                     |                                          |              |              |                                          | ``Party`` element containing it.         |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,abbreviation,color,is_write_in,leader_person_ids,logo_uri,name
    par0001,DEM,0000FF,false,per50001,https://example.gov/dem.png,Democratic Party
    par0002,REP,FF0000,false,per50002,https://example.gov/rep.png,Republican Party


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

A base model for all Contest types: :ref:`single-csv-ballot-measure-contest`, :ref:`single-csv-candidate-contest`, :ref:`single-csv-party-contest`, and :ref:`single-csv-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                          |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | :ref:`single-csv-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | :ref:`single-csv-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                          |                                          |              |              | :ref:`single-csv-electoral-district`     | implementation is required to ignore the |
|                          |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                          |                                          |              |              | the contest. Required in main feed;      |                                          |
|                          |                                          |              |              | optional in overlays.                    |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | :ref:`single-csv-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                          |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                          |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                          |                                          |              |              | overlays.                                | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                          |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                          |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`single-csv-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                          |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                          |                                          |              |              | :ref:`single-csv-vote-variation`.        | it.                                      |
|                          |                                          |              |              | Clearable in overlays.                   |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                          |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                          |                                          |              |              |                                          | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                          |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                          |                                          |              |              | in overlays.                             | it.                                      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


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
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|                |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|                |                |              |              | is the default ordering, and can be      | ignore it.                               |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`single-csv-ordered-contest`.    |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-person:

person
~~~~~~

The Person object represents an individual (such as a candidate, election official, or party leader).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearContactInformation/>``, ``<ClearPartyId/>``, ``<ClearProfession/>``).

+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==========================================+==============+==============+==========================================+==========================================+
| contact_information | :ref:`single-csv-contact-information`    | Optional     | Repeats      | Contact information for the person.      | If the element is invalid or not         |
|                     |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_of_birth       | ``xs:date``                              | Optional     | Single       | Date of birth of the person. Clearable   | If the field is invalid or not present,  |
|                     |                                          |              |              | in overlays.                             | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier | :ref:`single-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                          |              |              | person to external systems. Clearable in | present, then the implementation is      |
|                     |                                          |              |              | overlays.                                | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| first_name          | ``xs:string``                            | Optional     | Single       | First name of the person. Clearable in   | If the field is invalid or not present,  |
|                     |                                          |              |              | overlays.                                | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_name           | :ref:`single-csv-internationalized-text` | Optional     | Single       | Full legal or preferred name of the      | If the element is invalid or not         |
|                     |                                          |              |              | person. Clearable in overlays.           | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| gender              | ``xs:string``                            | Optional     | Single       | Gender of the person. Clearable in       | If the field is invalid or not present,  |
|                     |                                          |              |              | overlays.                                | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| last_name           | ``xs:string``                            | Optional     | Single       | Last name of the person. Clearable in    | If the field is invalid or not present,  |
|                     |                                          |              |              | overlays.                                | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| middle_name         | ``xs:string``                            | Optional     | Repeats      | Middle name(s) of the person. Clearable  | If the field is invalid or not present,  |
|                     |                                          |              |              | in overlays.                             | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| nickname            | ``xs:string``                            | Optional     | Single       | Nickname or informal name. Clearable in  | If the field is invalid or not present,  |
|                     |                                          |              |              | overlays.                                | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id            | ``xs:IDREF``                             | Optional     | Single       | References the :ref:`single-csv-party`   | If the field is invalid or not present,  |
|                     |                                          |              |              | to which the person belongs. Clearable   | then the implementation is required to   |
|                     |                                          |              |              | in overlays.                             | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| prefix              | ``xs:string``                            | Optional     | Single       | Name prefix (e.g. "Dr.", "Rev.").        | If the field is invalid or not present,  |
|                     |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| profession          | :ref:`single-csv-internationalized-text` | Optional     | Single       | Occupation or profession of the person.  | If the element is invalid or not         |
|                     |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| suffix              | ``xs:string``                            | Optional     | Single       | Name suffix (e.g. "Jr.", "III", "Esq."). | If the field is invalid or not present,  |
|                     |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                          |              |              |                                          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| title               | :ref:`single-csv-internationalized-text` | Optional     | Single       | Official title held by the person.       | If the element is invalid or not         |
|                     |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                     |                                          |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,first_name,last_name,middle_name,nickname,prefix,suffix,title,profession,party_id,date_of_birth,gender
    per50001,Ken,Cuccinelli,T.,,II,,Attorney General,Attorney,par0001,1968-07-30,male


.. _single-csv-polling-location:

polling_location
~~~~~~~~~~~~~~~~

The PollingLocation object represents a site where voters cast ballots in person or drop off early/absentee ballots. In VIP 7.0, facility names are placed in ``AddressStructured.LocationName``.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearDirections/>``, ``<ClearPhotoUri/>``, ``<ClearIsInactive/>``). AddressStructured and LocationType are optional in overlays.
EmergencyNotice is permitted only in overlays.
In overlays, PollingLocation has an optional attribute ``isNew="true"`` to indicate that a polling location is newly added rather than modifying an existing one.

+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                | Required?    | Repeats?     | Description                                 | Error Handling                           |
+=====================+==========================================+==============+==============+=============================================+==========================================+
| address_structured  | :ref:`single-csv-simple-address-type`    | **Required** | Repeats      | Structured address including facility name. | AddressStructured is required for        |
|                     |                                          |              |              | Required in main feed; optional in          | PollingLocation in main feeds.           |
|                     |                                          |              |              | overlays. Multiple addresses in different   |                                          |
|                     |                                          |              |              | languages can be specified.                 |                                          |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| location_identifier | :ref:`single-csv-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus  | If the element is invalid or not         |
|                     |                                          |              |              | Code, geocoder ID). Clearable in overlays.  | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| directions          | :ref:`single-csv-internationalized-text` | Optional     | Single       | Instructions for locating the polling site  | If the element is invalid or not         |
|                     |                                          |              |              | or room. Clearable in overlays.             | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| hours               | :ref:`single-csv-internationalized-text` | Optional     | Single       | Operating hours as text. Clearable in       | If the element is invalid or not         |
|                     |                                          |              |              | overlays. *(NB: deprecated in favor of      | present, then the implementation is      |
|                     |                                          |              |              | :ref:`single-csv-schedule-with-timezone`)*. | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| schedule            | :ref:`single-csv-schedule-with-timezone` | Optional     | Repeats      | Structured schedule of operating dates and  | If the element is invalid or not         |
|                     |                                          |              |              | hours. Clearable in overlays.               | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| location_type       | :ref:`single-csv-polling-location-type`  | **Required** | Single       | The type of voting conducted at this        | LocationType is required for             |
|                     |                                          |              |              | location (InPersonDayOf, InPersonEarly, or  | PollingLocation in main feeds.           |
|                     |                                          |              |              | DropOff). Required in main feed; optional   |                                          |
|                     |                                          |              |              | in overlays.                                |                                          |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| lat_lng             | :ref:`single-csv-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.         | If the element is invalid or not         |
|                     |                                          |              |              | Clearable in overlays.                      | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| party_ids           | ``xs:IDREFS``                            | Optional     | Single       | If present, indicates which parties'        | If the field is invalid or not present,  |
|                     |                                          |              |              | primaries occur at this location. Clearable | then the implementation is required to   |
|                     |                                          |              |              | in overlays.                                | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| photo_uri           | :ref:`single-csv-internationalized-uri`  | Optional     | Single       | Link to a photo of the location. Clearable  | If the element is invalid or not         |
|                     |                                          |              |              | in overlays.                                | present, then the implementation is      |
|                     |                                          |              |              |                                             | required to ignore it.                   |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| is_inactive         | ``xs:string``                            | Optional     | Single       | If specified, marks the location as closed  | If the field is invalid or not present,  |
|                     |                                          |              |              | or inactive, with the text stating the      | then the implementation is required to   |
|                     |                                          |              |              | reason why. Clearable in overlays.          | ignore it.                               |
+---------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,location_type,directions,photo_uri,party_ids,is_inactive
    poll001,InPersonDayOf,Use gymnasium entrance,https://example.gov/poll.jpg,,
    poll002,DropOff,Curbside ballot drop box,,,Water main break


.. _single-csv-precinct:

precinct
~~~~~~~~

The Precinct object represents a voting precinct or precinct split within a Locality.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearBallotStyleId/>``, ``<ClearPollingLocationIds/>``, ``<ClearIsInactive/>``). LocalityId and Name are optional in overlays. EmergencyNotice is permitted only in overlays.

+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=======================================+==============+==============+==========================================+==========================================+
| ballot_style_id        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                        |                                       |              |              | :ref:`single-csv-ballot-style` voted by  | then the implementation is required to   |
|                        |                                       |              |              | electors in this precinct. Clearable in  | ignore it.                               |
|                        |                                       |              |              | overlays.                                |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_ids | ``xs:IDREFS``                         | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                        |                                       |              |              | :ref:`single-csv-electoral-district`     | then the implementation is required to   |
|                        |                                       |              |              | elements containing this precinct.       | ignore it.                               |
|                        |                                       |              |              | Clearable in overlays.                   |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier    | :ref:`single-csv-external-identifier` | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                        |                                       |              |              | precinct to other datasets (e.g.         | present, then the implementation is      |
|                        |                                       |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only           | ``xs:boolean``                        | Optional     | Single       | Specifies if this precinct conducts      | If the field is missing or invalid, the  |
|                        |                                       |              |              | mail-only elections. Clearable in        | implementation is required to assume     |
|                        |                                       |              |              | overlays.                                | IsMailOnly is false.                     |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| locality_id            | ``xs:IDREF``                          | **Required** | Single       | References the containing                | If LocalityId is invalid or not present, |
|                        |                                       |              |              | :ref:`single-csv-locality`. Required in  | the implementation is required to ignore |
|                        |                                       |              |              | main feed; optional in overlays.         | the Precinct containing it.              |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                   | ``xs:string``                         | **Required** | Single       | Name of the precinct. Required in main   | If Name is invalid or not present, the   |
|                        |                                       |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                        |                                       |              |              |                                          | Precinct containing it.                  |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number                 | ``xs:string``                         | Optional     | Single       | Precinct number or code. Clearable in    | If the field is invalid or not present,  |
|                        |                                       |              |              | overlays.                                | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids   | ``xs:IDREFS``                         | Optional     | Single       | Links to polling locations serving this  | If the field is invalid or not present,  |
|                        |                                       |              |              | precinct. Clearable in overlays.         | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_split_name    | ``xs:string``                         | Optional     | Single       | Sub-identifier for precinct splits.      | If the field is invalid or not present,  |
|                        |                                       |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| spatial_boundary       | :ref:`single-csv-spatial-boundary`    | Optional     | Single       | Geospatial boundary defining the         | If the element is invalid or not         |
|                        |                                       |              |              | precinct polygon. Clearable in overlays. | present, then the implementation is      |
|                        |                                       |              |              |                                          | required to ignore it.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ward                   | ``xs:string``                         | Optional     | Single       | Ward identifier if applicable. Clearable | If the field is invalid or not present,  |
|                        |                                       |              |              | in overlays.                             | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive            | ``xs:string``                         | Optional     | Single       | If specified, marks the precinct as      | If the field is invalid or not present,  |
|                        |                                       |              |              | inactive, stating the reason why.        | then the implementation is required to   |
|                        |                                       |              |              | Clearable in overlays.                   | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,ballot_style_id,electoral_district_ids,is_mail_only,locality_id,name,number,polling_location_ids,precinct_split_name,ward
    pre90111,bs00010,ed001 ed002,false,loc70001,203 - GEORGETOWN,0203,pl00001,split13,5


.. _single-csv-retention-contest:

retention_contest
~~~~~~~~~~~~~~~~~

``RetentionContest`` extends :ref:`single-csv-ballot-measure-contest` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| candidate_id | ``xs:IDREF`` | **Required** | Single       | Links to the :ref:`single-csv-candidate` | If the field is invalid or not present,  |
|              |              |              |              | being retained.                          | the implementation is required to ignore |
|              |              |              |              |                                          | the ``RetentionContest`` element         |
|              |              |              |              |                                          | containing it.                           |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_id    | ``xs:IDREF`` | Optional     | Single       | Links to the information about the       | If the field is invalid or not present,  |
|              |              |              |              | office.                                  | then the implementation is required to   |
|              |              |              |              |                                          | ignore it.                               |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-schedule-with-timezone:

schedule_with_timezone
~~~~~~~~~~~~~~~~~~~~~~

Defines a schedule of dates and hours of operation with an optional IANA time zone. If the time zone is omitted, hours are assumed to be in the local time of the enclosing entity. ScheduleWithTimezone has an optional ``label`` attribute.

In overlay feeds, elements of type ScheduleWithTimezone are clearable using ``<ClearSchedule/>`` (or ``<ClearDefaultPollingHours/>``, etc. depending on the tag name).

+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type               | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=========================+==============+==============+==========================================+==========================================+
| time_zone              | ``xs:string``           | Optional     | Single       | The named IANA time zone (e.g.           | If the field is invalid or not present,  |
|                        |                         |              |              | "America/New_York", "Etc/UTC",           | then the implementation is required to   |
|                        |                         |              |              | "Etc/GMT+1"). Must match canonical       | ignore it.                               |
|                        |                         |              |              | Continent/City format. If not present,   |                                          |
|                        |                         |              |              | hours are assumed to be in local time.   |                                          |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_date             | ``xs:date``             | Optional     | Single       | The date on which this schedule begins.  | If the field is invalid or not present,  |
|                        |                         |              |              |                                          | then the implementation is required to   |
|                        |                         |              |              |                                          | ignore it.                               |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_date               | ``xs:date``             | Optional     | Single       | The date on which this schedule ends.    | If the field is invalid or not present,  |
|                        |                         |              |              |                                          | then the implementation is required to   |
|                        |                         |              |              |                                          | ignore it.                               |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours                  | :ref:`single-csv-hours` | Optional     | Repeats      | Blocks of hours during which the         | If the element is invalid or not         |
|                        |                         |              |              | location is open on days in the date     | present, then the implementation is      |
|                        |                         |              |              | range.                                   | required to ignore it.                   |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_open_24_hours       | ``xs:boolean``          | Optional     | Single       | Indicates if the location is open 24     | If the field is invalid or not present,  |
|                        |                         |              |              | hours a day during this date range (e.g. | then the implementation is required to   |
|                        |                         |              |              | 24-hour ballot drop boxes).              | ignore it.                               |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_only_by_appointment | ``xs:boolean``          | Optional     | Single       | If true, the location is only open       | If the field is invalid or not present,  |
|                        |                         |              |              | during the specified window with an      | then the implementation is required to   |
|                        |                         |              |              | appointment.                             | ignore it.                               |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_or_by_appointment   | ``xs:boolean``          | Optional     | Single       | If true, the location is open during the | If the field is invalid or not present,  |
|                        |                         |              |              | window and may also be open by           | then the implementation is required to   |
|                        |                         |              |              | appointment.                             | ignore it.                               |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_subject_to_change   | ``xs:boolean``          | Optional     | Single       | If true, hours may be subject to change. | If the field is invalid or not present,  |
|                        |                         |              |              | Voters should verify prior to arrival.   | then the implementation is required to   |
|                        |                         |              |              |                                          | ignore it.                               |
+------------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,time_zone,start_date,end_date,is_open_24_hours,is_only_by_appointment,is_or_by_appointment,is_subject_to_change
    sch001,America/New_York,2024-10-10,2024-10-12,false,false,true,false
    sch002,America/New_York,2024-10-13,2024-10-15,false,true,false,false


.. _single-csv-simple-address-type:

simple_address_type
~~~~~~~~~~~~~~~~~~~

A ``SimpleAddressType`` represents a structured physical or mailing address. It has an optional attribute, ``language``, which defaults to ``i-default``.

When multiple ``SimpleAddressType`` elements are provided on an entity (such as ``AddressStructured`` on a polling location, or ``MailingAddress`` / ``PhysicalAddress`` on contact information), each must have a distinct ``language`` attribute to specify the address in multiple languages.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| location_name | ``xs:string`` | Optional     | Single       | The name of the location or facility     | If the field is invalid or not present,  |
|               |               |              |              | (e.g. "Albemarle High School").          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| address_line  | ``xs:string`` | **Required** | Repeats      | Street address line(s). Multiple         | If no AddressLine is provided, the       |
|               |               |              |              | AddressLine tags may appear in order     | implementation should ignore the         |
|               |               |              |              | (e.g. street address, suite/room).       | SimpleAddressType containing it.         |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city          | ``xs:string`` | Optional     | Single       | The city, town, or municipality.         | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| county        | ``xs:string`` | Optional     | Single       | The county or parish.                    | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| region        | ``xs:string`` | Optional     | Single       | The state, province, or primary          | If the field is invalid or not present,  |
|               |               |              |              | sub-national region (e.g. "VA").         | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| country       | ``xs:string`` | Optional     | Single       | The country (e.g. "USA").                | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| world_region  | ``xs:string`` | Optional     | Single       | Global or continental region if          | If the field is invalid or not present,  |
|               |               |              |              | applicable.                              | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| postal_code   | ``xs:string`` | Optional     | Single       | The postal code or ZIP code.             | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-source:

source
~~~~~~

The Source object represents the organization publishing the information. In a VIP 7.0 main feed file, exactly one Source object must be present. Source is excluded from feed overlays.

+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+==========================================+==============+==============+==========================================+==========================================+
| date_time                   | ``xs:dateTime``                          | **Required** | Single       | Specifies the date and time of feed      | If the field is invalid, then the        |
|                             |                                          |              |              | production in local time.                | implementation is required to ignore the |
|                             |                                          |              |              |                                          | ``Source`` element containing it.        |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description                 | :ref:`single-csv-internationalized-text` | Optional     | Single       | Describes the organization and the data  | If the element is invalid or not         |
|                             |                                          |              |              | contained in the feed.                   | present, then the implementation is      |
|                             |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| feed_contact_information_id | :ref:`single-csv-contact-information`    | Optional     | Single       | Contact information for inquiries about  | If the element is invalid or not         |
|                             |                                          |              |              | the feed data.                           | present, then the implementation is      |
|                             |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                        | ``xs:string``                            | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                             |                                          |              |              | publishing the feed.                     | implementation is required to ignore the |
|                             |                                          |              |              |                                          | ``Source`` element containing it.        |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| organization_uri            | :ref:`single-csv-internationalized-uri`  | Optional     | Single       | Web address of the organization          | If the element is invalid or not         |
|                             |                                          |              |              | publishing the feed.                     | present, then the implementation is      |
|                             |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| terms_of_use_uri            | :ref:`single-csv-internationalized-uri`  | Optional     | Single       | Web address where Terms of Use for the   | If the element is invalid or not         |
|                             |                                          |              |              | feed data can be found.                  | present, then the implementation is      |
|                             |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vip_id                      | ``xs:string``                            | **Required** | Single       | FIPS code identifying the state or       | If the field is invalid, then the        |
|                             |                                          |              |              | jurisdiction.                            | implementation is required to ignore the |
|                             |                                          |              |              |                                          | ``Source`` element containing it.        |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,date_time,description,name,organization_uri,terms_of_use_uri,vip_id
    source01,2024-10-24T14:25:28,SBE is official source,"State Board of Elections",http://www.sbe.virginia.gov/,http://example.com/terms,51


.. _single-csv-spatial-boundary:

spatial_boundary
~~~~~~~~~~~~~~~~

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+--------------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                            | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+================================+==============+==============+==============+==========================================+==========================================+
| external_geospatial_feature_id | ``xs:IDREF`` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                                |              |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                                |              |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                                |              |              |              |                                          | it.                                      |
+--------------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,external_geospatial_feature_id
    sb1,egf1


.. _single-csv-street-segment:

street_segment
~~~~~~~~~~~~~~

A StreetSegment object represents a range of house numbers along a street and links them to the containing :ref:`single-csv-precinct`. Street segments are excluded from feed overlays.

+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                  | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+============================+==============+==============+==========================================+==========================================+
| address_direction      | ``xs:string``              | Optional     | Single       | Specifies trailing directional component | If the field is invalid or not present,  |
|                        |                            |              |              | of the address (e.g. "NE").              | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city                   | ``xs:string``              | **Required** | Single       | City or municipality name.               | If the field is invalid, then the        |
|                        |                            |              |              |                                          | implementation is required to ignore the |
|                        |                            |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_addresses | ``xs:boolean``             | Optional     | Single       | If true, the segment covers all          | If the field is invalid or not present,  |
|                        |                            |              |              | addresses on this street. OddEvenBoth    | then the implementation is required to   |
|                        |                            |              |              | must be "both".                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_streets   | ``xs:boolean``             | Optional     | Single       | If true, covers all streets in the city. | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| odd_even_both          | :ref:`single-csv-oeb-enum` | **Required** | Single       | Specifies whether odd, even, or both     | If OddEvenBoth is missing or invalid,    |
|                        |                            |              |              | sides of the street are included from    | the implementation is required to ignore |
|                        |                            |              |              | :ref:`single-csv-oeb-enum`.              | the StreetSegment containing it.         |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_id            | ``xs:IDREF``               | **Required** | Single       | References the containing                | If the field is invalid, then the        |
|                        |                            |              |              | :ref:`single-csv-precinct`.              | implementation is required to ignore the |
|                        |                            |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_house_number     | ``xs:integer``             | Optional     | Single       | Starting house number for the segment    | If the field is invalid or not present,  |
|                        |                            |              |              | range.                                   | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_house_number       | ``xs:integer``             | Optional     | Single       | Ending house number for the segment      | If the field is invalid or not present,  |
|                        |                            |              |              | range.                                   | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_prefix    | ``xs:string``              | Optional     | Single       | Prefix to the house number if any.       | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_suffix    | ``xs:string``              | Optional     | Single       | Suffix to the house number if any.       | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| region                 | ``xs:string``              | **Required** | Single       | State, province, or primary sub-national | If the field is invalid, then the        |
|                        |                            |              |              | region (e.g. "VA").                      | implementation is required to ignore the |
|                        |                            |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| country                | ``xs:string``              | Optional     | Single       | Country code or name (e.g. "USA").       | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_direction       | ``xs:string``              | Optional     | Single       | Leading directional prefix for the       | If the field is invalid or not present,  |
|                        |                            |              |              | street (e.g. "N", "NW").                 | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_name            | ``xs:string``              | Optional     | Single       | Street name.                             | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_suffix          | ``xs:string``              | Optional     | Single       | Street type suffix (e.g. "St", "Ave",    | If the field is invalid or not present,  |
|                        |                            |              |              | "Rd").                                   | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| unit_number            | ``xs:string``              | Optional     | Repeats      | Unit, apartment, or suite number(s).     | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| postal_code            | ``xs:string``              | Optional     | Single       | Postal code or ZIP code.                 | If the field is invalid or not present,  |
|                        |                            |              |              |                                          | then the implementation is required to   |
|                        |                            |              |              |                                          | ignore it.                               |
+------------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,address_direction,city,includes_all_addresses,includes_all_streets,odd_even_both,precinct_id,start_house_number,end_house_number,house_number_prefix,house_number_suffix,region,country,street_direction,street_name,street_suffix,unit_number,postal_code
    ss000001,N,Washington,false,false,odd,pre90113,101,199,,,DC,USA,NW,Delaware,St,,20001
    ss000002,S,Washington,true,false,both,pre90112,,,,,DC,USA,SE,Wisconsin,Ave,,20002


.. _single-csv-term:

term
~~~~

+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+====================================+==============+==============+==========================================+==========================================+
| term_type       | :ref:`single-csv-office-term-type` | Optional     | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|                 |                                    |              |              | :ref:`single-csv-office-term-type` for   | the implementation is required to ignore |
|                 |                                    |              |              | valid values).                           | the ``Office`` element containing it.    |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term_start_date | ``xs:date``                        | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|                 |                                    |              |              | term of the office.                      | then the implementation is required to   |
|                 |                                    |              |              |                                          | ignore it.                               |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term_end_date   | ``xs:date``                        | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|                 |                                    |              |              | term of the office.                      | then the implementation is required to   |
|                 |                                    |              |              |                                          | ignore it.                               |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-csv-time-without-zone:

time_without_zone
~~~~~~~~~~~~~~~~~

A time value with no time zone. The time zone is specified in an enclosing structure, such as a :ref:`single-csv-schedule-with-timezone` element. The pattern is:

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))``


.. _single-csv-voter-service:

voter_service
~~~~~~~~~~~~~

+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+=======================================+==============+==============+==========================================+==========================================+
| description                 | ``xs:string``                         | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                             |                                       |              |              | available.                               | present, then the implementation is      |
|                             |                                       |              |              |                                          | required to ignore it.                   |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_official_person_id | ``xs:IDREF``                          | Optional     | Single       | The :ref:`authority <single-csv-person>` | If the field is invalid or not present,  |
|                             |                                       |              |              | for a particular voter service.          | then the implementation is required to   |
|                             |                                       |              |              |                                          | ignore it.                               |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                        | :ref:`single-csv-voter-service-type`  | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                             |                                       |              |              | <single-csv-voter-service-type>`.        | then the implementation is required to   |
|                             |                                       |              |              |                                          | ignore it.                               |
+-----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                  | ``xs:string``                         | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                             |                                       |              |              | cataloging another type of voter         | then the implementation is required to   |
|                             |                                       |              |              | service.                                 | ignore it.                               |
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

Enumeration describing the set of supported external identifier types for entities such as contests, districts, candidates, and localities.

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
| other          | Any identifier which does not fall into any of the |
|                | above categories.                                  |
+----------------+----------------------------------------------------+


.. _single-csv-location-identifier-type:

location_identifier_type
~~~~~~~~~~~~~~~~~~~~~~~~

Enumeration describing the set of supported location identifier types.

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| latlong      | A latitude/longitude pair, e.g.                    |
|              | `40.6970243,-74.1443098`.                          |
+--------------+----------------------------------------------------+
| pluscode     | An Open Location Code / Plus Code, e.g.            |
|              | `87G8PXRX+86`.                                     |
+--------------+----------------------------------------------------+
| geocoder-id  | A geocoder- or platform-specific identifier such   |
|              | as a Google Place ID. The enclosing element        |
|              | specifies the data provider along with the value.  |
+--------------+----------------------------------------------------+
| other        | Any location identifier that does not fall into    |
|              | the above categories. When using this value,       |
|              | OtherType should be specified.                     |
+--------------+----------------------------------------------------+


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


.. _single-csv-polling-location-type:

polling_location_type
~~~~~~~~~~~~~~~~~~~~~

A list of the various types of polling locations.

+---------------+----------------------------------------------------+
| Tag           | Description                                        |
+===============+====================================================+
| InPersonDayOf | A location for in-person voting on election day.   |
+---------------+----------------------------------------------------+
| InPersonEarly | A location for in-person voting before election    |
|               | day.                                               |
+---------------+----------------------------------------------------+
| DropOff       | A location for dropping off a completed early or   |
|               | absentee ballot.  This includes both staffed       |
|               | locations and ballot drop boxex.                   |
+---------------+----------------------------------------------------+


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
