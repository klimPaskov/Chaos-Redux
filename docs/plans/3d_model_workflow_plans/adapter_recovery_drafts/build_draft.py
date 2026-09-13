from pathlib import Path
import ast
import difflib
import hashlib
import json

root = Path(__file__).resolve().parent
repo = root.parents[3]
base = repo / '.tools/3d_pipeline/adapter'
changes = {}
def patch(filename, old, new):
    text = changes.setdefault(filename, (base / filename).read_text(encoding='utf-8-sig'))
    if text.count(old) != 1 and old.startswith('    output.parent.mkdir'):
        start=text.index('def export_mesh('); end=text.index('\ndef select_armature_and_action',start)
        portion=text[start:end]
        assert portion.count(old)==1
        changes[filename]=text[:start]+portion.replace(old,new)+text[end:]
        return
    if text.count(old) != 1:
        raise ValueError((filename, old[:100], text.count(old)))
    changes[filename] = text.replace(old, new)

patch('blender_worker.py', 'not 1 <= len(mesh_names) <= 16:', 'not 1 <= len(mesh_names) <= 512:')
patch('blender_worker.py', 'Promotion requires one to sixteen exact mesh names.', 'Promotion requires one to 512 exact mesh names from the complete same-rig receipt.')
patch('chaosx_blender_hoi4_mcp.py', 'one exact rig and 1-16 exact meshes', 'one exact rig and 1-512 exact meshes')
patch('blender_worker.py', '    exported_checkpoint = job / "blender" / "checkpoints" / "06_exported.blend"\n    save_blend(exported_checkpoint)', '    save_blend(exported_checkpoint)')
patch('blender_worker.py', '    output.parent.mkdir(parents=True, exist_ok=True)\n    bpy.ops.wm.open_mainfile(filepath=str(blend))\n    pdx = load_pdx(req["io_pdx_root"])', '''    explicit_checkpoint = payload.get("checkpoint_rel")
    exported_checkpoint = within(job, explicit_checkpoint, allow_missing=True) if explicit_checkpoint else job / "blender" / "checkpoints" / "06_exported.blend"
    if explicit_checkpoint and (exported_checkpoint.suffix != ".blend" or exported_checkpoint.parent != blend.parent or exported_checkpoint == blend or exported_checkpoint.exists()):
        raise ValueError("Explicit export checkpoint must be a new sibling .blend; overwrite is forbidden.")
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend), use_scripts=False)
    pdx = load_pdx(req["io_pdx_root"])''')
patch('chaosx_blender_hoi4_mcp.py', '''def chaosx_blender_hoi4_export_mesh(
    job_id: str,
    blend_rel: str,
    output_rel: str,
    split_verts: bool = False,
)''', '''def chaosx_blender_hoi4_export_mesh(
    job_id: str,
    blend_rel: str,
    output_rel: str,
    split_verts: bool = False,
    checkpoint_rel: str | None = None,
)''')
patch('chaosx_blender_hoi4_mcp.py', '{"blend_rel": blend_rel, "output_rel": output_rel, "split_verts": split_verts},', '{"blend_rel": blend_rel, "output_rel": output_rel, "split_verts": split_verts, "checkpoint_rel": checkpoint_rel},')

# Preserve metadata-only promotion invariants. Resolve an empty working
# collection only inside explicitly hash-bound manual repair operations.
patch('manual_creature_rig.py', '\ndef _mesh_signature(objects):', '''
def _repair_collection(h):
    bpy = h["bpy"]
    objects = h["mesh_objects"]() + h["armatures"]()
    if not objects or any(not obj.get("chaosx_working") or obj.library or obj.data.library or obj.get("chaosx_source_protected") or obj.get("chaosx_reference_read_only") for obj in objects):
        raise ValueError("Require explicitly approved local working objects.")
    collection = bpy.data.collections.get("WORKING")
    if collection is None:
        collection = bpy.data.collections.new("WORKING")
        bpy.context.scene.collection.children.link(collection)
    elif collection.library or collection.get("chaosx_source_protected") or collection.get("chaosx_reference_read_only"):
        raise ValueError("Working collection is protected or linked.")
    if collection.name not in {c.name for c in bpy.context.scene.collection.children_recursive}:
        raise ValueError("Working collection does not belong to the active scene.")
    return collection


def _mesh_signature(objects):''')
for old in ['h["_working_collection"]().objects.link(rig)', 'h["_working_collection"]().objects.link(obj)']:
    patch('manual_creature_rig.py', old, old.replace('h["_working_collection"]()', '_repair_collection(h)'))
