.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-polling-location:

PollingLocation
===============

The PollingLocation object represents a site where voters cast or drop off ballots.

+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=========================================+==============+==============+==========================================+==========================================+
| StructuredAddress | :ref:`multi-xml-simple-address-type`    | Optional     | Single       | Represents the various structured parts  | One of AddressStructured and AddressLine |
|                   |                                         |              |              | of an address to a polling location.     | should be present for a given Polling    |
|                   |                                         |              |              |                                          | Location. If none is present, the        |
|                   |                                         |              |              |                                          | implementation is required to ignore the |
|                   |                                         |              |              |                                          | ``PollingLocation`` element containing   |
|                   |                                         |              |              |                                          | it.                                      |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AddressLine       | ``xs:string``                           | Optional     | Repeats      | Represents the various parts of an       | One of AddressStructured and AddressLine |
|                   |                                         |              |              | address to a polling location.           | should be present for a given Polling    |
|                   |                                         |              |              |                                          | Location. If none is present, the        |
|                   |                                         |              |              |                                          | implementation is required to ignore the |
|                   |                                         |              |              |                                          | ``PollingLocation`` element containing   |
|                   |                                         |              |              |                                          | it.                                      |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions        | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                   |                                         |              |              | locating the polling location.           | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours             | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]**  |                                         |              |              | the polling location is open (**NB:**    | present, then the implementation is      |
|                   |                                         |              |              | this element is deprecated in favor of   | required to ignore it.                   |
|                   |                                         |              |              | the more structured                      |                                          |
|                   |                                         |              |              | :ref:`multi-xml-hours-open` element. It  |                                          |
|                   |                                         |              |              | is strongly encouraged that data         |                                          |
|                   |                                         |              |              | providers move toward contributing hours |                                          |
|                   |                                         |              |              | in this format).                         |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId       | ``xs:IDREF``                            | Optional     | Single       | Links to an :ref:`multi-xml-hours-open`  | If the field is invalid or not present,  |
|                   |                                         |              |              | element, which is a schedule of dates    | then the implementation is required to   |
|                   |                                         |              |              | and hours during which the polling       | ignore it.                               |
|                   |                                         |              |              | location is available.                   |                                          |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsDropBox         | ``xs:boolean``                          | Optional     | Single       | Indicates if this polling location is a  | If the field is invalid or not present,  |
|                   |                                         |              |              | drop box.                                | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsEarlyVoting     | ``xs:boolean``                          | Optional     | Single       | Indicates if this polling location is an | If the field is invalid or not present,  |
|                   |                                         |              |              | early vote site.                         | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng            | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                   |                                         |              |              | this polling location.                   | present, then the implementation is      |
|                   |                                         |              |              |                                          | required to ignore it.                   |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name              | ``xs:string``                           | Optional     | Single       | Name of the polling location.            | If the field is invalid or not present,  |
|                   |                                         |              |              |                                          | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
+-------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PhotoUri          | ``xs:anyURI``                           | Optional     | Single       | Contains a link to an image of the       | If the field is invalid or not present,  |
|                   |                                         |              |              | polling location.                        | then the implementation is required to   |
|                   |                                         |              |              |                                          | ignore it.                               |
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
      <StructuredAddress>
         <LocationName>ALBERMARLE HIGH SCHOOL</LocationName>
         <Line1>2775 Hydraulic Rd</Line1>
         <City>CHARLOTTESVILLE</City>
         <State>VA</State>
         <Zip>22901</Zip>
      </StructuredAddress>
      <HoursOpenId>hours0002</HoursOpenId>
      <IsDropBox>true</IsDropBox>
      <IsEarlyVoting>true</IsEarlyVoting>
      <LatLng>
         <Latitude>38.009939</Latitude>
         <Longitude>-78.506204</Longitude>
      </LatLng>
   </PollingLocation>


.. _multi-xml-lat-lng:

LatLng
------

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Latitude     | ``xs:double`` | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|              |               |              |              |                                          | implementation is required to ignore it. |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Longitude    | ``xs:double`` | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|              |               |              |              |                                          | implementation is required to ignore it. |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Source       | ``xs:string`` | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|              |               |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|              |               |              |              | example, this could be the name of a     | ignore it.                               |
|              |               |              |              | geocoding service.                       |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-simple-address-type:

SimpleAddressType
-----------------

A ``SimpleAddressType`` represents a structured address.

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| LocationName | ``xs:string`` | Optional     | Single       | The name of the building a part of the   | If the field is invalid or not present,  |
|              |               |              |              | structured address.                      | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line1        | ``xs:string`` | Optional     | Single       | The address line for a structured        | If no ``Line1`` is provided, the         |
|              |               |              |              | address. Should include the street       | implementation should ignore the         |
|              |               |              |              | number, stree name, and any prefix and   | ``SimpleAddressType``.                   |
|              |               |              |              | suffix.                                  |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line2        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Line3        | ``xs:string`` | Optional     | Single       | TBD                                      | If the field is invalid or not present,  |
|              |               |              |              |                                          | then the implementation is required to   |
|              |               |              |              |                                          | ignore it.                               |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City         | ``xs:string`` | Optional     | Single       | TBD                                      | If no ``City`` is not provided, the      |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State        | ``xs:string`` | Optional     | Single       | TBD                                      | If no ``State`` is not provided, the     |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip          | ``xs:string`` | Optional     | Single       | TBD                                      | If no ``Zip`` is not provided, the       |
|              |               |              |              |                                          | implementation should ignore the         |
|              |               |              |              |                                          | ``SimpleAddressType``.                   |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
