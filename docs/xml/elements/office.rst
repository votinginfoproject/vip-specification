Office
======

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| Tag                  | Data Type                 | Required?  | Repeats? |Description            |Error Handling              |
|                      |                           |            |          |                       |                            |
+======================+===========================+============+==========+=======================+============================+
| ContactInformation   |:doc:`ContactInformation   | Optional   | Repeats  |Specifies the contact  |If the element is invalid or|
|                      |<contact_information>`     |            |          |information for the    |not present, the            |
|                      |                           |            |          |office and/or          |implementation is required  |
|                      |                           |            |          |individual holding the |to ignore it.               |
|                      |                           |            |          |office.                |                            |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| ElectoralDistrictId  | xs:IDREF                  |**Required**| Single   |Links to the           |If the field is invalid or  |
|                      |                           |            |          |:doc:`ElectoralDistrict|not present, the            |
|                      |                           |            |          |<electoral_district>`  |implementation is required  |
|                      |                           |            |          |element associated with|to ignore the ``Office``    |
|                      |                           |            |          |the office.            |element containing it.      |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| ExternalIdentifiers  |:doc:`ExternalIdentifiers  | Optional   | Single   |Other identifiers that |If the element is invalid or|
|                      |<external_identifiers>`    |            |          |link this office to    |not present, the            |
|                      |                           |            |          |other related datasets |implementation is required  |
|                      |                           |            |          |(e.g. campaign finance |to ignore it.               |
|                      |                           |            |          |systems, OCD IDs, et   |                            |
|                      |                           |            |          |al.).                  |                            |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| FilingDeadline       | xs:date                   | Optional   | Single   |Specifies the date and |If the field is invalid or  |
|                      |                           |            |          |time when a candidate  |not present, the            |
|                      |                           |            |          |must have filed for the|implementation is required  |
|                      |                           |            |          |contest for the office.|to ignore it.               |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| IsPartisan           | xs:boolean                | Optional   | Single   |Indicates whether the  |If the field is invalid or  |
|                      |                           |            |          |office is partisan.    |not present, the            |
|                      |                           |            |          |                       |implementation is required  |
|                      |                           |            |          |                       |to ignore it.               |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| Name                 |:doc:`InternationalizedText|**Required**| Single   |The name of the office.|If the field is invalid or  |
|                      |<internationalized_text>`  |            |          |                       |not present, the            |
|                      |                           |            |          |                       |implementation is required  |
|                      |                           |            |          |                       |to ignore the ``Office``    |
|                      |                           |            |          |                       |element containing it.      |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| OfficeHolderPersonId | xs:IDREF                  | Optional   | Repeats  |Links to the           |If the field is invalid or  |
|                      |                           |            |          |:doc:`Person <person>` |not present, the            |
|                      |                           |            |          |element(s) that hold   |implementation is required  |
|                      |                           |            |          |additional information |to ignore it.               |
|                      |                           |            |          |about the current      |                            |
|                      |                           |            |          |office holder(s).      |                            |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+
| Term                 |`Term`_                    | Optional   | Single   |Defines the term the   |If the element is invalid or|
|                      |                           |            |          |office can be held.    |not present, the            |
|                      |                           |            |          |                       |implementation is required  |
|                      |                           |            |          |                       |to ignore it.               |
+----------------------+---------------------------+------------+----------+-----------------------+----------------------------+

Term
----

+-----------+-----------------------------------+------------+----------+-----------------------------------+----------------------------+
| Tag       | Data Type                         | Required?  | Repeats? |Description                        |Error Handling              |
|           |                                   |            |          |                                   |                            |
+===========+===================================+============+==========+===================================+============================+
| Type      |:doc:`OfficeTermType               |**Required**| Single   |Specifies the type of office term  |If the field is invalid or  |
|           |<../enumerations/office_term_type>`|            |          |(see :doc:`OfficeTermType          |not present, the            |
|           |                                   |            |          |<../enumerations/office_term_type>`|implementation is required  |
|           |                                   |            |          |for valid values).                 |to ignore the ``Office``    |
|           |                                   |            |          |                                   |element containing it.      |
+-----------+-----------------------------------+------------+----------+-----------------------------------+----------------------------+
| StartDate | xs:date                           | Optional   | Single   |Specifies the start date for the   |If the field is invalid or  |
|           |                                   |            |          |current term of the office.        |not present, the            |
|           |                                   |            |          |                                   |implementation is required  |
|           |                                   |            |          |                                   |to ignore it.               |
+-----------+-----------------------------------+------------+----------+-----------------------------------+----------------------------+
| EndDate   | xs:date                           | Optional   | Single   |Specifies the end date for the     |If the field is invalid or  |
|           |                                   |            |          |current term of the office.        |not present, the            |
|           |                                   |            |          |                                   |implementation is required  |
|           |                                   |            |          |                                   |to ignore it.               |
+-----------+-----------------------------------+------------+----------+-----------------------------------+----------------------------+

.. code-block:: xml
   :linenos:

   <Office id="off0000">
     <ElectoralDistrictId>ed60129</ElectoralDistrictId>
     <FilingDeadline>1900-01-01</FilingDeadline>
     <IsPartisan>false</IsPartisan>
     <Name>
       <Text language="en">Governor</Text>
     </Name>
     <Term>
       <Type>full-term</Type>
     </Term>
   </Office>
