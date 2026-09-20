"""Compare every source triangle with the reimported actual PDX mesh bytes."""

import bpy
import collections
import json
import sys
from pathlib import Path


source, proof, output = (Path(path) for path in sys.argv[sys.argv.index("--") + 1:])
records = {}
for label, blend in (("source", source), ("reimport", proof)):
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    obj = next(obj for obj in bpy.context.scene.objects if obj.type == "MESH")
    mesh = obj.data
    positions = [tuple(round(float(value), 5) for value in obj.matrix_world @ vertex.co) for vertex in mesh.vertices]
    keys = []
    for face in mesh.polygons:
        if len(face.vertices) != 3:
            raise ValueError("Triangle comparison requires triangles")
        keys.append(tuple(sorted(positions[index] for index in face.vertices)))
    records[label] = collections.Counter(keys)
missing = records["source"] - records["reimport"]
added = records["reimport"] - records["source"]
report = {
    "source": str(source),
    "proof": str(proof),
    "source_triangles": sum(records["source"].values()),
    "reimport_triangles": sum(records["reimport"].values()),
    "missing_triangles": sum(missing.values()),
    "added_triangles": sum(added.values()),
    "equal": not missing and not added,
}
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report), flush=True)
if not report["equal"]:
    raise ValueError("PDX export changed the source triangle multiset")
