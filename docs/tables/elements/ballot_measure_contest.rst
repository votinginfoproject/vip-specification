.. This file is auto-generated.  Do not edit it by hand!

+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :doc:`InternationalizedText            | Optional     | Single       | Specifies a statement in opposition to   | If the field is invalid or not present,  |
|                  | <internationalized_text>`              |              |              | the referendum. It does not necessarily  | then the implementation is required to   |
|                  |                                        |              |              | appear on the ballot.                    | ignore it.                               |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :doc:`InternationalizedText            | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the field is invalid or not present,  |
|                  | <internationalized_text>`              |              |              | not voting) on this proposition will     | then the implementation is required to   |
|                  |                                        |              |              | have (i.e. whether abstaining is         | ignore it.                               |
|                  |                                        |              |              | considered a vote against it).           |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :doc:`InternationalizedText            | Optional     | Single       | Specifies the full text of the           | If the field is invalid or not present,  |
|                  | <internationalized_text>`              |              |              | referendum as it appears on the ballot.  | then the implementation is required to   |
|                  |                                        |              |              |                                          | ignore it.                               |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | xs:anyURI                              | Optional     | Single       | Specifies a URI that links to additional | If the field is invalid or not present,  |
|                  |                                        |              |              | information about the referendum.        | then the implementation is required to   |
|                  |                                        |              |              |                                          | ignore it.                               |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :doc:`InternationalizedText            | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                  |                                        |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                  |                                        |              |              | 50% plus one vote). Other common         |                                          |
|                  |                                        |              |              | thresholds are "three-fifths" and        |                                          |
|                  |                                        |              |              | "two-thirds". If there are `competing    |                                          |
|                  |                                        |              |              | initiatives`_, information about their   |                                          |
|                  |                                        |              |              | effect on the passage of the             |                                          |
|                  |                                        |              |              | BallotMeasureContest would go here.      |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :doc:`InternationalizedText            | Optional     | Single       | Specifies a statement in favor of the    | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum. It does not necessarily      | present, then the implementation is      |
|                  |                                        |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :doc:`InternationalizedText            | Optional     | Single       | Specifies a short summary of the         | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum that is on the ballot, below  | present, then the implementation is      |
|                  |                                        |              |              | the title, but above the text.           | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :doc:`BallotMeasureType                | Optional     | Single       | Specifies the particular type of ballot  | If the element is invalid or not         |
|                  | <../enumerations/ballot_measure_type>` |              |              | measure. Must be one of the valid        | present, then the implementation is      |
|                  |                                        |              |              | :doc:`BallotMeasureType                  | required to ignore it.                   |
|                  |                                        |              |              | <../enumerations/ballot_measure_type>`   |                                          |
|                  |                                        |              |              | options.                                 |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | xs:string                              | Optional     | Single       | Allows for cataloging a new              | If the element is invalid or not         |
|                  |                                        |              |              | :doc:`BallotMeasureType                  | present, then the implementation is      |
|                  |                                        |              |              | <../enumerations/ballot_measure_type>`   | required to ignore it.                   |
|                  |                                        |              |              | option, when Type is specified as        |                                          |
|                  |                                        |              |              | "other."                                 |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
