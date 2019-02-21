.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-internationalized-text:

internationalized_text
======================

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-csv-contest-base`

* Any element that extends :ref:`multi-csv-ballot-selection-base`

* :ref:`multi-csv-candidate`

* :ref:`multi-csv-contact-information`

* :ref:`multi-csv-election`

* :ref:`multi-csv-election-administration`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-person`

* :ref:`multi-csv-polling-location`

* :ref:`multi-csv-source`

NOTE: Internationalized Text is not currently supported for CSV submissions. 

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| text         | ``xs:string`` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |               |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |               |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |               |              |              |                                          | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |               |              |              |                                          | element.                                 |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
