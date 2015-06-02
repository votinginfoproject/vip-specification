OrderedContest
==============

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:doc:`BallotStyle <ballot_style>` to accurate depict exactly what will show up on a particular
ballot in the proper order.

+-------------------+------------+------------+----------+---------------------------+--------------------+
| Tag               | Data Type  | Required?  | Repeats? |Description                |Error Handling      |
|                   |            |            |          |                           |                    |
+===================+============+============+==========+===========================+====================+
| BallotSelectionId | xs:IDREF   | Optional   | Repeats  |Links to elements that     |If the field is     |
|                   |            |            |          |extend                     |invalid or not      |
|                   |            |            |          |:doc:`BallotSelectionBase  |present, the        |
|                   |            |            |          |<ballot_selection_base>`.  |implementation is   |
|                   |            |            |          |                           |required to ignore  |
|                   |            |            |          |                           |it.                 |
+-------------------+------------+------------+----------+---------------------------+--------------------+
| ContestId         | xs:IDREF   |**Required**| Single   |Links to elements that     |If the field is     |
|                   |            |            |          |extend :doc:`ContestBase   |invalid or not      |
|                   |            |            |          |<contest_base>`.           |present, the        |
|                   |            |            |          |                           |implementation is   |
|                   |            |            |          |                           |required to ignore  |
|                   |            |            |          |                           |the                 |
|                   |            |            |          |                           |``OrderedContest``  |
|                   |            |            |          |                           |element containing  |
|                   |            |            |          |                           |it.                 |
+-------------------+------------+------------+----------+---------------------------+--------------------+

.. code-block:: xml
   :linenos:

   <OrderedContest id="oc20262">
     <ContestId>cc20262</ContestId>
   </OrderedContest>
