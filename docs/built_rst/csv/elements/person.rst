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
| date_of_birth          | ``xs:date``                           | Optional     | Single       | Represents the individual's date of      |                                          |
|                        |                                       |              |              | birth.                                   |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers   | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Identifiers for this person.             |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| first_name             | ``xs:string``                         | Optional     | Single       | Represents an individual's first name.   |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_name              | ``xs:string``                         | Optional     | Single       | Specifies a person's full name (**NB:**  |                                          |
|                        |                                       |              |              | this information is                      |                                          |
|                        |                                       |              |              | :ref:`multi-csv-internationalized-text`  |                                          |
|                        |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                       |              |              | in multiple languages).                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| gender                 | ``xs:string``                         | Optional     | Single       | Specifies a person's gender.             |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| last_name              | ``xs:string``                         | Optional     | Single       | Represents an individual's last name.    |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| middle_name            | ``xs:string``                         | Optional     | Repeats      | Represents any number of names between   |                                          |
|                        |                                       |              |              | an individual's first and last names     |                                          |
|                        |                                       |              |              | (e.g. John **Ronald Reuel** Tolkien).    |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| nickname               | ``xs:string``                         | Optional     | Single       | Represents an individual's nickname.     |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id               | ``xs:IDREF``                          | Optional     | Single       | Refers to the associated                 |                                          |
|                        |                                       |              |              | :ref:`multi-csv-party`. This information |                                          |
|                        |                                       |              |              | is intended to be used by feed consumers |                                          |
|                        |                                       |              |              | to help them disambiguate the person's   |                                          |
|                        |                                       |              |              | identity, but not to be presented as     |                                          |
|                        |                                       |              |              | part of any ballot information. For that |                                          |
|                        |                                       |              |              | see :ref:`multi-csv-candidate`           |                                          |
|                        |                                       |              |              | **PartyId**.                             |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| prefix                 | ``xs:string``                         | Optional     | Single       | Specifies a prefix associated with a     |                                          |
|                        |                                       |              |              | person (e.g. Dr.).                       |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| profession             | ``xs:string``                         | Optional     | Single       | Specifies a person's profession (**NB:** |                                          |
|                        |                                       |              |              | this information is                      |                                          |
|                        |                                       |              |              | :ref:`multi-csv-internationalized-text`  |                                          |
|                        |                                       |              |              | because it sometimes appears on ballots  |                                          |
|                        |                                       |              |              | in multiple languages).                  |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| suffix                 | ``xs:string``                         | Optional     | Single       | Specifies a suffix associated with a     |                                          |
|                        |                                       |              |              | person (e.g. Jr.).                       |                                          |
+------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| title                  | ``xs:string``                         | Optional     | Single       | A title associated with a person         |                                          |
|                        |                                       |              |              | (**NB:** this information is             |                                          |
|                        |                                       |              |              | :ref:`multi-csv-internationalized-text`  |                                          |
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
