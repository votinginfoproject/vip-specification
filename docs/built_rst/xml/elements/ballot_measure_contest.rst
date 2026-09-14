.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-measure-contest:

BallotMeasureContest
====================

BallotMeasureContest extends :ref:`multi-xml-contest-base` and provides information about a ballot measure or referendum before the voters.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearConStatement/>``, ``<ClearProStatement/>``, ``<ClearFullText/>``).

+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Statement in opposition to the measure.  | If the element is invalid or not         |
|                  |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the element is invalid or not         |
|                  |                                         |              |              | not voting) on this proposition will     | present, then the implementation is      |
|                  |                                         |              |              | have (i.e. whether abstaining is         | required to ignore it.                   |
|                  |                                         |              |              | considered a vote against it). Clearable |                                          |
|                  |                                         |              |              | in overlays.                             |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Full legal text of the ballot measure.   | If the element is invalid or not         |
|                  |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|                  |                                         |              |              | about the measure. Clearable in          | present, then the implementation is      |
|                  |                                         |              |              | overlays.                                | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                  |                                         |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                  |                                         |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                  |                                         |              |              | 50% plus one vote). Other common         |                                          |
|                  |                                         |              |              | thresholds are "three-fifths" and        |                                          |
|                  |                                         |              |              | "two-thirds". Clearable in overlays.     |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Statement in support of the measure.     | If the element is invalid or not         |
|                  |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Summary explanation of the measure.      | If the element is invalid or not         |
|                  |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :ref:`multi-xml-ballot-measure-type`    | Optional     | Single       | Specifies the particular type of ballot  | If the field is invalid or not present,  |
|                  |                                         |              |              | measure from                             | then the implementation is required to   |
|                  |                                         |              |              | :ref:`multi-xml-ballot-measure-type`     | ignore it.                               |
|                  |                                         |              |              | (e.g. initiative, referendum,            |                                          |
|                  |                                         |              |              | constitutional amendment). Clearable in  |                                          |
|                  |                                         |              |              | overlays.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | ``xs:string``                           | Optional     | Single       | Custom measure type if Type is "other".  | If the field is invalid or not present,  |
|                  |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotMeasureContest id="bmc30001">
      <BallotSelectionIds>bms30001a bms30001b</BallotSelectionIds>
      <BallotTitle>
         <Text language="en">State Bond Initiative</Text>
         <Text language="es">Iniciativa de Bonos del Estado</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Bond Initiative</Name>
      <ConStatement>
         <Text language="en">Opponents argue this increases state debt.</Text>
      </ConStatement>
      <ProStatement>
         <Text language="en">Supporters state this funds critical school repairs.</Text>
      </ProStatement>
      <Type>referendum</Type>
   </BallotMeasureContest>


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
