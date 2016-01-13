.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-candidate-contest:

CandidateContest
================

CandidateContest extends :ref:`single-xml-contest-base` and represents a contest among
candidates.

+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+================+==============+==============+==========================================+==========================================+
| NumberElected  | ``xs:integer`` | Optional     | Single       | Number of candidates that are elected in | If the field is invalid or not present,  |
|                |                |              |              | the contest (i.e. "N" of N-of-M).        | then the implementation is required to   |
|                |                |              |              |                                          | ignore it.                               |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeId       | ``xs:IDREF``   | Optional     | Repeats      | References an :ref:`single-xml-office`   | If the field is invalid or not present,  |
|                |                |              |              | element, if available, which gives       | then the implementation is required to   |
|                |                |              |              | additional information about the office. | ignore it.                               |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrimaryPartyId | ``xs:IDREF``   | Optional     | Single       | References a :ref:`single-xml-party`     | If the field is invalid or not present,  |
|                |                |              |              | element, if the contest is related to a  | then the implementation is required to   |
|                |                |              |              | particular party.                        | ignore it.                               |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VotesAllowed   | ``xs:integer`` | Optional     | Single       | Maximum number of votes/write-ins per    | If the field is invalid or not present,  |
|                |                |              |              | voter in this contest.                   | then the implementation is required to   |
|                |                |              |              |                                          | ignore it.                               |
+----------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

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
