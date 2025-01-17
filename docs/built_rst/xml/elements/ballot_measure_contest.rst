.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-measure-contest:

BallotMeasureContest
====================

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends :ref:`multi-xml-contest-base`.

+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a statement in opposition to   |                                          |
|                  |                                         |              |              | the referendum. It does not necessarily  |                                          |
|                  |                                         |              |              | appear on the ballot.                    |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies what effect abstaining (i.e.   |                                          |
|                  |                                         |              |              | not voting) on this proposition will     |                                          |
|                  |                                         |              |              | have (i.e. whether abstaining is         |                                          |
|                  |                                         |              |              | considered a vote against it).           |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the full text of the           |                                          |
|                  |                                         |              |              | referendum as it appears on the ballot.  |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | ``xs:anyURI``                           | Optional     | Single       | Specifies a URI that links to additional |                                          |
|                  |                                         |              |              | information about the referendum.        |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the threshold of votes that    |                                          |
|                  |                                         |              |              | the referendum needs in order to pass.   |                                          |
|                  |                                         |              |              | The default is a simple majority (i.e.   |                                          |
|                  |                                         |              |              | 50% plus one vote). Other common         |                                          |
|                  |                                         |              |              | thresholds are "three-fifths" and        |                                          |
|                  |                                         |              |              | "two-thirds". If there are `competing    |                                          |
|                  |                                         |              |              | initiatives`_, information about their   |                                          |
|                  |                                         |              |              | effect on the passage of the             |                                          |
|                  |                                         |              |              | BallotMeasureContest would go here.      |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a statement in favor of the    |                                          |
|                  |                                         |              |              | referendum. It does not necessarily      |                                          |
|                  |                                         |              |              | appear on the ballot.                    |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a short summary of the         |                                          |
|                  |                                         |              |              | referendum that is on the ballot, below  |                                          |
|                  |                                         |              |              | the title, but above the text.           |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :ref:`multi-xml-ballot-measure-type`    | Optional     | Single       | Specifies the particular type of ballot  |                                          |
|                  |                                         |              |              | measure. Must be one of the valid        |                                          |
|                  |                                         |              |              | :ref:`multi-xml-ballot-measure-type`     |                                          |
|                  |                                         |              |              | options.                                 |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | ``xs:string``                           | Optional     | Single       | Allows for cataloging a new              |                                          |
|                  |                                         |              |              | :ref:`multi-xml-ballot-measure-type`     |                                          |
|                  |                                         |              |              | option, when Type is specified as        |                                          |
|                  |                                         |              |              | "other."                                 |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotMeasureContest id="bmc30001">
      <BallotSelectionIds>bms30001a bms30001b</BallotSelectionIds>
      <BallotTitle>
         <Text language="en">State of the State</Text>
         <Text language="es">Estado del Estado.</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Referendum on Virginia</Name>
      <ConStatement label="bmc30001con">
         <Text language="en">This is no good.</Text>
         <Text language="es">Esto no es bueno.</Text>
      </ConStatement>
      <EffectOfAbstain label="bmc30001abs">
         <Text language="en">Nothing will happen.</Text>
         <Text language="es">Nada pasará.</Text>
      </EffectOfAbstain>
      <ProStatement label="bmc30001pro">
         <Text language="en">Everything will be great.</Text>
         <Text language="es">Todo va a estar bien.</Text>
      </ProStatement>
      <Type>referendum</Type>
   </BallotMeasureContest>

.. _competing initiatives: http://ballotpedia.org/Laws_governing_the_initiative_process_in_California#Competing_initiatives


.. _multi-xml-contest-base:

ContestBase
-----------

A base model for all Contest types: :ref:`multi-xml-ballot-measure-contest`,
:ref:`multi-xml-candidate-contest`, :ref:`multi-xml-party-contest`,
and :ref:`multi-xml-retention-contest` (NB: the latter because it extends
:ref:`multi-xml-ballot-measure-contest`).

+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                     | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=========================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation            | ``xs:string``                           | Optional     | Single       | An abbreviation for the contest.         |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSelectionIds      | ``xs:IDREFS``                           | Optional     | Single       | References a set of BallotSelections,    |                                          |
|                         |                                         |              |              | which could be of any selection type     |                                          |
|                         |                                         |              |              | that extends                             |                                          |
|                         |                                         |              |              | :ref:`multi-xml-ballot-selection-base`.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotSubTitle          | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Subtitle of the contest as it appears on |                                          |
|                         |                                         |              |              | the ballot.                              |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| BallotTitle             | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Title of the contest as it appears on    |                                          |
|                         |                                         |              |              | the ballot.                              |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | ``xs:IDREF``                            | **Required** | Single       | References an                            |                                          |
|                         |                                         |              |              | :ref:`multi-xml-electoral-district`      |                                          |
|                         |                                         |              |              | element that represents the geographical |                                          |
|                         |                                         |              |              | scope of the contest.                    |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectorateSpecification | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies any changes to the eligible    |                                          |
|                         |                                         |              |              | electorate for this contest past the     |                                          |
|                         |                                         |              |              | usual, "all registered voters"           |                                          |
|                         |                                         |              |              | electorate. This subtag will most often  |                                          |
|                         |                                         |              |              | be used for primaries and local          |                                          |
|                         |                                         |              |              | elections. In primaries, voters may have |                                          |
|                         |                                         |              |              | to be registered as a specific party to  |                                          |
|                         |                                         |              |              | vote, or there may be special rules for  |                                          |
|                         |                                         |              |              | which ballot a voter can pull. In some   |                                          |
|                         |                                         |              |              | local elections, non-citizens can vote.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers for a contest that     |                                          |
|                         |                                         |              |              | links to another source of information.  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasRotation             | ``xs:boolean``                          | Optional     | Single       | Indicates whether the selections in the  |                                          |
|                         |                                         |              |              | contest are rotated.                     |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                    | ``xs:string``                           | **Required** | Single       | Name of the contest, not necessarily how |                                          |
|                         |                                         |              |              | it appears on the ballot (NB:            |                                          |
|                         |                                         |              |              | BallotTitle should be used for this      |                                          |
|                         |                                         |              |              | purpose).                                |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder           | ``xs:integer``                          | Optional     | Single       | Order in which the contests are listed   |                                          |
|                         |                                         |              |              | on the ballot. This is the default       |                                          |
|                         |                                         |              |              | ordering, and can be overrides by data   |                                          |
|                         |                                         |              |              | in a :ref:`multi-xml-ballot-style`       |                                          |
|                         |                                         |              |              | element.                                 |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoteVariation           | :ref:`multi-xml-vote-variation`         | Optional     | Single       | Vote variation associated with the       |                                          |
|                         |                                         |              |              | contest (e.g. n-of-m, majority, et al).  |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherVoteVariation      | ``xs:string``                           | Optional     | Single       | If "other" is selected as the            |                                          |
|                         |                                         |              |              | **VoteVariation**, the name of the       |                                          |
|                         |                                         |              |              | variation can be specified here.         |                                          |
+-------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
