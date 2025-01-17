.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-measure-selection:

BallotMeasureSelection
======================

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:ref:`multi-xml-ballot-measure-contest` that would appear on the ballot.
BallotMeasureSelection extends :ref:`multi-xml-ballot-selection-base`.

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| Selection    | :ref:`multi-xml-internationalized-text` | **Required** | Single       | Selection text for a                     |                                          |
|              |                                         |              |              | :ref:`multi-xml-ballot-measure-contest`  |                                          |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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


.. _multi-xml-ballot-selection-base:

BallotSelectionBase
-------------------

A base model for all ballot selection types:
:ref:`multi-xml-ballot-measure-selection`,
:ref:`multi-xml-candidate-selection`, and :ref:`multi-xml-party-selection`.

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    |                                          |
|               |                |              |              | listed on the ballot or in results. This |                                          |
|               |                |              |              | is the default ordering, and can be      |                                          |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`multi-xml-ordered-contest`.     |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
