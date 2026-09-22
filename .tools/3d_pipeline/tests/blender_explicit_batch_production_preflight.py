"""Read-only production evidence; edits exist only in unsaved Blender memory."""
import json
import sys
import time
from pathlib import Path
import bpy
sys.path.insert(0, str(Path(__file__).resolve().parent))
from blender_locator_adapter_integration import PIPELINE_ROOT, REPO_ROOT, blender_worker as api
import explicit_batch_repair as batch


def main():
    base = REPO_ROOT / 'docs/assets/002_zombie_outbreak/models_3d'
    job = base / 'demonic_zombies'
    source = job / 'blender/checkpoints/06_df_winding_02.blend'
    expected = '0C0D094809547615EF27587612C44761FE5D78D5612DE285AC43FD84B214B8BB'
    assert api.file_sha256(source) == expected
    bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    statistics = {}
    fingerprints = []
    for mode in ((True,) if '--quick' in sys.argv else (True, False)):
        stats = {}
        started = time.perf_counter()
        fingerprints.append(api._promotion_fingerprint(job, (), include_sections=True, cache_image_records=mode, image_cache_stats=stats))
        statistics[str(mode)] = {**stats, 'elapsed_seconds':time.perf_counter()-started}
        print('CACHE_TIMING', mode, statistics[str(mode)], flush=True)
    if '--quick' not in sys.argv:
        assert fingerprints[0] == fingerprints[1]
    evidence = job / 'evidence/finalize_2026-09-12/orientation_ray_review.json'
    candidates = json.loads(evidence.read_text())['candidate_faces_by_mesh']
    rows = []
    for name, faces in candidates.items():
        if name in {'mesh.007','mesh.009'} or not faces:
            continue
        obj = bpy.data.objects[name]
        row = dict(mesh=name, rig=obj.modifiers[0].object.name, topology_sha256=api._mesh_region_topology(obj.data), selection_sha256='0'*64,
            review_evidence='Reviewed orientation_ray_review.json; exclude the two already applied mesh.007/.009 lists; no inferred faces.', face_indices=faces, angular_tolerance_degrees=0.5)
        row['selection_sha256'] = api._promotion_digest(batch.selection_records(obj, 'winding', row))
        rows.append(row)
    batch.validate_specs({'meshes':rows}, 'winding')
    originals = [batch.preflight_mesh(api, row, 'winding') for row in rows]
    before = batch.project_fingerprint(api, fingerprints[0], originals, 'winding')
    for original in originals:
        batch._apply(api, original, 'winding')
    bpy.context.view_layer.update()
    proofs = [batch.verify_mesh(api, original, 'winding') for original in originals]
    after = batch.project_fingerprint(api, api._promotion_fingerprint(job, (), include_sections=True), originals, 'winding')
    assert before == after
    assert api.file_sha256(source) == expected
    result = {'status':'pass_read_only_no_save', 'demonic':{'source_sha256':expected, 'mesh_count':len(rows), 'face_count':sum(len(row['face_indices']) for row in rows),
        'spec':{'meshes':rows}, 'review_evidence_sha256':api.file_sha256(evidence), 'cached_uncached_equal':len(fingerprints)==2, 'cache_stats':statistics, 'protected_before':before, 'protected_after':after, 'mesh_proofs':proofs}}
    bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    # Read the exact blocking corner; there is no approved replacement vector.
    job = base / 'parasitic_zombies'
    source = job / 'blender/checkpoints/05_contact_v19_death.blend'
    expected = 'B8BA8C582D874EE1D7D0C0AEBFE5D9E2121796D52D791941D7064BE6DF46A832'
    assert api.file_sha256(source) == expected
    bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    matches = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH' and len(obj.data.polygons) > 24825 and list(obj.data.polygons[24825].vertices) == [24820,24838,24819]]
    assert len(matches) == 1
    obj = matches[0]
    raw = batch.raw_normals(obj.data)
    face = obj.data.polygons[24825]
    loop = face.loop_indices[2]
    result['parasitic'] = {'source_sha256':expected, 'mesh':obj.name, 'face':24825, 'corner':2, 'vertex':obj.data.loops[loop].vertex_index,
        'native_direction':list(obj.data.corner_normals[loop].vector), 'raw_pair':raw['values'][loop], 'raw_storage_sha256':api._promotion_digest(raw),
        'topology_sha256':api._mesh_region_topology(obj.data), 'replacement_vector_approved':False, 'mutation_attempted':False}
    result['parasitic']['neighbor_faces']=[{'face':face.index,'vertices':list(face.vertices),'positions_local':[list(obj.data.vertices[v].co) for v in face.vertices],
        'normal_local':list(face.normal),'corner_normals_local':[list(obj.data.corner_normals[i].vector) for i in face.loop_indices],
        'raw_pairs':[raw['values'][i] for i in face.loop_indices], 'uvs':{layer.name:[list(layer.data[i].uv) for i in face.loop_indices] for layer in obj.data.uv_layers}}
        for face in obj.data.polygons if 24819 in face.vertices]
    assert api.file_sha256(source) == expected
    job = base / 'mutant_zombies'
    source = job / 'blender/checkpoints/05_v15_winding_v1_attack.blend'
    expected = '138DE96AC6F0957321768ECB00805091EE7E113F176A91DD46FC0A4B3F5720A8'
    assert api.file_sha256(source) == expected
    bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    meshes = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
    inventory = {}
    for obj in meshes:
        actual = [{obj.vertex_groups[group.group].name: float(group.weight) for group in vertex.groups} for vertex in obj.data.vertices]
        assert all(1 <= len(weights) <= 4 and all(v>0 for v in weights.values()) and abs(sum(weights.values())-1)<1e-6 for weights in actual)
        inventory[obj.name] = {'vertices':len(actual), 'weights_sha256':api._promotion_digest(actual), 'topology_sha256':api._mesh_region_topology(obj.data)}
    cached = api._promotion_fingerprint(job, (), include_sections=True)
    uncached = api._promotion_fingerprint(job, (), include_sections=True, cache_image_records=False)
    assert cached == uncached and api.file_sha256(source) == expected
    result['mutant'] = {'source_sha256':expected, 'mutation_needed':False, 'reason':'Existing exact skin and winding are accepted; read-only current inventory only.', 'meshes':inventory, 'cached_uncached_equal':True, 'full_sha256':cached['sha256']}
    path = PIPELINE_ROOT / 'reports/explicit_batch_repair_1_10_47_production.json'
    path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('PRODUCTION_PREFLIGHT_PASS_NO_SAVE', path, flush=True)


if __name__ == '__main__':
    main()
