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

Certain files are required to serve different types of information. Below is a listing of which files are required for different VIP data sets. 

Required files:
	- election.txt
	- source.txt
	- state.txt 
	- department.txt

Files to serve polling locations:
	- election_administration.txt
	- department.txt
	- locality.txt 
	- polling_location.txt
	- precinct.txt
	- street_segment.txt

Files to serve candidate contests:
	- candidate.txt
	- candidate_contest.txt
	- candidate_selection.txt
	- office.txt

Files to serve referenda and ballot measures:
	- ballot_measure_contest.txt 
	- ballot_measure_selection.txt

Files to serve retention contests:
	- retention_contest.txt

CSV files must be comma-delimited, UTF-8 .txt files, named according to the specification. The id attribute
for the state object should be the state's FIPS number. The id attributes are not required to remain constant
for the same piece of semantic data across multiple productions of the feed (e.g. candidate Michael Smith,
running for dogcatcher in Iowa, is not required to have the same candidate id attribute each time the state
of Iowa publishes data). Please see our XML :doc:`Best Practices <../xml_data_best_practices>`
document when creating IDs and labels for your elements.

For the data itself, the special characters &, <, and > need to be encoded as &amp;, &lt;, and &gt;,
respectively.

.. _sample xml file: https://github.com/votinginfoproject/vip-specification/blob/release/sample_feed.xml
.. _xsd file: https://github.com/votinginfoproject/vip-specification/blob/release/vip_spec.xsd

.. _element_files:

Element Files
-------------

.. toctree::
   :maxdepth: 2
   :glob:

   element_files/*

.. _enumerations:

