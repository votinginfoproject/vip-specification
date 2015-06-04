XML Data Best Practices
=======================

Following is a series of best practice for data collection and XML file creation and suggestions about best practices of
formatting data within your VIP XML file.

Element Identifiers
-------------------

Most elements within the VIP feed require unique identifiers, ``xs:ID`` data types, and in order to maintain uniqueness
and provide context for the identifiers, the best practice is to use `Hungarian-Style`_ notation for identifiers.

ID values should follow Hungarian-Style notation, were the identifier prefix implicitly names the data element.  Below
is a list of preferred prefixes by element:

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
All XML files should be encoded UFT-8 and line breaks should be LF (``\n``) as opposed to CR LF (``\r\n``).

For consistency across files and to aid human readability all lines should be indented two spaces and tabs should not
be used.

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

 ``<BallotMeasureContest id="bm390616670907">
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


