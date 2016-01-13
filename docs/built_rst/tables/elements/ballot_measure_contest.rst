.. This file is auto-generated.  Do not edit it by hand!

+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a statement in opposition to   | If the element is invalid or not         |
|                  |                                         |              |              | the referendum. It does not necessarily  | present, then the implementation is      |
|                  |                                         |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the element is invalid or not         |
|                  |                                         |              |              | not voting) on this proposition will     | present, then the implementation is      |
|                  |                                         |              |              | have (i.e. whether abstaining is         | required to ignore it.                   |
|                  |                                         |              |              | considered a vote against it).           |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the full text of the           | If the element is invalid or not         |
|                  |                                         |              |              | referendum as it appears on the ballot.  | present, then the implementation is      |
|                  |                                         |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | ``xs:anyURI``                           | Optional     | Single       | Specifies a URI that links to additional | If the field is invalid or not present,  |
|                  |                                         |              |              | information about the referendum.        | then the implementation is required to   |
|                  |                                         |              |              |                                          | ignore it.                               |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                  |                                         |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                  |                                         |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                  |                                         |              |              | 50% plus one vote). Other common         |                                          |
|                  |                                         |              |              | thresholds are "three-fifths" and        |                                          |
|                  |                                         |              |              | "two-thirds". If there are `competing    |                                          |
|                  |                                         |              |              | initiatives`_, information about their   |                                          |
|                  |                                         |              |              | effect on the passage of the             |                                          |
|                  |                                         |              |              | BallotMeasureContest would go here.      |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a statement in favor of the    | If the element is invalid or not         |
|                  |                                         |              |              | referendum. It does not necessarily      | present, then the implementation is      |
|                  |                                         |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies a short summary of the         | If the element is invalid or not         |
|                  |                                         |              |              | referendum that is on the ballot, below  | present, then the implementation is      |
|                  |                                         |              |              | the title, but above the text.           | required to ignore it.                   |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :ref:`multi-xml-ballot-measure-type`    | Optional     | Single       | Specifies the particular type of ballot  | If the field is invalid or not present,  |
|                  |                                         |              |              | measure. Must be one of the valid        | then the implementation is required to   |
|                  |                                         |              |              | :ref:`multi-xml-ballot-measure-type`     | ignore it.                               |
|                  |                                         |              |              | options.                                 |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | ``xs:string``                           | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                  |                                         |              |              | :ref:`multi-xml-ballot-measure-type`     | then the implementation is required to   |
|                  |                                         |              |              | option, when Type is specified as        | ignore it.                               |
|                  |                                         |              |              | "other."                                 |                                          |
+------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
