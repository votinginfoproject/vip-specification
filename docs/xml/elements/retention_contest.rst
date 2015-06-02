RetentionContest
================

``RetentionContest`` extends :doc:`BallotMeasureContest <ballot_measure_contest>` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+-------------+------------+------------+----------+----------------------+----------------------------+
| Tag         | Data Type  | Required?  | Repeats? |Description           |Error Handling              |
|             |            |            |          |                      |                            |
+=============+============+============+==========+======================+============================+
| CandidateId | xs:IDREF   |**Required**| Single   |Links to the          |If the field is invalid or  |
|             |            |            |          |:doc:`Candidate       |not present, the            |
|             |            |            |          |<candidate>` being    |implementation is required  |
|             |            |            |          |retained.             |to ignore the               |
|             |            |            |          |                      |``RetentionContest`` element|
|             |            |            |          |                      |containing it.              |
+-------------+------------+------------+----------+----------------------+----------------------------+
| OfficeId    | xs:IDREF   | Optional   | Single   |Links to the          |If the field is invalid or  |
|             |            |            |          |information about the |not present, the            |
|             |            |            |          |office.               |implementation is required  |
|             |            |            |          |                      |to ignore it.               |
+-------------+------------+------------+----------+----------------------+----------------------------+
