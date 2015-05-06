.. Voting Information Project Specification documentation master file, created by
   sphinx-quickstart on Fri May  1 12:23:13 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the VIP Specification documentation
==============================================
Welcome to the `Voting Information Project's`_ (VIP) open XML and flat file (CSV) format. This data
format provides an easy way to produce data that lets developers take a voter's address, compare it
to street segments, and determine that voter's precinct (or precinct split). Knowing a voter's
precinct allows information disseminators (such as `Google`_) to provide voters with their official
polling locations (and early voting sites), ballots (including both candidates and referenda), local
election administrations, and election officials.

.. _Voting Information Project's: https://www.votinginfoproject.org/
.. _Google: https://developers.google.com/civic-information/

The documentation is split into two distinct parts.

* :ref:`xml-docs`
* :ref:`csv-docs`

.. _xml-docs:

XML Documentation
------------------

.. toctree::
   :maxdepth: 2

   xml/index

.. _csv-docs:

CSV Documentation
------------------

.. toctree::
   :maxdepth: 2

   source
   election
   state
   locality
   precinct
   precinct_split
   election_administration
   election_official
   polling_location
   early_vote_site
   contest
   electoral_district
   ballot
   candidate
   referendum
   custom_ballot
   ballot_response
   street_segment
   contest_result
   ballot_line_result

.. todolist::
