"""Audit the installed base zombie against the exact-reference PDX package."""

import hashlib
import json
import re
import wave
from pathlib import Path

from PIL import Image


JOB = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[6]
BASE = JOB / "provider" / "user_selected_exact_20260920"
RUNTIME = REPO / "gfx" / "models" / "units" / "chaosx_zombies"
ROLES = ("idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death")
SOURCE_SHA256 = "7e702c098884d221b000bb6e8764677489e7a4c22d26f6637d8a2e002ab60a43"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def same_file(source, installed):
    if not source.is_file() or not installed.is_file():
        raise FileNotFoundError(source, installed)
    if source.read_bytes() != installed.read_bytes():
        raise ValueError(f"Installed bytes differ from export: {installed}")
    return {"bytes": installed.stat().st_size, "sha256": sha(installed), "runtime": installed.relative_to(REPO).as_posix()}


if sha(JOB / "refs" / "source" / "user_selected_original.png") != SOURCE_SHA256 or sha(JOB / "refs" / "original" / "user_selected_exact_input_20260920.png") != SOURCE_SHA256:
    raise ValueError("The final lineage does not use the selected user image")

files = {"mesh": same_file(BASE / "export" / "mesh" / "chaosx_zombies.mesh", RUNTIME / "chaosx_zombies.mesh")}
if re.search(rb"Image_[0-9]+\.dds", (RUNTIME / "chaosx_zombies.mesh").read_bytes()):
    raise ValueError("Exported mesh still references provider placeholder textures")
for role in ROLES:
    files[f"anim_{role}"] = same_file(BASE / "export" / "anim" / f"chaosx_zombies_{role}.anim", RUNTIME / f"chaosx_zombies_{role}.anim")
for name in ("diffuse_direct", "normal", "specular"):
    filename = f"chaosx_zombies_{name}.dds"
    files[f"texture_{name}"] = same_file(BASE / "textures" / "dds" / filename, RUNTIME / filename)
    if Image.open(RUNTIME / filename).size != (1024, 1024):
        raise ValueError(f"Incorrect DDS dimensions: {filename}")

export = json.loads((BASE / "blender" / "reports" / "exact_reference_pdx_export.json").read_text(encoding="utf-8"))
geometry = export["mesh"]["geometry"]
if any(geometry[key] for key in ("loose_boundary_edges", "non_manifold_edges", "degenerate_faces")):
    raise ValueError(f"Defective source geometry: {geometry}")
if geometry["triangles"] != 30000 or [stream["triangles"] for stream in export["mesh"]["mesh_streams"]] != [20000, 10000]:
    raise ValueError("Wrong PDX stream partition")
comparison = json.loads((BASE / "blender" / "reports" / "exact_reference_export_triangle_comparison.json").read_text(encoding="utf-8"))
if not comparison["equal"] or comparison["source_triangles"] != 30000:
    raise ValueError("Source and actual-byte triangle multisets differ")

gfx = (REPO / "gfx" / "entities" / "chaosx_zombies.gfx").read_text(encoding="utf-8")
entity = (REPO / "gfx" / "entities" / "chaosx_zombies.asset").read_text(encoding="utf-8")
bindings = (RUNTIME / "animation_chaosx_zombies.asset").read_text(encoding="utf-8")
if sorted(int(index) for index in re.findall(r"\bindex\s*=\s*(\d+)", gfx)) != [0, 1]:
    raise ValueError("GFX does not bind both PDX streams")
if not re.search(r"\bscale\s*=\s*0\.8\b", entity):
    raise ValueError("Entity lacks vanilla infantry scale")
for name in ("diffuse_direct", "normal", "specular"):
    if gfx.count(f"chaosx_zombies_{name}.dds") != 2:
        raise ValueError(f"Map missing from one PDX stream: {name}")
for role in ROLES:
    if f'id = "{role}"' not in gfx or f'file = "chaosx_zombies_{role}.anim"' not in bindings:
        raise ValueError(f"Missing role registration: {role}")

audio_asset = (REPO / "sound" / "chaosx_zombies_sound.asset").read_text(encoding="utf-8")
shared_audio = (REPO / "sound" / "chaosx_sound.asset").read_text(encoding="utf-8")
defined = set(re.findall(r'\bname\s*=\s*"(chaosx_[a-z_]+|ZZZ_infantry_idle)"', audio_asset + shared_audio))
used = set(re.findall(r'soundeffect\s*=\s*"([^"]+)"', entity))
if used - defined:
    raise ValueError(f"Undefined zombie entity sound effects: {sorted(used - defined)}")
categories = set()
for body in re.findall(r'category\s*=\s*\{[\s\S]*?soundeffects\s*=\s*\{([^}]*)\}', audio_asset + shared_audio):
    categories.update(re.findall(r'\b(?:chaosx_[a-z_]+|ZZZ_infantry_idle)\b', body))
