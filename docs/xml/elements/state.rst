State
=====

The State object includes state-wide election information. The ID attribute is
recommended to be the state's FIPS code, along with the prefix "st".

.. include:: ../../tables/elements/state.rst

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <State id="st51">
      <ElectionAdministrationId>ea40133</ElectionAdministrationId>
      <ExternalIdentifiers>
        <ExternalIdentifier>
	  <Type>ocd-id</Type>
	  <Value>ocd-division/country:us/state:va</Value>
	</ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Virginia</Name>
   </State>
