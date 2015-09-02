ElectoralDistrict
=================

The ``ElectoralDistrict`` object represents the geographic area in which contests are held. Examples
of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District",
or "Union School District". The geographic area that comprises a ``ElectoralDistrict`` is defined by
which precincts link to the ``ElectoralDistrict``.

.. include:: ../../tables/elements/electoral_district.rst

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
