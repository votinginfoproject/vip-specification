ElectoralDistrict
=================

.. todo::

   Document ElectoralDistrict

+---------------------+---------------------+-----------+----------+----------------------+----------------------------+
| Tag                 | Data Type           | Required? | Repeats? |Description           |Error Handling              |
|                     |                     |           |          |                      |                            |
+=====================+=====================+===========+==========+======================+============================+
| ExternalIdentifiers | ExternalIdentifiers | Optional  | Single   |                      |                            |
+---------------------+---------------------+-----------+----------+----------------------+----------------------------+
| Name                | xs:string           | Optional  | Single   |                      |                            |
+---------------------+---------------------+-----------+----------+----------------------+----------------------------+
| Number              | xs:integer          | Optional  | Single   |                      |                            |
+---------------------+---------------------+-----------+----------+----------------------+----------------------------+
| Type                | DistrictType        | Optional  | Single   |                      |                            |
+---------------------+---------------------+-----------+----------+----------------------+----------------------------+
| OtherType           | xs:string           | Optional  | Single   |                      |                            |
+---------------------+---------------------+-----------+----------+----------------------+----------------------------+

.. code-block:: xml
   :linenos:
      
   <ElectoralDistrict id="ed60129">
      <ExternalIdentifiers>
        <ExternalIdentifier>
          <Type>ocd-id</Type>
	  <Value>ocd-division/country:us/state:va</Value>
	</ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Commonwealth of Virginia</Name>
      <Type>state</Type>
   </ElectoralDistrict>
