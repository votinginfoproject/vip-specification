.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-party-contest:

party_contest
=============

An extension of :ref:`multi-csv-contest-base` which describes a contest in
which the possible ballot selections are of type :ref:`multi-csv-party-selection`. These could include contests in which straight-party
selections are allowed, or party-list contests (although these are more common
outside of the United States).

.. code-block:: csv-table
   :linenos:


    id,abbreviation,ballot_selection_ids,ballot_sub_title,ballot_title,electoral_district_id,electorate_specification,external_identifier_type,external_identifier_othertype,external_identifier_value,has_rotation,name,sequence_order,vote_variation,other_vote_variation
    pcon001,PC1071,bs001 bs002,,Party Election,ed001,all registered voters,,,,false,Straight Party Vote,3,,


.. _multi-csv-contest-base:

contest_base
------------

A base model for all Contest types: :ref:`multi-csv-ballot-measure-contest`,
:ref:`multi-csv-candidate-contest`, :ref:`multi-csv-party-contest`,
and :ref:`multi-csv-retention-contest` (NB: the latter because it extends
:ref:`multi-csv-ballot-measure-contest`).

+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=================================+==============+==============+==========================================+==========================================+
| abbreviation             | ``xs:string``                   | Optional     | Single       | An abbreviation for the contest.         | If the field is invalid or not present,  |
|                          |                                 |              |              |                                          | then the implementation should ignore    |
|                          |                                 |              |              |                                          | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_selection_ids     | ``xs:IDREFS``                   | Optional     | Single       | References a set of BallotSelections,    | If the field is invalid or not present,  |
|                          |                                 |              |              | which could be of any selection type     | then the implementation should ignore    |
|                          |                                 |              |              | that extends                             | it.                                      |
|                          |                                 |              |              | :ref:`multi-csv-ballot-selection-base`.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_sub_title         | ``xs:string``                   | Optional     | Single       | Subtitle of the contest as it appears on | If the element is invalid or not         |
|                          |                                 |              |              | the ballot.                              | present, then the implementation should  |
|                          |                                 |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_title             | ``xs:string``                   | Optional     | Single       | Title of the contest as it appears on    | If the element is invalid or not         |
|                          |                                 |              |              | the ballot.                              | present, then the implementation should  |
|                          |                                 |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electoral_district_id    | ``xs:IDREF``                    | **Required** | Single       | References an                            | If the field is invalid, then the        |
|                          |                                 |              |              | :ref:`multi-csv-electoral-district`      | implementation should ignore it.         |
|                          |                                 |              |              | element that represents the geographical |                                          |
|                          |                                 |              |              | scope of the contest.                    |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| electorate_specification | ``xs:string``                   | Optional     | Single       | Specifies any changes to the eligible    | If the element is invalid or not         |
|                          |                                 |              |              | electorate for this contest past the     | present, then the implementation should  |
|                          |                                 |              |              | usual, "all registered voters"           | ignore it.                               |
|                          |                                 |              |              | electorate. This subtag will most often  |                                          |
|                          |                                 |              |              | be used for primaries and local          |                                          |
|                          |                                 |              |              | elections. In primaries, voters may have |                                          |
|                          |                                 |              |              | to be registered as a specific party to  |                                          |
|                          |                                 |              |              | vote, or there may be special rules for  |                                          |
|                          |                                 |              |              | which ballot a voter can pull. In some   |                                          |
|                          |                                 |              |              | local elections, non-citizens can vote.  |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers     | ``xs:string``                   | Optional     | Single       | Other identifiers for a contest that     | If the element is invalid or not         |
|                          |                                 |              |              | links to another source of information.  | present, then the implementation should  |
|                          |                                 |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_rotation             | ``xs:boolean``                  | Optional     | Single       | Indicates whether the selections in the  | If the field is invalid or not present,  |
|                          |                                 |              |              | contest are rotated.                     | then the implementation should ignore    |
|                          |                                 |              |              |                                          | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                     | ``xs:string``                   | Optional     | Single       | Name of the contest, not necessarily how | If the field is invalid or not present,  |
|                          |                                 |              |              | it appears on the ballot (NB:            | then the implementation should ignore    |
|                          |                                 |              |              | BallotTitle should be used for this      | it.                                      |
|                          |                                 |              |              | purpose).                                |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| sequence_order           | ``xs:integer``                  | Optional     | Single       | Order in which the contests are listed   | If the field is invalid or not present,  |
|                          |                                 |              |              | on the ballot. This is the default       | then the implementation should ignore    |
|                          |                                 |              |              | ordering, and can be overrides by data   | it.                                      |
|                          |                                 |              |              | in a :ref:`multi-csv-ballot-style`       |                                          |
|                          |                                 |              |              | element.                                 |                                          |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| vote_variation           | :ref:`multi-csv-vote-variation` | Optional     | Single       | Vote variation associated with the       | If the field is invalid or not present,  |
|                          |                                 |              |              | contest (e.g. n-of-m, majority, et al).  | then the implementation should ignore    |
|                          |                                 |              |              |                                          | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_vote_variation     | ``other_vote_variation``        | Optional     | Single       | If "other" is selected as the            | If the field is invalid or not present,  |
|                          |                                 |              |              | **VoteVariation**, the name of the       | then the implementation should ignore    |
|                          |                                 |              |              | variation can be specified here.         | it.                                      |
+--------------------------+---------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-external-identifiers:

external_identifiers
~~~~~~~~~~~~~~~~~~~~

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-csv-candidate`

* Any element that extends :ref:`multi-csv-contest-base`

* :ref:`multi-csv-electoral-district`

* :ref:`multi-csv-locality`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-precinct`

* :ref:`multi-csv-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+---------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+======================================+==============+==============+==========================================+==========================================+
| external_identifier | :ref:`multi-csv-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                     |                                      |              |              | identifier it is (see                    | must be present for                      |
|                     |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                     |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                     |                                      |              |              |                                          | present, the implementation is required  |
|                     |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                     |                                      |              |              |                                          | element.                                 |
+---------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-csv-external-identifier:

external_identifier
^^^^^^^^^^^^^^^^^^^

+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================+==============+==============+==========================================+==========================================+
| type         | ``identifier_type`` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                     |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                     |              |              |                                          | it.                                      |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type   | ``xs:string``       | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                     |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                     |              |              | outside the options listed in            | ignore it.                               |
|              |                     |              |              | :ref:`multi-csv-identifier-type`.        |                                          |
|              |                     |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                     |              |              | using this field.                        |                                          |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| value        | ``xs:string``       | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                     |              |              |                                          | the implementation is required to ignore |
|              |                     |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                     |              |              |                                          | it.                                      |
+--------------+---------------------+--------------+--------------+------------------------------------------+------------------------------------------+
