.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-election-notice:

ElectionNotice
==============

The ElectionNotice description. 

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`multi-xml-internationalized-text` | **Required** | Single       | NoticeText description                   | If the element is invalid, then the      |
|              |                                         |              |              |                                          | implementation is required to ignore the |
|              |                                         |              |              |                                          | ``ElectionNotice`` element containing    |
|              |                                         |              |              |                                          | it.                                      |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | ``xs:anyURI``                           | Optional     | Single       | NoticeUri description                    | If the field is invalid or not present,  |
|              |                                         |              |              |                                          | then the implementation is required to   |
|              |                                         |              |              |                                          | ignore it.                               |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
