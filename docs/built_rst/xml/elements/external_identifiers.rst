.. This file is auto-generated.  Do not edit it by hand!

.. _xml-multi-external-identifiers:

ExternalIdentifiers
===================

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :doc:`Candidate <candidate>`

* Any element that extends :doc:`ContestBase <contest_base>`

* :doc:`ElectoralDistrict <electoral_district>`

* :doc:`Locality <locality>`

* :doc:`Office <office>`

* :doc:`Party <party>`

* :doc:`Precinct <precinct>`

* :doc:`State <state>`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+--------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type             | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=======================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | `ExternalIdentifier`_ | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                    |                       |              |              | identifier it is (see                    | must be present for                      |
|                    |                       |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                    |                       |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                    |                       |              |              |                                          | present, the implementation is required  |
|                    |                       |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                    |                       |              |              |                                          | element.                                 |
+--------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _xml-multi-external-identifier:

ExternalIdentifier
------------------

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`IdentifierType               | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              | <../enumerations/identifier_type>` |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                    |              |              | :doc:`IdentifierType                     | the ``ElectionIdentifier`` containing    |
|              |                                    |              |              | <../enumerations/identifier_type>`.      | it.                                      |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | xs:string                          | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                    |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                    |              |              | outside the options listed in            | ignore it.                               |
|              |                                    |              |              | :doc:`IdentifierType                     |                                          |
|              |                                    |              |              | <../enumerations/identifier_type>`.      |                                          |
|              |                                    |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                    |              |              | using this field.                        |                                          |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | xs:string                          | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                    |              |              |                                          | the implementation is required to ignore |
|              |                                    |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                    |              |              |                                          | it.                                      |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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
