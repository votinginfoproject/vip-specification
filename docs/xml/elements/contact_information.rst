ContactInformation
==================

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:doc:`ElectionAdministration <election_administration>`, :doc:`Office <office>`,
:doc:`Person <person>`, :doc:`Source <source>`).

+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Tag            | Data Type                    | Required?        | Repeats?  | Description          | Error Handling       |
|                |                              |                  |           |                      |                      |
+================+==============================+==================+===========+======================+======================+
| identifier     |xs:string                     | **Required**     | Attribute |                      |                      |
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| AddressLine    |xs:string                     | Optional         | Repeats   |Represents the various|If the field is       |
|                |                              |                  |           |parts of an address to|invalid or not        |
|                |                              |                  |           |a physical location.  |present, the          |
|                |                              |                  |           |                      |implementation is     |
|                |                              |                  |           |                      |required to ignore it.|
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Email          |xs:string                     | Optional         | Repeats   |An email address for  |If the field is       |
|                |                              |                  |           |the contact.          |invalid or not        |
|                |                              |                  |           |                      |present, the          |
|                |                              |                  |           |                      |implementation is     |
|                |                              |                  |           |                      |required to ignore it.|
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Fax            |xs:string                     | Optional         | Repeats   |A fax line for the    |If the field is       |
|                |                              |                  |           |contact.              |invalid or not        |
|                |                              |                  |           |                      |present, the          |
|                |                              |                  |           |                      |implementation is     |
|                |                              |                  |           |                      |required to ignore it.|
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
|Hours           |:doc:`InternationalizedText   |Optional          | Single    |Contains the hours (in|If the element is     |
|**[deprecated]**|<internationalized_text>`     |                  |           |local time) that the  |invalid or not        |
|                |                              |                  |           |location is open *(NB:|present, the          |
|                |                              |                  |           |this element is       |implementation is     |
|                |                              |                  |           |deprecated in favor of|required to ignore it.|
|                |                              |                  |           |the more structured   |                      |
|                |                              |                  |           |:doc:`HoursOpen       |                      |
|                |                              |                  |           |<hours_open>` element.|                      |
|                |                              |                  |           |It is strongly        |                      |
|                |                              |                  |           |encouraged that data  |                      |
|                |                              |                  |           |providers move toward |                      |
|                |                              |                  |           |collecting hours in   |                      |
|                |                              |                  |           |this format)*.        |                      |
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| HoursOpenId    |xs:IDREF                      | Optional         | Single    |References an         |If the field is       |
|                |                              |                  |           |:doc:`HoursOpen       |invalid or not        |
|                |                              |                  |           |<hours_open>` element,|present, the          |
|                |                              |                  |           |which lists the hours |implementation is     |
|                |                              |                  |           |of operation for a    |required to ignore it.|
|                |                              |                  |           |location.             |                      |
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Name           | xs:string                    | Optional         | Single    |The name of the       |If the field is       |
|                |                              |                  |           |location or contact.  |invalid or not        |
|                |                              |                  |           |                      |present, the          |
|                |                              |                  |           |                      |implementation is     |
|                |                              |                  |           |                      |required to ignore it.|
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Phone          | xs:string                    | Optional         | Repeats   |A phone number for the|If the field is       |
|                |                              |                  |           |contact.              |invalid or not        |
|                |                              |                  |           |                      |present, the          |
|                |                              |                  |           |                      |implementation is     |
|                |                              |                  |           |                      |required to ignore it.|
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Uri            | xs:anyURI                    | Optional         | Repeats   |An informational URI  |If the field is       |
|                |                              |                  |           |for the contact or    |invalid or not        |
|                |                              |                  |           |location.             |present, the          |
|                |                              |                  |           |                      |implementation is     |
|                |                              |                  |           |                      |required to ignore it.|
+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
