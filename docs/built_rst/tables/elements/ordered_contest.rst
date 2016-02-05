.. This file is auto-generated.  Do not edit it by hand!

+---------------------------+---------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
| Tag                       | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                                  |
+===========================+===============+==============+==============+==========================================+=================================================+
| ContestId                 | ``xs:IDREF``  | **Required** | Single       | Links to elements that extend            | If the field is invalid or not present, the     |
|                           |               |              |              | :ref:`multi-xml-contest-base`.           | implementation is required to ignore the        |
|                           |               |              |              |                                          | ``OrderedContest`` element containing it.       |
+---------------------------+---------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
| OrderedBallotSelectionIds | ``xs:IDREFS`` | Optional     | Single       | Links to elements that extend            | If the field is invalid or not present, the     |
|                           |               |              |              | :ref:`multi-xml-ballot-selection-base`.  | implementation is required to ignore it. If an  |
|                           |               |              |              |                                          | ``OrderedBallotSelectionIds`` element is not    |
|                           |               |              |              |                                          | present, the presumed order of the selection    |
|                           |               |              |              |                                          | will be the order of                            |
|                           |               |              |              |                                          | :ref:`multi-xml-ballot-selection-base`-extended |
|                           |               |              |              |                                          | elements referenced by the underlying           |
|                           |               |              |              |                                          | :ref:`multi-xml-contest-base`-extended          |
|                           |               |              |              |                                          | elements.                                       |
+---------------------------+---------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
