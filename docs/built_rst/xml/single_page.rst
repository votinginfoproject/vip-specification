.. This file is auto-generated.  Do not edit it by hand!

.. _single-xml:

XML Elements & Enumerations (Single Page)
=========================================

.. contents::
   :local:


.. _single-xml-elements:

Elements
--------


.. _single-xml-ballot-measure-contest:

BallotMeasureContest
~~~~~~~~~~~~~~~~~~~~

BallotMeasureContest extends :ref:`single-xml-contest-base` and provides information about a ballot measure or referendum before the voters.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearConStatement/>``, ``<ClearProStatement/>``, ``<ClearFullText/>``).

+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+==========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :ref:`single-xml-internationalized-text` | Optional     | Single       | Statement in opposition to the measure.  | If the element is invalid or not         |
|                  |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                          |              |              |                                          | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :ref:`single-xml-internationalized-text` | Optional     | Single       | Describes effect of abstaining on the    | If the element is invalid or not         |
|                  |                                          |              |              | measure. Clearable in overlays.          | present, then the implementation is      |
|                  |                                          |              |              |                                          | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :ref:`single-xml-internationalized-text` | Optional     | Single       | Full legal text of the ballot measure.   | If the element is invalid or not         |
|                  |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                          |              |              |                                          | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|                  |                                          |              |              | about the measure. Clearable in          | present, then the implementation is      |
|                  |                                          |              |              | overlays.                                | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :ref:`single-xml-internationalized-text` | Optional     | Single       | Threshold required for passage (e.g.     | If the element is invalid or not         |
|                  |                                          |              |              | "majority", "two-thirds"). Clearable in  | present, then the implementation is      |
|                  |                                          |              |              | overlays.                                | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :ref:`single-xml-internationalized-text` | Optional     | Single       | Statement in support of the measure.     | If the element is invalid or not         |
|                  |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                          |              |              |                                          | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :ref:`single-xml-internationalized-text` | Optional     | Single       | Summary explanation of the measure.      | If the element is invalid or not         |
|                  |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                  |                                          |              |              |                                          | required to ignore it.                   |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :ref:`single-xml-ballot-measure-type`    | Optional     | Single       | Type of measure from                     | If the field is invalid or not present,  |
|                  |                                          |              |              | :ref:`single-xml-ballot-measure-type`.   | then the implementation is required to   |
|                  |                                          |              |              | Clearable in overlays.                   | ignore it.                               |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | ``xs:string``                            | Optional     | Single       | Custom measure type if Type is "other".  | If the field is invalid or not present,  |
|                  |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                  |                                          |              |              |                                          | ignore it.                               |
+------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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


.. _single-xml-contest-base:

ContestBase
^^^^^^^^^^^

A base model for all Contest types: :ref:`single-xml-ballot-measure-contest`, :ref:`single-xml-candidate-contest`, :ref:`single-xml-party-contest`, and :ref:`single-xml-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+==========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                         |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`single-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`single-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                         |                                          |              |              | :ref:`single-xml-electoral-district`     | implementation is required to ignore the |
|                         |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                         |                                          |              |              | the contest. Required in main feed;      |                                          |
|                         |                                          |              |              | optional in overlays.                    |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`single-xml-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                         |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                         |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier      | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                         |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                         |                                          |              |              | overlays.                                | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                         |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                         |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`single-xml-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                         |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                         |                                          |              |              | :ref:`single-xml-vote-variation`.        | it.                                      |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                         |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                         |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-ballot-measure-selection:

BallotMeasureSelection
~~~~~~~~~~~~~~~~~~~~~~

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:ref:`single-xml-ballot-measure-contest` that would appear on the ballot.
BallotMeasureSelection extends :ref:`single-xml-ballot-selection-base`.

+--------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==========================================+==============+==============+==========================================+==========================================+
| Selection    | :ref:`single-xml-internationalized-text` | **Required** | Single       | Selection text for a                     | If the element is invalid or not         |
|              |                                          |              |              | :ref:`single-xml-ballot-measure-contest` | present, the implementation is required  |
|              |                                          |              |              |                                          | to ignore the BallotMeasureSelection     |
|              |                                          |              |              |                                          | containing it.                           |
+--------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotMeasureSelection id="bms30001a">
      <Selection label="bms30001at">
         <Text language="en">Yes</Text>
         <Text language="es">Sí</Text>
      </Selection>
   </BallotMeasureSelection>
   <BallotMeasureSelection id="bms30001b">
      <Selection label="bms30001bt">
         <Text language="en">No</Text>
         <Text language="es">No</Text>
      </Selection>
   </BallotMeasureSelection>


.. _single-xml-ballot-selection-base:

BallotSelectionBase
^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-xml-ballot-measure-selection`,
:ref:`single-xml-candidate-selection`, and :ref:`single-xml-party-selection`.

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|               |                |              |              | is the default ordering, and can be      | ignore it.                               |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`single-xml-ordered-contest`.    |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-ballot-selection-base:

BallotSelectionBase
~~~~~~~~~~~~~~~~~~~

A base model for all ballot selection types:
:ref:`single-xml-ballot-measure-selection`,
:ref:`single-xml-candidate-selection`, and :ref:`single-xml-party-selection`.

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|               |                |              |              | is the default ordering, and can be      | ignore it.                               |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`single-xml-ordered-contest`.    |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-ballot-style:

BallotStyle
~~~~~~~~~~~

A container for the contests/measures on the ballot.

+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=========================================+==============+==============+==========================================+==========================================+
| ImageUri          | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Specifies a URI that returns an image of | If the element is invalid or not         |
|                   |                                         |              |              | the sample ballot.                       | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedContestIds | ``xs:IDREFS``                           | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                   |                                         |              |              | :ref:`single-xml-ordered-contest`        | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyIds          | ``xs:IDREFS``                           | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                   |                                         |              |              | :ref:`single-xml-party`s.                | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotStyle id="bs00000">
      <OrderedContestIds>oc20003 oc20004 oc20005 oc20025 oc20355 oc20449</OrderedContestIds>
   </BallotStyle>


.. _single-xml-candidate:

Candidate
~~~~~~~~~

The Candidate object represents a candidate in a contest. If a candidate is running in multiple contests, each contest **must** have its own Candidate object.

+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| Tag                | Data Type                                        | Required?    | Repeats?     | Description                                       | Error Handling                           |
+====================+==================================================+==============+==============+===================================================+==========================================+
| BallotName         | :ref:`single-xml-internationalized-text`         | **Required** | Single       | The candidate's name as it will appear on the     | If the element is invalid, then the      |
|                    |                                                  |              |              | ballot.                                           | implementation is required to ignore the |
|                    |                                                  |              |              |                                                   | ``Candidate`` element containing it.     |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ContactInformation | :ref:`single-xml-contact-information`            | Optional     | Single       | Campaign or official contact information for the  | If the element is invalid or not         |
|                    |                                                  |              |              | candidate.                                        | present, then the implementation is      |
|                    |                                                  |              |              |                                                   | required to ignore it.                   |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`single-xml-external-identifier`            | Optional     | Repeats      | External identifier(s) linking this candidate to  | If the element is invalid or not         |
|                    |                                                  |              |              | external systems.                                 | present, then the implementation is      |
|                    |                                                  |              |              |                                                   | required to ignore it.                   |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| FileDate           | ``xs:date``                                      | Optional     | Single       | Date when the candidate filed for office.         | If the field is invalid or not present,  |
|                    |                                                  |              |              |                                                   | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| IsIncumbent        | ``xs:boolean``                                   | Optional     | Single       | Indicates whether the candidate currently holds   | If the field is invalid or not present,  |
|                    |                                                  |              |              | the office.                                       | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| IsTopTicket        | ``xs:boolean``                                   | Optional     | Single       | Indicates whether the candidate is at the top of  | If the field is invalid or not present,  |
|                    |                                                  |              |              | a ticket.                                         | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| PartyId            | ``xs:IDREF``                                     | Optional     | Single       | References the candidate's affiliated             | If the field is invalid or not present,  |
|                    |                                                  |              |              | :ref:`single-xml-party`.                          | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| PersonId           | ``xs:IDREF``                                     | Optional     | Single       | References the underlying                         | If the field is invalid or not present,  |
|                    |                                                  |              |              | :ref:`single-xml-person` record.                  | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| PostElectionStatus | :ref:`single-xml-candidate-post-election-status` | Optional     | Single       | Post-election outcome status from                 | If the field is invalid or not present,  |
|                    |                                                  |              |              | :ref:`single-xml-candidate-post-election-status`. | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| PreElectionStatus  | :ref:`single-xml-candidate-pre-election-status`  | Optional     | Single       | Pre-election qualification status from            | If the field is invalid or not present,  |
|                    |                                                  |              |              | :ref:`single-xml-candidate-pre-election-status`.  | then the implementation is required to   |
|                    |                                                  |              |              |                                                   | ignore it.                               |
+--------------------+--------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Candidate id="can10961">
      <BallotName>
         <Text language="en">Ken T. Cuccinelli II</Text>
      </BallotName>
      <PartyId>par0001</PartyId>
      <PersonId>per10961</PersonId>
   </Candidate>


.. _single-xml-candidate-contest:

CandidateContest
~~~~~~~~~~~~~~~~

CandidateContest extends :ref:`single-xml-contest-base` and represents a contest among candidates.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumberElected/>``, ``<ClearOfficeIds/>``, ``<ClearPrimaryPartyIds/>``, ``<ClearVotesAllowed/>``).

+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+================+==============+==============+==========================================+==========================================+
| NumberElected   | ``xs:integer`` | Optional     | Single       | Number of candidates elected in this     | If the field is invalid or not present,  |
|                 |                |              |              | contest (i.e. "N" of N-of-M). Clearable  | then the implementation is required to   |
|                 |                |              |              | in overlays.                             | ignore it.                               |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeIds       | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-xml-office`      | If the field is invalid or not present,  |
|                 |                |              |              | elements associated with the contest.    | then the implementation is required to   |
|                 |                |              |              | Clearable in overlays.                   | ignore it.                               |
+-----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrimaryPartyIds | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-xml-party`       | If the field is invalid or not present,  |
|                 |                |              |              | elements if the contest is               | then the implementation is required to   |
|                 |                |              |              | party-specific. Clearable in overlays.   | ignore it.                               |
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


.. _single-xml-contest-base:

ContestBase
^^^^^^^^^^^

A base model for all Contest types: :ref:`single-xml-ballot-measure-contest`, :ref:`single-xml-candidate-contest`, :ref:`single-xml-party-contest`, and :ref:`single-xml-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+==========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                         |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`single-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`single-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                         |                                          |              |              | :ref:`single-xml-electoral-district`     | implementation is required to ignore the |
|                         |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                         |                                          |              |              | the contest. Required in main feed;      |                                          |
|                         |                                          |              |              | optional in overlays.                    |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`single-xml-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                         |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                         |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier      | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                         |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                         |                                          |              |              | overlays.                                | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                         |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                         |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`single-xml-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                         |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                         |                                          |              |              | :ref:`single-xml-vote-variation`.        | it.                                      |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                         |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                         |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-candidate-selection:

CandidateSelection
~~~~~~~~~~~~~~~~~~

CandidateSelection extends :ref:`single-xml-ballot-selection-base` and represents a ballot selection for one or more candidates in a candidate contest.

+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+================+==============+==============+==========================================+==========================================+
| CandidateIds        | ``xs:IDREFS``  | **Required** | Single       | References :ref:`single-xml-candidate`   | If CandidateIds is invalid or not        |
|                     |                |              |              | elements that comprise this selection    | present, the implementation is required  |
|                     |                |              |              | (e.g. candidate and running mate).       | to ignore the CandidateSelection         |
|                     |                |              |              |                                          | containing it.                           |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyIds | ``xs:IDREFS``  | Optional     | Single       | References :ref:`single-xml-party`       | If the field is invalid or not present,  |
|                     |                |              |              | elements endorsing this candidate        | then the implementation is required to   |
|                     |                |              |              | selection.                               | ignore it.                               |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | ``xs:boolean`` | Optional     | Single       | Signifies whether this selection         | If the field is invalid or not present,  |
|                     |                |              |              | represents a write-in line.              | then the implementation is required to   |
|                     |                |              |              |                                          | ignore it.                               |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateSelection id="cs10861">
      <CandidateIds>can10861a can10861b</CandidateIds>
      <EndorsementPartyIds>par0001</EndorsementPartyIds>
   </CandidateSelection>


.. _single-xml-ballot-selection-base:

BallotSelectionBase
^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-xml-ballot-measure-selection`,
:ref:`single-xml-candidate-selection`, and :ref:`single-xml-party-selection`.

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|               |                |              |              | is the default ordering, and can be      | ignore it.                               |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`single-xml-ordered-contest`.    |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-checksum:

