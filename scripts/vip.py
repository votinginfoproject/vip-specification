"""
Entry point for the reST script for VIP contributors.

Script usage:

From the repository root (using Python 3.4 or above):

  $ python scripts/vip.py -h

reStructuredText (aka reST) [1] is a markup language used for
documentation.  VIP uses reST for its documentation.

This script is mainly for auto-generating much of the reST markup
(especially the reST that involve tables).  The script generates the
reST from configuration files that are in a format called YAML [2]
(specifically YAML 1.1 [3]).  YAML files are much easier to edit and
manipulate than reST when tables are involved.  The YAML can also be
thought of as at part of the VIP documentation in an "open data" format,
since the YAML represents tabular data stored in a structured,
machine-readable form.


[1] reST: http://docutils.sourceforge.net/rst.html
[2] YAML: http://yaml.org/
[3] YAML 1.1: http://yaml.org/spec/1.1/

"""

import argparse
import contextlib
import logging
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap

from lxml import etree

from vippy import common
from vippy.common import XML_DIR
from vippy import rest


_log = logging.getLogger()

REPO_ROOT = Path(__file__).resolve().parent.parent
ZONE_NAME_RE = re.compile(
    r"^(Africa|America|Antarctica|Arctic|Asia|Atlantic|Australia|"
    r"Brazil|Canada|Chile|Etc|Europe|Indian|Mexico|Pacific|US)"
    r"(/[A-Za-z0-9+_-]+)+$"
)
DEPRECATED_CANONICAL_PREFIXES = (
    "US/",
    "Canada/",
    "Mexico/",
    "Brazil/",
    "Chile/",
)

FORMATTER_CLASS = argparse.RawDescriptionHelpFormatter

HELP_SUMMARY = """\
Helper script for VIP contributors.
"""


def _wrap(text):
    """Format text for help output."""
    paras = text.split("\n\n")
    paras = [textwrap.fill(p) for p in paras]
    text = "\n\n".join(paras)

    return text


def ns_to_paths(ns, parent_dir, ext):
    """Return the list of paths specified by an argparse.Namespace object."""
    path = ns.path
    if path:
        paths = [path]
    else:
        rel_paths = common.get_all_files(parent_dir, ext=ext)
        paths = [os.path.join(parent_dir, p) for p in rel_paths]
    return paths


def command_norm_yaml(ns):
    """Run the norm_yaml command."""
    parent_dir = common.YAML_DIR
    paths = ns_to_paths(ns, parent_dir=parent_dir, ext=".yaml")
    for path in paths:
        common.normalize_yaml(path)


def command_make_rest(ns):
    """Run the make_rest command."""
    rest.update_rest_files(ns.type_name)


def command_scratch(ns):
    """Run the scratch command."""
    rest.analyze_types()


def _parse_xml_safe(path):
    """Parse an XML file with XXE and network access disabled."""
    parser = etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
    )
    return etree.parse(str(path), parser)


