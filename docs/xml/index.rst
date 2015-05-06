XML Specification
=================

* :ref:`getting-started`

  * :ref:`naming-convention`

* :ref:`elements`

.. _getting-started:

Getting Started
---------------

The actual election information specifies collections of elements, some containing links between
each other. The entire set of tags must be encapsulated in a root object named vip_object. See the
`sample xml file`_ and `xsd file`_ for more details.

Each top-level tag is a container for other fields, described in their own section. The only required
top-level tags are the :doc:`source object <elements/source>` and the
:doc:`election object <elements/election>`, each of which must be present exactly once. All other
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

.. _sample xml file: https://github.com/votinginfoproject/vip-specification/blob/vip5/sample_feed.xml
.. _xsd file: https://github.com/votinginfoproject/vip-specification/blob/vip5/vip_spec.xsd

.. _naming-convention:

Naming convention
~~~~~~~~~~~~~~~~~

The file containing the VIP feed should be named
vipFeed-[FIPS code for state or county]-[election year]-[election month]-[election day].xml. If the
file is zipped, the file extensions of .zip or .xml.zip are also acceptable.

For instance, vipFeed-19-2012-11-06.zip denotes Iowa's (the FIPS code for IA is 19) feed for the
Nov 6, 2012 election.

.. _elements:

Elements
--------

.. toctree::
   :maxdepth: 2
   :glob:
      
   elements/source
   elements/*
