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
| BallotName          | :ref:`multi-xml-internationalized-text`         | **Required** | Single       | The candidate's name as it will be       |                                          |
|                     |                                                 |              |              | displayed on the official ballot (e.g.   |                                          |
|                     |                                                 |              |              | "Ken T. Cuccinelli II").                 |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ContactInformation  | :ref:`multi-xml-contact-information`            | Optional     | Single       | Contact and physical address information |                                          |
|                     |                                                 |              |              | for this Candidate and/or their campaign |                                          |
|                     |                                                 |              |              | (see                                     |                                          |
|                     |                                                 |              |              | :ref:`multi-xml-contact-information`).   |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`           | Optional     | Single       | Another identifier for a candidate that  |                                          |
|                     |                                                 |              |              | links to another source of information   |                                          |
|                     |                                                 |              |              | (e.g. a campaign committee ID that links |                                          |
|                     |                                                 |              |              | to a campaign finance system).           |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileDate            | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for the    |                                          |
|                     |                                                 |              |              | contest.                                 |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsIncumbent         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   |                                          |
|                     |                                                 |              |              | incumbent for the office associated with |                                          |
|                     |                                                 |              |              | the contest.                             |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsTopTicket         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   |                                          |
|                     |                                                 |              |              | top of a ticket that includes multiple   |                                          |
|                     |                                                 |              |              | candidates.                              |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId             | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-xml-party`    |                                          |
|                     |                                                 |              |              | element with additional information      |                                          |
|                     |                                                 |              |              | about the candidate's affiliated party.  |                                          |
|                     |                                                 |              |              | This is the party affiliation that is    |                                          |
|                     |                                                 |              |              | intended to be presented as part of      |                                          |
|                     |                                                 |              |              | ballot information.                      |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PersonId            | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-xml-person`   |                                          |
|                     |                                                 |              |              | element with additional information      |                                          |
|                     |                                                 |              |              | about the candidate.                     |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostElectionStatus  | :ref:`multi-xml-candidate-post-election-status` | Optional     | Single       | Final status of the candidate (e.g.      |                                          |
|                     |                                                 |              |              | winner, withdrawn, etc...).              |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PreElectionStatus   | :ref:`multi-xml-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate     |                                          |
|                     |                                                 |              |              | (e.g. filed, qualified, etc...).         |                                          |
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
