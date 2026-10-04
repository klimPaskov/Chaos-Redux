"""Read-only PDX material preview worker (2026-10-04 texture repack evidence).

Launched headless through the repository route:
  python .tools/3d_pipeline/review/review_cli.py blender --script <this file> --config <request.json>
which runs the dependency-locked Blender with --background --factory-startup and the locked
io_pdx_mesh extension. The worker imports one runtime .mesh per job into a disposable scene,
rebinds an approximation of the HOI4 PdxMeshAdvanced (PDX_IMPROVED_BLINN_PHONG) channel decoding,
and renders PNG views. It never saves a .blend and never writes outside the request's out paths.

Channel decoding mirrored from gfx/FX/pdxmesh.shader + standardfuncsgfx.fxh:
  base colour  = diffuse.rgb
  metallic     = 1 - (1 - spec.B)^2                     (MetalnessRemapped)
  specular F0  = spec.G^2 * 0.4  -> Principled "Specular IOR Level" = F0 / 0.08
  roughness    = 1 - spec.A                             (A is glossiness; skill-mandated preview mapping)
  normal       = UnpackRRxGNormal: x = normal.G, y = normal.A (shader negates y to undo the PDX V flip;
                 Blender UVs are already unflipped by the importer, so stored Y is used directly),
                 z = sqrt(saturate(1 - x^2 - y^2))
  normal.B is the shader's EMISSIVE term (applied at night only); day previews ignore it.
Mask mode tints texels where the mask PNG is white, for locating metal regions on the model.
"""
import json
import math
import os
import sys

import bpy
import mathutils

CFG = json.load(open(sys.argv[sys.argv.index("--") + 1], encoding="utf-8"))
BLENDER_DIR = os.path.dirname(bpy.app.binary_path)


def pdx():
    from bl_ext.user_default.io_pdx_mesh.pdx_blender import blender_import_export as m  # noqa: E402
    return m


def clear():
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.armatures, bpy.data.actions, bpy.data.materials,
                 bpy.data.cameras, bpy.data.lights, bpy.data.images):
        for item in list(coll):
            coll.remove(item)


def mesh_objects():
    return [o for o in bpy.data.objects if o.type == "MESH" and not o.name.startswith("CX_")]


def bounds(objs):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in objs:
        ev = o.evaluated_get(dg)
        mw = ev.matrix_world
        pts.extend(mw @ v.co for i, v in enumerate(ev.data.vertices) if i % 5 == 0)
    lo = mathutils.Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = mathutils.Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi


def setup_world():
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x, sc.render.resolution_y = CFG.get("res", [640, 880])
    sc.view_settings.view_transform = "Standard"
    world = bpy.data.worlds.new("CX_World")
    sc.world = world
    world.use_nodes = True
    nt = world.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputWorld")
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    env.image = bpy.data.images.load(os.path.join(BLENDER_DIR, bpy.app.version_string.rsplit(".", 1)[0],
                                                  "datafiles", "studiolights", "world", CFG.get("hdri", "sunrise.exr")))
    bg_env = nt.nodes.new("ShaderNodeBackground")
    bg_env.inputs[1].default_value = CFG.get("env_strength", 0.9)
    bg_cam = nt.nodes.new("ShaderNodeBackground")
    bg_cam.inputs[0].default_value = (*CFG.get("backdrop", (0.42, 0.44, 0.40)), 1)
    lp = nt.nodes.new("ShaderNodeLightPath")
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(env.outputs[0], bg_env.inputs[0])
    nt.links.new(lp.outputs["Is Camera Ray"], mix.inputs[0])
    nt.links.new(bg_env.outputs[0], mix.inputs[1])
    nt.links.new(bg_cam.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    sun = bpy.data.lights.new("CX_sun", "SUN")
    sun.energy = CFG.get("sun", 3.0)
    obj = bpy.data.objects.new("CX_sun", sun)
    sc.collection.objects.link(obj)
    obj.rotation_euler = (-mathutils.Vector((-0.45, -0.6, 0.9))).to_track_quat("-Z", "Y").to_euler()
    cam = bpy.data.objects.new("CX_Camera", bpy.data.cameras.new("CX_Camera"))
    sc.collection.objects.link(cam)
    cam.data.type = "ORTHO"
    sc.camera = cam
    return cam


def shoot(cam, objs, direction, path, margin=1.10):
    lo, hi = bounds(objs)
    c = (lo + hi) / 2
    ext = max((hi - lo).length, 1e-3)
    d = mathutils.Vector(direction).normalized()
    cam.location = c + d * ext * 4
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    cam.data.ortho_scale = ext * margin
    cam.data.clip_start, cam.data.clip_end = ext * 0.01, ext * 20
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)


