<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:sch="http://purl.oclc.org/dsdl/schematron"
                xmlns:vip="http://votinginfoproject.org/schematron-build"
                exclude-result-prefixes="xs vip">

  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>

  <xsl:variable name="xsdDoc" select="document('vip_spec.xsd')"/>
  <xsl:variable name="tzDoc" select="document('iana_timezones.xml')"/>

  <xsl:function name="vip:quote-seq" as="xs:string">
    <xsl:param name="items" as="xs:string*"/>
    <xsl:value-of select="concat('(', string-join(for $s in $items return concat('''', replace($s, '''', ''''''), ''''), ', '), ')')"/>
  </xsl:function>

  <!-- Map a complexType name in vip_spec.xsd to the XML element names that can have that type. -->
  <xsl:function name="vip:elements-for-parent-type" as="xs:string*">
    <xsl:param name="typeName" as="xs:string"/>
    <xsl:variable name="directElements" as="xs:string*"
                  select="distinct-values($xsdDoc//xs:element[@type = $typeName and not(@onlyInOverlay)]/@name)"/>
    <xsl:variable name="subtypeNames" as="xs:string*"
                  select="distinct-values($xsdDoc/xs:schema/xs:complexType[xs:complexContent/xs:extension[@base = $typeName]]/@name)"/>
    <xsl:variable name="subElements" as="xs:string*"
                  select="for $st in $subtypeNames return vip:elements-for-parent-type($st)"/>
    <xsl:variable name="selfTopLevel" as="xs:string*">
      <xsl:choose>
        <xsl:when test="$typeName = 'ContestBase'">Contest</xsl:when>
        <xsl:when test="$typeName = 'BallotSelectionBase'">BallotSelection</xsl:when>
        <xsl:when test="$typeName = ('BallotMeasureContest', 'CandidateContest', 'PartyContest', 'RetentionContest')">
          <xsl:sequence select="($typeName, 'Contest')"/>
        </xsl:when>
        <xsl:when test="$typeName = ('BallotMeasureSelection', 'CandidateSelection', 'PartySelection')">
          <xsl:sequence select="($typeName, 'BallotSelection')"/>
        </xsl:when>
        <xsl:when test="$typeName = ('BallotStyle', 'Candidate', 'Election', 'ElectoralDistrict',
                                     'ExternalFile', 'Locality', 'Office', 'OrderedContest',
                                     'Party', 'Person', 'PollingLocation', 'Precinct',
                                     'StreetSegment')">
          <xsl:value-of select="$typeName"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="sourceElements" as="xs:string*">
      <xsl:if test="$typeName = 'ContactInformation'">FeedContactInformation</xsl:if>
    </xsl:variable>
    <xsl:sequence select="distinct-values(($selfTopLevel, $directElements, $subElements, $sourceElements))"/>
  </xsl:function>

  <!-- Expand space-separated XSD type names into concrete parent/child XPath context paths for Main Feed. -->
  <xsl:function name="vip:resolve-schema-types" as="xs:string">
    <xsl:param name="typeList" as="xs:string"/>
    <xsl:variable name="types" select="tokenize(normalize-space($typeList), '\s+')[. != '']"/>
    <xsl:variable name="xsdPaths" as="xs:string*">
      <xsl:for-each select="$xsdDoc/xs:schema/xs:complexType">
        <xsl:variable name="ctName" select="string(@name)"/>
        <xsl:variable name="parentElems" select="vip:elements-for-parent-type($ctName)"/>
        <xsl:for-each select=".//xs:element[@type = $types and not(@onlyInOverlay)]">
          <xsl:variable name="childName" select="string(@name)"/>
          <xsl:for-each select="$parentElems">
            <xsl:sequence select="concat(., '/', $childName)"/>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:for-each>
    </xsl:variable>
    <xsl:variable name="sourceFields" as="xs:string*">
      <xsl:if test="'xs:dateTime' = $types">Source/DateTime</xsl:if>
      <xsl:if test="'InternationalizedText' = $types">Source/Description</xsl:if>
      <xsl:if test="'ContactInformation' = $types">Source/FeedContactInformation</xsl:if>
      <xsl:if test="'xs:string' = $types">
        <xsl:sequence select="('Source/Name', 'Source/VipId')"/>
      </xsl:if>
      <xsl:if test="'InternationalizedUri' = $types">
        <xsl:sequence select="('Source/OrganizationUri', 'Source/TermsOfUseUri')"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="allPaths" select="distinct-values(($xsdPaths, $sourceFields))"/>
    <xsl:value-of select="string-join($allPaths, ' | ')"/>
  </xsl:function>

  <!-- Strip overlay-only sections. -->
  <xsl:template match="*[@onlyInOverlay]"/>

  <!-- Prune <active> references to stripped patterns so iso-schematron.rnc IDREFs remain valid. -->
  <xsl:template match="sch:active">
    <xsl:variable name="patId" select="normalize-space(@pattern)"/>
    <xsl:if test="exists(//sch:pattern[@id = $patId and not(@onlyInOverlay)])">
      <xsl:copy>
        <xsl:apply-templates select="@* | node()"/>
      </xsl:copy>
    </xsl:if>
  </xsl:template>

  <!-- Inline IANA timezone lists from iana_timezones.xml. -->
  <xsl:template match="sch:let[@name = 'ianaCanonicalZones']">
    <xsl:copy>
      <xsl:apply-templates select="@*[not(local-name() = ('value', 'onlyInMain', 'onlyInOverlay'))]"/>
      <xsl:attribute name="value"
                     select="vip:quote-seq(for $z in $tzDoc/IanaTimeZones/Zone[@canonical = 'true'] return string($z))"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="sch:let[@name = 'ianaAliasZones']">
    <xsl:copy>
      <xsl:apply-templates select="@*[not(local-name() = ('value', 'onlyInMain', 'onlyInOverlay'))]"/>
      <xsl:attribute name="value"
                     select="vip:quote-seq(for $z in $tzDoc/IanaTimeZones/Zone[@canonical = 'false'] return string($z))"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="sch:let[@name = 'ianaAliasTargets']">
    <xsl:copy>
      <xsl:apply-templates select="@*[not(local-name() = ('value', 'onlyInMain', 'onlyInOverlay'))]"/>
      <xsl:attribute name="value"
                     select="vip:quote-seq(for $z in $tzDoc/IanaTimeZones/Zone[@canonical = 'false'] return string($z/@target))"/>
    </xsl:copy>
  </xsl:template>

  <!-- Expand @schemaType on <sch:rule> into a concrete XPath @context. -->
  <xsl:template match="sch:rule[@schemaType]">
    <xsl:copy>
      <xsl:apply-templates select="@*[not(local-name() = ('schemaType', 'context', 'onlyInMain', 'onlyInOverlay'))]"/>
      <xsl:attribute name="context" select="vip:resolve-schema-types(@schemaType)"/>
      <xsl:apply-templates select="node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- Strip build-time attributes everywhere. -->
  <xsl:template match="@onlyInMain | @onlyInOverlay | @schemaType"/>

  <xsl:template match="node() | @*">
    <xsl:copy>
      <xsl:apply-templates select="@* | node()"/>
    </xsl:copy>
  </xsl:template>

</xsl:stylesheet>
