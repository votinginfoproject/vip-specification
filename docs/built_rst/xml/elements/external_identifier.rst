.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-external-identifier:

ExternalIdentifier
==================

Specifies an external identifier for an entity, linking it to another dataset or system. ExternalIdentifier has optional attributes ``label`` and ``provider``.

In overlay feeds, this element is clearable using ``<ClearExternalIdentifier/>`` on elements where it is marked clearable.

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier from    | If the field is invalid or not present,  |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows defining an identifier type       | If the field is invalid or not present,  |
|              |                                  |              |              | outside                                  | then the implementation is required to   |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`. Type   | ignore it.                               |
|              |                                  |              |              | should be set to "other" when using this |                                          |
|              |                                  |              |              | field.                                   |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier value.          | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifier>
      <Type>ocd-id</Type>
      <Value>ocd-division/country:us/state:nc/county:durham</Value>
   </ExternalIdentifier>
   <ExternalIdentifier>
      <Type>fips</Type>
      <Value>37063</Value>
   </ExternalIdentifier>
   <ExternalIdentifier>
      <Type>other</Type>
      <OtherType>census</OtherType>
      <Value>99063</Value>
   </ExternalIdentifier>
