Person
======



.. todo::
   
   Add preamble. Add description for PartyId, Prefix, Suffix, and Title.

+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| Tag                | Data Type              | Required?    | Repeats?   | Description          | Error Handling                 |
|                    |                        |              |            |                      |                                |
+====================+========================+==============+============+======================+================================+
| id                 | xs:ID                  | **Required** | Attribute  |                      |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| ContactInformation | ContactInformation     | Optional     | Repeats    |                      |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| DateOfBirth        | xs:date                | Optional     | Single     |**DateOfBirth**       |If the **DateOfBirth** is       |
|                    |                        |              |            |represents the        |invalid or not present, the     |
|                    |                        |              |            |individual's date of  |implementation is required to   |
|                    |                        |              |            |birth.                |ignore it.                      |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| FirstName          | xs:string              | Optional     | Single     |**FirstName**         |If the **FirstName** is invalid |
|                    |                        |              |            |represents an         |or not present, the             |
|                    |                        |              |            |individual's first    |implementation is required to   |
|                    |                        |              |            |name.                 |ignore it.                      |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| LastName           | xs:string              | Optional     | Single     |**LastName**          |If the **LastName** is invalid  |
|                    |                        |              |            |represents an         |or not present, the             |
|                    |                        |              |            |individual's last     |implementation is required to   |
|                    |                        |              |            |name.                 |ignore it.                      |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| MiddleName         | xs:string              | Optional     | Repeats    |**MiddleName**        |If the **MiddleName** is invalid|
|                    |                        |              |            |represents any number |or not present, the             |
|                    |                        |              |            |of names between an   |implementation is required to   |
|                    |                        |              |            |individual's first and|ignore it.                      |
|                    |                        |              |            |last names (e.g. John |                                |
|                    |                        |              |            |**Ronald Reuel**      |                                |
|                    |                        |              |            |Tolkien).             |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| Nickname           | xs:string              | Optional     | Single     |**Nickname**          |If the **Nickname** is invalid  |
|                    |                        |              |            |represents an         |or not present, the             |
|                    |                        |              |            |individual's nickname.|implementation is required to   |
|                    |                        |              |            |                      |ignore it.                      |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| PartyId            | xs:IDREF               | Optional     | Single     |**PartyId** refers to |If the **PartyId** is invalid or|
|                    |                        |              |            |the associated        |not present, the implementation |
|                    |                        |              |            |:doc:`Party <party>`. |is required to ignore it.       |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| Prefix             | xs:string              | Optional     | Single     |                      |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| Profession         | InternationalizedText  | Optional     | Single     |                      |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| Suffix             | xs:string              | Optional     | Single     |                      |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+
| Title              | InternationalizedText  | Optional     | Single     |                      |                                |
+--------------------+------------------------+--------------+------------+----------------------+--------------------------------+

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
