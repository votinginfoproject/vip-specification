.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-street-segment:

street_segment
==============

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address, in which case these values
are equal.

+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+===========================+==============+==============+==========================================+==========================================+
| address_direction      | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                        |                           |              |              | of the entire address. An example is     | then the implementation is required to   |
|                        |                           |              |              | "NE" for the address "100 E Capitol St   | ignore it.                               |
|                        |                           |              |              | NE."                                     |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city                   | ``xs:string``             | **Required** | Single       | The city specifies the city or town of   | If the field is invalid, then the        |
|                        |                           |              |              | the address.                             | implementation is required to ignore it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_addresses | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                        |                           |              |              | address on this street. If this is       | then the implementation is required to   |
|                        |                           |              |              | *true*, then the values of               | ignore it.                               |
|                        |                           |              |              | **StartHouseNumber** and                 |                                          |
|                        |                           |              |              | **EndHouseNumber** should be ignored.    |                                          |
|                        |                           |              |              | The value of **OddEvenBoth** must be     |                                          |
|                        |                           |              |              | *both*.                                  |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| includes_all_streets   | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                        |                           |              |              | street in this city. If this is *true*,  | then the implementation is required to   |
|                        |                           |              |              | then the values of **OddEvenBoth**,      | ignore it.                               |
|                        |                           |              |              | **StartHouseNumber**,                    |                                          |
|                        |                           |              |              | **EndHouseNumber**, **StreetName**, and  |                                          |
|                        |                           |              |              | **Zip** should be ignored.               |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| odd_even_both          | :ref:`multi-csv-oeb-enum` | Optional     | Single       | Specifies whether the odd side of the    | If the field is not present or invalid,  |
|                        |                           |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                        |                           |              |              | even side, or both are in included in    | the StreetSegment containing it.         |
|                        |                           |              |              | the street segment.                      |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_id            | ``xs:IDREF``              | Optional     | Single       | References the :ref:`multi-csv-precinct` | If the field is not present or invalid,  |
|                        |                           |              |              | that contains the entire street segment. | the implementation is required to ignore |
|                        |                           |              |              |                                          | the StreetSegment element containing it. |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_house_number     | ``xs:integer``            | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** or       |
|                        |                           |              |              | segment starts. This value is necessary  | **IncludesAllStreets** are true, if the  |
|                        |                           |              |              | for the street segment to make any       | field is not present or invalid, the     |
|                        |                           |              |              | sense. Unless **IncludesAllAddresses**   | implementation is required to ignore the |
|                        |                           |              |              | or **IncludesAllStreets** are true, this | StreetSegment element containing it. If  |
|                        |                           |              |              | value must be less than or equal to      | the **StartHouseNumber** is greater than |
|                        |                           |              |              | **EndHouseNumber**. If                   | the **EndHouseNumber**, the              |
|                        |                           |              |              | **IncludesAllAddresses** or              | implementation should ignore the element |
|                        |                           |              |              | **IncludesAllStreets** are true, this    | containing them.                         |
|                        |                           |              |              | value is ignored.                        |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_house_number       | ``xs:integer``            | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** or       |
|                        |                           |              |              | segment ends. This value is necessary    | **IncludesAllStreets** are true, if the  |
|                        |                           |              |              | for the street segment to make any       | field is not present or invalid, the     |
|                        |                           |              |              | sense. Unless **IncludesAllAddresses**   | implementation is required to ignore the |
|                        |                           |              |              | or **IncludesAllStreets** are true, it   | StreetSegment element containing it. If  |
|                        |                           |              |              | must be greater than or equal to         | the **EndHouseNumber** is less than the  |
|                        |                           |              |              | **StartHouseNumber**. If                 | **StartHouseNumber**, the implementation |
|                        |                           |              |              | **IncludesAllAddresses** or              | should ignore the element containing it. |
|                        |                           |              |              | **IncludesAllStreets** are true, this    |                                          |
|                        |                           |              |              | value is ignored.                        |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_prefix    | ``xs:string``             | Optional     | Single       | Part of a street address. It may contain | If the field is not present of invalid,  |
|                        |                           |              |              | letters or slashes (e.g., 'B' in 'B22    | the implementation is required to ignore |
|                        |                           |              |              | Main St')                                | it.                                      |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| house_number_suffix    | ``xs:string``             | Optional     | Single       | Part of a street address. It may contain | If the field is not present of invalid,  |
|                        |                           |              |              | letters or slashes (e.g., 1/2 in '22 1/2 | the implementation is required to ignore |
|                        |                           |              |              | Main St')                                | it.                                      |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state                  | ``xs:string``             | **Required** | Single       | Specifies the two-letter state           | If the field is invalid, then the        |
|                        |                           |              |              | abbreviation of the address.             | implementation is required to ignore it. |
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
|                        |                           |              |              | "100 E Capitol St NE."                   |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| unit_number            | ``xs:string``             | Optional     | Repeats      | The apartment/unit number for a street   | If the field is invalid or not present,  |
|                        |                           |              |              | segment. If this value is present then   | then the implementation is required to   |
|                        |                           |              |              | **StartHouseNumber** must be equal to    | ignore it.                               |
|                        |                           |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                        |                           |              |              | used if **IncludesAllAddresses** or      |                                          |
|                        |                           |              |              | **IncludesAllStreets** are true.         |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| zip                    | ``xs:string``             | Optional     | Single       | Specifies the zip code of the address.   | If the field is invalid or not present,  |
|                        |                           |              |              | It may be 5 or 9 digits, and it may      | then the implementation is required to   |
|                        |                           |              |              | include a hyphen ('-'). It is required   | ignore it.                               |
|                        |                           |              |              | as it helps with geocoding, which is     |                                          |
|                        |                           |              |              | crucial for distributors.                |                                          |
+------------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,address_direction,city,includes_all_addresses,includes_all_streets,odd_even_both,precinct_id,start_house_number,end_house_number,state,street_direction,street_name,street_suffix,unit_number,zip
    ss000001,N,Washington,false,false,odd,pre90113,101,199,DC,NW,Delaware,St,,20001
    ss000002,S,Washington,true,false,both,pre90112,,,DC,SE,Wisconsin,Ave,,20002
