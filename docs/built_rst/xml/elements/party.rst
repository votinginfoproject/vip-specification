.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-party:

Party
=====

The Party object represents a political party or ballot grouping.

+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation       | ``xs:string``                           | Optional     | Single       | Abbreviation for the party name (e.g.    | If the field is invalid or not present,  |
|                    |                                         |              |              | "DEM", "REP").                           | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color              | :ref:`multi-xml-html-color-string`      | Optional     | Single       | Six-digit hexadecimal HTML color code    | If the element is invalid or not         |
|                    |                                         |              |              | associated with the party.               | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`multi-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                         |              |              | party to other datasets.                 | present, then the implementation is      |
|                    |                                         |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn          | ``xs:boolean``                          | Optional     | Single       | Indicates if the party represents        | If the field is invalid or not present,  |
|                    |                                         |              |              | write-in selections.                     | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
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
