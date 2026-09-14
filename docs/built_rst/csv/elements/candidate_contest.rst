.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-candidate-contest:

candidate_contest
=================

CandidateContest extends :ref:`multi-csv-contest-base` and represents a contest among candidates.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumberElected/>``, ``<ClearOfficeIds/>``, ``<ClearPrimaryPartyIds/>``, ``<ClearVotesAllowed/>``).

+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+================+==============+==============+==========================================+==========================================+
| number_elected    | ``xs:integer`` | Optional     | Single       | Number of candidates elected in this     | If the field is invalid or not present,  |
|                   |                |              |              | contest (i.e. "N" of N-of-M). Clearable  | then the implementation is required to   |
|                   |                |              |              | in overlays.                             | ignore it.                               |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_ids        | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-csv-office`       | If the field is invalid or not present,  |
|                   |                |              |              | elements associated with the contest.    | then the implementation is required to   |
|                   |                |              |              | Clearable in overlays.                   | ignore it.                               |
+-------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| primary_party_ids | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-csv-party`        | If the field is invalid or not present,  |
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
| electorate_specification | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                          |                                         |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                          |                                         |              |              | party affiliation for primaries).        | ignore it.                               |
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
| vote_variation           | :ref:`multi-csv-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                          |                                         |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                          |                                         |              |              | :ref:`multi-csv-vote-variation`.         | it.                                      |
|                          |                                         |              |              | Clearable in overlays.                   |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``xs:string``                           | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                          |                                         |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                          |                                         |              |              |                                          | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive              | ``xs:string``                           | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                          |                                         |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                          |                                         |              |              | in overlays.                             | it.                                      |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
