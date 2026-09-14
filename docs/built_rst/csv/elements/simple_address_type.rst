.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-simple-address-type:

simple_address_type
===================

A ``SimpleAddressType`` represents a structured physical or mailing address. It has an optional attribute, ``language``, which defaults to ``i-default``.

When multiple ``SimpleAddressType`` elements are provided on an entity (such as ``AddressStructured`` on a polling location, or ``MailingAddress`` / ``PhysicalAddress`` on contact information), each must have a distinct ``language`` attribute to specify the address in multiple languages.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| location_name | ``xs:string`` | Optional     | Single       | The name of the location or facility     | If the field is invalid or not present,  |
|               |               |              |              | (e.g. "Albemarle High School").          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| address_line  | ``xs:string`` | **Required** | Repeats      | Street address line(s). Multiple         | If no AddressLine is provided, the       |
|               |               |              |              | AddressLine tags may appear in order     | implementation should ignore the         |
|               |               |              |              | (e.g. street address, suite/room).       | SimpleAddressType containing it.         |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| city          | ``xs:string`` | Optional     | Single       | The city, town, or municipality.         | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| county        | ``xs:string`` | Optional     | Single       | The county or parish.                    | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| region        | ``xs:string`` | Optional     | Single       | The state, province, or primary          | If the field is invalid or not present,  |
|               |               |              |              | sub-national region (e.g. "VA").         | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| country       | ``xs:string`` | Optional     | Single       | The country (e.g. "USA").                | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| world_region  | ``xs:string`` | Optional     | Single       | Global or continental region if          | If the field is invalid or not present,  |
|               |               |              |              | applicable.                              | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| postal_code   | ``xs:string`` | Optional     | Single       | The postal code or ZIP code.             | If the field is invalid or not present,  |
|               |               |              |              |                                          | then the implementation is required to   |
|               |               |              |              |                                          | ignore it.                               |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
