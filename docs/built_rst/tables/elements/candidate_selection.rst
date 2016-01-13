.. This file is auto-generated.  Do not edit it by hand!

+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+================+==============+==============+==========================================+==========================================+
| CandidateIds        | ``xs:IDREFS``  | Optional     | Single       | References a set of                      | If the field is invalid or not present,  |
|                     |                |              |              | :ref:`multi-xml-candidate` elements. The | then the implementation is required to   |
|                     |                |              |              | number of candidates that can be         | ignore it.                               |
|                     |                |              |              | references is unbounded in cases where   |                                          |
|                     |                |              |              | the ballot selection is for a ticket     |                                          |
|                     |                |              |              | (e.g. "President/Vice President",        |                                          |
|                     |                |              |              | "Governor/Lt Governor").                 |                                          |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyIds | ``xs:IDREFS``  | Optional     | Single       | References a set of                      | If the field is invalid or not present,  |
|                     |                |              |              | :ref:`multi-xml-party` elements, which   | then the implementation is required to   |
|                     |                |              |              | signifies one or more endorsing parties  | ignore it.                               |
|                     |                |              |              | for the candidate(s).                    |                                          |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | ``xs:boolean`` | Optional     | Single       | Signifies if the particular ballot       | If the field is invalid or not present,  |
|                     |                |              |              | selection allows for write-in            | then the implementation is required to   |
|                     |                |              |              | candidates. If true, one or more         | ignore it.                               |
|                     |                |              |              | write-in candidates are allowed for this |                                          |
|                     |                |              |              | contest.                                 |                                          |
+---------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
