.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-precinct:

Precinct
========

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:ref:`Source.VipId <multi-xml-source>`, :ref:`Locality.Name <multi-xml-locality>`, :ref:`Precinct.Ward <multi-xml-precinct>`,
:ref:`Precinct.Name <multi-xml-precinct>`, and :ref:`Precinct.Number <multi-xml-precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| BallotStyleId        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-xml-ballot-style`, which a   | then the implementation is required to   |
|                      |                                       |              |              | person who lives in this precinct will   | ignore it.                               |
|                      |                                       |              |              | vote.                                    |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictIds | ``xs:IDREFS``                         | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-xml-electoral-district`s     | then the implementation is required to   |
|                      |                                       |              |              | (e.g., congressional district, state     | ignore it.                               |
|                      |                                       |              |              | house district, school board district)   |                                          |
|                      |                                       |              |              | to which the entire precinct/precinct    |                                          |
|                      |                                       |              |              | split belongs. **Highly Recommended** if |                                          |
|                      |                                       |              |              | candidate information is to be provided. |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifier for the precinct that   | If the element is invalid or not         |
|                      |                                       |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                      |                                       |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly           | ``xs:boolean``                        | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                      |                                       |              |              | mail-only elections.                     | implementation is required to assume     |
|                      |                                       |              |              |                                          | `IsMailOnly` is false.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId           | ``xs:IDREF``                          | **Required** | Single       | Links to the :ref:`multi-xml-locality`   | If the field is invalid or not present,  |
|                      |                                       |              |              | that comprises the precinct.             | the implementation is required to ignore |
|                      |                                       |              |              |                                          | the precinct element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | ``xs:string``                         | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid or not present,  |
|                      |                                       |              |              | if no name exists).                      | the implementation is required to ignore |
|                      |                                       |              |              |                                          | the precinct element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number               | ``xs:string``                         | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                      |                                       |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                      |                                       |              |              | legal). Should be used if the `Name`     | ignore it.                               |
|                      |                                       |              |              | field is populated by a name and not a   |                                          |
|                      |                                       |              |              | number.                                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds   | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the precinct's       | If the field is invalid or not present,  |
|                      |                                       |              |              | :ref:`multi-xml-polling-location`        | then the implementation is required to   |
|                      |                                       |              |              | object(s).                               | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName    | ``xs:string``                         | Optional     | Single       | If this field is empty, then this        | If the field is invalid or not present,  |
|                      |                                       |              |              | `Precinct` object represents a full      | then the implementation is required to   |
|                      |                                       |              |              | precinct. If this field is present, then | ignore it.                               |
|                      |                                       |              |              | this `Precinct` object represents one    |                                          |
|                      |                                       |              |              | portion of a split precinct. Each        |                                          |
|                      |                                       |              |              | `Precinct` object that represents one    |                                          |
|                      |                                       |              |              | portion of a split precinct **must**     |                                          |
|                      |                                       |              |              | have the same `Name` value, but          |                                          |
|                      |                                       |              |              | different `PrecinctSplitName` values.    |                                          |
|                      |                                       |              |              | See the `sample_feed.xml` file for       |                                          |
|                      |                                       |              |              | examples.                                |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                 | ``xs:string``                         | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                      |                                       |              |              | contained within.                        | then the implementation is required to   |
|                      |                                       |              |              |                                          | ignore it.                               |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <Precinct id="pre90111">
      <BallotStyleId>bs00010</BallotStyleId>
      <ElectoralDistrictIds>ed60129 ed60311 ed60054</ElectoralDistrictIds>
      <IsMailOnly>false</IsMailOnly>
      <LocalityId>loc70001</LocalityId>
      <Name>203 - GEORGETOWN</Name>
      <Number>0203</Number>
      <PollingLocationIds>pl81274</PollingLocationIds>
   </Precinct>
   <!--
     Precinct split. Name and PollingLocationIds are the same but
     PrecinctSplitName is present, the ElectoralDistrictIds are different,
     and the BallotStyleId is different.
   -->
   <Precinct id="pre90348sp0000">
     <BallotStyleId>bs00002</BallotStyleId>
     <ElectoralDistrictIds>ed60129 ed60054 ed60150</ElectoralDistrictIds>
     <IsMailOnly>false</IsMailOnly>
     <LocalityId>loc70001</LocalityId>
     <Name>201 - JACK JOUETT</Name>
     <Number>0201</Number>
     <PollingLocationIds>pl00000 pl81273 pl81662</PollingLocationIds>
     <PrecinctSplitName>0000</PrecinctSplitName>
   </Precinct>
   <Precinct id="pre90348sp0001">
     <BallotStyleId>bs00015</BallotStyleId>
     <ElectoralDistrictIds>ed60129 ed60054 ed60267</ElectoralDistrictIds>
     <IsMailOnly>false</IsMailOnly>
     <LocalityId>loc70001</LocalityId>
     <Name>201 - JACK JOUETT</Name>
     <Number>0201</Number>
     <PollingLocationIds>pl00000 pl81273 pl81662</PollingLocationIds>
     <PrecinctSplitName>0001</PrecinctSplitName>
   </Precinct>
