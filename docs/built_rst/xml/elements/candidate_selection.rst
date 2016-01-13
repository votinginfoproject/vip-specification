.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate-selection:

CandidateSelection
==================

CandidateSelection extends :ref:`single-xml-ballot-selection-base` and represents a
ballot selection for a candidate contest.

+--------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+================+==============+==============+==========================================+==========================================+
| CandidateId        | ``xs:IDREF``   | Optional     | Repeats      | References a :ref:`single-xml-candidate` | If the field is invalid or not present,  |
|                    |                |              |              | element. The number of candidates that   | then the implementation is required to   |
|                    |                |              |              | can be references is unbounded in cases  | ignore it.                               |
|                    |                |              |              | where the ballot selection is for a      |                                          |
|                    |                |              |              | ticket (e.g. "President/Vice President", |                                          |
|                    |                |              |              | "Governor/Lt Governor").                 |                                          |
+--------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyId | ``xs:IDREF``   | Optional     | Repeats      | References a :ref:`single-xml-party`     | If the field is invalid or not present,  |
|                    |                |              |              | element, which signifies one or more     | then the implementation is required to   |
|                    |                |              |              | endorsing parties for the candidate(s).  | ignore it.                               |
+--------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn          | ``xs:boolean`` | Optional     | Single       | Signifies if the particular ballot       | If the field is invalid or not present,  |
|                    |                |              |              | selection allows for write-in            | then the implementation is required to   |
|                    |                |              |              | candidates. If true, one or more         | ignore it.                               |
|                    |                |              |              | write-in candidates are allowed for this |                                          |
|                    |                |              |              | contest.                                 |                                          |
+--------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateSelection id="cs10861">
      <CandidateId>can10861a</CandidateId>
      <CandidateId>can10861b</CandidateId>
      <EndorsementPartyId>par0001</EndorsementPartyId>
   </CandidateSelection>
