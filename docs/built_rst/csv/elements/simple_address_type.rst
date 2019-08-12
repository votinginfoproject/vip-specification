.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-simple-address-type:

simple_address_type
===================

A ``SimpleAddressType`` represents a structured address.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| location_name | ``xs:string`` | Optional     | Single       | The name of the building a part of the   | If the field is invalid or not present,  |
|               |               |              |              | structured address.                      | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| line_1        | ``xs:string`` | **Required** | Single       | The address line for a structured        | If no ``Line1`` is provided, the         |
|               |               |              |              | address. Should include the street       | implementation should ignore the         |
|               |               |              |              | number, stree name, and any prefix and   | ``SimpleAddressType``.                   |
|               |               |              |              | suffix.                                  |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| line_2        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| line_3        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city          | ``xs:string`` | **Required** | Single       | TBD                                      | If no ``City`` is not provided, the      |
|               |               |              |              |                                          | implementation should ignore the         |
|               |               |              |              |                                          | ``SimpleAddressType``.                   |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state         | ``xs:string`` | **Required** | Single       | TBD                                      | If no ``State`` is not provided, the     |
|               |               |              |              |                                          | implementation should ignore the         |
|               |               |              |              |                                          | ``SimpleAddressType``.                   |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| zip           | ``xs:string`` | Optional     | Single       | TBD                                      | If no ``Zip`` is not provided, the       |
|               |               |              |              |                                          | implementation should ignore the         |
|               |               |              |              |                                          | ``SimpleAddressType``.                   |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
