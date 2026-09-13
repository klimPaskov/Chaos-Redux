from pathlib import Path
root=Path.cwd(); draft=root/'docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/motion_retarget'
p=root/'.tools/3d_pipeline/adapter/blender_worker.py'; s=p.read_text(encoding='utf-8')
s=s.replace('{"meshy_animate", "professional_source"}', '{"meshy_animate", "meshy_text_to_motion", "professional_source"}')
s=s.replace('source_kind must be meshy_animate or professional_source.', 'source_kind must be meshy_animate, meshy_text_to_motion or professional_source.')
s=s.replace('    source_pose_cache: Dict[int, Dict[str, Tuple[Vector, Quaternion]]] = {}', '''    from retarget_root_motion import vertical_root_basis_location
    target_roots = [b for b in target_rig.data.bones if b.parent is None and b.name in bone_chains]
    if len(target_roots) != 1:
        raise ValueError("Retarget requires exactly one explicitly mapped target root.")
    target_root = target_roots[0]
    if target_rig.pose.bones[target_root.name].constraints:
        raise ValueError("Root translation proof requires an unconstrained target root.")
    root_source_name = bone_chains[target_root.name][-1]
    scale_ref = payload.get("root_scale_reference")
    anatomical_scale = 1.0
    scale_evidence = {"policy": "world_units_identity", "ratio": 1.0}
    if source_kind == "meshy_text_to_motion" and not scale_ref:
        raise ValueError("Text-to-Motion requires explicit measured root_scale_reference joint-head pairs.")
    if scale_ref:
        if not isinstance(scale_ref, dict) or set(scale_ref) != {"source_head_bones", "target_head_bones"}:
            raise ValueError("root_scale_reference requires source_head_bones and target_head_bones only.")
        lengths = []
        for key, rig in (("source_head_bones", source_rig), ("target_head_bones", target_rig)):
            pair = scale_ref[key]
            if not isinstance(pair, list) or len(pair) != 2 or pair[0] == pair[1] or any(name not in rig.data.bones for name in pair):
                raise ValueError("Scale reference must name two distinct existing joints per rig.")
            points = [rig.matrix_world @ rig.data.bones[name].head_local for name in pair]
            distance = (points[1] - points[0]).length
            if not math.isfinite(distance) or distance <= 1e-6:
                raise ValueError("Measured anatomical span is zero or invalid.")
            lengths.append(distance)
        anatomical_scale = lengths[1] / lengths[0]
        scale_evidence = {"policy": "measured_world_joint_head_span", "reference": scale_ref,
                          "source_world_span": lengths[0], "target_world_span": lengths[1], "ratio": anatomical_scale}
    root_world_cache = {}
    target_basis_to_world = (target_rig.matrix_world @ target_root.matrix_local).to_3x3()
    source_object_rotation = source_rig.matrix_world.to_quaternion().normalized()
    target_object_rotation = target_rig.matrix_world.to_quaternion().normalized()
    source_pose_cache: Dict[int, Dict[str, Tuple[Vector, Quaternion]]] = {}''',1)
s=s.replace('        source_deltas: Dict[str, Tuple[Vector, Quaternion]] = {}', '        root_world_cache[frame] = (source_rig.matrix_world @ source_rig.pose.bones[root_source_name].matrix).translation.copy()\n        source_deltas: Dict[str, Tuple[Vector, Quaternion]] = {}',1)
s=s.replace('            source_deltas[target_name] = (location.copy(), source_world_rotation)', '''            # Conjugate the source armature-space delta through both object orientations.
            source_world_rotation = (target_object_rotation.inverted() @ source_object_rotation
                                     @ source_world_rotation @ source_object_rotation.inverted()
                                     @ target_object_rotation).normalized()
            source_deltas[target_name] = (location.copy(), source_world_rotation)''',1)
s=s.replace('''    for frame in range(frame_start, frame_end + 1):
        bpy.context.scene.frame_set(frame)
        for target_name in bone_chains:''', '''    root_world_proof = []
    target_rest_root_world = (target_rig.matrix_world @ target_root.matrix_local).translation.copy()
    for frame in range(frame_start, frame_end + 1):
        bpy.context.scene.frame_set(frame)
        for target_name in bone_chains:''',1)
s=s.replace('''                root_delta = source_location - source_root_location
                target_bone.location = Vector((0.0, 0.0, root_delta.z * location_scale))''', '''                source_world_delta = (root_world_cache[frame] - root_world_cache[frame_start]) * anatomical_scale
                target_bone.location = Vector(vertical_root_basis_location(
                    source_world_delta, (0.0, 0.0, 0.0), target_basis_to_world))''',1)
