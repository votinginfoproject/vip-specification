.. This file is auto-generated.  Do not edit it by hand!

+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=============================+==============+==============+==========================================+==========================================+
| AddressLine      | xs:string                   | Optional     | Repeats      | Represents the various parts of an       | If the field is invalid or not present,  |
|                  |                             |              |              | address of a physical or mailing         | the implementation is required to ignore |
|                  |                             |              |              | location.                                | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Email            | xs:string                   | Optional     | Repeats      | An email address for the contact.        | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | the implementation is required to ignore |
|                  |                             |              |              |                                          | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Fax              | xs:string                   | Optional     | Repeats      | A fax line for the contact.              | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | the implementation is required to ignore |
|                  |                             |              |              |                                          | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :doc:`InternationalizedText | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]** | <internationalized_text>`   |              |              | the location is open *(NB: this element  | present, the implementation is required  |
|                  |                             |              |              | is deprecated in favor of the more       | to ignore it.                            |
|                  |                             |              |              | structured :doc:`HoursOpen <hours_open>` |                                          |
|                  |                             |              |              | element. It is strongly encouraged that  |                                          |
|                  |                             |              |              | data providers move toward contributing  |                                          |
|                  |                             |              |              | hours in this format)*.                  |                                          |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | xs:IDREF                    | Optional     | Single       | References an :doc:`HoursOpen            | If the field is invalid or not present,  |
|                  |                             |              |              | <hours_open>` element, which lists the   | the implementation is required to ignore |
|                  |                             |              |              | hours of operation for a location.       | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name             | xs:string                   | Optional     | Single       | The name of the location or contact.     | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | the implementation is required to ignore |
|                  |                             |              |              |                                          | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Phone            | xs:string                   | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | the implementation is required to ignore |
|                  |                             |              |              |                                          | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Uri              | xs:anyURI                   | Optional     | Repeats      | An informational URI for the contact or  | If the field is invalid or not present,  |
|                  |                             |              |              | location.                                | the implementation is required to ignore |
|                  |                             |              |              |                                          | it.                                      |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
