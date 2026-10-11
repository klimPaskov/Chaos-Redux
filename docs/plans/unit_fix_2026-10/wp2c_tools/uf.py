import sys
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import bpy, numpy as np, math
from mathutils import Vector, Matrix, Quaternion
import zv as z, importlib as _il; _il.reload(z)
R = r"<mod root>/"
def jroot(job):
    for fam in ("014_cannibalism", "002_zombie_outbreak", "012_africa"):
        p = R + "docs/assets/%s/models_3d/%s/" % (fam, job)
        import os
        if os.path.isdir(p): return p
    raise KeyError(job)
def open_ck(job, name):
    bpy.ops.wm.open_mainfile(filepath=jroot(job) + "blender/checkpoints/" + name)
def save_ck(job, name):
    bpy.ops.wm.save_as_mainfile(filepath=jroot(job) + "blender/checkpoints/" + name)
def setup(single=True, color=(0.78, 0.74, 0.68)):
    z.setup_world()
    sh = bpy.context.scene.display.shading
    if single:
        sh.color_type = 'SINGLE'; sh.single_color = color
    sh.show_cavity = True; sh.cavity_type = 'BOTH'
def snap(path, objs, view, center, size, res=(600, 600)):
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y = res
    for o in bpy.data.objects:
        if o.type == 'ARMATURE': o.hide_render = True
    z.shot(path, objs, view, center=Vector(center), size=size)
    return path
def wmat(arm): return arm.matrix_world