def generate_iana_timezones_xml(zoneinfo_dir, output_path):
    """Generate iana_timezones.xml deterministically from tzdata files.

    Args:
        zoneinfo_dir: Directory containing tzdata.zi, zone1970.tab, and zone.tab.
        output_path: Destination file path for the generated XML registry.

    Returns:
        Tuple of (canonical_count, alias_count) written to output_path.
    """
    zoneinfo = Path(zoneinfo_dir)
    tzdata_path = zoneinfo / "tzdata.zi"
    zone1970_path = zoneinfo / "zone1970.tab"
    zone_tab_path = zoneinfo / "zone.tab"

    z_entries = set()
    links = {}
    with tzdata_path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.split("#", 1)[0].strip()
            if not line:
                continue
            parts = line.split()
            if parts[0] == "Z" and len(parts) >= 2:
                z_entries.add(parts[1])
            elif parts[0] == "L" and len(parts) >= 3:
                target, link_name = parts[1], parts[2]
                links[link_name] = target

    tab_zones = set()
    for tab_path in (zone1970_path, zone_tab_path):
        with tab_path.open("r", encoding="utf-8") as handle:
            for raw_line in handle:
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) >= 3:
                    tab_zones.add(parts[2])

    candidate_zones = sorted(
        z for z in (z_entries | set(links) | tab_zones) if ZONE_NAME_RE.match(z)
    )

    root = etree.Element("IanaTimeZones")
    canonical_count = 0
    alias_count = 0
    for zone in candidate_zones:
        is_canonical = (
            (zone in z_entries or zone in tab_zones)
            and not zone.startswith(DEPRECATED_CANONICAL_PREFIXES)
        )
        elem = etree.SubElement(root, "Zone")
        elem.text = zone
        if is_canonical:
            elem.set("canonical", "true")
            canonical_count += 1
        elif zone in links:
            target = links[zone]
            seen = {zone}
            while target in links and target not in seen:
                seen.add(target)
                target = links[target]
            elem.set("canonical", "false")
            elem.set("target", target)
            alias_count += 1
        else:
            raise ValueError(
                f"Unhandled non-canonical zone without link target: {zone}"
            )

    etree.indent(root, space="  ")
    tree = etree.ElementTree(root)
    output_file = Path(output_path)
    tree.write(
        str(output_file),
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
    )
    return canonical_count, alias_count


def command_update_timezones(ns):
    """Regenerate iana_timezones.xml from system tzdata files."""
    zoneinfo = Path(ns.zoneinfo_dir)
    for req_file in ("tzdata.zi", "zone1970.tab", "zone.tab"):
        req_path = zoneinfo / req_file
        if not req_path.is_file():
            _log.error("tzdata file not found: %s", req_path)
            sys.exit(1)
    canonical_count, alias_count = generate_iana_timezones_xml(
        ns.zoneinfo_dir, ns.output
    )
    _log.info(
        "Wrote %s (%d canonical zones, %d alias zones)",
        ns.output,
        canonical_count,
        alias_count,
    )


def command_build_schemas(ns):
    """Build XSD and Schematron artifacts using saxonb-xslt."""
    builds = [
        ("vip_spec.xsd", "vip_mainfeed_transform.xsl", "vip_main.xsd"),
        ("vip_spec.xsd", "vip_overlay_transform.xsl", "vip_overlay.xsd"),
        (
            "vip_spec.sch",
            "vip_mainfeed_schematron_transform.xsl",
            "vip_main.sch",
        ),
        (
            "vip_spec.sch",
            "vip_overlay_schematron_transform.xsl",
            "vip_overlay.sch",
        ),
    ]
    for src, xsl, out in builds:
        cmd = [
            "saxonb-xslt",
            f"-s:{src}",
            f"-xsl:{xsl}",
            f"-o:{out}",
        ]
        _log.info("Building %s from %s via %s", out, src, xsl)
        try:
            subprocess.run(cmd, cwd=str(REPO_ROOT), check=True, shell=False)
        except FileNotFoundError:
            _log.error(
                "saxonb-xslt not found on PATH; please install libsaxonb-java."
            )
            sys.exit(1)


def _inject_base_feed_pi(xml_text, base_feed_uri):
    """Insert <?vip-base-feed href="..."?> right after any XML declaration."""
    safe_uri = base_feed_uri.replace('"', "%22").replace("?>", "%3F%3E")
    pi = f'<?vip-base-feed href="{safe_uri}"?>\n'
    bom = "\ufeff" if xml_text.startswith("\ufeff") else ""
    body = xml_text[len(bom) :]
    decl_match = re.match(r"^(\s*<\?xml\b[^?]*\?>\s*)", body)
    if decl_match:
        end = decl_match.end(1)
        return bom + body[:end] + pi + body[end:]
    return bom + pi + body


