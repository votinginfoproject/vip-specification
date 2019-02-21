.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-office:

office
======

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+======================================+==============+==============+==========================================+==========================================+
| contact_information      | :ref:`multi-csv-contact-information` | Optional     | Repeats      | Specifies the contact information for    | If the element is invalid or not         |
|                          |                                      |              |              | the office and/or individual holding the | present, then the implementation is      |
|                          |                                      |              |              | office.                                  | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description              | ``xs:string``                        | Optional     | Single       | A brief description of the office and    | If the element is invalid or not         |
|                          |                                      |              |              | its purpose.                             | present, then the implementation is      |
|                          |                                      |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                         | **Required** | Single       | Links to the                             | If the field is invalid or not present,  |
|                          |                                      |              |              | :ref:`multi-csv-electoral-district`      | the implementation is required to ignore |
|                          |                                      |              |              | element associated with the office.      | the ``Office`` element containing it.    |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:IDREF``                         | Optional     | Single       | Other identifiers that link this office  | If the element is invalid or not         |
|                          |                                      |              |              | to other related datasets (e.g. campaign | present, then the implementation is      |
|                          |                                      |              |              | finance systems, OCD IDs, et al.).       | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| filing_deadline          | ``xs:date``                          | Optional     | Single       | Specifies the date and time when a       | If the field is invalid or not present,  |
|                          |                                      |              |              | candidate must have filed for the        | then the implementation is required to   |
|                          |                                      |              |              | contest for the office.                  | ignore it.                               |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_partisan              | ``xs:boolean``                       | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                          |                                      |              |              | partisan.                                | then the implementation is required to   |
|                          |                                      |              |              |                                          | ignore it.                               |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                        | **Required** | Single       | The name of the office.                  | If the field is invalid or not present,  |
|                          |                                      |              |              |                                          | the implementation is required to ignore |
|                          |                                      |              |              |                                          | the ``Office`` element containing it.    |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_holder_person_ids | ``xs:IDREFS``                        | Optional     | Single       | Links to the :ref:`multi-csv-person`     | If the field is invalid or not present,  |
|                          |                                      |              |              | element(s) that hold additional          | then the implementation is required to   |
|                          |                                      |              |              | information about the current office     | ignore it.                               |
|                          |                                      |              |              | holder(s).                               |                                          |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term                     | :ref:`multi-csv-term`                | Optional     | Single       | Defines the term the office can be held. | If the element is invalid or not         |
|                          |                                      |              |              |                                          | present, then the implementation is      |
|                          |                                      |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,electoral_district_id,external_identifier_type,external_identifier_othertype,external_identifier_value,filing_deadline,is_partisan,name,office_holder_person_ids,term_type,term_start_date,term_end_date
    off001,ed001,,,,,true,Deputy Chief of Staff,per50003,full-term,2002-01-21,
    off002,ed001,,,,,true,Deputy Deputy Chief of Staff,per50001,unexpired-term,2002-01-21,
    off003,ed001,,,,,false,General Secretary of Secretaries,per50004,full-term,2002-01-21,


.. _multi-csv-term:

term
----

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| type         | :ref:`multi-csv-office-term-type` | Optional     | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              |                                   |              |              | :ref:`multi-csv-office-term-type` for    | the implementation is required to ignore |
|              |                                   |              |              | valid values).                           | the ``Office`` element containing it.    |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| start_date   | ``xs:date``                       | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                   |              |              | term of the office.                      | then the implementation is required to   |
|              |                                   |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| end_date     | ``xs:date``                       | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                   |              |              | term of the office.                      | then the implementation is required to   |
|              |                                   |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


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

.. code-block:: csv-table
   :linenos:


    id,address_line_1,address_line_2,address_line_3,directions,email,fax,hours,hours_open_id,latitude,longitude,latlng_source,name,phone,uri,parent_id
    ci0827,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,off001
    ci0828,The White House,1600 Pennsylvania Ave,,,josh@example.com,,Early to very late,,,,,Josh Lyman,555-111-2222,http://lemonlyman.example.com,vs01
