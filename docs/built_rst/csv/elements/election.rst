.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-election:

election
========

The Election object represents an election event. A feed must contain **exactly one** Election object in the main feed. In feed overlays, Election can appear to update election metadata.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearAbsenteeBallotInfo/>``). Fields that are required in the main feed (Date and TopLevelLocalityId) are optional in overlays.

+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                           | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============================+=========================================+==============+==============+==========================================+==========================================+
| absentee_ballot_info          | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Information about requesting absentee    | If the element is invalid or not         |
|                               |                                         |              |              | ballots.                                 | present, then the implementation is      |
|                               |                                         |              |              |                                          | required to ignore it.                   |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_request_deadline     | ``xs:date``                             | Optional     | Single       | Specifies the last day to request an     | If the field is invalid or not present,  |
|                               |                                         |              |              | absentee ballot (e.g. "2024-10-25").     | then the implementation is required to   |
|                               |                                         |              |              |                                          | ignore it.                               |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date                          | ``xs:date``                             | **Required** | Single       | Date of the election in local time.      | If the field is invalid, then the        |
|                               |                                         |              |              | Required in main feed; optional in       | implementation is required to ignore the |
|                               |                                         |              |              | overlays.                                | ``Election`` element containing it.      |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_type                 | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Specifies the type or highest            | If the element is invalid or not         |
|                               |                                         |              |              | controlling authority for the election   | present, then the implementation is      |
|                               |                                         |              |              | (e.g. federal, state, county, city,      | required to ignore it.                   |
|                               |                                         |              |              | town, or general, primary, special).     |                                          |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_election_day_registration | ``xs:boolean``                          | Optional     | Single       | Specifies if a voter can register on the | If the field is invalid or not present,  |
|                               |                                         |              |              | same day of the election (i.e., the last | then the implementation is required to   |
|                               |                                         |              |              | day of the election). Valid values are   | ignore it.                               |
|                               |                                         |              |              | "true" and "false".                      |                                          |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| schedule                      | :ref:`multi-csv-schedule-with-timezone` | Optional     | Repeats      | Schedule of voting dates and hours for   | If the element is invalid or not         |
|                               |                                         |              |              | the election.                            | present, then the implementation is      |
|                               |                                         |              |              |                                          | required to ignore it.                   |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_statewide                  | ``xs:boolean``                          | Optional     | Single       | Indicates whether the election is        | If the field is invalid or not present,  |
|                               |                                         |              |              | statewide.                               | then the implementation is required to   |
|                               |                                         |              |              |                                          | ignore it.                               |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                          | :ref:`multi-csv-internationalized-text` | Optional     | Single       | The name of the election.                | If the element is invalid or not         |
|                               |                                         |              |              |                                          | present, then the implementation is      |
|                               |                                         |              |              |                                          | required to ignore it.                   |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_deadline         | ``xs:date``                             | Optional     | Single       | Specifies the last day to register for   | If the field is invalid or not present,  |
|                               |                                         |              |              | the election with the possible exception | then the implementation is required to   |
|                               |                                         |              |              | of Election Day registration (e.g.       | ignore it.                               |
|                               |                                         |              |              | "2024-10-15").                           |                                          |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_info             | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Information about voter registration.    | If the element is invalid or not         |
|                               |                                         |              |              |                                          | present, then the implementation is      |
|                               |                                         |              |              |                                          | required to ignore it.                   |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| results_uri                   | :ref:`multi-csv-internationalized-uri`  | Optional     | Single       | Web address where election results may   | If the element is invalid or not         |
|                               |                                         |              |              | be found.                                | present, then the implementation is      |
|                               |                                         |              |              |                                          | required to ignore it.                   |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| top_level_locality_id         | ``xs:IDREF``                            | **Required** | Single       | Links to the top-level                   | If the field is invalid or not present,  |
|                               |                                         |              |              | :ref:`multi-csv-locality` for the        | the implementation is required to ignore |
|                               |                                         |              |              | election (e.g. the state locality).      | the Election containing it.              |
|                               |                                         |              |              | Required in main feed; optional in       |                                          |
|                               |                                         |              |              | overlays.                                |                                          |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,date,name,election_type,top_level_locality_id,is_statewide,registration_info,absentee_ballot_info,results_uri,has_election_day_registration,registration_deadline,absentee_request_deadline
    ele001,2024-11-05,2024 General Election,General,loc51,true,https://vote.va.gov/register,https://vote.va.gov/absentee,https://vote.va.gov/results,false,2024-10-15,2024-10-25
