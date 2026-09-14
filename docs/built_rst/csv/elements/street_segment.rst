.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-street-segment:

street_segment
==============

A StreetSegment object represents a range of house numbers along a street and links them to the containing :ref:`multi-csv-precinct`. Street segments are excluded from feed overlays.

+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+===========================+==============+==============+==========================================+==========================================+
| address_direction      | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                        |                           |              |              | of the entire address. An example is     | then the implementation is required to   |
|                        |                           |              |              | "NE" for the address "100 E Capitol St   | ignore it.                               |
|                        |                           |              |              | NE."                                     |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city                   | ``xs:string``             | **Required** | Single       | The city specifies the city or town of   | If the field is invalid, then the        |
|                        |                           |              |              | the address (e.g. "Richmond",            | implementation is required to ignore the |
|                        |                           |              |              | "Springfield").                          | ``StreetSegment`` element containing it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_addresses | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                        |                           |              |              | address on this street. If this is true, | then the implementation is required to   |
|                        |                           |              |              | then the values of StartHouseNumber and  | ignore it.                               |
|                        |                           |              |              | EndHouseNumber should be ignored. The    |                                          |
|                        |                           |              |              | value of OddEvenBoth must be "both".     |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_streets   | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                        |                           |              |              | street in this city. If this is true,    | then the implementation is required to   |
|                        |                           |              |              | then the values of OddEvenBoth,          | ignore it.                               |
|                        |                           |              |              | StartHouseNumber, EndHouseNumber,        |                                          |
|                        |                           |              |              | StreetName, and PostalCode should be     |                                          |
|                        |                           |              |              | ignored.                                 |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| odd_even_both          | :ref:`multi-csv-oeb-enum` | **Required** | Single       | Specifies whether the odd side of the    | If OddEvenBoth is missing or invalid,    |
|                        |                           |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                        |                           |              |              | even side, or both are included in the   | the StreetSegment containing it.         |
|                        |                           |              |              | street segment from                      |                                          |
|                        |                           |              |              | :ref:`multi-csv-oeb-enum`.               |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_id            | ``xs:IDREF``              | **Required** | Single       | References the :ref:`multi-csv-precinct` | If the field is invalid, then the        |
|                        |                           |              |              | that contains the entire street segment. | implementation is required to ignore the |
|                        |                           |              |              | If a precinct has a                      | ``StreetSegment`` element containing it. |
|                        |                           |              |              | :ref:`multi-csv-spatial-boundary` which  |                                          |
|                        |                           |              |              | also contains the entire street segment, |                                          |
|                        |                           |              |              | then the precinct assignment from the    |                                          |
|                        |                           |              |              | segment will be preferred over the       |                                          |
|                        |                           |              |              | assignment defined by the spatial        |                                          |
|                        |                           |              |              | boundary.                                |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_house_number     | ``xs:integer``            | Optional     | Single       | The house number at which the street     | If the field is invalid or not present,  |
|                        |                           |              |              | segment starts (e.g. 100). This value is | then the implementation is required to   |
|                        |                           |              |              | necessary for the street segment to make | ignore it.                               |
|                        |                           |              |              | any sense. Unless IncludesAllAddresses   |                                          |
|                        |                           |              |              | or IncludesAllStreets are true, this     |                                          |
|                        |                           |              |              | value must be less than or equal to      |                                          |
|                        |                           |              |              | EndHouseNumber. If IncludesAllAddresses  |                                          |
|                        |                           |              |              | or IncludesAllStreets are true, this     |                                          |
|                        |                           |              |              | value is ignored.                        |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_house_number       | ``xs:integer``            | Optional     | Single       | The house number at which the street     | If the field is invalid or not present,  |
|                        |                           |              |              | segment ends (e.g. 198). This value is   | then the implementation is required to   |
|                        |                           |              |              | necessary for the street segment to make | ignore it.                               |
|                        |                           |              |              | any sense. Unless IncludesAllAddresses   |                                          |
|                        |                           |              |              | or IncludesAllStreets are true, it must  |                                          |
|                        |                           |              |              | be greater than or equal to              |                                          |
|                        |                           |              |              | StartHouseNumber. If                     |                                          |
|                        |                           |              |              | IncludesAllAddresses or                  |                                          |
|                        |                           |              |              | IncludesAllStreets are true, this value  |                                          |
|                        |                           |              |              | is ignored.                              |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_prefix    | ``xs:string``             | Optional     | Single       | Part of a street address. It may contain | If the field is invalid or not present,  |
|                        |                           |              |              | letters or slashes (e.g., 'B' in 'B22    | then the implementation is required to   |
|                        |                           |              |              | Main St'). If this value is present then | ignore it.                               |
|                        |                           |              |              | StartHouseNumber must be equal to        |                                          |
|                        |                           |              |              | EndHouseNumber. This field cannot be     |                                          |
|                        |                           |              |              | used if IncludesAllAddresses or          |                                          |
|                        |                           |              |              | IncludesAllStreets are true.             |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_suffix    | ``xs:string``             | Optional     | Single       | Part of a street address. It may contain | If the field is invalid or not present,  |
|                        |                           |              |              | letters or slashes (e.g., 1/2 in '22 1/2 | then the implementation is required to   |
|                        |                           |              |              | Main St'). If this value is present then | ignore it.                               |
|                        |                           |              |              | StartHouseNumber must be equal to        |                                          |
|                        |                           |              |              | EndHouseNumber. This field cannot be     |                                          |
|                        |                           |              |              | used if IncludesAllAddresses or          |                                          |
|                        |                           |              |              | IncludesAllStreets are true.             |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| region                 | ``xs:string``             | **Required** | Single       | State, province, or primary sub-national | If the field is invalid, then the        |
|                        |                           |              |              | region (e.g. "VA").                      | implementation is required to ignore the |
|                        |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| country                | ``xs:string``             | Optional     | Single       | Country code or name (e.g. "USA").       | If the field is invalid or not present,  |
|                        |                           |              |              |                                          | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_direction       | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                        |                           |              |              | of the street address (e.g., the "E" in  | then the implementation is required to   |
|                        |                           |              |              | "100 E Capitol St NE").                  | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_name            | ``xs:string``             | Optional     | Single       | Represents the name of the street for    | If the field is invalid or not present,  |
|                        |                           |              |              | the address. A special wildcard, "*",    | then the implementation is required to   |
|                        |                           |              |              | denotes every street in the given        | ignore it.                               |
|                        |                           |              |              | city/town. It optionally may contain     |                                          |
|                        |                           |              |              | street direction, street suffix or       |                                          |
|                        |                           |              |              | address direction (e.g., both "Capitol"  |                                          |
|                        |                           |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                        |                           |              |              | the address "100 E Capitol St NE"),      |                                          |
|                        |                           |              |              | however this is not preferred. Preferred |                                          |
|                        |                           |              |              | is street name alone (e.g. "Capitol").   |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| street_suffix          | ``xs:string``             | Optional     | Single       | Represents the abbreviated,              | If the field is invalid or not present,  |
|                        |                           |              |              | non-directional suffix to the street     | then the implementation is required to   |
|                        |                           |              |              | name. An example is "St" for the address | ignore it.                               |
|                        |                           |              |              | "100 E Capitol St NE", or "Ave", "Rd",   |                                          |
|                        |                           |              |              | "Blvd".                                  |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| unit_number            | ``xs:string``             | Optional     | Repeats      | The apartment/unit number for a street   | If the field is invalid or not present,  |
|                        |                           |              |              | segment (e.g. "Apt 3B"). If this value   | then the implementation is required to   |
|                        |                           |              |              | is present then StartHouseNumber must be | ignore it.                               |
|                        |                           |              |              | equal to EndHouseNumber. This field      |                                          |
|                        |                           |              |              | cannot be used if IncludesAllAddresses   |                                          |
|                        |                           |              |              | or IncludesAllStreets are true.          |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| postal_code            | ``xs:string``             | Optional     | Single       | Specifies the postal or ZIP code of the  | If the field is invalid or not present,  |
|                        |                           |              |              | address (e.g. "22902" or "22902-1234").  | then the implementation is required to   |
|                        |                           |              |              |                                          | ignore it.                               |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,address_direction,city,includes_all_addresses,includes_all_streets,odd_even_both,precinct_id,start_house_number,end_house_number,house_number_prefix,house_number_suffix,region,country,street_direction,street_name,street_suffix,unit_number,postal_code
    ss000001,N,Washington,false,false,odd,pre90113,101,199,,,DC,USA,NW,Delaware,St,,20001
    ss000002,S,Washington,true,false,both,pre90112,,,,,DC,USA,SE,Wisconsin,Ave,,20002
