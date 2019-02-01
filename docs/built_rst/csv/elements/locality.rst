.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-locality:

locality
========

The Locality object represents the jurisdiction below the :ref:`multi-csv-state` (e.g. county).

+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=======================================+==============+==============+==========================================+==========================================+
| election_administration_id | ``xs:IDREF``                          | Optional     | Single       | Links to the locality's                  | If the field is invalid or not present,  |
|                            |                                       |              |              | :ref:`multi-csv-election-administration` | then the implementation is required to   |
|                            |                                       |              |              | object.                                  | ignore it.                               |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers       | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Another identifier for a locality that   | If the element is invalid or not         |
|                            |                                       |              |              | links to another dataset (e.g.           | present, then the implementation is      |
|                            |                                       |              |              | `OCD-ID`_)                               | required to ignore it.                   |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                       | ``xs:string``                         | **Required** | Single       | Specifies the name of a locality.        | If the field is not present or invalid,  |
|                            |                                       |              |              |                                          | the implementation is required to ignore |
|                            |                                       |              |              |                                          | the Locality element containing it.      |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids       | ``xs:IDREF``                          | Optional     | Single       | Specifies a link to a set of the         | If the field is invalid or not present,  |
|                            |                                       |              |              | locality's :ref:`polling locations       | the implementation is required to ignore |
|                            |                                       |              |              | <multi-csv-polling-location>`s. If early | it. However, the implementation should   |
|                            |                                       |              |              | vote centers or ballot drop locations    | still check to see if there are any      |
|                            |                                       |              |              | are locality-wide, they should be        | polling locations associated with this   |
|                            |                                       |              |              | specified here.                          | locality's state.                        |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state_id                   | ``xs:IDREF``                          | **Required** | Single       | References the locality's                | If the field is invalid or not present,  |
|                            |                                       |              |              | :ref:`multi-csv-state`.                  | the implementation is required to ignore |
|                            |                                       |              |              |                                          | the Locality element containing.         |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                       | :ref:`multi-csv-district-type`        | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                            |                                       |              |              | county, town, et al.), which is one of   | then the implementation is required to   |
|                            |                                       |              |              | the various :ref:`DistrictType           | ignore it.                               |
|                            |                                       |              |              | enumerations <multi-csv-district-type>`. |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type                 | ``xs:string``                         | Optional     | Single       | Allows for defining a type of locality   | If the field is invalid or not present,  |
|                            |                                       |              |              | that falls outside the options listed in | then the implementation is required to   |
|                            |                                       |              |              | :ref:`DistrictType                       | ignore it.                               |
|                            |                                       |              |              | <multi-csv-district-type>`.              |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_administration_id,external_identifier_type,external_identifier_othertype,external_identifier_value,name,polling_location_ids,state_id,type,other_type
    loc001,ea123,ocd-id,,ocd-division/country:us/state:co/county:denver,Locality #1,poll001 poll002,st51,city,
    loc002,ea345,,,,Locality #2,,st51,other,unique type


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
