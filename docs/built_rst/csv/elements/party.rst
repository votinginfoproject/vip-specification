.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party:

party
=====

This element describes a political party and the metadata associated with them. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated :ref:`multi-csv-candidate-contest` can use the **PrimaryPartyIds** field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| abbreviation         | ``xs:string``                         | Optional     | Single       | An abbreviation for the party name.      |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| color                | :ref:`multi-csv-html-color-string`    | Optional     | Single       | The preferred display color for the      |                                          |
|                      |                                       |              |              | party, for use in maps and other         |                                          |
|                      |                                       |              |              | displays.                                |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Other identifiers that link this party   |                                          |
|                      |                                       |              |              | to other related data sets (e.g. a       |                                          |
|                      |                                       |              |              | campaign finance system, etc).           |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_write_in          | ``xs:boolean``                        | Optional     | Single       | Signals if this political party is one   |                                          |
|                      |                                       |              |              | that is officially recognized by a       |                                          |
|                      |                                       |              |              | local, state, or federal organization,   |                                          |
|                      |                                       |              |              | or is a "write-in" in jurisdictions      |                                          |
|                      |                                       |              |              | which allow candidates to free-form      |                                          |
|                      |                                       |              |              | enter their political affiliation. If    |                                          |
|                      |                                       |              |              | this field is not present then it is     |                                          |
|                      |                                       |              |              | assumed to be false.                     |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| leader_person_ids    | ``xs:IDREFS``                         | Optional     | Single       | A reference of :ref:`multi-csv-person`   |                                          |
|                      |                                       |              |              | elements which are leaders of the        |                                          |
|                      |                                       |              |              | `Party`.                                 |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| logo_uri             | ``xs:anyURI``                         | Optional     | Single       | Web address of a logo to use in          |                                          |
|                      |                                       |              |              | displays.                                |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                 | ``xs:string``                         | **Required** | Single       | The name of the party.                   |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,abbreviation,color,external_identifier_type,external_identifier_othertype,external_identifier_value,is_write_in,leader_person_ids,logo_uri,name
    par01,REP,ff0000,,,,true,,http://example.com/elephant.png,Republican
    par02,DEM,0000ff,,,,false,per01,http://example.com/donkey.png,Democrat
    par03,GRN,efefef,,,,,,http://example.com/tree.png,Green
    par04,WFP,ee99aa,,,,,,http://example.com/worker.png,Working Families Party
