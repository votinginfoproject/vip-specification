.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-electoral-district:

ElectoralDistrict
=================

The ``ElectoralDistrict`` object represents the geographic area in which contests are held. Examples
of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District",
or "Union School District". The geographic area that comprises a ``ElectoralDistrict`` is defined by
which precincts link to the ``ElectoralDistrict``.

+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=======================================+==============+==============+==========================================+==========================================+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifiers that link to external  | If the element is invalid or not         |
|                     |                                       |              |              | datasets (e.g. `OCD-IDs`_)               | present, then the implementation is      |
|                     |                                       |              |              |                                          | required to ignore it.                   |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | ``xs:string``                         | **Required** | Single       | Specifies the electoral area's name.     | If the field is invalid or not present,  |
|                     |                                       |              |              |                                          | then the implementation is required to   |
|                     |                                       |              |              |                                          | ignore the ``ElectoralDistrict`` object  |
|                     |                                       |              |              |                                          | containing it.                           |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number              | ``xs:integer``                        | Optional     | Single       | Specifies the district number of the     | If the field is invalid or not present,  |
|                     |                                       |              |              | district (e.g. 34, in the case of the    | then the implementation is required to   |
|                     |                                       |              |              | 34th State Senate District). If a number | ignore it.                               |
|                     |                                       |              |              | is not applicable, instead of leaving    |                                          |
|                     |                                       |              |              | the field blank, leave this field out of |                                          |
|                     |                                       |              |              | the object; empty strings are not valid  |                                          |
|                     |                                       |              |              | for xs:integer fields.                   |                                          |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                | :ref:`multi-xml-district-type`        | **Required** | Single       | Specifies the type of electoral area.    | If the field is invalid or not present,  |
|                     |                                       |              |              |                                          | then the implementation is required to   |
|                     |                                       |              |              |                                          | ignore the ``ElectoralDistrict`` object  |
|                     |                                       |              |              |                                          | containing it.                           |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType           | ``xs:string``                         | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                     |                                       |              |              | :ref:`multi-xml-district-type` option    | then the implementation is required to   |
|                     |                                       |              |              | when ``Type`` is specified as "other".   | ignore it.                               |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <ElectoralDistrict id="ed60129">
      <ExternalIdentifiers>
        <ExternalIdentifier>
          <Type>ocd-id</Type>
          <Value>ocd-division/country:us/state:va</Value>
        </ExternalIdentifier>
        <ExternalIdentifier>
          <Type>fips</Type>
          <Value>51</Value>
        </ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Commonwealth of Virginia</Name>
      <Type>state</Type>
   </ElectoralDistrict>


.. _multi-xml-external-identifiers:

ExternalIdentifiers
-------------------

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-xml-candidate`

* Any element that extends :ref:`multi-xml-contest-base`

* :ref:`multi-xml-electoral-district`

* :ref:`multi-xml-locality`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-precinct`

* :ref:`multi-xml-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+======================================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | :ref:`multi-xml-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                    |                                      |              |              | identifier it is (see                    | must be present for                      |
|                    |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                    |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                    |                                      |              |              |                                          | present, the implementation is required  |
|                    |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                    |                                      |              |              |                                          | element.                                 |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-external-identifier:

ExternalIdentifier
~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                                  |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                  |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                  |              |              | outside the options listed in            | ignore it.                               |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
|              |                                  |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                  |              |              | using this field.                        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifiers>
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:nc/county:durham</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>FIPS</Type>
         <Value>37063</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>OTHER</Type>
         <OtherType>GNIS</OtherType>
         <Value>1008550</Value>
      </ExternalIdentifier>
      <external_identifer>
         <Type>OTHER</Type>
         <OtherType>census</OtherType>
         <Value>99063</Value>
      </ExternalIdentifier>
   </ExternalIdentifiers>
