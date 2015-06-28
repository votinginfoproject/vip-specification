.. This file is auto-generated.  Do not edit it by hand!

+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=============================+==============+==============+==========================================+==========================================+
| Date                       | xs:date                     | **Required** | Single       | Specifies when the election is being     | If the field is not present or invalid,  |
|                            |                             |              |              | held. The Date is considered to be in    | the implementation is required to ignore |
|                            |                             |              |              | the timezone local to the state holding  | the election element containing it.      |
|                            |                             |              |              | the election.                            |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionType               | :doc:`InternationalizedText | Optional     | Single       | Specifies the highest controlling        | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | authority for election (e.g., federal,   | present, the implementation is required  |
|                            |                             |              |              | state, county, city, town, etc.)         | to ignore it.                            |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                    | xs:IDREF                    | **Required** | Single       | Specifies a link to the state element    | If the field is not present or invalid,  |
|                            |                             |              |              | where the election is being held.        | the implementation is required to ignore |
|                            |                             |              |              |                                          | the element containing it.               |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsStatewide                | xs:boolean                  | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                            |                             |              |              | statewide.                               | the implementation is required to        |
|                            |                             |              |              |                                          | default to "yes".                        |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                       | :doc:`InternationalizedText | Optional     | Single       | The name for the election (**NB:** while | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | optional, this element is highly         | present, the implementation is required  |
|                            |                             |              |              | recommended).                            | to ignore it.                            |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationInfo           | :doc:`InternationalizedText | Optional     | Single       | Specifies information about registration | If the field is invalid or not present,  |
|                            | <internationalized_text>`   |              |              | for this election either as text or a    | the implementation is required to ignore |
|                            |                             |              |              | URL.                                     | it.                                      |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeBallotInfo         | :doc:`InternationalizedText | Optional     | Single       | Specifies information about requesting   | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | absentee ballots either as text or a URL | present, the implementation is required  |
|                            |                             |              |              |                                          | to ignore it.                            |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ResultsUrl                 | xs:anyUri                   | Optional     | Single       | Contains a URL where results for the     | If the field is invalid or not present,  |
|                            |                             |              |              | election may be found                    | the implementation is required to ignore |
|                            |                             |              |              |                                          | it.                                      |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingHours               | :doc:`InternationalizedText | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]**           | <internationalized_text>`   |              |              | Election Day polling locations are open. | present, the implementation is required  |
|                            |                             |              |              | If polling hours differ in specific      | to ignore it.                            |
|                            |                             |              |              | polling locations, alternative hours may |                                          |
|                            |                             |              |              | be specified in the                      |                                          |
|                            |                             |              |              | :doc:`PollingLocation                    |                                          |
|                            |                             |              |              | <polling_location>` object *(NB: this    |                                          |
|                            |                             |              |              | element is deprecated in favor of the    |                                          |
|                            |                             |              |              | more structured :doc:`HoursOpen          |                                          |
|                            |                             |              |              | <hours_open>` element. It is strongly    |                                          |
|                            |                             |              |              | encouraged that data providers move      |                                          |
|                            |                             |              |              | toward contributing hours in this        |                                          |
|                            |                             |              |              | format)*.                                |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId                | xs:IDREF                    | Optional     | Single       | References the :doc:`HoursOpen           | If the field is invalid or not present,  |
|                            |                             |              |              | <hours_open>` element, which lists the   | the implementation is required to ignore |
|                            |                             |              |              | hours of operation for polling           | it.                                      |
|                            |                             |              |              | locations.                               |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasElectionDayRegistration | xs:boolean                  | Optional     | Single       | Specifies if a voter can register on the | If the field is invalid or not present,  |
|                            |                             |              |              | same day of the election (i.e., the last | the implementation is required to ignore |
|                            |                             |              |              | day of the election). Valid items are    | it.                                      |
|                            |                             |              |              | "yes" and "no".                          |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationDeadline       | xs:date                     | Optional     | Single       | Specifies the last day to register for   | If the field is invalid or not present,  |
|                            |                             |              |              | the election with the possible exception | the implementation is required to ignore |
|                            |                             |              |              | of Election Day registration.            | it.                                      |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeRequestDeadline    | xs:date                     | Optional     | Single       | Specifies the last day to request an     | If the field is invalid or not present,  |
|                            |                             |              |              | absentee ballot.                         | the implementation is required to ignore |
|                            |                             |              |              |                                          | it.                                      |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
