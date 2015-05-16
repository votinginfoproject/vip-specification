BallotMeasureSelection
======================

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:doc:`BallotMeasureContest <ballot_measure_contest>` that would appear on the ballot.
BallotMeasureSelection extends :doc:`BallotSelectionBase <ballot_selection_base>`.

+-----------+----------------------------+--------------+----------+--------------------------+--------------------------+
| Tag       | Data Type                  | Required?    | Repeats? | Description              | Error Handling           |
|           |                            |              |          |                          |                          |
+===========+============================+==============+==========+==========================+==========================+
| Selection |:doc:`InternationalizedText | **Required** | Single   |Selection text for a      |If the element is invalid |
|           |<internationalized_text>`   |              |          |:doc:`BallotMeasureContest|or not present, the       |
|           |                            |              |          |<ballot_measure_contest>` |implementation is required|
|           |                            |              |          |                          |to ignore the             |
|           |                            |              |          |                          |BallotMeasureSelection    |
|           |                            |              |          |                          |containing it.            |
+-----------+----------------------------+--------------+----------+--------------------------+--------------------------+
