Person
======



.. todo::
   
   Add preamble. Add description for PartyId, Prefix, Suffix, and Title.

.. todo::

   Remove id

+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| Tag                | Data Type                 | Required?    | Repeats?   | Description            | Error Handling                 |
|                    |                           |              |            |                        |                                |
+====================+===========================+==============+============+========================+================================+
| ContactInformation |:doc:`ContactInformation   | Optional     | Repeats    |                        |                                |
|                    |<contact_information>`     |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| DateOfBirth        | xs:date                   | Optional     | Single     |Represents the          |If the field is invalid or not  |
|                    |                           |              |            |individual's date of    |present, the implementation is  |
|                    |                           |              |            |birth.                  |required to ignore it.          |
|                    |                           |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| FirstName          | xs:string                 | Optional     | Single     |Represents an           |If the field is invalid or not  |
|                    |                           |              |            |individual's first name.|present, the implementation is  |
|                    |                           |              |            |                        |required to ignore it.          |
|                    |                           |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| LastName           | xs:string                 | Optional     | Single     |Represents an           |If the field is invalid or not  |
|                    |                           |              |            |individual's last name. |present, the implementation is  |
|                    |                           |              |            |                        |required to ignore it.          |
|                    |                           |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| MiddleName         | xs:string                 | Optional     | Repeats    |Represents any number of|If the field is invalid or not  |
|                    |                           |              |            |names between an        |present, the implementation is  |
|                    |                           |              |            |individual's first and  |required to ignore it.          |
|                    |                           |              |            |last names (e.g. John   |                                |
|                    |                           |              |            |**Ronald Reuel**        |                                |
|                    |                           |              |            |Tolkien).               |                                |
|                    |                           |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| Nickname           | xs:string                 | Optional     | Single     |Represents an           |If the field is invalid or not  |
|                    |                           |              |            |individual's nickname.  |present, the implementation is  |
|                    |                           |              |            |                        |required to ignore it.          |
|                    |                           |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| PartyId            | xs:IDREF                  | Optional     | Single     |Refers to the associated|If the field is invalid or not  |
|                    |                           |              |            |:doc:`Party <party>`.   |present, the implementation is  |
|                    |                           |              |            |                        |required to ignore it.          |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| Prefix             | xs:string                 | Optional     | Single     |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| Profession         |:doc:`InternationalizedText| Optional     | Single     |                        |                                |
|                    |<internationalized_text>`  |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| Suffix             | xs:string                 | Optional     | Single     |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+
| Title              |:doc:`InternationalizedText| Optional     | Single     |                        |                                |
|                    |<internationalized_text>`  |              |            |                        |                                |
+--------------------+---------------------------+--------------+------------+------------------------+--------------------------------+

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
