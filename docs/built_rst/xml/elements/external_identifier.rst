.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-external-identifier:

ExternalIdentifier
==================

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier. Must   |                                          |
|              |                                  |              |              | be one of the valid types as defined by  |                                          |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows for cataloging an                 |                                          |
|              |                                  |              |              | ``ExternalIdentifier`` type that falls   |                                          |
|              |                                  |              |              | outside the options listed in            |                                          |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
|              |                                  |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                  |              |              | using this field.                        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier.                |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifiers>
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:nc/county:durham</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>FIPS</Type>
         <Value>37063</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>OTHER</Type>
         <OtherType>GNIS</OtherType>
         <Value>1008550</Value>
      </ExternalIdentifier>
      <external_identifer>
         <Type>OTHER</Type>
         <OtherType>census</OtherType>
         <Value>99063</Value>
      </ExternalIdentifier>
   </ExternalIdentifiers>
