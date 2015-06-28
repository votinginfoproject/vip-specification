.. This file is auto-generated.  Do not edit it by hand!

+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==============+==============+==============+==========================================+==========================================+
| Hours               | `Hours`_     | Optional     | Repeats      | Blocks of hours in the date range in     | If the field is invalid or not present,  |
|                     |              |              |              | which the place is open.                 | the implementation is required to ignore |
|                     |              |              |              |                                          | it.                                      |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOnlyByAppointment | xs:boolean   | Optional     | Single       | If true, the place is only open during   | If the field is invalid or not present,  |
|                     |              |              |              | the specified time window with an        | the implementation is required to ignore |
|                     |              |              |              | appointment.                             | it.                                      |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOrByAppointment   | xs:boolean   | Optional     | Single       | If true, the place is open during the    | If the field is invalid or not present,  |
|                     |              |              |              | hours specified time window and may also | the implementation is required to ignore |
|                     |              |              |              | be open with an appointment.             | it.                                      |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsSubjectToChange   | xs:boolean   | Optional     | Single       | If true, the place should be open during | If the field is invalid or not present,  |
|                     |              |              |              | the specified time window, but may be    | the implementation is required to ignore |
|                     |              |              |              | subject to change. People should contact | it.                                      |
|                     |              |              |              | prior to arrival to confirm hours are    |                                          |
|                     |              |              |              | still accurate.                          |                                          |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate           | xs:date      | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |              |              |              | start and end times and options begin.   | the implementation is required to ignore |
|                     |              |              |              |                                          | it.                                      |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate             | xs:date      | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |              |              |              | start and end times and options end.     | the implementation is required to ignore |
|                     |              |              |              |                                          | it.                                      |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