s=s.replace('''        bpy.context.view_layer.update()

    scale_cleanup = sanitize_action_scale_channels()
    root_cleanup = {''', '''        bpy.context.view_layer.update()
        actual_delta = (target_rig.matrix_world @ target_rig.pose.bones[target_root_name].matrix).translation - target_rest_root_world
        expected_delta = Vector((0.0, 0.0, (root_world_cache[frame].z - root_world_cache[frame_start].z) * anatomical_scale))
        error = (actual_delta - expected_delta).length
        if error > 2e-5:
            raise RuntimeError("Retarget root world displacement differs from scaled vertical source: " + str({"frame": frame, "error": error}))
        root_world_proof.append({"frame": frame, "source_world": list(root_world_cache[frame]),
                                 "expected_target_delta": list(expected_delta), "actual_target_delta": list(actual_delta), "error": error})

    scale_cleanup = sanitize_action_scale_channels()
    root_cleanup = {''',1)
s=s.replace('''        "policy": "provider armature-space motion reconstructed hierarchy-first through target rest and animated parent bases; target-root X/Y motion removed and Z retained; source pose-basis translation is converted to target pose-basis units by source-world-scale divided by target-world-scale",''', '''        "policy": "source hierarchy world-root delta scaled by explicit measured joint-head span; world X/Y removed; world Z converted through inverse target armature/rest-root basis; rotations conjugated through source/target object orientations",
        "anatomical_scale": scale_evidence,
        "world_root_displacement_proof": root_world_proof,
        "maximum_world_root_error": max(row["error"] for row in root_world_proof),''',1)
s=s.replace('"location_scale_formula": "source_armature_uniform_world_scale / target_armature_uniform_world_scale"', '"location_scale_formula": "source_world_delta * measured_world_joint_span_ratio then inverse_target_world_rest_basis"',2)
s=s.replace('    bpy.ops.wm.open_mainfile(filepath=str(blend))\n    audited_target_promotion', '    if checkpoint == blend or checkpoint.exists():\n        raise ValueError("Animation transfer requires a new sibling checkpoint.")\n    bpy.ops.wm.open_mainfile(filepath=str(blend))\n    if bpy.data.actions.get(action_name) is not None:\n        raise ValueError("Animation transfer requires a new target action name.")\n    audited_target_promotion',1)
s=s.replace('    if operation == "rotate_existing_assembly_yaw":', '    if operation == "inspect_animation_source":\n        from retarget_root_motion import inspect_animation_source\n        return inspect_animation_source(req, globals())\n    if operation == "rotate_existing_assembly_yaw":',1)
(draft/p.name).write_bytes(s.encode('utf-8'))
p=root/'.tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py'; s=p.read_text(encoding='utf-8')
s=s.replace('Literal["meshy_animate", "professional_source"]','Literal["meshy_animate", "meshy_text_to_motion", "professional_source"]')
start=s.index('def chaosx_blender_hoi4_import_animation_action('); end=s.index('\n@mcp.tool()',start)
chunk=s[start:end].replace('    source_armature_name: str = "",','    source_armature_name: str = "",\n    root_scale_reference: Dict[str, list[str]] | None = None,').replace('            "bone_chains": bone_chains or {},','            "bone_chains": bone_chains or {},\n            "root_scale_reference": root_scale_reference,')
s=s[:start]+chunk+s[end:]
s+='''\n\n@mcp.tool()
def chaosx_blender_hoi4_inspect_animation_source(job_id: str, source_rel: str, source_sha256: str) -> Dict[str, Any]:
    """Read standalone FBX skeleton/action identity in a disposable scene without a target checkpoint."""
    return _run(job_id, "inspect_animation_source", {"source_rel": source_rel, "source_sha256": source_sha256})
'''
# Tool definitions must precede the server entry point.
block=s[s.rindex('\n\n@mcp.tool()'):]; s=s[:s.rindex('\n\n@mcp.tool()')]
idx=s.index('if __name__ == "__main__":'); s=s[:idx]+block+'\n\n'+s[idx:]
(draft/p.name).write_bytes(s.encode('utf-8'))
for p in draft.glob('*.py'):
    if p.name != 'stage.py': compile(p.read_text(encoding='utf-8-sig'),str(p),'exec')
print('Staged worker/server/helper compile successfully')

