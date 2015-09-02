.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==============+==============+==============+==========================================+==========================================+
| ContestId                | xs:IDREF     | **Required** | Single       | Links to elements that extend            | If the field is invalid or not present,  |
|                          |              |              |              | :doc:`ContestBase <contest_base>`.       | the implementation is required to ignore |
|                          |              |              |              |                                          | the ``OrderedContest`` element           |
|                          |              |              |              |                                          | containing it.                           |
+--------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedBallotSelectionId | xs:IDREF     | Optional     | Repeats      | Links to elements that extend            | If the field is invalid or not present,  |
|                          |              |              |              | :doc:`BallotSelectionBase                | the implementation is required to ignore |
|                          |              |              |              | <ballot_selection_base>`.                | it. If no ``OrderedBallotSelectionId``   |
|                          |              |              |              |                                          | elements are present, the presumed order |
|                          |              |              |              |                                          | of the selection will be the order of    |
|                          |              |              |              |                                          | :doc:`BallotSelectionBase                |
|                          |              |              |              |                                          | <ballot_selection_base>`-extended        |
|                          |              |              |              |                                          | elements referenced by the underlying    |
|                          |              |              |              |                                          | :doc:`ContestBase                        |
|                          |              |              |              |                                          | <contest_base>`-extended elements.       |
+--------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
