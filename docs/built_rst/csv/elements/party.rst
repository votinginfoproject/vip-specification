.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party:

party
=====

The Party object represents a political party or ballot grouping.

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| abbreviation        | ``xs:string``                           | Optional     | Single       | Abbreviation for the party name (e.g.    | If the field is invalid or not present,  |
|                     |                                         |              |              | "DEM", "REP").                           | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| color               | :ref:`multi-csv-html-color-string`      | Optional     | Single       | Six-digit hexadecimal HTML color code    | If the element is invalid or not         |
|                     |                                         |              |              | associated with the party.               | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier | :ref:`multi-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                         |              |              | party to other datasets.                 | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in         | ``xs:boolean``                          | Optional     | Single       | Indicates if the party represents        | If the field is invalid or not present,  |
|                     |                                         |              |              | write-in selections.                     | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| leader_person_ids   | ``xs:IDREFS``                           | Optional     | Single       | References to :ref:`multi-csv-person`    | If the field is invalid or not present,  |
|                     |                                         |              |              | elements for party leadership.           | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| logo_uri            | :ref:`multi-csv-internationalized-uri`  | Optional     | Single       | URI pointing to the party logo.          | If the element is invalid or not         |
|                     |                                         |              |              |                                          | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                | :ref:`multi-csv-internationalized-text` | **Required** | Single       | Official name of the party.              | If the element is invalid, then the      |
|                     |                                         |              |              |                                          | implementation is required to ignore the |
|                     |                                         |              |              |                                          | ``Party`` element containing it.         |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,abbreviation,color,is_write_in,leader_person_ids,logo_uri,name
    par0001,DEM,0000FF,false,per50001,https://example.gov/dem.png,Democratic Party
    par0002,REP,FF0000,false,per50002,https://example.gov/rep.png,Republican Party
