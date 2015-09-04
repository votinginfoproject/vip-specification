BallotMeasureSelection
======================

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:doc:`BallotMeasureContest <ballot_measure_contest>` that would appear on the ballot.
BallotMeasureSelection extends :doc:`BallotSelectionBase <ballot_selection_base>`.

.. include:: ../../tables/elements/ballot_measure_selection.rst

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
