.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-polling-location:

polling_location
================

The PollingLocation object represents a site where voters cast or drop off ballots.

+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+==========================+==============+==============+==========================================+==========================================+
| address_line    | ``xs:string``            | **Required** | Repeats      | Represents the various parts of an       | At least one valid ``AddressLine`` must  |
|                 |                          |              |              | address to a polling location. For CSV   | be present for ``PollingLocation`` to be |
|                 |                          |              |              | implementations, repeating               | valid. If no valid ``AddressLine`` is    |
|                 |                          |              |              | ``address_line`` columns should be       | present, the implementation is required  |
|                 |                          |              |              | incremented, e.g. address_line1,         | to ignore the ``PollingLocation``        |
|                 |                          |              |              | address_line2, address_line3.            | element containing it.                   |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions      | ``xs:string``            | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                 |                          |              |              | locating the polling location.           | present, then the implementation is      |
|                 |                          |              |              |                                          | required to ignore it.                   |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours           | ``xs:string``            | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
|                 |                          |              |              | the polling location is open (**NB:**    | present, then the implementation is      |
|                 |                          |              |              | this element is deprecated in favor of   | required to ignore it.                   |
|                 |                          |              |              | the more structured                      |                                          |
|                 |                          |              |              | :ref:`multi-csv-hours-open` element. It  |                                          |
|                 |                          |              |              | is strongly encouraged that data         |                                          |
|                 |                          |              |              | providers move toward contributing hours |                                          |
|                 |                          |              |              | in this format).                         |                                          |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id   | ``xs:IDREF``             | Optional     | Single       | Links to an :ref:`multi-csv-hours-open`  | If the field is invalid or not present,  |
|                 |                          |              |              | element, which is a schedule of dates    | then the implementation is required to   |
|                 |                          |              |              | and hours during which the polling       | ignore it.                               |
|                 |                          |              |              | location is available.                   |                                          |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_drop_box     | ``xs:boolean``           | Optional     | Single       | Indicates if this polling location is a  | If the field is invalid or not present,  |
|                 |                          |              |              | drop box.                                | then the implementation is required to   |
|                 |                          |              |              |                                          | ignore it.                               |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_early_voting | ``xs:boolean``           | Optional     | Single       | Indicates if this polling location is an | If the field is invalid or not present,  |
|                 |                          |              |              | early vote site.                         | then the implementation is required to   |
|                 |                          |              |              |                                          | ignore it.                               |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| lat_lng         | :ref:`multi-csv-lat-lng` | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                 |                          |              |              | this polling location.                   | present, then the implementation is      |
|                 |                          |              |              |                                          | required to ignore it.                   |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name            | ``xs:string``            | Optional     | Single       | Name of the polling location.            | If the field is invalid or not present,  |
|                 |                          |              |              |                                          | then the implementation is required to   |
|                 |                          |              |              |                                          | ignore it.                               |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| photo_uri       | ``xs:string``            | Optional     | Single       | Contains a link to an image of the       | If the field is invalid or not present,  |
|                 |                          |              |              | polling location.                        | then the implementation is required to   |
|                 |                          |              |              |                                          | ignore it.                               |
+-----------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,name,address_line,directions,hours,photo_uri,hours_open_id,is_drop_box,is_early_voting,latitude,longitude,latlng_source
    poll001,ALBERMARLE HIGH SCHOOL","2775 Hydraulic Rd Charlottesville, VA 22901,Use back door,7am-8pm,www.picture.com,ho001,false,true,38.0754627,78.5014875,Google Maps
    poll002,Public Library, Main St Denver,next to the checkout counter,7am-8pm,www.picture.com,,false,true,38.0754627,78.5014875,Google Maps
    poll003,Historic Society,,wheelchair entrance,7am-8pm,www.picture.com,,false,true,,,
    poll004,Community Center,,behind the big oak tree,7am-8pm,www.picture.com,,false,true,,,


.. _multi-csv-lat-lng:

lat_long
--------

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+===============+==============+==============+==========================================+==========================================+
| latitude      | ``xs:float``  | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| longitude     | ``xs:float``  | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|               |               |              |              |                                          | implementation is required to ignore it. |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| latlng_source | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|               |               |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|               |               |              |              | example, this could be the name of a     | ignore it.                               |
|               |               |              |              | geocoding service.                       |                                          |
+---------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
