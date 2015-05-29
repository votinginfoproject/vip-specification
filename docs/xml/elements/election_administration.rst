ElectionAdministration
======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| Tag                 | Data Type             | Required?   | Repeats?   | Description               | Error Handling           |
|                     |                       |             |            |                           |                          |
+=====================+=======================+=============+============+===========================+==========================+
| AbsenteeUri         | xs:anyURI             | Optional    | Single     |Specifies the web          |If the field is invalid or|
|                     |                       |             |            |address for                |not present, the          |
|                     |                       |             |            |information on             |implementation is required|
|                     |                       |             |            |absentee voting.           |to ignore it.             |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| AmIRegisteredUri    | xs:anyURI             | Optional    | Single     |Specifies the web          |If the field is invalid or|
|                     |                       |             |            |address for                |not present, the          |
|                     |                       |             |            |information on whether     |implementation is required|
|                     |                       |             |            |an individual is           |to ignore it.             |
|                     |                       |             |            |registered.                |                          |
|                     |                       |             |            |                           |                          |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| Department          |:ref:`Department       | **Required**| Repeats    |Describes the              |If the element is invalid |
|                     |<ea-dep>`              |             |            |administrative body        |or not present, the       |
|                     |                       |             |            |for a particular voter     |implementation is required|
|                     |                       |             |            |service.                   |to ignore the             |
|                     |                       |             |            |                           |**ElectionAdministration**|
|                     |                       |             |            |                           |object that contains it.  |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| ElectionsUri        | xs:anyURI             | Optional    | Single     |Specifies web address      |If the field is invalid or|
|                     |                       |             |            |the administration's       |not present, the          |
|                     |                       |             |            |website.                   |implementation is required|
|                     |                       |             |            |                           |to ignore it.             |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| RegistrationUri     | xs:anyURI             | Optional    | Single     |Specifies web address for  |If the field is invalid or|
|                     |                       |             |            |information on registering |not present, the          |
|                     |                       |             |            |to vote.                   |implementation is required|
|                     |                       |             |            |                           |to ignore it.             |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| RulesUri            | xs:anyURI             | Optional    | Single     |Specifies a URL for the    |If the field is invalid   |
|                     |                       |             |            |election rules and laws (if|the implementation is     |
|                     |                       |             |            |any) for the jurisdiction  |required to ignore it.    |
|                     |                       |             |            |of the administration.     |                          |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| WhatIsOnMyBallotUri | xs:anyURI             | Optional    | Single     |Specifies web address for  |If the field is invalid or|
|                     |                       |             |            |information on what is on  |not present, the          |
|                     |                       |             |            |an individual's ballot.    |implementation is required|
|                     |                       |             |            |                           |to ignore it.             |
|                     |                       |             |            |                           |                          |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+
| WhereDoIVoteUri     | xs:anyURI             | Optional    | Single     |The Specifies web address  |If the field is invalid or|
|                     |                       |             |            |for information on where an|not present, the          |
|                     |                       |             |            |individual votes based on  |implementation is required|
|                     |                       |             |            |their address.             |to ignore it.             |
|                     |                       |             |            |                           |                          |
+---------------------+-----------------------+-------------+------------+---------------------------+--------------------------+

.. _ea-dep:

ElectionAdministration.Department
---------------------------------

+--------------------------+-------------------------------------------------+------------+-----------+------------------------+---------------------------+
| Tag                      | Data Type                                       | Required?  | Repeats?  | Description            | Error Handling            |
|                          |                                                 |            |           |                        |                           |
+==========================+=================================================+============+===========+========================+===========================+
| ContactInformation       | :doc:`ContactInformation <contact_information>` | Optional   | Single    |Contact and physical    |If the element is invalid  |
|                          |                                                 |            |           |address information for |or not present, the        |
|                          |                                                 |            |           |the election            |implementation is required |
|                          |                                                 |            |           |administration body (see|to ignore it.              |
|                          |                                                 |            |           |:doc:`ContactInformation|                           |
|                          |                                                 |            |           |<contact_information>`).|                           |
+--------------------------+-------------------------------------------------+------------+-----------+------------------------+---------------------------+
| ElectionOfficialPersonId | xs:IDREF                                        | Optional   | Single    |The individual to       |If the element is invalid  |
|                          |                                                 |            |           |contact at the election |or not present, the        |
|                          |                                                 |            |           |administration          |implementation is required |
|                          |                                                 |            |           |office. The specified   |to ignore it.              |
|                          |                                                 |            |           |person should be the    |                           |
|                          |                                                 |            |           |:doc:`election official |                           |
|                          |                                                 |            |           |<person>`.              |                           |
+--------------------------+-------------------------------------------------+------------+-----------+------------------------+---------------------------+
| VoterService             | :ref:`VoterService <ea-dep-voter-service>`      | Optional   | Repeats   |The types of services   |If the element is invalid  |
|                          |                                                 |            |           |and appropriate contact |or not present, the        |
|                          |                                                 |            |           |individual available to |implementation is required |
|                          |                                                 |            |           |voters.                 |to ignore it.              |
+--------------------------+-------------------------------------------------+------------+-----------+------------------------+---------------------------+

