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


.. _multi-csv-external-identifiers:

external_identifiers
--------------------

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
~~~~~~~~~~~~~~~~~~~

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


.. _multi-csv-internationalized-text:

internationalized_text
----------------------

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-csv-contest-base`

* Any element that extends :ref:`multi-csv-ballot-selection-base`

* :ref:`multi-csv-candidate`

* :ref:`multi-csv-contact-information`

* :ref:`multi-csv-election`

* :ref:`multi-csv-election-administration`

* :ref:`multi-csv-office`

* :ref:`multi-csv-party`

* :ref:`multi-csv-person`

* :ref:`multi-csv-polling-location`

* :ref:`multi-csv-source`

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| text         | ``xs:string`` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |               |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |               |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |               |              |              |                                          | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |               |              |              |                                          | element.                                 |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
