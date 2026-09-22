"""Disposable native transactions and protected-data negative regressions."""
import copy
import json
import math
import sys
import tempfile
from pathlib import Path
import bpy
sys.path.insert(0, str(Path(__file__).resolve().parent))
from blender_locator_adapter_integration import PIPELINE_ROOT, RIG_NAME, ROOT_BONE, PARENT_BONE, blender_worker as api, create_fixture
import explicit_batch_repair as batch


def run():
    results = {}
    with tempfile.TemporaryDirectory(prefix="chaosx_batch_") as directory:
        job = Path(directory)
        for operation, kind in batch.OPERATIONS.items():
            create_fixture(job)
            body = bpy.data.objects['FixtureBody']
            body.vertex_groups.new(name=ROOT_BONE)
            second = body.copy()
            second.data = body.data.copy()
            second.name = 'FixtureSecond'
            bpy.context.scene.collection.objects.link(second)
            unselected = body.copy()
            unselected.data = body.data.copy()
            unselected.name = 'FixtureUnselected'
            bpy.context.scene.collection.objects.link(unselected)
            for obj in (body, second):
                if kind == 'winding':
                    obj.data.polygons[0].flip()
                obj.data.normals_split_custom_set([list(n.vector) for n in obj.data.corner_normals])
                obj.data.update()
            source = job / (kind + '_source.blend')
            bpy.ops.wm.save_as_mainfile(filepath=str(source), relative_remap=False)
            bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
            rows = []
            for name in ('FixtureBody', 'FixtureSecond'):
                obj = bpy.data.objects[name]
                row = dict(mesh=name, rig=RIG_NAME, topology_sha256=api._mesh_region_topology(obj.data), selection_sha256='0'*64, review_evidence='Disposable explicit two-mesh regression selection.')
                if kind == 'winding':
                    row.update(face_indices=[0], angular_tolerance_degrees=0.5)
                else:
                    face = obj.data.polygons[0]
                    prior = list(obj.data.corner_normals[face.loop_start].vector)
                    prior = [v/math.sqrt(sum(x*x for x in prior)) for v in prior]
                    requested = [prior[0]+0.03, prior[1]+0.02, prior[2]+0.01]
                    requested = [v/math.sqrt(sum(x*x for x in requested)) for v in requested]
                    row['corners'] = [dict(face_index=0, corner_index=0, vertex_index=face.vertices[0], expected_before=prior, requested_after=requested)]
                row['selection_sha256'] = api._promotion_digest(batch.selection_records(obj, kind, row))
                rows.append(row)
            spec = job / (kind + '.json')
            spec.write_text(json.dumps({'meshes':rows}), encoding='utf-8')
            request = dict(operation=operation, job_root=str(job), payload=dict(blend_rel=source.name, checkpoint_rel=kind+'_repaired.blend', expected_source_sha256=api.file_sha256(source), repair_spec_rel=spec.name, expected_repair_spec_sha256=api.file_sha256(spec)))
            captures = []
            native_snapshot = api._promotion_fingerprint
            def capture(*args, **kwargs):
                value = native_snapshot(*args, **kwargs)
                captures.append(copy.deepcopy(value))
                return value
            api._promotion_fingerprint = capture
            try:
                results[kind] = batch.run_repair(request, api)
            except Exception:
                if len(captures) > 1:
                    a, b = captures[0]['sections']['geometry']['FixtureBody'], captures[1]['sections']['geometry']['FixtureBody']
                    print('GEOMETRY_DELTA', json.dumps({key:[a[key], b[key]] for key in a if a[key] != b[key]}))
                raise
            finally:
                api._promotion_fingerprint = native_snapshot
            assert len(captures) == 3, 'Exactly one full before/after/reopened fingerprint per transaction'
            assert results[kind]['source_immutable'] and results[kind]['reopen_comparison']['accepted']
            cached_stats, uncached_stats = {}, {}
            cached = api._promotion_fingerprint(job, (), include_sections=True, image_cache_stats=cached_stats)
            uncached = api._promotion_fingerprint(job, (), include_sections=True, cache_image_records=False, image_cache_stats=uncached_stats)
            assert cached == uncached
            results[kind]['cached_uncached_equality'] = {'equal':True, 'cached':cached_stats, 'uncached':uncached_stats}
            failures = {}
            def reject(label, mutate):
                bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
                originals = [batch.preflight_mesh(api, row, kind) for row in rows]
                before = batch.project_fingerprint(api, api._promotion_fingerprint(job, (), include_sections=True), originals, kind)
                for original in originals:
                    batch._apply(api, original, kind)
                mutate()
                bpy.context.view_layer.update()
                try:
                    for original in originals:
                        batch.verify_mesh(api, original, kind)
                    after = batch.project_fingerprint(api, api._promotion_fingerprint(job, (), include_sections=True), originals, kind)
                    if before != after:
                        raise RuntimeError('Protected fingerprint mismatch')
                except (ValueError, RuntimeError) as exc:
                    failures[label] = str(exc)
                else:
                    raise AssertionError('Accepted protected drift: ' + label)
            reject('unselected_mesh_position', lambda: setattr(bpy.data.objects['FixtureUnselected'].data.vertices[0], 'co', (7,8,9)))
            reject('selected_mesh_position', lambda: setattr(bpy.data.objects['FixtureBody'].data.vertices[0], 'co', (7,8,9)))
            reject('image_content_metadata', lambda: setattr(bpy.data.images['FixtureDiffuse'], 'alpha_mode', 'NONE'))
            reject('material_property', lambda: bpy.data.materials['FixtureMaterial'].__setitem__('shader', 'Changed'))
            reject('rig_property', lambda: bpy.data.objects[RIG_NAME].data.__setitem__('unexpected', True))
            reject('action_property', lambda: bpy.data.actions[0].__setitem__('unexpected', True))
            reject('unselected_face', lambda: bpy.data.objects['FixtureBody'].data.polygons[1].flip())
            reject('unselected_uv', lambda: setattr(bpy.data.objects['FixtureBody'].data.uv_layers[0].data[5], 'uv', (9,9)))
            reject('unselected_weight', lambda: bpy.data.objects['FixtureBody'].vertex_groups[PARENT_BONE].add([2], .3, 'REPLACE'))
            if kind == 'normals':
                def change_raw():
                    attribute = bpy.data.objects['FixtureBody'].data.attributes['custom_normal']
                    attribute.data[1].value = (100,200)
                    bpy.data.objects['FixtureBody'].data.update()
                reject('unselected_raw_corner', change_raw)
                bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
                tiny = copy.deepcopy(rows[0])
                prior = tiny['corners'][0]['expected_before']
                requested = [prior[0]+1e-10, prior[1], prior[2]]
                length = math.sqrt(sum(v*v for v in requested))
                tiny['corners'][0]['requested_after'] = [v/length for v in requested]
                original = batch.preflight_mesh(api, tiny, kind)
                batch._apply(api, original, kind)
                try:
                    batch.verify_mesh(api, original, kind)
                except RuntimeError as exc:
                    assert 'unchanged native raw pair' in str(exc)
                    failures['quantized_native_noop'] = str(exc)
                else:
                    raise AssertionError('Accepted a quantized native no-op')
            # A bad final row must fail before the first mesh is touched.
            bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
            bad = copy.deepcopy(rows)
            bad[-1]['selection_sha256'] = '0'*64
            applied = batch._apply
            calls = []
            def forbidden_apply(*args):
                calls.append(True)
                raise AssertionError('Mutation before complete preflight')
            batch._apply = forbidden_apply
            bad_spec = job / (kind + '_bad.json')
            bad_spec.write_text(json.dumps({'meshes':bad}), encoding='utf-8')
            bad_request = copy.deepcopy(request)
            bad_request['payload'].update(checkpoint_rel=kind+'_bad.blend', repair_spec_rel=bad_spec.name, expected_repair_spec_sha256=api.file_sha256(bad_spec))
            try:
                batch.run_repair(bad_request, api)
            except ValueError as exc:
                failures['all_preconditions_before_mutation'] = str(exc)
            else:
                raise AssertionError('Accepted invalid final precondition')
            finally:
                batch._apply = applied
            assert calls == [] and not (job / (kind+'_bad.blend')).exists()
            results[kind]['negative_cases'] = failures
        from mesh_inspection_repair import inspect_mesh_landmarks
        landmark_req={'job_root':str(job),'payload':{'blend_rel':source.name,'expected_source_sha256':api.file_sha256(source),'mesh_names':['FixtureBody','FixtureSecond'],'report_rel':'evidence/landmarks.json'}}
        landmarks=inspect_mesh_landmarks(landmark_req,api.__dict__)
        inventory=json.loads((job/landmarks['report']).read_text())
        for row in inventory['meshes'].values():
            assert api._promotion_digest(row['topology_records'])==row['topology_sha256']
            assert row['custom_normal_storage'][0]['type']=='INT16_2D'
        results['landmarks']={'exact_topology_records':True,'custom_normal_storage':True,'source_immutable':landmarks['source_immutable']}
        from material_visibility_probe import run_material_visibility_probe
        framing = {'preview_region':{'min':[-1,-1,-1],'max':[1,1,1]}, 'preview_resolution':1024}
        calls = []
        def render_capture(job, stem, views, **kwargs):
            calls.append(kwargs)
            path = job / (stem + '.png')
            path.write_bytes(b'framing forwarding fixture')
            return [path.name]
        probe_request = {'job_root':str(job), 'payload':dict(blend_rel=source.name, expected_source_sha256=api.file_sha256(source),
            material_visibility={'target_mesh_names':['FixtureBody']}, render_previews=True, preview_frame=1, runtime_stem='focused_probe', preview_view_names=['front'], **framing)}
        visibility = run_material_visibility_probe(probe_request, bpy=bpy, render_previews=render_capture, action_hash=api._mesh_region_action_hash)
        assert calls == [framing]*3 and visibility['source_reloaded'] and not visibility['checkpoint_saved']
        results['visibility_framing'] = {'passed':True, 'three_render_calls':calls, 'source_immutable':visibility['source_sha256_before']==visibility['source_sha256_after']}
    target = PIPELINE_ROOT / 'reports/explicit_batch_repair_1_10_47_native.json'
    lock=json.loads((PIPELINE_ROOT/'config/dependencies.lock.json').read_text())['routes']['blender_hoi4_adapter']
    results['adapter_build']={'version':lock['version'],'source_sha256':{path:api.file_sha256(PIPELINE_ROOT.parents[1]/path) for path in set(lock['source_sha256'])|{'.tools/3d_pipeline/adapter/explicit_batch_repair.py'}}}
    target.write_text(json.dumps(results, indent=2)+'\n', encoding='utf-8')
    print('NATIVE_BATCH_REPAIR_PASS', target)


if __name__ == '__main__':
    run()
