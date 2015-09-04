OrderedContest
==============

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:doc:`BallotStyle <ballot_style>` to accurate depict exactly what will show up on a particular
ballot in the proper order.

.. include:: ../../tables/elements/ordered_contest.rst

.. code-block:: xml
   :linenos:

   <OrderedContest id="oc20003abc">
      <ContestId>cc20003</ContestId>
      <OrderedBallotSelectionId>cs10961</OrderedBallotSelectionId>
      <OrderedBallotSelectionId>cs10962</OrderedBallotSelectionId>
      <OrderedBallotSelectionId>cs10963</OrderedBallotSelectionId>
   </OrderedContest>
