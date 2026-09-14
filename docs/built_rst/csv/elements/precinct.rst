.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-precinct:

precinct
========

The Precinct object represents a voting precinct or precinct split within a Locality.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearBallotStyleId/>``, ``<ClearPollingLocationIds/>``, ``<ClearIsInactive/>``). LocalityId and Name are optional in overlays. EmergencyNotice is permitted only in overlays.

+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                    | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+========================+======================================+==============+==============+==========================================+==========================================+
| ballot_style_id        | ``xs:IDREF``                         | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                        |                                      |              |              | :ref:`multi-csv-ballot-style` voted by   | then the implementation is required to   |
|                        |                                      |              |              | electors in this precinct. Clearable in  | ignore it.                               |
|                        |                                      |              |              | overlays.                                |                                          |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_ids | ``xs:IDREFS``                        | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                        |                                      |              |              | :ref:`multi-csv-electoral-district`s     | then the implementation is required to   |
|                        |                                      |              |              | (e.g., congressional district, state     | ignore it.                               |
|                        |                                      |              |              | house district, school board district)   |                                          |
|                        |                                      |              |              | to which the entire precinct/precinct    |                                          |
|                        |                                      |              |              | split belongs. Highly Recommended if     |                                          |
|                        |                                      |              |              | candidate information is to be provided. |                                          |
|                        |                                      |              |              | Clearable in overlays.                   |                                          |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier    | :ref:`multi-csv-external-identifier` | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                        |                                      |              |              | precinct to other datasets (e.g.         | present, then the implementation is      |
|                        |                                      |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_mail_only           | ``xs:boolean``                       | Optional     | Single       | Specifies if this precinct conducts      | If the field is missing or invalid, the  |
|                        |                                      |              |              | mail-only elections. Clearable in        | implementation is required to assume     |
|                        |                                      |              |              | overlays.                                | IsMailOnly is false.                     |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| locality_id            | ``xs:IDREF``                         | **Required** | Single       | References the containing                | If LocalityId is invalid or not present, |
|                        |                                      |              |              | :ref:`multi-csv-locality`. Required in   | the implementation is required to ignore |
|                        |                                      |              |              | main feed; optional in overlays.         | the Precinct containing it.              |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                   | ``xs:string``                        | **Required** | Single       | Name of the precinct. Required in main   | If Name is invalid or not present, the   |
|                        |                                      |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                        |                                      |              |              |                                          | Precinct containing it.                  |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number                 | ``xs:string``                        | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                        |                                      |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                        |                                      |              |              | legal). Should be used if the Name field | ignore it.                               |
|                        |                                      |              |              | is populated by a name and not a number. |                                          |
|                        |                                      |              |              | Clearable in overlays.                   |                                          |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids   | ``xs:IDREFS``                        | Optional     | Single       | Links to polling locations serving this  | If the field is invalid or not present,  |
|                        |                                      |              |              | precinct. Clearable in overlays.         | then the implementation is required to   |
|                        |                                      |              |              |                                          | ignore it.                               |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| precinct_split_name    | ``xs:string``                        | Optional     | Single       | If this field is empty, then this        | If the field is invalid or not present,  |
|                        |                                      |              |              | Precinct object represents a full        | then the implementation is required to   |
|                        |                                      |              |              | precinct. If this field is present, then | ignore it.                               |
|                        |                                      |              |              | this Precinct object represents one      |                                          |
|                        |                                      |              |              | portion of a split precinct. Each        |                                          |
|                        |                                      |              |              | Precinct object that represents one      |                                          |
|                        |                                      |              |              | portion of a split precinct must have    |                                          |
|                        |                                      |              |              | the same Name value, but different       |                                          |
|                        |                                      |              |              | PrecinctSplitName values (e.g. "Split    |                                          |
|                        |                                      |              |              | A", "Split B"). See the sample_feed.xml  |                                          |
|                        |                                      |              |              | file for examples. Clearable in          |                                          |
|                        |                                      |              |              | overlays.                                |                                          |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| spatial_boundary       | :ref:`multi-csv-spatial-boundary`    | Optional     | Single       | Defines the spatial boundary of the      | If the element is invalid or not         |
|                        |                                      |              |              | precinct. All voter addresses contained  | present, then the implementation is      |
|                        |                                      |              |              | within this boundary are assigned to the | required to ignore it.                   |
|                        |                                      |              |              | precinct. If a voter address also maps   |                                          |
|                        |                                      |              |              | to a :doc:`StreetSegment                 |                                          |
|                        |                                      |              |              | <street_segment>`, then the precinct     |                                          |
|                        |                                      |              |              | assignment from the StreetSegment will   |                                          |
|                        |                                      |              |              | be preferred over the assignment defined |                                          |
|                        |                                      |              |              | by the spatial boundary. Clearable in    |                                          |
|                        |                                      |              |              | overlays.                                |                                          |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ward                   | ``xs:string``                        | Optional     | Single       | Ward identifier if applicable. Clearable | If the field is invalid or not present,  |
|                        |                                      |              |              | in overlays.                             | then the implementation is required to   |
|                        |                                      |              |              |                                          | ignore it.                               |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_inactive            | ``xs:string``                        | Optional     | Single       | If specified, marks the precinct as      | If the field is invalid or not present,  |
|                        |                                      |              |              | inactive, stating the reason why.        | then the implementation is required to   |
|                        |                                      |              |              | Clearable in overlays.                   | ignore it.                               |
+------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,ballot_style_id,electoral_district_ids,is_mail_only,locality_id,name,number,polling_location_ids,precinct_split_name,ward
    pre90111,bs00010,ed001 ed002,false,loc70001,203 - GEORGETOWN,0203,pl00001,split13,5
