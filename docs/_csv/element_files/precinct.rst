precinct.txt  
======================

The Precinct object represents a precinct, which is contained within a Locality. While the id attribute does not have to be static across feeds for one election, the combination of Source.VipId, Locality.Name, Precinct.Ward, Precinct.Name, and Precinct.Number should remain constant across feeds for one election (NB: not all of the fields just mentioned are required – omitting those non-required fields is fine).

To support precinct splits within the CSV specification, create a precinct record for each precinct split and then populate electoral_district_ids and polling_location_ids with each record (multiples allowed with a space separated ( ) concatenation) which applies to that split. The street_segment records will then reference the precinct_id, be it a regular precinct or a split precinct. 

.. csv-table:: precinct
	:file: ../../csv/template_files/precinct.txt
	:header: "CSV Element", "Description"

.. literalinclude:: ../../csv/example_files/precinct.txt
   :linenos: