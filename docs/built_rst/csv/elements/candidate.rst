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
| ballot_name          | ``xs:string``                                   | **Required** | Single       | The candidate's name as it will be       | If the element is invalid or not         |
|                      |                                                 |              |              | displayed on the official ballot (e.g.   | present, then the implementation is      |
|                      |                                                 |              |              | "Ken T. Cuccinelli II").                 | required to ignore the Candidate element |
|                      |                                                 |              |              |                                          | containing it.                           |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| contact_information  | ``xs:string``                                   | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                      |                                                 |              |              | for this Candidate and/or their campaign | present, then the implementation is      |
|                      |                                                 |              |              | (see                                     | required to ignore it.                   |
|                      |                                                 |              |              | :ref:`multi-csv-contact-information`).   |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`multi-csv-external-identifiers`           | Optional     | Single       | Another identifier for a candidate that  | If the element is invalid or not         |
|                      |                                                 |              |              | links to another source of information   | present, then the implementation is      |
|                      |                                                 |              |              | (e.g. a campaign committee ID that links | required to ignore it.                   |
|                      |                                                 |              |              | to a campaign finance system).           |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| file_date            | ``xs:date``                                     | Optional     | Single       | Date when the candidate filed for the    | If the field is invalid or not present,  |
|                      |                                                 |              |              | contest.                                 | then the implementation is required to   |
|                      |                                                 |              |              |                                          | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_incumbent         | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                      |                                                 |              |              | incumbent for the office associated with | then the implementation is required to   |
|                      |                                                 |              |              | the contest.                             | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_top_ticket        | ``xs:boolean``                                  | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                      |                                                 |              |              | top of a ticket that includes multiple   | then the implementation is required to   |
|                      |                                                 |              |              | candidates.                              | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_id             | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-csv-party`    | If the field is invalid or not present,  |
|                      |                                                 |              |              | element with additional information      | then the implementation is required to   |
|                      |                                                 |              |              | about the candidate's affiliated party.  | ignore it.                               |
|                      |                                                 |              |              | This is the party affiliation that is    |                                          |
|                      |                                                 |              |              | intended to be presented as part of      |                                          |
|                      |                                                 |              |              | ballot information.                      |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| person_id            | ``xs:IDREF``                                    | Optional     | Single       | Reference to a :ref:`multi-csv-person`   | If the field is invalid or not present,  |
|                      |                                                 |              |              | element with additional information      | then the implementation is required to   |
|                      |                                                 |              |              | about the candidate.                     | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| post_election_status | :ref:`multi-csv-candidate-post-election-status` | Optional     | Single       | Final status of the candidate (e.g.      | If the field is invalid or not present,  |
|                      |                                                 |              |              | winner, withdrawn, etc...).              | then the implementation is required to   |
|                      |                                                 |              |              |                                          | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| pre_election_status  | :ref:`multi-csv-candidate-pre-election-status`  | Optional     | Single       | Registration status of the candidate     | If the field is invalid or not present,  |
|                      |                                                 |              |              | (e.g. filed, qualified, etc...).         | then the implementation is required to   |
|                      |                                                 |              |              |                                          | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,ballot_name,external_identifier_type,external_identifier_othertype,external_identifier_value,file_date,is_incumbent,is_top_ticket,party_id,person_id,post_election_status,pre_election_status
    can001,Jude Fawley,,,,2016-12-01,true,false,par01,per50001,,filed
    can002,Arabella Donn,,,,2016-12-01,false,false,par02,per50002,,qualified
    can003,John Coltrane,,,,2016-09-23,false,false,par02,per50003,,qualified
    can004,Miles Davis,,,,2016-05-26,false,false,par01,per50004,,qualified


.. _multi-csv-external-identifiers:

external_identifiers
--------------------

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-csv-candidate`

* Any element that extends :ref:`multi-csv-contest-base`

* :ref:`multi-csv-electoral-district`

* :ref:`multi-csv-locality`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-precinct`

* :ref:`multi-csv-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+---------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+======================================+==============+==============+==========================================+==========================================+
| external_identifier | :ref:`multi-csv-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                     |                                      |              |              | identifier it is (see                    | must be present for                      |
|                     |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                     |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                     |                                      |              |              |                                          | present, the implementation is required  |
|                     |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                     |                                      |              |              |                                          | element.                                 |
+---------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-external-identifier:

external_identifier
~~~~~~~~~~~~~~~~~~~

+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================+==============+==============+==========================================+==========================================+
| type         | ``identifier_type`` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                     |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                     |              |              |                                          | it.                                      |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``       | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                     |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                     |              |              | outside the options listed in            | ignore it.                               |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        |                                          |
|              |                     |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                     |              |              | using this field.                        |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``       | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                     |              |              |                                          | the implementation is required to ignore |
|              |                     |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                     |              |              |                                          | it.                                      |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
