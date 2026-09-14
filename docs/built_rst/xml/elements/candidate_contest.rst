.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate-contest:

CandidateContest
================

CandidateContest extends :ref:`multi-xml-contest-base` and represents a contest among candidates.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumberElected/>``, ``<ClearOfficeIds/>``, ``<ClearPrimaryPartyIds/>``, ``<ClearVotesAllowed/>``).

+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+================+==============+==============+==========================================+==========================================+
| NumberElected   | ``xs:integer`` | Optional     | Single       | Number of candidates elected in this     | If the field is invalid or not present,  |
|                 |                |              |              | contest (i.e. "N" of N-of-M). Clearable  | then the implementation is required to   |
|                 |                |              |              | in overlays.                             | ignore it.                               |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeIds       | ``xs:IDREFS``  | Optional     | Single       | References a set of                      | If the field is invalid or not present,  |
|                 |                |              |              | :ref:`multi-xml-office` elements, if     | then the implementation is required to   |
|                 |                |              |              | available, which give additional         | ignore it.                               |
|                 |                |              |              | information about the offices. Note: the |                                          |
|                 |                |              |              | order of the office IDs must be in the   |                                          |
|                 |                |              |              | same order as the candidates listed in   |                                          |
|                 |                |              |              | BallotSelectionIds (e.g., if             |                                          |
|                 |                |              |              | BallotSelectionIds reference candidate   |                                          |
|                 |                |              |              | selections with President first and      |                                          |
|                 |                |              |              | Vice-President second, OfficeIds should  |                                          |
|                 |                |              |              | reference the office of President first  |                                          |
|                 |                |              |              | and Vice-President second). Clearable in |                                          |
|                 |                |              |              | overlays.                                |                                          |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrimaryPartyIds | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-xml-party`        | If the field is invalid or not present,  |
|                 |                |              |              | elements if the contest is               | then the implementation is required to   |
|                 |                |              |              | party-specific (e.g. a Democratic or     | ignore it.                               |
|                 |                |              |              | Republican primary). Clearable in        |                                          |
|                 |                |              |              | overlays.                                |                                          |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VotesAllowed    | ``xs:integer`` | Optional     | Single       | Maximum number of selections a voter may | If the field is invalid or not present,  |
|                 |                |              |              | make in this contest. Clearable in       | then the implementation is required to   |
|                 |                |              |              | overlays.                                | ignore it.                               |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateContest id="cc20003">
      <BallotSelectionIds>cs10961 cs10962</BallotSelectionIds>
      <BallotTitle>
         <Text language="en">Governor of Virginia</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Governor</Name>
      <NumberElected>1</NumberElected>
      <OfficeIds>off0000</OfficeIds>
      <VotesAllowed>1</VotesAllowed>
   </CandidateContest>


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
