.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-locality:

locality
========

The Locality object represents any jurisdictional level—including states, counties, cities, and towns. Localities form a tree hierarchy using ``ParentLocalityId``, with the root locality representing the state (with ``Type="state"``).

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearDefaultPollingHours/>``, ``<ClearElectionAdministration/>``, ``<ClearIsInactive/>``). Name is optional in overlays. Emergency notices and overridden hours are only permitted in overlays.

+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                                | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+==========================================+==============+==============+==========================================+==========================================+
| election_administration     | :ref:`multi-csv-election-administration` | Optional     | Single       | The election administration entity for   | If the element is invalid or not         |
|                             |                                          |              |              | this locality. In overlays, this entity  | present, then the implementation is      |
|                             |                                          |              |              | is replaced as a single unit or cleared  | required to ignore it.                   |
|                             |                                          |              |              | with <ClearElectionAdministration/>.     |                                          |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier         | :ref:`multi-csv-external-identifier`     | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                             |                                          |              |              | locality to external datasets (e.g.      | present, then the implementation is      |
|                             |                                          |              |              | OCD-ID, FIPS). Clearable in overlays.    | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only                | ``xs:boolean``                           | Optional     | Single       | Specifies if the locality runs mail-only | If the field is missing or invalid, the  |
|                             |                                          |              |              | elections. If true, all precincts within | implementation is required to assume     |
|                             |                                          |              |              | this locality also run mail-only         | IsMailOnly is false.                     |
|                             |                                          |              |              | elections unless otherwise specified.    |                                          |
|                             |                                          |              |              | Ballot drop boxes may be used in         |                                          |
|                             |                                          |              |              | addition to mail ballots. Clearable in   |                                          |
|                             |                                          |              |              | overlays.                                |                                          |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                        | ``xs:string``                            | **Required** | Single       | Name of the locality. Required in main   | If the field is invalid, then the        |
|                             |                                          |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                             |                                          |              |              |                                          | ``Locality`` element containing it.      |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids        | ``xs:IDREFS``                            | Optional     | Single       | References locality-wide polling         | If the field is invalid or not present,  |
|                             |                                          |              |              | locations (e.g. central early vote sites | then the implementation is required to   |
|                             |                                          |              |              | or countywide drop boxes accessible to   | ignore it.                               |
|                             |                                          |              |              | any voter in the locality). Clearable in |                                          |
|                             |                                          |              |              | overlays.                                |                                          |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| parent_locality_id          | ``xs:IDREF``                             | Optional     | Single       | References the parent                    | If the field is invalid or not present,  |
|                             |                                          |              |              | :ref:`multi-csv-locality` in the         | then the implementation is required to   |
|                             |                                          |              |              | jurisdiction hierarchy (e.g. a county    | ignore it.                               |
|                             |                                          |              |              | referencing its parent state, or a town  |                                          |
|                             |                                          |              |              | referencing its parent county). If       |                                          |
|                             |                                          |              |              | omitted, this is a top-level             |                                          |
|                             |                                          |              |              | jurisdiction (e.g. the state).           |                                          |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                        | :ref:`multi-csv-district-type`           | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                             |                                          |              |              | state, county, city, town, et al.),      | then the implementation is required to   |
|                             |                                          |              |              | which is one of the various              | ignore it.                               |
|                             |                                          |              |              | :ref:`DistrictType enumerations          |                                          |
|                             |                                          |              |              | <multi-csv-district-type>`. Clearable in |                                          |
|                             |                                          |              |              | overlays.                                |                                          |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                  | ``xs:string``                            | Optional     | Single       | Allows defining a type of locality       | If the field is invalid or not present,  |
|                             |                                          |              |              | outside :ref:`multi-csv-district-type`.  | then the implementation is required to   |
|                             |                                          |              |              | Clearable in overlays.                   | ignore it.                               |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| default_polling_hours       | :ref:`multi-csv-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for day-of       | If the element is invalid or not         |
|                             |                                          |              |              | polling locations throughout this        | present, then the implementation is      |
|                             |                                          |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| default_early_vote_hours    | :ref:`multi-csv-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for in-person    | If the element is invalid or not         |
|                             |                                          |              |              | early voting locations throughout this   | present, then the implementation is      |
|                             |                                          |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| default_dropoff_hours       | :ref:`multi-csv-schedule-with-timezone`  | Optional     | Repeats      | Default operating hours for ballot       | If the element is invalid or not         |
|                             |                                          |              |              | drop-off locations throughout this       | present, then the implementation is      |
|                             |                                          |              |              | locality. Clearable in overlays.         | required to ignore it.                   |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive                 | ``xs:string``                            | Optional     | Single       | If specified, marks the locality as      | If the field is invalid or not present,  |
|                             |                                          |              |              | inactive and explains the reason why     | then the implementation is required to   |
|                             |                                          |              |              | (e.g. "Jurisdiction not holding          | ignore it.                               |
|                             |                                          |              |              | elections on this date"). Clearable in   |                                          |
|                             |                                          |              |              | overlays.                                |                                          |
+-----------------------------+------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,name,parent_locality_id,type,other_type,is_mail_only,polling_location_ids
    loc51,Virginia,,state,,false,
    loc70001,Albemarle County,loc51,county,,false,pl001 pl002
