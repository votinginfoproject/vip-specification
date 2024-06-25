.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-department:

department
==========

+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+======================================+==============+==============+==========================================+==========================================+
| election_official_person_id | ``xs:IDREF``                         | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                             |                                      |              |              | election administration office. The      | then the implementation is required to   |
|                             |                                      |              |              | specified person should be the           | ignore it.                               |
|                             |                                      |              |              | :ref:`election official                  |                                          |
|                             |                                      |              |              | <multi-csv-person>`.                     |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| voter_service               | :ref:`multi-csv-voter-service`       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                             |                                      |              |              | contact individual available to voters.  | present, then the implementation is      |
|                             |                                      |              |              |                                          | required to ignore it.                   |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_administration_id  | ``xs:IDREF``                         | Optional     | Single       | The election administration that the     | If the field is invalid or not present,  |
|                             |                                      |              |              | department is a part of.                 | then the implementation is required to   |
|                             |                                      |              |              |                                          | ignore it.                               |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_official_person_id,election_administration_id
    dep01,per50002,ea123
    dep02,per50002,ea345
    dep03,per50002,ea625
    dep04,per50002,ea625
