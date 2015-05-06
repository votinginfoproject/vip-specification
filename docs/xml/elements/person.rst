Person
======

.. todo::

   Add preamble. Add description for PartyId, Prefix, Suffix, and Title.

+------------------+---------------------+-----------------+-----------------+---------------+
|Tag               |Data                 |Optional/Required|Description      |Error          |
|                  |Type                 |                 |                 |Handling       |
+==================+=====================+=================+=================+===============+
|ContactInformation|ContactInformation   |Optional         |                 |               |
+------------------+---------------------+-----------------+-----------------+---------------+
|DateOfBirth       |Date                 |Optional         |**DateOfBirth**  |If the         |
|                  |                     |                 |represents the   |**DateOfBirth**|
|                  |                     |                 |individual's     |is invalid or  |
|                  |                     |                 |date of birth.   |not present,   |
|                  |                     |                 |                 |the            |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|FirstName         |String               |Optional         |**FirstName**    |If the         |
|                  |                     |                 |represents an    |**FirstName**  |
|                  |                     |                 |individual's     |is invalid or  |
|                  |                     |                 |first name.      |not present,   |
|                  |                     |                 |                 |the            |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|LastName          |String               |Optional         |**LastName**     |If the         |
|                  |                     |                 |represents an    |**LastName** is|
|                  |                     |                 |individual's     |invalid or not |
|                  |                     |                 |last name.       |present, the   |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|MiddleName        |String               |Optional;        |**MiddleName**   |If the         |
|                  |                     |multiple allowed |represents any   |**LastName** is|
|                  |                     |                 |number of names  |invalid or not |
|                  |                     |                 |between an       |present, the   |
|                  |                     |                 |individual's     |implementation |
|                  |                     |                 |first and last   |is required to |
|                  |                     |                 |names.           |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|Nickname          |String               |Optional         |**Nickname**     |If the         |
|                  |                     |                 |represents an    |**Nickname** is|
|                  |                     |                 |individual's     |invalid or not |
|                  |                     |                 |nickname.        |present, the   |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|PartyId           |IDREF                |Optional         |**PartyId**      |If the         |
|                  |                     |                 |refers to the    |**PartyId** is |
|                  |                     |                 |associated       |invalid or not |
|                  |                     |                 |**Party**.       |present, the   |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|Prefix            |String               |Optional         |                 |               |
+------------------+---------------------+-----------------+-----------------+---------------+
|Profession        |InternationalizedText|Optional         |**Profession**   |If the         |
|                  |                     |                 |describes an     |**Profession** |
|                  |                     |                 |individuals      |is invalid or  |
|                  |                     |                 |profession.      |not present,   |
|                  |                     |                 |                 |the            |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|Suffix            |String               |Optional         |                 |If the         |
|                  |                     |                 |                 |**Suffix** is  |
|                  |                     |                 |                 |invalid or not |
|                  |                     |                 |                 |present, the   |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+
|Title             |InternationalizedText|Optional         |**Title**        |If the         |
|                  |                     |                 |                 |**Title** is   |
|                  |                     |                 |                 |invalid or not |
|                  |                     |                 |                 |present, the   |
|                  |                     |                 |                 |implementation |
|                  |                     |                 |                 |is required to |
|                  |                     |                 |                 |ignore it.     |
+------------------+---------------------+-----------------+-----------------+---------------+


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
