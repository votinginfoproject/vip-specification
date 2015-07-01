.. This file is auto-generated.  Do not edit it by hand!

+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type        | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==================+==============+==============+==========================================+==========================================+
| AbsenteeUri         | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on absentee voting.          | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AmIRegisteredUri    | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on whether an individual is  | then the implementation is required to   |
|                     |                  |              |              | registered.                              | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Department          | :ref:`Department | **Required** | Repeats      | Describes the administrative body for a  | If the element is invalid, then the      |
|                     | <ea-dep>`        |              |              | particular voter service.                | implementation is required to ignore the |
|                     |                  |              |              |                                          | ``ElectionAdministration`` element       |
|                     |                  |              |              |                                          | containing it.                           |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionsUri        | xs:anyURI        | Optional     | Single       | Specifies web address the                | If the field is invalid or not present,  |
|                     |                  |              |              | administration's website.                | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationUri     | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | registering to vote.                     | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RulesUri            | xs:anyURI        | Optional     | Single       | Specifies a URL for the election rules   | If the field is invalid or not present,  |
|                     |                  |              |              | and laws (if any) for the jurisdiction   | then the implementation is required to   |
|                     |                  |              |              | of the administration.                   | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | what is on an individual's ballot.       | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhereDoIVoteUri     | xs:anyURI        | Optional     | Single       | The Specifies web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on where an individual votes | then the implementation is required to   |
|                     |                  |              |              | based on their address.                  | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
