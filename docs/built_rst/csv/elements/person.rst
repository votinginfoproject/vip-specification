.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-person:

person
======

The Person object represents an individual (such as a candidate, election official, or party leader).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearContactInformation/>``, ``<ClearPartyId/>``, ``<ClearProfession/>``).

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| contact_information | :ref:`multi-csv-contact-information`    | Optional     | Repeats      | Contact information for the person.      | If the element is invalid or not         |
|                     |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date_of_birth       | ``xs:date``                             | Optional     | Single       | Date of birth of the person. Clearable   | If the field is invalid or not present,  |
|                     |                                         |              |              | in overlays.                             | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier | :ref:`multi-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                         |              |              | person to external systems. Clearable in | present, then the implementation is      |
|                     |                                         |              |              | overlays.                                | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| first_name          | ``xs:string``                           | Optional     | Single       | First name of the person. Clearable in   | If the field is invalid or not present,  |
|                     |                                         |              |              | overlays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| full_name           | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Full legal or preferred name of the      | If the element is invalid or not         |
|                     |                                         |              |              | person. Clearable in overlays.           | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| gender              | ``xs:string``                           | Optional     | Single       | Gender of the person. Clearable in       | If the field is invalid or not present,  |
|                     |                                         |              |              | overlays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| last_name           | ``xs:string``                           | Optional     | Single       | Last name of the person. Clearable in    | If the field is invalid or not present,  |
|                     |                                         |              |              | overlays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| middle_name         | ``xs:string``                           | Optional     | Repeats      | Middle name(s) of the person. Clearable  | If the field is invalid or not present,  |
|                     |                                         |              |              | in overlays.                             | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| nickname            | ``xs:string``                           | Optional     | Single       | Nickname or informal name. Clearable in  | If the field is invalid or not present,  |
|                     |                                         |              |              | overlays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id            | ``xs:IDREF``                            | Optional     | Single       | References the :ref:`multi-csv-party` to | If the field is invalid or not present,  |
|                     |                                         |              |              | which the person belongs. Clearable in   | then the implementation is required to   |
|                     |                                         |              |              | overlays.                                | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| prefix              | ``xs:string``                           | Optional     | Single       | Name prefix (e.g. "Dr.", "Rev.").        | If the field is invalid or not present,  |
|                     |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| profession          | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Occupation or profession of the person.  | If the element is invalid or not         |
|                     |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| suffix              | ``xs:string``                           | Optional     | Single       | Name suffix (e.g. "Jr.", "III", "Esq."). | If the field is invalid or not present,  |
|                     |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| title               | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Official title held by the person.       | If the element is invalid or not         |
|                     |                                         |              |              | Clearable in overlays.                   | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,first_name,last_name,middle_name,nickname,prefix,suffix,title,profession,party_id,date_of_birth,gender
    per50001,Ken,Cuccinelli,T.,,II,,Attorney General,Attorney,par0001,1968-07-30,male
