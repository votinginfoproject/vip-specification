PartySelection
==============

This element extends :doc:`BallotSelectionBase <ballot_selection_base>` to
support contests in which the selections can be groups of one or more parties.

+---------+-----------+------------+----------+----------------------+-------------------------------+
| Tag     | Data Type | Required?  | Repeats? |Description           |Error Handling                 |
|         |           |            |          |                      |                               |
+=========+===========+============+==========+======================+===============================+
| PartyId | xs:IDREF  |**Required**| Repeats  |One or more           |If one or more parties         |
|         |           |            |          |:doc:`Party <party>`  |referenced are invalid or not  |
|         |           |            |          |IDs which collectively|present, the implementation is |
|         |           |            |          |represent a ballot    |required to ignore the         |
|         |           |            |          |selection.            |PartySelection containing it.  |
+---------+-----------+------------+----------+----------------------+-------------------------------+
