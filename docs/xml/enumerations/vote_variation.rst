VoteVariation
=============

    
+----------------------+----------------------------------------------------------------------------------+
| Name                 | Description                                                                      |
|                      |                                                                                  |
+======================+==================================================================================+
| 1-of-m               | When a voter can select only one candidate in a contest.                         |
+----------------------+----------------------------------------------------------------------------------+
| approval_            | When a voter can select as many candidates as desired.                           |
+----------------------+----------------------------------------------------------------------------------+
| cumulative_          | When a voter can allocate more than one vote to a given candidate.               |
+----------------------+----------------------------------------------------------------------------------+
| majority             | A candidate must get at least 50% of the votes in order to win.                  |
+----------------------+----------------------------------------------------------------------------------+
| n-of-m               | A voter can select between zero and *N* of the candidates.                       |
+----------------------+----------------------------------------------------------------------------------+
| plurality            | The candidate with the most number of votes, even if not a majority, wins.       |
+----------------------+----------------------------------------------------------------------------------+
| range_               |                                                                                  |
+----------------------+----------------------------------------------------------------------------------+
| rcv_                 | For ranked choice voting for ranking candidates in order of preference rather    |
|                      | than voting for a single candidate.                                              |
+----------------------+----------------------------------------------------------------------------------+
| rcv-borda_           | For the Borda variation of ranked choice voting.                                 |
+----------------------+----------------------------------------------------------------------------------+
| super-majority       | A candidate must get greater than 50% of the vote (e.g., three-fifths or         |
|                      | two-thirds) in order to win.                                                     |
+----------------------+----------------------------------------------------------------------------------+
| other                | Used when the vote variation type is not included in this enumeration.           |
+----------------------+----------------------------------------------------------------------------------+

.. _approval: http://en.wikipedia.org/wiki/Approval_voting
.. _cumulative: http://en.wikipedia.org/wiki/Cumulative_voting
.. _range: http://en.wikipedia.org/wiki/Range_voting
.. _rcv: http://en.wikipedia.org/wiki/Instant-runoff_voting
.. _rcv-borda: http://en.wikipedia.org/wiki/Borda_count
