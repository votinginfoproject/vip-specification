Candidate
=========

The Candidate object represents a candidate in a contest. If a candidate is running in multiple contests, the same
Candidate object may be used.
   
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| Tag                 | Data Type                                       | Required?    | Repeats? | Description          | Error Handling       |
|                     |                                                 |              |          |                      |                      |
+=====================+=================================================+==============+==========+======================+======================+
| BallotName          |:doc:`InternationalizedText                      | **Required** | Single   |The candidate's name  |If the element is     |
|                     |<internationalized_text>`                        |              |          |as it will be         |invalid or not        |
|                     |                                                 |              |          |displayed on the      |present, then the     |
|                     |                                                 |              |          |official ballot       |implementation is     |
|                     |                                                 |              |          |(e.g. "Ken            |required to ignore the|
|                     |                                                 |              |          |T. Cuccinelli II").   |Candidate element     |
|                     |                                                 |              |          |                      |containing it.        |
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| ExternalIdentifiers |:doc:`ExternalIdentifiers                        | Optional     | Single   |Another identifier for|If the element is     |
|                     |<external_identifiers>`                          |              |          |a candidate that links|invalid or not        |
|                     |                                                 |              |          |to another source of  |present, then the     |
|                     |                                                 |              |          |information (e.g. a   |implementation is     |
|                     |                                                 |              |          |campaign committee ID |required to ignore it.|
|                     |                                                 |              |          |that links to a       |                      |
|                     |                                                 |              |          |campaign finance      |                      |
|                     |                                                 |              |          |system).              |                      |
|                     |                                                 |              |          |                      |                      |
|                     |                                                 |              |          |                      |                      |
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| FileDate            |xs:dateTime                                      | Optional     | Single   |Date and time when the|If the field is       |
|                     |                                                 |              |          |candidate filed for   |invalid or not        |
|                     |                                                 |              |          |the contest.          |present, then the     |
|                     |                                                 |              |          |                      |implementation is     |
|                     |                                                 |              |          |                      |required to ignore it.|
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| IsIncumbent         |xs:boolean                                       | Optional     | Single   |Indicates whether the |If the field is       |
|                     |                                                 |              |          |candidate is the      |invalid or not        |
|                     |                                                 |              |          |incumbent for the     |present, then the     |
|                     |                                                 |              |          |office associated with|implementation is     |
|                     |                                                 |              |          |the contest.          |required to ignore it.|
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| IsTopTicket         |xs:boolean                                       | Optional     | Single   |Indicates whether the |If the field is       |
|                     |                                                 |              |          |candidate is the top  |invalid or not        |
|                     |                                                 |              |          |of a ticket that      |present, then the     |
|                     |                                                 |              |          |includes multiple     |implementation is     |
|                     |                                                 |              |          |candidates.           |required to ignore it.|
|                     |                                                 |              |          |                      |                      |
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| PartyId             |xs:IDREF                                         | Optional     | Single   |Reference to a        |If the field is       |
|                     |                                                 |              |          |:doc:`Party <party>`  |invalid or not        |
|                     |                                                 |              |          |element with          |present, then the     |
|                     |                                                 |              |          |additional information|implementation is     |
|                     |                                                 |              |          |about the candidate's |required to ignore it.|
|                     |                                                 |              |          |affiliated party.     |                      |
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| PersonId            |xs:IDREF                                         | Optional     | Single   |Reference to a        |If the field is       |
|                     |                                                 |              |          |:doc:`Person <person>`|invalid or not        |
|                     |                                                 |              |          |element with          |present, then the     |
|                     |                                                 |              |          |additional information|implementation is     |
|                     |                                                 |              |          |about the candidate.  |required to ignore it.|
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| PostElectionStatus  |:doc:`CandidatePostElectionStatus                | Optional     | Single   |Final status of the   |If the field is       |
|                     |<../enumerations/candidate_post_election_status>`|              |          |candidate (e.g.       |invalid or not        |
|                     |                                                 |              |          |winner, withdrawn,    |present, then the     |
|                     |                                                 |              |          |etc...).              |implementation is     |
|                     |                                                 |              |          |                      |required to ignore it.|
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| PreElectionStatus   |:doc:`CandidatePreElectionStatus                 | Optional     | Single   |Registration status of|If the field is       |
|                     |<../enumerations/candidate_pre_election_status>` |              |          |the candidate (e.g.   |invalid or not        |
|                     |                                                 |              |          |filed, qualified,     |present, then the     |
|                     |                                                 |              |          |etc...).              |implementation is     |
|                     |                                                 |              |          |                      |required to ignore it.|
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+
| SequenceOrder       |xs:integer                                       | Optional     | Single   |The order in which the|If the field is       |
|                     |                                                 |              |          |candidate can be      |invalid or not        |
|                     |                                                 |              |          |listed on the ballot  |present, then the     |
|                     |                                                 |              |          |or in results.        |implementation is     |
|                     |                                                 |              |          |                      |required to ignore it.|
+---------------------+-------------------------------------------------+--------------+----------+----------------------+----------------------+

.. code-block:: xml
   :linenos:

   <Candidate id="can10961">
      <BallotName>
        <Text language="en">Ken T. Cuccinelli II</Text>
      </BallotName>
      <PartyId>par0001</PartyId>
      <PersonId>per10961</PersonId>
   </Candidate>
