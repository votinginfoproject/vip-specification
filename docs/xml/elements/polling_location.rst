PollingLocation
===============

The PollingLocation object represents a site where voters cast or drop off ballots.

+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| Tag                   | Data Type                 | Required?    | Repeats?   | Description                 | Error Handling        |
|                       |                           |              |            |                             |                       |
+=======================+===========================+==============+============+=============================+=======================+
| AddressLine           | xs:string                 | Optional     | Repeats    |Represents the various parts |If the field is invalid|
|                       |                           |              |            |of an address to a polling   |or not present, the    |
|                       |                           |              |            |location.                    |implementation is      |
|                       |                           |              |            |                             |required to ignore the |
|                       |                           |              |            |                             |PollingLocation element|
|                       |                           |              |            |                             |that contains it.      |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| Directions            |:doc:`InternationalizedText| Optional     | Single     |Specifies further            |If the field is invalid|
|                       |<internationalized_text>`  |              |            |instructions for locating the|or not present, the    |
|                       |                           |              |            |polling location.            |implementation is      |
|                       |                           |              |            |                             |required to ignore it. |
|                       |                           |              |            |                             |                       |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| Hours **[deprecated]**|:doc:`InternationalizedText| Optional     | Single     |Contains the hours (in local |If the field is invalid|
|                       |<internationalized_text>`  |              |            |time) that the polling       |or not present, the    |
|                       |                           |              |            |location is open (*NB: this  |implementation is      |
|                       |                           |              |            |element is deprecated in     |required to ignore it. |
|                       |                           |              |            |favor of the more structured |                       |
|                       |                           |              |            |HoursOpen element. It is     |                       |
|                       |                           |              |            |strongly encouraged that data|                       |
|                       |                           |              |            |providers move toward        |                       |
|                       |                           |              |            |contributing hours in this   |                       |
|                       |                           |              |            |format)*.                    |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| HoursOpenId           | xs:IDREF                  | Optional     | Single     |Links to an :doc:`HoursOpen  |If the field is invalid|
|                       |                           |              |            |<hours_open>` element, which |or not present, the    |
|                       |                           |              |            |is a schedule of dates and   |implementation is      |
|                       |                           |              |            |hours during which the       |required to ignore it. |
|                       |                           |              |            |polling location is          |                       |
|                       |                           |              |            |available.                   |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
|                       |                           |              |            |                             |                       |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| IsDropBox             | xs:boolean                | Optional     | Single     |Indicates if this polling    |If the field is invalid|
|                       |                           |              |            |location is a drop box.      |or not present, the    |
|                       |                           |              |            |                             |implementation is      |
|                       |                           |              |            |                             |required to ignore it. |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| IsEarlyVoting         | xs:boolean                | Optional     | Single     |Indicates if this polling    |If the field is invalid|
|                       |                           |              |            |location is an early vote    |or not present, the    |
|                       |                           |              |            |site.                        |implementation is      |
|                       |                           |              |            |                             |required to ignore it. |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| LatLng                | :ref:`LatLng              | Optional     | Single     |Specifies the latitude and   |If the element is      |
|                       | <pl-latlng>`              |              |            |longitude of this polling    |invalid or not present,|
|                       |                           |              |            |location.                    |the implementation is  |
|                       |                           |              |            |                             |required to ignore it. |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+
| PhotoUri              | xs:anyURI                 | Optional     | Single     |Contains a link to an image  |If the field is invalid|
|                       |                           |              |            |of the polling location.     |or not present, the    |
|                       |                           |              |            |                             |implementation is      |
|                       |                           |              |            |                             |required to ignore it. |
+-----------------------+---------------------------+--------------+------------+-----------------------------+-----------------------+

.. _pl-latlng:

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| Tag                   | Data Type             | Required?    | Repeats?   | Description        | Error Handling        |
|                       |                       |              |            |                    |                       |
+=======================+=======================+==============+============+====================+=======================+
| Latitude              | xs:float              | **Required** | Single     |The latitude of the |If field is invalid or |
|                       |                       |              |            |polling location.   |not present, the       |
|                       |                       |              |            |                    |implementation is      |
|                       |                       |              |            |                    |required to ignore the |
|                       |                       |              |            |                    |element containing it. |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| Longitude             | xs:float              | **Required** | Single     |The longitude of the|If the field is invalid|
|                       |                       |              |            |polling location.   |or not present, the    |
|                       |                       |              |            |                    |implementation is      |
|                       |                       |              |            |                    |required to ignore the |
|                       |                       |              |            |                    |element containing it. |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| Source                | xs:string             | Optional     | Single     |The system used to  |If the field is invalid|
|                       |                       |              |            |perform the lookup  |or not present, the    |
|                       |                       |              |            |from location name  |implementation is      |
|                       |                       |              |            |to lat/lng. For     |required to ignore it. |
|                       |                       |              |            |example, this could |                       |
|                       |                       |              |            |be the name of a    |                       |
|                       |                       |              |            |geocoding service.  |                       |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+

.. _`WGS 84`: http://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS_84

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl81274">
      <AddressLine>ALBEMARLE HIGH SCHOOL</AddressLine>
      <AddressLine>2775 Hydraulic Rd</AddressLine>
      <AddressLine>Charlottesville, VA 229018917</AddressLine>
      <HoursOpenId>hours0001</HoursOpenId>
      <LatLng>
        <Latitude>38.0754627</Latitude>
        <Longitude>-78.5014875</Longitude>
        <Source>Google Maps</Source>
      </LatLng>
   </PollingLocation>

