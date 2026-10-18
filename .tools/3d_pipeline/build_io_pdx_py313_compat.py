"""Build the reproducible Python 3.13 compatibility archive for io_pdx_mesh 0.91.

Blender 5.2 uses Python 3.13, which removed ``imp``, removed the old
``Material.shadow_method`` property, and no longer accepts a positional context
dictionary for operators. Keep the upstream 0.91 archive intact and change only
those compatibility sites in a separate locked archive.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
LOCK = json.loads((ROOT / "config/dependencies.lock.json").read_text(encoding="utf-8"))
SOURCE = ROOT / "vendor/io_pdx_mesh/blender-io_pdx_mesh.zip"
OUTPUT = ROOT / "vendor/io_pdx_mesh/blender-io_pdx_mesh-0.91-py313.zip"
PATCHES = {
    "io_pdx_mesh/__init__.py": [
        (
            b"from imp import reload",
            b"from importlib import reload",
        ),
    ],
    "io_pdx_mesh/pdx_maya/maya_ui.py": [
        (
            b"from imp import reload",
            b"from importlib import reload",
        ),
    ],
    "io_pdx_mesh/pdx_blender/blender_import_export.py": [
        (
            b'    new_shader.shadow_method = "CLIP"',
            b'    if hasattr(new_shader, "shadow_method"):\n'
            b'        new_shader.shadow_method = "CLIP"',
        ),
        # Multi-stream meshes join their created objects; Blender 4+ rejects the
        # positional context dictionary, so pass the same members to temp_override.
        (
            b'                ctx = bpy.context.copy()\n'
            b'                ctx["active_object"] = created[0]\n'
            b'                ctx["selected_editable_objects"] = created\n'
            b'                bpy.ops.object.join(ctx)\n'
            b'                ctx.clear()',
            b'                with bpy.context.temp_override(\n'
            b'                    active_object=created[0],\n'
            b'                    object=created[0],\n'
            b'                    selected_objects=created,\n'
            b'                    selected_editable_objects=created,\n'
            b'                ):\n'
            b'                    bpy.ops.object.join()',
        ),
    ],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    expected = LOCK["routes"]["io_pdx_mesh"]["sha256"].upper()
    if sha256(SOURCE) != expected:
        raise RuntimeError("The upstream io_pdx_mesh archive differs from the dependency lock")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    with ZipFile(SOURCE) as original, ZipFile(OUTPUT, "w") as patched:
        for entry in original.infolist():
            data = original.read(entry.filename)
            if entry.filename in PATCHES:
                for old, new in PATCHES[entry.filename]:
                    old = old.replace(b"\n", b"\r\n") if b"\r\n" in data and old not in data else old
                    new = new.replace(b"\n", b"\r\n") if b"\r\n" in data and b"\r\n" in old else new
                    if data.count(old) != 1:
                        raise RuntimeError(f"Unexpected compatibility anchor in {entry.filename}")
                    data = data.replace(old, new)
                seen.add(entry.filename)
            patched.writestr(entry, data)
    if seen != PATCHES.keys():
        OUTPUT.unlink(missing_ok=True)
        raise RuntimeError(f"Missing io_pdx_mesh patch targets: {sorted(PATCHES.keys() - seen)}")
    print(f"{OUTPUT}: {sha256(OUTPUT)}")


if __name__ == "__main__":
    main()
