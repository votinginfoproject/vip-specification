ExternalIdentifiers
===================

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :doc:`Candidate <candidate>`

* Any element that extends :doc:`ContestBase <contest_base>`

* :doc:`ElectoralDistrict <electoral_district>`

* :doc:`Locality <locality>`

* :doc:`Office <office>`

* :doc:`Party <party>`

* :doc:`Precinct <precinct>`

* :doc:`State <state>`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. include:: ../../tables/elements/external_identifiers.rst

ExternalIdentifier
------------------

.. include:: ../../tables/elements/external_identifier.rst

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
