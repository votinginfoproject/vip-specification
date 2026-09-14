.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-internationalized-text:

InternationalizedText
=====================

``InternationalizedText`` represents text translated into one or more languages. It has an optional attribute ``label``.

Text can be represented either as direct element content (treated as default language ``i-default``):

.. code-block:: xml

   <Name label="office_mayor">Mayor</Name>

or as one or more child ``<Text>`` elements with explicit language tags:

.. code-block:: xml

   <Name label="office_mayor">
      <Text language="en">Mayor</Text>
      <Text language="es">Alcalde</Text>
      <Text language="zh">市長</Text>
      <Text language="i-default">Mayor</Text>
   </Name>

NOTE: InternationalizedText is not supported in CSV submissions.

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Text         | :ref:`multi-xml-language-string` | Optional     | Repeats      | Contains the translated string of text   | If the element is invalid or not         |
|              |                                  |              |              | with a language attribute.               | present, then the implementation is      |
|              |                                  |              |              |                                          | required to ignore it.                   |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
