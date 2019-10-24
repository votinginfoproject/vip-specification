.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-polling-location:

polling_location
================

The PollingLocation object represents a site where voters cast or drop off ballots.

+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                                  | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================================+==========================+==============+==============+==========================================+==========================================+
| :ref:`multi-csv-simple-address-type` | ``simple-address-type``  | Optional     | Single       | Represents the various structured parts  | One of **AddressStructured** and         |
|                                      |                          |              |              | of an address to a polling location.     | **AddressLine** should be present for a  |
|                                      |                          |              |              |                                          | given Polling Location. If none is       |
|                                      |                          |              |              |                                          | present, the implementation is required  |
|                                      |                          |              |              |                                          | to ignore the ``PollingLocation``        |
|                                      |                          |              |              |                                          | element containing it.                   |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| address_line                         | ``xs:string``            | Optional     | Repeats      | Represents the various parts of an       | One of AddressStructured and AddressLine |
|                                      |                          |              |              | address to a polling location.           | should be present for a given Polling    |
|                                      |                          |              |              |                                          | Location. If none is present, the        |
|                                      |                          |              |              |                                          | implementation is required to ignore the |
|                                      |                          |              |              |                                          | ``PollingLocation`` element containing   |
|                                      |                          |              |              |                                          | it.                                      |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions                           | ``xs:string``            | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                                      |                          |              |              | locating the polling location.           | present, then the implementation is      |
|                                      |                          |              |              |                                          | required to ignore it.                   |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours                                | ``xs:string``            | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
|                                      |                          |              |              | the polling location is open (**NB:**    | present, then the implementation is      |
|                                      |                          |              |              | this element is deprecated in favor of   | required to ignore it.                   |
|                                      |                          |              |              | the more structured                      |                                          |
|                                      |                          |              |              | :ref:`multi-csv-hours-open` element. It  |                                          |
|                                      |                          |              |              | is strongly encouraged that data         |                                          |
|                                      |                          |              |              | providers move toward contributing hours |                                          |
|                                      |                          |              |              | in this format).                         |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id                        | ``xs:IDREF``             | Optional     | Single       | Links to an :ref:`multi-csv-hours-open`  | If the field is invalid or not present,  |
|                                      |                          |              |              | element, which is a schedule of dates    | then the implementation is required to   |
|                                      |                          |              |              | and hours during which the polling       | ignore it.                               |
|                                      |                          |              |              | location is available.                   |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_drop_box                          | ``xs:boolean``           | Optional     | Single       | Indicates if this polling location is a  | If the field is invalid or not present,  |
|                                      |                          |              |              | drop box.                                | then the implementation is required to   |
|                                      |                          |              |              |                                          | ignore it.                               |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_early_voting                      | ``xs:boolean``           | Optional     | Single       | Indicates if this polling location is an | If the field is invalid or not present,  |
|                                      |                          |              |              | early vote site.                         | then the implementation is required to   |
|                                      |                          |              |              |                                          | ignore it.                               |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| lat_lng                              | :ref:`multi-csv-lat-lng` | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                                      |                          |              |              | this polling location.                   | present, then the implementation is      |
|                                      |                          |              |              |                                          | required to ignore it.                   |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                                 | ``xs:string``            | Optional     | Single       | Name of the polling location.            | If the field is invalid or not present,  |
|                                      |                          |              |              |                                          | then the implementation is required to   |
|                                      |                          |              |              |                                          | ignore it.                               |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| photo_uri                            | ``xs:string``            | Optional     | Single       | Contains a link to an image of the       | If the field is invalid or not present,  |
|                                      |                          |              |              | polling location.                        | then the implementation is required to   |
|                                      |                          |              |              |                                          | ignore it.                               |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,name,address_line,structured_location_name,structured_line_1,structured_city,structured_state,structured_zip,directions,hours,photo_uri,hours_open_id,is_drop_box,is_early_voting,latitude,longitude,latlng_source
    poll001,,,ALBERMARLE HIGH SCHOOL,2775 Hydraulic Rd,Charlottesville,VA,22901,Use back door,7am-8pm,www.picture.com,ho001,false,true,38.0754627,78.5014875,Google Maps
    poll002,Public Library,Main St Denver CO,,,,,,next to the checkout counter,7am-8pm,www.picture.com,,false,true,38.0754627,78.5014875,Google Maps


.. _multi-csv-lat-lng:

lat_long
--------

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| latitude      | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|               |               |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|               |               |              |              | example, this could be the name of a     | ignore it.                               |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-simple-address-type:

simple_address_type
-------------------

A ``SimpleAddressType`` represents a structured address.

+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+===============+==============+==============+==========================================+==========================================+
| structured_location_name | ``xs:string`` | Optional     | Single       | The name of the building a part of the   | If the field is invalid or not present,  |
|                          |               |              |              | structured address.                      | then the implementation is required to   |
|                          |               |              |              |                                          | ignore it.                               |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_1        | ``xs:string`` | **Required** | Single       | The address line for a structured        | If no ``Line1`` is provided, the         |
|                          |               |              |              | address. Should include the street       | implementation should ignore the         |
|                          |               |              |              | number, street name, and any prefix and  | ``SimpleAddressType``.                   |
|                          |               |              |              | suffix.                                  |                                          |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_2        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|                          |               |              |              |                                          | then the implementation is required to   |
|                          |               |              |              |                                          | ignore it.                               |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_3        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|                          |               |              |              |                                          | then the implementation is required to   |
|                          |               |              |              |                                          | ignore it.                               |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_city          | ``xs:string`` | **Required** | Single       | TBD                                      | If ``City`` is not provided, the         |
|                          |               |              |              |                                          | implementation should ignore the         |
|                          |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_state         | ``xs:string`` | **Required** | Single       | TBD                                      | If ``State`` is not provided, the        |
|                          |               |              |              |                                          | implementation should ignore the         |
|                          |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_zip           | ``xs:string`` | **Required** | Single       | TBD                                      | If ``Zip`` is not provided, the          |
|                          |               |              |              |                                          | implementation should ignore the         |
|                          |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
