.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-hours-open:

hours_open
==========

A structured way of describing the days and hours that a place such as a
:ref:`multi-csv-office` or :ref:`multi-csv-polling-location` is open, or
that an event such as an :ref:`multi-csv-election` is happening. The range of days
indicated by the `StartDate` and `EndDate` in each `Schedule`_ element
should not overlap with peer `Schedule`_ elements. For example, it is
invalid to specify a schedule from 10/01/2016 to 10/31/2016 and also
specify a schedule from 10/10/2016 to 10/11/2016 within the same `HoursOpen`
element.

+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===========================+==============+==============+==========================================+==========================================+
| schedule     | :ref:`multi-csv-schedule` | **Required** | Repeats      | Defines a block of days and hours that a | At least one valid `Schedule`_ must be   |
|              |                           |              |              | place will be open.                      | present for ``HoursOpen`` to be valid.   |
|              |                           |              |              |                                          | If no valid `Schedule`_ is present, the  |
|              |                           |              |              |                                          | implementation is required to ignore the |
|              |                           |              |              |                                          | ``HoursOpen`` element.                   |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-schedule:

schedule
--------

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type              | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+========================+==============+==============+==========================================+==========================================+
| hours                  | :ref:`multi-csv-hours` | Optional     | Repeats      | Blocks of hours in the date range in     | If the element is invalid or not         |
|                        |                        |              |              | which the place is open.                 | present, then the implementation is      |
|                        |                        |              |              |                                          | required to ignore it.                   |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_only_by_appointment | ``xs:boolean``         | Optional     | Single       | If true, the place is only open during   | If the field is invalid or not present,  |
|                        |                        |              |              | the specified time window with an        | then the implementation is required to   |
|                        |                        |              |              | appointment.                             | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_or_by_appointment   | ``xs:boolean``         | Optional     | Single       | If true, the place is open during the    | If the field is invalid or not present,  |
|                        |                        |              |              | hours specified time window and may also | then the implementation is required to   |
|                        |                        |              |              | be open with an appointment.             | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_subject_to_change   | ``xs:boolean``         | Optional     | Single       | If true, the place should be open during | If the field is invalid or not present,  |
|                        |                        |              |              | the specified time window, but may be    | then the implementation is required to   |
|                        |                        |              |              | subject to change. People should contact | ignore it.                               |
|                        |                        |              |              | prior to arrival to confirm hours are    |                                          |
|                        |                        |              |              | still accurate.                          |                                          |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_date             | ``xs:date``            | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                        |                        |              |              | start and end times and options begin.   | then the implementation is required to   |
|                        |                        |              |              |                                          | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_date               | ``xs:date``            | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                        |                        |              |              | start and end times and options end.     | then the implementation is required to   |
|                        |                        |              |              |                                          | ignore it.                               |
+------------------------+------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,start_time,end_time,is_only_by_appointment,is_or_by_appointment,is_subject_to_change,start_date,end_date,hours_open_id
    sch001,07:00:00-06:00,22:00:00-06:00,,true,,2016-10-10,2016-10-12,ho001
    sch002,09:00:00-06:00,20:00:00-06:00,true,,,2016-10-13,2016-10-15,ho001
    sch003,08:00:00-06:00,14:00:00-06:00,,,true,2016-10-10,2016-10-15,ho002


.. _multi-csv-hours:

hours
~~~~~

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=================================+==============+==============+==========================================+==========================================+
| start_time   | :ref:`multi-csv-time-with-zone` | Optional     | Single       | The time at which this place opens.      | If the element is invalid or not         |
|              |                                 |              |              |                                          | present, then the implementation is      |
|              |                                 |              |              |                                          | required to ignore it.                   |
+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_time     | :ref:`multi-csv-time-with-zone` | Optional     | Single       | The time at which this place closes.     | If the element is invalid or not         |
|              |                                 |              |              |                                          | present, then the implementation is      |
|              |                                 |              |              |                                          | required to ignore it.                   |
+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-time-with-zone:

time_with_zone
^^^^^^^^^^^^^^

A string pattern restricting the value to a time with an included offset from
UTC. The pattern is

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))(Z|[+-]((0[0-9]|1[0-3]):[0-5][0-9]|14:00))``

.. code-block:: xml
   :linenos:

   <HoursOpen id="hours0001">
     <Schedule>
       <Hours>
         <StartTime>06:00:00-05:00</StartTime>
         <EndTime>12:00:00-05:00</EndTime>
       </Hours>
       <Hours>
         <StartTime>13:00:00-05:00</StartTime>
         <EndTime>19:00:00-05:00</EndTime>
       </Hours>
       <StartDate>2013-11-05</StartDate>
       <EndDate>2013-11-05</EndDate>
     </Schedule>
   </HoursOpen>
