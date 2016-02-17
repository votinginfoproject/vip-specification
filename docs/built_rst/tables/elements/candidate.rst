.. This file is auto-generated.  Do not edit it by hand!

+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=================================================+==============+==============+==========================================+==========================================+
| BallotName          | :ref:`multi-xml-internationalized-text`         | **Required** | Single       | The candidate's name as it will be       | If the element is invalid or not         |
|                     |                                                 |              |              | displayed on the official ballot (e.g.   | present, then the implementation is      |
|                     |                                                 |              |              | "Ken T. Cuccinelli II").                 | required to ignore the Candidate element |
|                     |                                                 |              |              |                                          | containing it.                           |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`           | Optional     | Single       | Another identifier for a candidate that  | If the element is invalid or not         |
|                     |                                                 |              |              | links to another source of information   | present, then the implementation is      |
|                     |                                                 |              |              | (e.g. a campaign committee ID that links | required to ignore it.                   |
|                     |                                                 |              |              | to a campaign finance system).           |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileDate            | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for the    | If the field is invalid or not present,  |
|                     |                                                 |              |              | contest.                                 | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsIncumbent         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                 |              |              | incumbent for the office associated with | then the implementation is required to   |
|                     |                                                 |              |              | the contest.                             | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsTopTicket         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                 |              |              | top of a ticket that includes multiple   | then the implementation is required to   |
|                     |                                                 |              |              | candidates.                              | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId             | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-xml-party`    | If the field is invalid or not present,  |
|                     |                                                 |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                 |              |              | about the candidate's affiliated party.  | ignore it.                               |
|                     |                                                 |              |              | This is the party affiliation that is    |                                          |
|                     |                                                 |              |              | intended to be presented as part of      |                                          |
|                     |                                                 |              |              | ballot information.                      |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PersonId            | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-xml-person`   | If the field is invalid or not present,  |
|                     |                                                 |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                 |              |              | about the candidate.                     | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostElectionStatus  | :ref:`multi-xml-candidate-post-election-status` | Optional     | Single       | Final status of the candidate (e.g.      | If the field is invalid or not present,  |
|                     |                                                 |              |              | winner, withdrawn, etc...).              | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PreElectionStatus   | :ref:`multi-xml-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate     | If the field is invalid or not present,  |
|                     |                                                 |              |              | (e.g. filed, qualified, etc...).         | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
