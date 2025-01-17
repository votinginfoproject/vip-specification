.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-voter-service:

voter_service
=============

+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+======================================+==============+==============+==========================================+==========================================+
| description                 | ``xs:string``                        | Optional     | Single       | Long description of the services         |                                          |
|                             |                                      |              |              | available.                               |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_official_person_id | ``xs:IDREF``                         | Optional     | Single       | The :ref:`authority <multi-csv-person>`  |                                          |
|                             |                                      |              |              | for a particular voter service.          |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                        | :ref:`multi-csv-voter-service-type`  | Optional     | Single       | The type of :ref:`voter service          |                                          |
|                             |                                      |              |              | <multi-csv-voter-service-type>`.         |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                  | ``xs:string``                        | Optional     | Single       | If Type is "other", OtherType allows for |                                          |
|                             |                                      |              |              | cataloging another type of voter         |                                          |
|                             |                                      |              |              | service.                                 |                                          |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,description,election_official_person_id,type,other_type,department_id
    vs01,A service we provide,per50002,other,overseas-voting,dep01
    vs00,Elections notifications,per50002,other,voter-registration,dep02
    vs02,Pencil sharpening,per50002,other,office-help,dep03
    vs03,Guided hike to polling place,per50002,other,polling-places,dep03
    vs04,Bike messenger ballot delivery,per50002,other,absentee-ballots,dep03
