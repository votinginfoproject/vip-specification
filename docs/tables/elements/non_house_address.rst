.. This file is auto-generated.  Do not edit it by hand!

+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+==============+==============+==============+==========================================+==========================================+
| AddressDirection | xs:string    | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is not present or invalid,  |
|                  |              |              |              | of the entire address. An example is     | the implementation is required to ignore |
|                  |              |              |              | "NE" for the address "100 E Capitol St   | it.                                      |
|                  |              |              |              | NE."                                     |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City             | xs:string    | **Required** | Single       | The city specifies the city or town of   | If the field is not present or invalid,  |
|                  |              |              |              | the address.                             | the implementation is required to ignore |
|                  |              |              |              |                                          | the element containing it.               |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State            | xs:string    | **Required** | Single       | Specifies the two-letter state           | If the field is not present or invalid,  |
|                  |              |              |              | abbreviation of the address.             | the implementation is required to ignore |
|                  |              |              |              |                                          | the element containing it.               |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection  | xs:string    | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is not present or invalid,  |
|                  |              |              |              | of the street address (e.g., the "E" in  | the implementation is required to ignore |
|                  |              |              |              | "100 E Capitol St NE").                  | it.                                      |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName       | xs:string    | **Required** | Single       | Represents the name of the street for    | If the field is not present or invalid,  |
|                  |              |              |              | the address. A special wildcard, "*",    | the implementation is required to ignore |
|                  |              |              |              | denotes every street in the given        | the element containing it.               |
|                  |              |              |              | city/town. It optionally may contain     |                                          |
|                  |              |              |              | street direction, street suffix or       |                                          |
|                  |              |              |              | address direction (e.g., both "Capitol"  |                                          |
|                  |              |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                  |              |              |              | the address "100 E Capitol St NE"),      |                                          |
|                  |              |              |              | however this is not preferred. Preferred |                                          |
|                  |              |              |              | is street name alone (e.g. "Capitol").   |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix     | xs:string    | Optional     | Single       | Represents the abbreviated,              | If the field is not present or invalid,  |
|                  |              |              |              | non-directional suffix to the street     | the implementation is required to ignore |
|                  |              |              |              | name. An example is "St" for the address | it.                                      |
|                  |              |              |              | "100 E Capitol St NE."                   |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip              | xs:string    | **Required** | Single       | Specifies the zip code of the address.   | If the field is not present or invalid,  |
|                  |              |              |              | It may be 5 or 9 digits, and it may      | the implementation is required to ignore |
|                  |              |              |              | include a hyphen ('-'). It is required   | the element containing it.               |
|                  |              |              |              | as it helps with geocoding, which is     |                                          |
|                  |              |              |              | crucial for distributors.                |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
