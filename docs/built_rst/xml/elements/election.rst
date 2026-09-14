.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election:

Election
========

The Election object represents an election event. A feed must contain **exactly one** Election object in the main feed. In feed overlays, Election can appear to update election metadata.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearSchedule/>``, ``<ClearAbsenteeBallotInfo/>``). Fields that are required in the main feed (Date and TopLevelLocalityId) are optional in overlays.

+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=========================================+==============+==============+==========================================+==========================================+
| AbsenteeBallotInfo         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Information about requesting absentee    | If the element is invalid or not         |
|                            |                                         |              |              | ballots.                                 | present, then the implementation is      |
|                            |                                         |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeRequestDeadline    | ``xs:date``                             | Optional     | Single       | Specifies the last day to request an     | If the field is invalid or not present,  |
|                            |                                         |              |              | absentee ballot (e.g. "2024-10-25").     | then the implementation is required to   |
|                            |                                         |              |              |                                          | ignore it.                               |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Date                       | ``xs:date``                             | **Required** | Single       | Date of the election in local time.      | If the field is invalid, then the        |
|                            |                                         |              |              | Required in main feed; optional in       | implementation is required to ignore the |
|                            |                                         |              |              | overlays.                                | ``Election`` element containing it.      |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionType               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the type or highest            | If the element is invalid or not         |
|                            |                                         |              |              | controlling authority for the election   | present, then the implementation is      |
|                            |                                         |              |              | (e.g. federal, state, county, city,      | required to ignore it.                   |
|                            |                                         |              |              | town, or general, primary, special).     |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasElectionDayRegistration | ``xs:boolean``                          | Optional     | Single       | Specifies if a voter can register on the | If the field is invalid or not present,  |
|                            |                                         |              |              | same day of the election (i.e., the last | then the implementation is required to   |
|                            |                                         |              |              | day of the election). Valid values are   | ignore it.                               |
|                            |                                         |              |              | "true" and "false".                      |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Schedule                   | :ref:`multi-xml-schedule-with-timezone` | Optional     | Repeats      | Schedule of voting dates and hours for   | If the element is invalid or not         |
|                            |                                         |              |              | the election.                            | present, then the implementation is      |
|                            |                                         |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsStatewide                | ``xs:boolean``                          | Optional     | Single       | Indicates whether the election is        | If the field is invalid or not present,  |
|                            |                                         |              |              | statewide.                               | then the implementation is required to   |
|                            |                                         |              |              |                                          | ignore it.                               |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | The name of the election.                | If the element is invalid or not         |
|                            |                                         |              |              |                                          | present, then the implementation is      |
|                            |                                         |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationDeadline       | ``xs:date``                             | Optional     | Single       | Specifies the last day to register for   | If the field is invalid or not present,  |
|                            |                                         |              |              | the election with the possible exception | then the implementation is required to   |
|                            |                                         |              |              | of Election Day registration (e.g.       | ignore it.                               |
|                            |                                         |              |              | "2024-10-15").                           |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationInfo           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Information about voter registration.    | If the element is invalid or not         |
|                            |                                         |              |              |                                          | present, then the implementation is      |
|                            |                                         |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ResultsUri                 | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Web address where election results may   | If the element is invalid or not         |
|                            |                                         |              |              | be found.                                | present, then the implementation is      |
|                            |                                         |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TopLevelLocalityId         | ``xs:IDREF``                            | **Required** | Single       | Links to the top-level                   | If the field is invalid or not present,  |
|                            |                                         |              |              | :ref:`multi-xml-locality` for the        | the implementation is required to ignore |
|                            |                                         |              |              | election (e.g. the state locality).      | the Election containing it.              |
|                            |                                         |              |              | Required in main feed; optional in       |                                          |
|                            |                                         |              |              | overlays.                                |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Election id="ele30000">
      <Date>2024-11-05</Date>
      <Name>
         <Text language="en">2024 General Election</Text>
         <Text language="es">Elecciones Generales de 2024</Text>
      </Name>
      <ElectionType>General</ElectionType>
      <HasElectionDayRegistration>false</HasElectionDayRegistration>
      <IsStatewide>true</IsStatewide>
      <RegistrationDeadline>2024-10-15</RegistrationDeadline>
      <AbsenteeRequestDeadline>2024-10-25</AbsenteeRequestDeadline>
      <ResultsUri>https://www.sbe.virginia.gov/ElectionResults.html</ResultsUri>
      <TopLevelLocalityId>loc51</TopLevelLocalityId>
   </Election>
