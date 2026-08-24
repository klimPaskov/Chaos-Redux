"""Read-only real-checkpoint regression for saved-normalization convergence."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

import bpy


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-blend", required=True)
    parser.add_argument("--target-height", required=True, type=float)
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else [])
    source = Path(args.source_blend).resolve()
    if not source.is_file() or source.suffix.casefold() != ".blend":
        raise ValueError("source-blend must be an existing Blender checkpoint.")
    with tempfile.TemporaryDirectory(prefix="chaosx_saved_normalization_") as temporary:
        checkpoint = Path(temporary) / "candidate.blend"
        shutil.copy2(source, checkpoint)
        proof = blender_worker.stabilize_saved_normalization(checkpoint, args.target_height)
        bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
        reopened = blender_worker.geometry_metrics()
        print(
            json.dumps(
                {
                    "status": "pass",
                    "source_read_only": str(source),
                    "target_height_m": args.target_height,
                    "persisted_height_m": reopened["dimensions"][2],
                    "corrections": proof["dependency_graph_corrections"],
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
