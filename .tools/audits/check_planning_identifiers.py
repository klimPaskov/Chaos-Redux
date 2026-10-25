"""Check planning reservations against runtime identities and the catalog.

Run from any directory with Python 3.9+; this command is read-only.
It checks the declared ledger, not arbitrary identifiers mentioned in prose.
"""

import collections
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOKEN = re.compile(r'#[^\r\n]*|"(?:\\.|[^"\\])*"|[A-Za-z0-9_:.@-]+|[{}=]')
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def tokens(text):
    return [m for m in TOKEN.finditer(text) if not m.group().startswith("#")]


def numeric_block(path, name):
    text = (ROOT / path).read_text(encoding="utf-8-sig")
    start = re.search(r"^" + re.escape(name) + r"\s*=\s*\{", text, re.M)
    if not start:
        raise ValueError(f"Missing constant category {name} in {path}")
    depth = 1
    end = None
    for token in tokens(text[start.end():]):
        if token.group() == "{":
            depth += 1
        elif token.group() == "}":
            depth -= 1
            if depth == 0:
                end = start.end() + token.start()
                break
    if end is None:
        raise ValueError(f"Unclosed constant category {name}")
    pairs = re.findall(r"^\s*([a-z][a-z0-9_]*)\s*=\s*(\d+)\s*$", text[start.end():end], re.M)
    if len(pairs) != len({key for key, _ in pairs}):
        raise ValueError(f"Repeated constant key in {name}")
    return {key: int(value) for key, value in pairs}


def event_definitions():
    found = collections.defaultdict(list)
    event_types = {"country_event", "news_event", "state_event", "unit_leader_event", "operative_leader_event"}
    for path in sorted((ROOT / "events").rglob("*.txt")):
        text = path.read_text(encoding="utf-8-sig")
        parsed = tokens(text)
        depth = 0
        current = False
        for i, token in enumerate(parsed):
            value = token.group()
            if depth == 0 and value in event_types and [m.group() for m in parsed[i + 1:i + 3]] == ["=", "{"]:
                current = True
            if current and depth == 1 and value == "id" and i + 2 < len(parsed) and parsed[i + 1].group() == "=":
                identifier = parsed[i + 2].group().strip('"')
                numeric = re.fullmatch(r"(.+)\.([0-9]+)", identifier)
                if numeric:
                    identifier = f"{numeric.group(1)}.{int(numeric.group(2))}"
                line = text.count("\n", 0, token.start()) + 1
                found[identifier].append(f"{path.relative_to(ROOT).as_posix()}:{line}")
            if value == "{":
                depth += 1
            elif value == "}":
                depth -= 1
                if depth == 0:
                    current = False
    return found


def workbook_sheet_rows(name):
    path = ROOT / "docs/spreadsheets/chaos_redux_events_catalog.xlsx"
    with zipfile.ZipFile(path) as archive:
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in relationships}
        sheet = next(s for s in workbook.find("m:sheets", NS) if s.attrib["name"] == name)
        relation = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
        target = targets[relation]
        target = target.lstrip("/") if target.startswith("/") else "xl/" + target
        shared = []
        if "xl/sharedStrings.xml" in archive.namelist():
            for item in ET.fromstring(archive.read("xl/sharedStrings.xml")):
                shared.append("".join(item.itertext()))
        rows = []
        for row in ET.fromstring(archive.read(target)).findall("m:sheetData/m:row", NS):
            values = {}
            for cell in row.findall("m:c", NS):
                column = re.match(r"[A-Z]+", cell.attrib["r"]).group()
                raw = cell.findtext("m:v", default="", namespaces=NS)
                kind = cell.attrib.get("t")
                if kind == "s":
                    value = shared[int(raw)]
                elif kind == "inlineStr":
                    value = "".join(t.text or "" for t in cell.findall("m:is//m:t", NS))
                else:
                    value = raw
                values[column] = value
            rows.append(values)
        return rows


