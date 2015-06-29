.. This file is auto-generated.  Do not edit it by hand!

+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+===================================================+==============+==============+==========================================+==========================================+
| BallotName          | :doc:`InternationalizedText                       | **Required** | Single       | The candidate's name as it will be       | If the element is invalid, then the      |
|                     | <internationalized_text>`                         |              |              | displayed on the official ballot (e.g.   | implementation is required to ignore the |
|                     |                                                   |              |              | "Ken T. Cuccinelli II").                 | ``Candidate`` element containing it.     |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers <external_identifiers>` | Optional     | Single       | Another identifier for a candidate that  | If the element is invalid or not         |
|                     |                                                   |              |              | links to another source of information   | present, then the implementation is      |
|                     |                                                   |              |              | (e.g. a campaign committee ID that links | required to ignore it.                   |
|                     |                                                   |              |              | to a campaign finance system).           |                                          |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileDate            | xs:date                                           | Optional     | Single       | Date and time when the candidate filed   | If the field is invalid or not present,  |
|                     |                                                   |              |              | for the contest.                         | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsIncumbent         | xs:boolean                                        | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                   |              |              | incumbent for the office associated with | then the implementation is required to   |
|                     |                                                   |              |              | the contest.                             | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsTopTicket         | xs:boolean                                        | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                   |              |              | top of a ticket that includes multiple   | then the implementation is required to   |
|                     |                                                   |              |              | candidates.                              | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId             | xs:IDREF                                          | Optional     | Single       | Reference to a :doc:`Party <party>`      | If the field is invalid or not present,  |
|                     |                                                   |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                   |              |              | about the candidate's affiliated party.  | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PersonId            | xs:IDREF                                          | Optional     | Single       | Reference to a :doc:`Person <person>`    | If the field is invalid or not present,  |
|                     |                                                   |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                   |              |              | about the candidate.                     | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostElectionStatus  | :doc:`CandidatePostElectionStatus                 | Optional     | Single       | Final status of the candidate (e.g.      | If the field is invalid or not present,  |
|                     | <../enumerations/candidate_post_election_status>` |              |              | winner, withdrawn, etc...).              | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PreElectionStatus   | :doc:`CandidatePreElectionStatus                  | Optional     | Single       | Registration status of the candidate     | If the field is invalid or not present,  |
|                     | <../enumerations/candidate_pre_election_status>`  |              |              | (e.g. filed, qualified, etc...).         | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder       | xs:integer                                        | Optional     | Single       | The order in which the candidate can be  | If the field is invalid or not present,  |
|                     |                                                   |              |              | listed on the ballot or in results.      | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
