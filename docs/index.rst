.. Voting Information Project Specification documentation master file, created by
   sphinx-quickstart on Fri May  1 12:23:13 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the VIP Specification documentation (VIP 7.0)
=========================================================
Welcome to the `Voting Information Project's`_ (VIP) open XML, CSV, and Feed Overlay format specification (Version 7.0). This data format provides an easy way to produce data that
lets developers take a voter's address, compare it to street segments, and
determine that voter's precinct (or precinct split). Knowing a voter's precinct
allows :ref:`information disseminators <vip-publishers>` to provide voters with
their official polling locations (and early voting sites), ballots (including
both candidates and referenda), local election administrations, and election
officials.

.. _Voting Information Project's: https://www.votinginfoproject.org/

To see a changelog of all of the updates, please see `the GitHub repository`_.

.. _`the GitHub repository`: https://github.com/votinginfoproject/vip-specification/blob/master/HISTORY.md

.. _vip-publishers:
Publishers of VIP data
----------------------
The following projects publish VIP data for end user consumption.

* `The Google Civic Information API <https://developers.google.com/civic-information/>`_

.. _xml-docs:

XML Documentation
-----------------

.. toctree::
   :maxdepth: 2

   xml


.. _overlay-docs-section:

Feed Overlay Documentation
--------------------------

.. toctree::
   :maxdepth: 2

   overlay


.. _csv-docs:

CSV Documentation
-----------------

.. toctree::
   :maxdepth: 2

   csv

Best Practices
-----------------

.. toctree::
   :maxdepth: 2

   data_best_practices
