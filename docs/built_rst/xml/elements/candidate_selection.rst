.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate-selection:

CandidateSelection
==================

CandidateSelection extends :ref:`multi-xml-ballot-selection-base` and represents a
ballot selection for a candidate contest.

+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+================+==============+==============+==========================================+==========================================+
| CandidateIds        | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                     |                |              |              | :ref:`multi-xml-candidate` elements. The |                                          |
|                     |                |              |              | number of candidates that can be         |                                          |
|                     |                |              |              | references is unbounded in cases where   |                                          |
|                     |                |              |              | the ballot selection is for a ticket     |                                          |
|                     |                |              |              | (e.g. "President/Vice President",        |                                          |
|                     |                |              |              | "Governor/Lt Governor").                 |                                          |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyIds | ``xs:IDREFS``  | Optional     | Single       | References a set of                      |                                          |
|                     |                |              |              | :ref:`multi-xml-party` elements, which   |                                          |
|                     |                |              |              | signifies one or more endorsing parties  |                                          |
|                     |                |              |              | for the candidate(s).                    |                                          |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | ``xs:boolean`` | Optional     | Single       | Signifies if the particular ballot       |                                          |
|                     |                |              |              | selection allows for write-in            |                                          |
|                     |                |              |              | candidates. If true, one or more         |                                          |
|                     |                |              |              | write-in candidates are allowed for this |                                          |
|                     |                |              |              | contest.                                 |                                          |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateSelection id="cs10861">
      <CandidateIds>can10861a can10861b</CandidateIds>
      <EndorsementPartyIds>par0001</EndorsementPartyIds>
   </CandidateSelection>


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
