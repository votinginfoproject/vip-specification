.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-person:

person
======

``Person`` defines information about a person. The person may be a candidate, election administrator,
or elected official. These elements reference ``Person``:

* :ref:`multi-csv-candidate`

* :ref:`multi-csv-election-administration`

* :ref:`multi-csv-office`

+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+=======================================+==============+==============+==========================================+==========================================+
| contact_information_id | ``xs:IDREF``                          | Optional     | Repeats      | Refers to the associated                 | If the element is invalid or not         |
|                        |                                       |              |              | :ref:`multi-csv-contact-information`.    | present, then the implementation is      |
|                        |                                       |              |              |                                          | required to ignore it.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_of_birth          | ``xs:date``                           | Optional     | Single       | Represents the individual's date of      | If the field is invalid or not present,  |
|                        |                                       |              |              | birth.                                   | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers   | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Identifiers for this person.             | If the element is invalid or not         |
|                        |                                       |              |              |                                          | present, then the implementation is      |
|                        |                                       |              |              |                                          | required to ignore it.                   |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| first_name             | ``xs:string``                         | Optional     | Single       | Represents an individual's first name.   | If the field is invalid or not present,  |
|                        |                                       |              |              |                                          | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_name              | ``xs:string``                         | Optional     | Single       | Specifies a person's full name (**NB:**  | If the element is invalid or not         |
|                        |                                       |              |              | this information is                      | present, then the implementation is      |
|                        |                                       |              |              | :ref:`multi-csv-internationalized-text`  | required to ignore it.                   |
|                        |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                       |              |              | in multiple languages).                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| gender                 | ``xs:string``                         | Optional     | Single       | Specifies a person's gender.             | If the field is invalid or not present,  |
|                        |                                       |              |              |                                          | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| last_name              | ``xs:string``                         | Optional     | Single       | Represents an individual's last name.    | If the field is invalid or not present,  |
|                        |                                       |              |              |                                          | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| middle_name            | ``xs:string``                         | Optional     | Repeats      | Represents any number of names between   | If the field is invalid or not present,  |
|                        |                                       |              |              | an individual's first and last names     | then the implementation is required to   |
|                        |                                       |              |              | (e.g. John **Ronald Reuel** Tolkien).    | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| nickname               | ``xs:string``                         | Optional     | Single       | Represents an individual's nickname.     | If the field is invalid or not present,  |
|                        |                                       |              |              |                                          | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id               | ``xs:IDREF``                          | Optional     | Single       | Refers to the associated                 | If the field is invalid or not present,  |
|                        |                                       |              |              | :ref:`multi-csv-party`. This information | then the implementation is required to   |
|                        |                                       |              |              | is intended to be used by feed consumers | ignore it.                               |
|                        |                                       |              |              | to help them disambiguate the person's   |                                          |
|                        |                                       |              |              | identity, but not to be presented as     |                                          |
|                        |                                       |              |              | part of any ballot information. For that |                                          |
|                        |                                       |              |              | see :ref:`multi-csv-candidate`           |                                          |
|                        |                                       |              |              | **PartyId**.                             |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| prefix                 | ``xs:string``                         | Optional     | Single       | Specifies a prefix associated with a     | If the field is invalid or not present,  |
|                        |                                       |              |              | person (e.g. Dr.).                       | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| profession             | ``xs:string``                         | Optional     | Single       | Specifies a person's profession (**NB:** | If the element is invalid or not         |
|                        |                                       |              |              | this information is                      | present, then the implementation is      |
|                        |                                       |              |              | :ref:`multi-csv-internationalized-text`  | required to ignore it.                   |
|                        |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                       |              |              | in multiple languages).                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| suffix                 | ``xs:string``                         | Optional     | Single       | Specifies a suffix associated with a     | If the field is invalid or not present,  |
|                        |                                       |              |              | person (e.g. Jr.).                       | then the implementation is required to   |
|                        |                                       |              |              |                                          | ignore it.                               |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| title                  | ``xs:string``                         | Optional     | Single       | A title associated with a person         | If the element is invalid or not         |
|                        |                                       |              |              | (**NB:** this information is             | present, then the implementation is      |
|                        |                                       |              |              | :ref:`multi-csv-internationalized-text`  | required to ignore it.                   |
|                        |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                       |              |              | in multiple languages).                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date_of_birth,first_name,gender,last_name,middle_name,nickname,party_id,prefix,profession,suffix,title
    per50001,1961-08-04,Barack,male,Obama,Hussein,,par02,,President,II,Mr. President
    per50002,1985-11-21,Carly,female,Jepsen,Rae,,par01,,Recording Artist,,
    per50003,1926-09-23,John,male,Coltrane,William,Trane,par02,,Recording Artist,Saint,
    per50004,1926-05-26,Miles,male,Davis,Dewey,,par01,,Recording Artist,III,


