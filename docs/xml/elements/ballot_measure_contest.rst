BallotMeasureContest
====================

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends extends :doc:`ContestBase <contest_base>`.

+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| Tag              | Data Type                             | Required?   | Repeats? | Description                          | Error Handling         |
|                  |                                       |             |          |                                      |                        |
+==================+=======================================+=============+==========+======================================+========================+
| ConStatement     |:doc:`InternationalizedText            | Optional    | Single   |Specifies a statement in opposition to|If the field is invalid |
|                  |<internationalized_text>`              |             |          |the referendum. It does not           |or not present, the     |
|                  |                                       |             |          |necessarily appear on the ballot.     |implementation is       |
|                  |                                       |             |          |                                      |required to ignore it.  |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| EffectOfAbstain  |:doc:`InternationalizedText            | Optional    | Single   |Specifies what effect abstaining      |If the field is invalid |
|                  |<internationalized_text>`              |             |          |(i.e. not voting) on this proposition |or not present, the     |
|                  |                                       |             |          |will have (i.e. whether abstaining is |implementation is       |
|                  |                                       |             |          |considered a vote against it).        |required to ignore it.  |
|                  |                                       |             |          |                                      |                        |
|                  |                                       |             |          |                                      |                        |
|                  |                                       |             |          |                                      |                        |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| FullText         |:doc:`InternationalizedText            | Optional    | Single   |Specifies the full text of the        |If the field is not     |
|                  |<internationalized_text>`              |             |          |referendum as it appears on the       |present or invalid, the |
|                  |                                       |             |          |ballot.                               |implementation is       |
|                  |                                       |             |          |                                      |required to ignore it.  |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| InfoUri          |xs:anyURI                              | Optional    | Single   |Specifies a URI that links to         |If the field is invalid |
|                  |                                       |             |          |additional information about the      |or not present, the     |
|                  |                                       |             |          |referendum.                           |implementation is       |
|                  |                                       |             |          |                                      |required to ignore it.  |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| PassageThreshold |:doc:`InternationalizedText            | Optional    | Single   |Specifies the threshold of votes that |If the element is       |
|                  |<internationalized_text>`              |             |          |the referendum needs in order to      |invalid or not present, |
|                  |                                       |             |          |pass. The default is a simple majority|the implementation is   |
|                  |                                       |             |          |(i.e. 50% plus one vote). Other common|required to ignore it.  |
|                  |                                       |             |          |thresholds are "three-fifths" and     |                        |
|                  |                                       |             |          |"two-thirds". If there are `competing |                        |
|                  |                                       |             |          |initiatives`_, information about their|                        |
|                  |                                       |             |          |effect on the passage of the          |                        |
|                  |                                       |             |          |BallotMeasureContest would go here.   |                        |
|                  |                                       |             |          |                                      |                        |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| ProStatement     |:doc:`InternationalizedText            | Optional    | Single   |Specifies a statement in favor of the |If the element is       |
|                  |<internationalized_text>`              |             |          |referendum. It does not necessarily   |invalid or not present, |
|                  |                                       |             |          |appear on the ballot.                 |the implementation is   |
|                  |                                       |             |          |                                      |required to ignore it.  |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| SummaryText      |:doc:`InternationalizedText            | Optional    | Single   |Specifies a short summary of the      |If the element is       |
|                  |<internationalized_text>`              |             |          |referendum that is on the ballot,     |invalid or not present, |
|                  |                                       |             |          |below the title, but above the text.  |the implementation is   |
|                  |                                       |             |          |                                      |required to ignore it.  |
|                  |                                       |             |          |                                      |                        |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| Type             |:doc:`BallotMeasureType                | Optional    | Single   |Specifies the particular type of      |If the element is       |
|                  |<../enumerations/ballot_measure_type>` |             |          |ballot measure. Must be one of the    |invalid or not present, |
|                  |                                       |             |          |valid :doc:`BallotMeasureType         |the implementation is   |
|                  |                                       |             |          |<../enumerations/ballot_measure_type>`|required to ignore it.  |
|                  |                                       |             |          |options.                              |                        |
|                  |                                       |             |          |                                      |                        |
|                  |                                       |             |          |                                      |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+
| OtherType        | xs:string                             | Optional    | Single   |Allows for cataloging a new           |If the element is       |
|                  |                                       |             |          |:doc:`BallotMeasureType               |invalid or not present, |
|                  |                                       |             |          |<../enumerations/ballot_measure_type>`|the implementation is   |
|                  |                                       |             |          |option, when Type is specified as     |required to ignore it.  |
|                  |                                       |             |          |"other."                              |                        |
+------------------+---------------------------------------+-------------+----------+--------------------------------------+------------------------+

.. _competing initiatives: http://ballotpedia.org/Laws_governing_the_initiative_process_in_California#Competing_initiatives
