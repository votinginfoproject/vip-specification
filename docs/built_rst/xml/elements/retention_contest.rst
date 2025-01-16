.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-retention-contest:

RetentionContest
================

``RetentionContest`` extends :ref:`multi-xml-ballot-measure-contest` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| CandidateId  | ``xs:IDREF`` | **Required** | Single       | Links to the :ref:`multi-xml-candidate`  |                                          |
|              |              |              |              | being retained.                          |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeId     | ``xs:IDREF`` | Optional     | Single       | Links to the information about the       |                                          |
|              |              |              |              | office.                                  |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <RetentionContest id="rc40001">
      <BallotSelectionIds>rc40001a rc40001b</BallotSelectionIds>
      <BallotTitle>
         <Text language="en">Retention of Supreme Court Justice</Text>
         <Text language="es">La retención de juez de la Corte Suprema</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Judicial Retention, Supreme Court</Name>
      <CandidateId>can14444</CandidateId>
      <OfficeId>off20006</OfficeId>
   </RetentionContest>
