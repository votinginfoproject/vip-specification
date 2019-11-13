.. This file is auto-generated.  Do not edit it by hand!

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Line1        | ``xs:string`` | **Required** | Single       | The address line for a structured        | If no ``Line1`` is provided, the         |
|              |               |              |              | address. Should include the street       | implementation should ignore the         |
|              |               |              |              | number, street name, and any prefix and  | ``SimpleAddressType``.                   |
|              |               |              |              | suffix.                                  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | **Required** | Single       | The City value of a structured address.  | If ``City`` is not provided, the         |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State        | ``xs:string`` | **Required** | Single       | The State value of a structured address. | If ``State`` is not provided, the        |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip          | ``xs:string`` | **Required** | Single       | The ZIP code of a structured address.    | If ``Zip`` is not provided, the          |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