def load(path, non_color):
    img = bpy.data.images.load(path)
    if non_color:
        img.colorspace_settings.name = "Non-Color"
        img.alpha_mode = "CHANNEL_PACKED"  # A is glossiness / normal Y, never opacity
    return img


def bind(objs, job):
    """Bind job textures; job["per_object"] maps an object-name prefix to its own texture set."""
    for prefix, tex in job.get("per_object", {}).items():
        bind_set([o for o in objs if o.name.startswith(prefix)], {**job, **tex})
    claimed = tuple(job.get("per_object", {}))
    bind_set([o for o in objs if not (claimed and o.name.startswith(claimed))], job)


def bind_set(objs, job):
    if not objs:
        return
    dif = load(job["diffuse"], False)
    spec = load(job["specular"], True) if job.get("specular") else None
    nrm = load(job["normal"], True) if job.get("normal") else None
    mask = load(job["mask"], True) if job.get("mask") else None
    for o in objs:
        uv = o.data.uv_layers.active.name if o.data.uv_layers else ""
        for i, slot in enumerate(o.material_slots):
            m = bpy.data.materials.new(f"CX_pdx_{o.name}_{i}")
            m.use_nodes = True
            slot.material = m
            nt = m.node_tree
            for n in list(nt.nodes):
                nt.nodes.remove(n)
            L = nt.links.new
            out = nt.nodes.new("ShaderNodeOutputMaterial")
            bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
            L(bsdf.outputs[0], out.inputs[0])
            tex_d = nt.nodes.new("ShaderNodeTexImage")
            tex_d.image = dif
            base = tex_d.outputs[0]
            if mask is not None:
                tex_m = nt.nodes.new("ShaderNodeTexImage")
                tex_m.image = mask
                mixc = nt.nodes.new("ShaderNodeMix")
                mixc.data_type = "RGBA"
                mixc.inputs["B"].default_value = (1.0, 0.05, 0.6, 1)
                L(tex_m.outputs[0], mixc.inputs["Factor"])
                L(base, mixc.inputs["A"])
                base = mixc.outputs["Result"]
            L(base, bsdf.inputs["Base Color"])
            if spec is None:
                bsdf.inputs["Roughness"].default_value = 0.8
                continue
            tex_s = nt.nodes.new("ShaderNodeTexImage")
            tex_s.image = spec
            sep = nt.nodes.new("ShaderNodeSeparateColor")
            L(tex_s.outputs["Color"], sep.inputs[0])

            def math_node(op, a=None, b=None, c=None, clamp=False):
                """Math node; each operand is a socket to link or a float default."""
                n = nt.nodes.new("ShaderNodeMath")
                n.operation = op
                n.use_clamp = clamp
                for idx, arg in enumerate((a, b, c)):
                    if arg is None:
                        continue
                    if isinstance(arg, (int, float)):
                        n.inputs[idx].default_value = float(arg)
                    else:
                        L(arg, n.inputs[idx])
                return n.outputs[0]

            # metallic = 1 - (1 - B)^2
            one_minus_b = math_node("SUBTRACT", 1.0, sep.outputs["Blue"])
            L(math_node("SUBTRACT", 1.0, math_node("MULTIPLY", one_minus_b, one_minus_b)), bsdf.inputs["Metallic"])
            # specular IOR level = G^2 * 0.4 / 0.08 = G^2 * 5
            g2 = math_node("MULTIPLY", sep.outputs["Green"], sep.outputs["Green"])
            L(math_node("MULTIPLY", g2, 5.0), bsdf.inputs["Specular IOR Level"])
            # roughness = 1 - A
            L(math_node("SUBTRACT", 1.0, tex_s.outputs["Alpha"]), bsdf.inputs["Roughness"])
            if nrm is not None:
                tex_n = nt.nodes.new("ShaderNodeTexImage")
                tex_n.image = nrm
                sepn = nt.nodes.new("ShaderNodeSeparateColor")
                L(tex_n.outputs["Color"], sepn.inputs[0])
                chans = {"R": sepn.outputs["Red"], "G": sepn.outputs["Green"], "B": sepn.outputs["Blue"],
                         "A": tex_n.outputs["Alpha"]}
                decode = job.get("decode", "GA")
                x = math_node("MULTIPLY_ADD", chans[decode[0]], 2.0, -1.0)
                y = math_node("MULTIPLY_ADD", chans[decode[1]], 2.0, -1.0)
                s = math_node("ADD", math_node("MULTIPLY", x, x), math_node("MULTIPLY", y, y))
                z = math_node("SQRT", math_node("SUBTRACT", 1.0, s, clamp=True))
                comb = nt.nodes.new("ShaderNodeCombineXYZ")
                L(x, comb.inputs[0])
                L(y, comb.inputs[1])
                L(z, comb.inputs[2])
                # Normal Map node expects colour-encoded tangent normals.
                enc = nt.nodes.new("ShaderNodeVectorMath")
                enc.operation = "MULTIPLY_ADD"
                enc.inputs[1].default_value = (0.5, 0.5, 0.5)
                enc.inputs[2].default_value = (0.5, 0.5, 0.5)
                L(comb.outputs[0], enc.inputs[0])
                nmap = nt.nodes.new("ShaderNodeNormalMap")
                nmap.space = "TANGENT"
                nmap.uv_map = uv
                L(enc.outputs[0], nmap.inputs["Color"])
                L(nmap.outputs[0], bsdf.inputs["Normal"])


