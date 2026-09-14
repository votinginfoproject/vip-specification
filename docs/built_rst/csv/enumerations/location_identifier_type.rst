.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-location-identifier-type:

location_identifier_type
========================

Enumeration describing the set of supported location identifier types.

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| latlong      | A latitude/longitude pair, e.g.                    |
|              | `40.6970243,-74.1443098`.                          |
+--------------+----------------------------------------------------+
| pluscode     | An Open Location Code / Plus Code, e.g.            |
|              | `87G8PXRX+86`.                                     |
+--------------+----------------------------------------------------+
| geocoder-id  | A geocoder- or platform-specific identifier such   |
|              | as a Google Place ID. The enclosing element        |
|              | specifies the data provider along with the value.  |
+--------------+----------------------------------------------------+
| other        | Any location identifier that does not fall into    |
|              | the above categories. When using this value,       |
|              | OtherType should be specified.                     |
+--------------+----------------------------------------------------+
