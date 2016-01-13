.. This file is auto-generated.  Do not edit it by hand!

+--------------------------+--------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
| Tag                      | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                                   |
+==========================+==============+==============+==============+==========================================+==================================================+
| ContestId                | ``xs:IDREF`` | **Required** | Single       | Links to elements that extend            | If the field is invalid or not present, the      |
|                          |              |              |              | :ref:`single-xml-contest-base`.          | implementation is required to ignore the         |
|                          |              |              |              |                                          | ``OrderedContest`` element containing it.        |
+--------------------------+--------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
| OrderedBallotSelectionId | ``xs:IDREF`` | Optional     | Repeats      | Links to elements that extend            | If the field is invalid or not present, the      |
|                          |              |              |              | :ref:`single-xml-ballot-selection-base`. | implementation is required to ignore it. If no   |
|                          |              |              |              |                                          | ``OrderedBallotSelectionId`` elements are        |
|                          |              |              |              |                                          | present, the presumed order of the selection     |
|                          |              |              |              |                                          | will be the order of                             |
|                          |              |              |              |                                          | :ref:`single-xml-ballot-selection-base`-extended |
|                          |              |              |              |                                          | elements referenced by the underlying            |
|                          |              |              |              |                                          | :ref:`single-xml-contest-base`-extended          |
|                          |              |              |              |                                          | elements.                                        |
+--------------------------+--------------+--------------+--------------+------------------------------------------+--------------------------------------------------+
