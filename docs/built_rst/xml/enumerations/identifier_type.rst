.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-identifier-type:

IdentifierType
==============

Enumeration describing the set of supported external identifier types for entities such as contests, districts, candidates, and localities.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| fips           | Federal Information Processing Standards codes for |
|                | states_, counties_, and cities_.                   |
+----------------+----------------------------------------------------+
| local-level    | An identifier generated or used by local           |
|                | governments or organizations.                      |
+----------------+----------------------------------------------------+
| national-level | An identifier generated or used by national        |
|                | organizations.                                     |
+----------------+----------------------------------------------------+
| ocd-id         | An `Open Civic Data Division Identifier`_.         |
+----------------+----------------------------------------------------+
| state-level    | An identifier generated or used by state           |
|                | governments or organizations.                      |
+----------------+----------------------------------------------------+
| other          | Any identifier which does not fall into any of the |
|                | above categories.                                  |
+----------------+----------------------------------------------------+

.. _states: http://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code
.. _counties: http://en.wikipedia.org/wiki/FIPS_county_code
.. _cities: http://geonames.usgs.gov/domestic/fips55codedef.html
.. _`Open Civic Data Division Identifier`: http://docs.opencivicdata.org/en/latest/proposals/0002.html

ExternalIdentifier has optional attributes:

  - ``label``: Optional label for tracking purposes.
  - ``provider``: Optional source of the information, such as the department or authority that provided the identifier.
