.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-schedule-with-timezone:

schedule_with_timezone
======================

Defines a schedule of dates and hours of operation with an optional IANA time zone. If the time zone is omitted, hours are assumed to be in the local time of the enclosing entity. ScheduleWithTimezone has an optional ``label`` attribute.

In overlay feeds, elements of type ScheduleWithTimezone are clearable using ``<ClearSchedule/>`` (or ``<ClearDefaultPollingHours/>``, etc. depending on the tag name).

+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type              | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+========================+==============+==============+==========================================+==========================================+
| time_zone              | ``xs:string``          | Optional     | Single       | The named IANA time zone (e.g.           | If the field is invalid or not present,  |
|                        |                        |              |              | "America/New_York", "Etc/UTC",           | then the implementation is required to   |
|                        |                        |              |              | "Etc/GMT+1"). Must match canonical       | ignore it.                               |
|                        |                        |              |              | Continent/City format. If not present,   |                                          |
|                        |                        |              |              | hours are assumed to be in local time.   |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_date             | ``xs:date``            | Optional     | Single       | The date on which this schedule begins.  | If the field is invalid or not present,  |
|                        |                        |              |              |                                          | then the implementation is required to   |
|                        |                        |              |              |                                          | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_date               | ``xs:date``            | Optional     | Single       | The date on which this schedule ends.    | If the field is invalid or not present,  |
|                        |                        |              |              |                                          | then the implementation is required to   |
|                        |                        |              |              |                                          | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours                  | :ref:`multi-csv-hours` | Optional     | Repeats      | Blocks of hours during which the         | If the element is invalid or not         |
|                        |                        |              |              | location is open on days in the date     | present, then the implementation is      |
|                        |                        |              |              | range.                                   | required to ignore it.                   |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_open_24_hours       | ``xs:boolean``         | Optional     | Single       | Indicates if the location is open 24     | If the field is invalid or not present,  |
|                        |                        |              |              | hours a day during this date range (e.g. | then the implementation is required to   |
|                        |                        |              |              | 24-hour ballot drop boxes).              | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_only_by_appointment | ``xs:boolean``         | Optional     | Single       | If true, the location is only open       | If the field is invalid or not present,  |
|                        |                        |              |              | during the specified window with an      | then the implementation is required to   |
|                        |                        |              |              | appointment.                             | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_or_by_appointment   | ``xs:boolean``         | Optional     | Single       | If true, the location is open during the | If the field is invalid or not present,  |
|                        |                        |              |              | window and may also be open by           | then the implementation is required to   |
|                        |                        |              |              | appointment.                             | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_subject_to_change   | ``xs:boolean``         | Optional     | Single       | If true, hours may be subject to change. | If the field is invalid or not present,  |
|                        |                        |              |              | Voters should verify prior to arrival.   | then the implementation is required to   |
|                        |                        |              |              |                                          | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,time_zone,start_date,end_date,is_open_24_hours,is_only_by_appointment,is_or_by_appointment,is_subject_to_change
    sch001,America/New_York,2024-10-10,2024-10-12,false,false,true,false
    sch002,America/New_York,2024-10-13,2024-10-15,false,true,false,false
