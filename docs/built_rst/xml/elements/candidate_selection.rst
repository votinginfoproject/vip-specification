.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate-selection:

CandidateSelection
==================

CandidateSelection extends :ref:`multi-xml-ballot-selection-base` and represents a ballot selection for one or more candidates in a candidate contest.

+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+================+==============+==============+==========================================+==========================================+
| CandidateIds        | ``xs:IDREFS``  | **Required** | Single       | References :ref:`multi-xml-candidate`    | If CandidateIds is invalid or not        |
|                     |                |              |              | elements that comprise this selection    | present, the implementation is required  |
|                     |                |              |              | (e.g. candidate and running mate).       | to ignore the CandidateSelection         |
|                     |                |              |              |                                          | containing it.                           |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyIds | ``xs:IDREFS``  | Optional     | Single       | References :ref:`multi-xml-party`        | If the field is invalid or not present,  |
|                     |                |              |              | elements endorsing this candidate        | then the implementation is required to   |
|                     |                |              |              | selection.                               | ignore it.                               |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | ``xs:boolean`` | Optional     | Single       | Signifies whether this selection         | If the field is invalid or not present,  |
|                     |                |              |              | represents a write-in line.              | then the implementation is required to   |
|                     |                |              |              |                                          | ignore it.                               |
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
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|               |                |              |              | is the default ordering, and can be      | ignore it.                               |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`multi-xml-ordered-contest`.     |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
