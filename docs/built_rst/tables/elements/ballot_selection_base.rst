.. This file is auto-generated.  Do not edit it by hand!

+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============+================+==============+==============+==========================================+==========================================+
| SequenceOrder | ``xs:integer`` | Optional     | Single       | The order in which a selection can be    | If the field is invalid or not present,  |
|               |                |              |              | listed on the ballot or in results. This | then the implementation is required to   |
|               |                |              |              | is the default ordering, and can be      | ignore it.                               |
|               |                |              |              | overridden by `OrderedBallotSlectionIds` |                                          |
|               |                |              |              | in :ref:`multi-xml-ordered-contest`.     |                                          |
+---------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
