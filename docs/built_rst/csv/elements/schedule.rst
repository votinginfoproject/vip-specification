.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-schedule:

schedule
========

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type              | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+========================+==============+==============+==========================================+==========================================+
| is_only_by_appointment | ``xs:boolean``         | Optional     | Single       | If true, the place is only open during   |                                          |
|                        |                        |              |              | the specified time window with an        |                                          |
|                        |                        |              |              | appointment.                             |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_or_by_appointment   | ``xs:boolean``         | Optional     | Single       | If true, the place is open during the    |                                          |
|                        |                        |              |              | hours specified time window and may also |                                          |
|                        |                        |              |              | be open with an appointment.             |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_subject_to_change   | ``xs:boolean``         | Optional     | Single       | If true, the place should be open during |                                          |
|                        |                        |              |              | the specified time window, but may be    |                                          |
|                        |                        |              |              | subject to change. People should contact |                                          |
|                        |                        |              |              | prior to arrival to confirm hours are    |                                          |
|                        |                        |              |              | still accurate.                          |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_date             | ``xs:date``            | Optional     | Single       | The date at which this collection of     |                                          |
|                        |                        |              |              | start and end times and options begin.   |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_date               | ``xs:date``            | Optional     | Single       | The date at which this collection of     |                                          |
|                        |                        |              |              | start and end times and options end.     |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id          | ``xs:IDREF``           | **Required** | Single       | A reference to the associated hours_open |                                          |
|                        |                        |              |              | element.                                 |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,start_time,end_time,is_only_by_appointment,is_or_by_appointment,is_subject_to_change,start_date,end_date,hours_open_id
    sch001,07:00:00-06:00,22:00:00-06:00,,true,,2016-10-10,2016-10-12,ho001
    sch002,09:00:00-06:00,20:00:00-06:00,true,,,2016-10-13,2016-10-15,ho001
    sch003,08:00:00-06:00,14:00:00-06:00,,,true,2016-10-10,2016-10-15,ho002