Checksum
~~~~~~~~

The ``Checksum`` object contains information about a cryptographic checksum, including
the raw checksum value and the cryptographic hash algorithm used to compute it.

+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+======================================+==============+==============+==========================================+==========================================+
| Algorithm    | :ref:`single-xml-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to | If the field is invalid, then the        |
|              |                                      |              |              | compute the checksum value.              | implementation is required to ignore the |
|              |                                      |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                        | **Required** | Single       | The raw cryptographic checksum value     | If the field is invalid, then the        |
|              |                                      |              |              | encoded as a non-delimited, lowercase    | implementation is required to ignore the |
|              |                                      |              |              | hexadecimal string.                      | ``Checksum`` element containing it.      |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <Checksum>
      <Algorithm>sha-256</Algorithm>
      <Value>65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e</Value>
    </Checksum>


.. _single-xml-contact-information:

ContactInformation
~~~~~~~~~~~~~~~~~~

Defines contact information (addresses, location identifiers, phone numbers, emails, schedules) for persons, election offices, voter services, or polling locations. ContactInformation has an optional attribute ``label``.

+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag                | Data Type                                | Required?    | Repeats?     | Description                                 | Error Handling                           |
+====================+==========================================+==============+==============+=============================================+==========================================+
| MailingAddress     | :ref:`single-xml-simple-address-type`    | Optional     | Repeats      | Structured mailing address for the contact. | If the element is invalid or not         |
|                    |                                          |              |              | Multiple addresses in different languages   | present, then the implementation is      |
|                    |                                          |              |              | can be specified.                           | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| PhysicalAddress    | :ref:`single-xml-simple-address-type`    | Optional     | Repeats      | Structured physical address for the         | If the element is invalid or not         |
|                    |                                          |              |              | contact. Multiple addresses in different    | present, then the implementation is      |
|                    |                                          |              |              | languages can be specified.                 | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LocationIdentifier | :ref:`single-xml-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus  | If the element is invalid or not         |
|                    |                                          |              |              | Code, coordinates).                         | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Directions         | :ref:`single-xml-internationalized-text` | Optional     | Single       | Directions for finding or reaching the      | If the element is invalid or not         |
|                    |                                          |              |              | contact location.                           | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Email              | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | Email address(es) for the contact.          | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Fax                | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | Fax number(s) for the contact.              | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Hours              | :ref:`single-xml-internationalized-text` | Optional     | Single       | Operating hours as free-form text. *(NB:    | If the element is invalid or not         |
|                    |                                          |              |              | deprecated in favor of                      | present, then the implementation is      |
|                    |                                          |              |              | :ref:`single-xml-schedule-with-timezone`)*. | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Schedule           | :ref:`single-xml-schedule-with-timezone` | Optional     | Repeats      | Structured schedule with dates and          | If the element is invalid or not         |
|                    |                                          |              |              | operating hours.                            | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LatLng             | :ref:`single-xml-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.         | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Name               | :ref:`single-xml-internationalized-text` | Optional     | Single       | Person or place name associated with this   | If the element is invalid or not         |
|                    |                                          |              |              | contact information.                        | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Phone              | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | Telephone number(s) for the contact.        | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Uri                | :ref:`single-xml-internationalized-uri`  | Optional     | Repeats      | Web address(es) for the contact.            | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ContactInformation label="office_contact">
      <PhysicalAddress language="en">
         <LocationName>City Hall</LocationName>
         <AddressLine>100 N Main St, Room 101</AddressLine>
         <City>Springfield</City>
         <Region>IL</Region>
         <PostalCode>62701</PostalCode>
      </PhysicalAddress>
      <LocationIdentifier provider="google">
         <Type>pluscode</Type>
         <Value>86HJQPRX+86</Value>
      </LocationIdentifier>
      <Email>elections@springfield.gov</Email>
      <Phone>217-555-0100</Phone>
      <Schedule>
         <TimeZone>America/Chicago</TimeZone>
         <Hours>
            <StartTime>08:30:00</StartTime>
            <EndTime>16:30:00</EndTime>
         </Hours>
      </Schedule>
      <Uri>https://elections.springfield.gov</Uri>
   </ContactInformation>


.. _single-xml-contest-base:

ContestBase
~~~~~~~~~~~

A base model for all Contest types: :ref:`single-xml-ballot-measure-contest`, :ref:`single-xml-candidate-contest`, :ref:`single-xml-party-contest`, and :ref:`single-xml-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+==========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                         |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`single-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`single-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                         |                                          |              |              | :ref:`single-xml-electoral-district`     | implementation is required to ignore the |
|                         |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                         |                                          |              |              | the contest. Required in main feed;      |                                          |
|                         |                                          |              |              | optional in overlays.                    |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`single-xml-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                         |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                         |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier      | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                         |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                         |                                          |              |              | overlays.                                | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                         |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                         |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`single-xml-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                         |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                         |                                          |              |              | :ref:`single-xml-vote-variation`.        | it.                                      |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                         |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                         |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-election:

Election
~~~~~~~~

The Election object represents an election event. A feed must contain **exactly one** Election object in the main feed. In feed overlays, Election can appear to update election metadata.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearAbsenteeBallotInfo/>``). Fields that are required in the main feed (Date and TopLevelLocalityId) are optional in overlays.

+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+==========================================+==============+==============+==========================================+==========================================+
| AbsenteeBallotInfo         | :ref:`single-xml-internationalized-text` | Optional     | Single       | Information about requesting absentee    | If the element is invalid or not         |
|                            |                                          |              |              | ballots.                                 | present, then the implementation is      |
|                            |                                          |              |              |                                          | required to ignore it.                   |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeRequestDeadline    | ``xs:date``                              | Optional     | Single       | Last day to request an absentee ballot.  | If the field is invalid or not present,  |
|                            |                                          |              |              |                                          | then the implementation is required to   |
|                            |                                          |              |              |                                          | ignore it.                               |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Date                       | ``xs:date``                              | **Required** | Single       | Date of the election in local time.      | If the field is invalid, then the        |
|                            |                                          |              |              | Required in main feed; optional in       | implementation is required to ignore the |
|                            |                                          |              |              | overlays.                                | ``Election`` element containing it.      |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionType               | :ref:`single-xml-internationalized-text` | Optional     | Single       | Type of election (e.g. General, Primary, | If the element is invalid or not         |
|                            |                                          |              |              | Special).                                | present, then the implementation is      |
|                            |                                          |              |              |                                          | required to ignore it.                   |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasElectionDayRegistration | ``xs:boolean``                           | Optional     | Single       | Specifies whether voters can register on | If the field is invalid or not present,  |
|                            |                                          |              |              | election day.                            | then the implementation is required to   |
|                            |                                          |              |              |                                          | ignore it.                               |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Schedule                   | :ref:`single-xml-schedule-with-timezone` | Optional     | Repeats      | Schedule of voting dates and hours for   | If the element is invalid or not         |
|                            |                                          |              |              | the election.                            | present, then the implementation is      |
|                            |                                          |              |              |                                          | required to ignore it.                   |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsStatewide                | ``xs:boolean``                           | Optional     | Single       | Indicates whether the election is        | If the field is invalid or not present,  |
|                            |                                          |              |              | statewide.                               | then the implementation is required to   |
|                            |                                          |              |              |                                          | ignore it.                               |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                       | :ref:`single-xml-internationalized-text` | Optional     | Single       | The name of the election.                | If the element is invalid or not         |
|                            |                                          |              |              |                                          | present, then the implementation is      |
|                            |                                          |              |              |                                          | required to ignore it.                   |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationDeadline       | ``xs:date``                              | Optional     | Single       | Last day to register to vote for the     | If the field is invalid or not present,  |
|                            |                                          |              |              | election.                                | then the implementation is required to   |
|                            |                                          |              |              |                                          | ignore it.                               |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationInfo           | :ref:`single-xml-internationalized-text` | Optional     | Single       | Information about voter registration.    | If the element is invalid or not         |
|                            |                                          |              |              |                                          | present, then the implementation is      |
|                            |                                          |              |              |                                          | required to ignore it.                   |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ResultsUri                 | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | Web address where election results may   | If the element is invalid or not         |
|                            |                                          |              |              | be found.                                | present, then the implementation is      |
|                            |                                          |              |              |                                          | required to ignore it.                   |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TopLevelLocalityId         | ``xs:IDREF``                             | **Required** | Single       | Links to the top-level                   | If the field is invalid or not present,  |
|                            |                                          |              |              | :ref:`single-xml-locality` for the       | the implementation is required to ignore |
|                            |                                          |              |              | election (e.g. the state locality).      | the Election containing it.              |
|                            |                                          |              |              | Required in main feed; optional in       |                                          |
|                            |                                          |              |              | overlays.                                |                                          |
+----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Election id="ele30000">
      <Date>2024-11-05</Date>
      <Name>
         <Text language="en">2024 General Election</Text>
         <Text language="es">Elecciones Generales de 2024</Text>
      </Name>
      <ElectionType>General</ElectionType>
      <HasElectionDayRegistration>false</HasElectionDayRegistration>
      <IsStatewide>true</IsStatewide>
      <RegistrationDeadline>2024-10-15</RegistrationDeadline>
      <AbsenteeRequestDeadline>2024-10-25</AbsenteeRequestDeadline>
      <ResultsUri>https://www.sbe.virginia.gov/ElectionResults.html</ResultsUri>
      <TopLevelLocalityId>loc51</TopLevelLocalityId>
   </Election>


.. _single-xml-election-administration:

ElectionAdministration
~~~~~~~~~~~~~~~~~~~~~~

The ElectionAdministration element represents an administrative body serving a locality's election functions. In VIP 7.0, ElectionAdministration is embedded directly by value inside a :ref:`single-xml-locality` element rather than referenced by an ID.

In overlay feeds, the entire ElectionAdministration element is replaced as a single unit on the locality, or cleared using ``<ClearElectionAdministration/>``.

+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============================+=========================================+==============+==============+==========================================+==========================================+
| AbsenteeUri                  | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for absentee voting          | If the element is invalid or not         |
|                              |                                         |              |              | information.                             | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AmIRegisteredUri             | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for voter registration       | If the element is invalid or not         |
|                              |                                         |              |              | status verification.                     | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTrackingUri            | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for tracking mail-in         | If the element is invalid or not         |
|                              |                                         |              |              | ballots.                                 | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotProvisionalTrackingUri | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for provisional ballot       | If the element is invalid or not         |
|                              |                                         |              |              | tracking.                                | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ContactInformation           | :ref:`single-xml-contact-information`   | Optional     | Single       | Primary contact information for the      | If the element is invalid or not         |
|                              |                                         |              |              | election administration.                 | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionsUri                 | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Primary web address for the election     | If the element is invalid or not         |
|                              |                                         |              |              | administration.                          | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationUri              | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for voter registration.      | If the element is invalid or not         |
|                              |                                         |              |              |                                          | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RulesUri                     | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for election rules,          | If the element is invalid or not         |
|                              |                                         |              |              | regulations, and statutes.               | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService                 | :ref:`single-xml-voter-service`         | Optional     | Repeats      | Specific voter services provided by the  | If the element is invalid or not         |
|                              |                                         |              |              | administration (e.g. voter registration, | present, then the implementation is      |
|                              |                                         |              |              | overseas voting).                        | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri          | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address where voters can see sample  | If the element is invalid or not         |
|                              |                                         |              |              | ballots.                                 | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhereDoIVoteUri              | :ref:`single-xml-internationalized-uri` | Optional     | Single       | Web address for official polling place   | If the element is invalid or not         |
|                              |                                         |              |              | lookup.                                  | present, then the implementation is      |
|                              |                                         |              |              |                                          | required to ignore it.                   |
+------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectionAdministration>
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <BallotTrackingUri>https://www.vote.virginia.gov/track</BallotTrackingUri>
      <BallotProvisionalTrackingUri>https://www.vote.virginia.gov/provisional</BallotProvisionalTrackingUri>
      <ContactInformation label="ea_contact">
         <Name>Virginia Department of Elections</Name>
         <PhysicalAddress>
            <AddressLine>Washington Building, First Floor</AddressLine>
            <AddressLine>1100 Bank Street</AddressLine>
            <City>Richmond</City>
            <Region>VA</Region>
            <PostalCode>23219</PostalCode>
         </PhysicalAddress>
         <Phone>804-864-8901</Phone>
         <Email>info@elections.virginia.gov</Email>
      </ContactInformation>
      <ElectionsUri>http://www.sbe.virginia.gov/</ElectionsUri>
      <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      <RulesUri>http://www.sbe.virginia.gov/rules</RulesUri>
      <WhatIsOnMyBallotUri>https://www.vote.virginia.gov/ballot</WhatIsOnMyBallotUri>
      <WhereDoIVoteUri>https://www.vote.virginia.gov/polling-place</WhereDoIVoteUri>
   </ElectionAdministration>


