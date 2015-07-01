Party
=====

This element describes a political party and the metadata associated with them.

.. include:: ../../tables/elements/party.rst

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
