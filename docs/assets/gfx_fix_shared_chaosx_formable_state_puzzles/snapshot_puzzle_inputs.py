"""Freeze exact runtime masks and local manifest geometry for the assigned puzzle repairs."""

from pathlib import Path
import hashlib
import json
import shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "docs/assets/gfx_fix_shared_chaosx_formable_state_puzzles"
PALETTE_FAMILIES = [
    "form_baltic_federation_category",
    "form_baltic_sea_empire_category",
    "form_north_sea_category",
    "form_scandinavia_category",
    "form_sweden_hungary_category",
]
RING_STATES = {
    "form_north_sea_category": {932: "interface/chaosx_formable_state_puzzle_form_north_sea_empire.gui"},
    "form_scandinavia_category": {910: "interface/chaosx_formable_state_puzzle_form_scandinavia.gui"},
    "GOE_form_hindustan": {
        320: "interface/chaosx_formable_state_puzzle_goe_form_hindustan.gui",
        321: "interface/chaosx_formable_state_puzzle_goe_form_hindustan.gui",
        985: "interface/chaosx_formable_state_puzzle_goe_form_hindustan.gui",
    },
    "unite_maghreb": {783: "interface/chaosx_formable_state_puzzle_unite_maghreb.gui"},
    "proclaim_greater_italy": {116: "interface/chaosx_formable_state_puzzle_proclaim_greater_italy.gui"},
    "unite_latin_africa": {796: "interface/chaosx_formable_state_puzzle_unite_latin_africa.gui"},
}

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_manifest(folder: str) -> tuple[Path, dict]:
    path = ROOT / "docs/formables/state_puzzles" / folder / "manifest.json"
    return path, json.loads(path.read_text(encoding="utf-8-sig"))

for name in ("source_runtime", "source_runtime_png", "source_masks", "contact_sheets", "processed", "candidate_dds", "mosaics"):
    (WORK / name).mkdir(parents=True, exist_ok=True)

palette_assets = []
manifests = {}
for folder in PALETTE_FAMILIES:
    manifest_path, manifest = load_manifest(folder)
    manifests[folder] = manifest
    for asset in manifest.get("assets", []):
        palette_assets.append({
            "family": folder,
            "state_id": asset["state_id"],
            "variant": asset["variant"],
            "runtime_dds": asset["dds"],
            "source_png_declared": asset.get("source_png"),
            "processed_png_declared": asset.get("processed_png"),
            "registered_bbox": asset.get("bbox"),
        })

ring_states = []
for folder, state_gui_map in RING_STATES.items():
    _, manifest = load_manifest(folder)
    if manifest.get("assets"):
        for state_id, gui_path in state_gui_map.items():
            pair = {a["variant"]: a for a in manifest["assets"] if a["state_id"] == state_id}
            if set(pair) != {"unresolved", "qualifying"}:
                raise RuntimeError(f"missing status pair: {folder} state {state_id}")
            position = pair["unresolved"].get("bbox", [None, None])[:2]
            ring_states.append({
                "family": folder,
                "state_id": state_id,
                "gui_file": gui_path,
                "old_gui_position": position,
                "old_size": None,
                "declared_mask_pixel_count": None,
                "source_mask_sha256": None,
                "runtime_dds": {variant: pair[variant]["dds"] for variant in pair},
                "position_source": "manifest bbox matches registered iconType top-left",
            })
    else:
        states = {s["state_id"]: s for s in manifest.get("states", [])}
        for state_id, gui_path in state_gui_map.items():
            state = states.get(state_id)
            if state is None:
                raise RuntimeError(f"missing state record: {folder} state {state_id}")
            position = state.get("position")
            if isinstance(position, dict):
                position = [position["x"], position["y"]]
            if position is None:
                position = state.get("canvas_position", state.get("projection_position"))
            ring_states.append({
                "family": folder,
                "state_id": state_id,
                "gui_file": gui_path,
                "old_gui_position": position,
                "old_size": state.get("projected_mask_size"),
                "declared_mask_pixel_count": state.get("geometry", {}).get("mask_pixel_count"),
                "source_mask_sha256": state.get("source_mask_sha256"),
                "runtime_dds": state["runtime_dds"],
                "position_source": "manifest position/projection_position",
            })

# Freeze every assigned palette asset and every distinct tiny island-marker asset.
targets = {}
for item in palette_assets:
    targets[item["runtime_dds"]] = {
        "family": item["family"], "state_id": item["state_id"],
        "variant": item["variant"], "palette_repair": True,
    }
for marker in ring_states:
    for variant, path in marker["runtime_dds"].items():
        targets.setdefault(path, {
            "family": marker["family"], "state_id": marker["state_id"],
            "variant": variant, "palette_repair": marker["family"] in PALETTE_FAMILIES,
        })