.. _single-xml-voter-service:

VoterService
^^^^^^^^^^^^

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`single-xml-contact-information`    | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          |                                          |              |              | service.                                 | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :ref:`single-xml-internationalized-text` | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          |                                          |              |              | available.                               | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                             | Optional     | Single       | The :ref:`authority <single-xml-person>` | If the field is invalid or not present,  |
|                          |                                          |              |              | for a particular voter service.          | then the implementation is required to   |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`single-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                          |                                          |              |              | <single-xml-voter-service-type>`.        | then the implementation is required to   |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                            | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                          |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                          |              |              | service.                                 | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-contact-information:

ContactInformation
^^^^^^^^^^^^^^^^^^

Defines contact information (addresses, location identifiers, phone numbers, emails, schedules) for persons, election offices, voter services, or polling locations. ContactInformation has an optional attribute ``label``.

+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag                | Data Type                                | Required?    | Repeats?     | Description                                 | Error Handling                           |
+====================+==========================================+==============+==============+=============================================+==========================================+
| MailingAddress     | :ref:`single-xml-simple-address-type`    | Optional     | Repeats      | Structured mailing address for the contact. | If the element is invalid or not         |
|                    |                                          |              |              | Multiple addresses in different languages   | present, then the implementation is      |
|                    |                                          |              |              | can be specified.                           | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| PhysicalAddress    | :ref:`single-xml-simple-address-type`    | Optional     | Repeats      | Structured physical address for the         | If the element is invalid or not         |
|                    |                                          |              |              | contact. Multiple addresses in different    | present, then the implementation is      |
|                    |                                          |              |              | languages can be specified.                 | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LocationIdentifier | :ref:`single-xml-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus  | If the element is invalid or not         |
|                    |                                          |              |              | Code, coordinates).                         | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Directions         | :ref:`single-xml-internationalized-text` | Optional     | Single       | Directions for finding or reaching the      | If the element is invalid or not         |
|                    |                                          |              |              | contact location.                           | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Email              | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | Email address(es) for the contact.          | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Fax                | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | Fax number(s) for the contact.              | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Hours              | :ref:`single-xml-internationalized-text` | Optional     | Single       | Operating hours as free-form text. *(NB:    | If the element is invalid or not         |
|                    |                                          |              |              | deprecated in favor of                      | present, then the implementation is      |
|                    |                                          |              |              | :ref:`single-xml-schedule-with-timezone`)*. | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Schedule           | :ref:`single-xml-schedule-with-timezone` | Optional     | Repeats      | Structured schedule with dates and          | If the element is invalid or not         |
|                    |                                          |              |              | operating hours.                            | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LatLng             | :ref:`single-xml-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.         | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Name               | :ref:`single-xml-internationalized-text` | Optional     | Single       | Person or place name associated with this   | If the element is invalid or not         |
|                    |                                          |              |              | contact information.                        | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Phone              | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | Telephone number(s) for the contact.        | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Uri                | :ref:`single-xml-internationalized-uri`  | Optional     | Repeats      | Web address(es) for the contact.            | If the element is invalid or not         |
|                    |                                          |              |              |                                             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ContactInformation label="office_contact">
      <PhysicalAddress language="en">
         <LocationName>City Hall</LocationName>
         <AddressLine>100 N Main St, Room 101</AddressLine>
         <City>Springfield</City>
         <Region>IL</Region>
         <PostalCode>62701</PostalCode>
      </PhysicalAddress>
      <LocationIdentifier provider="google">
         <Type>pluscode</Type>
         <Value>86HJQPRX+86</Value>
      </LocationIdentifier>
      <Email>elections@springfield.gov</Email>
      <Phone>217-555-0100</Phone>
      <Schedule>
         <TimeZone>America/Chicago</TimeZone>
         <Hours>
            <StartTime>08:30:00</StartTime>
            <EndTime>16:30:00</EndTime>
         </Hours>
      </Schedule>
      <Uri>https://elections.springfield.gov</Uri>
   </ContactInformation>


.. _single-xml-electoral-district:

ElectoralDistrict
~~~~~~~~~~~~~~~~~

An ElectoralDistrict represents a geographic boundary or jurisdiction for representation, contests, and offices.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumber/>``, ``<ClearExternalIdentifier/>``). Name and Type are optional in overlays.

+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+==========================================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                          |              |              | district to other datasets (e.g.         | present, then the implementation is      |
|                    |                                          |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name               | :ref:`single-xml-internationalized-text` | **Required** | Single       | Name of the district. Required in main   | If the element is invalid, then the      |
|                    |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                    |                                          |              |              |                                          | ``ElectoralDistrict`` element containing |
|                    |                                          |              |              |                                          | it.                                      |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number             | ``xs:integer``                           | Optional     | Single       | Number of the district (e.g. "57").      | If the field is invalid or not present,  |
|                    |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type               | :ref:`single-xml-district-type`          | **Required** | Single       | Type of district from                    | If the field is invalid, then the        |
|                    |                                          |              |              | :ref:`single-xml-district-type`.         | implementation is required to ignore the |
|                    |                                          |              |              | Required in main feed; optional in       | ``ElectoralDistrict`` element containing |
|                    |                                          |              |              | overlays.                                | it.                                      |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType          | ``xs:string``                            | Optional     | Single       | Custom district type if Type is "other". | If the field is invalid or not present,  |
|                    |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectoralDistrict id="ed60129">
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:va/sldl:57</Value>
      </ExternalIdentifier>
      <Name>
         <Text language="en">Virginia's 57th House of Delegates district</Text>
      </Name>
      <Number>57</Number>
      <Type>state-house</Type>
   </ElectoralDistrict>


.. _single-xml-emergency-notice:

EmergencyNotice
~~~~~~~~~~~~~~~

A notification for election administrators to post emergency or last-minute updates (e.g. polling place relocations, hours extensions, severe weather alerts).

In VIP 7.0, EmergencyNotice elements are permitted only in feed overlays on :ref:`single-xml-locality`, :ref:`single-xml-polling-location`, and :ref:`single-xml-precinct` elements.

+--------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`single-xml-internationalized-text` | Optional     | Repeats      | The emergency notification text, which   | If the element is invalid or not         |
|              |                                          |              |              | may be localized in multiple languages.  | present, then the implementation is      |
|              |                                          |              |              |                                          | required to ignore it.                   |
+--------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|              |                                          |              |              | regarding the emergency notice.          | present, then the implementation is      |
|              |                                          |              |              |                                          | required to ignore it.                   |
+--------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AppliesTo    | ``xs:string``                            | Optional     | Repeats      | Contexts in which this emergency notice  | If the field is invalid or not present,  |
|              |                                          |              |              | applies. If omitted, applies generally.  | then the implementation is required to   |
|              |                                          |              |              |                                          | ignore it.                               |
+--------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <EmergencyNotice>
      <NoticeText>
         <Text language="en">Polling location moved due to water main break.</Text>
         <Text language="es">El centro de votación se ha trasladado debido a una rotura de tubería.</Text>
      </NoticeText>
      <NoticeUri>https://elections.example.gov/notices/precinct-203</NoticeUri>
      <AppliesTo>polling_place</AppliesTo>
   </EmergencyNotice>


.. _single-xml-external-file:

ExternalFile
~~~~~~~~~~~~

The ``ExternalFile`` object holds a reference to a file external to the feed itself, such as a shapefile archive. External files are packaged along with the VIP feed into a single archive.

+--------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                  | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+============================+==============+==============+==========================================+==========================================+
| FileUri      | ``xs:anyURI``              | **Required** | Single       | The URI or filename of the external      | If the field is invalid, then the        |
|              |                            |              |              | file.                                    | implementation is required to ignore the |
|              |                            |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Checksum     | :ref:`single-xml-checksum` | **Required** | Single       | The cryptographic checksum of the        | If the element is invalid, then the      |
|              |                            |              |              | external file.                           | implementation is required to ignore the |
|              |                            |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalFile id="ef1">
      <FileUri>precinct_shapes.zip</FileUri>
      <Checksum>
         <Algorithm>sha-256</Algorithm>
         <Value>65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e</Value>
      </Checksum>
   </ExternalFile>


.. _single-xml-checksum:

Checksum
^^^^^^^^

The ``Checksum`` object contains information about a cryptographic checksum, including
the raw checksum value and the cryptographic hash algorithm used to compute it.

+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+======================================+==============+==============+==========================================+==========================================+
| Algorithm    | :ref:`single-xml-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to | If the field is invalid, then the        |
|              |                                      |              |              | compute the checksum value.              | implementation is required to ignore the |
|              |                                      |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                        | **Required** | Single       | The raw cryptographic checksum value     | If the field is invalid, then the        |
|              |                                      |              |              | encoded as a non-delimited, lowercase    | implementation is required to ignore the |
|              |                                      |              |              | hexadecimal string.                      | ``Checksum`` element containing it.      |
+--------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <Checksum>
      <Algorithm>sha-256</Algorithm>
      <Value>65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e</Value>
    </Checksum>


.. _single-xml-external-geospatial-feature:

ExternalGeospatialFeature
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+======================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                         | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                      |              |              | :ref:`single-xml-external-file`          | implementation is required to ignore the |
|                   |                                      |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`single-xml-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                      |              |              |                                          | implementation is required to ignore the |
|                   |                                      |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              |                                          | containing it.                           |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`single-xml-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    | If the element is invalid, then the      |
|                   |                                      |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                   |                                      |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              | the referenced external file. This is a  | containing it.                           |
|                   |                                      |              |              | repeated field in the XML specification, |                                          |
|                   |                                      |              |              | but a scalar field in the CSV            |                                          |
|                   |                                      |              |              | specification. If more than one          |                                          |
|                   |                                      |              |              | identifier is required with the CSV      |                                          |
|                   |                                      |              |              | specifiation, multiple values can be     |                                          |
|                   |                                      |              |              | provided by delimited by space.          |                                          |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-feature-identifier:

FeatureIdentifier
^^^^^^^^^^^^^^^^^

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Index        | ``xs:string`` | **Required** | Single       | The index value for the shapefile        | If the Index field is invalid or not     |
|              |               |              |              | feature.                                 | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the FeatureIdentifier          |
|              |               |              |              |                                          | containing it.                           |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-external-identifier:

ExternalIdentifier
~~~~~~~~~~~~~~~~~~

Specifies an external identifier for an entity, linking it to another dataset or system. ExternalIdentifier has optional attributes ``label`` and ``provider``.

In overlay feeds, this element is clearable using ``<ClearExternalIdentifier/>`` on elements where it is marked clearable.

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`single-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier from    | If the field is invalid or not present,  |
|              |                                   |              |              | :ref:`single-xml-identifier-type`.       | the implementation is required to ignore |
|              |                                   |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                   |              |              |                                          | it.                                      |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                     | Optional     | Single       | Allows defining an identifier type       | If the field is invalid or not present,  |
|              |                                   |              |              | outside                                  | then the implementation is required to   |
|              |                                   |              |              | :ref:`single-xml-identifier-type`. Type  | ignore it.                               |
|              |                                   |              |              | should be set to "other" when using this |                                          |
|              |                                   |              |              | field.                                   |                                          |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                     | **Required** | Single       | Specifies the identifier value.          | If the field is invalid or not present,  |
|              |                                   |              |              |                                          | the implementation is required to ignore |
|              |                                   |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                   |              |              |                                          | it.                                      |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifier>
      <Type>ocd-id</Type>
      <Value>ocd-division/country:us/state:nc/county:durham</Value>
   </ExternalIdentifier>
   <ExternalIdentifier>
      <Type>fips</Type>
      <Value>37063</Value>
   </ExternalIdentifier>
   <ExternalIdentifier>
      <Type>other</Type>
      <OtherType>census</OtherType>
      <Value>99063</Value>
   </ExternalIdentifier>


.. _single-xml-feature-identifier:

FeatureIdentifier
~~~~~~~~~~~~~~~~~

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Index        | ``xs:string`` | **Required** | Single       | The index value for the shapefile        | If the Index field is invalid or not     |
|              |               |              |              | feature.                                 | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the FeatureIdentifier          |
|              |               |              |              |                                          | containing it.                           |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-hours:

Hours
~~~~~

The open and close time for a location. Times must be fully specified without time zone information. The time zone is specified in the containing :ref:`single-xml-schedule-with-timezone` element. Hours has an optional ``label`` attribute.

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| StartTime    | :ref:`single-xml-time-without-zone` | **Required** | Single       | The time at which the location opens.    | If StartTime is invalid or not present,  |
|              |                                     |              |              |                                          | the implementation is required to ignore |
|              |                                     |              |              |                                          | the Hours element containing it.         |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | :ref:`single-xml-time-without-zone` | **Required** | Single       | The time at which the location closes.   | If EndTime is invalid or not present,    |
|              |                                     |              |              |                                          | the implementation is required to ignore |
|              |                                     |              |              |                                          | the Hours element containing it.         |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-time-without-zone:

TimeWithoutZone
^^^^^^^^^^^^^^^

A time value with no time zone. The time zone is specified in an enclosing structure, such as a :ref:`single-xml-schedule-with-timezone` element. The pattern is:

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))``

