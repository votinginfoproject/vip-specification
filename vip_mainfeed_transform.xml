<?xml version="1.0" encoding="UTF-8"?>
<xsl:transform version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xsl:output method="xml" indent="yes" encoding="UTF-8" />

  <!-- Remove any elements with the onlyInOverlay attribute. -->
  <xsl:template match="//*[@onlyInOverlay]" />

  <!-- Replace clearable attribute on overlays with a minOccurs="0",
       since clearable in overlays implies optional in the main feed. -->
  <xsl:template match="//xs:element[@clearable and @type != 'EmergencyNotice']" >
    <xsl:copy>
      <xsl:apply-templates select="node()|@*[name(.)!='clearable' and name(.)!='optionalInOverlay']" />
      <xsl:attribute name="minOccurs">0</xsl:attribute>
    </xsl:copy>
  </xsl:template>

  <!-- Delete the optionalInOverlay attribute. -->
  <xsl:template match="@optionalInOverlay" />

  <!-- By default, copy input to output with no modification. -->
  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="xs:schema">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
      <!-- Root VIP feed element. -->
      <xs:element name="VipObject">
	<xs:complexType>
	  <xs:sequence>
            <!-- This replaces the "referendum" element in VIP -->
            <xs:element name="BallotMeasureContest" type="BallotMeasureContest" minOccurs="0" maxOccurs="unbounded" />
            <!-- Generic string for a ballot measure (referendum) selection -->
            <xs:element name="BallotMeasureSelection" type="BallotMeasureSelection" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="BallotSelection" type="BallotSelectionBase" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="BallotStyle" type="BallotStyle" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Candidate" type="Candidate" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="CandidateContest" type="CandidateContest" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="CandidateSelection" type="CandidateSelection" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Contest" type="ContestBase" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Election" type="Election" minOccurs="1" maxOccurs="1" />
            <xs:element name="ElectoralDistrict" type="ElectoralDistrict" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="ExternalFile" type="ExternalFile" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Locality" type="Locality" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Office" type="Office" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="OrderedContest" type="OrderedContest" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Party" type="Party" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="PartyContest" type="PartyContest" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="PartySelection" type="PartySelection" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Person" type="Person" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="PollingLocation" type="PollingLocation" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Precinct" type="Precinct" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="RetentionContest" type="RetentionContest" minOccurs="0" maxOccurs="unbounded" />
            <xs:element name="Source" minOccurs="1" maxOccurs="1">
              <xs:complexType>
		<xs:sequence>
		  <xs:element name="DateTime" type="xs:dateTime" />
		  <xs:element name="Description" type="InternationalizedText" minOccurs="0" />
		  <xs:element name="FeedContactInformation" type="ContactInformation" minOccurs="0" />
		  <xs:element name="Name" type="xs:string" />
		  <xs:element name="OrganizationUri" type="InternationalizedUri" minOccurs="0" />
		  <xs:element name="TermsOfUseUri" type="InternationalizedUri" minOccurs="0" />
		  <xs:element name="VipId" type="xs:string" />
		</xs:sequence>
		<xs:attribute name="id" type="xs:ID" use="required" />
              </xs:complexType>
            </xs:element>
	    <xs:element name="StreetSegment" type="StreetSegment" minOccurs="0" maxOccurs="unbounded" />
	  </xs:sequence>
	  <xs:attribute name="schemaVersion" type="xs:decimal" use="required" fixed="7.0" />
	</xs:complexType>
      </xs:element>
    </xsl:copy>
  </xsl:template>
</xsl:transform>
