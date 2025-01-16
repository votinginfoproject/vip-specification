.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election:

Election
========

The Election object represents an Election Day, which usually consists of many individual contests
and/or referenda. A feed must contain **exactly one** Election object. All relationships in the
feed (e.g., street segment to precinct to polling location) are assumed to relate only to
the Election specified by this object. It is permissible, and recommended, to combine unrelated
contests (e.g., a special election and a general election) that occur on the same day into one feed
with one Election object.

+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=========================================+==============+==============+==========================================+==========================================+
| Date                       | ``xs:date``                             | **Required** | Single       | Specifies when the election is being     |                                          |
|                            |                                         |              |              | held. The `Date` is considered to be in  |                                          |
|                            |                                         |              |              | the timezone local to the state holding  |                                          |
|                            |                                         |              |              | the election.                            |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionType               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the highest controlling        |                                          |
|                            |                                         |              |              | authority for election (e.g., federal,   |                                          |
|                            |                                         |              |              | state, county, city, town, etc.)         |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                    | ``xs:IDREF``                            | **Required** | Single       | Specifies a link to the `State` element  |                                          |
|                            |                                         |              |              | where the election is being held.        |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsStatewide                | ``xs:boolean``                          | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                            |                                         |              |              | statewide.                               | the implementation is required to        |
|                            |                                         |              |              |                                          | default to "yes".                        |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | The name for the election (**NB:** while |                                          |
|                            |                                         |              |              | optional, this element is highly         |                                          |
|                            |                                         |              |              | recommended).                            |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationInfo           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies information about registration |                                          |
|                            |                                         |              |              | for this election either as text or a    |                                          |
|                            |                                         |              |              | URI.                                     |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeBallotInfo         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies information about requesting   |                                          |
|                            |                                         |              |              | absentee ballots either as text or a URI |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ResultsUri                 | ``xs:anyURI``                           | Optional     | Single       | Contains a URI where results for the     |                                          |
|                            |                                         |              |              | election may be found                    |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingHours               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  |                                          |
| **[deprecated]**           |                                         |              |              | Election Day polling locations are open. |                                          |
|                            |                                         |              |              | If polling hours differ in specific      |                                          |
|                            |                                         |              |              | polling locations, alternative hours may |                                          |
|                            |                                         |              |              | be specified in the                      |                                          |
|                            |                                         |              |              | :ref:`multi-xml-polling-location` object |                                          |
|                            |                                         |              |              | *(NB: this element is deprecated in      |                                          |
|                            |                                         |              |              | favor of the more structured             |                                          |
|                            |                                         |              |              | :ref:`multi-xml-hours-open` element. It  |                                          |
|                            |                                         |              |              | is strongly encouraged that data         |                                          |
|                            |                                         |              |              | providers move toward contributing hours |                                          |
|                            |                                         |              |              | in this format)*.                        |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId                | ``xs:IDREF``                            | Optional     | Single       | References the                           |                                          |
|                            |                                         |              |              | :ref:`multi-xml-hours-open` element,     |                                          |
|                            |                                         |              |              | which lists the hours of operation for   |                                          |
|                            |                                         |              |              | polling locations.                       |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasElectionDayRegistration | ``xs:boolean``                          | Optional     | Single       | Specifies if a voter can register on the |                                          |
|                            |                                         |              |              | same day of the election (i.e., the last |                                          |
|                            |                                         |              |              | day of the election). Valid items are    |                                          |
|                            |                                         |              |              | "yes" and "no".                          |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationDeadline       | ``xs:date``                             | Optional     | Single       | Specifies the last day to register for   |                                          |
|                            |                                         |              |              | the election with the possible exception |                                          |
|                            |                                         |              |              | of Election Day registration.            |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeRequestDeadline    | ``xs:date``                             | Optional     | Single       | Specifies the last day to request an     |                                          |
|                            |                                         |              |              | absentee ballot.                         |                                          |
+----------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Election id="ele30000">
     <AbsenteeRequestDeadline>2013-10-30</AbsenteeRequestDeadline>
     <Date>2013-11-05</Date>
     <ElectionType>
       <Text language="en">General</Text>
       <Text language="es">Generales</Text>
     </ElectionType>
     <HasElectionDayRegistration>false</HasElectionDayRegistration>
     <HoursOpenId>hours0001</HoursOpenId>
     <IsStatewide>true</IsStatewide>
     <Name>
       <Text language="en">2013 Statewide General</Text>
     </Name>
     <RegistrationDeadline>2013-10-15</RegistrationDeadline>
     <ResultsUri>http://www.sbe.virginia.gov/ElectionResults.html</ResultsUri>
     <StateId>st51</StateId>
   </Election>
