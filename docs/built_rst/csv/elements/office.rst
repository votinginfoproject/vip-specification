.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-office:

office
======

``Office`` represents an elected or appointed government office associated with an electoral district (e.g. Mayor, Governor, School Board).

+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=========================================+==============+==============+==========================================+==========================================+
| contact_information      | :ref:`multi-csv-contact-information`    | Optional     | Repeats      | Contact information for the office.      | If the element is invalid or not         |
|                          |                                         |              |              |                                          | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| description              | :ref:`multi-csv-internationalized-text` | Optional     | Single       | Brief description of the office and its  | If the element is invalid or not         |
|                          |                                         |              |              | responsibilities.                        | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                            | **Required** | Single       | Links to the                             | If ElectoralDistrictId is invalid or not |
|                          |                                         |              |              | :ref:`multi-csv-electoral-district`      | present, the implementation is required  |
|                          |                                         |              |              | representing the geographical scope of   | to ignore the Office containing it.      |
|                          |                                         |              |              | the office.                              |                                          |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier      | :ref:`multi-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                          |                                         |              |              | office to external systems (e.g.         | present, then the implementation is      |
|                          |                                         |              |              | OCD-ID).                                 | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| filing_deadline          | ``xs:date``                             | Optional     | Single       | Filing deadline date for candidates      | If the field is invalid or not present,  |
|                          |                                         |              |              | running for this office.                 | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_partisan              | ``xs:boolean``                          | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                          |                                         |              |              | partisan.                                | then the implementation is required to   |
|                          |                                         |              |              |                                          | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | :ref:`multi-csv-internationalized-text` | **Required** | Single       | Official name of the office.             | If Name is invalid or not present, the   |
|                          |                                         |              |              |                                          | implementation is required to ignore the |
|                          |                                         |              |              |                                          | Office containing it.                    |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_holder_person_ids | ``xs:IDREFS``                           | Optional     | Single       | References to :ref:`multi-csv-person`    | If the field is invalid or not present,  |
|                          |                                         |              |              | elements for the current office          | then the implementation is required to   |
|                          |                                         |              |              | holder(s).                               | ignore it.                               |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| term                     | :ref:`multi-csv-term`                   | Optional     | Single       | Defines the term length and dates of the | If the element is invalid or not         |
|                          |                                         |              |              | office.                                  | present, then the implementation is      |
|                          |                                         |              |              |                                          | required to ignore it.                   |
+--------------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,electoral_district_id,filing_deadline,is_partisan,name,office_holder_person_ids,term_type,term_start_date,term_end_date
    off001,ed001,2024-06-01,true,Governor,per50001,full-term,2022-01-15,2026-01-15