if used - categories:
    raise ValueError(f"Zombie entity sound effects lack categories: {sorted(used - categories)}")
wave_names = re.findall(r'file\s*=\s*"(002_zombie_outbreak/zombies/[^"]+\.wav)"', audio_asset)
for name in wave_names:
    path = REPO / "sound" / name
    with wave.open(str(path), "rb") as stream:
        if (stream.getnchannels(), stream.getsampwidth(), stream.getframerate()) != (1, 2, 44100):
            raise ValueError(f"Wrong WAV format: {name}")

states = {}
for body in re.split(r"\n\tstate\s*=\s*\{", entity)[1:]:
    found = re.search(r'\bname\s*=\s*"([^"]+)"', body)
    if found:
        states[found.group(1)] = body
durations = {}
for role in ROLES:
    if role not in states:
        raise ValueError(f"Missing state: {role}")
    action = export["animations"][role]
    duration = (action["frame_end"] - action["frame_start"]) / action["fps"]
    cues = [float(value) for value in re.findall(r'event\s*=\s*\{\s*time\s*=\s*([0-9.]+)', states[role])]
    if any(cue < 0 or cue > duration for cue in cues):
        raise ValueError(f"Sound cue outside {role} action: {cues} / {duration}")
    durations[role] = {"fps": action["fps"], "frame_range": [action["frame_start"], action["frame_end"]], "duration_s": duration, "sound_cues_s": cues}
if not re.search(r'\blooping\s*=\s*no[\s\S]*?\bnext_state\s*=\s*"idle"', states["training"]):
    raise ValueError("Training action must return to idle")

icons = {}
for label, path, size in (
    ("large", REPO / "gfx" / "interface" / "counters" / "divisions_large" / "zombies_icon.dds", (152, 42)),
    ("onmap", REPO / "gfx" / "interface" / "counters" / "divisions_small" / "onmap_unit_zombies_icon.dds", (60, 12)),
    ("text", REPO / "gfx" / "texticons" / "unit_zombies_icon_small.dds", (60, 12)),
):
    image = Image.open(path).convert("RGBA")
    if image.size != size or any(image.crop((frame * image.width // 2, 0, (frame + 1) * image.width // 2, image.height)).getbbox() is None for frame in range(2)):
        raise ValueError(f"Missing icon frame: {label}")
    icons[label] = {"sha256": sha(path), "size": list(image.size)}
if Image.open(REPO / "gfx" / "texticons" / "unit_zombies_icon_small.dds").convert("RGBA").tobytes() != Image.open(REPO / "gfx" / "interface" / "counters" / "divisions_small" / "onmap_unit_zombies_icon.dds").convert("RGBA").tobytes():
    raise ValueError("Text and on-map zombie icons differ")

visual = json.loads((BASE / "blender" / "reports" / "exact_reference_actual_byte_visual_review.json").read_text(encoding="utf-8"))
reimport = json.loads((BASE / "blender" / "reports" / "exact_reference_pdx_reimport.json").read_text(encoding="utf-8"))
for role in ROLES:
    record = visual["roles"][role]
    proof = reimport["roles"][role]
    if record["bones"] != 24 or record["triangles"] != 30000 or len(record["frames"]) != 20:
        raise ValueError(f"Incomplete actual-byte visual review: {role}")
    if any(not (JOB / path).is_file() for path in record["frames"]):
        raise FileNotFoundError(f"Missing screenshot for {role}")
    welded = proof["geometry"]["position_welded_topology"]
    if any(welded[key] for key in ("loose_boundary_edges", "non_manifold_edges", "degenerate_faces")):
        raise ValueError(f"Actual-byte topology defect: {role}")

report = {
    "status": "offline_package_verified",
    "source_reference_sha256": SOURCE_SHA256,
    "files": files,
    "geometry": {"vertices": geometry["vertices"], "triangles": geometry["triangles"], "streams": [stream["triangles"] for stream in export["mesh"]["mesh_streams"]], "source_export_triangle_multiset_equal": True},
    "actions": durations,
    "audio": {"wav_declarations": len(wave_names), "entity_effects": sorted(used), "entity_effects_categorized": True, "pcm16_44100_mono": True},
    "icons": icons,
    "actual_byte_reimport": {"roles": len(ROLES), "screenshots": 160, "views_per_phase": ["front", "left", "back", "three_quarter"]},
    "limits": ["No agent-run Hearts of Iron IV playback or live shader/audio validation."],
}
path = Path(__file__).with_name("exact_selected_runtime_audit_20260920.json")
path.write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps({"status": report["status"], "screenshots": 160, "wav_declarations": len(wave_names), "output": str(path)}))
