HoursOpen
=========

A structured way of describing the days and hours that a place such as a
:doc:`Office <office>` or :doc:`PollingLocation <polling_location>` is open, or
that an event such as an :doc:`Election <election>` is happening.

+----------+--------------------+------------+----------+-----------------------+----------------------------------+
| Tag      | Data Type          | Required?  | Repeats? |Description            |Error Handling                    |
|          |                    |            |          |                       |                                  |
+==========+====================+============+==========+=======================+==================================+
| Schedule | Schedule           |**Required**| Repeats  |Defines a block of days|At least one valid `Schedule`_    |
|          |                    |            |          |and hours that a place |must be present for ``HoursOpen`` |
|          |                    |            |          |will be open.          |to be valid. If no valid          |
|          |                    |            |          |                       |`Schedule`_ is present, the       |
|          |                    |            |          |                       |implementation is required to     |
|          |                    |            |          |                       |ignore the ``HoursOpen`` element. |
+----------+--------------------+------------+----------+-----------------------+----------------------------------+

Schedule
--------

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

+---------------------+------------------+-----------+----------+----------------------+----------------------------+
| Tag                 | Data Type        | Required? | Repeats? |Description           |Error Handling              |
|                     |                  |           |          |                      |                            |
+=====================+==================+===========+==========+======================+============================+
| Hours               | Hours            | Optional  | Repeats  |Blocks of hours in the|If the field is invalid or  |
|                     |                  |           |          |date range in which   |not present, the            |
|                     |                  |           |          |the place is open.    |implementation is required  |
|                     |                  |           |          |                      |to ignore it.               |
+---------------------+------------------+-----------+----------+----------------------+----------------------------+
| IsOnlyByAppointment | xs:boolean       | Optional  | Single   |If true, the place is |If the field is invalid or  |
|                     |                  |           |          |only open during the  |not present, the            |
|                     |                  |           |          |specified time window |implementation is required  |
|                     |                  |           |          |with an appointment.  |to ignore it.               |
+---------------------+------------------+-----------+----------+----------------------+----------------------------+
| IsOrByAppointment   | xs:boolean       | Optional  | Single   |If true, the place is |If the field is invalid or  |
|                     |                  |           |          |open during the hours |not present, the            |
|                     |                  |           |          |specified time window |implementation is required  |
|                     |                  |           |          |and may also be open  |to ignore it.               |
|                     |                  |           |          |with an appointment.  |                            |
+---------------------+------------------+-----------+----------+----------------------+----------------------------+
| IsSubjectToChange   | xs:boolean       | Optional  | Single   |If true, the place    |If the field is invalid or  |
|                     |                  |           |          |should be open during |not present, the            |
|                     |                  |           |          |the specified time    |implementation is required  |
|                     |                  |           |          |window, but may be    | to ignore it.              |
|                     |                  |           |          |subject to change.    |                            |
|                     |                  |           |          |People should contact |                            |
|                     |                  |           |          |prior to arrival to   |                            |
|                     |                  |           |          |confirm hours are     |                            |
|                     |                  |           |          |still accurate.       |                            |
+---------------------+------------------+-----------+----------+----------------------+----------------------------+
| StartDate           | xs:date          | Optional  | Single   |The date at which this|If the field is invalid or  |
|                     |                  |           |          |collection of start   |not present, the            |
|                     |                  |           |          |and end times and     |implementation is required  |
|                     |                  |           |          |options begin.        |to ignore it.               |
+---------------------+------------------+-----------+----------+----------------------+----------------------------+
| EndDate             | xs:date          | Optional  | Single   |The date at which this|If the field is invalid or  |
|                     |                  |           |          |collection of start   |not present, the            |
|                     |                  |           |          |and end times and     |implementation is required  |
|                     |                  |           |          |options end.          |to ignore it.               |
+---------------------+------------------+-----------+----------+----------------------+----------------------------+

Hours
-----

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

+-----------+---------------+-----------+----------+----------------------+--------------------------------+
| Tag       | Data Type     | Required? | Repeats? |Description           |Error Handling                  |
|           |               |           |          |                      |                                |
+===========+===============+===========+==========+======================+================================+
| StartTime | TimeWithZone  | Optional  | Single   |The time at which this|If the field is invalid or      |
|           |               |           |          |place opens.          |not present, the implementation |
|           |               |           |          |                      |is required to ignore it.       |
+-----------+---------------+-----------+----------+----------------------+--------------------------------+
| EndTime   | TimeWithZone  | Optional  | Single   |The time at which this|If the field is invalid or not  |
|           |               |           |          |place closes.         |present, the implementation is  |
|           |               |           |          |                      |required to ignore it.          |
+-----------+---------------+-----------+----------+----------------------+--------------------------------+

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
