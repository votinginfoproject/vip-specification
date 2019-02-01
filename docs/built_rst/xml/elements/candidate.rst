.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate:

Candidate
=========

The Candidate object represents a candidate in a contest. If a candidate is
running in multiple contests, each contest **must** have its own Candidate
object. Candidate objects may **not** be reused between Contests.

+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=================================================+==============+==============+==========================================+==========================================+
| BallotName          | :ref:`multi-xml-internationalized-text`         | **Required** | Single       | The candidate's name as it will be       | If the element is invalid or not         |
|                     |                                                 |              |              | displayed on the official ballot (e.g.   | present, then the implementation is      |
|                     |                                                 |              |              | "Ken T. Cuccinelli II").                 | required to ignore the Candidate element |
|                     |                                                 |              |              |                                          | containing it.                           |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ContactInformation  | :ref:`multi-xml-contact-information`            | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                     |                                                 |              |              | for this Candidate and/or their campaign | present, then the implementation is      |
|                     |                                                 |              |              | (see                                     | required to ignore it.                   |
|                     |                                                 |              |              | :ref:`multi-xml-contact-information`).   |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`           | Optional     | Single       | Another identifier for a candidate that  | If the element is invalid or not         |
|                     |                                                 |              |              | links to another source of information   | present, then the implementation is      |
|                     |                                                 |              |              | (e.g. a campaign committee ID that links | required to ignore it.                   |
|                     |                                                 |              |              | to a campaign finance system).           |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileDate            | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for the    | If the field is invalid or not present,  |
|                     |                                                 |              |              | contest.                                 | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsIncumbent         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                 |              |              | incumbent for the office associated with | then the implementation is required to   |
|                     |                                                 |              |              | the contest.                             | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsTopTicket         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                 |              |              | top of a ticket that includes multiple   | then the implementation is required to   |
|                     |                                                 |              |              | candidates.                              | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId             | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-xml-party`    | If the field is invalid or not present,  |
|                     |                                                 |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                 |              |              | about the candidate's affiliated party.  | ignore it.                               |
|                     |                                                 |              |              | This is the party affiliation that is    |                                          |
|                     |                                                 |              |              | intended to be presented as part of      |                                          |
|                     |                                                 |              |              | ballot information.                      |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PersonId            | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-xml-person`   | If the field is invalid or not present,  |
|                     |                                                 |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                 |              |              | about the candidate.                     | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostElectionStatus  | :ref:`multi-xml-candidate-post-election-status` | Optional     | Single       | Final status of the candidate (e.g.      | If the field is invalid or not present,  |
|                     |                                                 |              |              | winner, withdrawn, etc...).              | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PreElectionStatus   | :ref:`multi-xml-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate     | If the field is invalid or not present,  |
|                     |                                                 |              |              | (e.g. filed, qualified, etc...).         | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Candidate id="can10961">
      <BallotName>
        <Text language="en">Ken T. Cuccinelli II</Text>
      </BallotName>
      <PartyId>par0001</PartyId>
      <PersonId>per10961</PersonId>
   </Candidate>


.. _multi-xml-external-identifiers:

ExternalIdentifiers
-------------------

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-xml-candidate`

* Any element that extends :ref:`multi-xml-contest-base`

* :ref:`multi-xml-electoral-district`

* :ref:`multi-xml-locality`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-precinct`

* :ref:`multi-xml-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+======================================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | :ref:`multi-xml-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                    |                                      |              |              | identifier it is (see                    | must be present for                      |
|                    |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                    |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                    |                                      |              |              |                                          | present, the implementation is required  |
|                    |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                    |                                      |              |              |                                          | element.                                 |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-external-identifier:

ExternalIdentifier
~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                                  |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                  |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                  |              |              | outside the options listed in            | ignore it.                               |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
|              |                                  |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                  |              |              | using this field.                        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifiers>
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:nc/county:durham</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>FIPS</Type>
         <Value>37063</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>OTHER</Type>
         <OtherType>GNIS</OtherType>
         <Value>1008550</Value>
      </ExternalIdentifier>
      <external_identifer>
         <Type>OTHER</Type>
         <OtherType>census</OtherType>
         <Value>99063</Value>
      </ExternalIdentifier>
   </ExternalIdentifiers>
