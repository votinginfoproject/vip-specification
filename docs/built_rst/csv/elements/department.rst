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


.. _multi-csv-voter-service:

voter_service
-------------

+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                         | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=============================+======================================+==============+==============+==========================================+==========================================+
| description                 | ``xs:string``                        | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                             |                                      |              |              | available.                               | present, then the implementation is      |
|                             |                                      |              |              |                                          | required to ignore it.                   |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_official_person_id | ``xs:IDREF``                         | Optional     | Single       | The :ref:`authority <multi-csv-person>`  | If the field is invalid or not present,  |
|                             |                                      |              |              | for a particular voter service.          | then the implementation is required to   |
|                             |                                      |              |              |                                          | ignore it.                               |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                        | :ref:`multi-csv-voter-service-type`  | Optional     | Single       | The type of :ref:`voter service          | If the field is invalid or not present,  |
|                             |                                      |              |              | <multi-csv-voter-service-type>`.         | then the implementation is required to   |
|                             |                                      |              |              |                                          | ignore it.                               |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                  | ``xs:string``                        | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                             |                                      |              |              | cataloging another type of voter         | then the implementation is required to   |
|                             |                                      |              |              | service.                                 | ignore it.                               |
+-----------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,description,election_official_person_id,type,other_type,department_id
    vs01,A service we provide,per50002,other,overseas-voting,dep01
    vs00,Elections notifications,per50002,other,voter-registration,dep02
    vs02,Pencil sharpening,per50002,other,office-help,dep03
    vs03,Guided hike to polling place,per50002,other,polling-places,dep03
    vs04,Bike messenger ballot delivery,per50002,other,absentee-ballots,dep03


.. _multi-csv-contact-information:

contact_information
-------------------

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`multi-csv-election-administration`, :ref:`multi-csv-office`,
:ref:`multi-csv-person`, :ref:`multi-csv-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+==========================+==============+==============+==========================================+==========================================+
| address_line  | ``xs:string``            | Optional     | Repeats      | The "location" portion of a mailing      | If the field is invalid or not present,  |
|               |                          |              |              | address. :ref:`See usage note.           | then the implementation is required to   |
|               |                          |              |              | <multi-csv-name-address-line-usage>`     | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| directions    | ``xs:string``            | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|               |                          |              |              | locating this entity.                    | present, then the implementation is      |
|               |                          |              |              |                                          | required to ignore it.                   |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| email         | ``xs:string``            | Optional     | Repeats      | An email address for the contact.        | If the field is invalid or not present,  |
|               |                          |              |              |                                          | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| fax           | ``xs:string``            | Optional     | Repeats      | A fax line for the contact.              | If the field is invalid or not present,  |
|               |                          |              |              |                                          | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours         | ``xs:string``            | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
|               |                          |              |              | the location is open *(NB: this element  | present, then the implementation is      |
|               |                          |              |              | is deprecated in favor of the more       | required to ignore it.                   |
|               |                          |              |              | structured :ref:`multi-csv-hours-open`   |                                          |
|               |                          |              |              | element. It is strongly encouraged that  |                                          |
|               |                          |              |              | data providers move toward contributing  |                                          |
|               |                          |              |              | hours in this format)*.                  |                                          |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_id | ``xs:IDREF``             | Optional     | Single       | References an                            | If the field is invalid or not present,  |
|               |                          |              |              | :ref:`multi-csv-hours-open` element,     | then the implementation is required to   |
|               |                          |              |              | which lists the hours of operation for a | ignore it.                               |
|               |                          |              |              | location.                                |                                          |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| lat_long      | :ref:`multi-csv-lat-lng` | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|               |                          |              |              | this entity.                             | present, then the implementation is      |
|               |                          |              |              |                                          | required to ignore it.                   |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name          | ``xs:string``            | Optional     | Single       | The name of the location or contact.     | If the field is invalid or not present,  |
|               |                          |              |              | :ref:`See usage note.                    | then the implementation is required to   |
|               |                          |              |              | <multi-csv-name-address-line-usage>`     | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| phone         | ``xs:string``            | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|               |                          |              |              |                                          | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| uri           | ``xs:anyURI``            | Optional     | Repeats      | An informational URI for the contact or  | If the field is invalid or not present,  |
|               |                          |              |              | location.                                | then the implementation is required to   |
|               |                          |              |              |                                          | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| parent_id     | ``xs:IDREF``             | Optional     | Repeats      | A reference to a record in source,       | If the field is invalid or not present,  |
|               |                          |              |              | department, voter_service, candidate,    | then the implementation is required to   |
|               |                          |              |              | person, or office.                       | ignore it.                               |
+---------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,address_line_1,address_line_2,address_line_3,directions,email,fax,hours,hours_open_id,latitude,longitude,latlng_source,name,phone,uri,parent_id
    ci0827,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,off001
    ci0828,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,vs01
