Party
=====

This element describes a political party and the metadata associated with them.

+---------------------+---------------------------+-----------+----------+----------------------+-------------------------------+
| Tag                 | Data Type                 | Required? | Repeats? |Description           |Error Handling                 |
|                     |                           |           |          |                      |                               |
+=====================+===========================+===========+==========+======================+===============================+
| Abbreviation        | xs:string                 | Optional  | Single   |An abbreviation for   |If the field is invalid or not |
|                     |                           |           |          |the party name.       |present, the implementation is |
|                     |                           |           |          |                      |required to ignore it.         |
+---------------------+---------------------------+-----------+----------+----------------------+-------------------------------+
| Color               | HtmlColorString           | Optional  | Single   |The preferred display |If the field is invalid or not |
|                     |                           |           |          |color for the party,  |present, the implementation is |
|                     |                           |           |          |for use in maps and   |required to ignore it.         |
|                     |                           |           |          |other displays.       |                               |
+---------------------+---------------------------+-----------+----------+----------------------+-------------------------------+
| ExternalIdentifiers |:doc:`ExternalIdentifiers  | Optional  | Single   |Other identifiers that|If the field is invalid or not |
|                     |<external_identifiers>`    |           |          |link this party to    |present, the implementation is |
|                     |                           |           |          |other related data    |required to ignore it.         |
|                     |                           |           |          |sets (e.g. a campaign |                               |
|                     |                           |           |          |finance system, etc). |                               |
+---------------------+---------------------------+-----------+----------+----------------------+-------------------------------+
| LogoUri             | xs:anyURI                 | Optional  | Single   |Web address of a logo |If the field is invalid or not |
|                     |                           |           |          |to use in displays.   |present, the implementation is |
|                     |                           |           |          |                      |required to ignore it.         |
+---------------------+---------------------------+-----------+----------+----------------------+-------------------------------+
| Name                |:doc:`InternationalizedText| Optional  | Single   |The name of the party.|If the field is invalid or not |
|                     |<internationalized_text>`  |           |          |                      |present, the implementation is |
|                     |                           |           |          |                      |required to ignore it.         |
+---------------------+---------------------------+-----------+----------+----------------------+-------------------------------+

.. code-block:: xml
   :linenos:

   <Party id="par0001">
     <Abbreviation>REP</Abbreviation>
     <Color>e91d0e</Color>
     <Name>
       <Text language="en">Republican</Text>
     </Name>
   </Party>
