.. This file is auto-generated.  Do not edit it by hand!

+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+=============================+==============+==============+==========================================+==========================================+
| Name            | xs:string                   | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                 |                             |              |              | that is providing the information.       | implementation is required to ignore the |
|                 |                             |              |              |                                          | source element containing it.            |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId           | xs:string                   | **Required** | Single       | Specifies the ID of the organization as  | If the field is invalid, then the        |
|                 |                             |              |              | assigned by VIP. This ID is not an       | implementation is required to ignore the |
|                 |                             |              |              | attribute so as not to interfere with    | source element containing it.            |
|                 |                             |              |              | organizations' own numbering conventions |                                          |
|                 |                             |              |              | (since id attributes must be unique      |                                          |
|                 |                             |              |              | across the entire file).                 |                                          |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateTime        | xs:dateTime                 | **Required** | Single       | Specifies the date and time of the feed  | If the field is invalid, then the        |
|                 |                             |              |              | production. The date/time is considered  | implementation is required to ignore the |
|                 |                             |              |              | to be in the timezone local to the       | element containing it.                   |
|                 |                             |              |              | organization. This datetime is required  |                                          |
|                 |                             |              |              | to match the datetime specified in the   |                                          |
|                 |                             |              |              | feed's filename.                         |                                          |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description     | :doc:`InternationalizedText | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                 | <internationalized_text>`   |              |              | organization providing the data and what | present, then the implementation is      |
|                 |                             |              |              | data is in the feed.                     | required to ignore it.                   |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUrl | xs:string                   | Optional     | Single       | Specifies a URL to the home page of the  | If the field is invalid or not present,  |
|                 |                             |              |              | organization publishing the data.        | then the implementation is required to   |
|                 |                             |              |              |                                          | ignore it.                               |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactId   | xs:IDREF                    | Optional     | Single       | Reference to the :doc:`person <person>`  | If the field is invalid or not present,  |
|                 |                             |              |              | who will respond to inquiries about the  | then the implementation is required to   |
|                 |                             |              |              | information contained within the file.   | ignore it.                               |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TouUrl          | xs:anyURI                   | Optional     | Single       | Specifies the website where the Terms of | If the field is invalid or not present,  |
|                 |                             |              |              | Use for the information in this file can | then the implementation is required to   |
|                 |                             |              |              | be found.                                | ignore it.                               |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
