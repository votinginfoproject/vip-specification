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
| absentee_request_deadline     | ``xs:date``                             | Optional     | Single       | Last day to request an absentee ballot.  | If the field is invalid or not present,  |
|                               |                                         |              |              |                                          | then the implementation is required to   |
|                               |                                         |              |              |                                          | ignore it.                               |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| date                          | ``xs:date``                             | **Required** | Single       | Date of the election in local time.      | If the field is invalid, then the        |
|                               |                                         |              |              | Required in main feed; optional in       | implementation is required to ignore the |
|                               |                                         |              |              | overlays.                                | ``Election`` element containing it.      |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_type                 | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Type of election (e.g. General, Primary, | If the element is invalid or not         |
|                               |                                         |              |              | Special).                                | present, then the implementation is      |
|                               |                                         |              |              |                                          | required to ignore it.                   |
+-------------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_election_day_registration | ``xs:boolean``                          | Optional     | Single       | Specifies whether voters can register on | If the field is invalid or not present,  |
|                               |                                         |              |              | election day.                            | then the implementation is required to   |
|                               |                                         |              |              |                                          | ignore it.                               |
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
| registration_deadline         | ``xs:date``                             | Optional     | Single       | Last day to register to vote for the     | If the field is invalid or not present,  |
|                               |                                         |              |              | election.                                | then the implementation is required to   |
|                               |                                         |              |              |                                          | ignore it.                               |
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
