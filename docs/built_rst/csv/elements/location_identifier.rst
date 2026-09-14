.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-location-identifier:

location_identifier
===================

Specifies an external identifier for a physical location (e.g. a polling location or contact address), such as a latitude/longitude pair, Plus Code, or geocoder ID. LocationIdentifier has optional attributes ``label``, ``provider`` (e.g. "Google"), and ``relativePriority`` (a decimal number indicating the relative preference of this identifier when multiple identifiers are provided).

In overlay feeds, this element is clearable using ``<ClearLocationIdentifier/>``.

+--------------+-------------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Tag          | Data Type                                 | Required?    | Repeats?     | Description                                | Error Handling                           |
+==============+===========================================+==============+==============+============================================+==========================================+
| type         | :ref:`multi-csv-location-identifier-type` | **Required** | Single       | Specifies the type of location identifier  | If the field is invalid or not present,  |
|              |                                           |              |              | from                                       | the implementation is required to ignore |
|              |                                           |              |              | :ref:`multi-csv-location-identifier-type`. | the ``LocationIdentifier`` containing    |
|              |                                           |              |              |                                            | it.                                      |
+--------------+-------------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``                             | Optional     | Single       | Specifies the type of identifier if        | If the field is invalid or not present,  |
|              |                                           |              |              | ``Type`` is set to "other".                | then the implementation is required to   |
|              |                                           |              |              |                                            | ignore it.                               |
+--------------+-------------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| value        | ``xs:string``                             | **Required** | Single       | Specifies the identifier value (e.g. Plus  | If the field is invalid or not present,  |
|              |                                           |              |              | Code, coordinates, Place ID).              | the implementation is required to ignore |
|              |                                           |              |              |                                            | the ``LocationIdentifier`` containing    |
|              |                                           |              |              |                                            | it.                                      |
+--------------+-------------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
