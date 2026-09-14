CSV Specification
=================

.. contents::
   :local:


.. _getting-started:

Getting Started
---------------

The CSV files contain election information, with files containing links between each other, that
can be transformed into an XML feed representing the data according to the base VIP XML specification. See
the `sample xml file`_ and `xsd file`_ for more details.

.. important::
   **Base Feed Only:** The CSV specification applies exclusively to the base VIP feed (corresponding to ``vip_spec.xsd`` / ``vip_main.xsd``). CSV format is **not supported** for Feed Overlays. Feed Overlays are supported exclusively in XML format (see :doc:`Feed Overlays <overlay>`).

Certain files are required to serve different types of information. Below is a listing of which files are required for different VIP data sets. 

Required files:
	- election.txt
	- source.txt
	- locality.txt

Files to serve polling locations:
	- election_administration.txt
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

CSV files must be comma-delimited, UTF-8 .txt files, named according to the specification. In VIP 7.0, political geography is represented by :ref:`multi-csv-locality`, where a state-level jurisdiction is represented as a locality record with ``type`` set to ``state`` (whose ``id`` should typically be based on the state's FIPS code, e.g. ``loc51``). In ``election.txt``, the state is linked via ``top_level_locality_id``. The id attributes are not required to remain constant for the same piece of semantic data across multiple productions of the feed. 

Elements & Enumerations
-----------------------


Single-page Format
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/csv/single_page


Elements (Separate Pages)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/csv/elements/*


Enumerations (Separate Pages)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/csv/enumerations/*
