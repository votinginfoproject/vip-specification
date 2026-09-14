.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-external-identifier:

external_identifier
===================

Specifies an external identifier for an entity, linking it to another dataset or system. ExternalIdentifier has optional attributes ``label`` and ``provider``.

In overlay feeds, this element is clearable using ``<ClearExternalIdentifier/>`` on elements where it is marked clearable.

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| type         | :ref:`multi-csv-identifier-type` | **Required** | Single       | Specifies the type of identifier from    | If the field is invalid or not present,  |
|              |                                  |              |              | :ref:`multi-csv-identifier-type`.        | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``                    | Optional     | Single       | Allows defining an identifier type       | If the field is invalid or not present,  |
|              |                                  |              |              | outside                                  | then the implementation is required to   |
|              |                                  |              |              | :ref:`multi-csv-identifier-type`. Type   | ignore it.                               |
|              |                                  |              |              | should be set to "other" when using this |                                          |
|              |                                  |              |              | field.                                   |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier value.          | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ExternalIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
