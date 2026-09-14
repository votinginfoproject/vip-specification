.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-contact-information:

contact_information
===================

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`multi-csv-election-administration`, :ref:`multi-csv-office`,
:ref:`multi-csv-person`, :ref:`multi-csv-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                                  | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================================+========================================+==============+==============+==========================================+==========================================+
| :ref:`multi-csv-simple-address-type` | ``simple-address-type``                | **Required** | Repeats      | Represents the various structured parts  | **AddressStructured** should be present  |
|                                      |                                        |              |              | of an address to a polling location.  If | for a given Contact Information. If none |
|                                      |                                        |              |              | multiple addresses are provided, each    | is present, the implementation is        |
|                                      |                                        |              |              | one must have a different language       | required to ignore the                   |
|                                      |                                        |              |              | attribute.  All addresses are considered | ``ContactInformation`` element           |
|                                      |                                        |              |              | equally authoritative.  Multiple         | containing it. If more than one          |
|                                      |                                        |              |              | addresses are supported in XML format    | **AddressStructured** exists with the    |
|                                      |                                        |              |              | only; CSV files must have exactly one    | same language code, the implementation   |
|                                      |                                        |              |              | address.                                 | is required to ignore the                |
|                                      |                                        |              |              |                                          | ``ContactInformation`` element           |
|                                      |                                        |              |              |                                          | containing it.                           |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions                           | ``xs:string``                          | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                                      |                                        |              |              | locating this entity.                    | present, then the implementation is      |
|                                      |                                        |              |              |                                          | required to ignore it.                   |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| email                                | ``xs:string``                          | Optional     | Repeats      | An email address for the contact.        | If the element is invalid or not         |
|                                      |                                        |              |              | Multiple languages may be provided if    | present, then the implementation is      |
|                                      |                                        |              |              | there are distinct e-mail addresses for  | required to ignore it.                   |
|                                      |                                        |              |              | communicating in different languages.    |                                          |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| fax                                  | ``xs:string``                          | Optional     | Repeats      | A fax line for the contact.  Multiple    | If the element is invalid or not         |
|                                      |                                        |              |              | languages may be provided if there are   | present, then the implementation is      |
|                                      |                                        |              |              | distinct numbers for communicating in    | required to ignore it.                   |
|                                      |                                        |              |              | different languages.                     |                                          |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours                                | ``xs:string``                          | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
|                                      |                                        |              |              | the location is open *(NB: this element  | present, then the implementation is      |
|                                      |                                        |              |              | is deprecated in favor of the more       | required to ignore it.                   |
|                                      |                                        |              |              | structured :ref:`multi-csv-hours-open`   |                                          |
|                                      |                                        |              |              | element. It is strongly encouraged that  |                                          |
|                                      |                                        |              |              | data providers move toward contributing  |                                          |
|                                      |                                        |              |              | hours in this format)*.                  |                                          |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open                           | ``???``                                | Optional     | Single       | An `multi-csv-hours-open` element, which | If the field is invalid or not present,  |
|                                      |                                        |              |              | lists the hours of operation for a       | then the implementation is required to   |
|                                      |                                        |              |              | location.                                | ignore it.                               |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| lat_long                             | :ref:`multi-csv-lat-lng`               | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                                      |                                        |              |              | this entity.                             | present, then the implementation is      |
|                                      |                                        |              |              |                                          | required to ignore it.                   |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                                 | ``xs:string``                          | Optional     | Single       | The name of the location or contact.     | If the element is invalid or not         |
|                                      |                                        |              |              | :ref:`See usage note.                    | present, then the implementation is      |
|                                      |                                        |              |              | <multi-csv-name-address-line-usage>`     | required to ignore it.                   |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| phone                                | ``xs:string``                          | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|                                      |                                        |              |              |                                          | then the implementation is required to   |
|                                      |                                        |              |              |                                          | ignore it.                               |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| uri                                  | :ref:`multi-csv-internationalized-uri` | Optional     | Repeats      | An informational URI for the contact or  | If the element is invalid or not         |
|                                      |                                        |              |              | location.                                | present, then the implementation is      |
|                                      |                                        |              |              |                                          | required to ignore it.                   |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| parent_id                            | ``xs:IDREF``                           | Optional     | Repeats      | A reference to a record in source,       | If the field is invalid or not present,  |
|                                      |                                        |              |              | department, voter_service, candidate,    | then the implementation is required to   |
|                                      |                                        |              |              | person, or office.                       | ignore it.                               |
+--------------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,address_line_1,address_line_2,address_line_3,directions,email,fax,hours,hours_open_id,latitude,longitude,latlng_source,name,phone,uri,parent_id
    ci0827,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,off001
    ci0828,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,vs01
