.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-candidate:

candidate
=========

The Candidate object represents a candidate in a contest. If a candidate is
running in multiple contests, each contest **must** have its own Candidate
object. Candidate objects may **not** be reused between Contests.

+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=================================================+==============+==============+==========================================+==========================================+
| ballot_name          | ``xs:string``                                   | **Required** | Single       | The candidate's name as it will be       |                                          |
|                      |                                                 |              |              | displayed on the official ballot (e.g.   |                                          |
|                      |                                                 |              |              | "Ken T. Cuccinelli II").                 |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`multi-csv-external-identifiers`           | Optional     | Single       | Another identifier for a candidate that  |                                          |
|                      |                                                 |              |              | links to another source of information   |                                          |
|                      |                                                 |              |              | (e.g. a campaign committee ID that links |                                          |
|                      |                                                 |              |              | to a campaign finance system).           |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_date            | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for the    |                                          |
|                      |                                                 |              |              | contest.                                 |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_incumbent         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   |                                          |
|                      |                                                 |              |              | incumbent for the office associated with |                                          |
|                      |                                                 |              |              | the contest.                             |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_top_ticket        | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   |                                          |
|                      |                                                 |              |              | top of a ticket that includes multiple   |                                          |
|                      |                                                 |              |              | candidates.                              |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id             | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-csv-party`    |                                          |
|                      |                                                 |              |              | element with additional information      |                                          |
|                      |                                                 |              |              | about the candidate's affiliated party.  |                                          |
|                      |                                                 |              |              | This is the party affiliation that is    |                                          |
|                      |                                                 |              |              | intended to be presented as part of      |                                          |
|                      |                                                 |              |              | ballot information.                      |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| person_id            | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-csv-person`   |                                          |
|                      |                                                 |              |              | element with additional information      |                                          |
|                      |                                                 |              |              | about the candidate.                     |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| post_election_status | :ref:`multi-csv-candidate-post-election-status` | Optional     | Single       | Final status of the candidate (e.g.      |                                          |
|                      |                                                 |              |              | winner, withdrawn, etc...).              |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pre_election_status  | :ref:`multi-csv-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate     |                                          |
|                      |                                                 |              |              | (e.g. filed, qualified, etc...).         |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_name,external_identifier_type,external_identifier_othertype,external_identifier_value,file_date,is_incumbent,is_top_ticket,party_id,person_id,post_election_status,pre_election_status
    can001,Jude Fawley,,,,2016-12-01,true,false,par01,per50001,,filed
    can002,Arabella Donn,,,,2016-12-01,false,false,par02,per50002,,qualified
    can003,John Coltrane,,,,2016-09-23,false,false,par02,per50003,,qualified
    can004,Miles Davis,,,,2016-05-26,false,false,par01,per50004,,qualified
