.. This file is auto-generated.  Do not edit it by hand!

Precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:doc:`Source.VipId <source>`, :doc:`Locality.Name <locality>`, :doc:`Precinct.Ward <precinct>`,
:doc:`Precinct.Name <precinct>`, and :doc:`Precinct.Number <precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

.. include:: ../../tables/elements/precinct.rst

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <Precinct id="pre90111">
      <BallotStyleId>bs00010</BallotStyleId>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <ElectoralDistrictId>ed60311</ElectoralDistrictId>
      <ElectoralDistrictId>ed60054</ElectoralDistrictId>
      <IsMailOnly>false</IsMailOnly>
      <LocalityId>loc70001</LocalityId>
      <Name>203 - GEORGETOWN</Name>
      <Number>0203</Number>
      <PollingLocationId>pl81274</PollingLocationId>
   </Precinct>
