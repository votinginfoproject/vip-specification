BallotMeasureContest
====================

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends extends :doc:`ContestBase <contest_base>`.

.. todo::

   Check specification to make sure FullText is a required field.

.. todo::

   Should Type be required?

+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| Tag              | Data Type                                         | Required?   | Repeats? | Description                              | Error Handling         |
|                  |                                                   |             |          |                                          |                        |
+==================+===================================================+=============+==========+==========================================+========================+
| ConStatement     |:doc:`InternationalizedText                        | Optional    | Single   |Specifies a statement in opposition to the|If the field is invalid |
|                  |<internationalized_text>`                          |             |          |referendum. It does not necessarily appear|or not present, the     |
|                  |                                                   |             |          |on the ballot.                            |implementation is       |
|                  |                                                   |             |          |                                          |required to ignore it.  |
|                  |                                                   |             |          |                                          |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| EffectOfAbstain  |:doc:`InternationalizedText                        | Optional    | Single   |Specifies what effect abstaining (i.e. not|If the field is invalid |
|                  |<internationalized_text>`                          |             |          |voting) on this proposition will have     |or not present, the     |
|                  |                                                   |             |          |(i.e. whether abstaining is considered a  |implementation is       |
|                  |                                                   |             |          |vote against it).                         |required to ignore it.  |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| FullText         |:doc:`InternationalizedText                        | **Required**| Single   |Specifies the full text of the referendum |If the field is not     |
|                  |<internationalized_text>`                          |             |          |as it appears on the ballot.              |present or invalid, the |
|                  |                                                   |             |          |                                          |implementation is       |
|                  |                                                   |             |          |                                          |required to ignore the  |
|                  |                                                   |             |          |                                          |element containing it.  |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| InfoUri          |xs:anyURI                                          | Optional    | Single   |Specifies a URI that links to additional  |If the field is invalid |
|                  |                                                   |             |          |information about the referendum.         |or not present, the     |
|                  |                                                   |             |          |                                          |implementation is       |
|                  |                                                   |             |          |                                          |required to ignore it.  |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| PassageThreshold |:doc:`InternationalizedText                        | Optional    | Single   |Specifies the threshold of votes that the |If the element is       |
|                  |<internationalized_text>`                          |             |          |referendum needs in order to pass. The    |invalid or not present, |
|                  |                                                   |             |          |default is a simple majority (i.e. 50%    |the implementation is   |
|                  |                                                   |             |          |plus one vote). Other common thresholds   |required to ignore it.  |
|                  |                                                   |             |          |are "three-fifths" and "two-thirds".      |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| ProStatement     |:doc:`InternationalizedText                        | Optional    | Single   |Specifies a statement in favor of the     |If the element is       |
|                  |<internationalized_text>`                          |             |          |referendum. It does not necessarily appear|invalid or not present, |
|                  |                                                   |             |          |on the ballot.                            |the implementation is   |
|                  |                                                   |             |          |                                          |required to ignore it.  |
|                  |                                                   |             |          |                                          |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| SummaryText      |:doc:`InternationalizedText                        | Optional    | Single   |Specifies a short summary of the          |If the element is       |
|                  |<internationalized_text>`                          |             |          |referendum that is on the ballot, below   |invalid or not present, |
|                  |                                                   |             |          |the title, but above the text.            |the implementation is   |
|                  |                                                   |             |          |                                          |required to ignore it.  |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| Type             |:doc:`BallotMeasureType                            | Optional    | Single   |Specifies the particular type of ballot   |If the element is       |
|                  |<../enumerations/ballot_measure_type>`             |             |          |measure. Must be one of the valid         |invalid or not present, |
|                  |                                                   |             |          |:doc:`ballot measure types                |the implementation is   |
|                  |                                                   |             |          |<../enumerations/ballot_measure_type>`.   |required to ignore it.  |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
|                  |                                                   |             |          |                                          |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
| OtherType        | xs:string                                         | Optional    | Single   |Allows for cataloging a new :doc:`ballot  |If the element is       |
|                  |                                                   |             |          |measure type                              |invalid or not present, |
|                  |                                                   |             |          |<../enumerations/ballot_measure_type>` of |the implementation is   |
|                  |                                                   |             |          |ballot measure when Type is specified as  |required to ignore it.  |
|                  |                                                   |             |          |"other."                                  |                        |
+------------------+---------------------------------------------------+-------------+----------+------------------------------------------+------------------------+
