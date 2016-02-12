.. This file is auto-generated.  Do not edit it by hand!

+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation | :ref:`multi-xml-contact-information`    | Optional     | Repeats      | Specifies contact information for the    | If the element is invalid or not         |
|                    |                                         |              |              | person.                                  | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateOfBirth        | ``xs:date``                             | Optional     | Single       | Represents the individual's date of      | If the field is invalid or not present,  |
|                    |                                         |              |              | birth.                                   | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FirstName          | ``xs:string``                           | Optional     | Single       | Represents an individual's first name.   | If the field is invalid or not present,  |
|                    |                                         |              |              |                                          | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullName           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a person's full name (**NB:**  | If the element is invalid or not         |
|                    |                                         |              |              | this information is                      | present, then the implementation is      |
|                    |                                         |              |              | :ref:`multi-xml-internationalized-text`  | required to ignore it.                   |
|                    |                                         |              |              | because it sometimes appears on ballots  |                                          |
|                    |                                         |              |              | in multiple languages).                  |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Gender             | ``xs:string``                           | Optional     | Single       | Specifies a person's gender.             | If the field is invalid or not present,  |
|                    |                                         |              |              |                                          | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LastName           | ``xs:string``                           | Optional     | Single       | Represents an individual's last name.    | If the field is invalid or not present,  |
|                    |                                         |              |              |                                          | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| MiddleName         | ``xs:string``                           | Optional     | Repeats      | Represents any number of names between   | If the field is invalid or not present,  |
|                    |                                         |              |              | an individual's first and last names     | then the implementation is required to   |
|                    |                                         |              |              | (e.g. John **Ronald Reuel** Tolkien).    | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Nickname           | ``xs:string``                           | Optional     | Single       | Represents an individual's nickname.     | If the field is invalid or not present,  |
|                    |                                         |              |              |                                          | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId            | ``xs:IDREF``                            | Optional     | Single       | Refers to the associated                 | If the field is invalid or not present,  |
|                    |                                         |              |              | :ref:`multi-xml-party`. This information | then the implementation is required to   |
|                    |                                         |              |              | is intended to be used by feed consumers | ignore it.                               |
|                    |                                         |              |              | to help them disambiguate the person's   |                                          |
|                    |                                         |              |              | identity, but not to be presented as     |                                          |
|                    |                                         |              |              | part of any ballot information. For that |                                          |
|                    |                                         |              |              | see :ref:`multi-xml-candidate`           |                                          |
|                    |                                         |              |              | **PartyId**.                             |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Prefix             | ``xs:string``                           | Optional     | Single       | Specifies a prefix associated with a     | If the field is invalid or not present,  |
|                    |                                         |              |              | person (e.g. Dr.).                       | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Profession         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a person's profession (**NB:** | If the element is invalid or not         |
|                    |                                         |              |              | this information is                      | present, then the implementation is      |
|                    |                                         |              |              | :ref:`multi-xml-internationalized-text`  | required to ignore it.                   |
|                    |                                         |              |              | because it sometimes appears on ballots  |                                          |
|                    |                                         |              |              | in multiple languages).                  |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Suffix             | ``xs:string``                           | Optional     | Single       | Specifies a suffix associated with a     | If the field is invalid or not present,  |
|                    |                                         |              |              | person (e.g. Jr.).                       | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Title              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | A title associated with a person         | If the element is invalid or not         |
|                    |                                         |              |              | (**NB:** this information is             | present, then the implementation is      |
|                    |                                         |              |              | :ref:`multi-xml-internationalized-text`  | required to ignore it.                   |
|                    |                                         |              |              | because it sometimes appears on ballots  |                                          |
|                    |                                         |              |              | in multiple languages).                  |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
