.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-external-file:

external_file
=============

The ``ExternalFile`` object holds a reference to a file external to the feed itself. 
External files are packaged along with the VIP feed into a single, archived file. 

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| file_uri     | ``xs:anyURI`` | **Required** | Single       | The URI of the external file.            |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| checksum_id  | ``xs:IDREF``  | **Required** | Single       | The cryptographic checksum of the        |                                          |
|              |               |              |              | referenced external file.                |                                          |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,file_uri,checksum_id
    ef1,precinct_shapes.zip,ch1
