ElectoralDistrict
=================

The ``ElectoralDistrict`` object represents the geographic area in which contests are held. Examples
of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District",
or "Union School District". The geographic area that comprises a ``ElectoralDistrict`` is defined by
which precincts link to the ``ElectoralDistrict``.

+---------------------+--------------------------------+------------+----------+--------------------------------+----------------------------+
| Tag                 | Data Type                      | Required?  | Repeats? |Description                     |Error Handling              |
|                     |                                |            |          |                                |                            |
+=====================+================================+============+==========+================================+============================+
| ExternalIdentifiers |:doc:`ExternalIdentifiers       | Optional   | Single   |Other identifiers that          |If the element is invalid or|
|                     |<external_identifiers>`         |            |          |link to external                |not present, then the       |
|                     |                                |            |          |datasets                        |implementation is required  |
|                     |                                |            |          |(e.g. `OCD-IDs`_)               |to ignore it.               |
+---------------------+--------------------------------+------------+----------+--------------------------------+----------------------------+
| Name                | xs:string                      |**Required**| Single   |Specifies the                   |If the field is invalid or  |
|                     |                                |            |          |electoral area's name.          |not present, then the       |
|                     |                                |            |          |                                |implementation is required  |
|                     |                                |            |          |                                |to ignore the               |
|                     |                                |            |          |                                |``ElectoralDistrict`` object|
|                     |                                |            |          |                                |containing it.              |
+---------------------+--------------------------------+------------+----------+--------------------------------+----------------------------+
| Number              | xs:integer                     | Optional   | Single   |Specifies the district          |If the field is invalid or  |
|                     |                                |            |          |number of the district          |not present, then the       |
|                     |                                |            |          |(e.g. 34, in the case           |implementation is required  |
|                     |                                |            |          |of the 34th State               |to ignore it.               |
|                     |                                |            |          |Senate District). If a          |                            |
|                     |                                |            |          |number is not                   |                            |
|                     |                                |            |          |applicable, instead of          |                            |
|                     |                                |            |          |leaving the field               |                            |
|                     |                                |            |          |blank, leave this               |                            |
|                     |                                |            |          |field out of the                |                            |
|                     |                                |            |          |object; empty strings           |                            |
|                     |                                |            |          |are not valid for               |                            |
|                     |                                |            |          |xs:integer fields.              |                            |
+---------------------+--------------------------------+------------+----------+--------------------------------+----------------------------+
| Type                |:doc:`DistrictType              |**Required**| Single   |Specifies the type of           |If the field is invalid or  |
|                     |<../enumerations/district_type>`|            |          |electoral area.                 |not present, then the       |
|                     |                                |            |          |                                |implementation is required  |
|                     |                                |            |          |                                |to ignore the               |
|                     |                                |            |          |                                |``ElectoralDistrict`` object|
|                     |                                |            |          |                                |containing it.              |
+---------------------+--------------------------------+------------+----------+--------------------------------+----------------------------+
| OtherType           | xs:string                      | Optional   | Single   |Allows for cataloging a new     |If the element is invalid or|
|                     |                                |            |          |:doc:`DistrictType              |not present, the            |
|                     |                                |            |          |<../enumerations/district_type>`|implementation is required  |
|                     |                                |            |          |option when ``Type`` is         |to ignore it.               |
|                     |                                |            |          |specified as "other".           |                            |
+---------------------+--------------------------------+------------+----------+--------------------------------+----------------------------+

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:
      
   <ElectoralDistrict id="ed60129">
      <ExternalIdentifiers>
        <ExternalIdentifier>
          <Type>ocd-id</Type>
	  <Value>ocd-division/country:us/state:va</Value>
	</ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Commonwealth of Virginia</Name>
      <Type>state</Type>
   </ElectoralDistrict>
