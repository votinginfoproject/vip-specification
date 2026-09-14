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

A base model for all Contest types: :ref:`multi-xml-ballot-measure-contest`, :ref:`multi-xml-candidate-contest`, :ref:`multi-xml-party-contest`, and :ref:`multi-xml-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                           | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                         |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                           | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                         |                                         |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         |                                         |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                         |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         |                                         |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                         |              |              |                                          | ignore it.                               |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                            | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                         |                                         |              |              | :ref:`multi-xml-electoral-district`      | implementation is required to ignore the |
|                         |                                         |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                         |                                         |              |              | the contest. Required in main feed;      |                                          |
|                         |                                         |              |              | optional in overlays.                    |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                         |                                         |              |              | electorate for this contest past the     | present, then the implementation should  |
|                         |                                         |              |              | usual "all registered voters"            | ignore it.                               |
|                         |                                         |              |              | electorate. This subtag will most often  |                                          |
|                         |                                         |              |              | be used for primaries and local          |                                          |
|                         |                                         |              |              | elections (e.g. in closed primaries,     |                                          |
|                         |                                         |              |              | voters may have to be registered as a    |                                          |
|                         |                                         |              |              | specific party to vote, or in some local |                                          |
|                         |                                         |              |              | elections, non-citizens can vote).       |                                          |
|                         |                                         |              |              | Clearable in overlays.                   |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier      | :ref:`multi-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                         |                                         |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                         |                                         |              |              | overlays.                                | ignore it.                               |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                          | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                         |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                         |                                         |              |              | in overlays.                             | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                           | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                         |                                         |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                         |                                         |              |              |                                          | ``ContestBase`` element containing it.   |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                          | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                         |                                         |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`multi-xml-vote-variation`         | Optional     | Single       | Vote variation associated with the       | If the field is invalid or not present,  |
|                         |                                         |              |              | contest from                             | then the implementation should ignore    |
|                         |                                         |              |              | :ref:`multi-xml-vote-variation` (e.g.    | it.                                      |
|                         |                                         |              |              | n-of-m, majority, plurality, ranked      |                                          |
|                         |                                         |              |              | choice, et al). Clearable in overlays.   |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                           | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                         |                                         |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                         |                                         |              |              |                                          | it.                                      |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive              | ``xs:string``                           | Optional     | Single       | If specified, the element is treated as  | If the field is invalid or not present,  |
|                         |                                         |              |              | inactive, and the value describes the    | then the implementation should ignore    |
|                         |                                         |              |              | reason (e.g. "Contest cancelled due to   | it.                                      |
|                         |                                         |              |              | unopposed candidate", "Backup polling    |                                          |
|                         |                                         |              |              | location"). Clearable in overlays.       |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
