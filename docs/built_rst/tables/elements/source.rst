.. This file is auto-generated.  Do not edit it by hand!

+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+=========================================+==============+==============+==========================================+==========================================+
| Name            | ``xs:string``                           | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                 |                                         |              |              | that is providing the information.       | implementation is required to ignore the |
|                 |                                         |              |              |                                          | ``Source`` element containing it.        |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId           | ``xs:string``                           | **Required** | Single       | Specifies the ID of the organization.    | If the field is invalid, then the        |
|                 |                                         |              |              | VIP uses FIPS_ codes for this ID.        | implementation is required to ignore the |
|                 |                                         |              |              |                                          | ``Source`` element containing it.        |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateTime        | ``xs:dateTime``                         | **Required** | Single       | Specifies the date and time of the feed  | If the field is invalid, then the        |
|                 |                                         |              |              | production. The date/time is considered  | implementation is required to ignore it. |
|                 |                                         |              |              | to be in the timezone local to the       |                                          |
|                 |                                         |              |              | organization.                            |                                          |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                 |                                         |              |              | organization providing the data and what | present, then the implementation is      |
|                 |                                         |              |              | data is in the feed.                     | required to ignore it.                   |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri | ``xs:string``                           | Optional     | Single       | Specifies a URI to the home page of the  | If the field is invalid or not present,  |
|                 |                                         |              |              | organization publishing the data.        | then the implementation is required to   |
|                 |                                         |              |              |                                          | ignore it.                               |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactId   | ``xs:IDREF``                            | Optional     | Single       | Reference to the :ref:`multi-xml-person` | If the field is invalid or not present,  |
|                 |                                         |              |              | who will respond to inquiries about the  | then the implementation is required to   |
|                 |                                         |              |              | information contained within the file.   | ignore it.                               |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TouUri          | ``xs:anyURI``                           | Optional     | Single       | Specifies the website where the Terms of | If the field is invalid or not present,  |
|                 |                                         |              |              | Use for the information in this file can | then the implementation is required to   |
|                 |                                         |              |              | be found.                                | ignore it.                               |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Version         | ``xs:string``                           | **Required** | Single       | Specifies the version of the data        | If the field is invalid, then the        |
|                 |                                         |              |              |                                          | implementation is required to ignore it. |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
