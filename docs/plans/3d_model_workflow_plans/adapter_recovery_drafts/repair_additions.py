

def validate_component_dds(header, file_size):
    import struct
    if len(header)<128 or header[:4]!=b'DDS ' or struct.unpack_from('<I',header,4)[0]!=124 or struct.unpack_from('<I',header,76)[0]!=32:
        raise ValueError('Invalid DDS header.')
    height,width=struct.unpack_from('<II',header,12)
    if width!=height or width not in {128,256,512,1024}: raise ValueError('Unit component maps must be matching square power-of-two DDS at most1024.')
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


def _component_material(req, h, job, material_name, spec):
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
        width,height=validate_component_dds(header,path.stat().st_size)
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
    topology_before=winding_inventory(mesh)
    for i in ids: mesh.polygons[i].flip()
    for u in mesh.uv_layers:
        for f in mesh.polygons:
            for i in f.loop_indices: u.data[i].uv=corners[u.name][f.index][mesh.loops[i].vertex_index]
    if mesh.has_custom_normals: mesh.normals_split_custom_set([(0,0,0)]*len(mesh.loops))
    mesh.update()
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
    return _finish(req,h,job,source,output,{'operation':'repair_explicit_mesh_winding','mesh':obj.name,'face_indices':ids,'face_indices_sha256':digest(ids),'topology_before':topology_before,'topology_after':topology_after,'positions_preserved':True,'corner_uvs_preserved':True,'rig_weights_actions_materials_preserved':True,'normal_policy':'recompute geometric normals after exact reviewed face flips','status':'repaired_requires_culling_on_visual_and_export_reimport_review'})


def _root_vertical_contact(h,rig,root,meshes,frame,clearance,excluded=()):
    from mathutils import Matrix,Vector
    bpy=h['bpy']; bpy.context.scene.frame_set(frame); bpy.context.view_layer.update()
    if root.parent is not None or rig.constraints or root.constraints:
        raise ValueError('Pure vertical contact requires an unconstrained true skeleton root.')
    original=root.location.copy(); head=rig.matrix_world@root.head
    basis=[]
    for axis in range(3):
        root.location=original; root.location[axis]+=1; bpy.context.view_layer.update()
        basis.append((rig.matrix_world@root.head)-head)
    root.location=original; bpy.context.view_layer.update()
    matrix=Matrix(basis).transposed()
    if abs(matrix.determinant())<1e-10: raise ValueError('Root location world basis is singular.')
    before,maximum=h['evaluated_contact_bounds'](meshes,list(excluded))
    delta=matrix.inverted()@Vector((0,0,clearance-before.z))
    root.location=original+delta
    root.keyframe_insert(data_path='location',frame=frame,group=root.name)
    bpy.context.view_layer.update()
    after,after_max=h['evaluated_contact_bounds'](meshes,list(excluded))
    displacement=(rig.matrix_world@root.head)-head
    if max(abs(displacement.x),abs(displacement.y))>1e-5 or abs(after.z-clearance)>1e-4:
        raise RuntimeError('Root-local correction failed pure world-Z/contact tolerance.')
    return {'frame':frame,'before':before.z,'after':after.z,'root_location_delta':list(delta),'world_displacement':list(displacement),'root_location_world_basis':[list(row) for row in matrix]}


