.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| LocationName | ``xs:string`` | Optional     | Single       | The name of the building a part of the   | If the field is invalid or not present,  |
|              |               |              |              | structured address.                      | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line1        | ``xs:string`` | **Required** | Single       | The address line for a structured        | If no ``Line1`` is provided, the         |
|              |               |              |              | address. Should include the street       | implementation should ignore the         |
|              |               |              |              | number, street name, and any prefix and  | ``SimpleAddressType``.                   |
|              |               |              |              | suffix.                                  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line2        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line3        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | **Required** | Single       | TBD                                      | If ``City`` is not provided, the         |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State        | ``xs:string`` | **Required** | Single       | TBD                                      | If ``State`` is not provided, the        |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip          | ``xs:string`` | **Required** | Single       | TBD                                      | If ``Zip`` is not provided, the          |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
