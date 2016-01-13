.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-measure-selection:

BallotMeasureSelection
======================

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:ref:`single-xml-ballot-measure-contest` that would appear on the ballot.
BallotMeasureSelection extends :ref:`single-xml-ballot-selection-base`.

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| Selection    | :ref:`multi-xml-internationalized-text` | **Required** | Single       | Selection text for a                     | If the element is invalid or not         |
|              |                                         |              |              | :ref:`single-xml-ballot-measure-contest` | present, the implementation is required  |
|              |                                         |              |              |                                          | to ignore the BallotMeasureSelection     |
|              |                                         |              |              |                                          | containing it.                           |
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
