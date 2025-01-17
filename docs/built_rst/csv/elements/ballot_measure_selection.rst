.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ballot-measure-selection:

ballot_measure_selection
========================

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:ref:`multi-csv-ballot-measure-contest` that would appear on the ballot.
BallotMeasureSelection extends :ref:`multi-csv-ballot-selection-base`.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| selection    | ``xs:string`` | **Required** | Single       | Selection text for a                     |                                          |
|              |               |              |              | :ref:`multi-csv-ballot-measure-contest`  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,sequence_order,selection
    bms001,1,Proposition A
    bms002,2,Proposition B


.. _multi-csv-ballot-selection-base:

ballot_selection_base
---------------------

A base model for all ballot selection types:
:ref:`multi-csv-ballot-measure-selection`,
:ref:`multi-csv-candidate-selection`, and :ref:`multi-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    |                                          |
|                |                |              |              | listed on the ballot or in results. This |                                          |
|                |                |              |              | is the default ordering, and can be      |                                          |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`multi-csv-ordered-contest`.     |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
