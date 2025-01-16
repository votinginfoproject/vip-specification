.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-ballot-style:

ballot_style
============

A container for the contests/measures on the ballot.

+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===============+==============+==============+==========================================+==========================================+
| image_uri            | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that returns an image of |                                          |
|                      |               |              |              | the sample ballot.                       |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ordered_contests_ids | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    |                                          |
|                      |               |              |              | :ref:`multi-csv-ordered-contest`         |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| party_ids            | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    |                                          |
|                      |               |              |              | :ref:`multi-csv-party`s.                 |                                          |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,image_uri,ordered_contest_ids,party_ids
    bs00010,http://i.giphy.com/26BoCh3PgT8ai45ji.gif,oc2025,par02
    bs00011,http://i.giphy.com/3oEjHYDWEICgEpAOjK.gif,oc3000 oc2025,par01
