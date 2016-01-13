.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election-administration:

ElectionAdministration
======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=============================+==============+==============+==========================================+==========================================+
| AbsenteeUri         | ``xs:anyURI``               | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                             |              |              | information on absentee voting.          | then the implementation is required to   |
|                     |                             |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AmIRegisteredUri    | ``xs:anyURI``               | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                             |              |              | information on whether an individual is  | then the implementation is required to   |
|                     |                             |              |              | registered.                              | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Department          | :ref:`multi-xml-department` | **Required** | Repeats      | Describes the administrative body for a  | There must be at least one valid         |
|                     |                             |              |              | particular voter service.                | `Department` in each                     |
|                     |                             |              |              |                                          | `ElectionAdministration` element. If no  |
|                     |                             |              |              |                                          | valid `Department` objects are present,  |
|                     |                             |              |              |                                          | the implementation is required to ignore |
|                     |                             |              |              |                                          | the `ElectionAdministration` object that |
|                     |                             |              |              |                                          | contains it/them.                        |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionsUri        | ``xs:anyURI``               | Optional     | Single       | Specifies web address the                | If the field is invalid or not present,  |
|                     |                             |              |              | administration's website.                | then the implementation is required to   |
|                     |                             |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationUri     | ``xs:anyURI``               | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                             |              |              | registering to vote.                     | then the implementation is required to   |
|                     |                             |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RulesUri            | ``xs:anyURI``               | Optional     | Single       | Specifies a URI for the election rules   | If the field is invalid or not present,  |
|                     |                             |              |              | and laws (if any) for the jurisdiction   | then the implementation is required to   |
|                     |                             |              |              | of the administration.                   | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri | ``xs:anyURI``               | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                             |              |              | what is on an individual's ballot.       | then the implementation is required to   |
|                     |                             |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhereDoIVoteUri     | ``xs:anyURI``               | Optional     | Single       | The Specifies web address for            | If the field is invalid or not present,  |
|                     |                             |              |              | information on where an individual votes | then the implementation is required to   |
|                     |                             |              |              | based on their address.                  | ignore it.                               |
+---------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-department:

Department
----------

+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information` | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          |                                      |              |              | for the election administration body     | present, then the implementation is      |
|                          |                                      |              |              | (see                                     | required to ignore it.                   |
|                          |                                      |              |              | :ref:`single-xml-contact-information`).  |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                         | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                                      |              |              | election administration office. The      | then the implementation is required to   |
|                          |                                      |              |              | specified person should be the           | ignore it.                               |
|                          |                                      |              |              | :ref:`election official                  |                                          |
|                          |                                      |              |              | <single-xml-person>`.                    |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`multi-xml-voter-service`       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          |                                      |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                                      |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-voter-service:

VoterService
------------

+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information`    | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          |                                         |              |              | service.                                 | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          |                                         |              |              | available.                               | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                            | Optional     | Single       | The :ref:`authority <single-xml-person>` | If the field is invalid or not present,  |
|                          |                                         |              |              | for a particular voter service.          | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                          |                                         |              |              | <single-xml-voter-service-type>`.        | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                           | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                         |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                         |              |              | service.                                 | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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
