Data Best Practices
=======================

Following is a series of best practice for data collection and file creation and suggestions about best practices of
formatting data within your VIP XML and CSV file.

.. _naming-convention:

Naming convention
-----------------

While many of the Voting Information Project's data processes are managed by software,
the quality of the entire system relies on human intervention, especially for error reporting
and quality control. For this reason, VIP files should follow a naming convention that
describes the contents of each individual feed file in an accessible way.

The file containing the VIP feed should be named using the following convention:

.. code-block:: none

   vipfeed-${FIPS}-${ELECTION_DATE}-${STATE}[-${LOCAL}].{xml|zip}

An explanation of each of the segments of the file naming convention above are as follows:

- ``${FIPS}`` - The `FIPS code`_ for the jurisdiction.
- ``${ELECTION_DATE}`` - The date of the election in `ISO 8601`_ format.
- ``${STATE}`` - The full state name (e.g. Alaska, Arkansas, etc...) and not the abbreviation. If
  there are spaces in the state name, they should be substituted with underscores (e.g. New York ->
  New_York).
- ``${LOCAL}`` (optional) - This additional identifier should be used if the file contains data
  from a specific jurisdiction. As with ``${STATE}`` above, all spaces should be substituted with
  underscores. For example, if the data contained in the file only covers Maricopa County, AZ for
  the November 6, 2012 election, the file name would be
  ``vipfeed-04013-2012-11-06-Arizona-Maricopa_County.xml``.
- ``{xml|zip}`` - If the file is an uncompressed XML document, the extension should be ``.xml.`` If
  the file is zipped, the file extension should end with ``.zip``.

For a final example, ``vipfeed-19-2012-11-06-Iowa.zip`` denotes Iowa's (**NB:** the FIPS code
for IA is 19) feed for the Nov 6, 2012 election that has been compressed.

.. _FIPS code: https://en.wikipedia.org/wiki/FIPS_county_code
.. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601




Element Identifiers
-------------------

Most elements within the VIP feed require unique identifiers, `xs:ID`_ data types. Conformance to ``xs:ID`` requires 
the identifying record to:
  - begin with a letter or underscore
  - only contain letters, digits, hyphens and periods
  - be unique across the VIP data set

  .. _xs:ID: http://www.datypic.com/sc/xsd/t-xsd_ID.html

In order to maintain uniqueness
and provide context for the identifiers, the best practice is to use `Hungarian-Style`_ notation for identifiers.

ID values should follow Hungarian-Style notation, were the identifier prefix implicitly names the data element.  Below
is a list of preferred prefixes by element (e.g. par00001 for a ``Party`` ``id``):

+----------------------------------------+---------------------------------------+
| Element                                | Prefix                                |
|                                        |                                       |
+========================================+=======================================+
| BallotMeasureContest                   | bmc                                   |
+----------------------------------------+---------------------------------------+
| BallotMeasureSelection                 | bms                                   |
+----------------------------------------+---------------------------------------+
| BallotStyle                            | bs                                    |
+----------------------------------------+---------------------------------------+
| Candidate                              | can                                   |
+----------------------------------------+---------------------------------------+
| CandidateContest                       | cc                                    |
+----------------------------------------+---------------------------------------+
| CandidateSelection                     | cs                                    |
+----------------------------------------+---------------------------------------+
| ContactInformation                     | ci                                    |
+----------------------------------------+---------------------------------------+
| Election                               | ele                                   |
+----------------------------------------+---------------------------------------+
| ElectionAdministration                 | ea                                    |
+----------------------------------------+---------------------------------------+
| ElectoralDistrict                      | ed                                    |
+----------------------------------------+---------------------------------------+
| HoursOpen                              | hours                                 |
+----------------------------------------+---------------------------------------+
| Locality                               | loc                                   |
+----------------------------------------+---------------------------------------+
| Office                                 | off                                   |
+----------------------------------------+---------------------------------------+
| OrderedContest                         | oc                                    |
+----------------------------------------+---------------------------------------+
| Party                                  | par                                   |
+----------------------------------------+---------------------------------------+
| PartyContest                           | pc                                    |
+----------------------------------------+---------------------------------------+
| PartySelection                         | ps                                    |
+----------------------------------------+---------------------------------------+
| Person                                 | per                                   |
+----------------------------------------+---------------------------------------+
| PollingLocation                        | pl                                    |
+----------------------------------------+---------------------------------------+
| RetentionContest                       | rc                                    |
+----------------------------------------+---------------------------------------+
| Source                                 | src                                   |
+----------------------------------------+---------------------------------------+
| State                                  | st                                    |
+----------------------------------------+---------------------------------------+
| StreetSegment                          | ss                                    |
+----------------------------------------+---------------------------------------+


