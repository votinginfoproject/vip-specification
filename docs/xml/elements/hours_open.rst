HoursOpen
=========

A structured way of describing the days and hours that a place such as a
:doc:`Office <office>` or :doc:`PollingLocation <polling_location>` is open, or
that an event such as an :doc:`Election <election>` is happening.  The range
of days indicated by the StartDate and EndDate in each :doc:`Schedule <schedule>`
element should not overlap with peer :doc:`Schedule <schedule>` elements.  For
example it is invalid to specify a schedule from 10/01/2016 to 10/31/2016 and also 
specify a schedule from 10/10/2016 to 10/11/2016 within the same 
:doc:`HoursOpen <hours_open>` element.

.. include:: ../../tables/elements/hours_open.rst

Schedule
--------

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

.. include:: ../../tables/elements/schedule.rst

Hours
-----

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

.. include:: ../../tables/elements/hours.rst

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
