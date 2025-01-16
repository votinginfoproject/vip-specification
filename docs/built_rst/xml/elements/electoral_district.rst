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
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifiers that link to external  |                                          |
|                     |                                       |              |              | datasets (e.g. `OCD-IDs`_)               |                                          |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | ``xs:string``                         | **Required** | Single       | Specifies the electoral area's name.     |                                          |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number              | ``xs:integer``                        | Optional     | Single       | Specifies the district number of the     |                                          |
|                     |                                       |              |              | district (e.g. 34, in the case of the    |                                          |
|                     |                                       |              |              | 34th State Senate District). If a number |                                          |
|                     |                                       |              |              | is not applicable, instead of leaving    |                                          |
|                     |                                       |              |              | the field blank, leave this field out of |                                          |
|                     |                                       |              |              | the object; empty strings are not valid  |                                          |
|                     |                                       |              |              | for xs:integer fields.                   |                                          |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                | :ref:`multi-xml-district-type`        | **Required** | Single       | Specifies the type of electoral area.    |                                          |
+---------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType           | ``xs:string``                         | Optional     | Single       | Allows for cataloging a new              |                                          |
|                     |                                       |              |              | :ref:`multi-xml-district-type` option    |                                          |
|                     |                                       |              |              | when ``Type`` is specified as "other".   |                                          |
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
