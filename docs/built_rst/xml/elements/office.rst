.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-office:

Office
======

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                   | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=======================+=========================================+==============+==============+==========================================+==========================================+
| ContactInformation    | :ref:`multi-xml-contact-information`    | Optional     | Repeats      | Links to the                             |                                          |
|                       |                                         |              |              | :ref:`multi-xml-contact-information`     |                                          |
|                       |                                         |              |              | element associated with the office.      |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description           | :ref:`multi-xml-internationalized-text` | Optional     | Single       | A brief description of the office and    |                                          |
|                       |                                         |              |              | its purpose.                             |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId   | ``xs:IDREF``                            | **Required** | Single       | Links to the                             |                                          |
|                       |                                         |              |              | :ref:`multi-xml-electoral-district`      |                                          |
|                       |                                         |              |              | element associated with the office.      |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers   | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers that link this office  |                                          |
|                       |                                         |              |              | to other related datasets (e.g. campaign |                                          |
|                       |                                         |              |              | finance systems, OCD IDs, et al.).       |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline        | ``xs:date``                             | Optional     | Single       | Specifies the date and time when a       |                                          |
|                       |                                         |              |              | candidate must have filed for the        |                                          |
|                       |                                         |              |              | contest for the office.                  |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan            | ``xs:boolean``                          | Optional     | Single       | Indicates whether the office is          |                                          |
|                       |                                         |              |              | partisan.                                |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                  | :ref:`multi-xml-internationalized-text` | **Required** | Single       | The name of the office.                  |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonIds | ``xs:IDREFS``                           | Optional     | Single       | Links to the :ref:`multi-xml-person`     |                                          |
|                       |                                         |              |              | element(s) that hold additional          |                                          |
|                       |                                         |              |              | information about the current office     |                                          |
|                       |                                         |              |              | holder(s).                               |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                  | :ref:`multi-xml-term`                   | Optional     | Single       | Defines the term the office can be held. |                                          |
+-----------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-term:

Term
----

+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-office-term-type` | **Required** | Single       | Specifies the type of office term (see   |                                          |
|              |                                   |              |              | :ref:`multi-xml-office-term-type` for    |                                          |
|              |                                   |              |              | valid values).                           |                                          |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | ``xs:date``                       | Optional     | Single       | Specifies the start date for the current |                                          |
|              |                                   |              |              | term of the office.                      |                                          |
+--------------+-----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | ``xs:date``                       | Optional     | Single       | Specifies the end date for the current   |                                          |
|              |                                   |              |              | term of the office.                      |                                          |
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


.. _multi-xml-contact-information:

ContactInformation
------------------

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:ref:`multi-xml-election-administration`, :ref:`multi-xml-office`,
:ref:`multi-xml-person`, :ref:`multi-xml-source`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=========================================+==============+==============+==========================================+==========================================+
| AddressLine      | ``xs:string``                           | Optional     | Repeats      | The "location" portion of a mailing      |                                          |
|                  |                                         |              |              | address. :ref:`See usage note.           |                                          |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions       | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies further instructions for       |                                          |
|                  |                                         |              |              | locating this entity.                    |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Email            | ``xs:string``                           | Optional     | Repeats      | An email address for the contact.        |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Fax              | ``xs:string``                           | Optional     | Repeats      | A fax line for the contact.              |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Contains the hours (in local time) that  |                                          |
| **[deprecated]** |                                         |              |              | the location is open *(NB: this element  |                                          |
|                  |                                         |              |              | is deprecated in favor of the more       |                                          |
|                  |                                         |              |              | structured :ref:`multi-xml-hours-open`   |                                          |
|                  |                                         |              |              | element. It is strongly encouraged that  |                                          |
|                  |                                         |              |              | data providers move toward contributing  |                                          |
|                  |                                         |              |              | hours in this format)*.                  |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | ``xs:IDREF``                            | Optional     | Single       | References an                            |                                          |
|                  |                                         |              |              | :ref:`multi-xml-hours-open` element,     |                                          |
|                  |                                         |              |              | which lists the hours of operation for a |                                          |
|                  |                                         |              |              | location.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng           | :ref:`multi-xml-lat-lng`                | Optional     | Single       | Specifies the latitude and longitude of  |                                          |
|                  |                                         |              |              | this entity.                             |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name             | ``xs:string``                           | Optional     | Single       | The name of the location or contact.     |                                          |
|                  |                                         |              |              | :ref:`See usage note.                    |                                          |
|                  |                                         |              |              | <multi-xml-name-address-line-usage>`     |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Phone            | ``xs:string``                           | Optional     | Repeats      | A phone number for the contact.          |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Uri              | ``xs:anyURI``                           | Optional     | Repeats      | An informational URI for the contact or  |                                          |
|                  |                                         |              |              | location.                                |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _multi-xml-name-address-line-usage:

``Name`` and ``AddressLine`` Usage Note
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``Name`` and ``AddressLine`` fields should be chosen so that a display
or mailing address can be constructed programmatically by joining the
``Name`` and ``AddressLine`` fields together.  For example, for the
following address::

    Department of Elections
    1 Dr. Carlton B. Goodlett Place, Room 48
    San Francisco, CA 94102

The name could be "Department of Elections" and the first address line
could be "1 Dr. Carlton B. Goodlett Place, Room 48."

However, VIP does not yet support the representation of mailing addresses
whose "name" portion spans more than one line, for example::

    California Secretary of State
    Elections Division
    1500 11th Street
    Sacramento, CA 95814

For addresses like the above, we recommend choosing a name like, "California
Secretary of State, Elections Division" with "1500 11th Street" as the
first address line. This would result in a programmatically constructed
address like the following::

    California Secretary of State, Elections Division
    1500 11th Street
    Sacramento, CA 95814

.. code-block:: xml
   :linenos:

   <ContactInformation label="ci10861a">
      <AddressLine>1600 Pennsylvania Ave</AddressLine>
      <AddressLine>Washington, DC 20006</AddressLine>
      <Email>president@whitehouse.gov</Email>
      <Phone>202-456-1111</Phone>
      <Phone annotation="TDD">202-456-6213</Phone>
      <Uri>http://www.whitehouse.gov</Uri>
   </ContactInformation>
