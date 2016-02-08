.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-contact-information:

ContactInformation
==================

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`multi-xml-election-administration`, :ref:`multi-xml-office`,
:ref:`multi-xml-person`, :ref:`multi-xml-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=========================================+==============+==============+==========================================+==========================================+
| AddressLine      | ``xs:string``                           | Optional     | Repeats      | The "location" portion of a mailing      | If the field is invalid or not present,  |
|                  |                                         |              |              | address. :ref:`See usage note.           | then the implementation is required to   |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                  |                                         |              |              | locating this entity.                    | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Email            | ``xs:string``                           | Optional     | Repeats      | An email address for the contact.        | If the field is invalid or not present,  |
|                  |                                         |              |              |                                          | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Fax              | ``xs:string``                           | Optional     | Repeats      | A fax line for the contact.              | If the field is invalid or not present,  |
|                  |                                         |              |              |                                          | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]** |                                         |              |              | the location is open *(NB: this element  | present, then the implementation is      |
|                  |                                         |              |              | is deprecated in favor of the more       | required to ignore it.                   |
|                  |                                         |              |              | structured :ref:`multi-xml-hours-open`   |                                          |
|                  |                                         |              |              | element. It is strongly encouraged that  |                                          |
|                  |                                         |              |              | data providers move toward contributing  |                                          |
|                  |                                         |              |              | hours in this format)*.                  |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | ``xs:IDREF``                            | Optional     | Single       | References an                            | If the field is invalid or not present,  |
|                  |                                         |              |              | :ref:`multi-xml-hours-open` element,     | then the implementation is required to   |
|                  |                                         |              |              | which lists the hours of operation for a | ignore it.                               |
|                  |                                         |              |              | location.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng           | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                  |                                         |              |              | this entity.                             | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name             | ``xs:string``                           | Optional     | Single       | The name of the location or contact.     | If the field is invalid or not present,  |
|                  |                                         |              |              | :ref:`See usage note.                    | then the implementation is required to   |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Phone            | ``xs:string``                           | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|                  |                                         |              |              |                                          | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Uri              | ``xs:anyURI``                           | Optional     | Repeats      | An informational URI for the contact or  | If the field is invalid or not present,  |
|                  |                                         |              |              | location.                                | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _multi-xml-name-address-line-usage:

``Name`` and ``AddressLine`` Usage Note
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. code-block:: xml
   :linenos:

   <ContactInformation label="ci10861a">
      <AddressLine>1600 Pennsylvania Ave</AddressLine>
      <AddressLine>Washington, DC 20006</AddressLine>
      <Email>president@whitehouse.gov</Email>
      <Phone>202-456-1111</Phone>
      <Phone annotation="TDD">202-456-6213</Phone>
      <Uri>http://www.whitehouse.gov</Uri>
   </ContactInformation>
