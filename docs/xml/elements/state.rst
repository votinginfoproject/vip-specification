State
=====

The State object includes state-wide election information. The ID attribute is recommended to be the
state's FIPS code.

+-------------------------+-------------------------+-----------+----------+---------------------------------+------------------------------------+
| Tag                     | Data Type               | Required? | Repeats? |Description                      |Error Handling                      |
|                         |                         |           |          |                                 |                                    |
+=========================+=========================+===========+==========+=================================+====================================+
| ElectionAdministrationId| xs:IDREF                | Optional  | Single   |Links to the state's election    |If the field is invalid or not      |
|                         |                         |           |          |administration object.           |present, the implementation is      |
|                         |                         |           |          |                                 |required to ignore it.              |
|                         |                         |           |          |                                 |                                    |
+-------------------------+-------------------------+-----------+----------+---------------------------------+------------------------------------+
| ExternalIdentifiers     |:doc:`ExternalIdentifiers| Optional  | Single   |Other identifier for the state   |If the field is invalid or not      |
|                         |<external_identifiers>`  |           |          |that relates to another dataset  |present, the implementation is      |
|                         |                         |           |          |(e.g. `OCD-ID`_).                |required to ignore it.              |
+-------------------------+-------------------------+-----------+----------+---------------------------------+------------------------------------+
| Name                    | xs:string               | Optional  | Single   |Specifiers the name of a state,  |If the field is not present or      |
|                         |                         |           |          |such as Alabama.                 |invalid, the implementation is      |
|                         |                         |           |          |                                 |required to ignore the element      |
|                         |                         |           |          |                                 |containing it.                      |
+-------------------------+-------------------------+-----------+----------+---------------------------------+------------------------------------+
| PollingLocationId       | xs:IDREF                | Optional  | Repeats  |Specifies a link to the state's  |If the field is missing or invalid, |
|                         |                         |           |          |:doc:`polling locations          |the implementation is required to   |
|                         |                         |           |          |<polling_location>`. If early    |ignore it.                          |
|                         |                         |           |          |vote centers or ballot drop      |                                    |
|                         |                         |           |          |locations are state-wide (e.g.,  |                                    |
|                         |                         |           |          |anyone in the state can use      |                                    |
|                         |                         |           |          |them), they can be specified     |                                    |
|                         |                         |           |          |here, but are encouraged to only |                                    |
|                         |                         |           |          |use the :doc:`Precinct           |                                    |
|                         |                         |           |          |<precinct>` element.             |                                    |
+-------------------------+-------------------------+-----------+----------+---------------------------------+------------------------------------+

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