def ground_existing_action(req,h):
    p=req['payload']; job,source,output=_open(req,h); bpy=h['bpy']
    rig=bpy.data.objects.get(p['target_armature_name']); meshes=h['mesh_objects']()
    if h['armatures']()!=[rig] or not meshes: raise ValueError('Require the exact unique working rig and meshes.')
    action=bpy.data.actions.get(p['source_action_name'])
    if action is None or h['_mesh_region_action_hash'](action)!=p['expected_action_sha256'].upper(): raise ValueError('Reviewed source action hash mismatch.')
    name(p['target_action_name'])
    if bpy.data.actions.get(p['target_action_name']): raise ValueError('Grounded action requires a new name.')
    root=rig.pose.bones.get(p['root_bone'])
    if root is None or root.parent is not None: raise ValueError('Require exact true skeleton root.')
    excluded=p.get('excluded_contact_bones',[])
    if not isinstance(excluded,list) or len(excluded)>128 or not set(excluded)<=set(rig.pose.bones.keys()): raise ValueError('Invalid exact contact bone exclusions.')
    kind=action.get('chaosx_animation_source_kind','')
    if kind=='manual_blender_gpt6_astra' and re.fullmatch('[A-Fa-f0-9]{64}',str(action.get('chaosx_manual_action_spec_sha256',''))):
        provenance={'source_kind':kind,'manual_spec_sha256':action['chaosx_manual_action_spec_sha256']}
    elif kind in {'meshy_animate','professional_source'}:
        provenance=h['action_provenance'](action)
    elif rig.get('chaosx_promotion_operation')=='promote_accepted_reimport' and all(obj.get('chaosx_promotion_source_sha256')==rig.get('chaosx_promotion_source_sha256') for obj in meshes):
        provenance={'source_kind':'accepted_recovered_checkpoint','source_sha256':rig['chaosx_promotion_source_sha256'],'validation_sha256':rig['chaosx_promotion_validation_sha256']}
        for relkey,hashkey in [('chaosx_promotion_source','chaosx_promotion_source_sha256'),('chaosx_promotion_validation','chaosx_promotion_validation_sha256')]:
            if h['file_sha256'](h['within'](job,rig[relkey]))!=rig[hashkey]: raise ValueError('Recovered lineage checksum mismatch.')
    else: raise ValueError('No retained reviewed manual/provider/recovered source lineage.')
    if rig.constraints or any(b.constraints for b in rig.pose.bones) or (rig.animation_data and any(not t.mute for t in rig.animation_data.nla_tracks)):
        raise ValueError('Grounding requires unconstrained explicit bone motion without active NLA.')
    before_actions={a.name:h['_mesh_region_action_hash'](a) for a in bpy.data.actions}
    signature=_mesh_signature(meshes)
    corrected=action.copy(); corrected.name=p['target_action_name']; corrected.use_fake_user=True
    rig.animation_data_create(); rig.animation_data.action=corrected
    start,end=map(int,action.frame_range)
    if not 0<=start<end<=start+1200: raise ValueError('Grounding requires a bounded integer action range.')
    path='pose.bones["'+root.name+'"].location'
    def body_keys(a):
        return digest([(c.data_path,c.array_index,[(list(k.co),list(k.handle_left),list(k.handle_right),k.interpolation) for k in c.keyframe_points]) for c,_ in h['action_fcurves'](a) if c.data_path!=path])
    original_body=body_keys(corrected)
    # Densify all root-location channels before changing any value so each
    # sampled original frame retains its own baseline, without accumulated edits.
    samples=[]
    for frame in range(start,end+1):
        bpy.context.scene.frame_set(frame); samples.append((frame,list(root.location)))
    for frame,location in samples:
        root.location=location; root.keyframe_insert(data_path='location',frame=frame,group=root.name)
    frames=[_root_vertical_contact(h,rig,root,meshes,frame,0,excluded) for frame in range(start,end+1)]
    for curve,_ in h['action_fcurves'](corrected):
        if curve.data_path==path:
            for key in curve.keyframe_points: key.interpolation='LINEAR'
    if body_keys(corrected)!=original_body or any(h['_mesh_region_action_hash'](bpy.data.actions[n])!=v for n,v in before_actions.items()) or _mesh_signature(meshes)!=signature:
        raise RuntimeError('Grounding altered original action/body data.')
    corrected['chaosx_grounding_source_action_sha256']=p['expected_action_sha256'].upper()
    corrected['chaosx_grounding_policy']='root_local_pure_world_z'
    bpy.context.scene.frame_set(start)
    return _finish(req,h,job,source,output,{'operation':'ground_existing_action','source_action':action.name,'action':corrected.name,'source_provenance':provenance,'frames':frames,'body_keys_and_original_actions_preserved':True,'native_action_sha256':h['_mesh_region_action_hash'](corrected),'status':'corrected_requires_export_reimport_review'})
