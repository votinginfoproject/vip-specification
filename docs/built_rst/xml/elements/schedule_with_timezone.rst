.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-schedule-with-timezone:

ScheduleWithTimezone
====================

Defines a schedule of dates and hours of operation with an optional IANA time zone. If the time zone is omitted, hours are assumed to be in the local time of the enclosing entity. ScheduleWithTimezone has an optional ``label`` attribute.

In overlay feeds, elements of type ScheduleWithTimezone are clearable using ``<ClearSchedule/>`` (or ``<ClearDefaultPollingHours/>``, etc. depending on the tag name).

+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type              | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+========================+==============+==============+==========================================+==========================================+
| TimeZone            | ``xs:string``          | Optional     | Single       | The named IANA time zone (e.g.           | If the field is invalid or not present,  |
|                     |                        |              |              | "America/New_York", "Etc/UTC",           | then the implementation is required to   |
|                     |                        |              |              | "Etc/GMT+1"). Must match canonical       | ignore it.                               |
|                     |                        |              |              | Continent/City format. If not present,   |                                          |
|                     |                        |              |              | hours are assumed to be in local time.   |                                          |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate           | ``xs:date``            | Optional     | Single       | The date on which this schedule begins.  | If the field is invalid or not present,  |
|                     |                        |              |              |                                          | then the implementation is required to   |
|                     |                        |              |              |                                          | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate             | ``xs:date``            | Optional     | Single       | The date on which this schedule ends.    | If the field is invalid or not present,  |
|                     |                        |              |              |                                          | then the implementation is required to   |
|                     |                        |              |              |                                          | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours               | :ref:`multi-xml-hours` | Optional     | Repeats      | Blocks of hours during which the         | If the element is invalid or not         |
|                     |                        |              |              | location is open on days in the date     | present, then the implementation is      |
|                     |                        |              |              | range.                                   | required to ignore it.                   |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOpen24Hours       | ``xs:boolean``         | Optional     | Single       | Indicates if the location is open 24     | If the field is invalid or not present,  |
|                     |                        |              |              | hours a day during this date range (e.g. | then the implementation is required to   |
|                     |                        |              |              | 24-hour ballot drop boxes).              | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOnlyByAppointment | ``xs:boolean``         | Optional     | Single       | If true, the location is only open       | If the field is invalid or not present,  |
|                     |                        |              |              | during the specified window with an      | then the implementation is required to   |
|                     |                        |              |              | appointment.                             | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOrByAppointment   | ``xs:boolean``         | Optional     | Single       | If true, the location is open during the | If the field is invalid or not present,  |
|                     |                        |              |              | window and may also be open by           | then the implementation is required to   |
|                     |                        |              |              | appointment.                             | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsSubjectToChange   | ``xs:boolean``         | Optional     | Single       | If true, hours may be subject to change. | If the field is invalid or not present,  |
|                     |                        |              |              | Voters should verify prior to arrival.   | then the implementation is required to   |
|                     |                        |              |              |                                          | ignore it.                               |
+---------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Schedule label="early_voting_week1">
      <TimeZone>America/New_York</TimeZone>
      <StartDate>2024-10-21</StartDate>
      <EndDate>2024-10-25</EndDate>
      <Hours>
         <StartTime>08:00:00</StartTime>
         <EndTime>17:00:00</EndTime>
      </Hours>
      <IsOpen24Hours>false</IsOpen24Hours>
      <IsOnlyByAppointment>false</IsOnlyByAppointment>
      <IsOrByAppointment>false</IsOrByAppointment>
      <IsSubjectToChange>false</IsSubjectToChange>
   </Schedule>


.. _multi-xml-hours:

Hours
-----

The open and close time for a location. All times must be fully specified without time zone information. The time zone is assumed to be specified in an enclosing element (e.g. in a :ref:`multi-xml-schedule-with-timezone` element). Hours has an optional ``label`` attribute.

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| StartTime    | :ref:`multi-xml-time-without-zone` | **Required** | Single       | The time at which the location opens     | If StartTime is invalid or not present,  |
|              |                                    |              |              | (e.g. "06:00:00").                       | the implementation is required to ignore |
|              |                                    |              |              |                                          | the Hours element containing it.         |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | :ref:`multi-xml-time-without-zone` | **Required** | Single       | The time at which the location closes    | If EndTime is invalid or not present,    |
|              |                                    |              |              | (e.g. "19:00:00").                       | the implementation is required to ignore |
|              |                                    |              |              |                                          | the Hours element containing it.         |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-time-without-zone:

TimeWithoutZone
~~~~~~~~~~~~~~~

A time value with no time zone. The time zone is specified in an enclosing structure, such as a :ref:`multi-xml-schedule-with-timezone` element. The pattern is:

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))``

.. code-block:: xml
   :linenos:

   <Schedule>
      <TimeZone>America/New_York</TimeZone>
      <Hours>
         <StartTime>06:00:00</StartTime>
         <EndTime>19:00:00</EndTime>
      </Hours>
      <StartDate>2024-11-05</StartDate>
      <EndDate>2024-11-05</EndDate>
   </Schedule>
