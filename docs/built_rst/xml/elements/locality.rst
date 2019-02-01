.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-locality:

Locality
========

The Locality object represents the jurisdiction below the :ref:`multi-xml-state` (e.g. county).

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                  | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`multi-xml-election-administration` | then the implementation is required to   |
|                          |                                       |              |              | object.                                  | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Another identifier for a locality that   | If the element is invalid or not         |
|                          |                                       |              |              | links to another dataset (e.g.           | present, then the implementation is      |
|                          |                                       |              |              | `OCD-ID`_)                               | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        | If the field is not present or invalid,  |
|                          |                                       |              |              |                                          | the implementation is required to ignore |
|                          |                                       |              |              |                                          | the Locality element containing it.      |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to a set of the         | If the field is invalid or not present,  |
|                          |                                       |              |              | locality's :ref:`polling locations       | the implementation is required to ignore |
|                          |                                       |              |              | <multi-xml-polling-location>`s. If early | it. However, the implementation should   |
|                          |                                       |              |              | vote centers or ballot drop locations    | still check to see if there are any      |
|                          |                                       |              |              | are locality-wide, they should be        | polling locations associated with this   |
|                          |                                       |              |              | specified here.                          | locality's state.                        |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                  | ``xs:IDREF``                          | **Required** | Single       | References the locality's                | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`multi-xml-state`.                  | the implementation is required to ignore |
|                          |                                       |              |              |                                          | the Locality element containing.         |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                          |                                       |              |              | county, town, et al.), which is one of   | then the implementation is required to   |
|                          |                                       |              |              | the various :ref:`DistrictType           | ignore it.                               |
|                          |                                       |              |              | enumerations <multi-xml-district-type>`. |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality   | If the field is invalid or not present,  |
|                          |                                       |              |              | that falls outside the options listed in | then the implementation is required to   |
|                          |                                       |              |              | :ref:`DistrictType                       | ignore it.                               |
|                          |                                       |              |              | <multi-xml-district-type>`.              |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <Locality id="loc70001">
     <ElectionAdministrationId>ea40001</ElectionAdministrationId>
     <ExternalIdentifiers>
       <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:va/county:albemarle</Value>
       </ExternalIdentifier>
     </ExternalIdentifiers>
     <Name>ALBEMARLE COUNTY</Name>
     <StateId>st51</StateId>
     <Type>county</Type>
   </Locality>


.. _multi-xml-external-identifiers:

ExternalIdentifiers
-------------------

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-xml-candidate`

* Any element that extends :ref:`multi-xml-contest-base`

* :ref:`multi-xml-electoral-district`

* :ref:`multi-xml-locality`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-precinct`

* :ref:`multi-xml-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+======================================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | :ref:`multi-xml-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                    |                                      |              |              | identifier it is (see                    | must be present for                      |
|                    |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                    |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                    |                                      |              |              |                                          | present, the implementation is required  |
|                    |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                    |                                      |              |              |                                          | element.                                 |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-external-identifier:

ExternalIdentifier
~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                                  |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                  |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                  |              |              | outside the options listed in            | ignore it.                               |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
|              |                                  |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                  |              |              | using this field.                        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
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
