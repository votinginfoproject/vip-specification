.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-external-identifier:

external_identifier
===================

+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================+==============+==============+==========================================+==========================================+
| type         | ``identifier_type`` | **Required** | Single       | Specifies the type of identifier. Must   |                                          |
|              |                     |              |              | be one of the valid types as defined by  |                                          |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``       | Optional     | Single       | Allows for cataloging an                 |                                          |
|              |                     |              |              | ``ExternalIdentifier`` type that falls   |                                          |
|              |                     |              |              | outside the options listed in            |                                          |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        |                                          |
|              |                     |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                     |              |              | using this field.                        |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``       | **Required** | Single       | Specifies the identifier.                |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
