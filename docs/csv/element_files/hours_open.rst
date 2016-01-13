hours_open.txt
==============

A structured way of describing the days and hours that a place such as a
:doc:`Office <office>` or :doc:`PollingLocation <polling_location>` is open, or
that an event such as an :doc:`Election <election>` is happening.

.. include:: ../../built_rst/tables/elements/hours_open.rst

Schedule
--------

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

.. include:: ../../built_rst/tables/elements/schedule.rst

Hours
-----

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

.. include:: ../../built_rst/tables/elements/hours.rst

TimeWithZone
------------

A string pattern restricting the value to a time with an included offset from
UTC. The pattern is

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))(Z|[+-]((0[0-9]|1[0-3]):[0-5][0-9]|14:00))``

.. literalinclude:: ../../csv/example_files/hours_open.txt
   :linenos:
