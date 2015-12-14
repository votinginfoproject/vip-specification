ElectionAdministration
======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

.. include:: ../../tables/elements/election_administration.rst

.. _ea-dep:

Department
----------

.. include:: ../../tables/elements/department.rst

.. _ea-dep-voter-service:

VoterService
------------

.. include:: ../../tables/elements/voter_service.rst

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
