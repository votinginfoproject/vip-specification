.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-polling-location:

PollingLocation
===============

The PollingLocation object represents a site where voters cast or drop off ballots.

+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=========================================+==============+==============+==========================================+==========================================+
| AddressStructured | :ref:`multi-xml-simple-address-type`    | Optional     | Single       | Represents the various structured parts  | One of **AddressStructured** and         |
|                   |                                         |              |              | of an address to a polling location.     | **AddressLine** should be present for a  |
|                   |                                         |              |              |                                          | given Polling Location. If none is       |
|                   |                                         |              |              |                                          | present, the implementation is required  |
|                   |                                         |              |              |                                          | to ignore the ``PollingLocation``        |
|                   |                                         |              |              |                                          | element containing it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AddressLine       | ``xs:string``                           | Optional     | Repeats      | Represents the various parts of an       | One of AddressStructured and AddressLine |
|                   |                                         |              |              | address to a polling location.           | should be present for a given Polling    |
|                   |                                         |              |              |                                          | Location. If none is present, the        |
|                   |                                         |              |              |                                          | implementation is required to ignore the |
|                   |                                         |              |              |                                          | ``PollingLocation`` element containing   |
|                   |                                         |              |              |                                          | it.                                      |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions        | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for       |                                          |
|                   |                                         |              |              | locating the polling location.           |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours             | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  |                                          |
| **[deprecated]**  |                                         |              |              | the polling location is open (**NB:**    |                                          |
|                   |                                         |              |              | this element is deprecated in favor of   |                                          |
|                   |                                         |              |              | the more structured                      |                                          |
|                   |                                         |              |              | :ref:`multi-xml-hours-open` element. It  |                                          |
|                   |                                         |              |              | is strongly encouraged that data         |                                          |
|                   |                                         |              |              | providers move toward contributing hours |                                          |
|                   |                                         |              |              | in this format).                         |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId       | ``xs:IDREF``                            | Optional     | Single       | Links to an :ref:`multi-xml-hours-open`  |                                          |
|                   |                                         |              |              | element, which is a schedule of dates    |                                          |
|                   |                                         |              |              | and hours during which the polling       |                                          |
|                   |                                         |              |              | location is available.                   |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsDropBox         | ``xs:boolean``                          | Optional     | Single       | Indicates if this polling location is a  |                                          |
|                   |                                         |              |              | drop box.                                |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsEarlyVoting     | ``xs:boolean``                          | Optional     | Single       | Indicates if this polling location is an |                                          |
|                   |                                         |              |              | early vote site.                         |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng            | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Specifies the latitude and longitude of  |                                          |
|                   |                                         |              |              | this polling location.                   |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name              | ``xs:string``                           | Optional     | Single       | Name of the polling location.            |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PhotoUri          | ``xs:anyURI``                           | Optional     | Single       | Contains a link to an image of the       |                                          |
|                   |                                         |              |              | polling location.                        |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl00000">
      <AddressLine>2775 Hydraulic Rd Charlottesville, VA 22901</AddressLine>
      <HoursOpenId>hours0002</HoursOpenId>
      <IsDropBox>true</IsDropBox>
      <IsEarlyVoting>true</IsEarlyVoting>
      <LatLng>
         <Latitude>38.009939</Latitude>
         <Longitude>-78.506204</Longitude>
      </LatLng>
      <Name>ALBERMARLE HIGH SCHOOL</Name>
   </PollingLocation>
   <!-- Or: -->
   <PollingLocation id="pl00000">
      <AddressStructured>
         <Line1>2775 Hydraulic Rd</Line1>
         <City>CHARLOTTESVILLE</City>
         <State>VA</State>
         <Zip>22901</Zip>
      </AddressStructured>
      <HoursOpenId>hours0002</HoursOpenId>
      <IsDropBox>true</IsDropBox>
      <IsEarlyVoting>true</IsEarlyVoting>
      <LatLng>
         <Latitude>38.009939</Latitude>
         <Longitude>-78.506204</Longitude>
      </LatLng>
      <Name>ALBERMARLE HIGH SCHOOL</Name>
   </PollingLocation>


.. _multi-xml-lat-lng:

LatLng
------

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Latitude     | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Longitude    | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Source       | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    |                                          |
|              |               |              |              | from location name to lat/lng. For       |                                          |
|              |               |              |              | example, this could be the name of a     |                                          |
|              |               |              |              | geocoding service.                       |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-simple-address-type:

SimpleAddressType
-----------------

A ``SimpleAddressType`` represents a structured address.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Line1        | ``xs:string`` | **Required** | Single       | The address line for a structured        |                                          |
|              |               |              |              | address. Should include the street       |                                          |
|              |               |              |              | number, street name, and any prefix and  |                                          |
|              |               |              |              | suffix.                                  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line2        | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line3        | ``xs:string`` | Optional     | Single       | Additional field for an address          |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | **Required** | Single       | The City value of a structured address.  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State        | ``xs:string`` | **Required** | Single       | The State value of a structured address. |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip          | ``xs:string`` | Optional     | Single       | The ZIP code of a structured address.    |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
