.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-party:

Party
=====

This element describes a political party and the metadata associated with it. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated candidate contest can use the PrimaryPartyIds field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation       | ``xs:string``                           | Optional     | Single       | An abbreviation for the party name (e.g. | If the field is invalid or not present,  |
|                    |                                         |              |              | "DEM", "REP", "LIB", "GRN").             | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color              | :ref:`multi-xml-html-color-string`      | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                    |                                         |              |              | party, for use in maps and other         | present, then the implementation is      |
|                    |                                         |              |              | displays, as a 6-character hexadecimal   | required to ignore it.                   |
|                    |                                         |              |              | HTML color code (e.g. "0000FF" for blue, |                                          |
|                    |                                         |              |              | "FF0000" for red).                       |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`multi-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                         |              |              | party to other datasets.                 | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn          | ``xs:boolean``                          | Optional     | Single       | Signals if this political party is one   | If the field is invalid or not present,  |
|                    |                                         |              |              | that is officially recognized by a       | then the implementation is required to   |
|                    |                                         |              |              | local, state, or federal organization,   | ignore it.                               |
|                    |                                         |              |              | or represents a "write-in" in            |                                          |
|                    |                                         |              |              | jurisdictions which allow candidates to  |                                          |
|                    |                                         |              |              | free-form enter their political          |                                          |
|                    |                                         |              |              | affiliation.                             |                                          |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LeaderPersonIds    | ``xs:IDREFS``                           | Optional     | Single       | References to :ref:`multi-xml-person`    | If the field is invalid or not present,  |
|                    |                                         |              |              | elements for party leadership.           | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri            | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | URI pointing to the party logo.          | If the element is invalid or not         |
|                    |                                         |              |              |                                          | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name               | :ref:`multi-xml-internationalized-text` | **Required** | Single       | Official name of the party.              | If the element is invalid, then the      |
|                    |                                         |              |              |                                          | implementation is required to ignore the |
|                    |                                         |              |              |                                          | ``Party`` element containing it.         |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Party id="par0001">
      <Abbreviation>DEM</Abbreviation>
      <Color>0000FF</Color>
      <Name>
         <Text language="en">Democratic Party</Text>
         <Text language="es">Partido Demócrata</Text>
      </Name>
   </Party>