.. _Hungarian-Style: http://en.wikipedia.org/wiki/Hungarian_notation

File Structure
--------------
All XML and CSV files should be encoded UFT-8 and line breaks should be LF (``\n``) as opposed to CR LF (``\r\n``).

For consistency across files and to aid human readability all indentation of elements should be an indent of two spaces
and tabs should not be used.  Each child node of an element should also be indented an additional two spaces.

General Data Structure
----------------------
All data that are presented to end users of the data (i.e. contest names, referendum text, polling location names,
street names, proper names), where possible, should be converted to Title Case to aid readability.

All data should be trimmed to remove leading and trailing white space.

Optional elements without values should be omitted from XML feed.

Specific Data Types
-------------------
Elements with a data type of ``xs:integer`` must contain a valid whole number greater than zero.

Elements with a data type of ``xs:anyURI`` should be entered as a fully qualified domain name
(e.g. https://www.votinginfoproject.org/)

Elements with a data type of ``xs:dateTime`` should be entered in `ISO-8601`_ format.

Elements with a data type of ``xs:boolean`` should either have a value of ``true`` or ``false``

Elements with a data type of ``xs:language`` should contain a two character, lower-case, value corresponding to the
`ISO 639`_ standard.

Elements that have enumerations which include an ``other`` should have a corresponding value assigned to ``OtherType`` within
the containing element.  For example:

.. code-block:: xml
   :linenos:

   <BallotMeasureContest id="bm390616670907">
      <BallotSelectionId>bms390616670907</BallotSelectionId>
      <ElectoralDistrictId>ed3906177703103</ElectoralDistrictId>
      <Name>Proposed Tax Levy School District</Name>
      <SequenceOrder>34</SequenceOrder>
      <FullText>
        <Text language="en">An additional tax for the benefit of the Lockland Local School District, County of Hamilton,
        Ohio, for the purpose of CURRENT EXPENSES at a rate not exceeding eleven and two-tenths (11.2) mills for each
        one dollar of valuation, which amounts to one dollar and twelve cents ($1.12) for each one hundred dollars of
        valuation, for a continuing period of time, commencing in 2015, first due in calendar year 2016.</Text>
      </FullText>
      <SummaryText>
        <Text language="en">4 Proposed Tax Levy</Text>
      </SummaryText>
      <Type>other</Type>
      <OtherType>bond</OtherType>
   </BallotMeasureContest>


.. _ISO-8601: http://en.wikipedia.org/wiki/ISO_8601
.. _ISO 639: http://en.wikipedia.org/wiki/ISO_639

Specific Data Elements
----------------------

Street Segments: Valid street segment records should not contain leading zeros in ``xs:integer`` fields and should have
a ``Zip`` value of ``00000`` if a value is unknown.

External Identifiers: External identifiers with an enumeration of ``fips`` should contain valid FIPS code values as
defined by the `U.S. Census Bureau`_.  External identifiers with an enumeration of ``ocd-id`` should contain a valid
`Open Civic Data Division Identifier`_.

For long text fields (e.g. ``FullText`` in ``BallotMeasureContest``) the XML line break (``&#xA;``) should be used to
enforce line break styling.

In all fields the characters ``<``, ``>``, and ``&`` should be encoded ``&lt;``, ``&gt;``, and ``&amp;`` respectively.

.. _U.S. Census Bureau: http://www.census.gov/geo/reference/ansi.html
.. _Open Civic Data Division Identifier: https://github.com/opencivicdata/ocd-division-ids


Geospatial Data
---------------

The following sections provide guidance and best practices on using
geospatial data with a VIP feed. Geospatial data represents the
geographic modeling of a shape on the Earth’s surface (i.e. a polygon on
a map), and within the context of a VIP feed is primarily used to model
the boundary of voter precincts. In places where voter precinct shapes
are available, this capability is intended to be straightforward and
lightweight to integrate with existing GIS tooling.

Geodetic Datum
~~~~~~~~~~~~~~

VIP exclusively uses the 84 revision of the World Geodetic System (WGS
84) as the geodetic reference system by which geospatial coordinates
are defined. This applies to geospatial coordinates provided within the
VIP feed itself (e.g. PollingLocation.LatLng) as well as coordinates
provided in an external geospatial file.


Assigning Voters to Precincts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Voter precincts are the atomic unit of electoral districts in the
U.S., and provide the mechanism by which voters are mapped to their
polling places, ballot information and more. It is critical that voter
locations are mapped to the correct precinct in a VIP feed in order to
provide the most accurate and reliable voting information.

There are two mechanisms by which voters can be assigned to precincts
in a VIP feed:

1. **Street segments**
      A voter address that maps to a street segment is assigned to the
      precinct given by StreetSegment.PrecinctId. This is the
      traditional approach of assigning voters to precincts that has
      been in use since the beginning of the VIP specification.

2. **Containment within a precinct boundary**
      A geocoded voter address that is contained within the geographic
      boundary of a precinct is considered assigned to that precinct.
      The geographic boundary of each precinct is defined by
      Precinct.SpatialBoundary. This is a newer approach of assigning
      voters to precincts that was supported starting with version 6.0
      of the VIP specification. Compared to the approach of using
      street segments, geospatial data offers a far more accurate and
      reliable solution to mapping voters to precincts, and thus
      should be the preferred approach whenever possible.

Providing both street segments and precinct shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some cases where precinct boundaries alone are not sufficient
to accurately map all voters to their precinct. For example, if a
precinct boundary divides an apartment building, there is no way to
distinguish the correct precinct for voters that live in this building
using a two-dimensional shape on a map.

To mitigate this limitation of geospatial data, it is possible to
provide **both** street segments and precinct shapes in the same VIP
feed. If a voter’s location is determined to map to a street segment
*and* is also contained within a precinct shape, the precinct assignment
from the street segment will be preferred.

Using the above example where a precinct boundary runs through an
apartment building, this scenario could be handled by providing street
segments in the VIP feed, in addition to precinct shapes, to specify the
mapping of apartment numbers to precinct. For N apartments in the
building, there could be N street segments provided in the feed, each
with a distinct StreetSegment.UnitNumber and precinct assignment. If a
voter address maps to one of these street segments, the precinct
assignment from the segment will supersede a precinct assignment given
by containment with a precinct shape.

Exporting and packaging geospatial files with a VIP feed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geospatial data files are provided in a native geospatial format. Each
geospatial file should adhere to standard industry conventions and
requirements of the corresponding GeospatialFormat. In most cases, these
files will be exported directly from a GIS tool or an Election
Management System and delivered alongside a VIP feed.

All referenced external files need to be packaged with the VIP feed
file, and archived together within a single ZIP file. The following is
an example of the file structure for the case of an XML feed file that
includes ESRI shapefiles.

**Example file structure:**

-  vipfeed-19-2012-11-06-Arizona.zip

   -  vipfeed-19-2012-11-06-Arizona.xml

   -  precinct_shapes1.zip

      - precinct_shapes1.shp
   
      - precinct_shapes1.shx
   
      - precinct_shapes1.dbf

   -  precinct_shapes2.zip

      - precinct_shapes2.shp
  
      - precinct_shapes2.shx
   
      - precinct_shapes2.dbf

The expected file type and structure of each individual geospatial file
will depend on the GeospatialFormat being used. The external file
referenced from the VIP feed may be a flat file, but it could also be a
ZIP file containing multiple relevant files, as the geospatial format
requires. The following provides geospatial data file requirements by
format.

**Expected file type and structure by Geospatial Format:**

+----------------------+----------------------+----------------------+
| **GeospatialFormat** | **Expected file      | **Description**      |
|                      | type**               |                      |
+======================+======================+======================+
| shp (ESRI shapefile) | .zip                 | The referenced       |
|                      |                      | external file should |
|                      |                      | be a ZIP archive     |
|                      |                      | containing, at a     |
|                      |                      | minimum, all files   |
|                      |                      | required by the      |
|                      |                      | `ESRI Shapefile      |
|                      |                      | f                    |
|                      |                      | ormat <https://www.l |
|                      |                      | oc.gov/preservation/ |
|                      |                      | digital/formats/fdd/ |
|                      |                      | fdd000280.shtml>`__. |
|                      |                      | The filename         |
|                      |                      | referenced from the  |
|                      |                      | VIP feed should be   |
|                      |                      | the name of the ZIP  |
|                      |                      | archive for the      |
|                      |                      | shapefile. Required  |
|                      |                      | files within the     |
|                      |                      | archive include a    |
|                      |                      | main *.shp* geometry |
|                      |                      | file, a *.shx* index |
|                      |                      | file, and a *.dbf*   |
|                      |                      | attributes file.     |
|                      |                      | Other optional files |
|                      |                      | as part of the ESRI  |
|                      |                      | Shapefile            |
|                      |                      | specification are    |
|                      |                      | permitted, but may   |
|                      |                      | be ignored.          |
|                      |                      |                      |
|                      |                      | Individual files     |
|                      |                      | within the shapefile |
|                      |                      | archive are          |
|                      |                      | identified by file   |
|                      |                      | extension. For       |
|                      |                      | example, the main    |
|                      |                      | geometry file is     |
|                      |                      | identified by the    |
|                      |                      | file within the      |
|                      |                      | archive with a       |
|                      |                      | .\ *shp* file        |
|                      |                      | extension,           |
|                      |                      | regardless of the    |
|                      |                      | file name. It is     |
|                      |                      | therefore required   |
|                      |                      | that there is only   |
|                      |                      | one file per         |
|                      |                      | expected file type   |
|                      |                      | within the archive.  |
+----------------------+----------------------+----------------------+

Referencing specific shapes within a geospatial data file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geospatial data files will usually contain many shapes. For example,
depending on how the source shape data is managed, it may be easiest to
export a single file containing all precinct shapes represented in the
VIP feed. A precinct boundary is modeled in the feed as a reference to
the external geospatial data file, but in most cases only one or a few
shapes contained in that file are relevant to the precinct.

The specific shape(s) within the external file that comprise the spatial
boundary of the geometric feature are captured by the field
**ExternalGeospatialFeature.ShapeIdentifier**. ShapeIdentifier is a
repeated string field, but the expected value will depend on the
geospatial format of the external file. For example, an integer type is
expected when using the ESRI shapefile format, so the string value of
ShapeIdentifier should be parsable as an integer.

**Expected type of ShapeIdentifier by GeospatialFormat:**

+----------------------+----------------------+----------------------+
| **GeospatialFormat** | **ShapeIdentifier    | **Description**      |
|                      | expected type**      |                      |
+======================+======================+======================+
| shp (ESRI shapefile) | 32-bit integer       | ShapeIdentifier      |
|                      |                      | should be parsable   |
|                      |                      | as a 32-bit integer. |
|                      |                      | Geometric features   |
|                      |                      | in an ESRI shapefile |
|                      |                      | are ordered in       |
|                      |                      | sequence, and the    |
|                      |                      | ShapeIdentifier      |
|                      |                      | value corresponds to |
|                      |                      | the zero-based index |
|                      |                      | of a record within   |
|                      |                      | the file. For        |
|                      |                      | example, a           |
|                      |                      | ShapeIdentifier      |
|                      |                      | value of “35” is a   |
|                      |                      | reference to the     |
|                      |                      | 36th sequential      |
|                      |                      | record in the        |
|                      |                      | shapefile.           |
+----------------------+----------------------+----------------------+

External file checksums
~~~~~~~~~~~~~~~~~~~~~~~

Geospatial data is provided in the form of supplemental files external
to the VIP feed itself. Since this effectively divides the full set of
information of the feed across multiple files, it’s essential that
references between files be reliable. This is ensured by verifiable
cryptographic checksums.

Each external file reference includes the name of the file and its
checksum. A checksum includes both the raw cryptographic hash of the
file's contents, as well as information about which cryptographic
algorithm was used to compute the value. A consumer of a VIP feed should
be able to compute a checksum value of an external file using the same
algorithm and independently verify it matches the checksum value in the
feed.

It’s worth noting that having a file checksum also introduces an
opportunity for consumers of the data to optimize their processing of
it. If the contents of a VIP feed are updated, but the checksum for an
external geospatial data file has not changed, then the consumer could
omit having to reprocess the geospatial aspects of the feed.

Requirements for precinct shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following are practical requirements when defining the spatial
boundary of a Precinct element (whether a precinct or precinct
split) with geospatial shapes.

-  The resolution of a polygon for a precinct shape can be as coarse or
   fine as needed, so long as the shape accurately represents the
   boundary of the precinct.

-  No two shapes should overlap.

-  All polygons must form a closed loop. That is, the polygon should
   start and end from the same point.

-  The border of a polygon must not intersect itself.

-  The spatial boundary of a Precinct is defined by a single geospatial
   feature. That feature, however, may contain one or more discrete
   and non-overlapping polygons as necessary to define the full extent of
   the boundary.

-  ShapeIdentifier must be a valid, existing reference in the external
   file.

-  ShapeIdentifier must have an expected type according to the table
   above.