.. _multi-csv-contact-information:

contact_information
-------------------

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`multi-csv-election-administration`, :ref:`multi-csv-office`,
:ref:`multi-csv-person`, :ref:`multi-csv-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+==========================+==============+==============+==========================================+==========================================+
| address_line  | ``xs:string``            | Optional     | Repeats      | The "location" portion of a mailing      | If the field is invalid or not present,  |
|               |                          |              |              | address. :ref:`See usage note.           | then the implementation is required to   |
|               |                          |              |              | <multi-csv-name-address-line-usage>`     | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions    | ``xs:string``            | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|               |                          |              |              | locating this entity.                    | present, then the implementation is      |
|               |                          |              |              |                                          | required to ignore it.                   |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| email         | ``xs:string``            | Optional     | Repeats      | An email address for the contact.        | If the field is invalid or not present,  |
|               |                          |              |              |                                          | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| fax           | ``xs:string``            | Optional     | Repeats      | A fax line for the contact.              | If the field is invalid or not present,  |
|               |                          |              |              |                                          | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours         | ``xs:string``            | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
|               |                          |              |              | the location is open *(NB: this element  | present, then the implementation is      |
|               |                          |              |              | is deprecated in favor of the more       | required to ignore it.                   |
|               |                          |              |              | structured :ref:`multi-csv-hours-open`   |                                          |
|               |                          |              |              | element. It is strongly encouraged that  |                                          |
|               |                          |              |              | data providers move toward contributing  |                                          |
|               |                          |              |              | hours in this format)*.                  |                                          |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id | ``xs:IDREF``             | Optional     | Single       | References an                            | If the field is invalid or not present,  |
|               |                          |              |              | :ref:`multi-csv-hours-open` element,     | then the implementation is required to   |
|               |                          |              |              | which lists the hours of operation for a | ignore it.                               |
|               |                          |              |              | location.                                |                                          |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| lat_long      | :ref:`multi-csv-lat-lng` | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|               |                          |              |              | this entity.                             | present, then the implementation is      |
|               |                          |              |              |                                          | required to ignore it.                   |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name          | ``xs:string``            | Optional     | Single       | The name of the location or contact.     | If the field is invalid or not present,  |
|               |                          |              |              | :ref:`See usage note.                    | then the implementation is required to   |
|               |                          |              |              | <multi-csv-name-address-line-usage>`     | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| phone         | ``xs:string``            | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|               |                          |              |              |                                          | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| uri           | ``xs:anyURI``            | Optional     | Repeats      | An informational URI for the contact or  | If the field is invalid or not present,  |
|               |                          |              |              | location.                                | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| parent_id     | ``xs:IDREF``             | Optional     | Repeats      | A reference to a record in source,       | If the field is invalid or not present,  |
|               |                          |              |              | department, voter_service, candidate,    | then the implementation is required to   |
|               |                          |              |              | person, or office.                       | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,address_line_1,address_line_2,address_line_3,directions,email,fax,hours,hours_open_id,latitude,longitude,latlng_source,name,phone,uri,parent_id
    ci0827,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,off001
    ci0828,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,vs01
