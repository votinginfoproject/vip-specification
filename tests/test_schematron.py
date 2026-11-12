"""Comprehensive validation tests for VIP 7.0 XSD, Schematron, docs, and CLI."""

import copy
import glob
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from lxml import etree
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def _extract_rule_ids(text):
    """Extract ordered list of [RULE-ID] tags emitted by Jing."""
    return re.findall(r"\[([A-Z0-9-]+)\]", text)


def _run_jing(schema_path, xml_paths, phase="strict"):
    """Run jing against one or more XML files and return CompletedProcess."""
    cmd = ["jing", "-p", phase, str(schema_path)] + [str(p) for p in xml_paths]
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def _valid_main_doc():
    """Return a minimal, valid VIP 7.0 VipObject XML Element (passes XSD & full)."""
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<VipObject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="7.0">
  <BallotMeasureContest id="bmc1">
    <BallotSelectionIds>bms1 bms2</BallotSelectionIds>
    <ElectoralDistrictId>ed1</ElectoralDistrictId>
    <Name>School Bond</Name>
    <VoteVariation>1-of-m</VoteVariation>
    <Type>referendum</Type>
  </BallotMeasureContest>
  <BallotMeasureSelection id="bms1">
    <SequenceOrder>0</SequenceOrder>
    <Selection><Text language="i-default">Yes</Text></Selection>
  </BallotMeasureSelection>
  <BallotMeasureSelection id="bms2">
    <SequenceOrder>1</SequenceOrder>
    <Selection><Text language="i-default">No</Text></Selection>
  </BallotMeasureSelection>
  <BallotStyle id="bs1">
    <OrderedContestIds>oc1 oc2</OrderedContestIds>
    <PartyIds>par1</PartyIds>
  </BallotStyle>
  <Candidate id="cand1">
    <BallotName><Text language="i-default">Alice Smith</Text></BallotName>
    <PartyId>par1</PartyId>
    <PersonId>per1</PersonId>
  </Candidate>
  <CandidateContest id="cc1">
    <BallotSelectionIds>cs1</BallotSelectionIds>
    <ElectoralDistrictId>ed1</ElectoralDistrictId>
    <Name>Mayor</Name>
    <VoteVariation>1-of-m</VoteVariation>
    <NumberElected>1</NumberElected>
    <OfficeIds>off1</OfficeIds>
    <PrimaryPartyIds>par1</PrimaryPartyIds>
    <VotesAllowed>1</VotesAllowed>
  </CandidateContest>
  <CandidateSelection id="cs1">
    <CandidateIds>cand1</CandidateIds>
    <EndorsementPartyIds>par1</EndorsementPartyIds>
  </CandidateSelection>
  <Election id="ele1">
    <AbsenteeRequestDeadline>2024-10-25</AbsenteeRequestDeadline>
    <Date>2024-11-05</Date>
    <Name><Text language="i-default">2024 General Election</Text></Name>
    <RegistrationDeadline>2024-10-15</RegistrationDeadline>
    <ResultsUri><Uri language="i-default">https://example.gov/results</Uri></ResultsUri>
    <TopLevelLocalityId>loc_state</TopLevelLocalityId>
  </Election>
  <ElectoralDistrict id="ed1">
    <ExternalIdentifier>
      <Type>ocd-id</Type>
      <Value>ocd-division/country:us/state:va</Value>
    </ExternalIdentifier>
    <Name><Text language="i-default">City of Springfield</Text></Name>
    <Number>0</Number>
    <Type>municipality</Type>
  </ElectoralDistrict>
  <ExternalFile id="ef1">
    <FileUri>boundaries/precincts.geojson</FileUri>
    <Checksum>
      <Algorithm>sha-256</Algorithm>
      <Value>0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef</Value>
    </Checksum>
  </ExternalFile>
  <Locality id="loc_state">
    <Name>Virginia</Name>
    <Type>state</Type>
  </Locality>
  <Locality id="loc1">
    <ElectionAdministration>
      <ContactInformation label="ea1">
        <PhysicalAddress language="i-default">
          <AddressLine>100 Main St</AddressLine>
          <City>Springfield</City>
          <Region>VA</Region>
          <Country>USA</Country>
          <PostalCode>22150</PostalCode>
        </PhysicalAddress>
        <Email>vote@example.gov</Email>
        <Schedule>
          <TimeZone>America/New_York</TimeZone>
          <Hours>
            <StartTime>08:00:00</StartTime>
            <EndTime>17:00:00</EndTime>
          </Hours>
        </Schedule>
        <Name>County Board</Name>
        <Uri>https://example.gov/ea</Uri>
      </ContactInformation>
      <ElectionsUri>https://example.gov/elections</ElectionsUri>
      <VoterService>
        <ElectionOfficialPersonId>per1</ElectionOfficialPersonId>
        <Type>voter-registration</Type>
      </VoterService>
    </ElectionAdministration>
    <ExternalIdentifier>
      <Type>fips</Type>
      <Value>51059</Value>
    </ExternalIdentifier>
    <Name>Fairfax County</Name>
    <PollingLocationIds>pl1</PollingLocationIds>
    <ParentLocalityId>loc_state</ParentLocalityId>
    <Type>county</Type>
  </Locality>
  <Office id="off1">
    <ElectoralDistrictId>ed1</ElectoralDistrictId>
    <FilingDeadline>2024-06-01</FilingDeadline>
    <Name><Text language="i-default">Mayor</Text></Name>
    <OfficeHolderPersonIds>per1</OfficeHolderPersonIds>
    <Term>
      <StartDate>2025-01-01</StartDate>
      <EndDate>2029-01-01</EndDate>
      <Type>full-term</Type>
    </Term>
  </Office>
  <OrderedContest id="oc1">
    <ContestId>cc1</ContestId>
    <OrderedBallotSelectionIds>cs1</OrderedBallotSelectionIds>
  </OrderedContest>
  <OrderedContest id="oc2">
    <ContestId>bmc1</ContestId>
    <OrderedBallotSelectionIds>bms2 bms1</OrderedBallotSelectionIds>
  </OrderedContest>
  <Party id="par1">
    <Abbreviation>IND</Abbreviation>
    <Color>0044aa</Color>
    <LeaderPersonIds>per1</LeaderPersonIds>
    <Name><Text language="i-default">Independent</Text></Name>
  </Party>
  <Person id="per1">
    <FullName><Text language="i-default">Alice Smith</Text></FullName>
    <PartyId>par1</PartyId>
  </Person>
  <PollingLocation id="pl1">
    <AddressStructured language="i-default">
      <LocationName>High School Gym</LocationName>
      <AddressLine>200 Oak Ave</AddressLine>
      <City>Springfield</City>
      <Region>VA</Region>
      <Country>US</Country>
      <PostalCode>22150-1234</PostalCode>
    </AddressStructured>
    <LocationIdentifier provider="google">
      <Type>pluscode</Type>
      <Value>87C4QPWV+2R</Value>
    </LocationIdentifier>
    <Directions><Text language="i-default">Use east entrance</Text></Directions>
    <Schedule>
      <TimeZone>America/New_York</TimeZone>
      <StartDate>2024-11-05</StartDate>
      <EndDate>2024-11-05</EndDate>
      <Hours>
        <StartTime>06:00:00</StartTime>
        <EndTime>19:00:00</EndTime>
      </Hours>
    </Schedule>
    <LocationType>InPersonDayOf</LocationType>
    <LatLng>
      <Latitude>38.78</Latitude>
      <Longitude>-77.18</Longitude>
    </LatLng>
  </PollingLocation>
  <Precinct id="prec1">
    <BallotStyleId>bs1</BallotStyleId>
    <ElectoralDistrictIds>ed1</ElectoralDistrictIds>
    <LocalityId>loc1</LocalityId>
    <Name>Precinct 1</Name>
    <PollingLocationIds>pl1</PollingLocationIds>
    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <FeatureIdentifier>
          <Index>0</Index>
        </FeatureIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>
  </Precinct>
  <Source id="src1">
    <DateTime>2024-10-20T12:00:00-04:00</DateTime>
    <Description><Text language="i-default">Official VIP feed</Text></Description>
    <FeedContactInformation>
      <Email>support@example.gov</Email>
      <Name>Support</Name>
    </FeedContactInformation>
    <Name>State Board of Elections</Name>
    <OrganizationUri>https://example.gov</OrganizationUri>
    <VipId>51</VipId>
  </Source>
  <StreetSegment id="ss1">
    <City>Springfield</City>
    <IncludesAllAddresses>false</IncludesAllAddresses>
    <IncludesAllStreets>false</IncludesAllStreets>
    <OddEvenBoth>odd</OddEvenBoth>
    <PrecinctId>prec1</PrecinctId>
    <StartHouseNumber>101</StartHouseNumber>
    <EndHouseNumber>199</EndHouseNumber>
    <Region>VA</Region>
    <StreetName>Main St</StreetName>
    <PostalCode>22150</PostalCode>
  </StreetSegment>
