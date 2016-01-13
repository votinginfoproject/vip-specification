.. This file is auto-generated.  Do not edit it by hand!

.. _xml-multi-office:

Office
======

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=================================================+==============+==============+==========================================+==========================================+
| ContactInformation   | :doc:`ContactInformation <contact_information>` | Optional     | Repeats      | Specifies the contact information for    | If the element is invalid or not         |
|                      |                                                 |              |              | the office and/or individual holding the | present, then the implementation is      |
|                      |                                                 |              |              | office.                                  | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId  | xs:IDREF                                        | **Required** | Single       | Links to the :doc:`ElectoralDistrict     | If the field is invalid or not present,  |
|                      |                                                 |              |              | <electoral_district>` element associated | the implementation is required to ignore |
|                      |                                                 |              |              | with the office.                         | the ``Office`` element containing it.    |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers that link this office  | If the element is invalid or not         |
|                      | </built_rst/xml/elements/external_identifiers>` |              |              | to other related datasets (e.g. campaign | present, then the implementation is      |
|                      |                                                 |              |              | finance systems, OCD IDs, et al.).       | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline       | xs:date                                         | Optional     | Single       | Specifies the date and time when a       | If the field is invalid or not present,  |
|                      |                                                 |              |              | candidate must have filed for the        | then the implementation is required to   |
|                      |                                                 |              |              | contest for the office.                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan           | xs:boolean                                      | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                      |                                                 |              |              | partisan.                                | then the implementation is required to   |
|                      |                                                 |              |              |                                          | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | :doc:`InternationalizedText                     | **Required** | Single       | The name of the office.                  | If the field is invalid or not present,  |
|                      | <internationalized_text>`                       |              |              |                                          | the implementation is required to ignore |
|                      |                                                 |              |              |                                          | the ``Office`` element containing it.    |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonId | xs:IDREF                                        | Optional     | Repeats      | Links to the :doc:`Person <person>`      | If the field is invalid or not present,  |
|                      |                                                 |              |              | element(s) that hold additional          | then the implementation is required to   |
|                      |                                                 |              |              | information about the current office     | ignore it.                               |
|                      |                                                 |              |              | holder(s).                               |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                 | `Term`_                                         | Optional     | Single       | Defines the term the office can be held. | If the element is invalid or not         |
|                      |                                                 |              |              |                                          | present, then the implementation is      |
|                      |                                                 |              |              |                                          | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _xml-multi-term:

Term
----

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`OfficeTermType                | **Required** | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              | <../enumerations/office_term_type>` |              |              | :doc:`OfficeTermType                     | the implementation is required to ignore |
|              |                                     |              |              | <../enumerations/office_term_type>` for  | the ``Office`` element containing it.    |
|              |                                     |              |              | valid values).                           |                                          |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | xs:date                             | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | then the implementation is required to   |
|              |                                     |              |              |                                          | ignore it.                               |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | xs:date                             | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | then the implementation is required to   |
|              |                                     |              |              |                                          | ignore it.                               |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Office id="off0000">
     <ElectoralDistrictId>ed60129</ElectoralDistrictId>
     <FilingDeadline>2013-01-01</FilingDeadline>
     <IsPartisan>false</IsPartisan>
     <Name>
       <Text language="en">Governor</Text>
     </Name>
     <Term>
       <Type>full-term</Type>
     </Term>
   </Office>
