Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

.. include:: ../../tables/elements/source.rst

.. _FIPS: https://www.census.gov/geo/reference/codes/cou.html

.. code-block:: xml
   :linenos:
   
   <Source id="src1">
      <DateTime>2013-10-24T14:25:28</DateTime>
      <Description>
         <Text language="en">SBE is the official source for Virginia data</Text>
      </Description>
      <Name>State Board of Elections, Commonwealth of Virginia</Name>
      <OrganizationUri>http://www.sbe.virginia.gov/</OrganizationUri>
      <VipId>51</VipId>
      <Version>5.0</Version>
   </Source>
