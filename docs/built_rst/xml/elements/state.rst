.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-state:

State
=====

The State object includes state-wide election information. The ID attribute is
recommended to be the state's FIPS code, along with the prefix "st".

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | ``xs:IDREF``                          | Optional     | Single       | Links to the state's election            | If the field is invalid or not present,  |
|                          |                                       |              |              | administration object.                   | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifier for the state that      | If the element is invalid or not         |
|                          |                                       |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                          |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | ``xs:string``                         | **Required** | Single       | Specifiers the name of a state, such as  | If the field is invalid, then the        |
|                          |                                       |              |              | Alabama.                                 | implementation is required to ignore it. |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds       | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the state's          | If the field is invalid or not present,  |
|                          |                                       |              |              | :ref:`polling locations                  | then the implementation is required to   |
|                          |                                       |              |              | <multi-xml-polling-location>`. If early  | ignore it.                               |
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


.. _multi-xml-external-identifiers:

ExternalIdentifiers
-------------------

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :ref:`multi-xml-candidate`

* Any element that extends :ref:`multi-xml-contest-base`

* :ref:`multi-xml-electoral-district`

* :ref:`multi-xml-locality`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-precinct`

* :ref:`multi-xml-state`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+======================================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | :ref:`multi-xml-external-identifier` | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                    |                                      |              |              | identifier it is (see                    | must be present for                      |
|                    |                                      |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                    |                                      |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                    |                                      |              |              |                                          | present, the implementation is required  |
|                    |                                      |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                    |                                      |              |              |                                          | element.                                 |
+--------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-external-identifier:

ExternalIdentifier
~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Type         | :ref:`multi-xml-identifier-type` | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              |                                  |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | ``xs:string``                    | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                  |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                  |              |              | outside the options listed in            | ignore it.                               |
|              |                                  |              |              | :ref:`multi-xml-identifier-type`.        |                                          |
|              |                                  |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                  |              |              | using this field.                        |                                          |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | ``xs:string``                    | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                  |              |              |                                          | the implementation is required to ignore |
|              |                                  |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                  |              |              |                                          | it.                                      |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifiers>
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:nc/county:durham</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>FIPS</Type>
         <Value>37063</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>OTHER</Type>
         <OtherType>GNIS</OtherType>
         <Value>1008550</Value>
      </ExternalIdentifier>
      <external_identifer>
         <Type>OTHER</Type>
         <OtherType>census</OtherType>
         <Value>99063</Value>
      </ExternalIdentifier>
   </ExternalIdentifiers>
