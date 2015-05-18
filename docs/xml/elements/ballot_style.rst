BallotStyle
===========

A container for the contests/measures on the ballot.

+------------------+------------+-----------+----------+----------------------+------------------------+
| Tag              | Data Type  | Required? | Repeats? | Description          | Error Handling         |
|                  |            |           |          |                      |                        |
+==================+============+===========+==========+======================+========================+
| ImageUri         | xs:anyURI  | Optional  | Single   |Specifies a URI that  |If the field is invalid |
|                  |            |           |          |returns an image of   |or not present, the     |
|                  |            |           |          |the sample ballot.    |implementation is       |
|                  |            |           |          |                      |required to ignore it.  |
+------------------+------------+-----------+----------+----------------------+------------------------+
| OrderedContestId | xs:IDREF   | Optional  | Repeats  |Reference to an       |If the field is invalid |
|                  |            |           |          |:doc:`OrderedContest  |or not present, the     |
|                  |            |           |          |<ordered_contest>`    |implementation is       |
|                  |            |           |          |                      |required to ignore it.  |
+------------------+------------+-----------+----------+----------------------+------------------------+
| PartyId          | xs:IDREF   | Optional  | Repeats  |Reference to a        |If the field is invalid |
|                  |            |           |          |:doc:`Party <party>`. |or not present, the     |
|                  |            |           |          |                      |implementation is       |
|                  |            |           |          |                      |required to ignore it.  |
+------------------+------------+-----------+----------+----------------------+------------------------+

.. code-block:: xml
   :linenos:

   <BallotStyle id="bs00000">
      <OrderedContestId>oc20003</OrderedContestId>
      <OrderedContestId>oc20004</OrderedContestId>
      <OrderedContestId>oc20005</OrderedContestId>
      <OrderedContestId>oc20025</OrderedContestId>
      <OrderedContestId>oc20355</OrderedContestId>
      <OrderedContestId>oc20449</OrderedContestId>
   </BallotStyle>

