.. This file is auto-generated.  Do not edit it by hand!

+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+==============+==============+==============+==========================================+==========================================+
| NumberElected  | xs:integer   | Optional     | Single       | Number of candidates that are elected in | If the field is invalid or not present,  |
|                |              |              |              | the contest (i.e. "N" of N-of-M).        | then the implementation is required to   |
|                |              |              |              |                                          | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeIds      | xs:IDREFS    | Optional     | Single       | References a set of :doc:`Office         | If the field is invalid or not present,  |
|                |              |              |              | <office>` elements, if available, which  | then the implementation is required to   |
|                |              |              |              | give additional information about the    | ignore it.                               |
|                |              |              |              | offices.                                 |                                          |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrimaryPartyId | xs:IDREF     | Optional     | Single       | References a :doc:`Party <party>`        | If the field is invalid or not present,  |
|                |              |              |              | element, if the contest is related to a  | then the implementation is required to   |
|                |              |              |              | particular party.                        | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VotesAllowed   | xs:integer   | Optional     | Single       | Maximum number of votes/write-ins per    | If the field is invalid or not present,  |
|                |              |              |              | voter in this contest.                   | then the implementation is required to   |
|                |              |              |              |                                          | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
