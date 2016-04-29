.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-hours-open:

HoursOpen
=========

A structured way of describing the days and hours that a place such as a
:ref:`multi-xml-office` or :ref:`multi-xml-polling-location` is open, or
that an event such as an :ref:`multi-xml-election` is happening. The range of days
indicated by the `StartDate` and `EndDate` in each `Schedule`_ element
should not overlap with peer `Schedule`_ elements. For example, it is
invalid to specify a schedule from 10/01/2016 to 10/31/2016 and also
specify a schedule from 10/10/2016 to 10/11/2016 within the same `HoursOpen`
element.

+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===========================+==============+==============+==========================================+==========================================+
| Schedule     | :ref:`multi-xml-schedule` | **Required** | Repeats      | Defines a block of days and hours that a | At least one valid `Schedule`_ must be   |
|              |                           |              |              | place will be open.                      | present for ``HoursOpen`` to be valid.   |
|              |                           |              |              |                                          | If no valid `Schedule`_ is present, the  |
|              |                           |              |              |                                          | implementation is required to ignore the |
|              |                           |              |              |                                          | ``HoursOpen`` element.                   |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-schedule:

Schedule
--------

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

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


.. _multi-xml-hours:

Hours
-----

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=================================+==============+==============+==========================================+==========================================+
| StartTime    | :ref:`multi-xml-time-with-zone` | Optional     | Single       | The time at which this place opens.      | If the element is invalid or not         |
|              |                                 |              |              |                                          | present, then the implementation is      |
|              |                                 |              |              |                                          | required to ignore it.                   |
+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | :ref:`multi-xml-time-with-zone` | Optional     | Single       | The time at which this place closes.     | If the element is invalid or not         |
|              |                                 |              |              |                                          | present, then the implementation is      |
|              |                                 |              |              |                                          | required to ignore it.                   |
+--------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-time-with-zone:

TimeWithZone
------------

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
