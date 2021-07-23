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
| LocalityId           | ``xs:IDREF``                          | **Required** | Single       | Links to the :ref:`multi-xml-locality`   | If the field is invalid, then the        |
|                      |                                       |              |              | that comprises the precinct.             | implementation is required to ignore the |
|                      |                                       |              |              |                                          | ``Precinct`` element containing it.      |
+----------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | ``xs:string``                         | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid, then the        |
|                      |                                       |              |              | if no name exists).                      | implementation is required to ignore the |
|                      |                                       |              |              |                                          | ``Precinct`` element containing it.      |
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
| SpatialBoundary      | :ref:`multi-xml-spatial-boundary`     | Optional     | Single       | Defines the spatial boundary of the      | If the element is invalid or not         |
|                      |                                       |              |              | precinct. All voter addresses contained  | present, then the implementation is      |
|                      |                                       |              |              | within this boundary are assigned to the | required to ignore it.                   |
|                      |                                       |              |              | precinct. If a voter address also maps   |                                          |
|                      |                                       |              |              | to a :doc:`StreetSegment                 |                                          |
|                      |                                       |              |              | <street_segment>`, then the precinct     |                                          |
|                      |                                       |              |              | assignment from the StreetSegment will   |                                          |
|                      |                                       |              |              | be preferred over the assignment from    |                                          |
|                      |                                       |              |              | the spatial boundary.                    |                                          |
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
      <SpatialBoundary>
        <ExternalGeospatialFeature>
          <ExternalFileId>ef1</ExternalFileId>
          <FileFormat>shp</FileFormat>
          <ShapeIdentifier>3</ShapeIdentifier>
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
| ExternalGeospatialFeature | :ref:`multi-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                           |                                              |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                           |                                              |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                           |                                              |              |              |                                          | it.                                      |
+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <ShapeIdentifier>3</ShapeIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>


.. _multi-xml-external-geospatial-feature:

ExternalGeospatialFeature
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+====================================+==============+==============+==========================================+==========================================+
| ExternalFileId  | ``xs:IDREF``                       | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                 |                                    |              |              | :ref:`multi-xml-external-file`           | implementation is required to ignore the |
|                 |                                    |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                 |                                    |              |              | define the feature's boundary.           | containing it.                           |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat      | :ref:`multi-xml-geospatial-format` | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                 |                                    |              |              |                                          | implementation is required to ignore the |
|                 |                                    |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                 |                                    |              |              |                                          | containing it.                           |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ShapeIdentifier | ``xs:string``                      | **Required** | Repeats      | Identifiers indicating which specific    | If the field is invalid, then the        |
|                 |                                    |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                 |                                    |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                 |                                    |              |              | the referenced external file. This is a  | containing it.                           |
|                 |                                    |              |              | repeated field in the XML specification, |                                          |
|                 |                                    |              |              | but a scalar field in the CSV            |                                          |
|                 |                                    |              |              | specification. If more than one          |                                          |
|                 |                                    |              |              | identifier is required with the CSV      |                                          |
|                 |                                    |              |              | specifiation, multiple values can be     |                                          |
|                 |                                    |              |              | provided by delimited by space.          |                                          |
+-----------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <ExternalGeospatialFeature>
      <ExternalFileId>ef1</ExternalFileId>
      <FileFormat>shp</FileFormat>
      <ShapeIdentifier>0</ShapeIdentifier>
      <ShapeIdentifier>7</ShapeIdentifier>
      <ShapeIdentifier>9</ShapeIdentifier>
    </ExternalGeospatialFeature>
