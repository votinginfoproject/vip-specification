.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-selection-base:

BallotSelectionBase
===================

A base model for all ballot selection types:
:ref:`multi-xml-ballot-measure-selection`,
:ref:`multi-xml-candidate-selection`, and :ref:`multi-xml-party-selection`.
Besides an id attribute, it has no additional fields.

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results.      | then the implementation is required to   |
|               |                |              |              |                                          | ignore it.                               |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
