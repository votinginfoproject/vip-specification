.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-candidate-selection:

candidate_selection
===================

CandidateSelection extends :ref:`multi-csv-ballot-selection-base` and represents a ballot selection for one or more candidates in a candidate contest.

+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+================+==============+==============+==========================================+==========================================+
| candidate_ids         | ``xs:IDREFS``  | **Required** | Single       | References a set of                      | If CandidateIds is invalid or not        |
|                       |                |              |              | :ref:`multi-csv-candidate` elements. The | present, the implementation is required  |
|                       |                |              |              | number of candidates that can be         | to ignore the CandidateSelection         |
|                       |                |              |              | referenced is unbounded in cases where   | containing it.                           |
|                       |                |              |              | the ballot selection is for a ticket     |                                          |
|                       |                |              |              | (e.g. "President/Vice President",        |                                          |
|                       |                |              |              | "Governor/Lt Governor").                 |                                          |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| endorsement_party_ids | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-csv-party`        | If the field is invalid or not present,  |
|                       |                |              |              | elements endorsing this candidate        | then the implementation is required to   |
|                       |                |              |              | selection.                               | ignore it.                               |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in           | ``xs:boolean`` | Optional     | Single       | Signifies whether this selection         | If the field is invalid or not present,  |
|                       |                |              |              | represents a write-in line.              | then the implementation is required to   |
|                       |                |              |              |                                          | ignore it.                               |
+-----------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,sequence_order,candidate_ids,endorsement_party_ids,is_write_in
    cs001,1,can001,par01,false
    cs002,2,can002,par02,false


.. _multi-csv-ballot-selection-base:

ballot_selection_base
---------------------

A base model for all ballot selection types:
:ref:`multi-csv-ballot-measure-selection`,
:ref:`multi-csv-candidate-selection`, and :ref:`multi-csv-party-selection`.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| sequence_order | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|                |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|                |                |              |              | is the default ordering, and can be      | ignore it.                               |
|                |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|                |                |              |              | in :ref:`multi-csv-ordered-contest`.     |                                          |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
