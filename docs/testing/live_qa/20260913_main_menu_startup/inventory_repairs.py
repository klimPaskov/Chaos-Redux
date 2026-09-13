"""Record task deltas against owner backups without staging existing user drafts."""
from pathlib import Path
import difflib
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parent
ORDER = ["scripts", "camp", "country", "decisions", "focus", "localisation", "models", "parent", "parent_cycle02", "alien_install", "models_embedded", "scripts_held_021", "terrain", "game_rules"]
TEXT = {".txt", ".md", ".gfx", ".gui", ".yml", ".py", ".json", ".toml"}
NEW = [
    "interface/startup_focus_shine.gfx",
    "common/decisions/categories/025_alien_technology_in_antarctica_categories.txt",
    "common/scripted_effects/003_holy_realm_effects.md",
    "common/scripted_effects/030_time_traveler_effects.md",
    "common/script_constants/027_doctrine_research_terrain_states.txt",
    "common/scripted_triggers/027_doctrine_research_terrain_triggers.txt",
    ".tools/3d_pipeline/adapter/identity_leaf_alias.py",
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def logical_lines(data):
    return [line + "\n" for line in data.decode("utf-8-sig").splitlines()]

backups = {}
for owner in ORDER:
    base = RUN / "baseline" / owner
    if not base.exists():
        continue
    for f in base.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(base)
        if owner == "game_rules" and len(rel.parts) == 1:
            rel = Path("common/game_rules") / rel
        backups.setdefault(rel.as_posix(), f)

rows, patches = [], []
for name, before in sorted(backups.items()):
    after = ROOT / name
    old = before.read_bytes()
    new = after.read_bytes() if after.exists() else None
    if new == old:
        continue
    row = {"path": name, "baseline": before.relative_to(ROOT).as_posix(), "before_sha256": digest(old), "after_sha256": digest(new) if new is not None else None, "change": "modified" if new is not None else "removed"}
    rows.append(row)
    if after.suffix in TEXT and new is not None:
        patches.extend(difflib.unified_diff(logical_lines(old), logical_lines(new), fromfile="a/" + name, tofile="b/" + name))

for name in NEW:
    after = ROOT / name
    if not after.exists() or name in backups:
        continue
    new = after.read_bytes()
    rows.append({"path": name, "baseline": None, "before_sha256": None, "after_sha256": digest(new), "change": "added_by_task"})
    patches.extend(difflib.unified_diff([], logical_lines(new), fromfile="/dev/null", tofile="b/" + name))

receipt = json.loads((RUN / "model_evidence/texture_rename_receipt.json").read_text(encoding="utf-8-sig"))
for item in receipt:
    dest = Path(item["new"])
    rows.append({"path": dest.relative_to(ROOT).as_posix(), "renamed_from": Path(item["old"]).relative_to(ROOT).as_posix(), "after_sha256": digest(dest.read_bytes()), "change": "renamed_identical_bytes", "receipt": "model_evidence/texture_rename_receipt.json"})

(RUN / "source_repair_inventory.json").write_text(json.dumps(sorted(rows, key=lambda r: r["path"]), indent=2) + "\n", encoding="utf-8")
(RUN / "source_repairs.patch").write_text("".join(patches), encoding="utf-8")
print(json.dumps({"source_changes": len(rows), "text_patch_bytes": (RUN / "source_repairs.patch").stat().st_size}))
