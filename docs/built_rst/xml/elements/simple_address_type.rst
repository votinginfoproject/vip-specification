.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-simple-address-type:

SimpleAddressType
=================

A ``SimpleAddressType`` represents a structured physical or mailing address. It has an optional attribute, ``language``, which defaults to ``i-default``.

When multiple ``SimpleAddressType`` elements are provided on an entity (such as ``AddressStructured`` on a polling location, or ``MailingAddress`` / ``PhysicalAddress`` on contact information), each must have a distinct ``language`` attribute to specify the address in multiple languages.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| LocationName | ``xs:string`` | Optional     | Single       | The name of the location or facility     | If the field is invalid or not present,  |
|              |               |              |              | (e.g. "Albemarle High School").          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AddressLine  | ``xs:string`` | **Required** | Repeats      | Street address line(s). Multiple         | If no AddressLine is provided, the       |
|              |               |              |              | AddressLine tags may appear in order     | implementation should ignore the         |
|              |               |              |              | (e.g. street address, suite/room).       | SimpleAddressType containing it.         |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | Optional     | Single       | The city, town, or municipality.         | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| County       | ``xs:string`` | Optional     | Single       | The county or parish.                    | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Region       | ``xs:string`` | Optional     | Single       | The state, province, or primary          | If the field is invalid or not present,  |
|              |               |              |              | sub-national region (e.g. "VA").         | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Country      | ``xs:string`` | Optional     | Single       | The country (e.g. "USA").                | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WorldRegion  | ``xs:string`` | Optional     | Single       | Global or continental region if          | If the field is invalid or not present,  |
|              |               |              |              | applicable.                              | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostalCode   | ``xs:string`` | Optional     | Single       | The postal code or ZIP code.             | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <AddressStructured language="en">
      <LocationName>Albemarle High School</LocationName>
      <AddressLine>2775 Hydraulic Rd</AddressLine>
      <City>Charlottesville</City>
      <County>Albemarle</County>
      <Region>VA</Region>
      <Country>USA</Country>
      <PostalCode>22901</PostalCode>
   </AddressStructured>
