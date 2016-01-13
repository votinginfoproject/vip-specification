.. This file is auto-generated.  Do not edit it by hand!

+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=============================+==============+==============+==========================================+==========================================+
| AddressLine      | xs:string                   | **Required** | Repeats      | Represents the various parts of an       | At least one valid ``AddressLine`` must  |
|                  |                             |              |              | address to a polling location.           | be present for ``PollingLocation`` to be |
|                  |                             |              |              |                                          | valid. If no valid ``AddressLine`` is    |
|                  |                             |              |              |                                          | present, the implementation is required  |
|                  |                             |              |              |                                          | to ignore the ``PollingLocation``        |
|                  |                             |              |              |                                          | element containing it.                   |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions       | :doc:`InternationalizedText | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                  | <internationalized_text>`   |              |              | locating the polling location.           | present, then the implementation is      |
|                  |                             |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :doc:`InternationalizedText | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]** | <internationalized_text>`   |              |              | the polling location is open (**NB:**    | present, then the implementation is      |
|                  |                             |              |              | this element is deprecated in favor of   | required to ignore it.                   |
|                  |                             |              |              | the more structured :doc:`HoursOpen      |                                          |
|                  |                             |              |              | <hours_open>` element. It is strongly    |                                          |
|                  |                             |              |              | encouraged that data providers move      |                                          |
|                  |                             |              |              | toward contributing hours in this        |                                          |
|                  |                             |              |              | format).                                 |                                          |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | xs:IDREF                    | Optional     | Single       | Links to an :doc:`HoursOpen              | If the field is invalid or not present,  |
|                  |                             |              |              | <hours_open>` element, which is a        | then the implementation is required to   |
|                  |                             |              |              | schedule of dates and hours during which | ignore it.                               |
|                  |                             |              |              | the polling location is available.       |                                          |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsDropBox        | xs:boolean                  | Optional     | Single       | Indicates if this polling location is a  | If the field is invalid or not present,  |
|                  |                             |              |              | drop box.                                | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsEarlyVoting    | xs:boolean                  | Optional     | Single       | Indicates if this polling location is an | If the field is invalid or not present,  |
|                  |                             |              |              | early vote site.                         | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng           | `LatLng`_                   | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                  |                             |              |              | this polling location.                   | present, then the implementation is      |
|                  |                             |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PhotoUri         | xs:anyURI                   | Optional     | Single       | Contains a link to an image of the       | If the field is invalid or not present,  |
|                  |                             |              |              | polling location.                        | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
