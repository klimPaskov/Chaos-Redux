"""Reopen the actual zombie PDX mesh with each exported action and collect adapter proofs."""

import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[7]
sys.path.insert(0, str(ROOT / ".tools" / "3d_pipeline"))
from blender_client import BlenderAdapterClient  # noqa: E402


JOB = Path(__file__).resolve().parents[2]
BASE = "provider/user_selected_exact_20260920"
MESH = f"{BASE}/export/mesh/chaosx_zombies.mesh"
REPORT = Path(__file__).parent / "blender" / "reports" / "exact_reference_pdx_reimport.json"
for stem in ("chaosx_zombies_diffuse_direct", "chaosx_zombies_specular", "chaosx_zombies_normal"):
    shutil.copy2(JOB / BASE / "textures" / "dds" / f"{stem}.dds", JOB / BASE / "export" / "mesh" / f"{stem}.dds")
client = BlenderAdapterClient(ROOT)
results = {"mesh": MESH, "roles": {}}
for role in ("idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"):
    result = client.reimport_export(
        "zombies",
        MESH,
        f"{BASE}/export/anim/chaosx_zombies_{role}.anim",
        f"exact_selected_{role}",
    )
    results["roles"][role] = result
    print(json.dumps({"role": role, "proof": result.get("proof_blend"), "mesh": result.get("meshes"), "bones": result.get("armatures")}), flush=True)
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(results, indent=2), encoding="utf-8")
