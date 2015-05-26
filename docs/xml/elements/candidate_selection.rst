CandidateSelection
==================

CandidateSelection extends :doc:`BallotSelectionBase <ballot_selection_base>` and represents a
ballot selection for a candidate contest.

+--------------------+------------+-----------+----------+----------------------+----------------------+
| Tag                | Data Type  | Required? | Repeats? | Description          | Error Handling       |
|                    |            |           |          |                      |                      |
+====================+============+===========+==========+======================+======================+
| CandidateId        | xs:IDREF   | Optional  | Repeats  |References a          |If the field is       |
|                    |            |           |          |:doc:`Candidate       |invalid or not        |
|                    |            |           |          |<candidate>`          |present, the          |
|                    |            |           |          |element. The number of|implementation is     |
|                    |            |           |          |candidates that can be|required to ignore it.|
|                    |            |           |          |references is         |                      |
|                    |            |           |          |unbounded in cases    |                      |
|                    |            |           |          |where the ballot      |                      |
|                    |            |           |          |selection is for a    |                      |
|                    |            |           |          |ticket.               |                      |
+--------------------+------------+-----------+----------+----------------------+----------------------+
| EndorsementPartyId | xs:IDREF   | Optional  | Repeats  |References a          |If the field is       |
|                    |            |           |          |:doc:`Party <party>`  |invalid or not        |
|                    |            |           |          |element, which        |present, the          |
|                    |            |           |          |signifies one or more |implementation is     |
|                    |            |           |          |endorsing parties for |required to ignore it.|
|                    |            |           |          |the candidate(s).     |                      |
+--------------------+------------+-----------+----------+----------------------+----------------------+
| IsWriteIn          | xs:boolean | Optional  | Single   |Signifies if the      |If the field is       |
|                    |            |           |          |particular ballot     |invalid or not        |
|                    |            |           |          |selection allows for  |present, the          |
|                    |            |           |          |write-in              |implementation is     |
|                    |            |           |          |candidates. If true,  |required to ignore it.|
|                    |            |           |          |one or more write-in  |                      |
|                    |            |           |          |candidates are allowed|                      |
|                    |            |           |          |for this contest.     |                      |
+--------------------+------------+-----------+----------+----------------------+----------------------+

.. code-block:: xml
   :linenos:
      
   <CandidateSelection id="cs10961">
      <CandidateId>can10961</CandidateId>
      <EndorsementPartyId>par0001</EndorsementPartyId>
   </CandidateSelection>
