.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-electoral-district:

electoral_district
==================

The ``ElectoralDistrict`` object represents the geographic area in which contests are held or representation is defined. Examples of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District", or "Union School District". The geographic area that comprises an ``ElectoralDistrict`` is defined by which precincts link to the ``ElectoralDistrict``.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumber/>``, ``<ClearExternalIdentifier/>``). Name and Type are optional in overlays.

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| external_identifier | :ref:`multi-csv-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                     |                                         |              |              | district to other datasets (e.g.         | present, then the implementation is      |
|                     |                                         |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                | :ref:`multi-csv-internationalized-text` | **Required** | Single       | Name of the district. Required in main   | If the element is invalid, then the      |
|                     |                                         |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                     |                                         |              |              |                                          | ``ElectoralDistrict`` element containing |
|                     |                                         |              |              |                                          | it.                                      |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| number              | ``xs:integer``                          | Optional     | Single       | Specifies the district number of the     | If the field is invalid or not present,  |
|                     |                                         |              |              | district (e.g. 34, in the case of the    | then the implementation is required to   |
|                     |                                         |              |              | 34th State Senate District, or 5). If a  | ignore it.                               |
|                     |                                         |              |              | number is not applicable, instead of     |                                          |
|                     |                                         |              |              | leaving the field blank, leave this      |                                          |
|                     |                                         |              |              | field out of the object. Clearable in    |                                          |
|                     |                                         |              |              | overlays.                                |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| type                | :ref:`multi-csv-district-type`          | **Required** | Single       | Specifies the type of electoral area     | If the field is invalid, then the        |
|                     |                                         |              |              | (e.g. state, congressional,              | implementation is required to ignore the |
|                     |                                         |              |              | state-senate, county, school) from       | ``ElectoralDistrict`` element containing |
|                     |                                         |              |              | :ref:`multi-csv-district-type`. Required | it.                                      |
|                     |                                         |              |              | in main feed; optional in overlays.      |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| other_type          | ``xs:string``                           | Optional     | Single       | Custom district type if Type is "other". | If the field is invalid or not present,  |
|                     |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,name,number,type,other_type
    ed60129,57th House of Delegates District,57,state-house,