.. code-block:: xml
   :linenos:

   <Schedule>
      <TimeZone>America/New_York</TimeZone>
      <Hours>
         <StartTime>06:00:00</StartTime>
         <EndTime>19:00:00</EndTime>
      </Hours>
      <StartDate>2024-11-05</StartDate>
      <EndDate>2024-11-05</EndDate>
   </Schedule>


.. _single-xml-html-color-string:

HtmlColorString
~~~~~~~~~~~~~~~

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``


.. _single-xml-internationalized-text:

InternationalizedText
~~~~~~~~~~~~~~~~~~~~~

``InternationalizedText`` represents text translated into one or more languages. It has an optional attribute ``label``.

Text can be represented either as direct element content (treated as default language ``i-default``):

.. code-block:: xml

   <Name label="office_mayor">Mayor</Name>

or as one or more child ``<Text>`` elements with explicit language tags:

.. code-block:: xml

   <Name label="office_mayor">
      <Text language="en">Mayor</Text>
      <Text language="es">Alcalde</Text>
      <Text language="zh">市長</Text>
      <Text language="i-default">Mayor</Text>
   </Name>

NOTE: InternationalizedText is not supported in CSV submissions.

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| Text         | :ref:`single-xml-language-string` | Optional     | Repeats      | Contains the translated string of text   | If the element is invalid or not         |
|              |                                   |              |              | with a language attribute.               | present, then the implementation is      |
|              |                                   |              |              |                                          | required to ignore it.                   |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-internationalized-uri:

InternationalizedUri
~~~~~~~~~~~~~~~~~~~~

``InternationalizedUri`` represents URIs pointing to language-specific versions of materials. It has an optional attribute ``label``.

Like ``InternationalizedText``, it supports either direct body content (fallback ``i-default``) or repeated child ``<Uri>`` elements with ``language`` attributes.

NOTE: InternationalizedUri is not supported in CSV submissions.

+--------------+--------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                      | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+================================+==============+==============+==========================================+==========================================+
| Uri          | :ref:`single-xml-language-uri` | Optional     | Repeats      | Contains a URI with a language           | If the element is invalid or not         |
|              |                                |              |              | attribute.                               | present, then the implementation is      |
|              |                                |              |              |                                          | required to ignore it.                   |
+--------------+--------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-language-string:

LanguageString
~~~~~~~~~~~~~~

``LanguageString`` extends xs:string and can contain text from any language. ``LanguageString``
has one required attribute, ``language``, that must contain the 2-character `language code`_ for the
type of language ``LanguageString`` contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

.. code-block:: xml
   :linenos:

   <BallotTitle>
      <Text language="en">Retention of Supreme Court Justice</Text>
      <Text language="es">La retención de juez de la Corte Suprema</Text>
   </BallotTitle>


.. _single-xml-language-uri:

LanguageUri
~~~~~~~~~~~

``LanguageUri`` extends xs:anyURI and can contain URIs for multiple languages. ``LanguageUri``
has one required attribute, ``language``, that must contain the 2-character `language code`_ for the
type of language ``LanguageUri`` contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


.. _single-xml-lat-lng:

LatLng
~~~~~~

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Latitude     | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|              |               |              |              |                                          | implementation is required to ignore it. |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Longitude    | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|              |               |              |              |                                          | implementation is required to ignore it. |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Source       | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|              |               |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|              |               |              |              | example, this could be the name of a     | ignore it.                               |
|              |               |              |              | geocoding service.                       |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-locality:

Locality
~~~~~~~~

The Locality object represents any jurisdictional level—including states, counties, cities, and towns. Localities form a tree hierarchy using ``ParentLocalityId``, with the root locality representing the state (with ``Type="state"``).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearDefaultPollingHours/>``, ``<ClearElectionAdministration/>``, ``<ClearIsInactive/>``). Name is optional in overlays. Emergency notices and overridden hours are only permitted in overlays.

