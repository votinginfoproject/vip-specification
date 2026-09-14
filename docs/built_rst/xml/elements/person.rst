.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-person:

Person
======

The Person object represents an individual (such as a candidate, election official, or party leader).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearContactInformation/>``, ``<ClearPartyId/>``, ``<ClearProfession/>``).

+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation | :ref:`multi-xml-contact-information`    | Optional     | Repeats      | Contact information for the person.      | If the element is invalid or not         |
|                    |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateOfBirth        | ``xs:date``                             | Optional     | Single       | Date of birth of the person. Clearable   | If the field is invalid or not present,  |
|                    |                                         |              |              | in overlays.                             | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`multi-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                         |              |              | person to external systems. Clearable in | present, then the implementation is      |
|                    |                                         |              |              | overlays.                                | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FirstName          | ``xs:string``                           | Optional     | Single       | First name of the person. Clearable in   | If the field is invalid or not present,  |
|                    |                                         |              |              | overlays.                                | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullName           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Full legal or preferred name of the      | If the element is invalid or not         |
|                    |                                         |              |              | person. Clearable in overlays.           | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Gender             | ``xs:string``                           | Optional     | Single       | Gender of the person. Clearable in       | If the field is invalid or not present,  |
|                    |                                         |              |              | overlays.                                | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LastName           | ``xs:string``                           | Optional     | Single       | Last name of the person. Clearable in    | If the field is invalid or not present,  |
|                    |                                         |              |              | overlays.                                | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| MiddleName         | ``xs:string``                           | Optional     | Repeats      | Represents any number of names between   | If the field is invalid or not present,  |
|                    |                                         |              |              | an individual's first and last names     | then the implementation is required to   |
|                    |                                         |              |              | (e.g. John **Ronald Reuel** Tolkien).    | ignore it.                               |
|                    |                                         |              |              | Clearable in overlays.                   |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Nickname           | ``xs:string``                           | Optional     | Single       | Represents an individual's nickname      | If the field is invalid or not present,  |
|                    |                                         |              |              | (e.g. "Bill" for William). Clearable in  | then the implementation is required to   |
|                    |                                         |              |              | overlays.                                | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId            | ``xs:IDREF``                            | Optional     | Single       | Refers to the associated                 | If the field is invalid or not present,  |
|                    |                                         |              |              | :ref:`multi-xml-party`. This information | then the implementation is required to   |
|                    |                                         |              |              | is intended to be used by feed consumers | ignore it.                               |
|                    |                                         |              |              | to help them disambiguate the person's   |                                          |
|                    |                                         |              |              | identity, but not to be presented as     |                                          |
|                    |                                         |              |              | part of ballot information (for that see |                                          |
|                    |                                         |              |              | :ref:`multi-xml-candidate` PartyId).     |                                          |
|                    |                                         |              |              | Clearable in overlays.                   |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Prefix             | ``xs:string``                           | Optional     | Single       | Specifies a prefix associated with a     | If the field is invalid or not present,  |
|                    |                                         |              |              | person (e.g. "Dr.", "Rev.", "Hon.").     | then the implementation is required to   |
|                    |                                         |              |              | Clearable in overlays.                   | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Profession         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Occupation or profession of the person.  | If the element is invalid or not         |
|                    |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Suffix             | ``xs:string``                           | Optional     | Single       | Specifies a suffix associated with a     | If the field is invalid or not present,  |
|                    |                                         |              |              | person (e.g. "Jr.", "III", "Esq.").      | then the implementation is required to   |
|                    |                                         |              |              | Clearable in overlays.                   | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Title              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Official title held by the person.       | If the element is invalid or not         |
|                    |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Person id="per10961">
      <ContactInformation>
         <Email>ken@example.com</Email>
         <Phone>804-555-0100</Phone>
      </ContactInformation>
      <FirstName>Ken</FirstName>
      <FullName>
         <Text language="en">Ken T. Cuccinelli II</Text>
      </FullName>
      <Gender>male</Gender>
      <LastName>Cuccinelli</LastName>
      <MiddleName>T.</MiddleName>
      <PartyId>par0001</PartyId>
      <Suffix>II</Suffix>
      <Title>
         <Text language="en">Attorney General</Text>
      </Title>
   </Person>
