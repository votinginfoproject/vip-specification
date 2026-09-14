.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party-contest:

party_contest
=============

An extension of :ref:`multi-csv-contest-base` which describes a contest in
which the possible ballot selections are of type :ref:`multi-csv-party-selection`. These could include contests in which straight-party
selections are allowed, or party-list contests (although these are more common
outside of the United States).

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,electoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation
    pcon001,PC1071,bs001 bs002,,Party Election,ed001,all registered voters,,,,false,Straight Party Vote,3,,


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
