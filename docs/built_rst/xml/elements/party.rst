.. This file is auto-generated.  Do not edit it by hand!

Party
=====

This element describes a political party and the metadata associated with them.

+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=================================================+==============+==============+==========================================+==========================================+
| Abbreviation        | xs:string                                       | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                     |                                                 |              |              |                                          | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color               | `HtmlColorString`_                              | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                     |                                                 |              |              | party, for use in maps and other         | present, then the implementation is      |
|                     |                                                 |              |              | displays.                                | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers that link this party   | If the element is invalid or not         |
|                     | </built_rst/xml/elements/external_identifiers>` |              |              | to other related data sets (e.g. a       | present, then the implementation is      |
|                     |                                                 |              |              | campaign finance system, etc).           | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri             | xs:anyURI                                       | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                     |                                                 |              |              | displays.                                | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | :doc:`InternationalizedText                     | Optional     | Single       | The name of the party.                   | If the element is invalid or not         |
|                     | <internationalized_text>`                       |              |              |                                          | present, then the implementation is      |
|                     |                                                 |              |              |                                          | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


HtmlColorString
---------------

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``

.. code-block:: xml
   :linenos:

   <Party id="par0001">
     <Abbreviation>REP</Abbreviation>
     <Color>e91d0e</Color>
     <Name>
       <Text language="en">Republican</Text>
     </Name>
   </Party>