def command_validate(ns):
    """Validate a VIP main feed or overlay XML against XSD and Schematron."""
    xml_path = Path(ns.xml_file).resolve()
    if not xml_path.is_file():
        _log.error("XML file not found: %s", xml_path)
        sys.exit(1)

    try:
        xml_doc = _parse_xml_safe(xml_path)
    except etree.XMLSyntaxError as exc:
        _log.error("XML syntax error in %s: %s", xml_path, exc)
        sys.exit(1)

    root_tag = etree.QName(xml_doc.getroot()).localname
    if ns.type == "auto":
        if root_tag == "VipObject":
            doc_type = "main"
        elif root_tag == "VipOverlay":
            doc_type = "overlay"
        else:
            _log.error(
                "Could not auto-detect feed type from root element <%s>",
                root_tag,
            )
            sys.exit(1)
    else:
        doc_type = ns.type
        expected_root = "VipObject" if doc_type == "main" else "VipOverlay"
        if root_tag != expected_root:
            _log.error(
                "Root element <%s> does not match --type %s (expected <%s>)",
                root_tag,
                doc_type,
                expected_root,
            )
            sys.exit(1)

    if ns.base_feed and doc_type != "overlay":
        _log.error("--base-feed can only be used when validating a VipOverlay")
        sys.exit(1)

    schema_stem = "vip_main" if doc_type == "main" else "vip_overlay"
    xsd_path = REPO_ROOT / f"{schema_stem}.xsd"
    sch_path = REPO_ROOT / f"{schema_stem}.sch"
    if not xsd_path.is_file() or not sch_path.is_file():
        _log.error(
            "Schema files not found (%s, %s); run 'vip.py build_schemas' first.",
            xsd_path.name,
            sch_path.name,
        )
        sys.exit(1)

    xsd_doc = _parse_xml_safe(xsd_path)
    xsd_schema = etree.XMLSchema(xsd_doc)
    if not xsd_schema.validate(xml_doc):
        _log.error("XSD validation failed against %s:", xsd_path.name)
        for entry in xsd_schema.error_log:
            print(
                f"{xml_path}:{entry.line}:{entry.column}: {entry.message}",
                file=sys.stderr,
            )
        sys.exit(1)

    has_base_pi = bool(
        xml_doc.xpath("/processing-instruction('vip-base-feed')")
    )
    with contextlib.ExitStack() as stack:
        target_xml = xml_path
        if ns.base_feed:
            if has_base_pi:
                _log.warning(
                    "Overriding embedded <?vip-base-feed?> PI with --base-feed %s",
                    ns.base_feed,
                )
            base_path = Path(ns.base_feed).resolve()
            if not base_path.is_file():
                _log.error("Base feed file not found: %s", base_path)
                sys.exit(1)
            doc_encoding = xml_doc.docinfo.encoding or "utf-8"
            tmpdir = stack.enter_context(tempfile.TemporaryDirectory())
            target_xml = Path(tmpdir) / xml_path.name
            original_text = xml_path.read_text(encoding=doc_encoding)
            cleaned_text = re.sub(
                r"<\?vip-base-feed\b.*?\?>\s*", "", original_text, flags=re.S
            )
            target_xml.write_text(
                _inject_base_feed_pi(cleaned_text, base_path.as_uri()),
                encoding=doc_encoding,
            )

        try:
            proc = subprocess.run(
                ["jing", "-p", ns.phase, str(sch_path), str(target_xml)],
                shell=False,
                check=False,
            )
        except FileNotFoundError:
            _log.error("jing not found on PATH; please install jing.")
            sys.exit(1)

    if proc.returncode != 0:
        sys.exit(proc.returncode)

    _log.info(
        "Validation passed (%s, phase=%s): %s",
        doc_type,
        ns.phase,
        xml_path,
    )


