.. This file is auto-generated.  Do not edit it by hand!

+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=========================================+==============+==============+==========================================+==========================================+
| Date                       | ``xs:date``                             | **Required** | Single       | Specifies when the election is being     | If the field is invalid, then the        |
|                            |                                         |              |              | held. The `Date` is considered to be in  | implementation is required to ignore the |
|                            |                                         |              |              | the timezone local to the state holding  | ``Election`` element containing it.      |
|                            |                                         |              |              | the election.                            |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionType               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the highest controlling        | If the element is invalid or not         |
|                            |                                         |              |              | authority for election (e.g., federal,   | present, then the implementation is      |
|                            |                                         |              |              | state, county, city, town, etc.)         | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                    | ``xs:IDREF``                            | **Required** | Single       | Specifies a link to the `State` element  | If the field is invalid, then the        |
|                            |                                         |              |              | where the election is being held.        | implementation is required to ignore the |
|                            |                                         |              |              |                                          | ``Election`` element containing it.      |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsStatewide                | ``xs:boolean``                          | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                            |                                         |              |              | statewide.                               | the implementation is required to        |
|                            |                                         |              |              |                                          | default to "yes".                        |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | The name for the election (**NB:** while | If the element is invalid or not         |
|                            |                                         |              |              | optional, this element is highly         | present, then the implementation is      |
|                            |                                         |              |              | recommended).                            | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationInfo           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies information about registration | If the element is invalid or not         |
|                            |                                         |              |              | for this election either as text or a    | present, then the implementation is      |
|                            |                                         |              |              | URI.                                     | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeBallotInfo         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies information about requesting   | If the element is invalid or not         |
|                            |                                         |              |              | absentee ballots either as text or a URI | present, then the implementation is      |
|                            |                                         |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ResultsUri                 | ``xs:anyURI``                           | Optional     | Single       | Contains a URI where results for the     | If the field is invalid or not present,  |
|                            |                                         |              |              | election may be found                    | then the implementation is required to   |
|                            |                                         |              |              |                                          | ignore it.                               |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingHours               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]**           |                                         |              |              | Election Day polling locations are open. | present, then the implementation is      |
|                            |                                         |              |              | If polling hours differ in specific      | required to ignore it.                   |
|                            |                                         |              |              | polling locations, alternative hours may |                                          |
|                            |                                         |              |              | be specified in the                      |                                          |
|                            |                                         |              |              | :ref:`multi-xml-polling-location` object |                                          |
|                            |                                         |              |              | *(NB: this element is deprecated in      |                                          |
|                            |                                         |              |              | favor of the more structured             |                                          |
|                            |                                         |              |              | :ref:`multi-xml-hours-open` element. It  |                                          |
|                            |                                         |              |              | is strongly encouraged that data         |                                          |
|                            |                                         |              |              | providers move toward contributing hours |                                          |
|                            |                                         |              |              | in this format)*.                        |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId                | ``xs:IDREF``                            | Optional     | Single       | References the                           | If the field is invalid or not present,  |
|                            |                                         |              |              | :ref:`multi-xml-hours-open` element,     | then the implementation is required to   |
|                            |                                         |              |              | which lists the hours of operation for   | ignore it.                               |
|                            |                                         |              |              | polling locations.                       |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasElectionDayRegistration | ``xs:boolean``                          | Optional     | Single       | Specifies if a voter can register on the | If the field is invalid or not present,  |
|                            |                                         |              |              | same day of the election (i.e., the last | then the implementation is required to   |
|                            |                                         |              |              | day of the election). Valid items are    | ignore it.                               |
|                            |                                         |              |              | "yes" and "no".                          |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationDeadline       | ``xs:date``                             | Optional     | Single       | Specifies the last day to register for   | If the field is invalid or not present,  |
|                            |                                         |              |              | the election with the possible exception | then the implementation is required to   |
|                            |                                         |              |              | of Election Day registration.            | ignore it.                               |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeRequestDeadline    | ``xs:date``                             | Optional     | Single       | Specifies the last day to request an     | If the field is invalid or not present,  |
|                            |                                         |              |              | absentee ballot.                         | then the implementation is required to   |
|                            |                                         |              |              |                                          | ignore it.                               |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
