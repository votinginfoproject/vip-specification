.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-internationalized-text:

InternationalizedText
=====================

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-xml-contest-base`

* Any element that extends :ref:`multi-xml-ballot-selection-base`

* :ref:`multi-xml-candidate`

* :ref:`multi-xml-contact-information`

* :ref:`multi-xml-election`

* :ref:`multi-xml-election-administration`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-person`

* :ref:`multi-xml-polling-location`

* :ref:`multi-xml-source`

NOTE: Internationalized Text is not currently supported for CSV submissions. "

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
