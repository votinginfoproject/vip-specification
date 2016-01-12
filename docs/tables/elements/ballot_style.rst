.. This file is auto-generated.  Do not edit it by hand!

+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+==============+==============+==============+==========================================+==========================================+
| ImageUri         | xs:anyURI    | Optional     | Single       | Specifies a URI that returns an image of | If the field is invalid or not present,  |
|                  |              |              |              | the sample ballot.                       | then the implementation is required to   |
|                  |              |              |              |                                          | ignore it.                               |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedContestId | xs:IDREF     | Optional     | Repeats      | Reference to an :doc:`OrderedContest     | If the field is invalid or not present,  |
|                  |              |              |              | </xml/elements/ordered_contest>`         | then the implementation is required to   |
|                  |              |              |              |                                          | ignore it.                               |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId          | xs:IDREF     | Optional     | Repeats      | Reference to a :doc:`Party <party>`.     | If the field is invalid or not present,  |
|                  |              |              |              |                                          | then the implementation is required to   |
|                  |              |              |              |                                          | ignore it.                               |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
