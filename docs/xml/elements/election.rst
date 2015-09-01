Election
========

The Election object represents an Election Day, which usually consists of many individual contests
and/or referenda. A feed must contain **exactly one** Election object. All relationships in the
feed (e.g., street segment to precinct to polling location) are assumed to relate only to
the Election specified by this object. It is permissible, and recommended, to combine unrelated
contests (e.g., a special election and a general election) that occur on the same day into one feed
with one Election object.

+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| Tag                       |Data Type                    |  Required?  |Repeats? | Description                           | Error handling                  |
|                           |                             |             |         |                                       |                                 |
+===========================+=============================+=============+=========+=======================================+=================================+
| Date                      |xs:date                      |**Required** |Single   |Specifies when the election is being   |If the field is not present or   |
|                           |                             |             |         |held. The Date is considered to be in  |invalid, the implementation is   |
|                           |                             |             |         |the timezone local to the state holding|required to ignore the election  |
|                           |                             |             |         |the election.                          |element containing it.           |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| ElectionType              |:doc:`InternationalizedText  |Optional     |Single   |Specifies the highest controlling      |If the element is invalid or not |
|                           |<internationalized_text>`    |             |         |authority for election (e.g., federal, |present, the implementation is   |
|                           |                             |             |         |state, county, city, town, etc.)       |required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| StateId                   |xs:IDREF                     |**Required** |Single   |Specifies a link to the state element  |If the field is not present or   |
|                           |                             |             |         |where the election is being held.      |invalid, the implementation is   |
|                           |                             |             |         |                                       |required to ignore the element   |
|                           |                             |             |         |                                       |containing it.                   |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| IsStatewide               |xs:boolean                   |Optional     |Single   |Indicates whether the election is      |If the field is not present or   |
|                           |                             |             |         |statewide.                             |invalid, the implementation is   |
|                           |                             |             |         |                                       |required to default to "yes".    |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| Name                      |:doc:`InternationalizedText  |Optional     |Single   |The name for the election (**NB:**     |If the element is invalid or not |
|                           |<internationalized_text>`    |             |         |while optional, this element is highly |present, the implementation is   |
|                           |                             |             |         |recommended).                          |required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| RegistrationInfo          |:doc:`InternationalizedText  |Optional     |Single   |Specifies information about            |If the field is invalid or not   |
|                           |<internationalized_text>`    |             |         |registration for this election either  |present, the implementation is   |
|                           |                             |             |         |as text or a URI.                      |required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| AbsenteeBallotInfo        |:doc:`InternationalizedText  |Optional     |Single   |Specifies information about requesting |If the element is invalid or not |
|                           |<internationalized_text>`    |             |         |absentee ballots either as text or a   |present, the implementation is   |
|                           |                             |             |         |URI                                    |required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
| ResultsUri                |xs:anyUri                    |Optional     |Single   |Contains a URI where results for the   |If the field is invalid or not   |
|                           |                             |             |         |election may be found                  |present, the implementation is   |
|                           |                             |             |         |                                       |required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
|PollingHours               |:doc:`InternationalizedText  |Optional     |Single   |Contains the hours (in local time) that|If the element is invalid or not |
|**[deprecated]**           |<internationalized_text>`    |             |         |Election Day polling locations are     |present, the implementation is   |
|                           |                             |             |         |open. If polling hours differ in       |required to ignore it.           |
|                           |                             |             |         |specific polling locations, alternative|                                 |
|                           |                             |             |         |hours may be specified in the          |                                 |
|                           |                             |             |         |:doc:`PollingLocation                  |                                 |
|                           |                             |             |         |<polling_location>` object *(NB: this  |                                 |
|                           |                             |             |         |element is deprecated in favor of the  |                                 |
|                           |                             |             |         |more structured :doc:`HoursOpen        |                                 |
|                           |                             |             |         |<hours_open>` element. It is strongly  |                                 |
|                           |                             |             |         |encouraged that data providers move    |                                 |
|                           |                             |             |         |toward contributing hours in this      |                                 |
|                           |                             |             |         |format)*.                              |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
|HoursOpenId                |xs:IDREF                     |Optional     |Single   |References the :doc:`HoursOpen         |If the field is invalid or not   |
|                           |                             |             |         |<hours_open>` element, which lists the |present, the implementation is   |
|                           |                             |             |         |hours of operation for polling         |required to ignore it.           |
|                           |                             |             |         |locations.                             |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
|HasElectionDayRegistration |xs:boolean                   |Optional     |Single   |Specifies if a voter can register on   |If the field is invalid or not   |
|                           |                             |             |         |the same day of the election (i.e., the|present, the implementation is   |
|                           |                             |             |         |last day of the election). Valid items |required to ignore it.           |
|                           |                             |             |         |are "yes" and "no".                    |                                 |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
|RegistrationDeadline       |xs:date                      |Optional     |Single   |Specifies the last day to register for |If the field is invalid or not   |
|                           |                             |             |         |the election with the possible         |present, the implementation is   |
|                           |                             |             |         |exception of Election Day registration.|required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+
|AbsenteeRequestDeadline    |xs:date                      |Optional     |Single   |Specifies the last day to request an   |If the field is invalid or not   |
|                           |                             |             |         |absentee ballot.                       |present, the implementation is   |
|                           |                             |             |         |                                       |required to ignore it.           |
|                           |                             |             |         |                                       |                                 |
|                           |                             |             |         |                                       |                                 |
+---------------------------+-----------------------------+-------------+---------+---------------------------------------+---------------------------------+

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

