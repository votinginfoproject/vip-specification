CandidateContest
================

CandidateContest extends :doc:`ContestBase <contest_base>` and represents a contest among
candidates.

+----------------+------------+-----------+----------+----------------------+-------------------------+
| Tag            | Data Type  | Required? | Repeats? | Description          | Error Handling          |
|                |            |           |          |                      |                         |
+================+============+===========+==========+======================+=========================+
| NumberElected  | xs:integer | Optional  | Single   |Number of candidates  |If the field is invalid  |
|                |            |           |          |that are elected in   |or not present, then the |
|                |            |           |          |the contest (i.e. "N" |implementation is        |
|                |            |           |          |of N-of-M).           |required to ignore it.   |
|                |            |           |          |                      |                         |
+----------------+------------+-----------+----------+----------------------+-------------------------+
| OfficeId       | xs:IDREF   | Optional  | Repeats  |References an         |If the field is invalid  |
|                |            |           |          |:doc:`Office <office>`|or not present, then the |
|                |            |           |          |element, if available,|implementation is        |
|                |            |           |          |which gives additional|required to ignore it.   |
|                |            |           |          |information about the |                         |
|                |            |           |          |office.               |                         |
+----------------+------------+-----------+----------+----------------------+-------------------------+
| PrimaryPartyId | xs:IDREF   | Optional  | Single   |References a          |If the field is invalid  |
|                |            |           |          |:doc:`Party <party>`  |or not present, then the |
|                |            |           |          |element, if the       |implementation is        |
|                |            |           |          |contest is related to |required to ignore it.   |
|                |            |           |          |a particular party.   |                         |
+----------------+------------+-----------+----------+----------------------+-------------------------+
| VotesAllowed   | xs:integer | Optional  | Single   |Maximum number of     |If the field is invalid  |
|                |            |           |          |votes/write-ins per   |or not present, then the |
|                |            |           |          |voter in this contest.|implementation is        |
|                |            |           |          |                      |required to ignore it.   |
+----------------+------------+-----------+----------+----------------------+-------------------------+

.. code-block:: xml
   :linenos:

   <CandidateContest id="cc20003">
      <BallotSelectionId>cs10961</BallotSelectionId>
      <BallotSelectionId>cs10962</BallotSelectionId>
      <BallotSelectionId>cs10963</BallotSelectionId>
      <BallotTitle>
        <Text language="en">Governor of Virginia</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Governor</Name>
      <NumberElected>1</NumberElected>
      <OfficeId>off0000</OfficeId>
      <VotesAllowed>1</VotesAllowed>
   </CandidateContest>
