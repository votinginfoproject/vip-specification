.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election-administration:

ElectionAdministration
======================

The ElectionAdministration element represents an administrative body serving a locality's election functions. In VIP 7.0, ElectionAdministration is embedded directly by value inside a :ref:`multi-xml-locality` element rather than referenced by an ID.

In overlay feeds, the entire ElectionAdministration element is replaced as a single unit on the locality, or cleared using ``<ClearElectionAdministration/>``.

+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| Tag                          | Data Type                              | Required?    | Repeats?     | Description                                                  | Error Handling                           |
+==============================+========================================+==============+==============+==============================================================+==========================================+
| AbsenteeUri                  | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address for absentee voting information.                 | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| AmIRegisteredUri             | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address for voter registration status verification.      | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| BallotTrackingUri            | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address for tracking mail-in ballots.                    | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| BallotProvisionalTrackingUri | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Specifies the web address for tracking information for a     | If the element is invalid or not         |
|                              |                                        |              |              | provisional ballot, supporting EAC guidelines for            | present, then the implementation is      |
|                              |                                        |              |              | "Processing Provisional Ballots"                             | required to ignore it.                   |
|                              |                                        |              |              | (https://www.eac.gov/research-and-data/provisional-voting/). |                                          |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| ContactInformation           | :ref:`multi-xml-contact-information`   | Optional     | Single       | Primary contact information for the election administration. | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| ElectionsUri                 | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Primary web address for the election administration.         | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| RegistrationUri              | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address for voter registration.                          | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| RulesUri                     | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address for election rules, regulations, and statutes.   | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| VoterService                 | :ref:`multi-xml-voter-service`         | Optional     | Repeats      | Specific voter services provided by the administration (e.g. | If the element is invalid or not         |
|                              |                                        |              |              | voter registration, overseas voting).                        | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri          | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address where voters can see sample ballots.             | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+
| WhereDoIVoteUri              | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Web address for official polling place lookup.               | If the element is invalid or not         |
|                              |                                        |              |              |                                                              | present, then the implementation is      |
|                              |                                        |              |              |                                                              | required to ignore it.                   |
+------------------------------+----------------------------------------+--------------+--------------+--------------------------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectionAdministration>
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <BallotTrackingUri>https://www.vote.virginia.gov/track</BallotTrackingUri>
      <BallotProvisionalTrackingUri>https://www.vote.virginia.gov/provisional</BallotProvisionalTrackingUri>
      <ContactInformation label="ea_contact">
         <Name>Virginia Department of Elections</Name>
         <PhysicalAddress>
            <AddressLine>Washington Building, First Floor</AddressLine>
            <AddressLine>1100 Bank Street</AddressLine>
            <City>Richmond</City>
            <Region>VA</Region>
            <PostalCode>23219</PostalCode>
         </PhysicalAddress>
         <Phone>804-864-8901</Phone>
         <Email>info@elections.virginia.gov</Email>
      </ContactInformation>
      <ElectionsUri>http://www.sbe.virginia.gov/</ElectionsUri>
      <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      <RulesUri>http://www.sbe.virginia.gov/rules</RulesUri>
      <WhatIsOnMyBallotUri>https://www.vote.virginia.gov/ballot</WhatIsOnMyBallotUri>
      <WhereDoIVoteUri>https://www.vote.virginia.gov/polling-place</WhereDoIVoteUri>
   </ElectionAdministration>


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
| ElectionOfficialPersonId | ``xs:IDREF``                            | Optional     | Single       | The :ref:`authority <multi-xml-person>`  | If the field is invalid or not present,  |
|                          |                                         |              |              | for a particular voter service.          | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                          |                                         |              |              | <multi-xml-voter-service-type>`.         | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                           | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                         |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                         |              |              | service.                                 | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-contact-information:

ContactInformation
------------------

For defining contact information about objects such as persons, boards of authorities, organizations, election offices, voter services, or polling locations. ContactInformation is always a sub-element of another object (e.g. :ref:`multi-xml-election-administration`, :ref:`multi-xml-office`, :ref:`multi-xml-person`). ContactInformation has an optional attribute ``label``, which allows the feed to refer back to the original label for the information (e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                                | Error Handling                           |
+====================+=========================================+==============+==============+============================================+==========================================+
| MailingAddress     | :ref:`multi-xml-simple-address-type`    | Optional     | Repeats      | Structured mailing address for the         | If the element is invalid or not         |
|                    |                                         |              |              | contact. Multiple addresses in different   | present, then the implementation is      |
|                    |                                         |              |              | languages can be specified.                | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| PhysicalAddress    | :ref:`multi-xml-simple-address-type`    | Optional     | Repeats      | Structured physical address for the        | If the element is invalid or not         |
|                    |                                         |              |              | contact. Multiple addresses in different   | present, then the implementation is      |
|                    |                                         |              |              | languages can be specified.                | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| LocationIdentifier | :ref:`multi-xml-location-identifier`    | Optional     | Repeats      | External location identifier(s) (e.g. Plus | If the element is invalid or not         |
|                    |                                         |              |              | Code, coordinates).                        | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Directions         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Directions for finding or reaching the     | If the element is invalid or not         |
|                    |                                         |              |              | contact location.                          | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Email              | :ref:`multi-xml-internationalized-text` | Optional     | Repeats      | Email address(es) for the contact.         | If the element is invalid or not         |
|                    |                                         |              |              |                                            | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Fax                | :ref:`multi-xml-internationalized-text` | Optional     | Repeats      | Fax number(s) for the contact.             | If the element is invalid or not         |
|                    |                                         |              |              |                                            | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Hours              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Operating hours as free-form text. *(NB:   | If the element is invalid or not         |
|                    |                                         |              |              | deprecated in favor of                     | present, then the implementation is      |
|                    |                                         |              |              | :ref:`multi-xml-schedule-with-timezone`)*. | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Schedule           | :ref:`multi-xml-schedule-with-timezone` | Optional     | Repeats      | Structured schedule with dates and         | If the element is invalid or not         |
|                    |                                         |              |              | operating hours.                           | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| LatLng             | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Latitude and longitude coordinates.        | If the element is invalid or not         |
|                    |                                         |              |              |                                            | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Name               | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Person or place name associated with this  | If the element is invalid or not         |
|                    |                                         |              |              | contact information.                       | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Phone              | :ref:`multi-xml-internationalized-text` | Optional     | Repeats      | Telephone number(s) for the contact.       | If the element is invalid or not         |
|                    |                                         |              |              |                                            | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Uri                | :ref:`multi-xml-internationalized-uri`  | Optional     | Repeats      | Web address(es) for the contact.           | If the element is invalid or not         |
|                    |                                         |              |              |                                            | present, then the implementation is      |
|                    |                                         |              |              |                                            | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+--------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ContactInformation label="office_contact">
      <PhysicalAddress language="en">
         <LocationName>City Hall</LocationName>
         <AddressLine>100 N Main St, Room 101</AddressLine>
         <City>Springfield</City>
         <Region>IL</Region>
         <PostalCode>62701</PostalCode>
      </PhysicalAddress>
      <LocationIdentifier provider="google">
         <Type>pluscode</Type>
         <Value>86HJQPRX+86</Value>
      </LocationIdentifier>
      <Email>elections@springfield.gov</Email>
      <Phone>217-555-0100</Phone>
      <Schedule>
         <TimeZone>America/Chicago</TimeZone>
         <Hours>
            <StartTime>08:30:00</StartTime>
            <EndTime>16:30:00</EndTime>
         </Hours>
      </Schedule>
      <Uri>https://elections.springfield.gov</Uri>
   </ContactInformation>
