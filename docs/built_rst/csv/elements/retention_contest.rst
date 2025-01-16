.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-retention-contest:

retention_contest
=================

``RetentionContest`` extends :ref:`multi-csv-ballot-measure-contest` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| candidate_id | ``xs:IDREF`` | **Required** | Single       | Links to the :ref:`multi-csv-candidate`  |                                          |
|              |              |              |              | being retained.                          |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| office_id    | ``xs:IDREF`` | Optional     | Single       | Links to the information about the       |                                          |
|              |              |              |              | office.                                  |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
