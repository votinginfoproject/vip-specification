.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ballot-style:

BallotStyle
===========

A container for the contests/measures on the ballot.

+-------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+========================================+==============+==============+==========================================+==========================================+
| ImageUri          | :ref:`multi-xml-internationalized-uri` | Optional     | Single       | Specifies a URI that returns an image of | If the element is invalid or not         |
|                   |                                        |              |              | the sample ballot.                       | present, then the implementation is      |
|                   |                                        |              |              |                                          | required to ignore it.                   |
+-------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedContestIds | ``xs:IDREFS``                          | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                   |                                        |              |              | :ref:`multi-xml-ordered-contest`         | then the implementation is required to   |
|                   |                                        |              |              |                                          | ignore it.                               |
+-------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyIds          | ``xs:IDREFS``                          | Optional     | Single       | Reference to a set of                    | If the field is invalid or not present,  |
|                   |                                        |              |              | :ref:`multi-xml-party`s.                 | then the implementation is required to   |
|                   |                                        |              |              |                                          | ignore it.                               |
+-------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotStyle id="bs00000">
      <OrderedContestIds>oc20003 oc20004 oc20005 oc20025 oc20355 oc20449</OrderedContestIds>
   </BallotStyle>
