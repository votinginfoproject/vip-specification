.. This file is auto-generated.  Do not edit it by hand!

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| ImageUri          | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that returns an image of | If the field is invalid or not present,  |
|                   |               |              |              | the sample ballot.                       | then the implementation is required to   |
|                   |               |              |              |                                          | ignore it.                               |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedContestIds | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                   |               |              |              | :ref:`multi-xml-ordered-contest`s        | then the implementation is required to   |
|                   |               |              |              |                                          | ignore it.                               |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyIds          | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                   |               |              |              | :ref:`multi-xml-party`s.                 | then the implementation is required to   |
|                   |               |              |              |                                          | ignore it.                               |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
