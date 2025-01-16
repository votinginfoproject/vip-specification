.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-office:

office
======

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================+==============+==============+==========================================+==========================================+
| description              | ``xs:string``         | Optional     | Single       | A brief description of the office and    |                                          |
|                          |                       |              |              | its purpose.                             |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``          | **Required** | Single       | Links to the                             |                                          |
|                          |                       |              |              | :ref:`multi-csv-electoral-district`      |                                          |
|                          |                       |              |              | element associated with the office.      |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:IDREF``          | Optional     | Single       | Other identifiers that link this office  |                                          |
|                          |                       |              |              | to other related datasets (e.g. campaign |                                          |
|                          |                       |              |              | finance systems, OCD IDs, et al.).       |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| filing_deadline          | ``xs:date``           | Optional     | Single       | Specifies the date and time when a       |                                          |
|                          |                       |              |              | candidate must have filed for the        |                                          |
|                          |                       |              |              | contest for the office.                  |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_partisan              | ``xs:boolean``        | Optional     | Single       | Indicates whether the office is          |                                          |
|                          |                       |              |              | partisan.                                |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``         | **Required** | Single       | The name of the office.                  |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_holder_person_ids | ``xs:IDREFS``         | Optional     | Single       | Links to the :ref:`multi-csv-person`     |                                          |
|                          |                       |              |              | element(s) that hold additional          |                                          |
|                          |                       |              |              | information about the current office     |                                          |
|                          |                       |              |              | holder(s).                               |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term                     | :ref:`multi-csv-term` | Optional     | Single       | Defines the term the office can be held. |                                          |
+--------------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,electoral_district_id,external_identifier_type,external_identifier_othertype,external_identifier_value,filing_deadline,is_partisan,name,office_holder_person_ids,term_type,term_start_date,term_end_date
    off001,ed001,,,,,true,Deputy Chief of Staff,per50003,full-term,2002-01-21,
    off002,ed001,,,,,true,Deputy Deputy Chief of Staff,per50001,unexpired-term,2002-01-21,
    off003,ed001,,,,,false,General Secretary of Secretaries,per50004,full-term,2002-01-21,
