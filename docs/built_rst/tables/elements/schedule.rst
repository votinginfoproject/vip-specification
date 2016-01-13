.. This file is auto-generated.  Do not edit it by hand!

+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type              | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+========================+==============+==============+==========================================+==========================================+
| Hours               | :ref:`multi-xml-hours` | Optional     | Repeats      | Blocks of hours in the date range in     | If the element is invalid or not         |
|                     |                        |              |              | which the place is open.                 | present, then the implementation is      |
|                     |                        |              |              |                                          | required to ignore it.                   |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOnlyByAppointment | ``xs:boolean``         | Optional     | Single       | If true, the place is only open during   | If the field is invalid or not present,  |
|                     |                        |              |              | the specified time window with an        | then the implementation is required to   |
|                     |                        |              |              | appointment.                             | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOrByAppointment   | ``xs:boolean``         | Optional     | Single       | If true, the place is open during the    | If the field is invalid or not present,  |
|                     |                        |              |              | hours specified time window and may also | then the implementation is required to   |
|                     |                        |              |              | be open with an appointment.             | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsSubjectToChange   | ``xs:boolean``         | Optional     | Single       | If true, the place should be open during | If the field is invalid or not present,  |
|                     |                        |              |              | the specified time window, but may be    | then the implementation is required to   |
|                     |                        |              |              | subject to change. People should contact | ignore it.                               |
|                     |                        |              |              | prior to arrival to confirm hours are    |                                          |
|                     |                        |              |              | still accurate.                          |                                          |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate           | ``xs:date``            | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |                        |              |              | start and end times and options begin.   | then the implementation is required to   |
|                     |                        |              |              |                                          | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate             | ``xs:date``            | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |                        |              |              | start and end times and options end.     | then the implementation is required to   |
|                     |                        |              |              |                                          | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
