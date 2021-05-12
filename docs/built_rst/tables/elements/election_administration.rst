.. This file is auto-generated.  Do not edit it by hand!

+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Tag                          | Data Type                        | Required?    | Repeats?     | Description                                                 | Error Handling                           |
+==============================+==================================+==============+==============+=============================================================+==========================================+
| AbsenteeUri                  | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on absentee       | If the field is invalid or not present,  |
|                              |                                  |              |              | voting.                                                     | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| AmIRegisteredUri             | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on whether an     | If the field is invalid or not present,  |
|                              |                                  |              |              | individual is registered.                                   | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| BallotTrackingUri            | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    | If the field is invalid or not present,  |
|                              |                                  |              |              | ballot cast by mail                                         | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| BallotProvisionalTrackingUri | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    | If the field is invalid or not present,  |
|                              |                                  |              |              | provisional ballot. To support EAC guidelines for           | then the implementation is required to   |
|                              |                                  |              |              | "Processing Provisional Ballots"                            | ignore it.                               |
|                              |                                  |              |              | (https://www.eac.gov/research-and-data/provisional-voting/) |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Department                   | :ref:`multi-xml-department`      | **Required** | Repeats      | Describes the administrative body for a particular voter    | There must be at least one valid         |
|                              |                                  |              |              | service.                                                    | `Department` in each                     |
|                              |                                  |              |              |                                                             | `ElectionAdministration` element. If no  |
|                              |                                  |              |              |                                                             | valid `Department` objects are present,  |
|                              |                                  |              |              |                                                             | the implementation is required to ignore |
|                              |                                  |              |              |                                                             | the `ElectionAdministration` object that |
|                              |                                  |              |              |                                                             | contains it/them.                        |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ElectionNotice               | :ref:`multi-xml-election-notice` | Optional     | Single       | A place for election administrators to post last minute and | If the element is invalid or not         |
|                              |                                  |              |              | emergency notifications pertaining to the election.         | present, then the implementation is      |
|                              |                                  |              |              |                                                             | required to ignore it.                   |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ElectionsUri                 | ``xs:anyURI``                    | Optional     | Single       | Specifies web address the administration's website.         | If the field is invalid or not present,  |
|                              |                                  |              |              |                                                             | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| RegistrationUri              | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on registering to     | If the field is invalid or not present,  |
|                              |                                  |              |              | vote.                                                       | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| RulesUri                     | ``xs:anyURI``                    | Optional     | Single       | Specifies a URI for the election rules and laws (if any)    | If the field is invalid or not present,  |
|                              |                                  |              |              | for the jurisdiction of the administration.                 | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri          | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on what is on an      | If the field is invalid or not present,  |
|                              |                                  |              |              | individual's ballot.                                        | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| WhereDoIVoteUri              | ``xs:anyURI``                    | Optional     | Single       | The Specifies web address for information on where an       | If the field is invalid or not present,  |
|                              |                                  |              |              | individual votes based on their address.                    | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