.. _ea-dep-voter-service:

ElectionAdministration.Department.VoterService
----------------------------------------------

+---------------------------+-------------------------------------+-----------+----------+--------------------------------------+------------------------+
| Tag                       | Data Type                           | Required? | Repeats? | Description                          | Error Handling         |
|                           |                                     |           |          |                                      |                        |
+===========================+=====================================+===========+==========+======================================+========================+
| ContactInformation        |:doc:`ContactInformation             | Optional  | Single   |The contact for a                     |If the element is       |
|                           |<contact_information>`               |           |          |particular voter                      |invalid or not present, |
|                           |                                     |           |          |service.                              |the implementation is   |
|                           |                                     |           |          |                                      |required to ignore it.  |
+---------------------------+-------------------------------------+-----------+----------+--------------------------------------+------------------------+
| Description               |:doc:`InternationalizedText          | Optional  | Single   |Long description of                   |If the field is invalid |
|                           |<internationalized_text>`            |           |          |the services                          |or not present, the     |
|                           |                                     |           |          |available.                            |implementation is       |
|                           |                                     |           |          |                                      |required to ignore it.  |
+---------------------------+-------------------------------------+-----------+----------+--------------------------------------+------------------------+
| ElectionOfficialPersonId  | xs:IDREF                            | Optional  | Single   |The :doc:`authority                   |If the field is invalid |
|                           |                                     |           |          |<person>` for a                       |or not present, the     |
|                           |                                     |           |          |particular voter                      |implementation is       |
|                           |                                     |           |          |service.                              |required to ignore it.  |
+---------------------------+-------------------------------------+-----------+----------+--------------------------------------+------------------------+
| Type                      |:doc:`VoterServiceType               | Optional  | Single   |The type of :doc:`voter service       |If the element is       |
|                           |<../enumerations/voter_service_type>`|           |          |<../enumerations/voter_service_type>`.|invalid or not present, |
|                           |                                     |           |          |                                      |the implementation is   |
|                           |                                     |           |          |                                      |required to ignore it.  |
+---------------------------+-------------------------------------+-----------+----------+--------------------------------------+------------------------+
| OtherType                 | xs:string                           | Optional  | Single   |If Type is "other",                   |If the field is invalid |
|                           |                                     |           |          |OtherType allows for                  |or not present, the     |
|                           |                                     |           |          |cataloging another                    |implementation is       |
|                           |                                     |           |          |type of voter service.                |required to ignore it.  |
+---------------------------+-------------------------------------+-----------+----------+--------------------------------------+------------------------+

.. code-block:: xml
   :linenos:
   
   <ElectionAdministration id="ea40133">
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <Department>
        <ContactInformation identifier="ci60000">
	  <AddressLine>Washington Building First Floor</AddressLine>
	  <AddressLine>1100 Bank Street</AddressLine>
	  <AddressLine>Richmond, VA 23219</AddressLine>
	  <Name>State Board of Elections</Name>
	</ContactInformation>
      </Department>
      <ElectionsUri>http://www.sbe.virginia.gov/</ElectionsUri>
      <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      <RulesUri>http://www.sbe.virginia.gov/</RulesUri>
      <WhatIsOnMyBallotUri>https://www.vote.virginia.gov/</WhatIsOnMyBallotUri>
      <WhereDoIVoteUri>https://www.vote.virginia.gov/</WhereDoIVoteUri>
   </ElectionAdministration>
