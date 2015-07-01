.. This file is auto-generated.  Do not edit it by hand!

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| PartyId      | xs:IDREF     | **Required** | Repeats      | One or more :doc:`Party <party>` IDs     | If one or more parties referenced are    |
|              |              |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |              |              |              | selection.                               | implementation is required to ignore the |
|              |              |              |              |                                          | PartySelection containing it.            |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
