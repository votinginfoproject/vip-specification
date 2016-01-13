precinct.txt
============

The precinct.txt file represents precincts, which are contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:doc:`Source.VipId <source>`, :doc:`Locality.Name <locality>`, :doc:`Precinct.Ward <precinct>`,
:doc:`Precinct.Name <precinct>`, and :doc:`Precinct.Number <precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

.. include:: ../../built_rst/tables/elements/precinct.rst

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. literalinclude:: ../../csv/example_files/precinct.txt
   :linenos: