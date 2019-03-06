.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-state:

state
=====

The State object includes state-wide election information. The ID attribute is
recommended to be the state's FIPS code, along with the prefix "st".

+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=======================================+==============+==============+==========================================+==========================================+
| election_administration_id | ``xs:IDREF``                          | Optional     | Single       | Links to the state's election            | If the field is invalid or not present,  |
|                            |                                       |              |              | administration object.                   | then the implementation is required to   |
|                            |                                       |              |              |                                          | ignore it.                               |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| external_identifiers       | :ref:`multi-csv-external-identifiers` | Optional     | Single       | Other identifier for the state that      | If the element is invalid or not         |
|                            |                                       |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                            |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                       | ``xs:string``                         | **Required** | Single       | Specifiers the name of a state, such as  | If the field is invalid, then the        |
|                            |                                       |              |              | Alabama.                                 | implementation is required to ignore it. |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_location_ids       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the state's          | If the field is invalid or not present,  |
|                            |                                       |              |              | :ref:`polling locations                  | then the implementation is required to   |
|                            |                                       |              |              | <multi-csv-polling-location>`. If early  | ignore it.                               |
|                            |                                       |              |              | vote centers or ballot drop locations    |                                          |
|                            |                                       |              |              | are state-wide (e.g., anyone in the      |                                          |
|                            |                                       |              |              | state can use them), they can be         |                                          |
|                            |                                       |              |              | specified here, but you are encouraged   |                                          |
|                            |                                       |              |              | to only use the                          |                                          |
|                            |                                       |              |              | :ref:`multi-csv-precinct` element.       |                                          |
+----------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,election_administration_id,external_identifier_type,external_identifier_othertype,external_identifier_value,name,polling_location_ids
    st51,ea123,ocd-id,,ocd-division/country:us/state:va,Virginia,