patch('manual_creature_rig.py', 'set(row) != {"name", "min", "max", "bones", "rigid"}', 'set(row) - {"name", "min", "max", "bones", "rigid", "mesh_names"} or not {"name", "min", "max", "bones", "rigid"} <= set(row)')
patch('manual_creature_rig.py', '        lo, hi = vector(row["min"]), vector(row["max"])', '''        if "mesh_names" in row:
            names=row["mesh_names"]
            if not isinstance(names,list) or not 1<=len(names)<=512 or len(set(names))!=len(names):
                raise ValueError("Region mesh_names requires 1-512 exact unique object names.")
            for n in names: name(n)
        lo, hi = vector(row["min"]), vector(row["max"])''')
patch('manual_creature_rig.py', '    before_geometry = h["geometry_metrics"]()', '''    if any(set(r.get("mesh_names",[]))-{obj.name for obj in meshes} for r in spec["weight_regions"]):
        raise ValueError("Weight region targets an unknown working mesh.")
    before_geometry = h["geometry_metrics"]()''')
patch('manual_creature_rig.py', 'if all(r["min"][i]<=point[i]<=r["max"][i] for i in range(3))', 'if ("mesh_names" not in r or obj.name in r["mesh_names"]) and all(r["min"][i]<=point[i]<=r["max"][i] for i in range(3))')

# The component-only builder never visits existing materials or reuses image
# names. DDS content remains job-authored and hash-bound; no shader source input.
patch('manual_creature_rig.py', 'set(spec) != {"name", "bone", "material", "vertices", "triangles", "loop_uvs"}', 'set(spec) - {"name", "bone", "material", "vertices", "triangles", "loop_uvs", "material_spec"} or not {"name", "bone", "material", "vertices", "triangles", "loop_uvs"} <= set(spec)')
patch('manual_creature_rig.py', '    material=bpy.data.materials.get(spec["material"])\n    if material is None or material not in [mat for obj in meshes for mat in obj.data.materials]:\n        raise ValueError("Component must use an inspected existing working material.")', '''    material=bpy.data.materials.get(spec["material"])
    if "material_spec" in spec:
        if material is not None:
            raise ValueError("Explicit component material must have a new unique name.")
        material = _component_material(req, h, job, spec["material"], spec["material_spec"])
    elif material is None or material not in [mat for obj in meshes for mat in obj.data.materials]:
        raise ValueError("Component requires an existing working material or explicit new job-owned PDX DDS maps.")''')

patch('blender_worker.py', '"author_measured_creature_rig", "attach_rigid_component", "author_measured_creature_action"}:', '"author_measured_creature_rig", "attach_rigid_component", "author_measured_creature_action", "repair_explicit_mesh_winding", "ground_existing_action"}:')
patch('blender_worker.py', 'f"export_anim_{safe_name(action.name)}.json"', 'f"export_anim_{safe_name(action.name)[:32]}_{hashlib.sha256(action.name.encode()).hexdigest()[:10]}.json"')
patch('chaosx_blender_hoi4_mcp.py', '    proof_name: str = "",\n) -> Dict[str, Any]:', '    proof_name: str = "",\n    stage_default_textures: bool = True,\n) -> Dict[str, Any]:')
patch('chaosx_blender_hoi4_mcp.py', '{"mesh_rel": mesh_rel, "anim_rel": anim_rel, "proof_name": proof_name},', '{"mesh_rel": mesh_rel, "anim_rel": anim_rel, "proof_name": proof_name, "stage_default_textures": stage_default_textures},')
patch('blender_worker.py', '    texture_staging = []\n    requested_texture_names', '''    texture_staging = []
    stage_defaults = payload.get("stage_default_textures", True)
    if type(stage_defaults) is not bool:
        raise ValueError("stage_default_textures must be an explicit boolean.")
    if not stage_defaults:
        adjacent = sorted(mesh.parent.glob("*.dds"))
        if not 1 <= len(adjacent) <= 128:
            raise ValueError("Preserved candidate textures require 1-128 adjacent DDS files.")
        for path in adjacent:
            if path.stat().st_size < 128 or path.read_bytes()[:4] != b"DDS ":
                raise ValueError("Invalid prestaged candidate DDS.")
            texture_staging.append({"source":path.relative_to(job).as_posix(), "staged":path.relative_to(job).as_posix(), "bytes":path.stat().st_size, "sha256":file_sha256(path), "copied":False, "policy":"preserve_prestaged_candidate"})
    requested_texture_names''')
