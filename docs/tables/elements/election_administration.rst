.. This file is auto-generated.  Do not edit it by hand!

+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type        | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==================+==============+==============+==========================================+==========================================+
| AbsenteeUri         | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on absentee voting.          | the implementation is required to ignore |
|                     |                  |              |              |                                          | it.                                      |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AmIRegisteredUri    | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on whether an individual is  | the implementation is required to ignore |
|                     |                  |              |              | registered.                              | it.                                      |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Department          | :ref:`Department | **Required** | Repeats      | Describes the administrative body for a  | If the element is invalid or not         |
|                     | <ea-dep>`        |              |              | particular voter service.                | present, the implementation is required  |
|                     |                  |              |              |                                          | to ignore the **ElectionAdministration** |
|                     |                  |              |              |                                          | object that contains it.                 |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionsUri        | xs:anyURI        | Optional     | Single       | Specifies web address the                | If the field is invalid or not present,  |
|                     |                  |              |              | administration's website.                | the implementation is required to ignore |
|                     |                  |              |              |                                          | it.                                      |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationUri     | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | registering to vote.                     | the implementation is required to ignore |
|                     |                  |              |              |                                          | it.                                      |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RulesUri            | xs:anyURI        | Optional     | Single       | Specifies a URL for the election rules   | If the field is invalid the              |
|                     |                  |              |              | and laws (if any) for the jurisdiction   | implementation is required to ignore it. |
|                     |                  |              |              | of the administration.                   |                                          |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | what is on an individual's ballot.       | the implementation is required to ignore |
|                     |                  |              |              |                                          | it.                                      |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhereDoIVoteUri     | xs:anyURI        | Optional     | Single       | The Specifies web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on where an individual votes | the implementation is required to ignore |
|                     |                  |              |              | based on their address.                  | it.                                      |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
