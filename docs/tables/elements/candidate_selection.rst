.. This file is auto-generated.  Do not edit it by hand!

+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==============+==============+==============+==========================================+==========================================+
| CandidateIds        | xs:IDREFS    | Optional     | Single       | References a set of :doc:`Candidate      | If the field is invalid or not present,  |
|                     |              |              |              | <candidate>` elements. The number of     | then the implementation is required to   |
|                     |              |              |              | candidates that can be references is     | ignore it.                               |
|                     |              |              |              | unbounded in cases where the ballot      |                                          |
|                     |              |              |              | selection is for a ticket (e.g.          |                                          |
|                     |              |              |              | "President/Vice President", "Governor/Lt |                                          |
|                     |              |              |              | Governor").                              |                                          |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyIds | xs:IDREFS    | Optional     | Single       | References a set of :doc:`Party <party>` | If the field is invalid or not present,  |
|                     |              |              |              | elements, which signifies one or more    | then the implementation is required to   |
|                     |              |              |              | endorsing parties for the candidate(s).  | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | xs:boolean   | Optional     | Single       | Signifies if the particular ballot       | If the field is invalid or not present,  |
|                     |              |              |              | selection allows for write-in            | then the implementation is required to   |
|                     |              |              |              | candidates. If true, one or more         | ignore it.                               |
|                     |              |              |              | write-in candidates are allowed for this |                                          |
|                     |              |              |              | contest.                                 |                                          |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
