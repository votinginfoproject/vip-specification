CSV Specification
=================

* :ref:`getting-started`

* :ref:`element_files`

* :ref:`enumerations`

.. _getting-started:

Getting Started
---------------

The CSV files contain election information, with files containing links between each other, that 
is compiled into an XML feed that represents the data according to the XML specification. See 
the `sample xml file`_ and `xsd file`_ for more details.

Becoming familiar with the XML requirements can help you better understand the CSV specifications. The only 
required top-level XML tags are the :doc:`source object <elements/source>` and the :doc:`election object 
<xml/elements/election>`, each of which must be present exactly once. This means that the corresponding 
CSV files, :doc:`source <element_files/source>` and :doc:`election <element_files/election>`, must contain 
only 1 record. All other element file records can exist an unlimited number of times, or not included at 
all; order of CSV records does not matter. 

CSV files must be comma-delimited, UTF-8 .txt files, named according to the specification. Because the XML 
requires each "id" attribute to be unique in a file, each CSV file must have an "id" field that is unique 
throughout all files in your dataset. The id attribute for the state object should be the state's FIPS number. 
The id attributes are not required to remain constant for the same piece of semantic data across multiple 
productions of the feed (e.g. candidate Michael Smith, running for dogcatcher in Iowa, is not required 
to have the same candidate id attribute each time the state of Iowa publishes data).

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
