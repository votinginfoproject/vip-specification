CandidateSelection
==================

CandidateSelection extends :doc:`BallotSelectionBase <ballot_selection_base>` and represents a
ballot selection for a candidate contest.

+--------------------+------------+-----------+----------+---------------------+--------------------+
| Tag                | Data Type  | Required? | Repeats? | Description         | Error Handling     |
|                    |            |           |          |                     |                    |
+====================+============+===========+==========+=====================+====================+
| CandidateId        | xs:IDREF   | Optional  | Repeats  |References a         |If the field is     |
|                    |            |           |          |:doc:`Candidate      |invalid or not      |
|                    |            |           |          |<candidate>`         |present, the        |
|                    |            |           |          |element. The number  |implementation is   |
|                    |            |           |          |of candidates that   |required to ignore  |
|                    |            |           |          |can be references is |it.                 |
|                    |            |           |          |unbounded in cases   |                    |
|                    |            |           |          |where the ballot     |                    |
|                    |            |           |          |selection is for a   |                    |
|                    |            |           |          |ticket               |                    |
|                    |            |           |          |(e.g. "President/Vice|                    |
|                    |            |           |          |President",          |                    |
|                    |            |           |          |"Governor/Lt         |                    |
|                    |            |           |          |Governor").          |                    |
+--------------------+------------+-----------+----------+---------------------+--------------------+
| EndorsementPartyId | xs:IDREF   | Optional  | Repeats  |References a         |If the field is     |
|                    |            |           |          |:doc:`Party <party>` |invalid or not      |
|                    |            |           |          |element, which       |present, the        |
|                    |            |           |          |signifies one or more|implementation is   |
|                    |            |           |          |endorsing parties for|required to ignore  |
|                    |            |           |          |the candidate(s).    |it.                 |
+--------------------+------------+-----------+----------+---------------------+--------------------+
| IsWriteIn          | xs:boolean | Optional  | Single   |Signifies if the     |If the field is     |
|                    |            |           |          |particular ballot    |invalid or not      |
|                    |            |           |          |selection allows for |present, the        |
|                    |            |           |          |write-in             |implementation is   |
|                    |            |           |          |candidates. If true, |required to ignore  |
|                    |            |           |          |one or more write-in |it.                 |
|                    |            |           |          |candidates are       |                    |
|                    |            |           |          |allowed for this     |                    |
|                    |            |           |          |contest.             |                    |
+--------------------+------------+-----------+----------+---------------------+--------------------+

.. code-block:: xml
   :linenos:
      
   <CandidateSelection id="cs10961">
      <CandidateId>can10961</CandidateId>
      <EndorsementPartyId>par0001</EndorsementPartyId>
   </CandidateSelection>
