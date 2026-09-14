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
| City         | ``xs:string`` | Optional     | Single       | The City value of a structured address   | If the field is invalid or not present,  |
|              |               |              |              | (e.g. "Charlottesville", "Springfield"). | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| County       | ``xs:string`` | Optional     | Single       | The county or parish (e.g. "Albemarle    | If the field is invalid or not present,  |
|              |               |              |              | County", "Fairfax").                     | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Region       | ``xs:string`` | Optional     | Single       | The Region value of a structured         | If the field is invalid or not present,  |
|              |               |              |              | address. This is country-dependent. For  | then the implementation is required to   |
|              |               |              |              | example, for US addresses, it is the     | ignore it.                               |
|              |               |              |              | two-letter state abbreviation (e.g.      |                                          |
|              |               |              |              | "VA"); for Canadian addresses it is the  |                                          |
|              |               |              |              | province (e.g. "ON").                    |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Country      | ``xs:string`` | Optional     | Single       | The Country value of a structured        | If the field is invalid or not present,  |
|              |               |              |              | address (e.g. "USA").                    | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WorldRegion  | ``xs:string`` | Optional     | Single       | Global or continental region if          | If the field is invalid or not present,  |
|              |               |              |              | applicable (e.g. "North America").       | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostalCode   | ``xs:string`` | Optional     | Single       | The postal code of a structured address. | If the field is invalid or not present,  |
|              |               |              |              | In the US, this is the ZIP code (e.g.    | then the implementation is required to   |
|              |               |              |              | "22902" or "22902-1234").                | ignore it.                               |
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