</VipObject>
"""
    return etree.fromstring(xml.encode("utf-8"))


def _valid_overlay_doc():
    """Return a minimal, valid VIP 7.0 VipOverlay XML Element.

    Compatible with _valid_main_doc for cross-document validation tests.
    """
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<VipOverlay xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="7.0">
  <Locality id="loc1">
    <EmergencyNotice>
      <NoticeText>
        <Text language="i-default">Hours extended until 9 PM.</Text>
        <Text language="es">Horario extendido hasta las 9 PM.</Text>
      </NoticeText>
      <NoticeUri>https://example.gov/notice</NoticeUri>
      <AppliesTo>search</AppliesTo>
      <AppliesTo>maps</AppliesTo>
    </EmergencyNotice>
    <PollingLocationIds>pl1 pl_new</PollingLocationIds>
    <OverriddenPollingHours>
      <TimeZone>America/New_York</TimeZone>
      <StartDate>2024-11-05</StartDate>
      <EndDate>2024-11-05</EndDate>
      <Hours>
        <StartTime>06:00:00</StartTime>
        <EndTime>21:00:00</EndTime>
      </Hours>
    </OverriddenPollingHours>
  </Locality>
  <PollingLocation id="pl_new" isNew="true">
    <AddressStructured language="i-default">
      <LocationName>Annex Drop Box</LocationName>
      <AddressLine>300 Pine Rd</AddressLine>
      <City>Springfield</City>
      <Region>VA</Region>
      <PostalCode>22150</PostalCode>
    </AddressStructured>
    <Schedule>
      <TimeZone>America/New_York</TimeZone>
      <StartDate>2024-10-25</StartDate>
      <EndDate>2024-11-05</EndDate>
      <IsOpen24Hours>true</IsOpen24Hours>
    </Schedule>
    <LocationType>DropOff</LocationType>
  </PollingLocation>
</VipOverlay>
"""
    return etree.fromstring(xml.encode("utf-8"))


def _sort_children(elem):
    """Sort top-level children of VipObject/VipOverlay alphabetically to keep XSD sequence valid."""
    children = [c for c in elem if isinstance(c.tag, str)]
    children.sort(key=lambda e: e.tag)
    elem[:] = children
    return elem


def _mutate_main(fn):
    """Build a mutated copy of _valid_main_doc(), preserving element ordering."""
    doc = _valid_main_doc()
    fn(doc)
    return _sort_children(doc)


def _mutate_overlay(fn):
    """Build a mutated copy of _valid_overlay_doc(), preserving element ordering."""
    doc = _valid_overlay_doc()
    fn(doc)
    return _sort_children(doc)


def _write_doc(path, elem, base_href=None):
    """Serialize an XML Element to path, optionally injecting <?vip-base-feed?>."""
    xml_bytes = etree.tostring(
        elem, encoding="utf-8", xml_declaration=True, pretty_print=True
    )
    if base_href is not None:
        safe_href = base_href.replace('"', "%22").replace("?>", "%3F%3E")
        text = xml_bytes.decode("utf-8")
        idx = text.find("?>")
        assert idx != -1
        pi = f'\n<?vip-base-feed href="{safe_href}"?>'
        text = text[: idx + 2] + pi + text[idx + 2 :]
        path.write_text(text, encoding="utf-8")
    else:
        path.write_bytes(xml_bytes)


