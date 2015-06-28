.. This file is auto-generated.  Do not edit it by hand!

+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+==============+==============+==============+==========================================+==========================================+
| CandidateId        | xs:IDREF     | Optional     | Repeats      | References a :doc:`Candidate             | If the field is invalid or not present,  |
|                    |              |              |              | <candidate>` element. The number of      | the implementation is required to ignore |
|                    |              |              |              | candidates that can be references is     | it.                                      |
|                    |              |              |              | unbounded in cases where the ballot      |                                          |
|                    |              |              |              | selection is for a ticket (e.g.          |                                          |
|                    |              |              |              | "President/Vice President", "Governor/Lt |                                          |
|                    |              |              |              | Governor").                              |                                          |
+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyId | xs:IDREF     | Optional     | Repeats      | References a :doc:`Party <party>`        | If the field is invalid or not present,  |
|                    |              |              |              | element, which signifies one or more     | the implementation is required to ignore |
|                    |              |              |              | endorsing parties for the candidate(s).  | it.                                      |
+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn          | xs:boolean   | Optional     | Single       | Signifies if the particular ballot       | If the field is invalid or not present,  |
|                    |              |              |              | selection allows for write-in            | the implementation is required to ignore |
|                    |              |              |              | candidates. If true, one or more         | it.                                      |
|                    |              |              |              | write-in candidates are allowed for this |                                          |
|                    |              |              |              | contest.                                 |                                          |
+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
