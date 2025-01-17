.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-street-segment:

StreetSegment
=============

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address, in which case these values
are equal.

+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===========================+==============+==============+==========================================+==========================================+
| AddressDirection     | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction |                                          |
|                      |                           |              |              | of the entire address. An example is     |                                          |
|                      |                           |              |              | "NE" for the address "100 E Capitol St   |                                          |
|                      |                           |              |              | NE."                                     |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City                 | ``xs:string``             | **Required** | Single       | The city specifies the city or town of   |                                          |
|                      |                           |              |              | the address.                             |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllAddresses | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    |                                          |
|                      |                           |              |              | address on this street. If this is       |                                          |
|                      |                           |              |              | *true*, then the values of               |                                          |
|                      |                           |              |              | **StartHouseNumber** and                 |                                          |
|                      |                           |              |              | **EndHouseNumber** should be ignored.    |                                          |
|                      |                           |              |              | The value of **OddEvenBoth** must be     |                                          |
|                      |                           |              |              | *both*.                                  |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllStreets   | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    |                                          |
|                      |                           |              |              | street in this city. If this is *true*,  |                                          |
|                      |                           |              |              | then the values of **OddEvenBoth**,      |                                          |
|                      |                           |              |              | **StartHouseNumber**,                    |                                          |
|                      |                           |              |              | **EndHouseNumber**, **StreetName**, and  |                                          |
|                      |                           |              |              | **Zip** should be ignored.               |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OddEvenBoth          | :ref:`multi-xml-oeb-enum` | **Required** | Single       | Specifies whether the odd side of the    | If the field is not present or invalid,  |
|                      |                           |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                      |                           |              |              | even side, or both are in included in    | the StreetSegment containing it.         |
|                      |                           |              |              | the street segment.                      |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctId           | ``xs:IDREF``              | **Required** | Single       | References the :ref:`multi-xml-precinct` |                                          |
|                      |                           |              |              | that contains the entire street segment. |                                          |
|                      |                           |              |              | If a precinct has a                      |                                          |
|                      |                           |              |              | :ref:`multi-xml-spatial-boundary` which  |                                          |
|                      |                           |              |              | also contains the entire street segment, |                                          |
|                      |                           |              |              | then the precinct assignment from the    |                                          |
|                      |                           |              |              | segment will be preferred over the       |                                          |
|                      |                           |              |              | assignment defined by the spatial        |                                          |
|                      |                           |              |              | boundary.                                |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartHouseNumber     | ``xs:integer``            | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** or       |
|                      |                           |              |              | segment starts. This value is necessary  | **IncludesAllStreets** are true, if the  |
|                      |                           |              |              | for the street segment to make any       | field is not present or invalid, the     |
|                      |                           |              |              | sense. Unless **IncludesAllAddresses**   | implementation is required to ignore the |
|                      |                           |              |              | or **IncludesAllStreets** are true, this | StreetSegment element containing it. If  |
|                      |                           |              |              | value must be less than or equal to      | the **StartHouseNumber** is greater than |
|                      |                           |              |              | **EndHouseNumber**. If                   | the **EndHouseNumber**, the              |
|                      |                           |              |              | **IncludesAllAddresses** or              | implementation should ignore the element |
|                      |                           |              |              | **IncludesAllStreets** are true, this    | containing them.                         |
|                      |                           |              |              | value is ignored.                        |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndHouseNumber       | ``xs:integer``            | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** or       |
|                      |                           |              |              | segment ends. This value is necessary    | **IncludesAllStreets** are true, if the  |
|                      |                           |              |              | for the street segment to make any       | field is not present or invalid, the     |
|                      |                           |              |              | sense. Unless **IncludesAllAddresses**   | implementation is required to ignore the |
|                      |                           |              |              | or **IncludesAllStreets** are true, it   | StreetSegment element containing it. If  |
|                      |                           |              |              | must be greater than or equal to         | the **EndHouseNumber** is less than the  |
|                      |                           |              |              | **StartHouseNumber**. If                 | **StartHouseNumber**, the implementation |
|                      |                           |              |              | **IncludesAllAddresses** or              | should ignore the element containing it. |
|                      |                           |              |              | **IncludesAllStreets** are true, this    |                                          |
|                      |                           |              |              | value is ignored.                        |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HouseNumberPrefix    | ``xs:string``             | Optional     | Single       | Part of a street address. It may contain |                                          |
|                      |                           |              |              | letters or slashes (e.g., 'B' in 'B22    |                                          |
|                      |                           |              |              | Main St'). If this value is present then |                                          |
|                      |                           |              |              | **StartHouseNumber** must be equal to    |                                          |
|                      |                           |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                      |                           |              |              | used if **IncludesAllAddresses** or      |                                          |
|                      |                           |              |              | **IncludesAllStreets** are true.         |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HouseNumberSuffix    | ``xs:string``             | Optional     | Single       | Part of a street address. It may contain |                                          |
|                      |                           |              |              | letters or slashes (e.g., 1/2 in '22 1/2 |                                          |
|                      |                           |              |              | Main St'). If this value is present then |                                          |
|                      |                           |              |              | **StartHouseNumber** must be equal to    |                                          |
|                      |                           |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                      |                           |              |              | used if **IncludesAllAddresses** or      |                                          |
|                      |                           |              |              | **IncludesAllStreets** are true.         |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State                | ``xs:string``             | **Required** | Single       | Specifies the two-letter state           |                                          |
|                      |                           |              |              | abbreviation of the address.             |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection      | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction |                                          |
|                      |                           |              |              | of the street address (e.g., the "E" in  |                                          |
|                      |                           |              |              | "100 E Capitol St NE").                  |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName           | ``xs:string``             | Optional     | Single       | Represents the name of the street for    |                                          |
|                      |                           |              |              | the address. A special wildcard, "*",    |                                          |
|                      |                           |              |              | denotes every street in the given        |                                          |
|                      |                           |              |              | city/town. It optionally may contain     |                                          |
|                      |                           |              |              | street direction, street suffix or       |                                          |
|                      |                           |              |              | address direction (e.g., both "Capitol"  |                                          |
|                      |                           |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                      |                           |              |              | the address "100 E Capitol St NE"),      |                                          |
|                      |                           |              |              | however this is not preferred. Preferred |                                          |
|                      |                           |              |              | is street name alone (e.g. "Capitol").   |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix         | ``xs:string``             | Optional     | Single       | Represents the abbreviated,              |                                          |
|                      |                           |              |              | non-directional suffix to the street     |                                          |
|                      |                           |              |              | name. An example is "St" for the address |                                          |
|                      |                           |              |              | "100 E Capitol St NE."                   |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| UnitNumber           | ``xs:string``             | Optional     | Repeats      | The apartment/unit number for a street   |                                          |
|                      |                           |              |              | segment. If this value is present then   |                                          |
|                      |                           |              |              | **StartHouseNumber** must be equal to    |                                          |
|                      |                           |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                      |                           |              |              | used if **IncludesAllAddresses** or      |                                          |
|                      |                           |              |              | **IncludesAllStreets** are true.         |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip                  | ``xs:string``             | Optional     | Single       | Specifies the zip code of the address.   |                                          |
|                      |                           |              |              | It may be 5 or 9 digits, and it may      |                                          |
|                      |                           |              |              | include a hyphen ('-'). It is required   |                                          |
|                      |                           |              |              | as it helps with geocoding, which is     |                                          |
|                      |                           |              |              | crucial for distributors.                |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <StreetSegment id="ss999999">
      <City>Charlottesville</City>
      <IncludesAllAddresses>true</IncludesAllAddresses>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre99999</PrecinctId>
      <State>VA</State>
      <StreetName>CHAPEL HILL</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <Zip>22901</Zip>
   </StreetSegment>
   <StreetSegment id="ss309904">
      <City>GREENWOOD</City>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre92145</PrecinctId>
      <StartHouseNumber>1</StartHouseNumber>
      <EndHouseNumber>201</EndHouseNumber>
      <State>VA</State>
      <StreetName>MISTY MOUNTAIN</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <Zip>22943</Zip>
   </StreetSegment>
   <StreetSegment id = "ss1"
      <City>GREENWOOD</City>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre92145</PrecinctId>
      <StartHouseNumber>1</StartHouseNumber>
      <EndHouseNumber>1</EndHouseNumber>
      <HouseNumberPrefix>B</HouseNumberPrefix>
      <HouseNumberSuffix>1/2</HouseNumberSuffix>
      <State>VA</State>
      <StreetName>MISTY MOUNTAIN</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <Zip>22943</Zip>
   </StreetSegment>
