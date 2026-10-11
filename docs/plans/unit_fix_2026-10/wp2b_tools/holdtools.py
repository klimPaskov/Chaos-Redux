import bpy, numpy as np, math
from mathutils import Matrix, Vector, Quaternion
import sys; sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import zv as z

def pbm(arm, name): return arm.matrix_world @ arm.pose.bones[name].matrix
def head(arm, name): return pbm(arm, name).translation
def rot3(arm, name): return pbm(arm, name).to_quaternion().to_matrix()

def set_rest(arm, on):
    arm.data.pose_position = 'REST' if on else 'POSE'
    bpy.context.view_layer.update()

def hand_centroid(arm, body, bone, thr=0.5):
    """World centroid of body vertices whose weight on `bone` is >= thr at the current evaluated pose, and that centroid in the bone frame."""
    gi = body.vertex_groups[bone].index
    idx = [v.index for v in body.data.vertices if any(g.group == gi and g.weight >= thr for g in v.groups)]
    dg = bpy.context.evaluated_depsgraph_get(); eo = body.evaluated_get(dg); me = eo.to_mesh()
    co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
    M = np.array(body.matrix_world); wc = co[idx] @ M[:3, :3].T + M[:3, 3]
    eo.to_mesh_clear()
    c = Vector(wc.mean(0))
    h = head(arm, bone); R = rot3(arm, bone)
    return c, R.inverted() @ (c - h), wc

def item_points(arm, item, bone, local_pts=None):
    """item vertices (sampled) in the bone frame, computed at the current evaluated pose of the item mesh (rigid on one bone)."""
    me = item.data
    co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); return co.reshape(-1, 3)

def solve_arm(arm, upper, fore, hand, target_palm, palm_off, iters=5, pole=None):
    """Two-bone reach: rotate `upper` and `fore` (about their heads) so the palm point (hand frame offset palm_off) lands on target_palm.
    Joint positions come from the child bone heads, so Meshy bone tails (meaningless lengths) are not used. Returns the residual distance."""
    for it in range(iters):
        S = head(arm, upper); E = head(arm, fore); W = head(arm, hand)
        P = W + rot3(arm, hand) @ Vector(palm_off)
        err = target_palm - P
        if err.length < 1e-3: break
        Wt = W + err
        L1 = (E - S).length; L2 = (W - E).length
        v = Wt - S; dist = v.length; u = v / dist
        d = min(max(dist, abs(L1 - L2) + 1e-3), L1 + L2 - 1e-3)
        a = (d * d + L1 * L1 - L2 * L2) / (2 * d); h = math.sqrt(max(L1 * L1 - a * a, 0.0))
        n = (E - S) - u * ((E - S).dot(u))
        if pole is not None: n = Vector(pole) - u * Vector(pole).dot(u)
        if n.length < 1e-4: n = Vector((0, 0, 1)) - u * u.z
        n.normalize()
        Enew = S + u * a + n * h
        Wnew = S + u * d
        rot_bone(arm, upper, S, (E - S), (Enew - S))
        E2 = head(arm, fore); W2 = head(arm, hand)
        rot_bone(arm, fore, E2, (W2 - E2), (Wnew - E2))
    S = head(arm, upper); W = head(arm, hand)
    P = W + rot3(arm, hand) @ Vector(palm_off)
    return (target_palm - P).length

def rot_bone(arm, name, pivot, cur, goal):
    q = cur.normalized().rotation_difference(goal.normalized())
    pb = arm.pose.bones[name]
    world = arm.matrix_world @ pb.matrix
    turned = Matrix.Translation(pivot) @ q.to_matrix().to_4x4() @ Matrix.Translation(-pivot) @ world
    pb.matrix = arm.matrix_world.inverted() @ turned
    bpy.context.view_layer.update()

def key_bones(arm, names, frame):
    for n in names:
        pb = arm.pose.bones[n]
        pb.keyframe_insert('rotation_quaternion', frame=frame)
