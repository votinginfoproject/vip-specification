.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-electoral-district:

electoral_district
==================

The ``ElectoralDistrict`` object represents the geographic area in which contests are held. Examples
of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District",
or "Union School District". The geographic area that comprises a ``ElectoralDistrict`` is defined by
which precincts link to the ``ElectoralDistrict``.

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| external_identifiers | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Other identifiers that link to external  | If the element is invalid or not         |
|                      |                                       |              |              | datasets (e.g. `OCD-IDs`_)               | present, then the implementation is      |
|                      |                                       |              |              |                                          | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                 | ``xs:string``                         | **Required** | Single       | Specifies the electoral area's name.     | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore the ``ElectoralDistrict`` object  |
|                      |                                       |              |              |                                          | containing it.                           |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number               | ``xs:integer``                        | Optional     | Single       | Specifies the district number of the     | If the field is invalid or not present,  |
|                      |                                       |              |              | district (e.g. 34, in the case of the    | then the implementation is required to   |
|                      |                                       |              |              | 34th State Senate District). If a number | ignore it.                               |
|                      |                                       |              |              | is not applicable, instead of leaving    |                                          |
|                      |                                       |              |              | the field blank, leave this field out of |                                          |
|                      |                                       |              |              | the object; empty strings are not valid  |                                          |
|                      |                                       |              |              | for xs:integer fields.                   |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                 | :ref:`multi-csv-district-type`        | **Required** | Single       | Specifies the type of electoral area.    | If the field is invalid or not present,  |
|                      |                                       |              |              |                                          | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore the ``ElectoralDistrict`` object  |
|                      |                                       |              |              |                                          | containing it.                           |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type           | ``xs:string``                         | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-csv-district-type` option    | then the implementation is required to   |
|                      |                                       |              |              | when ``Type`` is specified as "other".   | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,external_identifier_type,external_identifier_othertype,external_identifier_value,name,number,type,other_type
    ed001,ocd-id,,ocd-division/country:us/state:ny/borough:brooklyn,Brooklyn,1,borough,
    ed002,other,community-board,4,CB 4,2,other,community-board


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
