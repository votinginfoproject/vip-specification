.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party:

party
=====

This element describes a political party and the metadata associated with it. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated candidate contest can use the PrimaryPartyIds field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| abbreviation        | ``xs:string``                           | Optional     | Single       | An abbreviation for the party name (e.g. | If the field is invalid or not present,  |
|                     |                                         |              |              | "DEM", "REP", "LIB", "GRN").             | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| color               | :ref:`multi-csv-html-color-string`      | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                     |                                         |              |              | party, for use in maps and other         | present, then the implementation is      |
|                     |                                         |              |              | displays, as a 6-character hexadecimal   | required to ignore it.                   |
|                     |                                         |              |              | HTML color code (e.g. "0000FF" for blue, |                                          |
|                     |                                         |              |              | "FF0000" for red).                       |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifier | :ref:`multi-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                         |              |              | party to other datasets.                 | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in         | ``xs:boolean``                          | Optional     | Single       | Signals if this political party is one   | If the field is invalid or not present,  |
|                     |                                         |              |              | that is officially recognized by a       | then the implementation is required to   |
|                     |                                         |              |              | local, state, or federal organization,   | ignore it.                               |
|                     |                                         |              |              | or represents a "write-in" in            |                                          |
|                     |                                         |              |              | jurisdictions which allow candidates to  |                                          |
|                     |                                         |              |              | free-form enter their political          |                                          |
|                     |                                         |              |              | affiliation.                             |                                          |
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
