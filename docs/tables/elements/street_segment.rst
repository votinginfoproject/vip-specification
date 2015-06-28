.. This file is auto-generated.  Do not edit it by hand!

+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=============================+==============+==============+==========================================+==========================================+
| NonHouseAddress      | `NonHouseAddress`_          | **Required** | Single       | The common street address (as well as    | If the element is not present or         |
|                      |                             |              |              | city, state, and zip) of the start and   | invalid, the implementation is required  |
|                      |                             |              |              | end points of the segment. Specific      | to ignore the StreetSegment element      |
|                      |                             |              |              | information such as street direction     | containing it                            |
|                      |                             |              |              | should be included.                      |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllAddresses | xs:boolean                  | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                      |                             |              |              | address on this street. If this is       | then the implementation is required to   |
|                      |                             |              |              | *true*, then the values of               | ignore it.                               |
|                      |                             |              |              | **StartHouseNumber** and                 |                                          |
|                      |                             |              |              | **EndHouseNumber** should be ignored.    |                                          |
|                      |                             |              |              | The value of **OddEvenBoth** must be     |                                          |
|                      |                             |              |              | *both*.                                  |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OddEvenBoth          | :doc:`OebEnum               | **Required** | Single       | Specifies whether the odd side of the    | If the field is not present or invalid,  |
|                      | <../enumerations/oeb_enum>` |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                      |                             |              |              | even side, or both are in included in    | the StreetSegment containing it.         |
|                      |                             |              |              | the street segment.                      |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctId           | xs:IDREF                    | Optional     | Single       | References the :doc:`precinct            | If the field is not present or invalid,  |
|                      |                             |              |              | <precinct>` that contains the entire     | the implementation is required to ignore |
|                      |                             |              |              | street segment.                          | the StreetSegment element containing it. |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartHouseNumber     | xs:integer                  | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** is true, |
|                      |                             |              |              | segment starts. This value is necessary  | if the field is not present or invalid,  |
|                      |                             |              |              | for the street segment to make any       | the implementation is required to ignore |
|                      |                             |              |              | sense. Unless **IncludesAllAddresses**   | the street segment element containing    |
|                      |                             |              |              | is true, this value must be less than or | it. If the **StartHouseNumber** is       |
|                      |                             |              |              | equal to **EndHouseNumber**. If          | greater than the **EndHouseNumber**, the |
|                      |                             |              |              | **IncludesAllAddresses** is true, this   | implementation should ignore the element |
|                      |                             |              |              | value is ignored.                        | containing them.                         |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndHouseNumber       | xs:integer                  | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** is true, |
|                      |                             |              |              | segment ends. This value is necessary    | if the field is not present or invalid,  |
|                      |                             |              |              | for the street segment to make any       | the implementation is required to ignore |
|                      |                             |              |              | sense. Unless **IncludesAllAddresses**   | the street segment element containing    |
|                      |                             |              |              | is true, it must be greater than or      | it. If the **EndHouseNumber** is less    |
|                      |                             |              |              | equal to **StartHouseNumber**. If        | than the **StartHouseNumber**, the       |
|                      |                             |              |              | **IncludesAllAddresses** is true, this   | implementation should ignore the element |
|                      |                             |              |              | value is ignored.                        | containing it.                           |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| UnitNumber           | xs:string                   | Optional     | Repeats      | The apartment/unit number for a street   | If the field is invalid or not present,  |
|                      |                             |              |              | segment. If this value is present then   | then the implementation is required to   |
|                      |                             |              |              | **StartHouseNumber** must be equal to    | ignore it.                               |
|                      |                             |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                      |                             |              |              | used if **IncludesAllAddresses** is      |                                          |
|                      |                             |              |              | true.                                    |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
