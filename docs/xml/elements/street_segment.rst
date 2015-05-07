StreetSegment
=============

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address in which case these values
are equal.

.. todo::

   This documentation needs to be thoroughly checked for accuracy.

.. todo::

   The generator made some required fields optional (e.g. city, state, zip). Validate that the spec
   ensures the field is required.

+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+
| Tag             | Data Type                      | Required?    | Repeats?   | Description            | Error Handling         |
|                 |                                |              |            |                        |                        |
+=================+================================+==============+============+========================+========================+
| NonHouseAddress |:ref:`NonHouseAddress           | Optional     | Single     |The common street       |If the element is not   |
|                 |<non-house-address>`            |              |            |address (as well as     |present or invalid, the |
|                 |                                |              |            |city, state, and zip) of|implementation is       |
|                 |                                |              |            |the start and end points|required to ignore the  |
|                 |                                |              |            |of the segment. Specific|StreetSegment element   |
|                 |                                |              |            |information such as     |containing it           |
|                 |                                |              |            |street direction should |                        |
|                 |                                |              |            |be included.            |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+
| OddEvenBoth     | :doc:`OebEnum <oeb_enum>`      | Optional     | Single     |Specifies whether the   |If the field is not     |
|                 |                                |              |            |odd side of the street  |present or invalid, the |
|                 |                                |              |            |(in terms of house      |implementation is       |
|                 |                                |              |            |numbers), the even side,|required to ignore the  |
|                 |                                |              |            |or both are in included |StreetSegment containing|
|                 |                                |              |            |in the street segment.  |it.                     |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+
| PrecinctId      | xs:IDREF                       | Optional     | Single     |References the          |If the field is not     |
|                 |                                |              |            |:doc:`precinct          |present or invalid, the |
|                 |                                |              |            |<precinct>` that        |implementation is       |
|                 |                                |              |            |contains the entire     |required to ignore the  |
|                 |                                |              |            |street segment.         |StreetSegment element   |
|                 |                                |              |            |                        |containing it.          |
|                 |                                |              |            |                        |                        |
+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+
| StartHouseNumber| xs:integer                     | Optional     | Single     |The house number at     |If the field is not     |
|                 |                                |              |            |which the street        |present or invalid, the |
|                 |                                |              |            |segment starts. This    |implementation is       |
|                 |                                |              |            |value is very           |required to ignore the  |
|                 |                                |              |            |necessary for the       |street segment element  |
|                 |                                |              |            |street segment to make  |containing it. If the   |
|                 |                                |              |            |any sense. It must be   |**StartHouseNumber** is |
|                 |                                |              |            |less than (or equal     |greater than the        |
|                 |                                |              |            |to) the                 |**EndHouseNumber**, the |
|                 |                                |              |            |EndHouseNumber. To      |implementation should   |
|                 |                                |              |            |specify any house on    |ignore the element      |
|                 |                                |              |            |the street (or when     |containing them.        |
|                 |                                |              |            |using the "\*"          |                        |
|                 |                                |              |            |wildcard for street     |                        |
|                 |                                |              |            |name), the best         |                        |
|                 |                                |              |            |practice is to put 0    |                        |
|                 |                                |              |            |in this field.          |                        |
+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+
| EndHouseNumber  | xs:integer                     | Optional     | Single     |The house number at     |If the field is not     |
|                 |                                |              |            |which the street        |present or invalid, the |
|                 |                                |              |            |segment ends. This      |implementation is       |
|                 |                                |              |            |value is very           |required to ignore the  |
|                 |                                |              |            |necessary for the       |street segment element  |
|                 |                                |              |            |street segment to make  |containing it. If the   |
|                 |                                |              |            |any sense. It must be   |**EndHouseNumber** is   |
|                 |                                |              |            |greater than (or equal  |less than the           |
|                 |                                |              |            |to) the                 |**StartHouseNumber**,   |
|                 |                                |              |            |StartHouseNumber. To    |the implementation      |
|                 |                                |              |            |specify any house on    |should ignore the       |
|                 |                                |              |            |the street (or when     |element containing it.  |
|                 |                                |              |            |using the "\*"          |                        |
|                 |                                |              |            |wildcard for street     |                        |
|                 |                                |              |            |name), the best         |                        |
|                 |                                |              |            |practice is to put a    |                        |
|                 |                                |              |            |very large number such  |                        |
|                 |                                |              |            |as 999999 in this       |                        |
|                 |                                |              |            |field.                  |                        |
|                 |                                |              |            |                        |                        |
+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+
| UnitNumber      | xs:string                      | Optional     | Repeats    |The apartment/unit      |If the field is not     |
|                 |                                |              |            |number for a street     |present or invalid, the |
|                 |                                |              |            |segment. If this value  |implementation is       |
|                 |                                |              |            |is present then         |required to ignore it.  |
|                 |                                |              |            |**StartHouseNumber**    |                        |
|                 |                                |              |            |must be equal to        |                        |
|                 |                                |              |            |**EndHouseNumber**.     |                        |
|                 |                                |              |            |                        |                        |
|                 |                                |              |            |                        |                        |
+-----------------+--------------------------------+--------------+------------+------------------------+------------------------+

