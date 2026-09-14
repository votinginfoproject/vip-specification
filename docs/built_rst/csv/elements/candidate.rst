.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-candidate:

candidate
=========

The Candidate object represents a candidate in a contest. If a candidate is running in multiple contests, each contest **must** have its own Candidate object.

+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| Tag                  | Data Type                                       | Required?    | Repeats?     | Description                                      | Error Handling                           |
+======================+=================================================+==============+==============+==================================================+==========================================+
| ballot_name          | :ref:`multi-csv-internationalized-text`         | **Required** | Single       | The candidate's name as it will appear on the    | If the element is invalid, then the      |
|                      |                                                 |              |              | ballot.                                          | implementation is required to ignore the |
|                      |                                                 |              |              |                                                  | ``Candidate`` element containing it.     |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| contact_information  | :ref:`multi-csv-contact-information`            | Optional     | Single       | Campaign or official contact information for the | If the element is invalid or not         |
|                      |                                                 |              |              | candidate.                                       | present, then the implementation is      |
|                      |                                                 |              |              |                                                  | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| external_identifier  | :ref:`multi-csv-external-identifier`            | Optional     | Repeats      | External identifier(s) linking this candidate to | If the element is invalid or not         |
|                      |                                                 |              |              | external systems.                                | present, then the implementation is      |
|                      |                                                 |              |              |                                                  | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| file_date            | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for office.        | If the field is invalid or not present,  |
|                      |                                                 |              |              |                                                  | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| is_incumbent         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate currently holds  | If the field is invalid or not present,  |
|                      |                                                 |              |              | the office.                                      | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| is_top_ticket        | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is at the top of | If the field is invalid or not present,  |
|                      |                                                 |              |              | a ticket.                                        | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| party_id             | ``xs:IDREF``                                    | Optional     | Single       | References the candidate's affiliated            | If the field is invalid or not present,  |
|                      |                                                 |              |              | :ref:`multi-csv-party`.                          | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| person_id            | ``xs:IDREF``                                    | Optional     | Single       | References the underlying                        | If the field is invalid or not present,  |
|                      |                                                 |              |              | :ref:`multi-csv-person` record.                  | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| post_election_status | :ref:`multi-csv-candidate-post-election-status` | Optional     | Single       | Post-election outcome status from                | If the field is invalid or not present,  |
|                      |                                                 |              |              | :ref:`multi-csv-candidate-post-election-status`. | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+
| pre_election_status  | :ref:`multi-csv-candidate-pre-election-status`  | Optional     | Single       | Pre-election qualification status from           | If the field is invalid or not present,  |
|                      |                                                 |              |              | :ref:`multi-csv-candidate-pre-election-status`.  | then the implementation is required to   |
|                      |                                                 |              |              |                                                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+--------------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,ballot_name,file_date,is_incumbent,is_top_ticket,party_id,person_id,post_election_status,pre_election_status
    can001,Jude Fawley,2024-03-01,true,false,par01,per50001,,qualified
