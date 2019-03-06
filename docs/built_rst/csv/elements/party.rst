.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party:

party
=====

This element describes a political party and the metadata associated with them. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated :ref:`multi-csv-candidate-contest` can use the **PrimaryPartyIds** field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| abbreviation         | ``xs:string``                         | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| color                | :ref:`multi-csv-html-color-string`    | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                      |                                       |              |              | party, for use in maps and other         | present, then the implementation is      |
|                      |                                       |              |              | displays.                                | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Other identifiers that link this party   | If the element is invalid or not         |
|                      |                                       |              |              | to other related data sets (e.g. a       | present, then the implementation is      |
|                      |                                       |              |              | campaign finance system, etc).           | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in          | ``xs:boolean``                        | Optional     | Single       | Signals if this political party is one   | If the field is invalid or not present,  |
|                      |                                       |              |              | that is officially recognized by a       | then the implementation is required to   |
|                      |                                       |              |              | local, state, or federal organization,   | ignore it.                               |
|                      |                                       |              |              | or is a "write-in" in jurisdictions      |                                          |
|                      |                                       |              |              | which allow candidates to free-form      |                                          |
|                      |                                       |              |              | enter their political affiliation. If    |                                          |
|                      |                                       |              |              | this field is not present then it is     |                                          |
|                      |                                       |              |              | assumed to be false.                     |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| logo_uri             | ``xs:anyURI``                         | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                      |                                       |              |              | displays.                                | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                 | ``xs:string``                         | Optional     | Single       | The name of the party.                   | If the element is invalid or not         |
|                      |                                       |              |              |                                          | present, then the implementation is      |
|                      |                                       |              |              |                                          | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,color,external_identifier_type,external_identifier_othertype,external_identifier_value,logo_uri,name
    par01,REP,ff0000,,,,http://example.com/elephant.png,Republican
    par02,DEM,0000ff,,,,http://example.com/donkey.png,Democrat
    par03,GRN,efefef,,,,http://example.com/tree.png,Green
    par04,WFP,ee99aa,,,,http://example.com/worker.png,Working Families Party


.. _multi-csv-html-color-string:

html_color_string
-----------------

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``
