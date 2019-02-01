.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-party:

Party
=====

This element describes a political party and the metadata associated with them. These can also include "dummy" parties to indicate a type of contest (e.g., a Voter Nominated :ref:`multi-xml-candidate-contest` can use the **PrimaryPartyIds** field and a dummy Party object to indicate that the contest is a "Top-Two" primary).

+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=========================================+==============+==============+==========================================+==========================================+
| Abbreviation        | ``xs:string``                           | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                     |                                         |              |              |                                          | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color               | :ref:`multi-xml-html-color-string`      | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                     |                                         |              |              | party, for use in maps and other         | present, then the implementation is      |
|                     |                                         |              |              | displays.                                | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :ref:`multi-xml-external-identifiers`   | Optional     | Single       | Other identifiers that link this party   | If the element is invalid or not         |
|                     |                                         |              |              | to other related data sets (e.g. a       | present, then the implementation is      |
|                     |                                         |              |              | campaign finance system, etc).           | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn           | ``xs:boolean``                          | Optional     | Single       | Signals if this political party is one   | If the field is invalid or not present,  |
|                     |                                         |              |              | that is officially recognized by a       | then the implementation is required to   |
|                     |                                         |              |              | local, state, or federal organization,   | ignore it.                               |
|                     |                                         |              |              | or is a "write-in" in jurisdictions      |                                          |
|                     |                                         |              |              | which allow candidates to free-form      |                                          |
|                     |                                         |              |              | enter their political affiliation. If    |                                          |
|                     |                                         |              |              | this field is not present then it is     |                                          |
|                     |                                         |              |              | assumed to be false.                     |                                          |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri             | ``xs:anyURI``                           | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                     |                                         |              |              | displays.                                | then the implementation is required to   |
|                     |                                         |              |              |                                          | ignore it.                               |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | :ref:`multi-xml-internationalized-text` | Optional     | Single       | The name of the party.                   | If the element is invalid or not         |
|                     |                                         |              |              |                                          | present, then the implementation is      |
|                     |                                         |              |              |                                          | required to ignore it.                   |
+---------------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-html-color-string:

HtmlColorString
---------------

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``

.. code-block:: xml
   :linenos:

   <Party id="par0001">
     <Abbreviation>REP</Abbreviation>
     <Color>e91d0e</Color>
     <Name>
       <Text language="en">Republican</Text>
     </Name>
   </Party>


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


.. _multi-xml-internationalized-text:

InternationalizedText
---------------------

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-xml-contest-base`

* Any element that extends :ref:`multi-xml-ballot-selection-base`

* :ref:`multi-xml-candidate`

* :ref:`multi-xml-contact-information`

* :ref:`multi-xml-election`

* :ref:`multi-xml-election-administration`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-person`

* :ref:`multi-xml-polling-location`

* :ref:`multi-xml-source`

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Text         | :ref:`multi-xml-language-string` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |                                  |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |                                  |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |                                  |              |              |                                          | present, the implementation is required  |
|              |                                  |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |                                  |              |              |                                          | element.                                 |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
