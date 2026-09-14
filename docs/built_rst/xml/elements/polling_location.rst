.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-polling-location:

PollingLocation
===============

The PollingLocation object represents a site where voters cast ballots in person or drop off early/absentee ballots. In VIP 7.0, facility names are placed in ``AddressStructured.LocationName``.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearDirections/>``, ``<ClearPhotoUri/>``, ``<ClearIsInactive/>``). AddressStructured and LocationType are optional in overlays.
EmergencyNotice is permitted only in overlays.
In overlays, PollingLocation has an optional attribute ``isNew="true"`` to indicate that a polling location is newly added rather than modifying an existing one.

+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                                | Error Handling                           |
+====================+=========================================+==============+==============+============================================+==========================================+
| AddressStructured  | :ref:`multi-xml-simple-address-type`    | **Required** | Repeats      | Represents the various structured parts of | AddressStructured is required for        |
|                    |                                         |              |              | an address to a polling location. If       | PollingLocation in main feeds.           |
|                    |                                         |              |              | multiple addresses are provided, each one  |                                          |
|                    |                                         |              |              | must have a distinct language attribute    |                                          |
|                    |                                         |              |              | (e.g. "en", "es"). All addresses are       |                                          |
|                    |                                         |              |              | considered equally authoritative. Facility |                                          |
|                    |                                         |              |              | names are specified in                     |                                          |
|                    |                                         |              |              | AddressStructured.LocationName. Required   |                                          |
|                    |                                         |              |              | in main feed; optional in overlays.        |                                          |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| LocationIdentifier | :ref:`multi-xml-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus | If the element is invalid or not         |
|                    |                                         |              |              | Code, geocoder ID). Clearable in overlays. | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Directions         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for         | If the element is invalid or not         |
|                    |                                         |              |              | locating the polling site or room (e.g.    | present, then the implementation is      |
|                    |                                         |              |              | "Enter through gymnasium doors on north    | required to ignore it.                   |
|                    |                                         |              |              | side of building"). Clearable in overlays. |                                          |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Hours              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Operating hours as text. Clearable in      | If the element is invalid or not         |
|                    |                                         |              |              | overlays. *(NB: deprecated in favor of     | present, then the implementation is      |
|                    |                                         |              |              | :ref:`multi-xml-schedule-with-timezone`)*. | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Schedule           | :ref:`multi-xml-schedule-with-timezone` | Optional     | Repeats      | Structured schedule of operating dates and | If the element is invalid or not         |
|                    |                                         |              |              | hours. Clearable in overlays.              | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| LocationType       | :ref:`multi-xml-polling-location-type`  | **Required** | Single       | The type of voting conducted at this       | LocationType is required for             |
|                    |                                         |              |              | location (InPersonDayOf, InPersonEarly, or | PollingLocation in main feeds.           |
|                    |                                         |              |              | DropOff). Required in main feed; optional  |                                          |
|                    |                                         |              |              | in overlays.                               |                                          |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| LatLng             | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.        | If the element is invalid or not         |
|                    |                                         |              |              | Clearable in overlays.                     | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| PartyIds           | ``xs:IDREFS``                           | Optional     | Single       | If present, indicates which parties'       | If the field is invalid or not present,  |
|                    |                                         |              |              | primaries occur at this location.          | then the implementation is required to   |
|                    |                                         |              |              | Clearable in overlays.                     | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| PhotoUri           | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Link to a photo of the location. Clearable | If the element is invalid or not         |
|                    |                                         |              |              | in overlays.                               | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| EmergencyNotice    | :ref:`multi-xml-emergency-notice`       | Optional     | Repeats      | Emergency notice specific to this polling  | If the element is invalid or not         |
|                    |                                         |              |              | location. Permitted only in feed overlays. | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| IsInactive         | ``xs:string``                           | Optional     | Single       | Whether this polling location is closed or | If the field is invalid or not present,  |
|                    |                                         |              |              | inactive, and should be ignored, with the  | then the implementation is required to   |
|                    |                                         |              |              | text stating the reason why (e.g. "Closed  | ignore it.                               |
|                    |                                         |              |              | due to localized flooding; voters          |                                          |
|                    |                                         |              |              | redirected to High School", or "Backup     |                                          |
|                    |                                         |              |              | polling location"). Clearable in overlays. |                                          |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl00001">
      <AddressStructured language="en">
         <LocationName>ALBEMARLE HIGH SCHOOL</LocationName>
         <AddressLine>2775 Hydraulic Rd</AddressLine>
         <City>CHARLOTTESVILLE</City>
         <Region>VA</Region>
         <PostalCode>22901</PostalCode>
      </AddressStructured>
      <LocationIdentifier provider="google" relativePriority="1.0">
         <Type>pluscode</Type>
         <Value>87G83W52+4F</Value>
      </LocationIdentifier>
      <LocationType>InPersonDayOf</LocationType>
      <Directions>
         <Text language="en">Use gymnasium entrance on east side.</Text>
      </Directions>
      <Schedule>
         <TimeZone>America/New_York</TimeZone>
         <StartDate>2024-11-05</StartDate>
         <EndDate>2024-11-05</EndDate>
         <Hours>
            <StartTime>06:00:00</StartTime>
            <EndTime>19:00:00</EndTime>
         </Hours>
      </Schedule>
      <LatLng>
         <Latitude>38.0754627</Latitude>
         <Longitude>-78.5014875</Longitude>
      </LatLng>
   </PollingLocation>
