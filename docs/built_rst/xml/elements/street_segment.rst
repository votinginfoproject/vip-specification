.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-street-segment:

StreetSegment
=============

A StreetSegment object represents a range of house numbers along a street and links them to the containing :ref:`multi-xml-precinct`. Street segments are excluded from feed overlays.

+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===========================+==============+==============+==========================================+==========================================+
| AddressDirection     | ``xs:string``             | Optional     | Single       | Specifies trailing directional component | If the field is invalid or not present,  |
|                      |                           |              |              | of the address (e.g. "NE").              | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City                 | ``xs:string``             | **Required** | Single       | City or municipality name.               | If the field is invalid, then the        |
|                      |                           |              |              |                                          | implementation is required to ignore the |
|                      |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllAddresses | ``xs:boolean``            | Optional     | Single       | If true, the segment covers all          | If the field is invalid or not present,  |
|                      |                           |              |              | addresses on this street. OddEvenBoth    | then the implementation is required to   |
|                      |                           |              |              | must be "both".                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllStreets   | ``xs:boolean``            | Optional     | Single       | If true, covers all streets in the city. | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OddEvenBoth          | :ref:`multi-xml-oeb-enum` | **Required** | Single       | Specifies whether odd, even, or both     | If OddEvenBoth is missing or invalid,    |
|                      |                           |              |              | sides of the street are included from    | the implementation is required to ignore |
|                      |                           |              |              | :ref:`multi-xml-oeb-enum`.               | the StreetSegment containing it.         |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctId           | ``xs:IDREF``              | **Required** | Single       | References the containing                | If the field is invalid, then the        |
|                      |                           |              |              | :ref:`multi-xml-precinct`.               | implementation is required to ignore the |
|                      |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartHouseNumber     | ``xs:integer``            | Optional     | Single       | Starting house number for the segment    | If the field is invalid or not present,  |
|                      |                           |              |              | range.                                   | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndHouseNumber       | ``xs:integer``            | Optional     | Single       | Ending house number for the segment      | If the field is invalid or not present,  |
|                      |                           |              |              | range.                                   | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HouseNumberPrefix    | ``xs:string``             | Optional     | Single       | Prefix to the house number if any.       | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HouseNumberSuffix    | ``xs:string``             | Optional     | Single       | Suffix to the house number if any.       | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Region               | ``xs:string``             | **Required** | Single       | State, province, or primary sub-national | If the field is invalid, then the        |
|                      |                           |              |              | region (e.g. "VA").                      | implementation is required to ignore the |
|                      |                           |              |              |                                          | ``StreetSegment`` element containing it. |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Country              | ``xs:string``             | Optional     | Single       | Country code or name (e.g. "USA").       | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection      | ``xs:string``             | Optional     | Single       | Leading directional prefix for the       | If the field is invalid or not present,  |
|                      |                           |              |              | street (e.g. "N", "NW").                 | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName           | ``xs:string``             | Optional     | Single       | Street name.                             | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix         | ``xs:string``             | Optional     | Single       | Street type suffix (e.g. "St", "Ave",    | If the field is invalid or not present,  |
|                      |                           |              |              | "Rd").                                   | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| UnitNumber           | ``xs:string``             | Optional     | Repeats      | Unit, apartment, or suite number(s).     | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostalCode           | ``xs:string``             | Optional     | Single       | Postal code or ZIP code.                 | If the field is invalid or not present,  |
|                      |                           |              |              |                                          | then the implementation is required to   |
|                      |                           |              |              |                                          | ignore it.                               |
+----------------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <StreetSegment id="ss999999">
      <City>Charlottesville</City>
      <IncludesAllAddresses>true</IncludesAllAddresses>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre99999</PrecinctId>
      <Region>VA</Region>
      <Country>USA</Country>
      <StreetName>CHAPEL HILL</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <PostalCode>22901</PostalCode>
   </StreetSegment>
