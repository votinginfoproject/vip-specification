XML Specification
=================

.. contents::
   :local:


.. _xml-getting-started:

Getting Started
---------------

The actual election information specifies collections of elements, some containing links between
each other. The entire set of tags must be encapsulated in a root object named vip_object. See the
`sample xml file`_ and `xsd file`_ for more details.

Each top-level tag is a container for other fields, described in their own section. The only required
top-level tags are the :doc:`source object <built_rst/xml/elements/source>` and the
:doc:`election object <built_rst/xml/elements/election>`, each of which must be present exactly once. All other
top-level tags can be repeated an unlimited number of times, or not included at all; order of
top-level tags does not matter. Each top-level tag is required to have a single attribute, "id",
which is required to be unique in a data file. The id attribute for the state object should be the
state's FIPS number and this is strongly recommended. The id attributes are not required to remain
constant for the same piece of semantic data across multiple productions of the feed (e.g.
candidate Michael Smith, running for dogcatcher in Iowa, is not required to have the same candidate
id attribute each time the state of Iowa publishes data).

In general, subtag data can appear a maximum of one time within each top-level tag object and in any
order. Exceptions are noted below.

For the data itself, the special characters &, <, and > need to be encoded as &amp;, &lt;, and &gt;,
respectively.

.. _sample xml file: https://github.com/votinginfoproject/vip-specification/blob/release/sample_feed.xml
.. _xsd file: https://github.com/votinginfoproject/vip-specification/blob/release/vip_spec.xsd


.. _naming-convention:

Naming convention
~~~~~~~~~~~~~~~~~

The file containing the VIP feed should be named using the following convention:

.. code-block:: none

   vipfeed-${FIPS}-${ELECTION_DATE}-${STATE}[-${LOCAL}].{xml|zip}

An explanation of each of the segments of the file naming convention above are as follows:

- ``${FIPS}`` - The `FIPS code`_ for the jurisdiction.
- ``${ELECTION_DATE}`` - The date of the election in `ISO 8601`_ format.
- ``${STATE}`` - The full state name (e.g. Alaska, Arkansas, etc...) and not the abbreviation. If
  there are spaces in the state name, they should be substituted with underscores (e.g. New York ->
  New_York).
- ``${LOCAL}`` (optional) - This additional identifier should be used if the file contains data
  from a specific jurisdiction. As with ``${STATE}`` above, all spaces should be substituted with
  underscores. For example, if the data contained in the file only covers Maricopa County, AZ for
  the November 6, 2012 election, the file name would be
  ``vipfeed-04013-2012-11-06-Arizona-Maricopa_County.xml``.
- ``{xml|zip}`` - If the file is an uncompressed XML document, the extension should be ``.xml.`` If
  the file is zipped, the file extension should end with ``.zip``.

For a final example, ``vipfeed-19-2012-11-06-Iowa.zip`` denotes Iowa's (**NB:** the FIPS code
for IA is 19) feed for the Nov 6, 2012 election that has been compressed.

.. _FIPS code: https://en.wikipedia.org/wiki/FIPS_county_code
.. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601

.. _best-practices:

Best Practices
--------------

There are many different ways to generate a valid feed. We strongly encourage
reviewing and adhering to the guidelines described in the following best
practices sections:

.. toctree::
   :maxdepth: 2

   xml_data_best_practices

These sections outline several recommendations for feed layout, element
identifiers, and enumeration selection that will make it easier to generate
and troubleshoot your VIP feeds.


Elements & Enumerations
-----------------------


Single-page Format
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/xml/single_page


Elements (Separate Pages)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/xml/elements/*


Enumerations (Separate Pages)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/xml/enumerations/*
