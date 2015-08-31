ContactInformation
==================

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:doc:`ElectionAdministration <election_administration>`, :doc:`Office <office>`,
:doc:`Person <person>`, :doc:`Source <source>`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+----------------+------------------------------+------------------+-----------+----------------------+----------------------+
| Tag            | Data Type                    | Required?        | Repeats?  | Description          | Error Handling       |
|                |                              |                  |           |                      |                      |
+================+==============================+==================+===========+======================+======================+
| AddressLine    |xs:string                     | Optional         | Repeats   |The "location" portion|If the field is       |
|                |                              |                  |           |of a mailing address. |invalid or not        |
|                |                              |                  |           |`See usage note.`_    |present, the          |
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
|                |                              |                  |           |contributing hours in |                      |
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
|                |                              |                  |           |`See usage note.`_    |present, the          |
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


.. _See usage note.:

``Name`` and ``AddressLine`` Usage Note
---------------------------------------

The ``Name`` and ``AddressLine`` fields should be chosen so that a display
or mailing address can be constructed programmatically by joining the
``Name`` and ``AddressLine`` fields together.  For example, for the
following address::

    Department of Elections
    1 Dr. Carlton B. Goodlett Place, Room 48
    San Francisco, CA 94102

The name could be "Department of Elections" and the first address line
could be "1 Dr. Carlton B. Goodlett Place, Room 48."

However, VIP does not yet support the representation of mailing addresses
whose "name" portion spans more than one line, for example::

    California Secretary of State
    Elections Division
    1500 11th Street
    Sacramento, CA 95814

For addresses like the above, we recommend choosing a name like, "California
Secretary of State, Elections Division" with "1500 11th Street" as the
first address line. This would result in a programmatically constructed
address like the following::

    California Secretary of State, Elections Division
    1500 11th Street
    Sacramento, CA 95814
