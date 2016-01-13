.. This file is auto-generated.  Do not edit it by hand!

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Text         | :ref:`multi-xml-language-string` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |                                  |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |                                  |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |                                  |              |              |                                          | present, the implementation is required  |
|              |                                  |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |                                  |              |              |                                          | element.                                 |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
