StreetSegment
=============

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address in which case these values
are equal.

+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| Tag                  | Data Type                               | Required?    | Repeats?   | Description            | Error Handling         |
|                      |                                         |              |            |                        |                        |
+======================+=========================================+==============+============+========================+========================+
| AddressDirection     | xs:string                               | Optional    | Single      |Specifies the           |If the field is not     |
|                      |                                         |             |             |(inter-)cardinal        |present or invalid, the |
|                      |                                         |             |             |direction of the        |implementation is       |
|                      |                                         |             |             |entire address. An      |required to ignore it.  |
|                      |                                         |             |             |example is "NE" for     |                        |
|                      |                                         |             |             |the address "100 E      |                        |
|                      |                                         |             |             |Capitol St NE."         |                        |
|                      |                                         |             |             |                        |                        |
+----------------------+-----------------------------------------+-------------+-------------+------------------------+------------------------+
| City                 | xs:string                               | **Required**| Single      |The city specifies the  |If the field is not     |
|                      |                                         |             |             |city or town of the     |present or invalid, the |
|                      |                                         |             |             |address.                |implementation is       |
|                      |                                         |             |             |                        |required to ignore the  |
|                      |                                         |             |             |                        |element containing it.  |
+----------------------+-----------------------------------------+-------------+-------------+------------------------+------------------------+
| IncludesAllAddresses | xs:boolean                              | Optional     | Single     |Specifies if the segment|If the field is not     |
|                      |                                         |              |            |covers every address on |present or invalid, the |
|                      |                                         |              |            |this street. If this is |implementation is       |
|                      |                                         |              |            |*true*, then the values |required to ignore it.  |
|                      |                                         |              |            |of **StartHouseNumber** |                        |
|                      |                                         |              |            |and **EndHouseNumber**  |                        |
|                      |                                         |              |            |should be ignored. The  |                        |
|                      |                                         |              |            |value of **OddEvenBoth**|                        |
|                      |                                         |              |            |must be *both*.         |                        |
|                      |                                         |              |            |                        |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| OddEvenBoth          |:doc:`OebEnum <../enumerations/oeb_enum>`| **Required** | Single     |Specifies whether the   |If the field is not     |
|                      |                                         |              |            |odd side of the street  |present or invalid, the |
|                      |                                         |              |            |(in terms of house      |implementation is       |
|                      |                                         |              |            |numbers), the even side,|required to ignore the  |
|                      |                                         |              |            |or both are in included |StreetSegment containing|
|                      |                                         |              |            |in the street segment.  |it.                     |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
|                      |                                         |              |            |                        |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| PrecinctId           | xs:IDREF                                | Optional     | Single     |References the          |If the field is not     |
|                      |                                         |              |            |:doc:`precinct          |present or invalid, the |
|                      |                                         |              |            |<precinct>` that        |implementation is       |
|                      |                                         |              |            |contains the entire     |required to ignore the  |
|                      |                                         |              |            |street segment.         |StreetSegment element   |
|                      |                                         |              |            |                        |containing it.          |
|                      |                                         |              |            |                        |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| StartHouseNumber     | xs:integer                              | Optional     | Single     |The house number at     |Unless                  |
|                      |                                         |              |            |which the street        |**IncludesAllAddresses**|
|                      |                                         |              |            |segment starts. This    |is true, if the field is|
|                      |                                         |              |            |value is necessary for  |not present or invalid, |
|                      |                                         |              |            |the street segment to   |the implementation is   |
|                      |                                         |              |            |make any sense. Unless  |required to ignore the  |
|                      |                                         |              |            |**IncludesAllAddresses**|street segment element  |
|                      |                                         |              |            |is true, this value must|containing it. If the   |
|                      |                                         |              |            |be less than or equal to|**StartHouseNumber** is |
|                      |                                         |              |            |**EndHouseNumber**. If  |greater than the        |
|                      |                                         |              |            |**IncludesAllAddresses**|**EndHouseNumber**, the |
|                      |                                         |              |            |is true, this value is  |implementation should   |
|                      |                                         |              |            |ignored.                |ignore the element      |
|                      |                                         |              |            |                        |containing them.        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| EndHouseNumber       | xs:integer                              | Optional     | Single     |The house number at     |Unless                  |
|                      |                                         |              |            |which the street        |**IncludesAllAddresses**|
|                      |                                         |              |            |segment ends. This      |is true, if the field is|
|                      |                                         |              |            |value is necessary for  |not present or invalid, |
|                      |                                         |              |            |the street segment to   |the implementation is   |
|                      |                                         |              |            |make any sense. Unless  |required to ignore the  |
|                      |                                         |              |            |**IncludesAllAddresses**|street segment element  |
|                      |                                         |              |            |is true, it must be     |containing it. If the   |
|                      |                                         |              |            |greater than or equal to|**EndHouseNumber** is   |
|                      |                                         |              |            |**StartHouseNumber**. If|less than the           |
|                      |                                         |              |            |**IncludesAllAddresses**|**StartHouseNumber**,   |
|                      |                                         |              |            |is true, this value is  |the implementation      |
|                      |                                         |              |            |ignored.                |should ignore the       |
|                      |                                         |              |            |                        |element containing it.  |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| State                | xs:string                               | **Required** | Single     |Specifies the           |If the field is not     |
|                      |                                         |              |            |two-letter state        |present or invalid, the |
|                      |                                         |              |            |abbreviation of the     |implementation is       |
|                      |                                         |              |            |address.                |required to ignore the  |
|                      |                                         |              |            |                        |element containing it.  |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| StreetDirection      | xs:string                               | Optional     | Single     |Specifies the           |If the field is not     |
|                      |                                         |              |            |(inter-)cardinal        |present or invalid, the |
|                      |                                         |              |            |direction of the        |implementation is       |
|                      |                                         |              |            |street address (e.g.,   |required to ignore it.  |
|                      |                                         |              |            |the "E" in "100 E       |                        |
|                      |                                         |              |            |Capitol St NE").        |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| StreetName           | xs:string                               | **Required** | Single     |Represents the name of  |If the field is not     |
|                      |                                         |              |            |the street for the      |present or invalid, the |
|                      |                                         |              |            |address. A special      |implementation is       |
|                      |                                         |              |            |wildcard, "*", denotes  |required to ignore the  |
|                      |                                         |              |            |every street in the     |element containing it.  |
|                      |                                         |              |            |given city/town. It     |                        |
|                      |                                         |              |            |optionally may contain  |                        |
|                      |                                         |              |            |street direction,       |                        |
|                      |                                         |              |            |street suffix or        |                        |
|                      |                                         |              |            |address direction       |                        |
|                      |                                         |              |            |(e.g., both "Capitol"   |                        |
|                      |                                         |              |            |and "E Capitol St NE"   |                        |
|                      |                                         |              |            |are acceptable for the  |                        |
|                      |                                         |              |            |address "100 E Capitol  |                        |
|                      |                                         |              |            |St NE"), however this   |                        |
|                      |                                         |              |            |is not                  |                        |
|                      |                                         |              |            |preferred. Preferred    |                        |
|                      |                                         |              |            |is street name alone    |                        |
|                      |                                         |              |            |(e.g. "Capitol").       |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| StreetSuffix         | xs:string                               | Optional     | Single     |Represents the          |If the field is not     |
|                      |                                         |              |            |abbreviated,            |present or invalid, the |
|                      |                                         |              |            |non-directional suffix  |implementation is       |
|                      |                                         |              |            |to the street name. An  |required to ignore it.  |
|                      |                                         |              |            |example is "St" for     |                        |
|                      |                                         |              |            |the address "100 E      |                        |
|                      |                                         |              |            |Capitol St NE."         |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| UnitNumber           | xs:string                               | Optional     | Repeats    |The apartment/unit      |If the field is not     |
|                      |                                         |              |            |number for a street     |present or invalid, the |
|                      |                                         |              |            |segment. If this value  |implementation is       |
|                      |                                         |              |            |is present then         |required to ignore it.  |
|                      |                                         |              |            |**StartHouseNumber**    |                        |
|                      |                                         |              |            |must be equal to        |                        |
|                      |                                         |              |            |**EndHouseNumber**. This|                        |
|                      |                                         |              |            |field cannot be used if |                        |
|                      |                                         |              |            |**IncludesAllAddresses**|                        |
|                      |                                         |              |            |is true.                |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
| Zip                  | xs:string                               | **Required** | Single     |Specifies the zip code  |If the field is not     |
|                      |                                         |              |            |of the address. It may  |present or invalid, the |
|                      |                                         |              |            |be 5 or 9 digits, and   |implementation is       |
|                      |                                         |              |            |it may include a        |required to ignore the  |
|                      |                                         |              |            |hyphen ('-'). It is     |element containing it.  |
|                      |                                         |              |            |required as it helps    |                        |
|                      |                                         |              |            |with geocoding, which   |                        |
|                      |                                         |              |            |is crucial for          |                        |
|                      |                                         |              |            |distributors.           |                        |
+----------------------+-----------------------------------------+--------------+------------+------------------------+------------------------+
