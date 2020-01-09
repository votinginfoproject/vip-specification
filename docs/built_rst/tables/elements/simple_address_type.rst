.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Line1        | ``xs:string`` | **Required** | Single       | The address line for a structured        | If no ``Line1`` is provided, the         |
|              |               |              |              | address. Should include the street       | implementation should ignore the         |
|              |               |              |              | number, street name, and any prefix and  | ``SimpleAddressType``.                   |
|              |               |              |              | suffix.                                  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line2        | ``xs:string`` | Optional     | Single       | Additional field for an address          | If no ``Line2`` is provided, the         |
|              |               |              |              |                                          | implementation should ignore it.         |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line3        | ``xs:string`` | Optional     | Single       | Additional field for an address          | If no ``Line3`` is provided, the         |
|              |               |              |              |                                          | implementation should ignore it.         |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | **Required** | Single       | The City value of a structured address.  | If ``City`` is not provided, the         |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State        | ``xs:string`` | **Required** | Single       | The State value of a structured address. | If ``State`` is not provided, the        |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip          | ``xs:string`` | Optional     | Single       | The ZIP code of a structured address.    | If ``Zip`` is not provided, the          |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