patch('blender_worker.py', '    for texture_name in tuple(dict.fromkeys(requested_texture_names + default_texture_names)):', '    for texture_name in (tuple(dict.fromkeys(requested_texture_names + default_texture_names)) if stage_defaults else ()):' )
patch('blender_worker.py', '    if fields["source_kind"] not in {"meshy_animate", "professional_source"}:', '''    if fields["source_kind"] == "manual_blender_gpt6_astra":
        spec_hash = str(action.get("chaosx_manual_action_spec_sha256", "")).upper()
        if not re.fullmatch(r"[0-9A-F]{64}", spec_hash) or not re.fullmatch(r"[0-9A-F]{64}", fields["source_sha256"]):
            raise RuntimeError("Manual action requires retained source checkpoint and declarative spec SHA-256.")
        fields.update(source_reference_id=spec_hash, source_action_name=action.name, manual_spec_sha256=spec_hash,
                      processing_policy="manual_blender_gpt6_astra_hash_bound_declarative_action")
        return fields
    if fields["source_kind"] not in {"meshy_animate", "professional_source"}:''')
new_tools = '''

@mcp.tool()
def chaosx_blender_hoi4_repair_explicit_mesh_winding(job_id: str, blend_rel: str, checkpoint_rel: str, expected_source_sha256: str, mesh_name: str, face_indices: list[int]) -> Dict[str, Any]:
    """Flip an exact reviewed face list in a new hash-bound sibling; preserve corners, weights, rig and actions."""
    return _run(job_id, "repair_explicit_mesh_winding", {"blend_rel":blend_rel,"checkpoint_rel":checkpoint_rel,"expected_source_sha256":expected_source_sha256,"mesh_name":mesh_name,"face_indices":face_indices})

@mcp.tool()
def chaosx_blender_hoi4_ground_existing_action(job_id: str, blend_rel: str, checkpoint_rel: str, expected_source_sha256: str, target_armature_name: str, source_action_name: str, expected_action_sha256: str, target_action_name: str, root_bone: str, excluded_contact_bones: list[str] | None = None) -> Dict[str, Any]:
    """Copy one reviewed skeletal action and correct true-root location in pure world Z."""
    return _run(job_id, "ground_existing_action", {"blend_rel":blend_rel,"checkpoint_rel":checkpoint_rel,"expected_source_sha256":expected_source_sha256,"target_armature_name":target_armature_name,"source_action_name":source_action_name,"expected_action_sha256":expected_action_sha256,"target_action_name":target_action_name,"root_bone":root_bone,"excluded_contact_bones":excluded_contact_bones or []})
'''
patch('chaosx_blender_hoi4_mcp.py','\ndef main() -> None:',new_tools+'\n\ndef main() -> None:')
patch('manual_creature_rig.py', '''            rig.location=base+Vector((0,0,.001-before.z))
            rig.keyframe_insert(data_path="location",frame=frame,group="object_contact_correction")
            bpy.context.view_layer.update()''', '''            _root_vertical_contact(h,rig,rig.pose.bones[spec["root_bone"]],meshes,frame,.001)
            bpy.context.view_layer.update()''')
patch('manual_creature_rig.py', '    base=rig.location.copy(); ground=[]; samples=[]', '''    base=rig.location.copy(); ground=[]; samples=[]
    root=rig.pose.bones[spec["root_bone"]]
    root_locations={}
    for frame in range(spec["frame_start"],spec["frame_end"]+1):
        scene.frame_set(frame); root_locations[frame]=root.location.copy()''')
patch('manual_creature_rig.py', '            _root_vertical_contact(h,rig,rig.pose.bones[spec["root_bone"]],meshes,frame,.001)', '''            root.location=root_locations[frame]; root.keyframe_insert(data_path="location",frame=frame,group=root.name)
            _root_vertical_contact(h,rig,root,meshes,frame,.001)''')
changes['manual_creature_rig.py'] += (root/'repair_additions.py').read_text(encoding='utf-8')
for filename, value in changes.items():
    ast.parse(value)
    (root/filename).write_text(value, encoding='utf-8')
diff = ''.join(''.join(difflib.unified_diff((base/f).read_text(encoding='utf-8-sig').splitlines(True), v.splitlines(True), fromfile=f'a/.tools/3d_pipeline/adapter/{f}', tofile=f'b/.tools/3d_pipeline/adapter/{f}')) for f,v in changes.items())
(root/'recovery.patch').write_text(diff, encoding='utf-8')
(root/'baseline_hashes.json').write_text(json.dumps({f:hashlib.sha256((base/f).read_bytes()).hexdigest().upper() for f in changes}, indent=2)+'\n', encoding='utf-8')
print({f:len(v.splitlines()) for f,v in changes.items()})
