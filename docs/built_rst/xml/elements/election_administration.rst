.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election-administration:

ElectionAdministration
======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Tag                          | Data Type                        | Required?    | Repeats?     | Description                                                 | Error Handling                           |
+==============================+==================================+==============+==============+=============================================================+==========================================+
| AbsenteeUri                  | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on absentee       | If the field is invalid or not present,  |
|                              |                                  |              |              | voting.                                                     | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| AmIRegisteredUri             | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on whether an     | If the field is invalid or not present,  |
|                              |                                  |              |              | individual is registered.                                   | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| BallotTrackingUri            | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    | If the field is invalid or not present,  |
|                              |                                  |              |              | ballot cast by mail                                         | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| BallotProvisionalTrackingUri | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    | If the field is invalid or not present,  |
|                              |                                  |              |              | provisional ballot. To support EAC guidelines for           | then the implementation is required to   |
|                              |                                  |              |              | "Processing Provisional Ballots"                            | ignore it.                               |
|                              |                                  |              |              | (https://www.eac.gov/research-and-data/provisional-voting/) |                                          |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Department                   | :ref:`multi-xml-department`      | Optional     | Repeats      | Describes the administrative body for a particular voter    | If the element is invalid or not         |
|                              |                                  |              |              | service.                                                    | present, then the implementation is      |
|                              |                                  |              |              |                                                             | required to ignore it.                   |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ElectionNotice               | :ref:`multi-xml-election-notice` | Optional     | Single       | A place for election administrators to post last minute and | If the element is invalid or not         |
|                              |                                  |              |              | emergency notifications pertaining to the election.         | present, then the implementation is      |
|                              |                                  |              |              |                                                             | required to ignore it.                   |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ElectionsUri                 | ``xs:anyURI``                    | Optional     | Single       | Specifies web address the administration's website.         | If the field is invalid or not present,  |
|                              |                                  |              |              |                                                             | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| RegistrationUri              | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on registering to     | If the field is invalid or not present,  |
|                              |                                  |              |              | vote.                                                       | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| RulesUri                     | ``xs:anyURI``                    | Optional     | Single       | Specifies a URI for the election rules and laws (if any)    | If the field is invalid or not present,  |
|                              |                                  |              |              | for the jurisdiction of the administration.                 | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri          | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on what is on an      | If the field is invalid or not present,  |
|                              |                                  |              |              | individual's ballot.                                        | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
+------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| WhereDoIVoteUri              | ``xs:anyURI``                    | Optional     | Single       | The Specifies web address for information on where an       | If the field is invalid or not present,  |
|                              |                                  |              |              | individual votes based on their address.                    | then the implementation is required to   |
|                              |                                  |              |              |                                                             | ignore it.                               |
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
| ContactInformation       | :ref:`multi-xml-contact-information` | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          |                                      |              |              | for the election administration body     | present, then the implementation is      |
|                          |                                      |              |              | (see                                     | required to ignore it.                   |
|                          |                                      |              |              | :ref:`multi-xml-contact-information`).   |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | ``xs:IDREF``                         | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                                      |              |              | election administration office. The      | then the implementation is required to   |
|                          |                                      |              |              | specified person should be the           | ignore it.                               |
|                          |                                      |              |              | :ref:`election official                  |                                          |
|                          |                                      |              |              | <multi-xml-person>`.                     |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`multi-xml-voter-service`       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          |                                      |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                                      |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-voter-service:

VoterService
~~~~~~~~~~~~

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
| AddressLine      | ``xs:string``                           | Optional     | Repeats      | The "location" portion of a mailing      | If the field is invalid or not present,  |
|                  |                                         |              |              | address. :ref:`See usage note.           | then the implementation is required to   |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                  |                                         |              |              | locating this entity.                    | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Email            | ``xs:string``                           | Optional     | Repeats      | An email address for the contact.        | If the field is invalid or not present,  |
|                  |                                         |              |              |                                          | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Fax              | ``xs:string``                           | Optional     | Repeats      | A fax line for the contact.              | If the field is invalid or not present,  |
|                  |                                         |              |              |                                          | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]** |                                         |              |              | the location is open *(NB: this element  | present, then the implementation is      |
|                  |                                         |              |              | is deprecated in favor of the more       | required to ignore it.                   |
|                  |                                         |              |              | structured :ref:`multi-xml-hours-open`   |                                          |
|                  |                                         |              |              | element. It is strongly encouraged that  |                                          |
|                  |                                         |              |              | data providers move toward contributing  |                                          |
|                  |                                         |              |              | hours in this format)*.                  |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | ``xs:IDREF``                            | Optional     | Single       | References an                            | If the field is invalid or not present,  |
|                  |                                         |              |              | :ref:`multi-xml-hours-open` element,     | then the implementation is required to   |
|                  |                                         |              |              | which lists the hours of operation for a | ignore it.                               |
|                  |                                         |              |              | location.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng           | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                  |                                         |              |              | this entity.                             | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name             | ``xs:string``                           | Optional     | Single       | The name of the location or contact.     | If the field is invalid or not present,  |
|                  |                                         |              |              | :ref:`See usage note.                    | then the implementation is required to   |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Phone            | ``xs:string``                           | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|                  |                                         |              |              |                                          | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Uri              | ``xs:anyURI``                           | Optional     | Repeats      | An informational URI for the contact or  | If the field is invalid or not present,  |
|                  |                                         |              |              | location.                                | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
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
| NoticeText   | :ref:`multi-xml-internationalized-text` | **Required** | Single       | The last minute or emergency             | If the element is invalid, then the      |
|              |                                         |              |              | notification text should be placed here. | implementation is required to ignore the |
|              |                                         |              |              |                                          | ``ElectionNotice`` element containing    |
|              |                                         |              |              |                                          | it.                                      |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | ``xs:anyURI``                           | Optional     | Single       | Optional URL for additional information  | If the field is invalid or not present,  |
|              |                                         |              |              | related to the last minute or emergency  | then the implementation is required to   |
|              |                                         |              |              | notification.                            | ignore it.                               |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


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
