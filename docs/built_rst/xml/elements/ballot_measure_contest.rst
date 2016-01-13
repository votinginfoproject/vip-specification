.. This file is auto-generated.  Do not edit it by hand!

.. _xml-multi-ballot-measure-contest:

BallotMeasureContest
====================

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends :doc:`ContestBase <contest_base>`.

+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :doc:`InternationalizedText            | Optional     | Single       | Specifies a statement in opposition to   | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | the referendum. It does not necessarily  | present, then the implementation is      |
|                  |                                        |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :doc:`InternationalizedText            | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | not voting) on this proposition will     | present, then the implementation is      |
|                  |                                        |              |              | have (i.e. whether abstaining is         | required to ignore it.                   |
|                  |                                        |              |              | considered a vote against it).           |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :doc:`InternationalizedText            | Optional     | Single       | Specifies the full text of the           | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum as it appears on the ballot.  | present, then the implementation is      |
|                  |                                        |              |              |                                          | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | xs:anyURI                              | Optional     | Single       | Specifies a URI that links to additional | If the field is invalid or not present,  |
|                  |                                        |              |              | information about the referendum.        | then the implementation is required to   |
|                  |                                        |              |              |                                          | ignore it.                               |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :doc:`InternationalizedText            | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                  |                                        |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                  |                                        |              |              | 50% plus one vote). Other common         |                                          |
|                  |                                        |              |              | thresholds are "three-fifths" and        |                                          |
|                  |                                        |              |              | "two-thirds". If there are `competing    |                                          |
|                  |                                        |              |              | initiatives`_, information about their   |                                          |
|                  |                                        |              |              | effect on the passage of the             |                                          |
|                  |                                        |              |              | BallotMeasureContest would go here.      |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :doc:`InternationalizedText            | Optional     | Single       | Specifies a statement in favor of the    | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum. It does not necessarily      | present, then the implementation is      |
|                  |                                        |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :doc:`InternationalizedText            | Optional     | Single       | Specifies a short summary of the         | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum that is on the ballot, below  | present, then the implementation is      |
|                  |                                        |              |              | the title, but above the text.           | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :doc:`BallotMeasureType                | Optional     | Single       | Specifies the particular type of ballot  | If the field is invalid or not present,  |
|                  | <../enumerations/ballot_measure_type>` |              |              | measure. Must be one of the valid        | then the implementation is required to   |
|                  |                                        |              |              | :doc:`BallotMeasureType                  | ignore it.                               |
|                  |                                        |              |              | <../enumerations/ballot_measure_type>`   |                                          |
|                  |                                        |              |              | options.                                 |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | xs:string                              | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                  |                                        |              |              | :doc:`BallotMeasureType                  | then the implementation is required to   |
|                  |                                        |              |              | <../enumerations/ballot_measure_type>`   | ignore it.                               |
|                  |                                        |              |              | option, when Type is specified as        |                                          |
|                  |                                        |              |              | "other."                                 |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotMeasureContest id="bmc30001">
      <BallotSelectionId>bms30001a</BallotSelectionId>
      <BallotSelectionId>bms30001b</BallotSelectionId>
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