class TestSchemaBuildsAndDocs(unittest.TestCase):
    """Verify schema determinism, timezone file integrity, and documentation examples."""

    @classmethod
    def setUpClass(cls):
        parser = etree.XMLParser(resolve_entities=False, no_network=True, load_dtd=False)
        cls.main_xsd = etree.XMLSchema(etree.parse(str(REPO_ROOT / "vip_main.xsd"), parser))
        cls.overlay_xsd = etree.XMLSchema(etree.parse(str(REPO_ROOT / "vip_overlay.xsd"), parser))

    def test_generated_schemas_match_xslt_transforms(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            builds = [
                ("vip_spec.xsd", "vip_mainfeed_transform.xsl", "vip_main.xsd"),
                ("vip_spec.xsd", "vip_overlay_transform.xsl", "vip_overlay.xsd"),
                ("vip_spec.sch", "vip_mainfeed_schematron_transform.xsl", "vip_main.sch"),
                ("vip_spec.sch", "vip_overlay_schematron_transform.xsl", "vip_overlay.sch"),
            ]
            for src, xsl, target in builds:
                out_path = Path(tmpdir) / target
                subprocess.run(
                    ["saxonb-xslt", f"-s:{src}", f"-xsl:{xsl}", f"-o:{out_path}"],
                    cwd=str(REPO_ROOT),
                    check=True,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(
                    out_path.read_text(encoding="utf-8"),
                    (REPO_ROOT / target).read_text(encoding="utf-8"),
                    f"Checked-in {target} differs from fresh XSLT output",
                )

    def test_iana_timezones_xml_structure(self):
        doc = etree.parse(str(REPO_ROOT / "iana_timezones.xml"))
        zones = doc.findall("Zone")
        self.assertGreater(len(zones), 500)
        canonical = set()
        aliases = {}
        deprecated_prefixes = ("US/", "Canada/", "Mexico/", "Brazil/", "Chile/")
        for z in zones:
            name = (z.text or "").strip()
            self.assertTrue(name)
            is_canon = z.get("canonical")
            self.assertIn(is_canon, ("true", "false"))
            if is_canon == "true":
                self.assertFalse(name.startswith(deprecated_prefixes), name)
                self.assertIsNone(z.get("target"))
                canonical.add(name)
            else:
                target = z.get("target")
                self.assertTrue(target, f"Alias {name} missing target")
                aliases[name] = target
        self.assertTrue(canonical.isdisjoint(aliases.keys()))
        self.assertIn("America/New_York", canonical)
        self.assertEqual(aliases.get("US/Eastern"), "America/New_York")
        for alias, target in aliases.items():
            self.assertIn(target, canonical, f"Alias {alias} target {target} not canonical")

    def test_overlay_rst_examples_valid(self):
        rst = (REPO_ROOT / "docs" / "overlay.rst").read_text(encoding="utf-8")
        parts = rst.split(".. code-block:: xml")
        blocks = []
        for p in parts[1:]:
            m = re.search(r"<\?xml.*?</VipOverlay>", p, re.S)
            if m:
                blocks.append(re.sub(r"\n   ", "\n", m.group(0)))
        self.assertEqual(len(blocks), 5)  # Root skeleton + 4 examples
        with tempfile.TemporaryDirectory() as tmpdir:
            example_paths = []
            for idx, b in enumerate(blocks):
                elem = etree.fromstring(b.encode("utf-8"))
                self.overlay_xsd.assertValid(elem)
                if idx > 0:  # Examples 1..4 must pass full Schematron cleanly
                    out = Path(tmpdir) / f"ex_{idx}.xml"
                    out.write_text(b, encoding="utf-8")
                    example_paths.append(out)
            proc = _run_jing(REPO_ROOT / "vip_overlay.sch", example_paths, phase="full")
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_yaml_doc_snippets_well_formed_and_valid(self):
        stubs = """
          <BallotMeasureSelection id="bms30001a"><Selection><Text language="i-default">Yes</Text></Selection></BallotMeasureSelection>
          <BallotMeasureSelection id="bms30001b"><Selection><Text language="i-default">No</Text></Selection></BallotMeasureSelection>
          <BallotStyle id="bs_stub"><OrderedContestIds>oc_stub</OrderedContestIds></BallotStyle>
          <Candidate id="can10961"><BallotName><Text language="i-default">A</Text></BallotName></Candidate>
          <Candidate id="can14444"><BallotName><Text language="i-default">B</Text></BallotName></Candidate>
          <CandidateSelection id="cs10961"><CandidateIds>can10961</CandidateIds></CandidateSelection>
          <CandidateSelection id="cs10962"><CandidateIds>can14444</CandidateIds></CandidateSelection>
          <CandidateContest id="cc_stub"><BallotSelectionIds>cs10961</BallotSelectionIds><ElectoralDistrictId>ed60129</ElectoralDistrictId><Name>CC</Name></CandidateContest>
          <ElectoralDistrict id="ed60129"><Name><Text language="i-default">D</Text></Name><Type>state-house</Type></ElectoralDistrict>
          <Locality id="loc51"><Name>VA</Name></Locality>
          <Locality id="loc70001"><Name>County</Name><ParentLocalityId>loc51</ParentLocalityId></Locality>
          <Office id="off0000"><ElectoralDistrictId>ed60129</ElectoralDistrictId><Name><Text language="i-default">O</Text></Name></Office>
          <Office id="off20006"><ElectoralDistrictId>ed60129</ElectoralDistrictId><Name><Text language="i-default">O2</Text></Name></Office>
          <OrderedContest id="oc_stub"><ContestId>cc_stub</ContestId></OrderedContest>
          <Party id="par0001"><Name><Text language="i-default">P1</Text></Name></Party>
          <Party id="par0002"><Name><Text language="i-default">P2</Text></Name></Party>
          <Person id="per10961"><FullName><Text language="i-default">Person</Text></FullName></Person>
          <PollingLocation id="pl00001"><AddressStructured language="i-default"><AddressLine>1 Main</AddressLine><City>Charlottesville</City><Region>VA</Region><PostalCode>22901</PostalCode></AddressStructured><LocationType>InPersonDayOf</LocationType></PollingLocation>
          <PollingLocation id="pl00002"><AddressStructured language="i-default"><AddressLine>2 Main</AddressLine><City>Charlottesville</City><Region>VA</Region><PostalCode>22901</PostalCode></AddressStructured><LocationType>DropOff</LocationType></PollingLocation>
          <BallotMeasureSelection id="rc40001a"><Selection><Text language="i-default">Yes</Text></Selection></BallotMeasureSelection>
          <BallotMeasureSelection id="rc40001b"><Selection><Text language="i-default">No</Text></Selection></BallotMeasureSelection>
          <Source id="src1"><DateTime>2024-10-24T14:25:28-04:00</DateTime><Name>S</Name><VipId>51</VipId></Source>
          <Election id="ele30000"><Date>2024-11-05</Date><TopLevelLocalityId>loc51</TopLevelLocalityId></Election>
        """
        root_stub = etree.fromstring(f'<VipObject schemaVersion="7.0">{stubs}</VipObject>'.encode())
        stub_by_id = {el.get("id"): el for el in root_stub if el.get("id")}
        sub_types = {
            "ExternalIdentifier", "LocationIdentifier", "LatLng", "Checksum",
            "Hours", "InternationalizedText", "LanguageString", "LanguageUri",
            "ExternalGeospatialFeature", "FeatureIdentifier", "VoterService",
        }
        tested_ov = []
        with tempfile.TemporaryDirectory() as tmpdir:
            for yp in sorted(glob.glob(str(REPO_ROOT / "docs/yaml/elements/*.yaml"))):
                with self.subTest(yaml_file=Path(yp).name):
                    data = yaml.safe_load(Path(yp).read_text(encoding="utf-8"))
                    post = data.get("post", "")
                    if not post:
                        continue
                    m = re.search(r":linenos:\s*\n\n(.*)$", post, re.S)
                    self.assertIsNotNone(m, yp)
                    lines = m.group(1).splitlines()
                    min_indent = min(
                        (len(line) - len(line.lstrip()) for line in lines if line.strip()),
                        default=0,
                    )
                    snippet = "\n".join(line[min_indent:] for line in lines)
                    wrapped = etree.fromstring(f"<Wrapper>{snippet}</Wrapper>".encode("utf-8"))
                    first_tag = next(el for el in wrapped if isinstance(el.tag, str)).tag
                    if first_tag == "EmergencyNotice":
                        doc_xml = (
                            '<VipOverlay schemaVersion="7.0">'
                            f'<Locality id="loc_em">{snippet}</Locality>'
                            "</VipOverlay>"
                        )
                        ov_el = etree.fromstring(doc_xml.encode("utf-8"))
                        self.overlay_xsd.assertValid(ov_el)
                        p = Path(tmpdir) / (Path(yp).stem + ".xml")
                        p.write_text(doc_xml, encoding="utf-8")
                        tested_ov.append(p)
                        continue
                    if first_tag == "Schedule":
                        inner = f'<PollingLocation id="pl_w"><AddressStructured language="i-default"><AddressLine>1 Main</AddressLine><City>Cville</City><Region>VA</Region><PostalCode>22901</PostalCode></AddressStructured>{snippet}<LocationType>InPersonDayOf</LocationType></PollingLocation>'
                    elif first_tag == "AddressStructured":
                        inner = f'<PollingLocation id="pl_w">{snippet}<LocationType>InPersonDayOf</LocationType></PollingLocation>'
                    elif first_tag == "ContactInformation":
                        inner = f'<Office id="off_w">{snippet}<ElectoralDistrictId>ed60129</ElectoralDistrictId><Name><Text language="i-default">Gov</Text></Name></Office>'
                    elif first_tag == "ElectionAdministration":
                        inner = f'<Locality id="loc_w">{snippet}<Name>County</Name><ParentLocalityId>loc51</ParentLocalityId></Locality>'
                    elif first_tag == "SpatialBoundary":
                        inner = f'<ExternalFile id="ef1"><FileUri>https://example.gov/p.geojson</FileUri><Checksum><Algorithm>sha-256</Algorithm><Value>{"0"*64}</Value></Checksum></ExternalFile><Precinct id="pr_w"><LocalityId>loc51</LocalityId><Name>P1</Name>{snippet}</Precinct>'
                    elif first_tag in sub_types:
                        continue
                    else:
                        inner = snippet

                    frag = etree.fromstring(
                        f'<VipObject schemaVersion="7.0">{inner}</VipObject>'.encode("utf-8")
                    )
                    for c in list(frag):
                        if not isinstance(c.tag, str):
                            frag.remove(c)
                    # Ensure standalone ExternalFile/Locality snippets have valid linkage in test wrapper
                    for loc in frag.findall("Locality"):
                        if loc.get("id") != "loc51" and loc.find("ParentLocalityId") is None:
                            etree.SubElement(loc, "ParentLocalityId").text = "loc51"
                    existing_ids = {el.get("id") for el in frag if el.get("id")}
                    has_source = frag.find("Source") is not None
                    has_election = frag.find("Election") is not None
                    for sid, sel in stub_by_id.items():
                        if sid in existing_ids:
                            continue
                        if sel.tag == "Source" and has_source:
                            continue
                        if sel.tag == "Election" and has_election:
                            continue
                        frag.append(copy.deepcopy(sel))
                    _sort_children(frag)
                    self.main_xsd.assertValid(frag)
            proc = _run_jing(REPO_ROOT / "vip_overlay.sch", tested_ov, phase="full")
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_overlay_xsd_w3c_portability_and_ncname_constraints(self):
        overlay_xsd_text = (REPO_ROOT / "vip_overlay.xsd").read_text(encoding="utf-8")
        self.assertNotIn('type="xs:IDREF"', overlay_xsd_text)
        self.assertNotIn('type="xs:IDREFS"', overlay_xsd_text)
        self.assertIn('name="NCNameList"', overlay_xsd_text)
        self.assertIn('type="xs:ID"', overlay_xsd_text)

        # Standalone overlay referencing base-feed ID 'pl1' passes XSD
        valid_ov = _valid_overlay_doc()
        self.overlay_xsd.assertValid(valid_ov)

        # Empty/whitespace-only NCNameList, invalid NCName, and duplicate xs:ID must fail XSD
        bad_ov_xmls = [
            '<VipOverlay schemaVersion="7.0"><Locality id="loc1"><PollingLocationIds/></Locality></VipOverlay>',
            '<VipOverlay schemaVersion="7.0"><Locality id="loc1"><PollingLocationIds>   </PollingLocationIds></Locality></VipOverlay>',
            '<VipOverlay schemaVersion="7.0"><Locality id="loc1"><PollingLocationIds>123bad</PollingLocationIds></Locality></VipOverlay>',
            '<VipOverlay schemaVersion="7.0"><Locality id="dup"><Name>A</Name></Locality><Locality id="dup"><Name>B</Name></Locality></VipOverlay>',
        ]
        for bad_xml in bad_ov_xmls:
            self.assertFalse(
                self.overlay_xsd.validate(etree.fromstring(bad_xml.encode("utf-8"))),
                bad_xml,
            )

    @unittest.skipUnless(
        shutil.which("javac") and shutil.which("java"),
        "JDK (javac/java) required for Xerces XSD 1.0 check",
    )
    def test_overlay_xsd_java_xerces_validation(self):
        valid_ov = _valid_overlay_doc()
        bad_empty = (
            '<VipOverlay schemaVersion="7.0">'
            '<Locality id="loc1"><PollingLocationIds/></Locality>'
            "</VipOverlay>"
        )
        bad_dup = (
            '<VipOverlay schemaVersion="7.0">'
            '<Locality id="dup"><Name>A</Name></Locality>'
            '<Locality id="dup"><Name>B</Name></Locality>'
            "</VipOverlay>"
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            td = Path(tmpdir)
            ok_path = td / "valid_ov.xml"
            _write_doc(ok_path, valid_ov)
            bad_empty_path = td / "bad_empty.xml"
            bad_empty_path.write_text(bad_empty, encoding="utf-8")
            bad_dup_path = td / "bad_dup.xml"
            bad_dup_path.write_text(bad_dup, encoding="utf-8")
            java_src = td / "XercesCheck.java"
            java_src.write_text(
                """
                import java.io.File;
                import javax.xml.XMLConstants;
                import javax.xml.transform.stream.StreamSource;
                import javax.xml.validation.Schema;
                import javax.xml.validation.SchemaFactory;
                public class XercesCheck {
                  public static void main(String[] args) throws Exception {
                    SchemaFactory sf = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
                    sf.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
                    sf.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
                    sf.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
                    Schema schema = sf.newSchema(new File(args[0]));
                    schema.newValidator().validate(new StreamSource(new File(args[1])));
                    for (int i = 2; i < args.length; i++) {
                      try {
                        schema.newValidator().validate(new StreamSource(new File(args[i])));
                        throw new RuntimeException("Expected XSD failure for " + args[i]);
                      } catch (org.xml.sax.SAXException expected) {}
                    }
                  }
                }
                """,
                encoding="utf-8",
            )
            subprocess.run(["javac", str(java_src)], check=True, capture_output=True, text=True)
            proc = subprocess.run(
                [
                    "java",
                    "-cp",
                    str(td),
                    "XercesCheck",
                    str(REPO_ROOT / "vip_overlay.xsd"),
                    str(ok_path),
                    str(bad_empty_path),
                    str(bad_dup_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


class TestSchematronRules(unittest.TestCase):
    """Exhaustive positive, negative-error, warning, and phase-isolation tests."""

    @classmethod
    def setUpClass(cls):
        parser = etree.XMLParser(resolve_entities=False, no_network=True, load_dtd=False)
        cls.main_xsd = etree.XMLSchema(etree.parse(str(REPO_ROOT / "vip_main.xsd"), parser))
        cls.overlay_xsd = etree.XMLSchema(etree.parse(str(REPO_ROOT / "vip_overlay.xsd"), parser))
        cls.main_sch = REPO_ROOT / "vip_main.sch"
        cls.overlay_sch = REPO_ROOT / "vip_overlay.sch"

    def _assert_batch_errors(self, schema_path, docs_with_expected_rule, phase="strict"):
        """Validate N documents in one jing call and assert exact ordered rule-ID sequence."""
        with tempfile.TemporaryDirectory() as tmpdir:
            paths = []
            expected_seq = []
            for i, (doc, rule_id, base_elem) in enumerate(docs_with_expected_rule):
                base_href = None
                if base_elem is not None:
                    bp = Path(tmpdir) / f"base_{i}.xml"
                    _write_doc(bp, base_elem)
                    base_href = bp.resolve().as_uri()
                p = Path(tmpdir) / f"case_{i}.xml"
                _write_doc(p, doc, base_href=base_href)
                paths.append(p)
                if isinstance(rule_id, tuple):
                    expected_seq.extend([rule_id[0]] * rule_id[1])
                elif rule_id:
                    expected_seq.append(rule_id)
            proc = _run_jing(schema_path, paths, phase=phase)
            out = proc.stdout + proc.stderr
            actual_seq = _extract_rule_ids(out)
            self.assertEqual(
                actual_seq,
                expected_seq,
                f"Mismatch for {schema_path.name} ({phase}).\nOutput:\n{out}",
            )
            if expected_seq:
                self.assertNotEqual(proc.returncode, 0)
            else:
                self.assertEqual(proc.returncode, 0, out)
            return out

    def test_baseline_main_and_overlay_valid_in_full_phase(self):
        main_doc = _valid_main_doc()
        ov_doc = _valid_overlay_doc()
        self.main_xsd.assertValid(main_doc)
        self.overlay_xsd.assertValid(ov_doc)
        with tempfile.TemporaryDirectory() as tmpdir:
            mp = Path(tmpdir) / "main.xml"
            op = Path(tmpdir) / "overlay.xml"
            op_cross = Path(tmpdir) / "overlay_cross.xml"
            _write_doc(mp, main_doc)
            _write_doc(op, ov_doc)
            _write_doc(op_cross, ov_doc, base_href=mp.resolve().as_uri())
            r = _run_jing(self.main_sch, [mp], phase="full")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            r = _run_jing(self.overlay_sch, [op, op_cross], phase="full")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_positive_edge_cases_pass_full_phase(self):
        """Verify allowed/exempt edge cases pass XSD and Schematron -p full without error or warning."""
        main_cases = []

        # 1. EndTime 24:00:00, IsOpen24Hours=true without Hours, omitted TimeZone
        def c_time_ok(d):
            sched = d.find("PollingLocation/Schedule")
            sched.find("Hours/EndTime").text = "24:00:00"
            pl = d.find("PollingLocation")
            s2 = etree.SubElement(pl, "Schedule")
            etree.SubElement(s2, "StartDate").text = "2024-11-04"
            etree.SubElement(s2, "EndDate").text = "2024-11-04"
            etree.SubElement(s2, "IsOpen24Hours").text = "true"
            # Maintain PollingLocation sequence (Schedule before LocationType)
            pl.remove(s2)
            idx = list(pl).index(sched)
            pl.insert(idx + 1, s2)
        main_cases.append(_mutate_main(c_time_ok))

        # 2. Case-insensitive BCP-47 tags, private-use x-custom, omitted AddressStructured @language
        def c_i18n_ok(d):
            t_el = d.find("Candidate/BallotName/Text")
            t_el.set("language", "I-DEFAULT")
            t2 = etree.SubElement(d.find("Candidate/BallotName"), "Text")
            t2.set("language", "zh-Hans")
            t2.text = "Alice"
            t3 = etree.SubElement(d.find("Candidate/BallotName"), "Text")
            t3.set("language", "x-local1")
            t3.text = "Ali"
            pl = d.find("PollingLocation")
            addr = pl.find("AddressStructured")
            del addr.attrib["language"]  # omitted defaults to i-default
            addr2 = copy.deepcopy(addr)
            addr2.set("language", "es")
            pl.insert(1, addr2)
        main_cases.append(_mutate_main(c_i18n_ok))

        # 3. Non-US address omits City/Region/PostalCode without triggering I18N-07 warning, plus Canadian PostalCode
        def c_nonus_ok(d):
            addr = d.find("PollingLocation/AddressStructured")
            addr.find("Country").text = "Canada"
            addr.find("PostalCode").text = "K1A 0B1"
            addr2 = d.find("Locality[@id='loc1']/ElectionAdministration/ContactInformation/PhysicalAddress")
            addr2.find("Country").text = "GB"
            addr2.remove(addr2.find("City"))
            addr2.remove(addr2.find("Region"))
            addr2.remove(addr2.find("PostalCode"))
        main_cases.append(_mutate_main(c_nonus_ok))

        # 4. 8-hop Locality chain to TopLevelLocalityId
        def c_8hops_ok(d):
            prev = "loc1"
            for hop in range(2, 9):
                loc = etree.SubElement(d, "Locality", id=f"loc{hop}")
                etree.SubElement(loc, "Name").text = f"Hop {hop}"
                etree.SubElement(loc, "ParentLocalityId").text = prev
                prev = f"loc{hop}"
        main_cases.append(_mutate_main(c_8hops_ok))

        # 5. Enum 'other' + OtherType/OtherVoteVariation paired properly + polymorphic xsi:type Contest
        def c_enum_poly_ok(d):
            ed = d.find("ElectoralDistrict")
            ed.find("Type").text = "other"
            etree.SubElement(ed, "OtherType").text = "special-district"
            bmc = d.find("BallotMeasureContest")
            bmc.find("VoteVariation").text = "other"
            ovv = etree.SubElement(bmc, "OtherVoteVariation")
            ovv.text = "custom-threshold"
            # Maintain ContestBase ordering: OtherVoteVariation goes at end of ContestBase before ConStatement/ProStatement/.../Type
            bmc.remove(ovv)
            bmc.insert(list(bmc).index(bmc.find("VoteVariation")) + 1, ovv)
        main_cases.append(_mutate_main(c_enum_poly_ok))

        # 6. Polymorphic <Contest xsi:type="BallotMeasureContest"> and <BallotSelection xsi:type="BallotMeasureSelection">
        def c_xsi_poly_ok(d):
            bmc = d.find("BallotMeasureContest")
            bmc.tag = "Contest"
            bmc.set("{http://www.w3.org/2001/XMLSchema-instance}type", "BallotMeasureContest")
            for bms in d.findall("BallotMeasureSelection"):
                bms.tag = "BallotSelection"
                bms.set("{http://www.w3.org/2001/XMLSchema-instance}type", "BallotMeasureSelection")
        main_cases.append(_mutate_main(c_xsi_poly_ok))

        # 7. StreetSegment IncludesAllStreets=true, IncludesAllAddresses=true, single-house even
        def c_ss_ok(d):
            ss2 = etree.Element("StreetSegment", id="ss_all_streets")
            etree.SubElement(ss2, "City").text = "Springfield"
            etree.SubElement(ss2, "IncludesAllAddresses").text = "false"
            etree.SubElement(ss2, "IncludesAllStreets").text = "true"
            etree.SubElement(ss2, "OddEvenBoth").text = "both"
            etree.SubElement(ss2, "PrecinctId").text = "prec1"
            etree.SubElement(ss2, "Region").text = "VA"
            d.append(ss2)
            ss3 = etree.Element("StreetSegment", id="ss_all_addr")
            etree.SubElement(ss3, "City").text = "Springfield"
            etree.SubElement(ss3, "IncludesAllAddresses").text = "true"
            etree.SubElement(ss3, "IncludesAllStreets").text = "false"
            etree.SubElement(ss3, "OddEvenBoth").text = "both"
            etree.SubElement(ss3, "PrecinctId").text = "prec1"
            etree.SubElement(ss3, "Region").text = "VA"
            etree.SubElement(ss3, "StreetName").text = "Oak Rd"
            d.append(ss3)
            ss4 = etree.Element("StreetSegment", id="ss_single_even")
            etree.SubElement(ss4, "City").text = "Springfield"
            etree.SubElement(ss4, "OddEvenBoth").text = "even"
            etree.SubElement(ss4, "PrecinctId").text = "prec1"
            etree.SubElement(ss4, "StartHouseNumber").text = "42"
            etree.SubElement(ss4, "EndHouseNumber").text = "42"
            etree.SubElement(ss4, "Region").text = "VA"
            etree.SubElement(ss4, "StreetName").text = "Elm St"
            d.append(ss4)
            # Standard 100..199 block range with OddEvenBoth='odd' passes without warning
            ss5 = etree.Element("StreetSegment", id="ss_block_range")
            etree.SubElement(ss5, "City").text = "Springfield"
            etree.SubElement(ss5, "OddEvenBoth").text = "odd"
            etree.SubElement(ss5, "PrecinctId").text = "prec1"
            etree.SubElement(ss5, "StartHouseNumber").text = "100"
            etree.SubElement(ss5, "EndHouseNumber").text = "199"
            etree.SubElement(ss5, "Region").text = "VA"
            etree.SubElement(ss5, "StreetName").text = "Maple Ave"
            d.append(ss5)
        main_cases.append(_mutate_main(c_ss_ok))

        # 8. Geo: latlong LocationIdentifier, sha-512 ExternalFile, LatLng at poles, Unicode lowercase OCD-ID
        def c_geo_ok(d):
            pl = d.find("PollingLocation")
            li = etree.Element("LocationIdentifier", provider="gps")
            etree.SubElement(li, "Type").text = "latlong"
            etree.SubElement(li, "Value").text = "-90.0, 180.0"
            pl.insert(list(pl).index(pl.find("Directions")), li)
            ef = d.find("ExternalFile")
            ef.find("Checksum/Algorithm").text = "sha-512"
            ef.find("Checksum/Value").text = "ab" * 64
            d.find("ElectoralDistrict/ExternalIdentifier/Value").text = (
                "ocd-division/country:us/state:nm/county:doña_ana"
            )
        main_cases.append(_mutate_main(c_geo_ok))

        # 9. US ContactInformation MailingAddress/PhysicalAddress omitting City/Region/PostalCode passes without I18N-07 warning
        def c_us_contact_addr_ok(d):
            ci = d.find("Locality[@id='loc1']/ElectionAdministration/ContactInformation")
            phys = ci.find("PhysicalAddress")
            phys.remove(phys.find("City"))
            phys.remove(phys.find("Region"))
            phys.remove(phys.find("PostalCode"))
            mail = etree.Element("MailingAddress")
            etree.SubElement(mail, "AddressLine").text = "PO Box 100, Springfield, VA 22150"
            ci.insert(0, mail)
        main_cases.append(_mutate_main(c_us_contact_addr_ok))

        for doc in main_cases:
            self.main_xsd.assertValid(doc)

        # Positive overlay cases (standalone + base-linked)
        ov_cases = []
        base_doc = _valid_main_doc()

        # Overlay: <ClearSchedule/> + <Schedule> (explicitly valid!), <IsInactive> + field update, <IsInactive> on isNew="true", <ClearSpatialBoundary/>, valid cross-doc SpatialBoundary reassignment, Enum clear-then-set & cross-doc merge
        def ov_complex_ok(d):
            pl_upd = etree.SubElement(d, "PollingLocation", id="pl1")
            etree.SubElement(pl_upd, "ClearSchedule")
            s = etree.SubElement(pl_upd, "Schedule")
            etree.SubElement(s, "StartDate").text = "2024-11-05"
            etree.SubElement(s, "EndDate").text = "2024-11-05"
            etree.SubElement(s, "IsOrByAppointment").text = "true"
            etree.SubElement(pl_upd, "IsInactive").text = "Relocated temporarily"

            # Add IsInactive to isNew="true" PollingLocation (must be allowed!)
            pl_new = d.find("PollingLocation[@isNew='true']")
            etree.SubElement(pl_new, "IsInactive").text = "Pending opening inspection"

            # Precinct ClearSpatialBoundary
            pr1 = etree.SubElement(d, "Precinct", id="prec1")
            etree.SubElement(pr1, "ClearSpatialBoundary")

            # ElectoralDistrict clear Type then set Type=other + OtherType
            ed = etree.SubElement(d, "ElectoralDistrict", id="ed1")
            etree.SubElement(ed, "Type").text = "other"
            etree.SubElement(ed, "OtherType").text = "fire-district"
        ov_cases.append((_mutate_overlay(ov_complex_ok), None))
        ov_cases.append((_mutate_overlay(ov_complex_ok), base_doc))

        # Overlay cross-doc SpatialBoundary reassignment matching base feature
        def ov_sb_ok(d):
            d[:] = []
            pr = etree.SubElement(d, "Precinct", id="prec1")
            sb = etree.SubElement(pr, "SpatialBoundary")
            egf = etree.SubElement(sb, "ExternalGeospatialFeature")
            etree.SubElement(egf, "ExternalFileId").text = "ef1"
            etree.SubElement(egf, "FileFormat").text = "shp"
            fi = etree.SubElement(egf, "FeatureIdentifier")
            etree.SubElement(fi, "Index").text = "0"
        ov_cases.append((_mutate_overlay(ov_sb_ok), base_doc))

        with tempfile.TemporaryDirectory() as tmpdir:
            main_paths = []
            for i, doc in enumerate(main_cases):
                p = Path(tmpdir) / f"main_pos_{i}.xml"
                _write_doc(p, doc)
                main_paths.append(p)
            r_main = _run_jing(self.main_sch, main_paths, phase="full")
            self.assertEqual(r_main.returncode, 0, r_main.stdout + r_main.stderr)

            ov_paths = []
            for i, (ov_doc, base_el) in enumerate(ov_cases):
                self.overlay_xsd.assertValid(ov_doc)
                href = None
                if base_el is not None:
                    bp = Path(tmpdir) / f"base_pos_{i}.xml"
                    _write_doc(bp, base_el)
                    href = bp.resolve().as_uri()
                op = Path(tmpdir) / f"ov_pos_{i}.xml"
                _write_doc(op, ov_doc, base_href=href)
                ov_paths.append(op)
            op_ssrf = Path(tmpdir) / "ov_ssrf.xml"
            _write_doc(op_ssrf, _valid_overlay_doc(), base_href="https://example.invalid/feed.xml")
            ov_paths.append(op_ssrf)
            op_unmatched_pi = Path(tmpdir) / "ov_unmatched_pi.xml"
            raw_ov = etree.tostring(
                _valid_overlay_doc(), encoding="utf-8", pretty_print=True
            ).decode("utf-8")
            op_unmatched_pi.write_text(
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                "<?vip-base-feed file:///nonexistent_unquoted_uri.xml?>\n"
                + raw_ov,
                encoding="utf-8",
            )
            ov_paths.append(op_unmatched_pi)
            r_ov = _run_jing(self.overlay_sch, ov_paths, phase="full")
            self.assertEqual(r_ov.returncode, 0, r_ov.stdout + r_ov.stderr)

    def test_main_error_rules_batch_1(self):
        """Test primary triggers for all main-feed error rule IDs."""
        cases = []

        # I18N-01: mixed text and <Text>
        def e_i18n_01(d):
            bn = d.find("Candidate/BallotName")
            bn.text = "Mixed text "
        cases.append((_mutate_main(e_i18n_01), "I18N-01", None))

        # I18N-02: whitespace-only <Text>
        def e_i18n_02(d):
            d.find("Candidate/BallotName/Text").text = "   "
        cases.append((_mutate_main(e_i18n_02), "I18N-02", None))

        # I18N-03: missing i-default
        def e_i18n_03(d):
            d.find("Candidate/BallotName/Text").set("language", "en")
        cases.append((_mutate_main(e_i18n_03), "I18N-03", None))

        # I18N-04: duplicate case-insensitive @language
        def e_i18n_04(d):
            t2 = etree.SubElement(d.find("Candidate/BallotName"), "Text")
            t2.set("language", "I-Default")
            t2.text = "Alice Duplicate"
        cases.append((_mutate_main(e_i18n_04), "I18N-04", None))

        # I18N-05: duplicate AddressStructured language on PollingLocation
        def e_i18n_05(d):
            pl = d.find("PollingLocation")
            a2 = copy.deepcopy(pl.find("AddressStructured"))
            a2.set("language", "I-DEFAULT")
            pl.insert(1, a2)
        cases.append((_mutate_main(e_i18n_05), "I18N-05", None))

        # I18N-06: invalid BCP-47 tag
        def e_i18n_06(d):
            bn = d.find("Candidate/BallotName")
            t2 = etree.SubElement(bn, "Text")
            t2.set("language", "zz")  # zz is not valid ISO 639-1
            t2.text = "Bob"
        cases.append((_mutate_main(e_i18n_06), "I18N-06", None))

        # I18N-07: whitespace-only AddressLine
        def e_i18n_07(d):
            d.find("PollingLocation/AddressStructured/AddressLine").text = "   "
        cases.append((_mutate_main(e_i18n_07), "I18N-07", None))

        # TZ-01: unrecognized IANA timezone (still matching XSD pattern Continent/City)
        def e_tz_01(d):
            d.find("PollingLocation/Schedule/TimeZone").text = "America/Fake_City"
        cases.append((_mutate_main(e_tz_01), "TZ-01", None))

        # TIME-01: StartTime >= EndTime
        def e_time_01(d):
            h = d.find("PollingLocation/Schedule/Hours")
            h.find("StartTime").text = "19:00:00"
            h.find("EndTime").text = "06:00:00"
        cases.append((_mutate_main(e_time_01), "TIME-01", None))

        # TIME-02: overlapping Hours in same Schedule
        def e_time_02(d):
            sched = d.find("PollingLocation/Schedule")
            h2 = etree.SubElement(sched, "Hours")
            etree.SubElement(h2, "StartTime").text = "18:00:00"
            etree.SubElement(h2, "EndTime").text = "20:00:00"
        cases.append((_mutate_main(e_time_02), "TIME-02", None))

        # TIME-03: Schedule StartDate > EndDate
        def e_time_03(d):
            sched = d.find("PollingLocation/Schedule")
            sched.find("StartDate").text = "2024-11-06"
            sched.find("EndDate").text = "2024-11-05"
        cases.append((_mutate_main(e_time_03), "TIME-03", None))

        # TIME-04: xs:date with timezone suffix
        def e_time_04(d):
            d.find("PollingLocation/Schedule/StartDate").text = "2024-11-05Z"
            d.find("PollingLocation/Schedule/EndDate").text = "2024-11-05"
        cases.append((_mutate_main(e_time_04), "TIME-04", None))

        # TIME-05: IsOpen24Hours=true combined with Hours
        def e_time_05(d):
            sched = d.find("PollingLocation/Schedule")
            io = etree.SubElement(sched, "IsOpen24Hours")
            io.text = "true"
            sched.remove(io)
            sched.insert(list(sched).index(sched.find("Hours")) + 1, io)
        cases.append((_mutate_main(e_time_05), "TIME-05", None))

        # REF-01: cross-type target reference (PartyId pointing to Person)
        def e_ref_01(d):
            d.find("Candidate/PartyId").text = "per1"
        cases.append((_mutate_main(e_ref_01), "REF-01", None))

        # REF-02: duplicate ID inside IDREFS
        def e_ref_02(d):
            d.find("BallotMeasureContest/BallotSelectionIds").text = "bms1 bms2 bms1"
        cases.append((_mutate_main(e_ref_02), "REF-02", None))

        # REF-03: CandidateContest pointing to BallotMeasureSelection
        def e_ref_03(d):
            d.find("CandidateContest/BallotSelectionIds").text = "bms1"
            d.find("OrderedContest[@id='oc1']/OrderedBallotSelectionIds").text = "bms1"
        cases.append((_mutate_main(e_ref_03), "REF-03", None))

        # REF-04: OrderedBallotSelectionIds not subset of Contest BallotSelectionIds
        def e_ref_04(d):
            d.find("OrderedContest[@id='oc1']/OrderedBallotSelectionIds").text = "cs1 bms1"
        cases.append((_mutate_main(e_ref_04), "REF-04", None))

        # REF-05: 2-hop ParentLocalityId cycle (loc2 and loc3 each trigger nocycle + root -> 4 REF-05 errors)
        def e_ref_05(d):
            l2 = etree.SubElement(d, "Locality", id="loc2")
            etree.SubElement(l2, "Name").text = "L2"
            etree.SubElement(l2, "ParentLocalityId").text = "loc3"
            l3 = etree.SubElement(d, "Locality", id="loc3")
            etree.SubElement(l3, "Name").text = "L3"
            etree.SubElement(l3, "ParentLocalityId").text = "loc2"
        cases.append((_mutate_main(e_ref_05), ("REF-05", 4), None))

        # REF-08: VotesAllowed != 1 when VoteVariation='1-of-m'
        def e_ref_08(d):
            d.find("CandidateContest/VotesAllowed").text = "2"
        cases.append((_mutate_main(e_ref_08), "REF-08", None))

        # ENUM-01: Type='other' missing OtherType
        def e_enum_01(d):
            d.find("ElectoralDistrict/Type").text = "other"
        cases.append((_mutate_main(e_enum_01), "ENUM-01", None))

        # SS-01: IncludesAllStreets=true with StreetName
        def e_ss_01(d):
            ss = d.find("StreetSegment")
            ss.find("IncludesAllStreets").text = "true"
            ss.find("OddEvenBoth").text = "both"
            ss.remove(ss.find("StartHouseNumber"))
            ss.remove(ss.find("EndHouseNumber"))
        cases.append((_mutate_main(e_ss_01), "SS-01", None))

        # SS-02: IncludesAllAddresses=true with house numbers
        def e_ss_02(d):
            ss = d.find("StreetSegment")
            ss.find("IncludesAllAddresses").text = "true"
            ss.find("OddEvenBoth").text = "both"
        cases.append((_mutate_main(e_ss_02), "SS-02", None))

        # SS-03: StartHouseNumber > EndHouseNumber
        def e_ss_03(d):
            ss = d.find("StreetSegment")
            ss.find("StartHouseNumber").text = "199"
            ss.find("EndHouseNumber").text = "101"
        cases.append((_mutate_main(e_ss_03), "SS-03", None))

        # SS-04: single-house even number with OddEvenBoth='odd'
        def e_ss_04(d):
            ss = d.find("StreetSegment")
            ss.find("StartHouseNumber").text = "100"
            ss.find("EndHouseNumber").text = "100"
            ss.find("OddEvenBoth").text = "odd"
        cases.append((_mutate_main(e_ss_04), "SS-04", None))

        # GEO-01: Latitude out of [-90, 90]
        def e_geo_01(d):
            d.find("PollingLocation/LatLng/Latitude").text = "91.5"
        cases.append((_mutate_main(e_geo_01), "GEO-01", None))

        # GEO-02: invalid pluscode
        def e_geo_02(d):
            d.find("PollingLocation/LocationIdentifier/Value").text = "INVALID-CODE"
        cases.append((_mutate_main(e_geo_02), "GEO-02", None))

        # GEO-03: invalid ocd-id
        def e_geo_03(d):
            d.find("ElectoralDistrict/ExternalIdentifier/Value").text = "not-an-ocd-id"
        cases.append((_mutate_main(e_geo_03), "GEO-03", None))

        # GEO-04: sha-256 wrong checksum length
        def e_geo_04(d):
            d.find("ExternalFile/Checksum/Value").text = "deadbeef"
        cases.append((_mutate_main(e_geo_04), "GEO-04", None))

        # GEO-05: duplicate FeatureIdentifier/Index on shp ExternalGeospatialFeature
        def e_geo_05(d):
            ef = d.find("ExternalFile")
            ef.find("FileUri").text = "boundaries/precincts.shp"
            egf = d.find("Precinct/SpatialBoundary/ExternalGeospatialFeature")
            egf.find("FileFormat").text = "shp"
            fi2 = etree.SubElement(egf, "FeatureIdentifier")
            etree.SubElement(fi2, "Index").text = "0"
        cases.append((_mutate_main(e_geo_05), "GEO-05", None))

        # HYG-01: ftp:// URI in InternationalizedUri
        def e_hyg_01(d):
            d.find("Source/OrganizationUri").text = "ftp://example.gov/file"
        cases.append((_mutate_main(e_hyg_01), "HYG-01", None))

        # HYG-02: empty ElectionAdministration container
        def e_hyg_02(d):
            d.find("Locality[@id='loc1']/ElectionAdministration")[:] = []
        cases.append((_mutate_main(e_hyg_02), "HYG-02", None))

        # HYG-03: whitespace-only Source/Name
        def e_hyg_03(d):
            d.find("Source/Name").text = "   "
        cases.append((_mutate_main(e_hyg_03), "HYG-03", None))

        self._assert_batch_errors(self.main_sch, cases, phase="strict")

    def test_main_error_rules_batch_2_variants(self):
        """Test secondary edge-case triggers (TIME-01 24:00 StartTime, empty Schedule, self-ParentLocality, polymorphic REF-03, etc.)."""
        cases = []

        # TIME-01: StartTime="24:00:00" fails even if EndTime="24:00:00"
        def v_time_01_start24(d):
            h = d.find("PollingLocation/Schedule/Hours")
            h.find("StartTime").text = "24:00:00"
            h.find("EndTime").text = "24:00:00"
        cases.append((_mutate_main(v_time_01_start24), "TIME-01", None))

        # TIME-03: Term StartDate > EndDate
        def v_time_03_term(d):
            term = d.find("Office/Term")
            term.find("StartDate").text = "2029-01-01"
            term.find("EndDate").text = "2025-01-01"
        cases.append((_mutate_main(v_time_03_term), "TIME-03", None))

        # TIME-05: Schedule with no Hours and no boolean flags
        def v_time_05_empty_sched(d):
            sched = d.find("PollingLocation/Schedule")
            sched.remove(sched.find("Hours"))
        cases.append((_mutate_main(v_time_05_empty_sched), "TIME-05", None))

        # REF-03: Polymorphic <Contest xsi:type="PartyContest"> pointing to CandidateSelection
        def v_ref_03_poly(d):
            cc = d.find("CandidateContest")
            cc.tag = "Contest"
            cc.set("{http://www.w3.org/2001/XMLSchema-instance}type", "PartyContest")
        cases.append((_mutate_main(v_ref_03_poly), "REF-03", None))

        # REF-05: self-referencing ParentLocalityId (fires both self and nocycle -> expect 2 REF-05)
        # Keep batch 2 clean with distinct 9-hop chain (exceeds 8-hop limit, hits only REF-05-root)
        def v_ref_05_9hops(d):
            prev = "loc1"
            for hop in range(2, 10):
                loc = etree.SubElement(d, "Locality", id=f"loc{hop}")
                etree.SubElement(loc, "Name").text = f"Hop {hop}"
                etree.SubElement(loc, "ParentLocalityId").text = prev
                prev = f"loc{hop}"
        cases.append((_mutate_main(v_ref_05_9hops), "REF-05", None))

        # ENUM-01: OtherType specified when Type != 'other'
        def v_enum_01_extra(d):
            etree.SubElement(d.find("ElectoralDistrict"), "OtherType").text = "extraneous"
        cases.append((_mutate_main(v_enum_01_extra), "ENUM-01", None))

        # GEO-03: invalid characters ('&', space) and uppercase Unicode letters in ocd-id
        def v_geo_03_amp(d):
            d.find("ElectoralDistrict/ExternalIdentifier/Value").text = (
                "ocd-division/country:us/state:va/county:king_&_queen"
            )
        cases.append((_mutate_main(v_geo_03_amp), "GEO-03", None))

        def v_geo_03_upper(d):
            d.find("ElectoralDistrict/ExternalIdentifier/Value").text = (
                "ocd-division/country:us/state:nm/county:Doña_Ana"
            )
        cases.append((_mutate_main(v_geo_03_upper), "GEO-03", None))

        # GEO-04: ExternalFile path traversal '..' in relative FileUri
        def v_geo_04_traversal(d):
            d.find("ExternalFile/FileUri").text = "../secret.geojson"
        cases.append((_mutate_main(v_geo_04_traversal), "GEO-04", None))

        # HYG-02: empty <BallotStyle id="bs1"/>
        def v_hyg_02_empty_bs(d):
            # Keep OrderedContestIds omitted ONLY on a second unused BallotStyle to avoid REF-01
            bs2 = etree.SubElement(d, "BallotStyle", id="bs_empty")
            assert bs2 is not None
        cases.append((_mutate_main(v_hyg_02_empty_bs), "HYG-02", None))

        self._assert_batch_errors(self.main_sch, cases, phase="strict")

    def test_overlay_error_rules_standalone_and_crossdoc(self):
        """Test all overlay-only and cross-doc error rules (OVR-01..03, 06..07, 10..11, ENUM-02)."""
        standalone_cases = []

        # OVR-01: empty <VipOverlay/>
        def o_01(d):
            d[:] = []
        standalone_cases.append((_mutate_overlay(o_01), "OVR-01", None))

        # OVR-02: empty entity <Locality id="loc1"/>
        def o_02(d):
            d.find("Locality")[:] = []
        standalone_cases.append((_mutate_overlay(o_02), "OVR-02", None))

        # OVR-03: isNew="true" missing LocationType
        def o_03(d):
            pl = d.find("PollingLocation[@isNew='true']")
            pl.remove(pl.find("LocationType"))
        standalone_cases.append((_mutate_overlay(o_03), "OVR-03", None))

        # OVR-07: duplicate case-insensitive AppliesTo
        def o_07(d):
            d.find("Locality/EmergencyNotice/AppliesTo[2]").text = "SEARCH"
        standalone_cases.append((_mutate_overlay(o_07), "OVR-07", None))

        # OVR-07: empty/whitespace-only AppliesTo
        def o_07_empty(d):
            d.find("Locality/EmergencyNotice/AppliesTo[2]").text = "   "
        standalone_cases.append((_mutate_overlay(o_07_empty), "OVR-07", None))

        # ENUM-02: standalone Type='other' without OtherType
        def o_enum_02(d):
            ed = etree.SubElement(d, "ElectoralDistrict", id="ed1")
            etree.SubElement(ed, "Type").text = "other"
        standalone_cases.append((_mutate_overlay(o_enum_02), "ENUM-02", None))

        # REF-01 standalone: PollingLocationIds resolving inside overlay points to Locality instead of PollingLocation
        def o_ref_01(d):
            d.find("Locality/PollingLocationIds").text = "loc1"
        standalone_cases.append((_mutate_overlay(o_ref_01), "REF-01", None))

        self._assert_batch_errors(self.overlay_sch, standalone_cases, phase="strict")

        # Cross-doc cases requiring base_doc
        base_doc = _valid_main_doc()
        cross_cases = []

        # OVR-06: SpatialBoundary reassignment references nonexistent index on ExternalFile in base feed
        def c_ovr_06(d):
            d[:] = []
            pr = etree.SubElement(d, "Precinct", id="prec1")
            sb = etree.SubElement(pr, "SpatialBoundary")
            egf = etree.SubElement(sb, "ExternalGeospatialFeature")
            etree.SubElement(egf, "ExternalFileId").text = "ef1"
            etree.SubElement(egf, "FileFormat").text = "geojson"
            fi = etree.SubElement(egf, "FeatureIdentifier")
            etree.SubElement(fi, "Index").text = "99"
        cross_cases.append((_mutate_overlay(c_ovr_06), "OVR-06", base_doc))

        # OVR-10: isNew="true" collides with existing base entity ID 'pl1'
        def c_ovr_10(d):
            d.find("PollingLocation[@isNew='true']").set("id", "pl1")
            d.find("Locality/PollingLocationIds").text = "pl1"
        cross_cases.append((_mutate_overlay(c_ovr_10), "OVR-10", base_doc))

        # OVR-11: PollingLocationIds references unknown ID not in base feed or @isNew="true"
        def c_ovr_11(d):
            d.find("Locality/PollingLocationIds").text = "pl1 pl_missing pl_new"
        cross_cases.append((_mutate_overlay(c_ovr_11), "OVR-11", base_doc))

        # ENUM-02 cross-doc: base has Type='municipality', overlay sets OtherType without setting Type='other'
        def c_enum_02(d):
            ed = etree.SubElement(d, "ElectoralDistrict", id="ed1")
            etree.SubElement(ed, "OtherType").text = "orphan-other"
        cross_cases.append((_mutate_overlay(c_enum_02), "ENUM-02", base_doc))

        # OVR-10-base / R22: non-VipObject XML file is rejected without probing its IDs
        cross_cases.append(
            (_valid_overlay_doc(), "OVR-10", etree.fromstring(b"<OtherXml><Locality id='loc1'/></OtherXml>"))
        )

        # REF-04 cross-doc: OrderedContest omits optional ContestId (inherited from base oc1 -> cc1) and references non-member selection bms1
        def c_ref_04_inherited_cid(d):
            oc = etree.SubElement(d, "OrderedContest", id="oc1")
            etree.SubElement(oc, "OrderedBallotSelectionIds").text = "cs1 bms1"
        cross_cases.append((_mutate_overlay(c_ref_04_inherited_cid), "REF-04", base_doc))

        self._assert_batch_errors(self.overlay_sch, cross_cases, phase="strict")

        # OVR-10-base: missing local base feed file in <?vip-base-feed?>
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_pi_ov = Path(tmpdir) / "missing_pi_ov.xml"
            _write_doc(
                missing_pi_ov,
                _valid_overlay_doc(),
                base_href=(Path(tmpdir) / "missing_base.xml").resolve().as_uri(),
            )
            proc = _run_jing(self.overlay_sch, [missing_pi_ov], phase="strict")
            self.assertNotEqual(proc.returncode, 0)
            self.assertEqual(_extract_rule_ids(proc.stdout + proc.stderr), ["OVR-10"])

    def test_warnings_pass_strict_and_fire_in_full_phase(self):
        """Verify all warning rules pass -p strict cleanly and emit exact rule IDs in -p full."""
        main_warnings = []

        # I18N-07 warning: US AddressStructured missing PostalCode
        def w_i18n_07(d):
            addr = d.find("PollingLocation/AddressStructured")
            addr.remove(addr.find("PostalCode"))
        main_warnings.append((_mutate_main(w_i18n_07), "I18N-07", None))

        # TZ-02: backward-compatible IANA alias US/Eastern
        def w_tz_02(d):
            d.find("PollingLocation/Schedule/TimeZone").text = "US/Eastern"
        main_warnings.append((_mutate_main(w_tz_02), "TZ-02", None))

        # TIME-06: Source/DateTime missing timezone offset
        def w_time_06(d):
            d.find("Source/DateTime").text = "2024-10-20T12:00:00"
        main_warnings.append((_mutate_main(w_time_06), "TIME-06", None))

        # TIME-07: RegistrationDeadline after Election Date
        def w_time_07(d):
            d.find("Election/RegistrationDeadline").text = "2024-11-06"
        main_warnings.append((_mutate_main(w_time_07), "TIME-07", None))

        # TIME-08: deprecated free-text Hours
        def w_time_08(d):
            pl = d.find("PollingLocation")
            h = etree.Element("Hours")
            h.text = "6am to 7pm"
            pl.insert(list(pl).index(pl.find("Schedule")), h)
        main_warnings.append((_mutate_main(w_time_08), "TIME-08", None))

        # REF-06: DropOff PollingLocation specifying PartyIds
        def w_ref_06(d):
            pl = d.find("PollingLocation")
            pl.find("LocationType").text = "DropOff"
            pi = etree.Element("PartyIds")
            pi.text = "par1"
            pl.insert(list(pl).index(pl.find("LatLng")), pi)
        main_warnings.append((_mutate_main(w_ref_06), "REF-06", None))

        # REF-07: IsMailOnly Precinct pointing to InPersonDayOf PollingLocation
        def w_ref_07(d):
            pr = d.find("Precinct")
            imo = etree.Element("IsMailOnly")
            imo.text = "true"
            pr.insert(list(pr).index(pr.find("LocalityId")), imo)
        main_warnings.append((_mutate_main(w_ref_07), "REF-07", None))

        # SS-03 warn: leading zero / 0 house number
        def w_ss_03(d):
            d.find("StreetSegment/StartHouseNumber").text = "0"
            d.find("StreetSegment/EndHouseNumber").text = "99"
            d.find("StreetSegment/OddEvenBoth").text = "both"
        main_warnings.append((_mutate_main(w_ss_03), "SS-03", None))

        # GEO-01 warn: Null Island (0, 0)
        def w_geo_01(d):
            d.find("PollingLocation/LatLng/Latitude").text = "0"
            d.find("PollingLocation/LatLng/Longitude").text = "0"
        main_warnings.append((_mutate_main(w_geo_01), "GEO-01", None))

        # GEO-02 warn: geocoder-id without @provider
        def w_geo_02(d):
            li = d.find("PollingLocation/LocationIdentifier")
            del li.attrib["provider"]
            li.find("Type").text = "geocoder-id"
            li.find("Value").text = "abc123"
        main_warnings.append((_mutate_main(w_geo_02), "GEO-02", None))

        # GEO-03 warn: non-numeric fips ExternalIdentifier
        def w_geo_03(d):
            d.find("Locality[@id='loc1']/ExternalIdentifier/Value").text = "VA059"
        main_warnings.append((_mutate_main(w_geo_03), "GEO-03", None))

        # GEO-04 warn: unused ExternalFile
        def w_geo_04(d):
            pr = d.find("Precinct")
            pr.remove(pr.find("SpatialBoundary"))
        main_warnings.append((_mutate_main(w_geo_04), "GEO-04", None))

        # HYG-02 warn: Person without FullName/FirstName/LastName
        def w_hyg_02(d):
            per = d.find("Person")
            per.remove(per.find("FullName"))
        main_warnings.append((_mutate_main(w_hyg_02), "HYG-02", None))

        # HYG-03 warn: whitespace-only @label attribute
        def w_hyg_03(d):
            d.find("Locality[@id='loc1']/ElectionAdministration/ContactInformation").set("label", "  ")
        main_warnings.append((_mutate_main(w_hyg_03), "HYG-03", None))

        # HYG-04 warn: malformed US ZIP code
        def w_hyg_04(d):
            d.find("PollingLocation/AddressStructured/PostalCode").text = "2215"
        main_warnings.append((_mutate_main(w_hyg_04), "HYG-04", None))

        # Strict phase: 0 errors!
        self._assert_batch_errors(
            self.main_sch, [(doc, None, b) for doc, _, b in main_warnings], phase="strict"
        )
        # Full phase: exact expected warning IDs and non-empty TZ-02 canonical target!
        full_out = self._assert_batch_errors(self.main_sch, main_warnings, phase="full")
        self.assertIn(
            "TimeZone 'US/Eastern' is a backward-compatible IANA alias; prefer canonical zone 'America/New_York'",
            full_out,
        )

        # Overlay warnings
        ov_warnings = []

        # OVR-03 warn: Clear* element on isNew="true"
        def ow_ovr_03(d):
            pl = d.find("PollingLocation[@isNew='true']")
            etree.SubElement(pl, "ClearDirections")
        ov_warnings.append((_mutate_overlay(ow_ovr_03), "OVR-03", None))

        # OVR-08 warn: Locality setting both DefaultPollingHours and OverriddenPollingHours
        def ow_ovr_08(d):
            loc = d.find("Locality")
            dph = etree.SubElement(loc, "DefaultPollingHours")
            etree.SubElement(dph, "TimeZone").text = "America/New_York"
            hrs = etree.SubElement(dph, "Hours")
            etree.SubElement(hrs, "StartTime").text = "06:00:00"
            etree.SubElement(hrs, "EndTime").text = "19:00:00"
        ov_warnings.append((_mutate_overlay(ow_ovr_08), "OVR-08", None))

        # I18N-07 warn in overlay: PollingLocation/AddressStructured missing PostalCode
        def ow_i18n_07(d):
            addr = d.find("PollingLocation[@isNew='true']/AddressStructured")
            addr.remove(addr.find("PostalCode"))
        ov_warnings.append((_mutate_overlay(ow_i18n_07), "I18N-07", None))

        self._assert_batch_errors(
            self.overlay_sch, [(doc, None, b) for doc, _, b in ov_warnings], phase="strict"
        )
        self._assert_batch_errors(self.overlay_sch, ov_warnings, phase="full")


class TestCliCommands(unittest.TestCase):
    """Test scripts/vip.py validate and update_timezones CLI subcommands."""

    def _run_cli(self, *args):
        """Invoke scripts/vip.py with args and return CompletedProcess."""
        return subprocess.run(
            [sys.executable, "scripts/vip.py", *args],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_validate_phases_and_base_feed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            td = Path(tmpdir)
            main_ok = td / "main_ok.xml"
            main_warn = td / "main_warn.xml"
            ov_ok = td / "ov_ok.xml"
            ov_bom = td / "ov_bom.xml"
            ov_bad_ref = td / "ov_bad_ref.xml"

            _write_doc(main_ok, _valid_main_doc())

            def add_warn(d):
                d.find("Source/DateTime").text = "2024-10-20T12:00:00"
            _write_doc(main_warn, _mutate_main(add_warn))

            _write_doc(ov_ok, _valid_overlay_doc())
            # UTF-8 BOM without XML declaration to verify _inject_base_feed_pi BOM handling
            ov_bom.write_text(
                "\ufeff"
                + etree.tostring(_valid_overlay_doc(), encoding="unicode"),
                encoding="utf-8",
            )

            def bad_ref(d):
                d.find("Locality/PollingLocationIds").text = "pl_does_not_exist"
            _write_doc(ov_bad_ref, _mutate_overlay(bad_ref))

            r_main_ok = self._run_cli("validate", str(main_ok))
            self.assertEqual(r_main_ok.returncode, 0, r_main_ok.stdout + r_main_ok.stderr)

            r_warn_strict = self._run_cli("validate", str(main_warn), "--phase", "strict")
            self.assertEqual(
                r_warn_strict.returncode, 0, r_warn_strict.stdout + r_warn_strict.stderr
            )

            r_warn_full = self._run_cli("validate", str(main_warn), "--phase", "full")
            self.assertNotEqual(r_warn_full.returncode, 0)
            self.assertIn("[TIME-06]", r_warn_full.stdout + r_warn_full.stderr)

            r_ov_cross_ok = self._run_cli(
                "validate", str(ov_ok), "--base-feed", str(main_ok), "--phase", "full"
            )
            self.assertEqual(
                r_ov_cross_ok.returncode, 0, r_ov_cross_ok.stdout + r_ov_cross_ok.stderr
            )

            r_ov_bom_ok = self._run_cli(
                "validate", str(ov_bom), "--base-feed", str(main_ok), "--phase", "strict"
            )
            self.assertEqual(
                r_ov_bom_ok.returncode, 0, r_ov_bom_ok.stdout + r_ov_bom_ok.stderr
            )

            ov_with_broken_pi = td / "ov_with_broken_pi.xml"
            _write_doc(
                ov_with_broken_pi,
                _valid_overlay_doc(),
                base_href=(td / "missing_embedded_base.xml").resolve().as_uri(),
            )
            r_ov_override = self._run_cli(
                "validate", str(ov_with_broken_pi), "--base-feed", str(main_ok)
            )
            self.assertEqual(
                r_ov_override.returncode, 0, r_ov_override.stdout + r_ov_override.stderr
            )
            self.assertIn("Overriding embedded", r_ov_override.stdout + r_ov_override.stderr)

            r_ov_cross_bad = self._run_cli(
                "validate", str(ov_bad_ref), "--base-feed", str(main_ok)
            )
            self.assertNotEqual(r_ov_cross_bad.returncode, 0)
            self.assertIn("[OVR-11]", r_ov_cross_bad.stdout + r_ov_cross_bad.stderr)

    def test_cli_update_timezones_synthetic_fixture(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            td = Path(tmpdir)
            tz_dir = td / "zoneinfo"
            tz_out = td / "iana_tz.xml"

            tz_dir.mkdir()
            (tz_dir / "tzdata.zi").write_text(
                "# Synthetic tzdata fixture\n"
                "Z America/New_York -5:0 US E%sT\n"
                "Z Etc/UTC 0 - UTC\n"
                "L America/New_York US/Eastern\n"
                "L US/Eastern America/Legacy_Chain\n"
                "Z EST -5:0 - EST\n",
                encoding="utf-8",
            )
            (tz_dir / "zone1970.tab").write_text(
                "# comment\nUS\t+404251-0740023\tAmerica/New_York\tEastern\n",
                encoding="utf-8",
            )
            (tz_dir / "zone.tab").write_text(
                "US\t+404251-0740023\tAmerica/New_York\tEastern\n",
                encoding="utf-8",
            )
            r_tz = self._run_cli(
                "update_timezones", "--zoneinfo-dir", str(tz_dir), "--output", str(tz_out)
            )
            self.assertEqual(r_tz.returncode, 0, r_tz.stdout + r_tz.stderr)
            tz_doc = etree.parse(str(tz_out))
            zones = {
                z.text: (z.get("canonical"), z.get("target"))
                for z in tz_doc.findall("Zone")
            }
            self.assertEqual(
                zones,
                {
                    "America/Legacy_Chain": ("false", "America/New_York"),
                    "America/New_York": ("true", None),
                    "Etc/UTC": ("true", None),
                    "US/Eastern": ("false", "America/New_York"),
                },
            )

            r_missing_tz = self._run_cli(
                "update_timezones",
                "--zoneinfo-dir",
                str(td / "no_such_zoneinfo"),
                "--output",
                str(tz_out),
            )
            self.assertNotEqual(r_missing_tz.returncode, 0)
            self.assertIn("tzdata file not found", r_missing_tz.stdout + r_missing_tz.stderr)

    def test_cli_validate_negative_error_paths(self):
        """Verify CLI error handling for missing files, syntax/XSD errors, and invalid flags."""
        with tempfile.TemporaryDirectory() as tmpdir:
            td = Path(tmpdir)
            main_ok = td / "main_ok.xml"
            ov_ok = td / "ov_ok.xml"
            bad_syntax = td / "bad_syntax.xml"
            unknown_root = td / "unknown_root.xml"
            xsd_invalid = td / "xsd_invalid.xml"

            _write_doc(main_ok, _valid_main_doc())
            _write_doc(ov_ok, _valid_overlay_doc())
            bad_syntax.write_text("<VipObject><unclosed></VipObject>", encoding="utf-8")
            unknown_root.write_text("<OtherRoot/>", encoding="utf-8")
            xsd_invalid.write_text(
                '<VipOverlay schemaVersion="7.0"><Bogus/></VipOverlay>',
                encoding="utf-8",
            )

            r_missing = self._run_cli("validate", str(td / "does_not_exist.xml"))
            self.assertNotEqual(r_missing.returncode, 0)
            self.assertIn("XML file not found", r_missing.stdout + r_missing.stderr)

            r_syntax = self._run_cli("validate", str(bad_syntax))
            self.assertNotEqual(r_syntax.returncode, 0)
            self.assertIn("XML syntax error", r_syntax.stdout + r_syntax.stderr)

            r_auto_root = self._run_cli("validate", str(unknown_root))
            self.assertNotEqual(r_auto_root.returncode, 0)
            self.assertIn(
                "Could not auto-detect feed type",
                r_auto_root.stdout + r_auto_root.stderr,
            )

            r_type_mismatch = self._run_cli(
                "validate", str(main_ok), "--type", "overlay"
            )
            self.assertNotEqual(r_type_mismatch.returncode, 0)
            self.assertIn(
                "does not match --type overlay",
                r_type_mismatch.stdout + r_type_mismatch.stderr,
            )

            r_base_on_main = self._run_cli(
                "validate", str(main_ok), "--base-feed", str(main_ok)
            )
            self.assertNotEqual(r_base_on_main.returncode, 0)
            self.assertIn(
                "--base-feed can only be used",
                r_base_on_main.stdout + r_base_on_main.stderr,
            )

            r_missing_base = self._run_cli(
                "validate", str(ov_ok), "--base-feed", str(td / "missing_base.xml")
            )
            self.assertNotEqual(r_missing_base.returncode, 0)
            self.assertIn("Base feed file not found", r_missing_base.stdout + r_missing_base.stderr)

            r_xsd = self._run_cli("validate", str(xsd_invalid))
            self.assertNotEqual(r_xsd.returncode, 0)
            self.assertIn("XSD validation failed", r_xsd.stdout + r_xsd.stderr)


if __name__ == "__main__":
    unittest.main()
