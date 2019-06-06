.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-person:

Person
======

``Person`` defines information about a person. The person may be a candidate, election administrator,
or elected official. These elements reference ``Person``:

* :ref:`multi-xml-candidate`

* :ref:`multi-xml-election-administration`

* :ref:`multi-xml-office`

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation  | :ref:`multi-xml-contact-information`    | Optional     | Repeats      | Specifies contact information for the    | If the element is invalid or not         |
|                     |                                         |              |              | person.                                  | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateOfBirth         | ``xs:date``                             | Optional     | Single       | Represents the individual's date of      | If the field is invalid or not present,  |
|                     |                                         |              |              | birth.                                   | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Identifiers for this person.             | If the element is invalid or not         |
|                     |                                         |              |              |                                          | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FirstName           | ``xs:string``                           | Optional     | Single       | Represents an individual's first name.   | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullName            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a person's full name (**NB:**  | If the element is invalid or not         |
|                     |                                         |              |              | this information is                      | present, then the implementation is      |
|                     |                                         |              |              | :ref:`multi-xml-internationalized-text`  | required to ignore it.                   |
|                     |                                         |              |              | because it sometimes appears on ballots  |                                          |
|                     |                                         |              |              | in multiple languages).                  |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Gender              | ``xs:string``                           | Optional     | Single       | Specifies a person's gender.             | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LastName            | ``xs:string``                           | Optional     | Single       | Represents an individual's last name.    | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| MiddleName          | ``xs:string``                           | Optional     | Repeats      | Represents any number of names between   | If the field is invalid or not present,  |
|                     |                                         |              |              | an individual's first and last names     | then the implementation is required to   |
|                     |                                         |              |              | (e.g. John **Ronald Reuel** Tolkien).    | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Nickname            | ``xs:string``                           | Optional     | Single       | Represents an individual's nickname.     | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId             | ``xs:IDREF``                            | Optional     | Single       | Refers to the associated                 | If the field is invalid or not present,  |
|                     |                                         |              |              | :ref:`multi-xml-party`. This information | then the implementation is required to   |
|                     |                                         |              |              | is intended to be used by feed consumers | ignore it.                               |
|                     |                                         |              |              | to help them disambiguate the person's   |                                          |
|                     |                                         |              |              | identity, but not to be presented as     |                                          |
|                     |                                         |              |              | part of any ballot information. For that |                                          |
|                     |                                         |              |              | see :ref:`multi-xml-candidate`           |                                          |
|                     |                                         |              |              | **PartyId**.                             |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Prefix              | ``xs:string``                           | Optional     | Single       | Specifies a prefix associated with a     | If the field is invalid or not present,  |
|                     |                                         |              |              | person (e.g. Dr.).                       | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Profession          | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a person's profession (**NB:** | If the element is invalid or not         |
|                     |                                         |              |              | this information is                      | present, then the implementation is      |
|                     |                                         |              |              | :ref:`multi-xml-internationalized-text`  | required to ignore it.                   |
|                     |                                         |              |              | because it sometimes appears on ballots  |                                          |
|                     |                                         |              |              | in multiple languages).                  |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Suffix              | ``xs:string``                           | Optional     | Single       | Specifies a suffix associated with a     | If the field is invalid or not present,  |
|                     |                                         |              |              | person (e.g. Jr.).                       | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Title               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | A title associated with a person         | If the element is invalid or not         |
|                     |                                         |              |              | (**NB:** this information is             | present, then the implementation is      |
|                     |                                         |              |              | :ref:`multi-xml-internationalized-text`  | required to ignore it.                   |
|                     |                                         |              |              | because it sometimes appears on ballots  |                                          |
|                     |                                         |              |              | in multiple languages).                  |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Person id="per50001">
      <ContactInformation label="ci60002">
        <Email>rwashburne@albemarle.org</Email>
        <Phone>4349724173</Phone>
      </ContactInformation>
      <FirstName>RICHARD</FirstName>
      <LastName>WASHBURNE</LastName>
      <MiddleName>J.</MiddleName>
      <Nickname>JAKE</Nickname>
      <Title>
        <Text language="en">General Registrar Physical</Text>
      </Title>
   </Person>


.. _multi-xml-contact-information:

ContactInformation
------------------

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
