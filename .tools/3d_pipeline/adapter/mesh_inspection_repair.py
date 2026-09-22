"""Read-only mesh landmark inspection and explicit winding repair.

This module deliberately contains no rigging, skinning, or action authoring. Skeletons,
skin weights, and skeletal actions are authored live in Blender.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest().upper()

def name(value):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]{0,127}", value):
        raise ValueError("An explicit safe identifier is required.")
    return value

def vector(value, count=3, bound=10000):
    if not isinstance(value, (list, tuple)) or len(value) != count or any(type(v) not in (int, float) or not math.isfinite(v) or abs(v) > bound for v in value):
        raise ValueError("Expected a bounded finite numeric vector.")
    return list(map(float, value))

def _open(req, h):
    p, job = req["payload"], Path(req["job_root"]).resolve()
    source = h["within"](job, p["blend_rel"])
    output = h["within"](job, p["checkpoint_rel"], allow_missing=True)
    expected = p["expected_source_sha256"]
    if not isinstance(expected, str) or not re.fullmatch(r"[A-Fa-f0-9]{64}", expected) or h["file_sha256"](source) != expected.upper():
        raise ValueError("Source checkpoint SHA-256 mismatch.")
    if source.suffix != ".blend" or output.suffix != ".blend" or output.parent != source.parent or output == source or output.exists():
        raise ValueError("Output must be a new sibling .blend; source overwrite is forbidden.")
    h["bpy"].ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    return job, source, output

def _finish(req, h, job, source, output, report):
    if h["file_sha256"](source) != req["payload"]["expected_source_sha256"].upper():
        raise RuntimeError("Source checkpoint changed during repair.")
    h['bpy'].context.view_layer.update()
    check_pixels = any(getattr(node,'image',None) is not None and not node.image.filepath and not node.image.packed_files for material in h['bpy'].data.materials if material.use_nodes for node in material.node_tree.nodes)
    fingerprint = h['_promotion_fingerprint'](job,[],include_sections=True) if check_pixels else None
    h["save_blend"](output)
    if check_pixels:
        h['bpy'].ops.wm.open_mainfile(filepath=str(output),use_scripts=False)
        persisted = h['_promotion_fingerprint'](job,[],include_sections=True)
        if fingerprint['sha256'] != persisted['sha256']:
            raise RuntimeError('Empty-path image checkpoint save/reopen fingerprint mismatch; output is not accepted. Changed sections: '+repr([key for key in fingerprint['sha256'] if fingerprint['sha256'][key]!=persisted['sha256'].get(key)])+'; object deltas: '+repr({n:{key:(row.get(key),persisted['sections']['objects'].get(n,{}).get(key)) for key in row if row.get(key)!=persisted['sections']['objects'].get(n,{}).get(key)} for n,row in fingerprint['sections']['objects'].items() if row!=persisted['sections']['objects'].get(n)}))
        report['empty_path_image_save_reopen_proof'] = {'passed':True,'image_sha256':persisted['sha256']['images'],'image_records':persisted['sections']['images'],'source_blend_sha256':h['file_sha256'](source)}
    report.update(source=source.relative_to(job).as_posix(), source_sha256=h["file_sha256"](source), checkpoint=output.relative_to(job).as_posix(), checkpoint_sha256=h["file_sha256"](output), new_provider_call=False)
    path = job/"blender"/"reports"/(output.stem+".json")
    path.parent.mkdir(parents=True, exist_ok=True)
    report["report"] = path.relative_to(job).as_posix()
    path.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    return report

def inspect_mesh_landmarks(req,h):
    import bpy
    p=req["payload"]; job=Path(req["job_root"]).resolve(); source=h["within"](job,p["blend_rel"])
    expected=p["expected_source_sha256"].upper()
    if not re.fullmatch(r"[A-F0-9]{64}",expected) or h["file_sha256"](source)!=expected: raise ValueError("Source SHA mismatch.")
    output=h["within"](job,p["report_rel"],allow_missing=True)
    if output.suffix!=".json" or output.exists() or not output.relative_to(job).parts[0] in {"evidence","blender","validation"}: raise ValueError("Use a new job-owned evidence JSON.")
    bpy.ops.wm.open_mainfile(filepath=str(source),use_scripts=False)
    names=p["mesh_names"]
    if not isinstance(names,list) or not 1<=len(names)<=16 or len(set(names))!=len(names): raise ValueError("Require 1-16 exact meshes.")
    meshes=[]
    for n in names:
        obj=bpy.data.objects.get(n)
        if obj is None or obj.type!="MESH" or len(obj.data.vertices)>200000: raise ValueError("Mesh missing or exceeds bounded inventory.")
        meshes.append(obj)
    data={"source":p["blend_rel"],"source_sha256":expected,"meshes":{obj.name:{"vertices":[{"index":v.index,"world":list(obj.matrix_world@v.co)} for v in obj.data.vertices],"triangles":[list(f.vertices) for f in obj.data.polygons],"materials":[m.name if m else None for m in obj.data.materials],"vertex_groups":[g.name for g in obj.vertex_groups],"vertex_weights":[[{"group":g.group,"bone":obj.vertex_groups[g.group].name,"weight":g.weight} for g in v.groups] for v in obj.data.vertices],"triangle_material_indices":[f.material_index for f in obj.data.polygons],"triangle_loop_uvs":{u.name:[[list(u.data[i].uv) for i in f.loop_indices] for f in obj.data.polygons] for u in obj.data.uv_layers},"triangle_normals_local":[list(f.normal) for f in obj.data.polygons],"triangle_corner_normals_local":[[list(obj.data.corner_normals[i].vector) for i in f.loop_indices] for f in obj.data.polygons],"normal_local_to_world":[list(r) for r in obj.matrix_world.inverted().transposed().to_3x3()]} for obj in meshes},"rigs":{rig.name:[{"name":b.name,"parent":b.parent.name if b.parent else None,"head":list(b.head_local),"tail":list(b.tail_local),"matrix_local":[list(v) for v in b.matrix_local],"pose_matrix_basis":[list(v) for v in rig.pose.bones[b.name].matrix_basis],"rotation_mode":rig.pose.bones[b.name].rotation_mode} for b in rig.data.bones] for rig in h["armatures"](False)}}
    for obj in meshes:
        mesh = obj.data
        custom = [a for a in mesh.attributes if a.name in {"custom_normal", ".custom_normal"}]
        data["meshes"][obj.name]["custom_normal_storage"] = [{"name": a.name, "domain": a.domain, "type": a.data_type,
            "values": [list(item.value) for item in a.data] if a.data_type == "INT16_2D" else None} for a in custom]
        data["meshes"][obj.name].update(topology_sha256=h["_mesh_region_topology"](mesh),
            topology_hash_policy="_mesh_region_topology_v1_exact_indexed_vertices_edges_loops_polygons_material_slots",
            topology_records={"vertices": [v.index for v in mesh.vertices],
                "edges": [(e.index, list(e.vertices)) for e in mesh.edges],
                "loops": [(loop.index, loop.vertex_index, loop.edge_index) for loop in mesh.loops],
                "polygons": [(f.index, f.loop_start, f.loop_total, list(f.vertices), f.material_index) for f in mesh.polygons]})
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(data,separators=(",",":"))+"\n",encoding="utf-8")
    if h["file_sha256"](source)!=expected: raise RuntimeError("Inspection altered source.")
    return {"operation":"inspect_mesh_landmarks","report":output.relative_to(job).as_posix(),"report_sha256":h["file_sha256"](output),"counts":{obj.name:len(obj.data.vertices) for obj in meshes},"source_immutable":True,"data_semantics":"rest mesh coordinates under current object transforms; no evaluated pose or semantic inference"}

def validate_component_dds(header, file_size, max_dimension=1024):
    import struct
    if len(header)<128 or header[:4]!=b'DDS ' or struct.unpack_from('<I',header,4)[0]!=124 or struct.unpack_from('<I',header,76)[0]!=32:
        raise ValueError('Invalid DDS header.')
    height,width=struct.unpack_from('<II',header,12)
    if max_dimension not in {1024,2048} or width!=height or width not in {128,256,512,1024,2048} or width>max_dimension: raise ValueError('DDS dimensions exceed the verified component/body texture budget.')
    depth,mips=struct.unpack_from('<II',header,24); mips=max(1,mips)
    if depth not in {0,1} or not 1<=mips<=width.bit_length() or struct.unpack_from('<I',header,112)[0]!=0:
        raise ValueError('Only bounded 2D DDS maps without arrays/cubemaps are supported.')
    flags,fourcc,bits,r,g,b,a=struct.unpack_from('<I4sIIIII',header,80)
    offset=128
    if flags==0x41 and fourcc==b'\0'*4 and (bits,r,g,b,a)==(32,0x00ff0000,0x0000ff00,0x000000ff,0xff000000):
        size=sum(max(1,width>>level)*max(1,height>>level)*4 for level in range(mips))
        if struct.unpack_from('<I',header,20)[0] not in {0,width*4}: raise ValueError('Unsupported BGRA row pitch.')
    elif flags&4 and fourcc in {b'DXT5',b'DX10'}:
        if fourcc==b'DX10':
            if len(header)<148: raise ValueError('Missing DX10 DDS extension.')
            fmt,dim,misc,array,misc2=struct.unpack_from('<IIIII',header,128)
            if fmt not in {77,78,98,99} or dim!=3 or misc!=0 or array!=1: raise ValueError('Require one alpha-capable BC3/BC7 2D DDS.')
            offset=148
        size=sum(max(1,(max(1,width>>level)+3)//4)*max(1,(max(1,height>>level)+3)//4)*16 for level in range(mips))
    else: raise ValueError('Require verified uncompressed A8R8G8B8/BGRA or alpha-capable BC3/BC7 DDS.')
    if file_size!=offset+size: raise ValueError('DDS payload size does not match declared dimensions/mips/encoding.')
    return width,height

def _component_material(req, h, job, material_name, spec, *, max_dimension=1024):
    bpy = h['bpy']
    if not isinstance(spec, dict) or set(spec) != {'shader', 'normal_packing', 'specular_packing', 'maps'} or spec['shader'] != 'PdxMeshAdvanced' or spec['normal_packing'] != 'RRxG' or spec['specular_packing'] != 'rgb_specular_alpha_glossiness':
        raise ValueError('Require explicit PdxMeshAdvanced RRxG normal and RGB specular/alpha glossiness maps.')
    if not isinstance(spec['maps'], dict) or set(spec['maps']) != {'diffuse', 'normal', 'specular'}:
        raise ValueError('Require all three exact DDS maps.')
    paths, sizes = {}, set()
    for role, row in spec['maps'].items():
        if not isinstance(row, dict) or set(row) != {'path_rel', 'sha256'}:
            raise ValueError('Map requires exact job path and SHA256.')
        path = h['within'](job, row['path_rel'])
        if path.suffix.lower() != '.dds' or not re.fullmatch(r'[A-Fa-f0-9]{64}', row['sha256']) or h['file_sha256'](path) != row['sha256'].upper():
            raise ValueError('DDS path or checksum mismatch.')
        with path.open('rb') as handle: header=handle.read(148)
        width,height=validate_component_dds(header,path.stat().st_size,max_dimension=max_dimension)
        sizes.add((width,height)); paths[role]=path
    if len(sizes)!=1: raise ValueError('Component map dimensions must match.')
    image_names = {role: material_name+'_'+role for role in paths}
    if any(bpy.data.images.get(n) for n in image_names.values()):
        raise ValueError('Component image names must be new; existing maps cannot be replaced.')
    material=bpy.data.materials.new(material_name)
    h['ensure_material_nodes'](material)
    shader=h['_principled_shader'](material)
    shader.inputs['Metallic'].default_value=0
    shader.inputs['Alpha'].default_value=1
    for role,path in paths.items():
        image=h['_load_texture_image'](path,image_names[role],non_color=role!='diffuse')
        if tuple(image.size) != next(iter(sizes)): raise ValueError('DDS decoder dimensions mismatch.')
        node=material.node_tree.nodes.new('ShaderNodeTexImage'); node.name='CHAOSX_'+role.upper()+'_TEXTURE'; node.image=image
        if role=='normal':
            separate=material.node_tree.nodes.new('ShaderNodeSeparateColor'); separate.mode='RGB'
            combine=material.node_tree.nodes.new('ShaderNodeCombineColor'); combine.mode='RGB'
            links=material.node_tree.links
            links.new(node.outputs['Color'],separate.inputs['Color'])
            links.new(separate.outputs['Green'],combine.inputs['Red'])
            links.new(node.outputs['Alpha'],combine.inputs['Green'])
            def math_node(op,a=None,b=None,a_value=0,b_value=0):
                n=material.node_tree.nodes.new('ShaderNodeMath'); n.operation=op
                n.inputs[0].default_value=a_value; n.inputs[1].default_value=b_value
                if a is not None: links.new(a,n.inputs[0])
                if b is not None: links.new(b,n.inputs[1])
                return n.outputs[0]
            x=math_node('SUBTRACT',math_node('MULTIPLY',separate.outputs['Green'],b_value=2),b_value=1)
            y=math_node('SUBTRACT',math_node('MULTIPLY',node.outputs['Alpha'],b_value=2),b_value=1)
            squared=math_node('ADD',math_node('MULTIPLY',x,x),math_node('MULTIPLY',y,y))
            z=math_node('SQRT',math_node('MAXIMUM',math_node('SUBTRACT',b=squared,a_value=1),b_value=0))
            encoded_z=math_node('MULTIPLY',math_node('ADD',z,b_value=1),b_value=.5)
            links.new(encoded_z,combine.inputs['Blue'])
            normal=material.node_tree.nodes.new('ShaderNodeNormalMap'); normal.name='CHAOSX_NORMAL_MAP'
            material.node_tree.links.new(combine.outputs['Color'],normal.inputs['Color'])
            material.node_tree.links.new(normal.outputs['Normal'],shader.inputs['Normal'])
        elif role=='specular':
            separate=material.node_tree.nodes.new('ShaderNodeSeparateColor'); separate.mode='RGB'
            material.node_tree.links.new(node.outputs['Color'],separate.inputs['Color'])
            material.node_tree.links.new(separate.outputs['Green'],shader.inputs['Specular IOR Level'])
            material.node_tree.links.new(separate.outputs['Blue'],shader.inputs['Metallic'])
            inverse=material.node_tree.nodes.new('ShaderNodeMath'); inverse.operation='SUBTRACT'; inverse.inputs[0].default_value=1
            material.node_tree.links.new(node.outputs['Alpha'],inverse.inputs[1])
            material.node_tree.links.new(inverse.outputs[0],shader.inputs['Roughness'])
        else:
            material.node_tree.links.new(node.outputs['Color'],shader.inputs['Base Color'])
    pdx=h['load_pdx'](req['io_pdx_root'])
    material[pdx['PDX_SHADER']]='PdxMeshAdvanced'; material['chaosx_pdx_shader']='PdxMeshAdvanced'
    material['chaosx_component_material_spec_sha256']=digest(spec)
    material['chaosx_component_material_maps']=json.dumps(spec,sort_keys=True)
    return material

def winding_inventory(mesh):
    edges={}
    for face in mesh.polygons:
        ids=list(face.vertices)
        for a,b in zip(ids,ids[1:]+ids[:1]):
            edges.setdefault(tuple(sorted((a,b))),[]).append((face.index,1 if a<b else -1))
    return {'boundary_edges':sum(len(v)==1 for v in edges.values()),'nonmanifold_edges':sum(len(v)>2 for v in edges.values()),'inconsistent_shared_edges':sum(len(v)==2 and v[0][1]==v[1][1] for v in edges.values())}

def repair_explicit_mesh_winding(req,h):
    p=req['payload']; job,source,output=_open(req,h); bpy=h['bpy']
    tolerance=p.get('angular_tolerance_degrees',0.25)
    if type(tolerance) not in (int,float) or not math.isfinite(tolerance) or not 0<tolerance<=0.5:raise ValueError('Explicit native normal angular tolerance must be positive and at most0.5 degrees.')
    obj=bpy.data.objects.get(p['mesh_name'])
    if obj not in h['mesh_objects']() or obj.library or obj.data.library or obj.data.shape_keys or obj.data.users!=1 or obj.get('chaosx_source_protected') or obj.get('chaosx_reference_read_only'):
        raise ValueError('Winding repair requires one exact unshared approved local working mesh.')
    mesh=obj.data; ids=p['face_indices']
    if not isinstance(ids,list) or not 1<=len(ids)<=100000 or len(set(ids))!=len(ids) or any(type(i) is not int or not 0<=i<len(mesh.polygons) for i in ids):
        raise ValueError('Require bounded exact unique existing face indices.')
    if any(len(f.vertices)!=3 for f in mesh.polygons): raise ValueError('Winding repair requires existing triangular topology.')
    # Reject non-UV corner data that requires a separate conversion contract.
    uv_names={u.name for u in mesh.uv_layers}
    if any(a.domain=='CORNER' and a.name not in uv_names and not a.name.startswith('.') and a.name!='custom_normal' for a in mesh.attributes):
        raise ValueError('Unsupported non-UV corner attributes require explicit preservation review.')
    before=h['_promotion_fingerprint'](job,[],include_sections=True)
    positions=digest([list(v.co) for v in mesh.vertices])
    faces={f.index:list(f.vertices) for f in mesh.polygons}
    corners={u.name:{f.index:{mesh.loops[i].vertex_index:list(u.data[i].uv) for i in f.loop_indices} for f in mesh.polygons} for u in mesh.uv_layers}
    from mesh_winding_repair import _corner_normals, _verify_normal_signs
    original_normals=_corner_normals(mesh); selected_faces=set(ids)
    unset_normals=[]
    for key,value in list(original_normals.items()):
        if sum(x*x for x in value)<1e-24:
            if key[0] not in selected_faces:
                raise ValueError('Untouched corner has undefined source normal: '+repr(key))
            geometric=tuple(mesh.polygons[key[0]].normal)
            if sum(x*x for x in geometric)<1e-24:
                raise ValueError('Selected face has no geometric normal for explicit unset-normal repair: '+repr(key))
            original_normals[key]=geometric
            unset_normals.append({'face_vertex':key,'source_normal':value,'geometric_source_normal':geometric})
    topology_before=winding_inventory(mesh)
    for i in ids: mesh.polygons[i].flip()
    for u in mesh.uv_layers:
        for f in mesh.polygons:
            for i in f.loop_indices: u.data[i].uv=corners[u.name][f.index][mesh.loops[i].vertex_index]
    mesh.update()
    desired=[None]*len(mesh.loops)
    for face in mesh.polygons:
        sign=-1 if face.index in selected_faces else 1
        for index in face.loop_indices:
            source_normal=original_normals[(face.index,mesh.loops[index].vertex_index)]
            magnitude=math.sqrt(sum(x*x for x in source_normal))
            desired[index]=tuple(sign*x/magnitude for x in source_normal)
    mesh.normals_split_custom_set(desired)
    mesh.update()
    normal_proof=_verify_normal_signs(mesh,original_normals,selected_faces,angular_tolerance_degrees=tolerance)
    if digest([list(v.co) for v in mesh.vertices])!=positions: raise RuntimeError('Winding repair moved vertices.')
    for f in mesh.polygons:
        old=faces[f.index]; new=list(f.vertices)
        expected=list(reversed(old)) if f.index in set(ids) else old
        if not any(new==expected[n:]+expected[:n] for n in range(3)): raise RuntimeError('Unexpected face connectivity change.')
        for u in mesh.uv_layers:
            if any(list(u.data[i].uv)!=corners[u.name][f.index][mesh.loops[i].vertex_index] for i in f.loop_indices): raise RuntimeError('Corner UV association changed.')
    after=h['_promotion_fingerprint'](job,[],include_sections=True)
    for section in ('objects','rigs','materials','images','actions','scene'):
        if before['sha256'][section]!=after['sha256'][section]: raise RuntimeError('Winding repair changed '+section)
    for n,row in before['sections']['geometry'].items():
        compare=after['sections']['geometry'][n]
        keys=('vertices','polygons','loops','weights','groups','materials','uv_settings','uv_active_index','properties') if n==obj.name else row.keys()
        if any(row[k]!=compare[k] for k in keys): raise RuntimeError('Winding repair changed preserved mesh data.')
    topology_after=winding_inventory(mesh)
    if any(topology_after[k]!=topology_before[k] for k in ('boundary_edges','nonmanifold_edges')) or topology_after['inconsistent_shared_edges']>topology_before['inconsistent_shared_edges']:
        raise RuntimeError('Winding repair changed topology or increased inconsistent edges.')
    mesh_name=obj.name
    report=_finish(req,h,job,source,output,{'operation':'repair_explicit_mesh_winding','mesh':obj.name,'face_indices':ids,'face_indices_sha256':digest(ids),'topology_before':topology_before,'topology_after':topology_after,'positions_preserved':True,'corner_uvs_preserved':True,'rig_weights_actions_materials_preserved':True,'normal_policy':'preserve every unaffected corner normal; negate only explicitly flipped face corners','normal_sign_proof':normal_proof,'selected_unset_normal_replacements':unset_normals,'status':'saved_pending_reopen_normal_proof'})

    bpy.ops.wm.open_mainfile(filepath=str(output),use_scripts=False)
    report['reopened_normal_sign_proof']=_verify_normal_signs(bpy.data.objects[mesh_name].data,original_normals,selected_faces,angular_tolerance_degrees=tolerance)
    report['status']='repaired_requires_culling_on_visual_and_export_reimport_review'
    (job/report['report']).write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    return report