def make_subparser(sub, command_name, help, command_func=None, details=None, **kwargs):
    """
    Create the "sub-parser" for our command-line parser.

    This facilitates having multiple "commands" for a single script,
    for example "norm_yaml", "make_rest", etc.
    """
    if command_func is None:
        command_func_name = "command_{0}".format(command_name)
        command_func = globals()[command_func_name]

    # Capitalize the first letter for the long description.
    desc = help[0].upper() + help[1:]
    if details is not None:
        desc += "\n\n{0}".format(details)
    desc = _wrap(desc)
    parser = sub.add_parser(
        command_name,
        formatter_class=FORMATTER_CLASS,
        help=help,
        description=desc,
        **kwargs
    )
    parser.set_defaults(run_command=command_func)
    return parser


def create_parser():
    """
    Create the command-line parser.

    Returns an ArgumentParser object.
    """
    root_parser = argparse.ArgumentParser(
        formatter_class=FORMATTER_CLASS, description=HELP_SUMMARY
    )
    sub = root_parser.add_subparsers(help="sub-command help")

    parser = make_subparser(
        sub,
        "norm_yaml",
        help=(
            "normalize one or more YAML files.  This command does things "
            "like alphabetize the keys in the YAML files, normalize the "
            "spacing, etc."
        ),
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        nargs="?",
        help="a path to a YAML file. Defaults to all files.",
    )

    parser = make_subparser(
        sub, "make_rest", help=("update all reST files from the YAML files.")
    )
    parser.add_argument(
        "type_name",
        metavar="TYPE_NAME",
        nargs="?",
        help=('the name of a type (e.g. "HoursOpen"). ' "Defaults to all types."),
    )

    parser = make_subparser(
        sub,
        "scratch",
        help=(
            "temporary command for development purposes. You can "
            "use / modify this command if you ever need a command for "
            "experimental purposes (e.g. to analyze the contents of "
            "the YAML files)."
        ),
    )

    parser = make_subparser(
        sub,
        "update_timezones",
        help="regenerate iana_timezones.xml from tzdata zoneinfo files.",
    )
    parser.add_argument(
        "--zoneinfo-dir",
        default="/usr/share/zoneinfo",
        help=(
            "path to tzdata zoneinfo directory "
            "(default: /usr/share/zoneinfo)."
        ),
    )
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "iana_timezones.xml"),
        help="output XML path (default: <repo>/iana_timezones.xml).",
    )

    make_subparser(
        sub,
        "build_schemas",
        help=(
            "build vip_main/vip_overlay XSD and Schematron files "
            "via saxonb-xslt."
        ),
    )

    parser = make_subparser(
        sub,
        "validate",
        help="validate a VIP XML feed or overlay against XSD and Schematron.",
    )
    parser.add_argument("xml_file", help="path to the XML file to validate.")
    parser.add_argument(
        "--type",
        choices=("auto", "main", "overlay"),
        default="auto",
        help="document type (default: auto-detect from root element).",
    )
    parser.add_argument(
        "--phase",
        choices=("strict", "full"),
        default="strict",
        help="Schematron validation phase (default: strict).",
    )
    parser.add_argument(
        "--base-feed",
        default=None,
        help=(
            "optional base VipObject XML path for cross-document "
            "overlay checks."
        ),
    )

    return root_parser


def main(argv=None):
    """
    Starting point for the script.

    This is what gets executed when the following is run from the
    repository root:

      $ python <path-to-this-file>

    """
    if argv is None:
        argv = sys.argv[1:]
    logging.basicConfig(
        level="DEBUG", style="{", format="vippy: [{levelname}] {message}"
    )
    common.configure_yaml()
    parser = create_parser()
    ns = parser.parse_args(argv)  # an argparse.Namespace object.
    try:
        ns.run_command
    except AttributeError:
        # We need to handle this exception because of the following
        # behavior change:
        #   http://bugs.python.org/issue16308
        parser.print_help()
    else:
        ns.run_command(ns)


if __name__ == "__main__":
    main()
