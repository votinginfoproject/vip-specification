.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-department:

department
==========

+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+======================================+==============+==============+==========================================+==========================================+
| election_official_person_id | ``xs:IDREF``                         | Optional     | Single       | The individual to contact at the         |                                          |
|                             |                                      |              |              | election administration office. The      |                                          |
|                             |                                      |              |              | specified person should be the           |                                          |
|                             |                                      |              |              | :ref:`election official                  |                                          |
|                             |                                      |              |              | <multi-csv-person>`.                     |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| voter_service               | :ref:`multi-csv-voter-service`       | Optional     | Repeats      | The types of services and appropriate    |                                          |
|                             |                                      |              |              | contact individual available to voters.  |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_administration_id  | ``xs:IDREF``                         | Optional     | Single       | The election administration that the     |                                          |
|                             |                                      |              |              | department is a part of.                 |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_official_person_id,election_administration_id
    dep01,per50002,ea123
    dep02,per50002,ea345
    dep03,per50002,ea625
    dep04,per50002,ea625
