precinct.txt  
======================

The Precinct object represents a precinct, which is contained within a Locality. While the id attribute does not have to be static across feeds for one election, the combination of Source.VipId, Locality.Name, Precinct.Ward, Precinct.Name, and Precinct.Number should remain constant across feeds for one election (NB: not all of the fields just mentioned are required – omitting those non-required fields is fine).

.. csv-table:: precinct
	:file: ../../csv/template_files/precinct.txt
	:header: "CSV Element", "Description"

.. literalinclude:: ../../csv/example_files/precinct.txt
   :linenos: