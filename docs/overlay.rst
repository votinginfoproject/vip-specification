.. _overlay-docs:

Feed Overlays Specification (VIP 7.0)
=====================================

.. contents::
   :local:
   :depth: 2


Overview
--------

Introduced in VIP 7.0, **Feed Overlays** provide a lightweight, targeted mechanism to update, augment, or clear information in a previously published base VIP feed. Rather than requiring election administrators to re-export, validate, and republish an entire multi-megabyte monolithic VIP feed for time-sensitive modifications (such as polling place closures, emergency relocations, extended voting hours, or last-minute candidate withdrawals), a feed overlay allows publishers to distribute concise XML delta updates that consumers apply directly against an existing base feed.

.. important::
   **XML-Only Support:** Feed Overlays are supported exclusively in XML format according to the ``vip_overlay.xsd`` schema. The CSV specification applies only to the base VIP feed; CSV format is **not** supported for overlays.


Root Element & Schema Version
-----------------------------

A feed overlay document must have a root element of ``<VipOverlay>`` with the ``schemaVersion`` attribute set to ``7.0``:

.. code-block:: xml
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <VipOverlay xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.io/schemas/vip_overlay.xsd"
               schemaVersion="7.0">
      <!-- Overlay elements go here -->
   </VipOverlay>


Application Semantics
---------------------

When a consumer processes a feed overlay, it applies the updates to the in-memory or persisted representation of the base feed using the following semantics:

1. **Targeting by ID:**
   Overlay elements reference the entity to modify in the base feed using the required ``id`` attribute. For example, ``<PollingLocation id="pl1001">`` targets the existing polling location in the base feed with ID ``pl1001``.

2. **Field Replacement (Upsert):**
   Any child elements explicitly provided inside an overlay entity replace the corresponding values in the base entity. If a field in the base entity was omitted or previously empty, the value from the overlay is added.

3. **Field Preservation:**
   Any fields not mentioned in the overlay entity retain their current values from the base feed. For instance, if an overlay updates only the ``Schedule`` of a ``PollingLocation``, the location's address, name, and coordinates remain unchanged.

4. **Clearing Values (``<Clear{FieldName}/>``):**
   In the base specification (``vip_spec.xsd``), fields designated with ``clearable="true"`` generate corresponding empty elements in the overlay schema of type ``ClearableField`` named ``<Clear{FieldName}/>``. When a consumer encounters a clear element, it removes that field's value from the targeted entity.
   
   Examples of clearable tags include:
   
   * ``<ClearSchedule/>`` (on PollingLocation, Election)
   * ``<ClearDirections/>`` (on PollingLocation)
   * ``<ClearPhotoUri/>`` (on PollingLocation, Person)
   * ``<ClearPollingLocationIds/>`` (on Locality, Precinct)
   * ``<ClearDefaultPollingHours/>``, ``<ClearDefaultEarlyVoteHours/>``, ``<ClearDefaultDropoffHours/>`` (on Locality)
   * ``<ClearElectionAdministration/>`` (on Locality)
   * ``<ClearIsInactive/>`` (on Locality, PollingLocation, Precinct)
   * ``<ClearIsMailOnly/>`` (on Locality, Precinct)

5. **Entity Deactivation (``<IsInactive>``):**
   The elements :ref:`multi-xml-locality`, :ref:`multi-xml-polling-location`, and :ref:`multi-xml-precinct` include an ``<IsInactive>`` element (of type ``xs:string``). In an overlay, setting ``<IsInactive>`` marks the entity as inactive or closed, with the text describing the reason for closure (e.g. ``<IsInactive>Closed due to severe flooding; relocated to High School</IsInactive>``). If an inactive status needs to be rescinded, the overlay can specify ``<ClearIsInactive/>``.

6. **Adding New Polling Places (``isNew="true"``):**
   Overlays are primarily designed to update existing entities, but unforeseen circumstances may require designating an entirely new voting site or drop box on short notice.
   
   The :ref:`multi-xml-polling-location` element in ``vip_overlay.xsd`` includes an optional XML attribute:
   
   * ``isNew`` (boolean, default ``false``)
   
   When ``isNew="true"``, consumers treat the element as a newly introduced polling location rather than an update to an existing record. When creating a new polling place, publishers must include all fields required for a valid location (such as ``AddressStructured`` and ``LocationType``). Newly introduced polling locations can then be referenced by ID in updated ``PollingLocationIds`` lists on precincts or localities.


Overlay-Only Features
---------------------

The VIP 7.0 specification defines certain elements with ``onlyInOverlay="true"``. These elements are valid **only** in feed overlays and are omitted from base feeds:

Emergency Notices
~~~~~~~~~~~~~~~~~

The :ref:`multi-xml-emergency-notice` element communicates urgent alerts, emergency orders, or disruption notices directly to voters:

* **On Localities:** A single ``<EmergencyNotice>`` may be attached to a :ref:`multi-xml-locality` to issue a jurisdiction-wide alert (e.g. countywide polling hours extension by judicial decree).
* **On Polling Locations:** Multiple repeating ``<EmergencyNotice>`` elements may be attached to a :ref:`multi-xml-polling-location` to notify voters of venue-specific conditions (e.g. power outages, parking changes, shuttle service).
* **On Precincts:** Multiple repeating ``<EmergencyNotice>`` elements may be attached to a :ref:`multi-xml-precinct`.

An ``<EmergencyNotice>`` includes:

* ``NoticeText``: Localized alert text (type :ref:`multi-xml-internationalized-text`, repeating with ``language`` attributes).
* ``NoticeUri``: Optional link to official emergency documentation or press releases.
* ``AppliesTo``: Scope of the emergency notice (e.g. ``polling_place``, ``vote_center``, ``ballot_drop_box``, ``jurisdiction``).

Locality Hour Overrides
~~~~~~~~~~~~~~~~~~~~~~~

In an overlay, a :ref:`multi-xml-locality` may declare hours that explicitly override the base defaults across all child voting locations within that jurisdiction:

* ``<OverriddenPollingHours>``: Overrides default day-of polling hours.
* ``<OverriddenEarlyVoteHours>``: Overrides default early voting hours.
* ``<OverriddenDropoffHours>``: Overrides default ballot drop-off hours.


Excluded Elements in Overlays
-----------------------------

To keep overlay processing predictable and lightweight, the following entities from the base specification are **excluded** from feed overlays:

* **Source:** A feed overlay does not define a new :ref:`multi-xml-source` object; the overlay is bound to the existing base feed.
* **StreetSegment:** Street segment address mappings remain in the base feed and cannot be modified via overlays.
* **ExternalFile:** External bulk geospatial boundary files are not distributed via overlays.


Examples
--------

Example 1: Polling Location Emergency Relocation & Notice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, polling location ``pl204`` experienced an emergency water main break and was moved to an alternate location. The overlay updates its address, adds an emergency notice with multilingual text, and updates its schedule:

.. code-block:: xml
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <VipOverlay xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.io/schemas/vip_overlay.xsd"
               schemaVersion="7.0">

      <PollingLocation id="pl204">
         <AddressStructured>
            <LocationName>Lincoln Middle School Gymnasium</LocationName>
            <AddressLine>456 Oak Street</AddressLine>
            <City>Springfield</City>
            <Region>IL</Region>
            <PostalCode>62701</PostalCode>
         </AddressStructured>

         <EmergencyNotice>
            <NoticeText>
               <Text language="en">Polling site relocated from Community Center to Middle School Gym due to water main break.</Text>
               <Text language="es">El centro de votación se trasladó del Centro Comunitario al gimnasio de la escuela intermedia por rotura de tubería.</Text>
            </NoticeText>
            <NoticeUri>https://elections.springfield.gov/notices/precinct-12-relocation</NoticeUri>
            <AppliesTo>polling_place</AppliesTo>
         </EmergencyNotice>

         <Directions>
            <Text language="en">Enter through side gymnasium doors off 5th Avenue.</Text>
         </Directions>
      </PollingLocation>

   </VipOverlay>

Example 2: Adding a New Emergency Drop Box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new emergency ballot drop box ``pl9001`` is deployed to handle high voter turnout. It uses ``isNew="true"`` and is immediately associated with locality ``loc7001``:

.. code-block:: xml
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <VipOverlay xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.io/schemas/vip_overlay.xsd"
               schemaVersion="7.0">

      <!-- Declare new drop box location -->
      <PollingLocation id="pl9001" isNew="true">
         <AddressStructured>
            <LocationName>City Hall North Plaza Drop Box</LocationName>
            <AddressLine>100 Civic Center Drive</AddressLine>
            <City>Springfield</City>
            <Region>IL</Region>
            <PostalCode>62701</PostalCode>
         </AddressStructured>
         <LocationType>drop-box</LocationType>
         <Schedule>
            <TimeZone>America/Chicago</TimeZone>
            <Hours>
               <StartTime>06:00:00</StartTime>
               <EndTime>20:00:00</EndTime>
            </Hours>
            <StartDate>2024-10-25</StartDate>
            <EndDate>2024-11-05</EndDate>
            <IsOpen24Hours>true</IsOpen24Hours>
         </Schedule>
      </PollingLocation>

      <!-- Add new drop box ID to existing locality polling locations list -->
      <Locality id="loc7001">
         <PollingLocationIds>pl201 pl202 pl203 pl204 pl9001</PollingLocationIds>
      </Locality>

   </VipOverlay>

Example 3: Deactivating a Polling Location and Clearing Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Polling location ``pl305`` is closed due to severe weather. The overlay sets ``IsInactive`` with the explanation, clears outdated driving directions using ``<ClearDirections/>``, and removes a photo with ``<ClearPhotoUri/>``:

.. code-block:: xml
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <VipOverlay xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.io/schemas/vip_overlay.xsd"
               schemaVersion="7.0">

      <PollingLocation id="pl305">
         <IsInactive>Facility closed due to localized power outage. Voters directed to County Courthouse (pl101).</IsInactive>
         <ClearDirections/>
         <ClearPhotoUri/>
      </PollingLocation>

   </VipOverlay>

Example 4: Countywide Court-Ordered Hours Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following a court ruling on election day, voting hours across all polling places in county ``loc7002`` are extended by two hours until 9:00 PM. The locality issues an ``EmergencyNotice`` and specifies ``<OverriddenPollingHours>``:

.. code-block:: xml
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <VipOverlay xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.io/schemas/vip_overlay.xsd"
               schemaVersion="7.0">

      <Locality id="loc7002">
         <EmergencyNotice>
            <NoticeText>
               <Text language="en">Pursuant to Superior Court Order #24-EV-982, all polling places in the county will remain open until 9:00 PM.</Text>
            </NoticeText>
            <NoticeUri>https://elections.county.gov/orders/hours-extension.pdf</NoticeUri>
            <AppliesTo>polling_place</AppliesTo>
         </EmergencyNotice>

         <OverriddenPollingHours>
            <TimeZone>America/Chicago</TimeZone>
            <Hours>
               <StartTime>06:00:00</StartTime>
               <EndTime>21:00:00</EndTime>
            </Hours>
            <StartDate>2024-11-05</StartDate>
            <EndDate>2024-11-05</EndDate>
         </OverriddenPollingHours>
      </Locality>

   </VipOverlay>