+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+===========================================+==============+==============+==========================================+==========================================+
| ElectionAdministration   | :ref:`single-xml-election-administration` | Optional     | Single       | The election administration entity for   | If the element is invalid or not         |
|                          |                                           |              |              | this locality. In overlays, this entity  | present, then the implementation is      |
|                          |                                           |              |              | is replaced as a single unit or cleared  | required to ignore it.                   |
|                          |                                           |              |              | with <ClearElectionAdministration/>.     |                                          |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EmergencyNotice          | :ref:`single-xml-emergency-notice`        | Optional     | Single       | Emergency notification applicable        | If the element is invalid or not         |
|                          |                                           |              |              | locality-wide. Permitted only in feed    | present, then the implementation is      |
|                          |                                           |              |              | overlays.                                | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier       | :ref:`single-xml-external-identifier`     | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                           |              |              | locality to external datasets (e.g.      | present, then the implementation is      |
|                          |                                           |              |              | OCD-ID, FIPS). Clearable in overlays.    | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly               | ``xs:boolean``                            | Optional     | Single       | Specifies if the locality runs mail-only | If the field is missing or invalid, the  |
|                          |                                           |              |              | elections. Clearable in overlays.        | implementation is required to assume     |
|                          |                                           |              |              |                                          | IsMailOnly is false.                     |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                             | **Required** | Single       | Name of the locality. Required in main   | If the field is invalid, then the        |
|                          |                                           |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                           |              |              |                                          | ``Locality`` element containing it.      |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                             | Optional     | Single       | References locality-wide polling         | If the field is invalid or not present,  |
|                          |                                           |              |              | locations (e.g. early vote sites or drop | then the implementation is required to   |
|                          |                                           |              |              | boxes). Clearable in overlays.           | ignore it.                               |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ParentLocalityId         | ``xs:IDREF``                              | Optional     | Single       | References the parent                    | If the field is invalid or not present,  |
|                          |                                           |              |              | :ref:`single-xml-locality` in the        | then the implementation is required to   |
|                          |                                           |              |              | jurisdiction hierarchy (e.g. county      | ignore it.                               |
|                          |                                           |              |              | pointing to state). If omitted, this is  |                                          |
|                          |                                           |              |              | a top-level jurisdiction.                |                                          |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`single-xml-district-type`           | Optional     | Single       | The kind of jurisdiction (e.g. state,    | If the field is invalid or not present,  |
|                          |                                           |              |              | county, city) from                       | then the implementation is required to   |
|                          |                                           |              |              | :ref:`single-xml-district-type`.         | ignore it.                               |
|                          |                                           |              |              | Clearable in overlays.                   |                                          |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                             | Optional     | Single       | Allows defining a type of locality       | If the field is invalid or not present,  |
|                          |                                           |              |              | outside :ref:`single-xml-district-type`. | then the implementation is required to   |
|                          |                                           |              |              | Clearable in overlays.                   | ignore it.                               |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DefaultPollingHours      | :ref:`single-xml-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for day-of       | If the element is invalid or not         |
|                          |                                           |              |              | polling locations throughout this        | present, then the implementation is      |
|                          |                                           |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OverriddenPollingHours   | :ref:`single-xml-schedule-with-timezone`  | Optional     | Repeats      | Overridden polling hours for day-of      | If the element is invalid or not         |
|                          |                                           |              |              | locations in this locality. Permitted    | present, then the implementation is      |
|                          |                                           |              |              | only in feed overlays.                   | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DefaultEarlyVoteHours    | :ref:`single-xml-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for in-person    | If the element is invalid or not         |
|                          |                                           |              |              | early voting locations throughout this   | present, then the implementation is      |
|                          |                                           |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OverriddenEarlyVoteHours | :ref:`single-xml-schedule-with-timezone`  | Optional     | Repeats      | Overridden early voting hours in this    | If the element is invalid or not         |
|                          |                                           |              |              | locality. Permitted only in feed         | present, then the implementation is      |
|                          |                                           |              |              | overlays.                                | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DefaultDropoffHours      | :ref:`single-xml-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for ballot       | If the element is invalid or not         |
|                          |                                           |              |              | drop-off locations throughout this       | present, then the implementation is      |
|                          |                                           |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OverriddenDropoffHours   | :ref:`single-xml-schedule-with-timezone`  | Optional     | Repeats      | Overridden drop-off hours in this        | If the element is invalid or not         |
|                          |                                           |              |              | locality. Permitted only in feed         | present, then the implementation is      |
|                          |                                           |              |              | overlays.                                | required to ignore it.                   |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive               | ``xs:string``                             | Optional     | Single       | If specified, marks the locality as      | If the field is invalid or not present,  |
|                          |                                           |              |              | inactive and explains the reason why.    | then the implementation is required to   |
|                          |                                           |              |              | Clearable in overlays.                   | ignore it.                               |
+--------------------------+-------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <!-- State-level locality (root) -->
   <Locality id="loc51">
      <Name>Virginia</Name>
      <Type>state</Type>
      <ElectionAdministration>
         <ElectionsUri>https://www.elections.virginia.gov/</ElectionsUri>
         <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      </ElectionAdministration>
   </Locality>

   <!-- County-level locality referencing parent state -->
   <Locality id="loc70001">
      <Name>ALBEMARLE COUNTY</Name>
      <ParentLocalityId>loc51</ParentLocalityId>
      <Type>county</Type>
      <IsMailOnly>false</IsMailOnly>
      <PollingLocationIds>pl00001 pl00002</PollingLocationIds>
      <DefaultPollingHours>
         <TimeZone>America/New_York</TimeZone>
         <Hours>
            <StartTime>06:00:00</StartTime>
            <EndTime>19:00:00</EndTime>
         </Hours>
      </DefaultPollingHours>
   </Locality>


.. _single-xml-location-identifier:

LocationIdentifier
~~~~~~~~~~~~~~~~~~

Specifies an external identifier for a physical location (e.g. a polling location or contact address), such as a latitude/longitude pair, Plus Code, or geocoder ID. LocationIdentifier has optional attributes ``label``, ``provider`` (e.g. "Google"), and ``relativePriority`` (a decimal number indicating the relative preference of this identifier when multiple identifiers are provided).

In overlay feeds, this element is clearable using ``<ClearLocationIdentifier/>``.

+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag          | Data Type                                  | Required?    | Repeats?     | Description                                 | Error Handling                           |
+==============+============================================+==============+==============+=============================================+==========================================+
| Type         | :ref:`single-xml-location-identifier-type` | **Required** | Single       | Specifies the type of location identifier   | If the field is invalid or not present,  |
|              |                                            |              |              | from                                        | the implementation is required to ignore |
|              |                                            |              |              | :ref:`single-xml-location-identifier-type`. | the ``LocationIdentifier`` containing    |
|              |                                            |              |              |                                             | it.                                      |
+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                              | Optional     | Single       | Specifies the type of identifier if         | If the field is invalid or not present,  |
|              |                                            |              |              | ``Type`` is set to "other".                 | then the implementation is required to   |
|              |                                            |              |              |                                             | ignore it.                               |
+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                              | **Required** | Single       | Specifies the identifier value (e.g. Plus   | If the field is invalid or not present,  |
|              |                                            |              |              | Code, coordinates, Place ID).               | the implementation is required to ignore |
|              |                                            |              |              |                                             | the ``LocationIdentifier`` containing    |
|              |                                            |              |              |                                             | it.                                      |
+--------------+--------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <LocationIdentifier provider="google" relativePriority="1.0">
      <Type>pluscode</Type>
      <Value>87G8PXRX+86</Value>
   </LocationIdentifier>
   <LocationIdentifier provider="google" relativePriority="0.8">
      <Type>geocoder-id</Type>
      <Value>ChIJ2eUgeAK6j4ARbn5u_wAGqWA</Value>
   </LocationIdentifier>


.. _single-xml-office:

Office
~~~~~~

``Office`` represents an elected or appointed government office associated with an electoral district (e.g. Mayor, Governor, School Board).

+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+==========================================+==============+==============+==========================================+==========================================+
| ContactInformation    | :ref:`single-xml-contact-information`    | Optional     | Repeats      | Contact information for the office.      | If the element is invalid or not         |
|                       |                                          |              |              |                                          | present, then the implementation is      |
|                       |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description           | :ref:`single-xml-internationalized-text` | Optional     | Single       | Brief description of the office and its  | If the element is invalid or not         |
|                       |                                          |              |              | responsibilities.                        | present, then the implementation is      |
|                       |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId   | ``xs:IDREF``                             | **Required** | Single       | Links to the                             | If ElectoralDistrictId is invalid or not |
|                       |                                          |              |              | :ref:`single-xml-electoral-district`     | present, the implementation is required  |
|                       |                                          |              |              | representing the geographical scope of   | to ignore the Office containing it.      |
|                       |                                          |              |              | the office.                              |                                          |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier    | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                       |                                          |              |              | office to external systems (e.g.         | present, then the implementation is      |
|                       |                                          |              |              | OCD-ID).                                 | required to ignore it.                   |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline        | ``xs:date``                              | Optional     | Single       | Filing deadline date for candidates      | If the field is invalid or not present,  |
|                       |                                          |              |              | running for this office.                 | then the implementation is required to   |
|                       |                                          |              |              |                                          | ignore it.                               |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan            | ``xs:boolean``                           | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                       |                                          |              |              | partisan.                                | then the implementation is required to   |
|                       |                                          |              |              |                                          | ignore it.                               |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                  | :ref:`single-xml-internationalized-text` | **Required** | Single       | Official name of the office.             | If Name is invalid or not present, the   |
|                       |                                          |              |              |                                          | implementation is required to ignore the |
|                       |                                          |              |              |                                          | Office containing it.                    |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonIds | ``xs:IDREFS``                            | Optional     | Single       | References to :ref:`single-xml-person`   | If the field is invalid or not present,  |
|                       |                                          |              |              | elements for the current office          | then the implementation is required to   |
|                       |                                          |              |              | holder(s).                               | ignore it.                               |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                  | :ref:`single-xml-term`                   | Optional     | Single       | Defines the term length and dates of the | If the element is invalid or not         |
|                       |                                          |              |              | office.                                  | present, then the implementation is      |
|                       |                                          |              |              |                                          | required to ignore it.                   |
+-----------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-term:

Term
^^^^

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`single-xml-office-term-type` | Optional     | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              |                                    |              |              | :ref:`single-xml-office-term-type` for   | the implementation is required to ignore |
|              |                                    |              |              | valid values).                           | the ``Office`` element containing it.    |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | ``xs:date``                        | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                    |              |              | term of the office.                      | then the implementation is required to   |
|              |                                    |              |              |                                          | ignore it.                               |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | ``xs:date``                        | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                    |              |              | term of the office.                      | then the implementation is required to   |
|              |                                    |              |              |                                          | ignore it.                               |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Office id="off0000">
     <ElectoralDistrictId>ed60129</ElectoralDistrictId>
     <FilingDeadline>2013-01-01</FilingDeadline>
     <IsPartisan>false</IsPartisan>
     <Name>
       <Text language="en">Governor</Text>
     </Name>
     <Term>
       <Type>full-term</Type>
     </Term>
   </Office>


.. _single-xml-ordered-contest:

OrderedContest
~~~~~~~~~~~~~~

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:ref:`single-xml-ballot-style` to accurate depict exactly what will show up on a particular
ballot in the proper order.

+---------------------------+---------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
| Tag                       | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                                   |
+===========================+===============+==============+==============+==========================================+==================================================+
| ContestId                 | ``xs:IDREF``  | **Required** | Single       | Links to elements that extend            | If the field is invalid or not present, the      |
|                           |               |              |              | :ref:`single-xml-contest-base`.          | implementation is required to ignore the         |
|                           |               |              |              |                                          | ``OrderedContest`` element containing it.        |
+---------------------------+---------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
| OrderedBallotSelectionIds | ``xs:IDREFS`` | Optional     | Single       | Links to elements that extend            | If the field is invalid or not present, the      |
|                           |               |              |              | :ref:`single-xml-ballot-selection-base`. | implementation is required to ignore it. If an   |
|                           |               |              |              |                                          | ``OrderedBallotSelectionIds`` element is not     |
|                           |               |              |              |                                          | present, the presumed order of the selection     |
|                           |               |              |              |                                          | will be the order of                             |
|                           |               |              |              |                                          | :ref:`single-xml-ballot-selection-base`-extended |
|                           |               |              |              |                                          | elements referenced by the underlying            |
|                           |               |              |              |                                          | :ref:`single-xml-contest-base`-extended          |
|                           |               |              |              |                                          | elements.                                        |
+---------------------------+---------------+--------------+--------------+------------------------------------------+--------------------------------------------------+

.. code-block:: xml
   :linenos:

   <OrderedContest id="oc20003abc">
      <ContestId>cc20003</ContestId>
      <OrderedBallotSelectionIds>cs10961 cs10962 cs10963</OrderedBallotSelectionIds>
   </OrderedContest>


.. _single-xml-party:

Party
~~~~~

The Party object represents a political party or ballot grouping.

+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+==========================================+==============+==============+==========================================+==========================================+
| Abbreviation       | ``xs:string``                            | Optional     | Single       | Abbreviation for the party name (e.g.    | If the field is invalid or not present,  |
|                    |                                          |              |              | "DEM", "REP").                           | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color              | :ref:`single-xml-html-color-string`      | Optional     | Single       | Six-digit hexadecimal HTML color code    | If the element is invalid or not         |
|                    |                                          |              |              | associated with the party.               | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                          |              |              | party to other datasets.                 | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn          | ``xs:boolean``                           | Optional     | Single       | Indicates if the party represents        | If the field is invalid or not present,  |
|                    |                                          |              |              | write-in selections.                     | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LeaderPersonIds    | ``xs:IDREFS``                            | Optional     | Single       | References to :ref:`single-xml-person`   | If the field is invalid or not present,  |
|                    |                                          |              |              | elements for party leadership.           | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri            | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | URI pointing to the party logo.          | If the element is invalid or not         |
|                    |                                          |              |              |                                          | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name               | :ref:`single-xml-internationalized-text` | **Required** | Single       | Official name of the party.              | If the element is invalid, then the      |
|                    |                                          |              |              |                                          | implementation is required to ignore the |
|                    |                                          |              |              |                                          | ``Party`` element containing it.         |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Party id="par0001">
      <Abbreviation>DEM</Abbreviation>
      <Color>0000FF</Color>
      <Name>
         <Text language="en">Democratic Party</Text>
         <Text language="es">Partido Demócrata</Text>
      </Name>
   </Party>


.. _single-xml-party-contest:

PartyContest
~~~~~~~~~~~~

An extension of :ref:`single-xml-contest-base` which describes a contest in
which the possible ballot selections are of type :ref:`single-xml-party-selection`. These could include contests in which straight-party
selections are allowed, or party-list contests (although these are more common
outside of the United States).


.. _single-xml-contest-base:

ContestBase
^^^^^^^^^^^

A base model for all Contest types: :ref:`single-xml-ballot-measure-contest`, :ref:`single-xml-candidate-contest`, :ref:`single-xml-party-contest`, and :ref:`single-xml-retention-contest`.

In overlay feeds, clearable fields can be cleared using empty ``<Clear{FieldName}/>`` elements (e.g. ``<ClearAbbreviation/>``, ``<ClearBallotSelectionIds/>``, ``<ClearIsInactive/>``). Name and ElectoralDistrictId are optional in overlays.

+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+==========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                            | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                            | Optional     | Single       | References BallotSelections belonging to | If the field is invalid or not present,  |
|                         |                                          |              |              | this contest. Clearable in overlays.     | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`single-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`single-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                         |                                          |              |              | the ballot. Clearable in overlays.       | present, then the implementation should  |
|                         |                                          |              |              |                                          | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                             | **Required** | Single       | References the                           | If the field is invalid, then the        |
|                         |                                          |              |              | :ref:`single-xml-electoral-district`     | implementation is required to ignore the |
|                         |                                          |              |              | representing the geographical scope of   | ``ContestBase`` element containing it.   |
|                         |                                          |              |              | the contest. Required in main feed;      |                                          |
|                         |                                          |              |              | optional in overlays.                    |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`single-xml-internationalized-text` | Optional     | Single       | Specifies rules or changes regarding     | If the element is invalid or not         |
|                         |                                          |              |              | eligible electors for this contest (e.g. | present, then the implementation should  |
|                         |                                          |              |              | party affiliation for primaries).        | ignore it.                               |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier      | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                         |                                          |              |              | contest to other sources. Clearable in   | present, then the implementation should  |
|                         |                                          |              |              | overlays.                                | ignore it.                               |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                           | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                         |                                          |              |              | contest rotate on the ballot. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                            | **Required** | Single       | Name of the contest. Required in main    | If the field is invalid, then the        |
|                         |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                         |                                          |              |              |                                          | ``ContestBase`` element containing it.   |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                           | Optional     | Single       | Default ballot ordering for the contest. | If the field is invalid or not present,  |
|                         |                                          |              |              | Clearable in overlays.                   | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`single-xml-vote-variation`         | Optional     | Single       | Voting variation (e.g. plurality,        | If the field is invalid or not present,  |
|                         |                                          |              |              | majority, rcv) from                      | then the implementation should ignore    |
|                         |                                          |              |              | :ref:`single-xml-vote-variation`.        | it.                                      |
|                         |                                          |              |              | Clearable in overlays.                   |                                          |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                            | Optional     | Single       | Custom voting variation if VoteVariation | If the field is invalid or not present,  |
|                         |                                          |              |              | is "other". Clearable in overlays.       | then the implementation should ignore    |
|                         |                                          |              |              |                                          | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive              | ``xs:string``                            | Optional     | Single       | If specified, marks the contest as       | If the field is invalid or not present,  |
|                         |                                          |              |              | inactive with the reason why. Clearable  | then the implementation should ignore    |
|                         |                                          |              |              | in overlays.                             | it.                                      |
+-------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-party-selection:

PartySelection
~~~~~~~~~~~~~~

This element extends :ref:`single-xml-ballot-selection-base` to
support contests in which the selections can be groups of one or more parties.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| PartyIds     | ``xs:IDREFS`` | **Required** | Single       | One or more :ref:`single-xml-party` IDs  | If one or more parties referenced are    |
|              |               |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |               |              |              | selection.                               | implementation is required to ignore the |
|              |               |              |              |                                          | PartySelection containing it.            |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-ballot-selection-base:

BallotSelectionBase
^^^^^^^^^^^^^^^^^^^

A base model for all ballot selection types:
:ref:`single-xml-ballot-measure-selection`,
:ref:`single-xml-candidate-selection`, and :ref:`single-xml-party-selection`.

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|               |                |              |              | is the default ordering, and can be      | ignore it.                               |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`single-xml-ordered-contest`.    |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-person:

Person
~~~~~~

The Person object represents an individual (such as a candidate, election official, or party leader).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearContactInformation/>``, ``<ClearPartyId/>``, ``<ClearProfession/>``).

+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+==========================================+==============+==============+==========================================+==========================================+
| ContactInformation | :ref:`single-xml-contact-information`    | Optional     | Repeats      | Contact information for the person.      | If the element is invalid or not         |
|                    |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateOfBirth        | ``xs:date``                              | Optional     | Single       | Date of birth of the person. Clearable   | If the field is invalid or not present,  |
|                    |                                          |              |              | in overlays.                             | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`single-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                          |              |              | person to external systems. Clearable in | present, then the implementation is      |
|                    |                                          |              |              | overlays.                                | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FirstName          | ``xs:string``                            | Optional     | Single       | First name of the person. Clearable in   | If the field is invalid or not present,  |
|                    |                                          |              |              | overlays.                                | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullName           | :ref:`single-xml-internationalized-text` | Optional     | Single       | Full legal or preferred name of the      | If the element is invalid or not         |
|                    |                                          |              |              | person. Clearable in overlays.           | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Gender             | ``xs:string``                            | Optional     | Single       | Gender of the person. Clearable in       | If the field is invalid or not present,  |
|                    |                                          |              |              | overlays.                                | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LastName           | ``xs:string``                            | Optional     | Single       | Last name of the person. Clearable in    | If the field is invalid or not present,  |
|                    |                                          |              |              | overlays.                                | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| MiddleName         | ``xs:string``                            | Optional     | Repeats      | Middle name(s) of the person. Clearable  | If the field is invalid or not present,  |
|                    |                                          |              |              | in overlays.                             | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Nickname           | ``xs:string``                            | Optional     | Single       | Nickname or informal name. Clearable in  | If the field is invalid or not present,  |
|                    |                                          |              |              | overlays.                                | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId            | ``xs:IDREF``                             | Optional     | Single       | References the :ref:`single-xml-party`   | If the field is invalid or not present,  |
|                    |                                          |              |              | to which the person belongs. Clearable   | then the implementation is required to   |
|                    |                                          |              |              | in overlays.                             | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Prefix             | ``xs:string``                            | Optional     | Single       | Name prefix (e.g. "Dr.", "Rev.").        | If the field is invalid or not present,  |
|                    |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Profession         | :ref:`single-xml-internationalized-text` | Optional     | Single       | Occupation or profession of the person.  | If the element is invalid or not         |
|                    |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Suffix             | ``xs:string``                            | Optional     | Single       | Name suffix (e.g. "Jr.", "III", "Esq."). | If the field is invalid or not present,  |
|                    |                                          |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                          |              |              |                                          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Title              | :ref:`single-xml-internationalized-text` | Optional     | Single       | Official title held by the person.       | If the element is invalid or not         |
|                    |                                          |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                          |              |              |                                          | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Person id="per10961">
      <ContactInformation>
         <Email>ken@example.com</Email>
         <Phone>804-555-0100</Phone>
      </ContactInformation>
      <FirstName>Ken</FirstName>
      <FullName>
         <Text language="en">Ken T. Cuccinelli II</Text>
      </FullName>
      <Gender>male</Gender>
      <LastName>Cuccinelli</LastName>
      <MiddleName>T.</MiddleName>
      <PartyId>par0001</PartyId>
      <Suffix>II</Suffix>
      <Title>
         <Text language="en">Attorney General</Text>
      </Title>
   </Person>


