.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate:

Candidate
=========

The Candidate object represents a candidate in a contest. If a candidate is running in multiple contests, each contest **must** have its own Candidate object.

+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| Tag                | Data Type                                       | Required?    | Repeats?     | Description                                     | Error Handling                           |
+====================+=================================================+==============+==============+=================================================+==========================================+
| BallotName         | :ref:`multi-xml-internationalized-text`         | **Required** | Single       | The candidate's name as it will appear on the   | If the element is invalid, then the      |
|                    |                                                 |              |              | ballot.                                         | implementation is required to ignore the |
|                    |                                                 |              |              |                                                 | ``Candidate`` element containing it.     |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| ContactInformation | :ref:`multi-xml-contact-information`            | Optional     | Single       | Campaign or official contact information for    | If the element is invalid or not         |
|                    |                                                 |              |              | the candidate.                                  | present, then the implementation is      |
|                    |                                                 |              |              |                                                 | required to ignore it.                   |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| ExternalIdentifier | :ref:`multi-xml-external-identifier`            | Optional     | Repeats      | External identifier(s) linking this candidate   | If the element is invalid or not         |
|                    |                                                 |              |              | to external systems.                            | present, then the implementation is      |
|                    |                                                 |              |              |                                                 | required to ignore it.                   |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| FileDate           | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for office.       | If the field is invalid or not present,  |
|                    |                                                 |              |              |                                                 | then the implementation is required to   |
|                    |                                                 |              |              |                                                 | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| IsIncumbent        | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate currently holds | If the field is invalid or not present,  |
|                    |                                                 |              |              | the office.                                     | then the implementation is required to   |
|                    |                                                 |              |              |                                                 | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| IsTopTicket        | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is at the top   | If the field is invalid or not present,  |
|                    |                                                 |              |              | of a ticket.                                    | then the implementation is required to   |
|                    |                                                 |              |              |                                                 | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| PartyId            | ``xs:IDREF``                                    | Optional     | Single       | References the candidate's affiliated           | If the field is invalid or not present,  |
|                    |                                                 |              |              | :ref:`multi-xml-party`.                         | then the implementation is required to   |
|                    |                                                 |              |              |                                                 | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| PersonId           | ``xs:IDREF``                                    | Optional     | Single       | References the underlying                       | If the field is invalid or not present,  |
|                    |                                                 |              |              | :ref:`multi-xml-person` record.                 | then the implementation is required to   |
|                    |                                                 |              |              |                                                 | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| PostElectionStatus | :ref:`multi-xml-candidate-post-election-status` | Optional     | Single       | Final status of the candidate from              | If the field is invalid or not present,  |
|                    |                                                 |              |              | :ref:`multi-xml-candidate-post-election-status` | then the implementation is required to   |
|                    |                                                 |              |              | (e.g. winner, withdrawn, etc...).               | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+
| PreElectionStatus  | :ref:`multi-xml-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate from       | If the field is invalid or not present,  |
|                    |                                                 |              |              | :ref:`multi-xml-candidate-pre-election-status`  | then the implementation is required to   |
|                    |                                                 |              |              | (e.g. filed, qualified, etc...).                | ignore it.                               |
+--------------------+-------------------------------------------------+--------------+--------------+-------------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Candidate id="can10961">
      <BallotName>
         <Text language="en">Ken T. Cuccinelli II</Text>
      </BallotName>
      <PartyId>par0001</PartyId>
      <PersonId>per10961</PersonId>
   </Candidate>
