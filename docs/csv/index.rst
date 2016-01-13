CSV Specification
=================

.. contents::
   :local:


.. _getting-started:

Getting Started
---------------

The CSV files contain election information, with files containing links between each other, that
is compiled into an XML feed that represents the data according to the XML specification. See
the `sample xml file`_ and `xsd file`_ for more details.

Becoming familiar with the XML requirements can help you better understand the CSV specifications. The only
required top-level XML tags are the :ref:`single-xml-source` object and the :ref:`single-xml-election` object,
each of which must be present exactly once. This means that the corresponding
CSV files, :doc:`Source <element_files/source>` and :ref:`single-xml-election`, must contain
only 1 record. All other element file records can exist an unlimited number of times, or not included at
all; order of CSV records does not matter.

CSV files must be comma-delimited, UTF-8 .txt files, named according to the specification. The id attribute
for the state object should be the state's FIPS number. The id attributes are not required to remain constant
for the same piece of semantic data across multiple productions of the feed (e.g. candidate Michael Smith,
running for dogcatcher in Iowa, is not required to have the same candidate id attribute each time the state
of Iowa publishes data). Please see our XML :doc:`Best Practices <../xml_data_best_practices>`
document when creating IDs and labels for your elements.

For the data itself, the special characters &, <, and > need to be encoded as &amp;, &lt;, and &gt;,
respectively.

.. _sample xml file: https://github.com/votinginfoproject/vip-specification/blob/vip5/sample_feed.xml
.. _xsd file: https://github.com/votinginfoproject/vip-specification/blob/vip5/vip_spec.xsd

.. _element_files:

Element Files
-------------

.. toctree::
   :maxdepth: 2
   :glob:

   element_files/*

.. _enumerations:

Enumerations
------------

.. toctree::
   :maxdepth: 2
   :glob:

   enumerations/*
