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

Voters can be assigned to a precinct in two ways. A voter location modeled by :doc:`StreetSegment <street_segment>`
is assigned to a precinct by :doc:`StreetSegment.PrecinctId <street_segment>`.
Alternatively, a precinct's spatial boundary can be modeled with :doc:`Precinct.SpatialBoundary  <precinct>`.
Any registered voter address contained within the spatial boundary of the precinct
is assigned to that precinct.

+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=======================================+==============+==============+==========================================+==========================================+
| BallotStyleId        | ``xs:IDREF``                          | Optional     | Single       | Links to the                             |                                          |
|                      |                                       |              |              | :ref:`multi-xml-ballot-style`, which a   |                                          |
|                      |                                       |              |              | person who lives in this precinct will   |                                          |
|                      |                                       |              |              | vote.                                    |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictIds | ``xs:IDREFS``                         | Optional     | Single       | Links to the                             |                                          |
|                      |                                       |              |              | :ref:`multi-xml-electoral-district`s     |                                          |
|                      |                                       |              |              | (e.g., congressional district, state     |                                          |
|                      |                                       |              |              | house district, school board district)   |                                          |
|                      |                                       |              |              | to which the entire precinct/precinct    |                                          |
|                      |                                       |              |              | split belongs. **Highly Recommended** if |                                          |
|                      |                                       |              |              | candidate information is to be provided. |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :ref:`multi-xml-external-identifiers` | Optional     | Single       | Other identifier for the precinct that   |                                          |
|                      |                                       |              |              | relates to another dataset (e.g.         |                                          |
|                      |                                       |              |              | `OCD-ID`_).                              |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly           | ``xs:boolean``                        | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                      |                                       |              |              | mail-only elections.                     | implementation is required to assume     |
|                      |                                       |              |              |                                          | `IsMailOnly` is false.                   |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId           | ``xs:IDREF``                          | **Required** | Single       | Links to the :ref:`multi-xml-locality`   |                                          |
|                      |                                       |              |              | that comprises the precinct.             |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | ``xs:string``                         | **Required** | Single       | Specifies the precinct's name (or number |                                          |
|                      |                                       |              |              | if no name exists).                      |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number               | ``xs:string``                         | Optional     | Single       | Specifies the precinct's number (e.g.,   |                                          |
|                      |                                       |              |              | 32 or 32A -- alpha characters are        |                                          |
|                      |                                       |              |              | legal). Should be used if the `Name`     |                                          |
|                      |                                       |              |              | field is populated by a name and not a   |                                          |
|                      |                                       |              |              | number.                                  |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds   | ``xs:IDREFS``                         | Optional     | Single       | Specifies a link to the precinct's       |                                          |
|                      |                                       |              |              | :ref:`multi-xml-polling-location`        |                                          |
|                      |                                       |              |              | object(s).                               |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName    | ``xs:string``                         | Optional     | Single       | If this field is empty, then this        |                                          |
|                      |                                       |              |              | `Precinct` object represents a full      |                                          |
|                      |                                       |              |              | precinct. If this field is present, then |                                          |
|                      |                                       |              |              | this `Precinct` object represents one    |                                          |
|                      |                                       |              |              | portion of a split precinct. Each        |                                          |
|                      |                                       |              |              | `Precinct` object that represents one    |                                          |
|                      |                                       |              |              | portion of a split precinct **must**     |                                          |
|                      |                                       |              |              | have the same `Name` value, but          |                                          |
|                      |                                       |              |              | different `PrecinctSplitName` values.    |                                          |
|                      |                                       |              |              | See the `sample_feed.xml` file for       |                                          |
|                      |                                       |              |              | examples.                                |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SpatialBoundary      | :ref:`multi-xml-spatial-boundary`     | Optional     | Single       | Defines the spatial boundary of the      |                                          |
|                      |                                       |              |              | precinct. All voter addresses contained  |                                          |
|                      |                                       |              |              | within this boundary are assigned to the |                                          |
|                      |                                       |              |              | precinct. If a voter address also maps   |                                          |
|                      |                                       |              |              | to a :doc:`StreetSegment                 |                                          |
|                      |                                       |              |              | <street_segment>`, then the precinct     |                                          |
|                      |                                       |              |              | assignment from the StreetSegment will   |                                          |
|                      |                                       |              |              | be preferred over the assignment from    |                                          |
|                      |                                       |              |              | the spatial boundary.                    |                                          |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                 | ``xs:string``                         | Optional     | Single       | Specifies the ward the precinct is       |                                          |
|                      |                                       |              |              | contained within.                        |                                          |
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
      <SpatialBoundary>
        <ExternalGeospatialFeature>
          <ExternalFileId>ef1</ExternalFileId>
          <FileFormat>shp</FileFormat>
          <FeatureIdentifier>
              <Index>3</Index>
          </FeatureIdentifier>
        </ExternalGeospatialFeature>
      </SpatialBoundary>
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


.. _multi-xml-spatial-boundary:

SpatialBoundary
---------------

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                       | Data Type                                    | Required?    | Repeats?     | Description                              | Error Handling                           |
+===========================+==============================================+==============+==============+==========================================+==========================================+
| ExternalGeospatialFeature | :ref:`multi-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        |                                          |
|                           |                                              |              |              | geospatial feature that is external to   |                                          |
|                           |                                              |              |              | the VIP feed.                            |                                          |
+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <FeatureIdentifier>
          <Index>3</Index>
        </FeatureIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>


.. _multi-xml-external-geospatial-feature:

ExternalGeospatialFeature
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=====================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                        | **Required** | Single       | Links to the                             |                                          |
|                   |                                     |              |              | :ref:`multi-xml-external-file`           |                                          |
|                   |                                     |              |              | containing the geospatial shape(s) that  |                                          |
|                   |                                     |              |              | define the feature's boundary.           |                                          |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`multi-xml-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       |                                          |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`multi-xml-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    |                                          |
|                   |                                     |              |              | shape(s) to use from the geospatial      |                                          |
|                   |                                     |              |              | file. These refer to identifiers within  |                                          |
|                   |                                     |              |              | the referenced external file. This is a  |                                          |
|                   |                                     |              |              | repeated field in the XML specification, |                                          |
|                   |                                     |              |              | but a scalar field in the CSV            |                                          |
|                   |                                     |              |              | specification. If more than one          |                                          |
|                   |                                     |              |              | identifier is required with the CSV      |                                          |
|                   |                                     |              |              | specifiation, multiple values can be     |                                          |
|                   |                                     |              |              | provided by delimited by space.          |                                          |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-feature-identifier:

FeatureIdentifier
^^^^^^^^^^^^^^^^^

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| Index        | ``xs:int``   | Optional     | Single       | The index value for the shapefile        |                                          |
|              |              |              |              | feature.                                 |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