def main():
    registry = json.loads((ROOT / "docs/specs/shared_identifier_registry.json").read_text(encoding="utf-8"))
    errors = []
    counts = {}
    bindings = [
        ("triggerable_scenarios", "common/script_constants/chaosx_triggerable_scenarios_constants.txt", "triggerable_scenario_id", "runtime_key"),
        ("cluster_identifiers", "common/script_constants/event_cluster_constants.txt", "event_cluster_id", "key"),
        ("world_end_scenarios", "common/script_constants/world_end_scenario_registry_constants.txt", "world_end_scenario_id", "key"),
    ]
    for family, source, category, key_field in bindings:
        rows = registry[family]
        by_id = {row["id"]: row for row in rows}
        if len(by_id) != len(rows):
            errors.append(f"Duplicate reserved numeric ID in {family}")
        live = numeric_block(source, category)
        if len(set(live.values())) != len(live):
            errors.append(f"Duplicate runtime numeric ID in {category}")
        for key, value in live.items():
            row = by_id.get(value)
            if row is None or row.get(key_field) != key:
                errors.append(f"{category}.{key}={value} conflicts with or is absent from the ledger")
        for row in rows:
            if row["state"].startswith("implemented") and live.get(row.get(key_field)) != row["id"]:
                errors.append(f"Missing runtime identity for {family}: {row}")
        counts[family] = {"registered_or_reserved": len(rows), "runtime_constants": len(live)}

    for row in registry["triggerable_scenarios"]:
        if row["label"] != f"SCN-{row['id']:03d}":
            errors.append(f"Mismatched SCN label: {row['label']}")
        if row["state"] == "reserved_proposed_design":
            paths = [ROOT / re.split(r":\d", item, maxsplit=1)[0] for item in row["evidence"]]
            if not any(p.is_file() and row["label"] in p.read_text(encoding="utf-8-sig") for p in paths):
                errors.append(f"{row['label']} is missing from its declared package evidence")

    presentations = registry.get("super_event_reservations", [])
    if len({row["id"] for row in presentations}) != len(presentations):
        errors.append("Duplicate reserved super-event presentation slot")
    if presentations:
        selector = (ROOT / "common/scripted_localisation/chaosx_scripted_localisation_super_events.txt").read_text(encoding="utf-8-sig")
        occupied = set()
        constants = {}
        for token in set(re.findall(r"flag\s*=\s*super_event_visible\s+value\s*=\s*([^\s}]+)", selector)):
            if token.isdecimal():
                occupied.add(int(token))
                continue
            match = re.fullmatch(r"constant:([a-z0-9_]+)\.([a-z0-9_]+)", token)
            if not match:
                errors.append(f"Unresolved super-event selector identity: {token}")
                continue
            category, key = match.groups()
            if category not in constants:
                values = []
                for path in (ROOT / "common/script_constants").glob("*.txt"):
                    if re.search(r"^" + re.escape(category) + r"\s*=\s*\{", path.read_text(encoding="utf-8-sig"), re.M):
                        values.append(numeric_block(path.relative_to(ROOT), category))
                constants[category] = values
            candidates = [values[key] for values in constants[category] if key in values]
            if len(set(candidates)) != 1:
                errors.append(f"Unresolved or ambiguous super-event constant: {token}")
            else:
                occupied.add(candidates[0])
        for path in (ROOT / "localisation/english").rglob("*.yml"):
            occupied.update(int(value) for value in re.findall(r"^\s*chaosx_super_event\.(\d+)\.[tdqa]\s*:", path.read_text(encoding="utf-8-sig"), re.M))
        for row in presentations:
            if row["state"] == "reserved_proposed_design" and row["id"] in occupied:
                errors.append(f"Reserved super-event slot {row['id']} already has a runtime selector or text identity")
        counts["super_event_presentations"] = {"planning_reservations": len(presentations), "occupied_selector_or_text_slots": len(occupied)}

    events = event_definitions()
    for identifier, locations in events.items():
        if len(locations) > 1:
            errors.append(f"Duplicate event definition {identifier}: {locations}")
    counts["event_definitions"] = sum(len(v) for v in events.values())
    tags = collections.defaultdict(list)
    for path in (ROOT / "common/country_tags").rglob("*.txt"):
        for match in re.finditer(r'^\s*([A-Z0-9]{3})\s*=\s*"', path.read_text(encoding="utf-8-sig"), re.M):
            tags[match.group(1)].append(path.relative_to(ROOT).as_posix())
    for tag, paths in tags.items():
        if len(paths) > 1:
            errors.append(f"Duplicate country tag {tag}: {paths}")
    counts["runtime_country_tags"] = len(tags)

    rows = workbook_sheet_rows("Clusters")
    headers = rows[0]
    id_column = next(k for k, v in headers.items() if v.strip().lower() == "cluster id")
    name_column = next(k for k, v in headers.items() if v.strip().lower() in {"name", "cluster name"})
    cluster_rows = {r["id"]: r for r in registry["cluster_identifiers"]}
    seen = set()
    for row in rows[1:]:
        if not row.get(id_column):
            continue
        value = int(row[id_column])
        if value in seen:
            errors.append(f"Duplicate workbook cluster ID {value}")
        seen.add(value)
        entry = cluster_rows.get(value)
        if entry is None or entry["name"].casefold() != row[name_column].strip().casefold():
            errors.append(f"Workbook cluster {value} ({row[name_column]}) conflicts with ledger")
    counts["catalog_cluster_rows"] = len(seen)
    result = {"passed": not errors, "counts": counts, "errors": errors,
              "scope": "Declared numeric reservations, their package evidence, runtime event definitions and country tags, canonical workbook cluster identities, and reserved super-event slots against literal/constant selectors and text identities. Audio IDs, historical prose and undeclared future identifiers are not inferred as presentation-slot definitions."}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
