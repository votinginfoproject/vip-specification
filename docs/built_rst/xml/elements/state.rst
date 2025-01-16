.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-state:

State
=====

The State object includes state-wide election information. The ID attribute is
recommended to be the state's FIPS code, along with the prefix "st".

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the state's election            |                                          |
|                          |                                       |              |              | administration object.                   |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifier for the state that      |                                          |
|                          |                                       |              |              | relates to another dataset (e.g.         |                                          |
|                          |                                       |              |              | `OCD-ID`_).                              |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifiers the name of a state, such as  |                                          |
|                          |                                       |              |              | Alabama.                                 |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the state's          |                                          |
|                          |                                       |              |              | :ref:`polling locations                  |                                          |
|                          |                                       |              |              | <multi-xml-polling-location>`. If early  |                                          |
|                          |                                       |              |              | vote centers or ballot drop locations    |                                          |
|                          |                                       |              |              | are state-wide (e.g., anyone in the      |                                          |
|                          |                                       |              |              | state can use them), they can be         |                                          |
|                          |                                       |              |              | specified here, but you are encouraged   |                                          |
|                          |                                       |              |              | to only use the                          |                                          |
|                          |                                       |              |              | :ref:`multi-xml-precinct` element.       |                                          |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <State id="st51">
      <ElectionAdministrationId>ea40133</ElectionAdministrationId>
      <ExternalIdentifiers>
        <ExternalIdentifier>
          <Type>ocd-id</Type>
          <Value>ocd-division/country:us/state:va</Value>
        </ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Virginia</Name>
   </State>
