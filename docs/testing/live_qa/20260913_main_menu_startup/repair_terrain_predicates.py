"""Replace invalid state terrain predicates using exact inherited map membership."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parent
GAME = Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")
assert not (ROOT / "history/states").exists()
assert not (ROOT / "map/definition.csv").exists()
assert not (ROOT / "map/default.map").exists()
assert not re.search(r'replace_path\s*=\s*"(?:history/states|map)"', (ROOT / "descriptor.mod").read_text())

def sha(data):
    return hashlib.sha256(data).hexdigest()

definitions = GAME / "map/definition.csv"
definition_bytes = definitions.read_bytes()
terrain_by_province = {}
for row in definition_bytes.decode("utf-8-sig").splitlines():
    fields = row.split(";")
    if len(fields) > 6 and fields[0].isdigit():
        terrain_by_province[int(fields[0])] = fields[6].strip()

groups = {k: [] for k in ("forest", "mountain", "plains")}
memberships, source_rows = {}, []
state_files = sorted((GAME / "history/states").glob("*.txt"), key=lambda f: f.name.lower())
for f in state_files:
    data = f.read_bytes()
    source_rows.append(f.name.lower() + ":" + sha(data) + "\n")
    text = re.sub(r"#.*", "", data.decode("utf-8-sig"))
    state_id = int(re.search(r"\bid\s*=\s*(\d+)", text)[1])
    assert int(re.match(r"\d+", f.name)[0]) == state_id, f
    block = re.search(r"\bprovinces\s*=\s*\{([^{}]*)\}", text)[1]
    provinces = [int(p) for p in re.findall(r"\d+", block)]
    for p in provinces:
        assert p in terrain_by_province and p not in memberships, (f, p)
        memberships[p] = state_id
    present = {terrain_by_province[p] for p in provinces}
    for terrain in groups:
        if terrain in present:
            groups[terrain].append(state_id)
groups = {k: sorted(v) for k, v in groups.items()}
assert len(state_files) == 1081 and len(terrain_by_province) == 13414 and len(memberships) == 10272
assert {k: len(v) for k, v in groups.items()} == {"forest": 454, "mountain": 459, "plains": 675}
assert sha(definition_bytes) == "86846be71198d6772c651638aa22e3656133198de9b7c49c6234ed48cf33d87b"
provenance = {"definition_sha256": sha(definition_bytes), "state_file_manifest_sha256": sha("".join(source_rows).encode()), "state_files": len(state_files), "definition_rows": len(terrain_by_province), "state_province_memberships": len(memberships), "state_overrides": 0, "definition_override": False, "default_map_override": False, "groups": groups}
(RUN / "startup_terrain_state_sets.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

constants = "# Event 027 terrain membership derived from the inherited province and state map.\n# Regenerate and review these arrays whenever province terrain or state membership changes.\n# Source and derivation: docs/testing/live_qa/20260913_main_menu_startup/startup_terrain_state_sets.json\n\ndoctrine_research_terrain_states = {\n\tschema = {\n\t\tany_key = yes\n\t\tarray = state\n\t}\n"
for terrain, states in groups.items():
    constants += "\t" + terrain + " = {\n"
    for start in range(0, len(states), 20):
        constants += "\t\t" + " ".join(map(str, states[start:start + 20])) + "\n"
    constants += "\t}\n"
constants += "}\n"
constant_path = ROOT / "common/script_constants/027_doctrine_research_terrain_states.txt"
trigger_path = ROOT / "common/scripted_triggers/027_doctrine_research_terrain_triggers.txt"
assert not constant_path.exists() and not trigger_path.exists()
triggers = "# Event 027 country geography predicates.\n# Input: current country scope. Output: whether a controlled state contains the named terrain.\n# PREV inside any_state_of is the calling country, preserving nested-country calls.\n# State sets are centralized map-derived script constants, not AI tuning values.\n\n"
for terrain in groups:
    triggers += f"doctrine_research_controls_state_with_{terrain} = {{\n\tany_state_of = {{\n\t\ttarget = constant:doctrine_research_terrain_states.{terrain}\n\t\tis_controlled_by = PREV\n\t}}\n}}\n\n"

files = ["common/scripted_effects/027_doctrine_research_ai_effects.txt", "common/scripted_effects/027_doctrine_research_effects.txt"]
receipt = []
for name in files:
    path = ROOT / name
    old = path.read_bytes()
    backup = RUN / "baseline/terrain" / name
    backup.parent.mkdir(parents=True, exist_ok=True)
    assert not backup.exists()
    backup.write_bytes(old)
    changes = []
    def replace(match):
        terrain = match[1].decode()
        actual = "mountain" if terrain == "mountains" else terrain
        changes.append(actual)
        return ("doctrine_research_controls_state_with_" + actual + " = yes").encode()
    new = re.sub(rb"any_controlled_state\s*=\s*\{\s*has_terrain\s*=\s*(forest|mountains|plains)\s*\}", replace, old)
    assert len(changes) == (2 if "_ai_" in name else 3), (name, changes)
    path.write_bytes(new)
    receipt.append({"path": name, "before_sha256": sha(old), "after_sha256": sha(new), "replaced_predicates": changes})
constant_path.write_text(constants, encoding="utf-8")
trigger_path.write_text(triggers, encoding="utf-8")
(RUN / "startup_terrain_repair_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"state_counts": {k: len(v) for k, v in groups.items()}, "replaced_predicates": sum(len(r["replaced_predicates"]) for r in receipt), "state_file_manifest_sha256": provenance["state_file_manifest_sha256"]}))
