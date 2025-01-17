.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-ordered-contest:

OrderedContest
==============

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:ref:`multi-xml-ballot-style` to accurate depict exactly what will show up on a particular
ballot in the proper order.

+---------------------------+---------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
| Tag                       | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                                  |
+===========================+===============+==============+==============+==========================================+=================================================+
| ContestId                 | ``xs:IDREF``  | **Required** | Single       | Links to elements that extend            |                                                 |
|                           |               |              |              | :ref:`multi-xml-contest-base`.           |                                                 |
+---------------------------+---------------+--------------+--------------+------------------------------------------+-------------------------------------------------+
| OrderedBallotSelectionIds | ``xs:IDREFS`` | Optional     | Single       | Links to elements that extend            | If the field is invalid or not present, the     |
|                           |               |              |              | :ref:`multi-xml-ballot-selection-base`.  | implementation is required to ignore it. If an  |
|                           |               |              |              |                                          | ``OrderedBallotSelectionIds`` element is not    |
|                           |               |              |              |                                          | present, the presumed order of the selection    |
|                           |               |              |              |                                          | will be the order of                            |
|                           |               |              |              |                                          | :ref:`multi-xml-ballot-selection-base`-extended |
|                           |               |              |              |                                          | elements referenced by the underlying           |
|                           |               |              |              |                                          | :ref:`multi-xml-contest-base`-extended          |
|                           |               |              |              |                                          | elements.                                       |
+---------------------------+---------------+--------------+--------------+------------------------------------------+-------------------------------------------------+

.. code-block:: xml
   :linenos:

   <OrderedContest id="oc20003abc">
      <ContestId>cc20003</ContestId>
      <OrderedBallotSelectionIds>cs10961 cs10962 cs10963</OrderedBallotSelectionIds>
   </OrderedContest>
