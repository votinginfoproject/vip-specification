.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-party:

Party
=====

This element describes a political party and the metadata associated with them. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated :ref:`multi-xml-candidate-contest` can use the **PrimaryPartyIds** field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation        | ``xs:string``                           | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color               | :ref:`multi-xml-html-color-string`      | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                     |                                         |              |              | party, for use in maps and other         | present, then the implementation is      |
|                     |                                         |              |              | displays.                                | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers that link this party   | If the element is invalid or not         |
|                     |                                         |              |              | to other related data sets (e.g. a       | present, then the implementation is      |
|                     |                                         |              |              | campaign finance system, etc).           | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | ``xs:boolean``                          | Optional     | Single       | Signals if this political party is one   | If the field is invalid or not present,  |
|                     |                                         |              |              | that is officially recognized by a       | then the implementation is required to   |
|                     |                                         |              |              | local, state, or federal organization,   | ignore it.                               |
|                     |                                         |              |              | or is a "write-in" in jurisdictions      |                                          |
|                     |                                         |              |              | which allow candidates to free-form      |                                          |
|                     |                                         |              |              | enter their political affiliation. If    |                                          |
|                     |                                         |              |              | this field is not present then it is     |                                          |
|                     |                                         |              |              | assumed to be false.                     |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LeaderPersonIds     | ``xs:IDREFS``                           | Optional     | Single       | A reference of :ref:`multi-xml-person`   | If the field is invalid or not present,  |
|                     |                                         |              |              | elements which are leaders of the        | then the implementation is required to   |
|                     |                                         |              |              | `Party`.                                 | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri             | ``xs:anyURI``                           | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                     |                                         |              |              | displays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | :ref:`multi-xml-internationalized-text` | **Required** | Single       | The name of the party.                   | If the element is invalid, then the      |
|                     |                                         |              |              |                                          | implementation is required to ignore it. |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Party id="par0001">
     <Abbreviation>REP</Abbreviation>
     <Color>e91d0e</Color>
     <IsWriteIn>false</IsWriteIn>
     <LeaderPersonIds>per01</LeaderPersonIds>
     <Name>
       <Text language="en">Republican</Text>
     </Name>
   </Party>


.. _multi-xml-html-color-string:

HtmlColorString
---------------

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``
