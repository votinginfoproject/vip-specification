.. This file is auto-generated.  Do not edit it by hand!

ElectionAdministration
======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type        | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==================+==============+==============+==========================================+==========================================+
| AbsenteeUri         | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on absentee voting.          | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AmIRegisteredUri    | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on whether an individual is  | then the implementation is required to   |
|                     |                  |              |              | registered.                              | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Department          | :ref:`Department | **Required** | Repeats      | Describes the administrative body for a  | There must be at least one valid         |
|                     | <ea-dep>`        |              |              | particular voter service.                | `Department` in each                     |
|                     |                  |              |              |                                          | `ElectionAdministration` element. If no  |
|                     |                  |              |              |                                          | valid `Department` objects are present,  |
|                     |                  |              |              |                                          | the implementation is required to ignore |
|                     |                  |              |              |                                          | the `ElectionAdministration` object that |
|                     |                  |              |              |                                          | contains it/them.                        |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionsUri        | xs:anyURI        | Optional     | Single       | Specifies web address the                | If the field is invalid or not present,  |
|                     |                  |              |              | administration's website.                | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationUri     | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | registering to vote.                     | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RulesUri            | xs:anyURI        | Optional     | Single       | Specifies a URI for the election rules   | If the field is invalid or not present,  |
|                     |                  |              |              | and laws (if any) for the jurisdiction   | then the implementation is required to   |
|                     |                  |              |              | of the administration.                   | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | what is on an individual's ballot.       | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhereDoIVoteUri     | xs:anyURI        | Optional     | Single       | The Specifies web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on where an individual votes | then the implementation is required to   |
|                     |                  |              |              | based on their address.                  | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _ea-dep:


Department
----------

+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          | <contact_information>`   |              |              | for the election administration body     | present, then the implementation is      |
|                          |                          |              |              | (see :doc:`ContactInformation            | required to ignore it.                   |
|                          |                          |              |              | <contact_information>`).                 |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                 | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                          |              |              | election administration office. The      | then the implementation is required to   |
|                          |                          |              |              | specified person should be the           | ignore it.                               |
|                          |                          |              |              | :doc:`election official <person>`.       |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`VoterService       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          | <ea-dep-voter-service>`  |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                          |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _ea-dep-voter-service:


VoterService
------------

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation              | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          | <contact_information>`                |              |              | service.                                 | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :doc:`InternationalizedText           | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          | <internationalized_text>`             |              |              | available.                               | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                              | Optional     | Single       | The :doc:`authority <person>` for a      | If the field is invalid or not present,  |
|                          |                                       |              |              | particular voter service.                | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`VoterServiceType                | Optional     | Single       | The type of :doc:`voter service          | If the field is invalid or not present,  |
|                          | <../enumerations/voter_service_type>` |              |              | <../enumerations/voter_service_type>`.   | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                             | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                       |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                       |              |              | service.                                 | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectionAdministration id="ea40133">
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <Department>
        <ContactInformation label="ci60000">
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