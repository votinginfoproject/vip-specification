.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-party-selection:

PartySelection
==============

This element extends :ref:`single-xml-ballot-selection-base` to
support contests in which the selections can be groups of one or more parties.

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| PartyId      | ``xs:IDREF`` | **Required** | Repeats      | One or more :ref:`single-xml-party` IDs  | If one or more parties referenced are    |
|              |              |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |              |              |              | selection.                               | implementation is required to ignore the |
|              |              |              |              |                                          | PartySelection containing it.            |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
