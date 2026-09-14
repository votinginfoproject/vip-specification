.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-office:

Office
======

``Office`` represents an elected or appointed government office associated with an electoral district (e.g. Mayor, Governor, School Board).

+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation    | :ref:`multi-xml-contact-information`    | Optional     | Repeats      | Contact information for the office.      | If the element is invalid or not         |
|                       |                                         |              |              |                                          | present, then the implementation is      |
|                       |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Brief description of the office and its  | If the element is invalid or not         |
|                       |                                         |              |              | responsibilities.                        | present, then the implementation is      |
|                       |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId   | ``xs:IDREF``                            | **Required** | Single       | Links to the                             | If ElectoralDistrictId is invalid or not |
|                       |                                         |              |              | :ref:`multi-xml-electoral-district`      | present, the implementation is required  |
|                       |                                         |              |              | representing the geographical scope of   | to ignore the Office containing it.      |
|                       |                                         |              |              | the office.                              |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier    | :ref:`multi-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                       |                                         |              |              | office to external systems (e.g.         | present, then the implementation is      |
|                       |                                         |              |              | OCD-ID).                                 | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline        | ``xs:date``                             | Optional     | Single       | Filing deadline date for candidates      | If the field is invalid or not present,  |
|                       |                                         |              |              | running for this office.                 | then the implementation is required to   |
|                       |                                         |              |              |                                          | ignore it.                               |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan            | ``xs:boolean``                          | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                       |                                         |              |              | partisan.                                | then the implementation is required to   |
|                       |                                         |              |              |                                          | ignore it.                               |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                  | :ref:`multi-xml-internationalized-text` | **Required** | Single       | Official name of the office.             | If Name is invalid or not present, the   |
|                       |                                         |              |              |                                          | implementation is required to ignore the |
|                       |                                         |              |              |                                          | Office containing it.                    |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonIds | ``xs:IDREFS``                           | Optional     | Single       | References to :ref:`multi-xml-person`    | If the field is invalid or not present,  |
|                       |                                         |              |              | elements for the current office          | then the implementation is required to   |
|                       |                                         |              |              | holder(s).                               | ignore it.                               |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                  | :ref:`multi-xml-term`                   | Optional     | Single       | Defines the term length and dates of the | If the element is invalid or not         |
|                       |                                         |              |              | office.                                  | present, then the implementation is      |
|                       |                                         |              |              |                                          | required to ignore it.                   |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-term:

Term
----

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-office-term-type` | Optional     | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              |                                   |              |              | :ref:`multi-xml-office-term-type` for    | the implementation is required to ignore |
|              |                                   |              |              | valid values).                           | the ``Office`` element containing it.    |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | ``xs:date``                       | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                   |              |              | term of the office.                      | then the implementation is required to   |
|              |                                   |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | ``xs:date``                       | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                   |              |              | term of the office.                      | then the implementation is required to   |
|              |                                   |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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