assets = []
pairs = {}
for runtime_path, meta in sorted(targets.items()):
    runtime = ROOT / runtime_path
    if not runtime.is_file():
        raise FileNotFoundError(runtime)
    relative = Path(runtime_path)
    before = WORK / "source_runtime" / relative
    before.parent.mkdir(parents=True, exist_ok=True)
    current_hash = sha(runtime)
    if before.exists():
        if sha(before) != current_hash:
            raise RuntimeError(f"refusing to overwrite changed source snapshot: {before}")
    else:
        shutil.copyfile(runtime, before)
    before_png = WORK / "source_runtime_png" / relative.with_suffix(".png")
    before_png.parent.mkdir(parents=True, exist_ok=True)
    if not before_png.exists():
        Image.open(before).convert("RGBA").save(before_png)
    image = Image.open(before_png).convert("RGBA")
    alpha = image.getchannel("A")
    core_mask = alpha.point(lambda value: 255 if value > 0 else 0)
    mask_dir = WORK / "source_masks" / meta["family"]
    mask_dir.mkdir(parents=True, exist_ok=True)
    mask_path = mask_dir / f"state_{meta['state_id']}_alpha_nonzero_mask.png"
    if mask_path.exists():
        if sha(mask_path) != sha(Path(before_png)):
            # Existing files are one-channel mask PNGs, so compare their pixels below.
            if Image.open(mask_path).convert("L").tobytes() != core_mask.tobytes():
                raise RuntimeError(f"refusing to overwrite changed core mask: {mask_path}")
    else:
        core_mask.save(mask_path)
    item = {
        **meta,
        "runtime_dds": runtime_path,
        "before_snapshot": str(before.relative_to(ROOT)).replace("\\", "/"),
        "before_sha256": sha(before),
        "before_png": str(before_png.relative_to(ROOT)).replace("\\", "/"),
        "before_png_sha256": sha(before_png),
        "canvas_size": image.size,
        "alpha_bbox": alpha.getbbox(),
        "opaque_pixel_count_alpha255": sum(1 for value in alpha.getdata() if value == 255),
        "visible_pixel_count_alpha_gt0": sum(1 for value in alpha.getdata() if value > 0),
        "core_mask_path": str(mask_path.relative_to(ROOT)).replace("\\", "/"),
        "core_mask_sha256": sha(mask_path),
    }
    assets.append(item)
    pairs.setdefault((meta["family"], meta["state_id"]), {})[meta["variant"]] = item

# Require identical binary geometry for every unresolved/qualifying pair.
pair_checks = []
for (family, state_id), variants in pairs.items():
    if set(variants) != {"unresolved", "qualifying"}:
        raise RuntimeError(f"incomplete status pair: {family} state {state_id}")
    unresolved = Image.open(ROOT / variants["unresolved"]["before_png"]).convert("RGBA")
    qualifying = Image.open(ROOT / variants["qualifying"]["before_png"]).convert("RGBA")
    alpha_u = unresolved.getchannel("A")
    alpha_q = qualifying.getchannel("A")
    mask_u = alpha_u.point(lambda value: 255 if value > 0 else 0)
    mask_q = alpha_q.point(lambda value: 255 if value > 0 else 0)
    if unresolved.size != qualifying.size or mask_u.tobytes() != mask_q.tobytes():
        raise RuntimeError(f"before binary masks differ: {family} state {state_id}")
    pair_checks.append({
        "family": family,
        "state_id": state_id,
        "canvas": unresolved.size,
        "binary_core_mask_equal": True,
        "opaque_pixel_count_alpha255": sum(1 for value in alpha_u.getdata() if value == 255),
        "visible_pixel_count_alpha_gt0": sum(1 for value in alpha_u.getdata() if value > 0),
    })

# Ring canvases are odd/even padded to keep the original state-mask center exact.
ring_plan = []
for item in ring_states:
    pair = pairs[(item["family"], item["state_id"])]
    old_w, old_h = pair["unresolved"]["canvas_size"]
    # A 12px ring needs a 1px transparent breathing edge. Keep the expanded
    # canvas parity aligned with the old canvas so the exact state-mask center
    # can be held with integer GUI position offsets.
    new_w, new_h = max(15, old_w), max(15, old_h)
    if (new_w - old_w) % 2:
        new_w += 1
    if (new_h - old_h) % 2:
        new_h += 1
    pad_x, pad_y = (new_w - old_w) // 2, (new_h - old_h) // 2
    old_x, old_y = item["old_gui_position"]
    ring_plan.append({
        **item,
        "old_canvas": [old_w, old_h],
        "new_canvas": [new_w, new_h],
        "core_padding": [pad_x, pad_y],
        "new_gui_position": [old_x - pad_x, old_y - pad_y],
        "ring_diameter_px": 12,
        "parent_gui_edit_required": pad_x > 0 or pad_y > 0,
    })

inventory = {
    "palette_families": PALETTE_FAMILIES,
    "palette_asset_count": len(palette_assets),
    "unique_runtime_asset_count": len(assets),
    "island_ring_states": ring_plan,
    "geometry_policy": "Runtime-recovered exact mask; no province boundaries are invented or edited.",
    "pair_checks": pair_checks,
    "parent_generator_palette_source": ".tools/repair_event6_state_puzzle_assets.py::process_state",
    "assets": assets,
}
output = WORK / "input_inventory_v2.json"
output.write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
print("palette assets:", len(palette_assets))
print("unique runtime assets:", len(assets))
print("paired states with exact binary masks:", len(pair_checks))
print("marker states:", len(ring_plan))
print("inventory:", output.relative_to(ROOT), sha(output))
for item in ring_plan:
    print(item["family"], item["state_id"], "old", item["old_canvas"], "new", item["new_canvas"], "pad", item["core_padding"], "GUI", item["old_gui_position"], "->", item["new_gui_position"], "mask pixels", item["declared_mask_pixel_count"])
