.. Voting Information Project Specification documentation master file, created by
   sphinx-quickstart on Fri May  1 12:23:13 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the VIP Specification documentation
==============================================
Welcome to the `Voting Information Project's`_ (VIP) :ref:`open XML <xml-docs>` and :ref:`CSV <csv-docs>`
format specification. This data format provides an easy way to produce data that
lets developers take a voter's address, compare it to street segments, and
determine that voter's precinct (or precinct split). Knowing a voter's precinct
allows information disseminators (such as `Google`_) to provide voters with
their official polling locations (and early voting sites), ballots (including
both candidates and referenda), local election administrations, and election
officials.

.. _Voting Information Project's: https://www.votinginfoproject.org/
.. _Google: https://developers.google.com/civic-information/

To see a changelog of all of the updates, please see `the GitHub repository`_.

.. _`the GitHub repository`: https://github.com/votinginfoproject/vip-specification/blob/release/HISTORY.md

.. _xml-docs:

XML Documentation
-----------------

.. toctree::
   :maxdepth: 2

   xml


.. _csv-docs:

CSV Documentation
-----------------

.. toctree::
   :maxdepth: 2

   csv/index