.. _non-house-address:

StreetSegment.NonHouseAddress
-----------------------------

+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| Tag               | Data Type  | Required?   | Repeats?    | Description          | Error Handling          |
|                   |            |             |             |                      |                         |
+===================+============+=============+=============+======================+=========================+
| AddressDirection  | xs:string  | Optional    | Single      |Specifies the         |If the field is not      |
|                   |            |             |             |(inter-)cardinal      |present or invalid, the  |
|                   |            |             |             |direction of the      |implementation is        |
|                   |            |             |             |entire address. An    |required to ignore it.   |
|                   |            |             |             |example is "NE" for   |                         |
|                   |            |             |             |the address "100 E    |                         |
|                   |            |             |             |Capitol St NE."       |                         |
|                   |            |             |             |                      |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| Apartment         | xs:string  | Optional    | Single      |Specifies the         |If the field is not      |
|                   |            |             |             |intra-building        |present or invalid, the  |
|                   |            |             |             |address. A prefix     |implementation is        |
|                   |            |             |             |(e.g. "Apt", "Suite") |required to ignore it.   |
|                   |            |             |             |is optional. Examples |                         |
|                   |            |             |             |are "Apt 303", "303", |                         |
|                   |            |             |             |"4G", "4th Floor."    |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| City              | xs:string  | **Required**| Single      |The city specifies the|If the field is not      |
|                   |            |             |             |city or town of the   |present or invalid, the  |
|                   |            |             |             |address.              |implementation is        |
|                   |            |             |             |                      |required to ignore the   |
|                   |            |             |             |                      |element containing it.   |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| HouseNumber       | xs:integer | Optional    | Single      |Specifies the house   |If the field is not      |
|                   |            |             |             |number part of a      |present or invalid, the  |
|                   |            |             |             |street address. It may|implementation is        |
|                   |            |             |             |only be numeric. It is|required to ignore it. If|
|                   |            |             |             |optional because: (1) |each of HouseNumber,     |
|                   |            |             |             |some addresses do not |HouseNumberSuffix, and   |
|                   |            |             |             |have numbers ("A      |HouseNumberPrefix is     |
|                   |            |             |             |Second St."), (2) some|blank, the address       |
|                   |            |             |             |addresses only have   |represents the entire    |
|                   |            |             |             |house number suffixes |street.                  |
|                   |            |             |             |("1/2 Second St."),   |                         |
|                   |            |             |             |and (3) a             |                         |
|                   |            |             |             |NonHouseAddress within|                         |
|                   |            |             |             |a StreetSegment should|                         |
|                   |            |             |             |not have a house      |                         |
|                   |            |             |             |number as it          |                         |
|                   |            |             |             |represents only the   |                         |
|                   |            |             |             |common aspects of the |                         |
|                   |            |             |             |address.              |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| HouseNumberPrefix | xs:string  | Optional    | Single      |Represents the house  |If the field is not      |
|                   |            |             |             |number part of a      |present or invalid, the  |
|                   |            |             |             |street address. It may|implementation is        |
|                   |            |             |             |contain letters or    |required to ignore it. If|
|                   |            |             |             |slashes (e.g., 'B' in |each of HouseNumber,     |
|                   |            |             |             |'B22 Main St').       |HouseNumberSuffix, and   |
|                   |            |             |             |                      |HouseNumberPrefix is     |
|                   |            |             |             |                      |blank, the address       |
|                   |            |             |             |                      |represents the entire    |
|                   |            |             |             |                      |street.                  |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| HouseNumberSuffix | xs:string  | Optional    | Single      |Represents the house  |If the field is not      |
|                   |            |             |             |number part of a      |present or invalid, the  |
|                   |            |             |             |street address. It may|implementation is        |
|                   |            |             |             |contain letters or    |required to ignore it. If|
|                   |            |             |             |slashes (e.g., B or   |each of HouseNumber,     |
|                   |            |             |             |1/2).                 |HouseNumberSuffix, and   |
|                   |            |             |             |                      |HouseNumberPrefix is     |
|                   |            |             |             |                      |blank, the address       |
|                   |            |             |             |                      |represents the entire    |
|                   |            |             |             |                      |street.                  |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| State             | xs:string  | **Required**| Single      |Specifies the         |If the field is not      |
|                   |            |             |             |two-letter state      |present or invalid, the  |
|                   |            |             |             |abbreviation of the   |implementation is        |
|                   |            |             |             |address.              |required to ignore the   |
|                   |            |             |             |                      |element containing it.   |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| StreetDirection   | xs:string  | Optional    | Single      |Specifies the         |If the field is not      |
|                   |            |             |             |(inter-)cardinal      |present or invalid, the  |
|                   |            |             |             |direction of the      |implementation is        |
|                   |            |             |             |street address (e.g., |required to ignore it.   |
|                   |            |             |             |the "E" in "100 E     |                         |
|                   |            |             |             |Capitol St NE").      |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| StreetName        | xs:string  | **Required**| Single      |Represents the name of|If the field is not      |
|                   |            |             |             |the street for the    |present or invalid, the  |
|                   |            |             |             |address. A special    |implementation is        |
|                   |            |             |             |wildcard, "*", denotes|required to ignore the   |
|                   |            |             |             |every street in the   |element containing it.   |
|                   |            |             |             |given city/town. It   |                         |
|                   |            |             |             |optionally may contain|                         |
|                   |            |             |             |street direction,     |                         |
|                   |            |             |             |street suffix or      |                         |
|                   |            |             |             |address direction     |                         |
|                   |            |             |             |(e.g., both "Capitol" |                         |
|                   |            |             |             |and "E Capitol St NE" |                         |
|                   |            |             |             |are acceptable for the|                         |
|                   |            |             |             |address "100 E Capitol|                         |
|                   |            |             |             |St NE"), however this |                         |
|                   |            |             |             |is not                |                         |
|                   |            |             |             |preferred. Preferred  |                         |
|                   |            |             |             |is street name alone  |                         |
|                   |            |             |             |(e.g. "Capitol").     |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| StreetSuffix      | xs:string  | Optional    | Single      |Represents the        |If the field is not      |
|                   |            |             |             |abbreviated,          |present or invalid, the  |
|                   |            |             |             |non-directional suffix|implementation is        |
|                   |            |             |             |to the street name. An|required to ignore it.   |
|                   |            |             |             |example is "St" for   |                         |
|                   |            |             |             |the address "100 E    |                         |
|                   |            |             |             |Capitol St NE."       |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
| Zip               | xs:string  | **Required**| Single      |Specifies the zip code|If the field is not      |
|                   |            |             |             |of the address. It may|present or invalid, the  |
|                   |            |             |             |be 5 or 9 digits, and |implementation is        |
|                   |            |             |             |it may include a      |required to ignore the   |
|                   |            |             |             |hyphen ('-'). It is   |element containing it.   |
|                   |            |             |             |required as it helps  |                         |
|                   |            |             |             |with geocoding, which |                         |
|                   |            |             |             |is crucial for        |                         |
|                   |            |             |             |distributors.         |                         |
+-------------------+------------+-------------+-------------+----------------------+-------------------------+
