.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-internationalized-uri:

InternationalizedUri
====================

``InternationalizedUri`` represents URIs pointing to language-specific versions of materials. It has an optional attribute ``label``.

Like ``InternationalizedText``, it supports either direct body content (fallback ``i-default``) or repeated child ``<Uri>`` elements with ``language`` attributes.

NOTE: InternationalizedUri is not supported in CSV submissions.

+--------------+-------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============================+==============+==============+==========================================+==========================================+
| Uri          | :ref:`multi-xml-language-uri` | Optional     | Repeats      | Contains a URI with a language           | If the element is invalid or not         |
|              |                               |              |              | attribute.                               | present, then the implementation is      |
|              |                               |              |              |                                          | required to ignore it.                   |
+--------------+-------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
