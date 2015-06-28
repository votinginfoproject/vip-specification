.. This file is auto-generated.  Do not edit it by hand!

+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+==============+==============+==============+==========================================+==========================================+
| ImageUri         | xs:anyURI    | Optional     | Single       | Specifies a URI that returns an image of | If the field is invalid or not present,  |
|                  |              |              |              | the sample ballot.                       | the implementation is required to ignore |
|                  |              |              |              |                                          | it.                                      |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedContestId | xs:IDREF     | Optional     | Repeats      | Reference to an :doc:`OrderedContest     | If the field is invalid or not present,  |
|                  |              |              |              | <ordered_contest>`                       | the implementation is required to ignore |
|                  |              |              |              |                                          | it.                                      |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId          | xs:IDREF     | Optional     | Repeats      | Reference to a :doc:`Party <party>`.     | If the field is invalid or not present,  |
|                  |              |              |              |                                          | the implementation is required to ignore |
|                  |              |              |              |                                          | it.                                      |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
