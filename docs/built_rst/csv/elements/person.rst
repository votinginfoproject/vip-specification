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
