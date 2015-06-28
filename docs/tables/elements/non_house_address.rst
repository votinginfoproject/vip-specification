.. This file is auto-generated.  Do not edit it by hand!

+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+==============+==============+==============+==========================================+==========================================+
| AddressDirection | xs:string    | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                  |              |              |              | of the entire address. An example is     | then the implementation is required to   |
|                  |              |              |              | "NE" for the address "100 E Capitol St   | ignore it.                               |
|                  |              |              |              | NE."                                     |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City             | xs:string    | **Required** | Single       | The city specifies the city or town of   | If the field is invalid, then the        |
|                  |              |              |              | the address.                             | implementation is required to ignore the |
|                  |              |              |              |                                          | element containing it.                   |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State            | xs:string    | **Required** | Single       | Specifies the two-letter state           | If the field is invalid, then the        |
|                  |              |              |              | abbreviation of the address.             | implementation is required to ignore the |
|                  |              |              |              |                                          | element containing it.                   |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection  | xs:string    | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                  |              |              |              | of the street address (e.g., the "E" in  | then the implementation is required to   |
|                  |              |              |              | "100 E Capitol St NE").                  | ignore it.                               |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName       | xs:string    | **Required** | Single       | Represents the name of the street for    | If the field is invalid, then the        |
|                  |              |              |              | the address. A special wildcard, "*",    | implementation is required to ignore the |
|                  |              |              |              | denotes every street in the given        | element containing it.                   |
|                  |              |              |              | city/town. It optionally may contain     |                                          |
|                  |              |              |              | street direction, street suffix or       |                                          |
|                  |              |              |              | address direction (e.g., both "Capitol"  |                                          |
|                  |              |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                  |              |              |              | the address "100 E Capitol St NE"),      |                                          |
|                  |              |              |              | however this is not preferred. Preferred |                                          |
|                  |              |              |              | is street name alone (e.g. "Capitol").   |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix     | xs:string    | Optional     | Single       | Represents the abbreviated,              | If the field is invalid or not present,  |
|                  |              |              |              | non-directional suffix to the street     | then the implementation is required to   |
|                  |              |              |              | name. An example is "St" for the address | ignore it.                               |
|                  |              |              |              | "100 E Capitol St NE."                   |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip              | xs:string    | **Required** | Single       | Specifies the zip code of the address.   | If the field is invalid, then the        |
|                  |              |              |              | It may be 5 or 9 digits, and it may      | implementation is required to ignore the |
|                  |              |              |              | include a hyphen ('-'). It is required   | element containing it.                   |
|                  |              |              |              | as it helps with geocoding, which is     |                                          |
|                  |              |              |              | crucial for distributors.                |                                          |
+------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
