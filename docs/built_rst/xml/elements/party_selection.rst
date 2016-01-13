.. This file is auto-generated.  Do not edit it by hand!

.. _xml-multi-party-selection:

PartySelection
==============

This element extends :doc:`BallotSelectionBase <ballot_selection_base>` to
support contests in which the selections can be groups of one or more parties.

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| PartyId      | xs:IDREF     | **Required** | Repeats      | One or more :doc:`Party <party>` IDs     | If one or more parties referenced are    |
|              |              |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |              |              |              | selection.                               | implementation is required to ignore the |
|              |              |              |              |                                          | PartySelection containing it.            |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