.. _single-xml-polling-location:

PollingLocation
~~~~~~~~~~~~~~~

The PollingLocation object represents a site where voters cast ballots in person or drop off early/absentee ballots. In VIP 7.0, facility names are placed in ``AddressStructured.LocationName``.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearDirections/>``, ``<ClearPhotoUri/>``, ``<ClearIsInactive/>``). AddressStructured and LocationType are optional in overlays.
EmergencyNotice is permitted only in overlays.
In overlays, PollingLocation has an optional attribute ``isNew="true"`` to indicate that a polling location is newly added rather than modifying an existing one.

+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Tag                | Data Type                                | Required?    | Repeats?     | Description                                 | Error Handling                           |
+====================+==========================================+==============+==============+=============================================+==========================================+
| AddressStructured  | :ref:`single-xml-simple-address-type`    | **Required** | Repeats      | Structured address including facility name. | AddressStructured is required for        |
|                    |                                          |              |              | Required in main feed; optional in          | PollingLocation in main feeds.           |
|                    |                                          |              |              | overlays. Multiple addresses in different   |                                          |
|                    |                                          |              |              | languages can be specified.                 |                                          |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LocationIdentifier | :ref:`single-xml-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus  | If the element is invalid or not         |
|                    |                                          |              |              | Code, geocoder ID). Clearable in overlays.  | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Directions         | :ref:`single-xml-internationalized-text` | Optional     | Single       | Instructions for locating the polling site  | If the element is invalid or not         |
|                    |                                          |              |              | or room. Clearable in overlays.             | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Hours              | :ref:`single-xml-internationalized-text` | Optional     | Single       | Operating hours as text. Clearable in       | If the element is invalid or not         |
|                    |                                          |              |              | overlays. *(NB: deprecated in favor of      | present, then the implementation is      |
|                    |                                          |              |              | :ref:`single-xml-schedule-with-timezone`)*. | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| Schedule           | :ref:`single-xml-schedule-with-timezone` | Optional     | Repeats      | Structured schedule of operating dates and  | If the element is invalid or not         |
|                    |                                          |              |              | hours. Clearable in overlays.               | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LocationType       | :ref:`single-xml-polling-location-type`  | **Required** | Single       | The type of voting conducted at this        | LocationType is required for             |
|                    |                                          |              |              | location (InPersonDayOf, InPersonEarly, or  | PollingLocation in main feeds.           |
|                    |                                          |              |              | DropOff). Required in main feed; optional   |                                          |
|                    |                                          |              |              | in overlays.                                |                                          |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| LatLng             | :ref:`single-xml-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.         | If the element is invalid or not         |
|                    |                                          |              |              | Clearable in overlays.                      | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| PartyIds           | ``xs:IDREFS``                            | Optional     | Single       | If present, indicates which parties'        | If the field is invalid or not present,  |
|                    |                                          |              |              | primaries occur at this location. Clearable | then the implementation is required to   |
|                    |                                          |              |              | in overlays.                                | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| PhotoUri           | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | Link to a photo of the location. Clearable  | If the element is invalid or not         |
|                    |                                          |              |              | in overlays.                                | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| EmergencyNotice    | :ref:`single-xml-emergency-notice`       | Optional     | Repeats      | Emergency notice specific to this polling   | If the element is invalid or not         |
|                    |                                          |              |              | location. Permitted only in feed overlays.  | present, then the implementation is      |
|                    |                                          |              |              |                                             | required to ignore it.                   |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+
| IsInactive         | ``xs:string``                            | Optional     | Single       | If specified, marks the location as closed  | If the field is invalid or not present,  |
|                    |                                          |              |              | or inactive, with the text stating the      | then the implementation is required to   |
|                    |                                          |              |              | reason why. Clearable in overlays.          | ignore it.                               |
+--------------------+------------------------------------------+--------------+--------------+---------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl00001">
      <AddressStructured language="en">
         <LocationName>ALBEMARLE HIGH SCHOOL</LocationName>
         <AddressLine>2775 Hydraulic Rd</AddressLine>
         <City>CHARLOTTESVILLE</City>
         <Region>VA</Region>
         <PostalCode>22901</PostalCode>
      </AddressStructured>
      <LocationIdentifier provider="google" relativePriority="1.0">
         <Type>pluscode</Type>
         <Value>87G83W52+4F</Value>
      </LocationIdentifier>
      <LocationType>InPersonDayOf</LocationType>
      <Directions>
         <Text language="en">Use gymnasium entrance on east side.</Text>
      </Directions>
      <Schedule>
         <TimeZone>America/New_York</TimeZone>
         <StartDate>2024-11-05</StartDate>
         <EndDate>2024-11-05</EndDate>
         <Hours>
            <StartTime>06:00:00</StartTime>
            <EndTime>19:00:00</EndTime>
         </Hours>
      </Schedule>
      <LatLng>
         <Latitude>38.0754627</Latitude>
         <Longitude>-78.5014875</Longitude>
      </LatLng>
   </PollingLocation>


.. _single-xml-precinct:

Precinct
~~~~~~~~

