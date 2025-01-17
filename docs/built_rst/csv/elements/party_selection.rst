.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party-selection:

party_selection
===============

This element extends :ref:`multi-csv-ballot-selection-base` to
support contests in which the selections can be groups of one or more parties.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| party_ids    | ``xs:IDREFS`` | **Required** | Single       | One or more :ref:`multi-csv-party` IDs   | If one or more parties referenced are    |
|              |               |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |               |              |              | selection.                               | implementation is required to ignore the |
|              |               |              |              |                                          | PartySelection containing it.            |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,sequence_order,party_ids
    ps001,1,par01 par04
    ps002,2,par02
    ps003,3,par03


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
