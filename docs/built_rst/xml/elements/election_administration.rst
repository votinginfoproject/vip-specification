.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election-administration:

ElectionAdministration
======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Tag                          | Data Type                        | Required?    | Repeats?     | Description                                                 | Error Handling                           |
+==============================+==================================+==============+==============+=============================================================+==========================================+
| AbsenteeUri                  | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on absentee       |                                          |
|                              |                                  |              |              | voting.                                                     |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| AmIRegisteredUri             | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on whether an     |                                          |
|                              |                                  |              |              | individual is registered.                                   |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| BallotTrackingUri            | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    |                                          |
|                              |                                  |              |              | ballot cast by mail                                         |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| BallotProvisionalTrackingUri | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    |                                          |
|                              |                                  |              |              | provisional ballot. To support EAC guidelines for           |                                          |
|                              |                                  |              |              | "Processing Provisional Ballots"                            |                                          |
|                              |                                  |              |              | (https://www.eac.gov/research-and-data/provisional-voting/) |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Department                   | :ref:`multi-xml-department`      | Optional     | Repeats      | Describes the administrative body for a particular voter    |                                          |
|                              |                                  |              |              | service.                                                    |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ElectionNotice               | :ref:`multi-xml-election-notice` | Optional     | Single       | A place for election administrators to post last minute and |                                          |
|                              |                                  |              |              | emergency notifications pertaining to the election.         |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ElectionsUri                 | ``xs:anyURI``                    | Optional     | Single       | Specifies web address the administration's website.         |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| RegistrationUri              | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on registering to     |                                          |
|                              |                                  |              |              | vote.                                                       |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| RulesUri                     | ``xs:anyURI``                    | Optional     | Single       | Specifies a URI for the election rules and laws (if any)    |                                          |
|                              |                                  |              |              | for the jurisdiction of the administration.                 |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri          | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on what is on an      |                                          |
|                              |                                  |              |              | individual's ballot.                                        |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| WhereDoIVoteUri              | ``xs:anyURI``                    | Optional     | Single       | The Specifies web address for information on where an       |                                          |
|                              |                                  |              |              | individual votes based on their address.                    |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectionAdministration id="ea40133">
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <BallotTrackingUri>https://www.vote.virginia.gov/</BallotTrackingUri>
      <BallotProvisionalTrackingUri>https://www.vote.virginia.gov/</BallotProvisionalTrackingUri>
      <Department>
        <ContactInformation label="ci60000">
          <AddressLine>Washington Building First Floor</AddressLine>
          <AddressLine>1100 Bank Street</AddressLine>
          <AddressLine>Richmond, VA 23219</AddressLine>
          <Name>State Board of Elections</Name>
        </ContactInformation>
      </Department>
      <ElectionNotice>
        <NoticeText>
          <Text language="en">This is an emergency notification for this election.</Text>
        </NoticeText>
        <NoticeURI>https://www.yadayada.gov</NoticeURI>
      </ElectionNotice>
      <ElectionsUri>http://www.sbe.virginia.gov/</ElectionsUri>
      <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      <RulesUri>http://www.sbe.virginia.gov/</RulesUri>
      <WhatIsOnMyBallotUri>https://www.vote.virginia.gov/</WhatIsOnMyBallotUri>
      <WhereDoIVoteUri>https://www.vote.virginia.gov/</WhereDoIVoteUri>
   </ElectionAdministration>


.. _multi-xml-department:

Department
----------

+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information` | Optional     | Single       | Contact and physical address information |                                          |
|                          |                                      |              |              | for the election administration body     |                                          |
|                          |                                      |              |              | (see                                     |                                          |
|                          |                                      |              |              | :ref:`multi-xml-contact-information`).   |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                         | Optional     | Single       | The individual to contact at the         |                                          |
|                          |                                      |              |              | election administration office. The      |                                          |
|                          |                                      |              |              | specified person should be the           |                                          |
|                          |                                      |              |              | :ref:`election official                  |                                          |
|                          |                                      |              |              | <multi-xml-person>`.                     |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`multi-xml-voter-service`       | Optional     | Repeats      | The types of services and appropriate    |                                          |
|                          |                                      |              |              | contact individual available to voters.  |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-voter-service:

VoterService
~~~~~~~~~~~~

+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information`    | Optional     | Single       | The contact for a particular voter       |                                          |
|                          |                                         |              |              | service.                                 |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Long description of the services         |                                          |
|                          |                                         |              |              | available.                               |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                            | Optional     | Single       | The :ref:`authority <multi-xml-person>`  |                                          |
|                          |                                         |              |              | for a particular voter service.          |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          |                                          |
|                          |                                         |              |              | <multi-xml-voter-service-type>`.         |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                           | Optional     | Single       | If Type is "other", OtherType allows for |                                          |
|                          |                                         |              |              | cataloging another type of voter         |                                          |
|                          |                                         |              |              | service.                                 |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-contact-information:

ContactInformation
~~~~~~~~~~~~~~~~~~

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`multi-xml-election-administration`, :ref:`multi-xml-office`,
:ref:`multi-xml-person`, :ref:`multi-xml-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=========================================+==============+==============+==========================================+==========================================+
| AddressLine      | ``xs:string``                           | Optional     | Repeats      | The "location" portion of a mailing      |                                          |
|                  |                                         |              |              | address. :ref:`See usage note.           |                                          |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for       |                                          |
|                  |                                         |              |              | locating this entity.                    |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Email            | ``xs:string``                           | Optional     | Repeats      | An email address for the contact.        |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Fax              | ``xs:string``                           | Optional     | Repeats      | A fax line for the contact.              |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  |                                          |
| **[deprecated]** |                                         |              |              | the location is open *(NB: this element  |                                          |
|                  |                                         |              |              | is deprecated in favor of the more       |                                          |
|                  |                                         |              |              | structured :ref:`multi-xml-hours-open`   |                                          |
|                  |                                         |              |              | element. It is strongly encouraged that  |                                          |
|                  |                                         |              |              | data providers move toward contributing  |                                          |
|                  |                                         |              |              | hours in this format)*.                  |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | ``xs:IDREF``                            | Optional     | Single       | References an                            |                                          |
|                  |                                         |              |              | :ref:`multi-xml-hours-open` element,     |                                          |
|                  |                                         |              |              | which lists the hours of operation for a |                                          |
|                  |                                         |              |              | location.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng           | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Specifies the latitude and longitude of  |                                          |
|                  |                                         |              |              | this entity.                             |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name             | ``xs:string``                           | Optional     | Single       | The name of the location or contact.     |                                          |
|                  |                                         |              |              | :ref:`See usage note.                    |                                          |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Phone            | ``xs:string``                           | Optional     | Repeats      | A phone number for the contact.          |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Uri              | ``xs:anyURI``                           | Optional     | Repeats      | An informational URI for the contact or  |                                          |
|                  |                                         |              |              | location.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _multi-xml-name-address-line-usage:

``Name`` and ``AddressLine`` Usage Note
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``Name`` and ``AddressLine`` fields should be chosen so that a display
or mailing address can be constructed programmatically by joining the
``Name`` and ``AddressLine`` fields together.  For example, for the
following address::

    Department of Elections
    1 Dr. Carlton B. Goodlett Place, Room 48
    San Francisco, CA 94102

The name could be "Department of Elections" and the first address line
could be "1 Dr. Carlton B. Goodlett Place, Room 48."

However, VIP does not yet support the representation of mailing addresses
whose "name" portion spans more than one line, for example::

    California Secretary of State
    Elections Division
    1500 11th Street
    Sacramento, CA 95814

For addresses like the above, we recommend choosing a name like, "California
Secretary of State, Elections Division" with "1500 11th Street" as the
first address line. This would result in a programmatically constructed
address like the following::

    California Secretary of State, Elections Division
    1500 11th Street
    Sacramento, CA 95814

.. code-block:: xml
   :linenos:

   <ContactInformation label="ci10861a">
      <AddressLine>1600 Pennsylvania Ave</AddressLine>
      <AddressLine>Washington, DC 20006</AddressLine>
      <Email>president@whitehouse.gov</Email>
      <Phone>202-456-1111</Phone>
      <Phone annotation="TDD">202-456-6213</Phone>
      <Uri>http://www.whitehouse.gov</Uri>
   </ContactInformation>


.. _multi-xml-election-notice:

ElectionNotice
--------------

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`multi-xml-internationalized-text` | **Required** | Single       | The last minute or emergency             |                                          |
|              |                                         |              |              | notification text should be placed here. |                                          |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | ``xs:anyURI``                           | Optional     | Single       | Optional URL for additional information  |                                          |
|              |                                         |              |              | related to the last minute or emergency  |                                          |
|              |                                         |              |              | notification.                            |                                          |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-voter-service:

VoterService
------------

+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :ref:`multi-xml-contact-information`    | Optional     | Single       | The contact for a particular voter       |                                          |
|                          |                                         |              |              | service.                                 |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Long description of the services         |                                          |
|                          |                                         |              |              | available.                               |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                            | Optional     | Single       | The :ref:`authority <multi-xml-person>`  |                                          |
|                          |                                         |              |              | for a particular voter service.          |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :ref:`multi-xml-voter-service-type`     | Optional     | Single       | The type of :ref:`voter service          |                                          |
|                          |                                         |              |              | <multi-xml-voter-service-type>`.         |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | ``xs:string``                           | Optional     | Single       | If Type is "other", OtherType allows for |                                          |
|                          |                                         |              |              | cataloging another type of voter         |                                          |
|                          |                                         |              |              | service.                                 |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
