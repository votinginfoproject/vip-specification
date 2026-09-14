.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-polling-location:

polling_location
================

The PollingLocation object represents a site where voters cast ballots in person or drop off early/absentee ballots. In VIP 7.0, facility names are placed in ``AddressStructured.LocationName``.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearDirections/>``, ``<ClearPhotoUri/>``, ``<ClearIsInactive/>``). AddressStructured and LocationType are optional in overlays.
EmergencyNotice is permitted only in overlays.
In overlays, PollingLocation has an optional attribute ``isNew="true"`` to indicate that a polling location is newly added rather than modifying an existing one.

+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                                | Error Handling                           |
+=====================+=========================================+==============+==============+============================================+==========================================+
| address_structured  | :ref:`multi-csv-simple-address-type`    | **Required** | Repeats      | Structured address including facility      | AddressStructured is required for        |
|                     |                                         |              |              | name. Required in main feed; optional in   | PollingLocation in main feeds.           |
|                     |                                         |              |              | overlays. Multiple addresses in different  |                                          |
|                     |                                         |              |              | languages can be specified.                |                                          |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| location_identifier | :ref:`multi-csv-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus | If the element is invalid or not         |
|                     |                                         |              |              | Code, geocoder ID). Clearable in overlays. | present, then the implementation is      |
|                     |                                         |              |              |                                            | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| directions          | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Instructions for locating the polling site | If the element is invalid or not         |
|                     |                                         |              |              | or room. Clearable in overlays.            | present, then the implementation is      |
|                     |                                         |              |              |                                            | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| hours               | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Operating hours as text. Clearable in      | If the element is invalid or not         |
|                     |                                         |              |              | overlays. *(NB: deprecated in favor of     | present, then the implementation is      |
|                     |                                         |              |              | :ref:`multi-csv-schedule-with-timezone`)*. | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| schedule            | :ref:`multi-csv-schedule-with-timezone` | Optional     | Repeats      | Structured schedule of operating dates and | If the element is invalid or not         |
|                     |                                         |              |              | hours. Clearable in overlays.              | present, then the implementation is      |
|                     |                                         |              |              |                                            | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| location_type       | :ref:`multi-csv-polling-location-type`  | **Required** | Single       | The type of voting conducted at this       | LocationType is required for             |
|                     |                                         |              |              | location (InPersonDayOf, InPersonEarly, or | PollingLocation in main feeds.           |
|                     |                                         |              |              | DropOff). Required in main feed; optional  |                                          |
|                     |                                         |              |              | in overlays.                               |                                          |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| lat_lng             | :ref:`multi-csv-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.        | If the element is invalid or not         |
|                     |                                         |              |              | Clearable in overlays.                     | present, then the implementation is      |
|                     |                                         |              |              |                                            | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| party_ids           | ``xs:IDREFS``                           | Optional     | Single       | If present, indicates which parties'       | If the field is invalid or not present,  |
|                     |                                         |              |              | primaries occur at this location.          | then the implementation is required to   |
|                     |                                         |              |              | Clearable in overlays.                     | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| photo_uri           | :ref:`multi-csv-internationalized-uri`  | Optional     | Single       | Link to a photo of the location. Clearable | If the element is invalid or not         |
|                     |                                         |              |              | in overlays.                               | present, then the implementation is      |
|                     |                                         |              |              |                                            | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| is_inactive         | ``xs:string``                           | Optional     | Single       | If specified, marks the location as closed | If the field is invalid or not present,  |
|                     |                                         |              |              | or inactive, with the text stating the     | then the implementation is required to   |
|                     |                                         |              |              | reason why. Clearable in overlays.         | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,location_type,directions,photo_uri,party_ids,is_inactive
    poll001,InPersonDayOf,Use gymnasium entrance,https://example.gov/poll.jpg,,
    poll002,DropOff,Curbside ballot drop box,,,Water main break
