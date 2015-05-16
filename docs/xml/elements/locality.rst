Locality
========

The Locality object represents the jurisdiction below the :doc:`state <state>` (e.g. county).

.. todo::

   Fill out description for ExternalIdentifiers

+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| Tag                      | Data Type           | Required?   | Repeats? | Description                     | Error Handling             |
+==========================+=====================+=============+==========+=================================+============================+
| ElectionAdministrationId | xs:IDREF            | Optional    | Single   |The **ElectionAdministrationId** |If the                      |
|                          |                     |             |          |links to the locality's          |**ElectionAdministrationId**|
|                          |                     |             |          |:doc:`election administration    |field is invalid the        |
|                          |                     |             |          |<election_administration>`       |implementation is required  |
|                          |                     |             |          |object.                          |to ignore it.               |
|                          |                     |             |          |                                 |                            |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| ExternalIdentifiers      | ExternalIdentifiers | Optional    | Single   |                                 |                            |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| Name                     | xs:string           | **Required**| Single   |The **Name** specifies the name  |If the **Name** field is not|
|                          |                     |             |          |of a locality.                   |present or invalid, the     |
|                          |                     |             |          |                                 |implementation is required  |
|                          |                     |             |          |                                 |to ignore the locality      |
|                          |                     |             |          |                                 |element containing it.      |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| PollingLocationId        | xs:IDREF            | Optional    | Repeats  |The **PollingLocationId**        |If the **PollingLocationId**|
|                          |                     |             |          |specifies a link to the          |field is missing or invalid,|
|                          |                     |             |          |locality's :doc:`polling         |the implementation is       |
|                          |                     |             |          |locations <polling_location>`. If|required to ignore          |
|                          |                     |             |          |early vote centers or ballot drop|it. However, the            |
|                          |                     |             |          |locations are locality-wide, they|implementation should still |
|                          |                     |             |          |should be specified here.        |check to see if there are   |
|                          |                     |             |          |                                 |any polling locations       |
|                          |                     |             |          |                                 |associated with this        |
|                          |                     |             |          |                                 |locality's state.           |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| StateId                  | xs:IDREF            | Optional    | Single   |The **StateId** links to the     |If the **StateId** field is |
|                          |                     |             |          |locality's :doc:`state <state>`. |invalid or not present, the |
|                          |                     |             |          |                                 |implementation is required  |
|                          |                     |             |          |                                 |to ignore the locality      |
|                          |                     |             |          |                                 |element containing.         |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| Type                     | DistrictType        | Optional    | Single   |The **Type** defines the kind of |If **Type** is invalid or   |
|                          |                     |             |          |locality (e.g. county, town, et  |not present, the            |
|                          |                     |             |          |al.), which is one of the various|implementation is required  |
|                          |                     |             |          |:doc:`DistrictType enumerations  |to ignore it.               |
|                          |                     |             |          |<../enumerations/district_type>`.|                            |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+
| OtherType                | xs:string           | Optional    | Single   |The **OtherType** element allows |If **OtherType** is invalid |
|                          |                     |             |          |for defining a type of locality  |or not present, the         |
|                          |                     |             |          |that falls outside the options   |implementation is required  |
|                          |                     |             |          |listed in :doc:`DistrictType     |to ignore it.               |
|                          |                     |             |          |<../enumerations/district_type>`.|                            |
+--------------------------+---------------------+-------------+----------+---------------------------------+----------------------------+

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
