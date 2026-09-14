.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-locality:

Locality
========

The Locality object represents any jurisdictional level—including states, counties, cities, and towns. Localities form a tree hierarchy using ``ParentLocalityId``, with the root locality representing the state (with ``Type="state"``).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearDefaultPollingHours/>``, ``<ClearElectionAdministration/>``, ``<ClearIsInactive/>``). Name is optional in overlays. Emergency notices and overridden hours are only permitted in overlays.

+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================================+==============+==============+==========================================+==========================================+
| ElectionAdministration   | :ref:`multi-xml-election-administration` | Optional     | Single       | The election administration entity for   | If the element is invalid or not         |
|                          |                                          |              |              | this locality. In overlays, this entity  | present, then the implementation is      |
|                          |                                          |              |              | is replaced as a single unit or cleared  | required to ignore it.                   |
|                          |                                          |              |              | with <ClearElectionAdministration/>.     |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EmergencyNotice          | :ref:`multi-xml-emergency-notice`        | Optional     | Single       | Emergency notification applicable        | If the element is invalid or not         |
|                          |                                          |              |              | locality-wide. Permitted only in feed    | present, then the implementation is      |
|                          |                                          |              |              | overlays.                                | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier       | :ref:`multi-xml-external-identifier`     | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                          |              |              | locality to external datasets (e.g.      | present, then the implementation is      |
|                          |                                          |              |              | OCD-ID, FIPS). Clearable in overlays.    | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly               | ``xs:boolean``                           | Optional     | Single       | Specifies if the locality runs mail-only | If the field is missing or invalid, the  |
|                          |                                          |              |              | elections. If true, all precincts within | implementation is required to assume     |
|                          |                                          |              |              | this locality also run mail-only         | IsMailOnly is false.                     |
|                          |                                          |              |              | elections unless otherwise specified.    |                                          |
|                          |                                          |              |              | Ballot drop boxes may be used in         |                                          |
|                          |                                          |              |              | addition to mail ballots. Clearable in   |                                          |
|                          |                                          |              |              | overlays.                                |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                            | **Required** | Single       | Name of the locality. Required in main   | If the field is invalid, then the        |
|                          |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                          |                                          |              |              |                                          | ``Locality`` element containing it.      |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                            | Optional     | Single       | References locality-wide polling         | If the field is invalid or not present,  |
|                          |                                          |              |              | locations (e.g. central early vote sites | then the implementation is required to   |
|                          |                                          |              |              | or countywide drop boxes accessible to   | ignore it.                               |
|                          |                                          |              |              | any voter in the locality). Clearable in |                                          |
|                          |                                          |              |              | overlays.                                |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ParentLocalityId         | ``xs:IDREF``                             | Optional     | Single       | References the parent                    | If the field is invalid or not present,  |
|                          |                                          |              |              | :ref:`multi-xml-locality` in the         | then the implementation is required to   |
|                          |                                          |              |              | jurisdiction hierarchy (e.g. a county    | ignore it.                               |
|                          |                                          |              |              | referencing its parent state, or a town  |                                          |
|                          |                                          |              |              | referencing its parent county). If       |                                          |
|                          |                                          |              |              | omitted, this is a top-level             |                                          |
|                          |                                          |              |              | jurisdiction (e.g. the state).           |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-district-type`           | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                          |                                          |              |              | state, county, city, town, et al.),      | then the implementation is required to   |
|                          |                                          |              |              | which is one of the various              | ignore it.                               |
|                          |                                          |              |              | :ref:`DistrictType enumerations          |                                          |
|                          |                                          |              |              | <multi-xml-district-type>`. Clearable in |                                          |
|                          |                                          |              |              | overlays.                                |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                            | Optional     | Single       | Allows defining a type of locality       | If the field is invalid or not present,  |
|                          |                                          |              |              | outside :ref:`multi-xml-district-type`.  | then the implementation is required to   |
|                          |                                          |              |              | Clearable in overlays.                   | ignore it.                               |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DefaultPollingHours      | :ref:`multi-xml-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for day-of       | If the element is invalid or not         |
|                          |                                          |              |              | polling locations throughout this        | present, then the implementation is      |
|                          |                                          |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OverriddenPollingHours   | :ref:`multi-xml-schedule-with-timezone`  | Optional     | Repeats      | Overridden polling hours for day-of      | If the element is invalid or not         |
|                          |                                          |              |              | locations in this locality. Permitted    | present, then the implementation is      |
|                          |                                          |              |              | only in feed overlays.                   | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DefaultEarlyVoteHours    | :ref:`multi-xml-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for in-person    | If the element is invalid or not         |
|                          |                                          |              |              | early voting locations throughout this   | present, then the implementation is      |
|                          |                                          |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OverriddenEarlyVoteHours | :ref:`multi-xml-schedule-with-timezone`  | Optional     | Repeats      | Overridden early voting hours in this    | If the element is invalid or not         |
|                          |                                          |              |              | locality. Permitted only in feed         | present, then the implementation is      |
|                          |                                          |              |              | overlays.                                | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DefaultDropoffHours      | :ref:`multi-xml-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for ballot       | If the element is invalid or not         |
|                          |                                          |              |              | drop-off locations throughout this       | present, then the implementation is      |
|                          |                                          |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OverriddenDropoffHours   | :ref:`multi-xml-schedule-with-timezone`  | Optional     | Repeats      | Overridden drop-off hours in this        | If the element is invalid or not         |
|                          |                                          |              |              | locality. Permitted only in feed         | present, then the implementation is      |
|                          |                                          |              |              | overlays.                                | required to ignore it.                   |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive               | ``xs:string``                            | Optional     | Single       | If specified, marks the locality as      | If the field is invalid or not present,  |
|                          |                                          |              |              | inactive and explains the reason why     | then the implementation is required to   |
|                          |                                          |              |              | (e.g. "Jurisdiction not holding          | ignore it.                               |
|                          |                                          |              |              | elections on this date"). Clearable in   |                                          |
|                          |                                          |              |              | overlays.                                |                                          |
+--------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <!-- State-level locality (root) -->
   <Locality id="loc51">
      <Name>Virginia</Name>
      <Type>state</Type>
      <ElectionAdministration>
         <ElectionsUri>https://www.elections.virginia.gov/</ElectionsUri>
         <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      </ElectionAdministration>
   </Locality>

   <!-- County-level locality referencing parent state -->
   <Locality id="loc70001">
      <Name>ALBEMARLE COUNTY</Name>
      <ParentLocalityId>loc51</ParentLocalityId>
      <Type>county</Type>
      <IsMailOnly>false</IsMailOnly>
      <PollingLocationIds>pl00001 pl00002</PollingLocationIds>
      <DefaultPollingHours>
         <TimeZone>America/New_York</TimeZone>
         <Hours>
            <StartTime>06:00:00</StartTime>
            <EndTime>19:00:00</EndTime>
         </Hours>
      </DefaultPollingHours>
   </Locality>
