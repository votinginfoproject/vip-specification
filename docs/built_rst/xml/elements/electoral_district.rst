.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-electoral-district:

ElectoralDistrict
=================

An ElectoralDistrict represents a geographic boundary or jurisdiction for representation, contests, and offices.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearNumber/>``, ``<ClearExternalIdentifier/>``). Name and Type are optional in overlays.

+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=========================================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | :ref:`multi-xml-external-identifier`    | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                    |                                         |              |              | district to other datasets (e.g.         | present, then the implementation is      |
|                    |                                         |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name               | :ref:`multi-xml-internationalized-text` | **Required** | Single       | Name of the district. Required in main   | If the element is invalid, then the      |
|                    |                                         |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                    |                                         |              |              |                                          | ``ElectoralDistrict`` element containing |
|                    |                                         |              |              |                                          | it.                                      |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number             | ``xs:integer``                          | Optional     | Single       | Number of the district (e.g. "57").      | If the field is invalid or not present,  |
|                    |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type               | :ref:`multi-xml-district-type`          | **Required** | Single       | Type of district from                    | If the field is invalid, then the        |
|                    |                                         |              |              | :ref:`multi-xml-district-type`. Required | implementation is required to ignore the |
|                    |                                         |              |              | in main feed; optional in overlays.      | ``ElectoralDistrict`` element containing |
|                    |                                         |              |              |                                          | it.                                      |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType          | ``xs:string``                           | Optional     | Single       | Custom district type if Type is "other". | If the field is invalid or not present,  |
|                    |                                         |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                    |                                         |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectoralDistrict id="ed60129">
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:va/sldl:57</Value>
      </ExternalIdentifier>
      <Name>
         <Text language="en">Virginia's 57th House of Delegates district</Text>
      </Name>
      <Number>57</Number>
      <Type>state-house</Type>
   </ElectoralDistrict>
