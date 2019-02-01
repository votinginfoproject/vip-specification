.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-person:

person
======

``Person`` defines information about a person. The person may be a candidate, election administrator,
or elected official. These elements reference ``Person``:

* :ref:`multi-csv-candidate`

* :ref:`multi-csv-election-administration`

* :ref:`multi-csv-office`

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| contact_information  | :ref:`multi-csv-contact-information`  | Optional     | Repeats      | Specifies contact information for the    | If the element is invalid or not         |
|                      |                                       |              |              | person.                                  | present, then the implementation is      |
|                      |                                       |              |              |                                          | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_of_birth        | ``xs:date``                           | Optional     | Single       | Represents the individual's date of      | If the field is invalid or not present,  |
|                      |                                       |              |              | birth.                                   | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Identifiers for this person.             | If the element is invalid or not         |
|                      |                                       |              |              |                                          | present, then the implementation is      |
|                      |                                       |              |              |                                          | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| first_name           | ``xs:string``                         | Optional     | Single       | Represents an individual's first name.   | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_name            | ``xs:string``                         | Optional     | Single       | Specifies a person's full name (**NB:**  | If the element is invalid or not         |
|                      |                                       |              |              | this information is                      | present, then the implementation is      |
|                      |                                       |              |              | :ref:`multi-csv-internationalized-text`  | required to ignore it.                   |
|                      |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                      |                                       |              |              | in multiple languages).                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| gender               | ``xs:string``                         | Optional     | Single       | Specifies a person's gender.             | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| last_name            | ``xs:string``                         | Optional     | Single       | Represents an individual's last name.    | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| middle_name          | ``xs:string``                         | Optional     | Repeats      | Represents any number of names between   | If the field is invalid or not present,  |
|                      |                                       |              |              | an individual's first and last names     | then the implementation is required to   |
|                      |                                       |              |              | (e.g. John **Ronald Reuel** Tolkien).    | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| nickname             | ``xs:string``                         | Optional     | Single       | Represents an individual's nickname.     | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id             | ``xs:IDREF``                          | Optional     | Single       | Refers to the associated                 | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-csv-party`. This information | then the implementation is required to   |
|                      |                                       |              |              | is intended to be used by feed consumers | ignore it.                               |
|                      |                                       |              |              | to help them disambiguate the person's   |                                          |
|                      |                                       |              |              | identity, but not to be presented as     |                                          |
|                      |                                       |              |              | part of any ballot information. For that |                                          |
|                      |                                       |              |              | see :ref:`multi-csv-candidate`           |                                          |
|                      |                                       |              |              | **PartyId**.                             |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| prefix               | ``xs:string``                         | Optional     | Single       | Specifies a prefix associated with a     | If the field is invalid or not present,  |
|                      |                                       |              |              | person (e.g. Dr.).                       | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| profession           | ``xs:string``                         | Optional     | Single       | Specifies a person's profession (**NB:** | If the element is invalid or not         |
|                      |                                       |              |              | this information is                      | present, then the implementation is      |
|                      |                                       |              |              | :ref:`multi-csv-internationalized-text`  | required to ignore it.                   |
|                      |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                      |                                       |              |              | in multiple languages).                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| suffix               | ``xs:string``                         | Optional     | Single       | Specifies a suffix associated with a     | If the field is invalid or not present,  |
|                      |                                       |              |              | person (e.g. Jr.).                       | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| title                | ``xs:string``                         | Optional     | Single       | A title associated with a person         | If the element is invalid or not         |
|                      |                                       |              |              | (**NB:** this information is             | present, then the implementation is      |
|                      |                                       |              |              | :ref:`multi-csv-internationalized-text`  | required to ignore it.                   |
|                      |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                      |                                       |              |              | in multiple languages).                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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

.. code-block:: csv-table
   :linenos:


    id,address_line_1,address_line_2,address_line_3,directions,email,fax,hours,hours_open_id,latitude,longitude,latlng_source,name,phone,uri,parent_id
    ci0827,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,off001
    ci0828,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,vs01


.. _multi-csv-internationalized-text:

internationalized_text
~~~~~~~~~~~~~~~~~~~~~~

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-csv-contest-base`

* Any element that extends :ref:`multi-csv-ballot-selection-base`

* :ref:`multi-csv-candidate`

* :ref:`multi-csv-contact-information`

* :ref:`multi-csv-election`

* :ref:`multi-csv-election-administration`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-person`

* :ref:`multi-csv-polling-location`

* :ref:`multi-csv-source`

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| text         | ``xs:string`` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |               |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |               |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |               |              |              |                                          | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |               |              |              |                                          | element.                                 |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-external-identifiers:

external_identifiers
--------------------

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-csv-candidate`

* Any element that extends :ref:`multi-csv-contest-base`

* :ref:`multi-csv-electoral-district`

* :ref:`multi-csv-locality`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-precinct`

* :ref:`multi-csv-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+---------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+======================================+==============+==============+==========================================+==========================================+
| external_identifier | :ref:`multi-csv-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                     |                                      |              |              | identifier it is (see                    | must be present for                      |
|                     |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                     |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                     |                                      |              |              |                                          | present, the implementation is required  |
|                     |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                     |                                      |              |              |                                          | element.                                 |
+---------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-external-identifier:

external_identifier
~~~~~~~~~~~~~~~~~~~

+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================+==============+==============+==========================================+==========================================+
| type         | ``identifier_type`` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                     |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                     |              |              |                                          | it.                                      |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``       | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                     |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                     |              |              | outside the options listed in            | ignore it.                               |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        |                                          |
|              |                     |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                     |              |              | using this field.                        |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``       | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                     |              |              |                                          | the implementation is required to ignore |
|              |                     |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                     |              |              |                                          | it.                                      |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-internationalized-text:

internationalized_text
----------------------

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-csv-contest-base`

* Any element that extends :ref:`multi-csv-ballot-selection-base`

* :ref:`multi-csv-candidate`

* :ref:`multi-csv-contact-information`

* :ref:`multi-csv-election`

* :ref:`multi-csv-election-administration`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-person`

* :ref:`multi-csv-polling-location`

* :ref:`multi-csv-source`

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| text         | ``xs:string`` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |               |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |               |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |               |              |              |                                          | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |               |              |              |                                          | element.                                 |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
