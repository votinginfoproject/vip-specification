.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-checksum:

checksum
========

The ``Checksum`` object contains information about a cryptographic checksum, including
the raw checksum value and the cryptographic hash algorithm used to compute it.

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| algorithm    | :ref:`multi-csv-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to | If the field is invalid, then the        |
|              |                                     |              |              | compute the checksum value.              | implementation is required to ignore the |
|              |                                     |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``                       | **Required** | Single       | The raw cryptographic checksum value.    | If the field is invalid, then the        |
|              |                                     |              |              |                                          | implementation is required to ignore the |
|              |                                     |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,algorithm,value
    ch1,sha-256,65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e
