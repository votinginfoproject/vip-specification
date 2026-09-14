.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-street-segment:

street_segment
==============

A StreetSegment object represents a range of house numbers along a street and links them to the containing :ref:`multi-csv-precinct`. Street segments are excluded from feed overlays.

+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+===========================+==============+==============+==========================================+==========================================+
| address_direction      | ``xs:string``             | Optional     | Single       | Specifies trailing directional component | If the field is invalid or not present,  |
|                        |                           |              |              | of the address (e.g. "NE").              | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city                   | ``xs:string``             | **Required** | Single       | City or municipality name.               | If the field is invalid, then the        |
|                        |                           |              |              |                                          | implementation is required to ignore the |
|                        |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_addresses | ``xs:boolean``            | Optional     | Single       | If true, the segment covers all          | If the field is invalid or not present,  |
|                        |                           |              |              | addresses on this street. OddEvenBoth    | then the implementation is required to   |
|                        |                           |              |              | must be "both".                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_streets   | ``xs:boolean``            | Optional     | Single       | If true, covers all streets in the city. | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| odd_even_both          | :ref:`multi-csv-oeb-enum` | **Required** | Single       | Specifies whether odd, even, or both     | If OddEvenBoth is missing or invalid,    |
|                        |                           |              |              | sides of the street are included from    | the implementation is required to ignore |
|                        |                           |              |              | :ref:`multi-csv-oeb-enum`.               | the StreetSegment containing it.         |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_id            | ``xs:IDREF``              | **Required** | Single       | References the containing                | If the field is invalid, then the        |
|                        |                           |              |              | :ref:`multi-csv-precinct`.               | implementation is required to ignore the |
|                        |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_house_number     | ``xs:integer``            | Optional     | Single       | Starting house number for the segment    | If the field is invalid or not present,  |
|                        |                           |              |              | range.                                   | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_house_number       | ``xs:integer``            | Optional     | Single       | Ending house number for the segment      | If the field is invalid or not present,  |
|                        |                           |              |              | range.                                   | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_prefix    | ``xs:string``             | Optional     | Single       | Prefix to the house number if any.       | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_suffix    | ``xs:string``             | Optional     | Single       | Suffix to the house number if any.       | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| region                 | ``xs:string``             | **Required** | Single       | State, province, or primary sub-national | If the field is invalid, then the        |
|                        |                           |              |              | region (e.g. "VA").                      | implementation is required to ignore the |
|                        |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| country                | ``xs:string``             | Optional     | Single       | Country code or name (e.g. "USA").       | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_direction       | ``xs:string``             | Optional     | Single       | Leading directional prefix for the       | If the field is invalid or not present,  |
|                        |                           |              |              | street (e.g. "N", "NW").                 | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_name            | ``xs:string``             | Optional     | Single       | Street name.                             | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_suffix          | ``xs:string``             | Optional     | Single       | Street type suffix (e.g. "St", "Ave",    | If the field is invalid or not present,  |
|                        |                           |              |              | "Rd").                                   | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| unit_number            | ``xs:string``             | Optional     | Repeats      | Unit, apartment, or suite number(s).     | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| postal_code            | ``xs:string``             | Optional     | Single       | Postal code or ZIP code.                 | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,address_direction,city,includes_all_addresses,includes_all_streets,odd_even_both,precinct_id,start_house_number,end_house_number,house_number_prefix,house_number_suffix,region,country,street_direction,street_name,street_suffix,unit_number,postal_code
    ss000001,N,Washington,false,false,odd,pre90113,101,199,,,DC,USA,NW,Delaware,St,,20001
    ss000002,S,Washington,true,false,both,pre90112,,,,,DC,USA,SE,Wisconsin,Ave,,20002
