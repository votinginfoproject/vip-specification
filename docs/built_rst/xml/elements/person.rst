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
| MiddleName         | ``xs:string``                           | Optional     | Repeats      | Middle name(s) of the person. Clearable  | If the field is invalid or not present,  |
|                    |                                         |              |              | in overlays.                             | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Nickname           | ``xs:string``                           | Optional     | Single       | Nickname or informal name. Clearable in  | If the field is invalid or not present,  |
|                    |                                         |              |              | overlays.                                | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId            | ``xs:IDREF``                            | Optional     | Single       | References the :ref:`multi-xml-party` to | If the field is invalid or not present,  |
|                    |                                         |              |              | which the person belongs. Clearable in   | then the implementation is required to   |
|                    |                                         |              |              | overlays.                                | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Prefix             | ``xs:string``                           | Optional     | Single       | Name prefix (e.g. "Dr.", "Rev.").        | If the field is invalid or not present,  |
|                    |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Profession         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Occupation or profession of the person.  | If the element is invalid or not         |
|                    |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Suffix             | ``xs:string``                           | Optional     | Single       | Name suffix (e.g. "Jr.", "III", "Esq."). | If the field is invalid or not present,  |
|                    |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
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
