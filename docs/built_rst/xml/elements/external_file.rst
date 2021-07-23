.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-external-file:

ExternalFile
============

The ``ExternalFile`` object holds a reference to a file external to the feed itself. 
External files are packaged along with the VIP feed into a single, archived file. 

+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                 | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===========================+==============+==============+==========================================+==========================================+
| Filename     | ``xs:string``             | **Required** | Single       | The name of the external file.           | If the field is invalid, then the        |
|              |                           |              |              |                                          | implementation is required to ignore the |
|              |                           |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Checksum     | :ref:`multi-xml-checksum` | **Required** | Single       | The cryptographic checksum of the        | If the element is invalid, then the      |
|              |                           |              |              | referenced external file.                | implementation is required to ignore the |
|              |                           |              |              |                                          | ``ExternalFile`` element containing it.  |
+--------------+---------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalFile id="ef1">
      <Filename>precinct_shapes.zip</Filename>
      <Checksum>
        <Algorithm>sha-256</Algorithm>
        <Value>65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e</Value>
      </Checksum>
   </State>


.. _multi-xml-checksum:

Checksum
--------

The ``Checksum`` object contains information about a cryptographic checksum, including
the raw checksum value and the cryptographic hash algorithm used to compute it.

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| Algorithm    | :ref:`multi-xml-checksum-algorithm` | **Required** | Single       | The cryptographic hash algorithm used to | If the field is invalid, then the        |
|              |                                     |              |              | compute the checksum value.              | implementation is required to ignore the |
|              |                                     |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                       | **Required** | Single       | The raw cryptographic checksum value.    | If the field is invalid, then the        |
|              |                                     |              |              |                                          | implementation is required to ignore the |
|              |                                     |              |              |                                          | ``Checksum`` element containing it.      |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <Checksum>
      <Algorithm>sha-256</Algorithm>
      <Value>65b634c5037f8a344616020d8060d233daa37b0f032a71d0d15ad7a5d3afa68e</Value>
    </Checksum>