The Precinct object represents a voting precinct or precinct split within a Locality.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearBallotStyleId/>``, ``<ClearPollingLocationIds/>``, ``<ClearIsInactive/>``). LocalityId and Name are optional in overlays. EmergencyNotice is permitted only in overlays.

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| BallotStyleId        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`single-xml-ballot-style` voted by  | then the implementation is required to   |
|                      |                                       |              |              | electors in this precinct. Clearable in  | ignore it.                               |
|                      |                                       |              |              | overlays.                                |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictIds | ``xs:IDREFS``                         | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`single-xml-electoral-district`     | then the implementation is required to   |
|                      |                                       |              |              | elements containing this precinct.       | ignore it.                               |
|                      |                                       |              |              | Clearable in overlays.                   |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier   | :ref:`single-xml-external-identifier` | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                      |                                       |              |              | precinct to other datasets (e.g.         | present, then the implementation is      |
|                      |                                       |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly           | ``xs:boolean``                        | Optional     | Single       | Specifies if this precinct conducts      | If the field is missing or invalid, the  |
|                      |                                       |              |              | mail-only elections. Clearable in        | implementation is required to assume     |
|                      |                                       |              |              | overlays.                                | IsMailOnly is false.                     |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId           | ``xs:IDREF``                          | **Required** | Single       | References the containing                | If LocalityId is invalid or not present, |
|                      |                                       |              |              | :ref:`single-xml-locality`. Required in  | the implementation is required to ignore |
|                      |                                       |              |              | main feed; optional in overlays.         | the Precinct containing it.              |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | ``xs:string``                         | **Required** | Single       | Name of the precinct. Required in main   | If Name is invalid or not present, the   |
|                      |                                       |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                      |                                       |              |              |                                          | Precinct containing it.                  |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number               | ``xs:string``                         | Optional     | Single       | Precinct number or code. Clearable in    | If the field is invalid or not present,  |
|                      |                                       |              |              | overlays.                                | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds   | ``xs:IDREFS``                         | Optional     | Single       | Links to polling locations serving this  | If the field is invalid or not present,  |
|                      |                                       |              |              | precinct. Clearable in overlays.         | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName    | ``xs:string``                         | Optional     | Single       | Sub-identifier for precinct splits.      | If the field is invalid or not present,  |
|                      |                                       |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SpatialBoundary      | :ref:`single-xml-spatial-boundary`    | Optional     | Single       | Geospatial boundary defining the         | If the element is invalid or not         |
|                      |                                       |              |              | precinct polygon. Clearable in overlays. | present, then the implementation is      |
|                      |                                       |              |              |                                          | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                 | ``xs:string``                         | Optional     | Single       | Ward identifier if applicable. Clearable | If the field is invalid or not present,  |
|                      |                                       |              |              | in overlays.                             | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EmergencyNotice      | :ref:`single-xml-emergency-notice`    | Optional     | Repeats      | Emergency notice specific to this        | If the element is invalid or not         |
|                      |                                       |              |              | precinct. Permitted only in feed         | present, then the implementation is      |
|                      |                                       |              |              | overlays.                                | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive           | ``xs:string``                         | Optional     | Single       | If specified, marks the precinct as      | If the field is invalid or not present,  |
|                      |                                       |              |              | inactive, stating the reason why.        | then the implementation is required to   |
|                      |                                       |              |              | Clearable in overlays.                   | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Precinct id="pre90111">
      <BallotStyleId>bs00010</BallotStyleId>
      <ElectoralDistrictIds>ed60129 ed60311</ElectoralDistrictIds>
      <IsMailOnly>false</IsMailOnly>
      <LocalityId>loc70001</LocalityId>
      <Name>203 - GEORGETOWN</Name>
      <Number>0203</Number>
      <PollingLocationIds>pl00001</PollingLocationIds>
   </Precinct>


.. _single-xml-spatial-boundary:

SpatialBoundary
^^^^^^^^^^^^^^^

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+---------------------------+-----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                       | Data Type                                     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===========================+===============================================+==============+==============+==========================================+==========================================+
| ExternalGeospatialFeature | :ref:`single-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                           |                                               |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                           |                                               |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                           |                                               |              |              |                                          | it.                                      |
+---------------------------+-----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <FeatureIdentifier>
          <Index>3</Index>
        </FeatureIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>


.. _single-xml-external-geospatial-feature:

ExternalGeospatialFeature
%%%%%%%%%%%%%%%%%%%%%%%%%

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+======================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                         | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                      |              |              | :ref:`single-xml-external-file`          | implementation is required to ignore the |
|                   |                                      |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`single-xml-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                      |              |              |                                          | implementation is required to ignore the |
|                   |                                      |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              |                                          | containing it.                           |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`single-xml-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    | If the element is invalid, then the      |
|                   |                                      |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                   |                                      |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              | the referenced external file. This is a  | containing it.                           |
|                   |                                      |              |              | repeated field in the XML specification, |                                          |
|                   |                                      |              |              | but a scalar field in the CSV            |                                          |
|                   |                                      |              |              | specification. If more than one          |                                          |
|                   |                                      |              |              | identifier is required with the CSV      |                                          |
|                   |                                      |              |              | specifiation, multiple values can be     |                                          |
|                   |                                      |              |              | provided by delimited by space.          |                                          |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-feature-identifier:

FeatureIdentifier
^^^^^^^^^^^^^^^^^

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Index        | ``xs:string`` | **Required** | Single       | The index value for the shapefile        | If the Index field is invalid or not     |
|              |               |              |              | feature.                                 | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the FeatureIdentifier          |
|              |               |              |              |                                          | containing it.                           |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-retention-contest:

RetentionContest
~~~~~~~~~~~~~~~~

``RetentionContest`` extends :ref:`single-xml-ballot-measure-contest` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| CandidateId  | ``xs:IDREF`` | **Required** | Single       | Links to the :ref:`single-xml-candidate` | If the field is invalid or not present,  |
|              |              |              |              | being retained.                          | the implementation is required to ignore |
|              |              |              |              |                                          | the ``RetentionContest`` element         |
|              |              |              |              |                                          | containing it.                           |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeId     | ``xs:IDREF`` | Optional     | Single       | Links to the information about the       | If the field is invalid or not present,  |
|              |              |              |              | office.                                  | then the implementation is required to   |
|              |              |              |              |                                          | ignore it.                               |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <RetentionContest id="rc40001">
      <BallotSelectionIds>rc40001a rc40001b</BallotSelectionIds>
      <BallotTitle>
         <Text language="en">Retention of Supreme Court Justice</Text>
         <Text language="es">La retención de juez de la Corte Suprema</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Judicial Retention, Supreme Court</Name>
      <CandidateId>can14444</CandidateId>
      <OfficeId>off20006</OfficeId>
   </RetentionContest>


.. _single-xml-schedule-with-timezone:

ScheduleWithTimezone
~~~~~~~~~~~~~~~~~~~~

Defines a schedule of dates and hours of operation with an optional IANA time zone. If the time zone is omitted, hours are assumed to be in the local time of the enclosing entity. ScheduleWithTimezone has an optional ``label`` attribute.

In overlay feeds, elements of type ScheduleWithTimezone are clearable using ``<ClearSchedule/>`` (or ``<ClearDefaultPollingHours/>``, etc. depending on the tag name).

+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================+==============+==============+==========================================+==========================================+
| TimeZone            | ``xs:string``           | Optional     | Single       | The named IANA time zone (e.g.           | If the field is invalid or not present,  |
|                     |                         |              |              | "America/New_York", "Etc/UTC",           | then the implementation is required to   |
|                     |                         |              |              | "Etc/GMT+1"). Must match canonical       | ignore it.                               |
|                     |                         |              |              | Continent/City format. If not present,   |                                          |
|                     |                         |              |              | hours are assumed to be in local time.   |                                          |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate           | ``xs:date``             | Optional     | Single       | The date on which this schedule begins.  | If the field is invalid or not present,  |
|                     |                         |              |              |                                          | then the implementation is required to   |
|                     |                         |              |              |                                          | ignore it.                               |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate             | ``xs:date``             | Optional     | Single       | The date on which this schedule ends.    | If the field is invalid or not present,  |
|                     |                         |              |              |                                          | then the implementation is required to   |
|                     |                         |              |              |                                          | ignore it.                               |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours               | :ref:`single-xml-hours` | Optional     | Repeats      | Blocks of hours during which the         | If the element is invalid or not         |
|                     |                         |              |              | location is open on days in the date     | present, then the implementation is      |
|                     |                         |              |              | range.                                   | required to ignore it.                   |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOpen24Hours       | ``xs:boolean``          | Optional     | Single       | Indicates if the location is open 24     | If the field is invalid or not present,  |
|                     |                         |              |              | hours a day during this date range (e.g. | then the implementation is required to   |
|                     |                         |              |              | 24-hour ballot drop boxes).              | ignore it.                               |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOnlyByAppointment | ``xs:boolean``          | Optional     | Single       | If true, the location is only open       | If the field is invalid or not present,  |
|                     |                         |              |              | during the specified window with an      | then the implementation is required to   |
|                     |                         |              |              | appointment.                             | ignore it.                               |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOrByAppointment   | ``xs:boolean``          | Optional     | Single       | If true, the location is open during the | If the field is invalid or not present,  |
|                     |                         |              |              | window and may also be open by           | then the implementation is required to   |
|                     |                         |              |              | appointment.                             | ignore it.                               |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsSubjectToChange   | ``xs:boolean``          | Optional     | Single       | If true, hours may be subject to change. | If the field is invalid or not present,  |
|                     |                         |              |              | Voters should verify prior to arrival.   | then the implementation is required to   |
|                     |                         |              |              |                                          | ignore it.                               |
+---------------------+-------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Schedule label="early_voting_week1">
      <TimeZone>America/New_York</TimeZone>
      <StartDate>2024-10-21</StartDate>
      <EndDate>2024-10-25</EndDate>
      <Hours>
         <StartTime>08:00:00</StartTime>
         <EndTime>17:00:00</EndTime>
      </Hours>
      <IsOpen24Hours>false</IsOpen24Hours>
      <IsOnlyByAppointment>false</IsOnlyByAppointment>
      <IsOrByAppointment>false</IsOrByAppointment>
      <IsSubjectToChange>false</IsSubjectToChange>
   </Schedule>


.. _single-xml-hours:

Hours
^^^^^

The open and close time for a location. Times must be fully specified without time zone information. The time zone is specified in the containing :ref:`single-xml-schedule-with-timezone` element. Hours has an optional ``label`` attribute.

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| StartTime    | :ref:`single-xml-time-without-zone` | **Required** | Single       | The time at which the location opens.    | If StartTime is invalid or not present,  |
|              |                                     |              |              |                                          | the implementation is required to ignore |
|              |                                     |              |              |                                          | the Hours element containing it.         |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | :ref:`single-xml-time-without-zone` | **Required** | Single       | The time at which the location closes.   | If EndTime is invalid or not present,    |
|              |                                     |              |              |                                          | the implementation is required to ignore |
|              |                                     |              |              |                                          | the Hours element containing it.         |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-time-without-zone:

TimeWithoutZone
%%%%%%%%%%%%%%%

A time value with no time zone. The time zone is specified in an enclosing structure, such as a :ref:`single-xml-schedule-with-timezone` element. The pattern is:

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))``

.. code-block:: xml
   :linenos:

   <Schedule>
      <TimeZone>America/New_York</TimeZone>
      <Hours>
         <StartTime>06:00:00</StartTime>
         <EndTime>19:00:00</EndTime>
      </Hours>
      <StartDate>2024-11-05</StartDate>
      <EndDate>2024-11-05</EndDate>
   </Schedule>


.. _single-xml-simple-address-type:

SimpleAddressType
~~~~~~~~~~~~~~~~~

A ``SimpleAddressType`` represents a structured physical or mailing address. It has an optional attribute, ``language``, which defaults to ``i-default``.

When multiple ``SimpleAddressType`` elements are provided on an entity (such as ``AddressStructured`` on a polling location, or ``MailingAddress`` / ``PhysicalAddress`` on contact information), each must have a distinct ``language`` attribute to specify the address in multiple languages.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| LocationName | ``xs:string`` | Optional     | Single       | The name of the location or facility     | If the field is invalid or not present,  |
|              |               |              |              | (e.g. "Albemarle High School").          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AddressLine  | ``xs:string`` | **Required** | Repeats      | Street address line(s). Multiple         | If no AddressLine is provided, the       |
|              |               |              |              | AddressLine tags may appear in order     | implementation should ignore the         |
|              |               |              |              | (e.g. street address, suite/room).       | SimpleAddressType containing it.         |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | Optional     | Single       | The city, town, or municipality.         | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| County       | ``xs:string`` | Optional     | Single       | The county or parish.                    | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Region       | ``xs:string`` | Optional     | Single       | The state, province, or primary          | If the field is invalid or not present,  |
|              |               |              |              | sub-national region (e.g. "VA").         | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Country      | ``xs:string`` | Optional     | Single       | The country (e.g. "USA").                | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WorldRegion  | ``xs:string`` | Optional     | Single       | Global or continental region if          | If the field is invalid or not present,  |
|              |               |              |              | applicable.                              | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostalCode   | ``xs:string`` | Optional     | Single       | The postal code or ZIP code.             | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <AddressStructured language="en">
      <LocationName>Albemarle High School</LocationName>
      <AddressLine>2775 Hydraulic Rd</AddressLine>
      <City>Charlottesville</City>
      <County>Albemarle</County>
      <Region>VA</Region>
      <Country>USA</Country>
      <PostalCode>22901</PostalCode>
   </AddressStructured>


.. _single-xml-source:

Source
~~~~~~

The Source object represents the organization publishing the information. In a VIP 7.0 main feed file, exactly one Source object must be present. Source is excluded from feed overlays.

+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+==========================================+==============+==============+==========================================+==========================================+
| DateTime               | ``xs:dateTime``                          | **Required** | Single       | Specifies the date and time of feed      | If the field is invalid, then the        |
|                        |                                          |              |              | production in local time.                | implementation is required to ignore the |
|                        |                                          |              |              |                                          | ``Source`` element containing it.        |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description            | :ref:`single-xml-internationalized-text` | Optional     | Single       | Describes the organization and the data  | If the element is invalid or not         |
|                        |                                          |              |              | contained in the feed.                   | present, then the implementation is      |
|                        |                                          |              |              |                                          | required to ignore it.                   |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactInformation | :ref:`single-xml-contact-information`    | Optional     | Single       | Contact information for inquiries about  | If the element is invalid or not         |
|                        |                                          |              |              | the feed data.                           | present, then the implementation is      |
|                        |                                          |              |              |                                          | required to ignore it.                   |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                   | ``xs:string``                            | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                        |                                          |              |              | publishing the feed.                     | implementation is required to ignore the |
|                        |                                          |              |              |                                          | ``Source`` element containing it.        |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri        | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | Web address of the organization          | If the element is invalid or not         |
|                        |                                          |              |              | publishing the feed.                     | present, then the implementation is      |
|                        |                                          |              |              |                                          | required to ignore it.                   |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TermsOfUseUri          | :ref:`single-xml-internationalized-uri`  | Optional     | Single       | Web address where Terms of Use for the   | If the element is invalid or not         |
|                        |                                          |              |              | feed data can be found.                  | present, then the implementation is      |
|                        |                                          |              |              |                                          | required to ignore it.                   |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId                  | ``xs:string``                            | **Required** | Single       | FIPS code identifying the state or       | If the field is invalid, then the        |
|                        |                                          |              |              | jurisdiction.                            | implementation is required to ignore the |
|                        |                                          |              |              |                                          | ``Source`` element containing it.        |
+------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _FIPS: https://www.census.gov/geo/reference/codes/cou.html

.. code-block:: xml
   :linenos:

   <Source id="src1">
      <DateTime>2024-10-24T14:25:28</DateTime>
      <Description>
         <Text language="en">SBE is the official source for Virginia election data.</Text>
      </Description>
      <FeedContactInformation>
         <Name>State Board of Elections Support</Name>
         <Email>elections@sbe.virginia.gov</Email>
      </FeedContactInformation>
      <Name>State Board of Elections, Commonwealth of Virginia</Name>
      <OrganizationUri>http://www.sbe.virginia.gov/</OrganizationUri>
      <TermsOfUseUri>http://www.sbe.virginia.gov/terms</TermsOfUseUri>
      <VipId>51</VipId>
   </Source>


.. _single-xml-spatial-boundary:

SpatialBoundary
~~~~~~~~~~~~~~~

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+---------------------------+-----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                       | Data Type                                     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===========================+===============================================+==============+==============+==========================================+==========================================+
| ExternalGeospatialFeature | :ref:`single-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                           |                                               |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                           |                                               |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                           |                                               |              |              |                                          | it.                                      |
+---------------------------+-----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <FeatureIdentifier>
          <Index>3</Index>
        </FeatureIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>


.. _single-xml-external-geospatial-feature:

ExternalGeospatialFeature
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+======================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                         | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                      |              |              | :ref:`single-xml-external-file`          | implementation is required to ignore the |
|                   |                                      |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`single-xml-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                      |              |              |                                          | implementation is required to ignore the |
|                   |                                      |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              |                                          | containing it.                           |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`single-xml-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    | If the element is invalid, then the      |
|                   |                                      |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                   |                                      |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                   |                                      |              |              | the referenced external file. This is a  | containing it.                           |
|                   |                                      |              |              | repeated field in the XML specification, |                                          |
|                   |                                      |              |              | but a scalar field in the CSV            |                                          |
|                   |                                      |              |              | specification. If more than one          |                                          |
|                   |                                      |              |              | identifier is required with the CSV      |                                          |
|                   |                                      |              |              | specifiation, multiple values can be     |                                          |
|                   |                                      |              |              | provided by delimited by space.          |                                          |
+-------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-feature-identifier:

FeatureIdentifier
%%%%%%%%%%%%%%%%%

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Index        | ``xs:string`` | **Required** | Single       | The index value for the shapefile        | If the Index field is invalid or not     |
|              |               |              |              | feature.                                 | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the FeatureIdentifier          |
|              |               |              |              |                                          | containing it.                           |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-street-segment:

StreetSegment
~~~~~~~~~~~~~

A StreetSegment object represents a range of house numbers along a street and links them to the containing :ref:`single-xml-precinct`. Street segments are excluded from feed overlays.

+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                  | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+============================+==============+==============+==========================================+==========================================+
| AddressDirection     | ``xs:string``              | Optional     | Single       | Specifies trailing directional component | If the field is invalid or not present,  |
|                      |                            |              |              | of the address (e.g. "NE").              | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City                 | ``xs:string``              | **Required** | Single       | City or municipality name.               | If the field is invalid, then the        |
|                      |                            |              |              |                                          | implementation is required to ignore the |
|                      |                            |              |              |                                          | ``StreetSegment`` element containing it. |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllAddresses | ``xs:boolean``             | Optional     | Single       | If true, the segment covers all          | If the field is invalid or not present,  |
|                      |                            |              |              | addresses on this street. OddEvenBoth    | then the implementation is required to   |
|                      |                            |              |              | must be "both".                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllStreets   | ``xs:boolean``             | Optional     | Single       | If true, covers all streets in the city. | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OddEvenBoth          | :ref:`single-xml-oeb-enum` | **Required** | Single       | Specifies whether odd, even, or both     | If OddEvenBoth is missing or invalid,    |
|                      |                            |              |              | sides of the street are included from    | the implementation is required to ignore |
|                      |                            |              |              | :ref:`single-xml-oeb-enum`.              | the StreetSegment containing it.         |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctId           | ``xs:IDREF``               | **Required** | Single       | References the containing                | If the field is invalid, then the        |
|                      |                            |              |              | :ref:`single-xml-precinct`.              | implementation is required to ignore the |
|                      |                            |              |              |                                          | ``StreetSegment`` element containing it. |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartHouseNumber     | ``xs:integer``             | Optional     | Single       | Starting house number for the segment    | If the field is invalid or not present,  |
|                      |                            |              |              | range.                                   | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndHouseNumber       | ``xs:integer``             | Optional     | Single       | Ending house number for the segment      | If the field is invalid or not present,  |
|                      |                            |              |              | range.                                   | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HouseNumberPrefix    | ``xs:string``              | Optional     | Single       | Prefix to the house number if any.       | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HouseNumberSuffix    | ``xs:string``              | Optional     | Single       | Suffix to the house number if any.       | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Region               | ``xs:string``              | **Required** | Single       | State, province, or primary sub-national | If the field is invalid, then the        |
|                      |                            |              |              | region (e.g. "VA").                      | implementation is required to ignore the |
|                      |                            |              |              |                                          | ``StreetSegment`` element containing it. |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Country              | ``xs:string``              | Optional     | Single       | Country code or name (e.g. "USA").       | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection      | ``xs:string``              | Optional     | Single       | Leading directional prefix for the       | If the field is invalid or not present,  |
|                      |                            |              |              | street (e.g. "N", "NW").                 | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName           | ``xs:string``              | Optional     | Single       | Street name.                             | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix         | ``xs:string``              | Optional     | Single       | Street type suffix (e.g. "St", "Ave",    | If the field is invalid or not present,  |
|                      |                            |              |              | "Rd").                                   | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| UnitNumber           | ``xs:string``              | Optional     | Repeats      | Unit, apartment, or suite number(s).     | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostalCode           | ``xs:string``              | Optional     | Single       | Postal code or ZIP code.                 | If the field is invalid or not present,  |
|                      |                            |              |              |                                          | then the implementation is required to   |
|                      |                            |              |              |                                          | ignore it.                               |
+----------------------+----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <StreetSegment id="ss999999">
      <City>Charlottesville</City>
      <IncludesAllAddresses>true</IncludesAllAddresses>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre99999</PrecinctId>
      <Region>VA</Region>
      <Country>USA</Country>
      <StreetName>CHAPEL HILL</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <PostalCode>22901</PostalCode>
   </StreetSegment>


.. _single-xml-term:

Term
~~~~

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`single-xml-office-term-type` | Optional     | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              |                                    |              |              | :ref:`single-xml-office-term-type` for   | the implementation is required to ignore |
|              |                                    |              |              | valid values).                           | the ``Office`` element containing it.    |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | ``xs:date``                        | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                    |              |              | term of the office.                      | then the implementation is required to   |
|              |                                    |              |              |                                          | ignore it.                               |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | ``xs:date``                        | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                    |              |              | term of the office.                      | then the implementation is required to   |
|              |                                    |              |              |                                          | ignore it.                               |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Office id="off0000">
     <ElectoralDistrictId>ed60129</ElectoralDistrictId>
     <FilingDeadline>2013-01-01</FilingDeadline>
     <IsPartisan>false</IsPartisan>
     <Name>
       <Text language="en">Governor</Text>
     </Name>
     <Term>
       <Type>full-term</Type>
     </Term>
   </Office>


