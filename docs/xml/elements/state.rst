State
=====

The State object includes state-wide election information. The ID attribute is recommended to be the
state's FIPS code.

.. todo::

   Add description for ExternalIdentifiers
   
+-------------------------+-----------------------+--------------+------------+---------------------------------+------------------------------------+
| Tag                     | Data Type             | Required?    | Repeats?   |Description                      |Error Handling                      |
|                         |                       |              |            |                                 |                                    |
+=========================+=======================+==============+============+=================================+====================================+
| id                      | xs:ID                 | **Required** | Attribute  |A unique identifier for the      |If the id is invalid or not present,|
|                         |                       |              |            |element.                         |the implementation is required to   |
|                         |                       |              |            |                                 |ignore the State element.           |
|                         |                       |              |            |                                 |                                    |
+-------------------------+-----------------------+--------------+------------+---------------------------------+------------------------------------+
| ElectionAdministrationId| xs:IDREF              | Optional     | Single     |The **ElectionAdministrationId** |If the **ElectionAdministrationId** |
|                         |                       |              |            |links to the state's election    |field is invalid or not present, the|
|                         |                       |              |            |administration object.           |implementation is required to ignore|
|                         |                       |              |            |                                 |it.                                 |
+-------------------------+-----------------------+--------------+------------+---------------------------------+------------------------------------+
| ExternalIdentifiers     | ExternalIdentifiers   | Optional     | Single     |                                 |                                    |
+-------------------------+-----------------------+--------------+------------+---------------------------------+------------------------------------+
| Name                    | xs:string             | Optional     | Single     |The **Name** is the name of a    |If the **Name** field is not present|
|                         |                       |              |            |state, such as Alabama.          |or invalid, the implementation is   |
|                         |                       |              |            |                                 |required to ignore the state element|
|                         |                       |              |            |                                 |containing it.                      |
+-------------------------+-----------------------+--------------+------------+---------------------------------+------------------------------------+
| PollingLocationId       | xs:IDREF              | Optional     | Repeats    |The **PollingLocationId**        |If the **PollingLocationId** field  |
|                         |                       |              |            |specifies a link to the state's  |is missing or invalid, the          |
|                         |                       |              |            |polling locations. If early vote |implementation is required to ignore|
|                         |                       |              |            |centers or ballot drop locations |it.                                 |
|                         |                       |              |            |are state-wide (e.g., anyone in  |                                    |
|                         |                       |              |            |the state can use them), they can|                                    |
|                         |                       |              |            |be specified here, but are       |                                    |
|                         |                       |              |            |encouraged to only use the       |                                    |
|                         |                       |              |            |**Precinct** element.            |                                    |
+-------------------------+-----------------------+--------------+------------+---------------------------------+------------------------------------+

.. code-block:: xml
   :linenos:

   <State id="st51">
      <ElectionAdministrationId>ea40133</ElectionAdministrationId>
      <ExternalIdentifiers>
        <ExternalIdentifier>
	  <Type>ocd-id</Type>
	  <Value>ocd-division/country:us/state:va</Value>
	</ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Virginia</Name>
   </State>
