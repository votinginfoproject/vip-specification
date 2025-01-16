.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-style:

BallotStyle
===========

A container for the contests/measures on the ballot.

+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+===============+==============+==============+==========================================+==========================================+
| ImageUri          | ``xs:anyURI`` | Optional     | Single       | Specifies a URI that returns an image of |                                          |
|                   |               |              |              | the sample ballot.                       |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedContestIds | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    |                                          |
|                   |               |              |              | :ref:`multi-xml-ordered-contest`         |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyIds          | ``xs:IDREFS`` | Optional     | Single       | Reference to a set of                    |                                          |
|                   |               |              |              | :ref:`multi-xml-party`s.                 |                                          |
+-------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotStyle id="bs00000">
      <OrderedContestIds>oc20003 oc20004 oc20005 oc20025 oc20355 oc20449</OrderedContestIds>
   </BallotStyle>