.. _single-xml-time-without-zone:

TimeWithoutZone
~~~~~~~~~~~~~~~

A time value with no time zone. The time zone is specified in an enclosing structure, such as a :ref:`single-xml-schedule-with-timezone` element. The pattern is:

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))``

.. code-block:: xml
   :linenos:

   <Schedule>
      <TimeZone>America/New_York</TimeZone>
      <Hours>
         <StartTime>06:00:00</StartTime>
         <EndTime>19:00:00</EndTime>
      </Hours>
      <StartDate>2024-11-05</StartDate>
      <EndDate>2024-11-05</EndDate>
   </Schedule>


.. _single-xml-voter-service:

VoterService
~~~~~~~~~~~~

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`single-xml-contact-information`    | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          |                                          |              |              | service.                                 | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :ref:`single-xml-internationalized-text` | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          |                                          |              |              | available.                               | present, then the implementation is      |
|                          |                                          |              |              |                                          | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                             | Optional     | Single       | The :ref:`authority <single-xml-person>` | If the field is invalid or not present,  |
|                          |                                          |              |              | for a particular voter service.          | then the implementation is required to   |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`single-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                          |                                          |              |              | <single-xml-voter-service-type>`.        | then the implementation is required to   |
|                          |                                          |              |              |                                          | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                            | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                          |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                          |              |              | service.                                 | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-enumerations:

Enumerations
------------


.. _single-xml-ballot-measure-type:

BallotMeasureType
~~~~~~~~~~~~~~~~~

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

.. _Wikipedia: http://en.wikipedia.org/wiki/Initiatives_and_referendums_in_the_United_States


.. _single-xml-candidate-post-election-status:

CandidatePostElectionStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


.. _single-xml-candidate-pre-election-status:

CandidatePreElectionStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~

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


.. _single-xml-checksum-algorithm:

ChecksumAlgorithm
~~~~~~~~~~~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| sha-256      | 256-bit cryptographic hash algorithm of the SHA-2  |
|              | family                                             |
+--------------+----------------------------------------------------+
| sha-512      | 512-bit cryptographic hash algorithm of the SHA-2  |
|              | family                                             |
+--------------+----------------------------------------------------+


.. _single-xml-district-type:

DistrictType
~~~~~~~~~~~~

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

.. _`special-purpose district`: http://en.wikipedia.org/wiki/Special-purpose_district
.. _town: http://en.wikipedia.org/wiki/Town#United_States
.. _`Wikipedia article`: http://en.wikipedia.org/wiki/Town#United_States


.. _single-xml-geospatial-format:

GeospatialFormat
~~~~~~~~~~~~~~~~

Geospatial file formats that are supported by the VIP specification.

+--------------+---------------------------------------------------------------------------+
| Tag          | Description                                                               |
+==============+===========================================================================+
| shp          | ESRI Shapefile (`reference                                                |
|              | <https://www.loc.gov/preservation/digital/formats/fdd/fdd000280.shtml>`_) |
+--------------+---------------------------------------------------------------------------+


.. _single-xml-identifier-type:

IdentifierType
~~~~~~~~~~~~~~

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

.. _states: http://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code
.. _counties: http://en.wikipedia.org/wiki/FIPS_county_code
.. _cities: http://geonames.usgs.gov/domestic/fips55codedef.html
.. _`Open Civic Data Division Identifier`: http://docs.opencivicdata.org/en/latest/proposals/0002.html

ExternalIdentifier has optional attributes:

  - ``label``: Optional label for tracking purposes.
  - ``provider``: Optional source of the information, such as the department or authority that provided the identifier.


.. _single-xml-location-identifier-type:

LocationIdentifierType
~~~~~~~~~~~~~~~~~~~~~~

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


.. _single-xml-oeb-enum:

OebEnum
~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| both         | Both even and odd addresses within the range.      |
+--------------+----------------------------------------------------+
| even         | Only even-numbered addresses within the range.     |
+--------------+----------------------------------------------------+
| odd          | Only odd-numbered addresses within the range.      |
+--------------+----------------------------------------------------+


.. _single-xml-office-term-type:

OfficeTermType
~~~~~~~~~~~~~~

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| full-term      | This election is for an office for which the       |
|                | existing term has been completed.                  |
+----------------+----------------------------------------------------+
| unexpired-term | This election is for an office for which the       |
|                | original term is not yet complete.                 |
+----------------+----------------------------------------------------+


.. _single-xml-polling-location-type:

PollingLocationType
~~~~~~~~~~~~~~~~~~~

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


.. _single-xml-vote-variation:

VoteVariation
~~~~~~~~~~~~~

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

.. _`Approval voting`: http://en.wikipedia.org/wiki/Approval_voting
.. _`Borda count`: http://en.wikipedia.org/wiki/Borda_count
.. _`Cumulative voting`: http://en.wikipedia.org/wiki/Cumulative_voting
.. _`proportional representation`: https://en.wikipedia.org/wiki/Proportional_representation
.. _`Range voting`: http://en.wikipedia.org/wiki/Range_voting
.. _`Ranked choice voting`: http://http://en.wikipedia.org/wiki/Ranked_Choice_Voting


.. _single-xml-voter-service-type:

VoterServiceType
~~~~~~~~~~~~~~~~

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
