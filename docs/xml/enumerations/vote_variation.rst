VoteVariation
=============


+----------------------+----------------------------------------------------------------------------------+
| Name                 | Description                                                                      |
|                      |                                                                                  |
+======================+==================================================================================+
| 1-of-m               | A method where each voter can select up to one candidate.                        |
+----------------------+----------------------------------------------------------------------------------+
| approval             | `Approval voting`_, where each voter can select as many candidates as desired.   |
+----------------------+----------------------------------------------------------------------------------+
| cumulative           | `Cumulative voting`_, where each voter can distribute their vote to up to        |
|                      | *N* candidates.                                                                  |
+----------------------+----------------------------------------------------------------------------------+
| majority             | A 1-of-m method where the winner needs more than 50% of the vote to be elected.  |
+----------------------+----------------------------------------------------------------------------------+
| n-of-m               | A method where each voter can select up to *N* candidates.                       |
+----------------------+----------------------------------------------------------------------------------+
| plurality            | A 1-of-m method where the candidate with the most votes is elected, regardless   |
|                      | of whether the candidate has more than 50% of the vote.                          |
+----------------------+----------------------------------------------------------------------------------+
| range                | `Range voting`_, where each voter can select a score for each candidate.         |
+----------------------+----------------------------------------------------------------------------------+
| rcv                  | `Ranked choice voting`_ (RCV), where each voter can rank the candidates, and     |
|                      | the ballots are counted in rounds.  Also known as instant-runoff voting (IRV)    |
|                      | and the single transferable vote (STV).                                          |
+----------------------+----------------------------------------------------------------------------------+
| rcv-borda            | `Borda count`_, where each voter can rank the candidates, and the rankings are   |
|                      | assigned point values.                                                           |
+----------------------+----------------------------------------------------------------------------------+
| super-majority       | A 1-of-m method where the winner needs more than some predetermined fraction     |
|                      | of the vote to be elected, where the fraction is more than 50% (e.g.             |
|                      | three-fifths or two-thirds).                                                     |
+----------------------+----------------------------------------------------------------------------------+
| other                | Used when the vote variation type is not included in this enumeration.           |
+----------------------+----------------------------------------------------------------------------------+

.. _`Approval voting`: http://en.wikipedia.org/wiki/Approval_voting
.. _`Borda count`: http://en.wikipedia.org/wiki/Borda_count
.. _`Cumulative voting`: http://en.wikipedia.org/wiki/Cumulative_voting
.. _`Range voting`: http://en.wikipedia.org/wiki/Range_voting
.. _`Ranked choice voting`: http://http://en.wikipedia.org/wiki/Ranked_Choice_Voting
