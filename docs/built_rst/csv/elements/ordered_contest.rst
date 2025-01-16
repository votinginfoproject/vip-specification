.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ordered-contest:

ordered_contest
===============

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:ref:`multi-csv-ballot-style` to accurate depict exactly what will show up on a particular
ballot in the proper order.

+------------------------------+--------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
| Tag                          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                                  |
+==============================+==============+==============+==============+==========================================+=================================================+
| contest_id                   | ``xs:IDREF`` | **Required** | Single       | Links to elements that extend            |                                                 |
|                              |              |              |              | :ref:`multi-csv-contest-base`.           |                                                 |
+------------------------------+--------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
| ordered_ballot_selection_ids | ``IDREFS``   | Optional     | Single       | Links to elements that extend            | If the field is invalid or not present, the     |
|                              |              |              |              | :ref:`multi-csv-ballot-selection-base`.  | implementation is required to ignore it. If an  |
|                              |              |              |              |                                          | ``OrderedBallotSelectionIds`` element is not    |
|                              |              |              |              |                                          | present, the presumed order of the selection    |
|                              |              |              |              |                                          | will be the order of                            |
|                              |              |              |              |                                          | :ref:`multi-csv-ballot-selection-base`-extended |
|                              |              |              |              |                                          | elements referenced by the underlying           |
|                              |              |              |              |                                          | :ref:`multi-csv-contest-base`-extended          |
|                              |              |              |              |                                          | elements.                                       |
+------------------------------+--------------+--------------+--------------+------------------------------------------+-------------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,contest_id,ordered_ballot_selection_ids
    oc2025,con001,bs001 bs002 bs003
    oc3000,con002,bs001
