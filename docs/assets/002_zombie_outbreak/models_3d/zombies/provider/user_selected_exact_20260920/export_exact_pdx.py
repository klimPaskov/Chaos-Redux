"""Export the exact-reference zombie mesh and eight reviewed actions through io_pdx_mesh."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[7]
sys.path.insert(0, str(ROOT / ".tools" / "3d_pipeline"))
from blender_client import BlenderAdapterClient  # noqa: E402


BASE = "provider/user_selected_exact_20260920"
BLEND = f"{BASE}/blender/checkpoints/56_exact_reference_final_grounded.blend"
REPORT = Path(__file__).parent / "blender" / "reports" / "exact_reference_pdx_export.json"
client = BlenderAdapterClient(ROOT)
results = {"source_blend": BLEND}
results["mesh"] = client.call(
    "chaosx_blender_hoi4_export_mesh",
    {
        "job_id": "zombies",
        "blend_rel": BLEND,
        "output_rel": f"{BASE}/export/mesh/chaosx_zombies.mesh",
        "checkpoint_rel": f"{BASE}/blender/checkpoints/57_exact_reference_exported.blend",
        "split_verts": False,
    },
)
print(json.dumps({"mesh": results["mesh"]}), flush=True)
results["animations"] = {}
for role in ("idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"):
    result = client.export_animation(
        "zombies",
        BLEND,
        f"zombies_{role}_exact_final",
        f"{BASE}/export/anim/chaosx_zombies_{role}.anim",
    )
    results["animations"][role] = result
    print(json.dumps({"role": role, "result": result}), flush=True)
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(results, indent=2), encoding="utf-8")