def dump_faces(objs, path):
    """Write rest-pose world triangle positions and UVs (u, v with v up) for host-side UV masking."""
    import numpy as np
    pos, uvs = [], []
    for o in objs:
        me = o.data
        me.calc_loop_triangles()
        uvl = me.uv_layers.active.data
        mw = o.matrix_world
        for t in me.loop_triangles:
            pos.append([tuple(mw @ me.vertices[v].co) for v in t.vertices])
            uvs.append([tuple(uvl[li].uv) for li in t.loops])
    np.savez(path, pos=np.array(pos, dtype=np.float64), uv=np.array(uvs, dtype=np.float64))


def main():
    report = []
    for job in CFG["jobs"]:
        clear()
        pdx().import_meshfile(job["mesh"], imp_mesh=True, imp_skel=True, imp_locs=False, join_materials=True, bonespace=False)
        objs = mesh_objects()
        if job.get("dump"):
            dump_faces(objs, job["dump"])
            if not job.get("diffuse"):
                continue
        cam = setup_world()
        bind(objs, job)
        os.makedirs(os.path.dirname(job["out_prefix"]), exist_ok=True)
        for name, d in CFG.get("views", {"front": [0, -1, 0.15], "three_quarter": [0.65, -0.75, 0.35]}).items():
            shoot(cam, objs, d, f"{job['out_prefix']}__{name}.png")
        tris = sum(sum(len(p.vertices) - 2 for p in o.data.polygons) for o in objs)
        report.append({"tag": job["out_prefix"], "objects": [o.name for o in objs], "tris": tris,
                       "uv": [o.data.uv_layers.active.name if o.data.uv_layers else None for o in objs]})
        print("FINAL", json.dumps(report[-1]))
    if CFG.get("report"):
        json.dump({"blender": bpy.app.version_string, "build": bpy.app.build_hash.decode(), "jobs": report},
                  open(CFG["report"], "w", encoding="utf-8"), indent=1)


main()
