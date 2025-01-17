.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-locality:

Locality
========

The Locality object represents the jurisdiction below the :ref:`multi-xml-state` (e.g. county).

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                  |                                          |
|                          |                                       |              |              | :ref:`multi-xml-election-administration` |                                          |
|                          |                                       |              |              | object.                                  |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Another identifier for a locality that   |                                          |
|                          |                                       |              |              | links to another dataset (e.g.           |                                          |
|                          |                                       |              |              | `OCD-ID`_)                               |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly               | ``xs:boolean``                        | Optional     | Single       | Determines if the locality runs          | If the field is missing or invalid, the  |
|                          |                                       |              |              | mail-only elections. If this is true,    | implementation is required to assume     |
|                          |                                       |              |              | then all precincts a part of the         | `IsMailOnly` is false.                   |
|                          |                                       |              |              | locality will also run mail-only         |                                          |
|                          |                                       |              |              | elections. Drop boxes may be used in     |                                          |
|                          |                                       |              |              | addition to this flag using a            |                                          |
|                          |                                       |              |              | :ref:`polling location                   |                                          |
|                          |                                       |              |              | <multi-xml-polling-location>` record     |                                          |
|                          |                                       |              |              | configured as a Drop Box.                |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to a set of the         |                                          |
|                          |                                       |              |              | locality's :ref:`polling locations       |                                          |
|                          |                                       |              |              | <multi-xml-polling-location>`s. If early |                                          |
|                          |                                       |              |              | vote centers or ballot drop locations    |                                          |
|                          |                                       |              |              | are locality-wide, they should be        |                                          |
|                          |                                       |              |              | specified here.                          |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                  | ``xs:IDREF``                          | **Required** | Single       | References the locality's                |                                          |
|                          |                                       |              |              | :ref:`multi-xml-state`.                  |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.       |                                          |
|                          |                                       |              |              | county, town, et al.), which is one of   |                                          |
|                          |                                       |              |              | the various :ref:`DistrictType           |                                          |
|                          |                                       |              |              | enumerations <multi-xml-district-type>`. |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality   |                                          |
|                          |                                       |              |              | that falls outside the options listed in |                                          |
|                          |                                       |              |              | :ref:`DistrictType                       |                                          |
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
     <IsMailOnly>true</IsMailOnly>
     <Name>ALBEMARLE COUNTY</Name>
     <StateId>st51</StateId>
     <Type>county</Type>
   </Locality>
