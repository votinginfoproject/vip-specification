.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-polling-location:

polling_location
================

The PollingLocation object represents a site where voters cast or drop off ballots.

+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                                  | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================================+==========================+==============+==============+==========================================+==========================================+
| address_line                         | ``xs:string``            | Optional     | Repeats      | Represents the various parts of an       | One of AddressStructured and AddressLine |
|                                      |                          |              |              | address to a polling location.           | should be present for a given Polling    |
|                                      |                          |              |              |                                          | Location. If none is present, the        |
|                                      |                          |              |              |                                          | implementation is required to ignore the |
|                                      |                          |              |              |                                          | ``PollingLocation`` element containing   |
|                                      |                          |              |              |                                          | it.                                      |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions                           | ``xs:string``            | Optional     | Single       | Specifies further instructions for       |                                          |
|                                      |                          |              |              | locating the polling location.           |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours                                | ``xs:string``            | Optional     | Single       | Contains the hours (in local time) that  |                                          |
|                                      |                          |              |              | the polling location is open (**NB:**    |                                          |
|                                      |                          |              |              | this element is deprecated in favor of   |                                          |
|                                      |                          |              |              | the more structured                      |                                          |
|                                      |                          |              |              | :ref:`multi-csv-hours-open` element. It  |                                          |
|                                      |                          |              |              | is strongly encouraged that data         |                                          |
|                                      |                          |              |              | providers move toward contributing hours |                                          |
|                                      |                          |              |              | in this format).                         |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id                        | ``xs:IDREF``             | Optional     | Single       | Links to an :ref:`multi-csv-hours-open`  |                                          |
|                                      |                          |              |              | element, which is a schedule of dates    |                                          |
|                                      |                          |              |              | and hours during which the polling       |                                          |
|                                      |                          |              |              | location is available.                   |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_drop_box                          | ``xs:boolean``           | Optional     | Single       | Indicates if this polling location is a  |                                          |
|                                      |                          |              |              | drop box.                                |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_early_voting                      | ``xs:boolean``           | Optional     | Single       | Indicates if this polling location is an |                                          |
|                                      |                          |              |              | early vote site.                         |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                                 | ``xs:string``            | Optional     | Single       | Name of the polling location.            |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| photo_uri                            | ``xs:string``            | Optional     | Single       | Contains a link to an image of the       |                                          |
|                                      |                          |              |              | polling location.                        |                                          |
+--------------------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,name,address_line,structured_line_1,structured_city,structured_state,structured_zip,directions,hours,photo_uri,hours_open_id,is_drop_box,is_early_voting,latitude,longitude,latlng_source
    poll001,ALBERMARLE HIGH SCHOOL,,2775 Hydraulic Rd,Charlottesville,VA,22901,Use back door,7am-8pm,www.picture.com,ho001,false,true,38.0754627,78.5014875,Google Maps
    poll002,Public Library,Main St Denver CO,,,,,,next to the checkout counter,7am-8pm,www.picture.com,,false,true,38.0754627,78.5014875,Google Maps


.. _multi-csv-lat-lng:

lat_long
--------

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| latitude      | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    |                                          |
|               |               |              |              | from location name to lat/lng. For       |                                          |
|               |               |              |              | example, this could be the name of a     |                                          |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-simple-address-type:

simple_address_type
-------------------

A ``SimpleAddressType`` represents a structured address.

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| structured_line_1 | ``xs:string`` | **Required** | Single       | The address line for a structured        |                                          |
|                   |               |              |              | address. Should include the street       |                                          |
|                   |               |              |              | number, street name, and any prefix and  |                                          |
|                   |               |              |              | suffix.                                  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_2 | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_line_3 | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_city   | ``xs:string`` | **Required** | Single       | The City value of a structured address.  |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_state  | ``xs:string`` | **Required** | Single       | The State value of a structured address. |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| structured_zip    | ``xs:string`` | Optional     | Single       | The ZIP code of a structured address.    |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
