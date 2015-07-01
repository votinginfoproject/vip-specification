.. This file is auto-generated.  Do not edit it by hand!

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| CandidateId  | xs:IDREF     | **Required** | Single       | Links to the :doc:`Candidate             | If the field is invalid, then the        |
|              |              |              |              | <candidate>` being retained.             | implementation is required to ignore the |
|              |              |              |              |                                          | ``RetentionContest`` element containing  |
|              |              |              |              |                                          | it.                                      |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeId     | xs:IDREF     | Optional     | Single       | Links to the information about the       | If the field is invalid or not present,  |
|              |              |              |              | office.                                  | then the implementation is required to   |
|              |              |              |              |                                          | ignore it.                               |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
