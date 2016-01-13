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
| AddressDirection     | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                      |                           |              |              | of the entire address. An example is     | then the implementation is required to   |
|                      |                           |              |              | "NE" for the address "100 E Capitol St   | ignore it.                               |
|                      |                           |              |              | NE."                                     |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City                 | ``xs:string``             | **Required** | Single       | The city specifies the city or town of   | If the field is invalid, then the        |
|                      |                           |              |              | the address.                             | implementation is required to ignore it. |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllAddresses | ``xs:boolean``            | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                      |                           |              |              | address on this street. If this is       | then the implementation is required to   |
|                      |                           |              |              | *true*, then the values of               | ignore it.                               |
|                      |                           |              |              | **StartHouseNumber** and                 |                                          |
|                      |                           |              |              | **EndHouseNumber** should be ignored.    |                                          |
|                      |                           |              |              | The value of **OddEvenBoth** must be     |                                          |
|                      |                           |              |              | *both*.                                  |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OddEvenBoth          | :ref:`multi-xml-oeb-enum` | **Required** | Single       | Specifies whether the odd side of the    | If the field is not present or invalid,  |
|                      |                           |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                      |                           |              |              | even side, or both are in included in    | the StreetSegment containing it.         |
|                      |                           |              |              | the street segment.                      |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctId           | ``xs:IDREF``              | Optional     | Single       | References the :doc:`precinct            | If the field is not present or invalid,  |
|                      |                           |              |              | <precinct>` that contains the entire     | the implementation is required to ignore |
|                      |                           |              |              | street segment.                          | the StreetSegment element containing it. |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartHouseNumber     | ``xs:integer``            | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** is true, |
|                      |                           |              |              | segment starts. This value is necessary  | if the field is not present or invalid,  |
|                      |                           |              |              | for the street segment to make any       | the implementation is required to ignore |
|                      |                           |              |              | sense. Unless **IncludesAllAddresses**   | the StreetSegment element containing it. |
|                      |                           |              |              | is true, this value must be less than or | If the **StartHouseNumber** is greater   |
|                      |                           |              |              | equal to **EndHouseNumber**. If          | than the **EndHouseNumber**, the         |
|                      |                           |              |              | **IncludesAllAddresses** is true, this   | implementation should ignore the element |
|                      |                           |              |              | value is ignored.                        | containing them.                         |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndHouseNumber       | ``xs:integer``            | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** is true, |
|                      |                           |              |              | segment ends. This value is necessary    | if the field is not present or invalid,  |
|                      |                           |              |              | for the street segment to make any       | the implementation is required to ignore |
|                      |                           |              |              | sense. Unless **IncludesAllAddresses**   | the StreetSegment element containing it. |
|                      |                           |              |              | is true, it must be greater than or      | If the **EndHouseNumber** is less than   |
|                      |                           |              |              | equal to **StartHouseNumber**. If        | the **StartHouseNumber**, the            |
|                      |                           |              |              | **IncludesAllAddresses** is true, this   | implementation should ignore the element |
|                      |                           |              |              | value is ignored.                        | containing it.                           |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State                | ``xs:string``             | **Required** | Single       | Specifies the two-letter state           | If the field is invalid, then the        |
|                      |                           |              |              | abbreviation of the address.             | implementation is required to ignore it. |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection      | ``xs:string``             | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                      |                           |              |              | of the street address (e.g., the "E" in  | then the implementation is required to   |
|                      |                           |              |              | "100 E Capitol St NE").                  | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName           | ``xs:string``             | **Required** | Single       | Represents the name of the street for    | If the field is invalid, then the        |
|                      |                           |              |              | the address. A special wildcard, "*",    | implementation is required to ignore it. |
|                      |                           |              |              | denotes every street in the given        |                                          |
|                      |                           |              |              | city/town. It optionally may contain     |                                          |
|                      |                           |              |              | street direction, street suffix or       |                                          |
|                      |                           |              |              | address direction (e.g., both "Capitol"  |                                          |
|                      |                           |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                      |                           |              |              | the address "100 E Capitol St NE"),      |                                          |
|                      |                           |              |              | however this is not preferred. Preferred |                                          |
|                      |                           |              |              | is street name alone (e.g. "Capitol").   |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix         | ``xs:string``             | Optional     | Single       | Represents the abbreviated,              | If the field is invalid or not present,  |
|                      |                           |              |              | non-directional suffix to the street     | then the implementation is required to   |
|                      |                           |              |              | name. An example is "St" for the address | ignore it.                               |
|                      |                           |              |              | "100 E Capitol St NE."                   |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| UnitNumber           | ``xs:string``             | Optional     | Repeats      | The apartment/unit number for a street   | If the field is invalid or not present,  |
|                      |                           |              |              | segment. If this value is present then   | then the implementation is required to   |
|                      |                           |              |              | **StartHouseNumber** must be equal to    | ignore it.                               |
|                      |                           |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                      |                           |              |              | used if **IncludesAllAddresses** is      |                                          |
|                      |                           |              |              | true.                                    |                                          |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip                  | ``xs:string``             | **Required** | Single       | Specifies the zip code of the address.   | If the field is invalid, then the        |
|                      |                           |              |              | It may be 5 or 9 digits, and it may      | implementation is required to ignore it. |
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
