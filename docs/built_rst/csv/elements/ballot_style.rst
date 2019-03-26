.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ballot-style:

ballot_style
============

A container for the contests/measures on the ballot.

+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===============+==============+==============+==========================================+==========================================+
| image_uri            | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that returns an image of | If the field is invalid or not present,  |
|                      |               |              |              | the sample ballot.                       | then the implementation is required to   |
|                      |               |              |              |                                          | ignore it.                               |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ordered_contests_ids | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                      |               |              |              | :ref:`multi-csv-ordered-contest`         | then the implementation is required to   |
|                      |               |              |              |                                          | ignore it.                               |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_ids            | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                      |               |              |              | :ref:`multi-csv-party`s.                 | then the implementation is required to   |
|                      |               |              |              |                                          | ignore it.                               |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,image_uri,ordered_contest_ids,party_ids
    bs00010,http://i.giphy.com/26BoCh3PgT8ai45ji.gif,oc2025,par02
    bs00011,http://i.giphy.com/3oEjHYDWEICgEpAOjK.gif,oc3000 oc2025,par01
