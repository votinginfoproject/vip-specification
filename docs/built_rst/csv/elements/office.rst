.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-office:

office
======

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================+==============+==============+==========================================+==========================================+
| description              | ``xs:string``         | Optional     | Single       | A brief description of the office and    | If the element is invalid or not         |
|                          |                       |              |              | its purpose.                             | present, then the implementation is      |
|                          |                       |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``          | **Required** | Single       | Links to the                             | If the field is invalid or not present,  |
|                          |                       |              |              | :ref:`multi-csv-electoral-district`      | the implementation is required to ignore |
|                          |                       |              |              | element associated with the office.      | the ``Office`` element containing it.    |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:IDREF``          | Optional     | Single       | Other identifiers that link this office  | If the element is invalid or not         |
|                          |                       |              |              | to other related datasets (e.g. campaign | present, then the implementation is      |
|                          |                       |              |              | finance systems, OCD IDs, et al.).       | required to ignore it.                   |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| filing_deadline          | ``xs:date``           | Optional     | Single       | Specifies the date and time when a       | If the field is invalid or not present,  |
|                          |                       |              |              | candidate must have filed for the        | then the implementation is required to   |
|                          |                       |              |              | contest for the office.                  | ignore it.                               |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_partisan              | ``xs:boolean``        | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                          |                       |              |              | partisan.                                | then the implementation is required to   |
|                          |                       |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``         | **Required** | Single       | The name of the office.                  | If the field is invalid or not present,  |
|                          |                       |              |              |                                          | the implementation is required to ignore |
|                          |                       |              |              |                                          | the ``Office`` element containing it.    |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_holder_person_ids | ``xs:IDREFS``         | Optional     | Single       | Links to the :ref:`multi-csv-person`     | If the field is invalid or not present,  |
|                          |                       |              |              | element(s) that hold additional          | then the implementation is required to   |
|                          |                       |              |              | information about the current office     | ignore it.                               |
|                          |                       |              |              | holder(s).                               |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term                     | :ref:`multi-csv-term` | Optional     | Single       | Defines the term the office can be held. | If the element is invalid or not         |
|                          |                       |              |              |                                          | present, then the implementation is      |
|                          |                       |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,electoral_district_id,external_identifier_type,external_identifier_othertype,external_identifier_value,filing_deadline,is_partisan,name,office_holder_person_ids,term_type,term_start_date,term_end_date
    off001,ed001,,,,,true,Deputy Chief of Staff,per50003,full-term,2002-01-21,
    off002,ed001,,,,,true,Deputy Deputy Chief of Staff,per50001,unexpired-term,2002-01-21,
    off003,ed001,,,,,false,General Secretary of Secretaries,per50004,full-term,2002-01-21,
