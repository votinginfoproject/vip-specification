.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-candidate-selection:

candidate_selection
===================

CandidateSelection extends :ref:`multi-csv-ballot-selection-base` and represents a
ballot selection for a candidate contest.

+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+================+==============+==============+==========================================+==========================================+
| candidate_ids         | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                       |                |              |              | :ref:`multi-csv-candidate` elements. The |                                          |
|                       |                |              |              | number of candidates that can be         |                                          |
|                       |                |              |              | references is unbounded in cases where   |                                          |
|                       |                |              |              | the ballot selection is for a ticket     |                                          |
|                       |                |              |              | (e.g. "President/Vice President",        |                                          |
|                       |                |              |              | "Governor/Lt Governor").                 |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| endorsement_party_ids | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                       |                |              |              | :ref:`multi-csv-party` elements, which   |                                          |
|                       |                |              |              | signifies one or more endorsing parties  |                                          |
|                       |                |              |              | for the candidate(s).                    |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in           | ``xs:boolean`` | Optional     | Single       | Signifies if the particular ballot       |                                          |
|                       |                |              |              | selection allows for write-in            |                                          |
|                       |                |              |              | candidates. If true, one or more         |                                          |
|                       |                |              |              | write-in candidates are allowed for this |                                          |
|                       |                |              |              | contest.                                 |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,sequence_order,candidate_ids,endorsement_party_ids,is_write_in
    cs001,3,can004,par01,false
    cs002,2,can001 can002,par03 par02,false
    cs003,1,can003,par02 par03,true


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
