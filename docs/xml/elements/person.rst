Person
======

``Person`` defines information about a person. The person may be a candidate, election administrator,
or elected official. These elements reference ``Person``:

* :doc:`Candidate <candidate>`

* :doc:`ElectionAdministration <election_administration>`

* :doc:`Office <office>`

+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| Tag                | Data Type                 | Required?    | Repeats?   | Description               | Error Handling                 |
|                    |                           |              |            |                           |                                |
+====================+===========================+==============+============+===========================+================================+
| ContactInformation |:doc:`ContactInformation   | Optional     | Repeats    |Specifies contact          |If the element is invalid or not|
|                    |<contact_information>`     |              |            |information for the        |present, the implementation is  |
|                    |                           |              |            |person.                    |required to ignore it.          |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| DateOfBirth        | xs:date                   | Optional     | Single     |Represents the             |If the field is invalid or not  |
|                    |                           |              |            |individual's date of       |present, the implementation is  |
|                    |                           |              |            |birth.                     |required to ignore it.          |
|                    |                           |              |            |                           |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| FirstName          | xs:string                 | Optional     | Single     |Represents an              |If the field is invalid or not  |
|                    |                           |              |            |individual's first name.   |present, the implementation is  |
|                    |                           |              |            |                           |required to ignore it.          |
|                    |                           |              |            |                           |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| LastName           | xs:string                 | Optional     | Single     |Represents an              |If the field is invalid or not  |
|                    |                           |              |            |individual's last name.    |present, the implementation is  |
|                    |                           |              |            |                           |required to ignore it.          |
|                    |                           |              |            |                           |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| MiddleName         | xs:string                 | Optional     | Repeats    |Represents any number of   |If the field is invalid or not  |
|                    |                           |              |            |names between an           |present, the implementation is  |
|                    |                           |              |            |individual's first and     |required to ignore it.          |
|                    |                           |              |            |last names (e.g. John      |                                |
|                    |                           |              |            |**Ronald Reuel**           |                                |
|                    |                           |              |            |Tolkien).                  |                                |
|                    |                           |              |            |                           |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| Nickname           | xs:string                 | Optional     | Single     |Represents an              |If the field is invalid or not  |
|                    |                           |              |            |individual's nickname.     |present, the implementation is  |
|                    |                           |              |            |                           |required to ignore it.          |
|                    |                           |              |            |                           |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| PartyId            | xs:IDREF                  | Optional     | Single     |Refers to the associated   |If the field is invalid or not  |
|                    |                           |              |            |:doc:`Party <party>`.      |present, the implementation is  |
|                    |                           |              |            |                           |required to ignore it.          |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| Prefix             | xs:string                 | Optional     | Single     |Specifies a prefix         |If the field is invalid or not  |
|                    |                           |              |            |associated with a person   |present, the implementation is  |
|                    |                           |              |            |(e.g. Dr.).                |required to ignore it.          |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| Profession         |:doc:`InternationalizedText| Optional     | Single     |Specifies a person's       |If the field is invalid or not  |
|                    |<internationalized_text>`  |              |            |profession (**NB:** this   |present, the implementation is  |
|                    |                           |              |            |information is             |required to ignore it.          |
|                    |                           |              |            |:doc:`InternationalizedText|                                |
|                    |                           |              |            |<internationalized_text>`  |                                |
|                    |                           |              |            |because it sometimes       |                                |
|                    |                           |              |            |appears on ballots in      |                                |
|                    |                           |              |            |multiple languages).       |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| Suffix             | xs:string                 | Optional     | Single     |Specifies a suffix         |If the field is invalid or not  |
|                    |                           |              |            |associated with a person   |present, the implementation is  |
|                    |                           |              |            |(e.g. Jr.).                |required to ignore it.          |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+
| Title              |:doc:`InternationalizedText| Optional     | Single     |A title associated with a  |If the field is invalid or not  |
|                    |<internationalized_text>`  |              |            |person (**NB:** this       |present, the implementation is  |
|                    |                           |              |            |information is             |required to ignore it.          |
|                    |                           |              |            |:doc:`InternationalizedText|                                |
|                    |                           |              |            |<internationalized_text>`  |                                |
|                    |                           |              |            |because it sometimes       |                                |
|                    |                           |              |            |appears on ballots in      |                                |
|                    |                           |              |            |multiple languages).       |                                |
+--------------------+---------------------------+--------------+------------+---------------------------+--------------------------------+

.. code-block:: xml
   :linenos:

   <Person id="per50001">
      <ContactInformation identifier="ci60002">
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
