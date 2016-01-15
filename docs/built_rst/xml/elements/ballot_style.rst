.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-style:

BallotStyle
===========

A container for the contests/measures on the ballot.

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

.. code-block:: xml
   :linenos:

   <BallotStyle id="bs00000">
      <OrderedContestId>oc20003</OrderedContestId>
      <OrderedContestId>oc20004</OrderedContestId>
      <OrderedContestId>oc20005</OrderedContestId>
      <OrderedContestId>oc20025</OrderedContestId>
      <OrderedContestId>oc20355</OrderedContestId>
      <OrderedContestId>oc20449</OrderedContestId>
   </BallotStyle>
