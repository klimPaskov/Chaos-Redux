"""Authored key tables for the eight rat actions (2026-10-03 repair).

Every number below was chosen by the agent from rest and pose renders of this rig; nothing is
generated. A key lists the bones it changes; `pose()` fills the remaining animated bones with the
hunched base values so every animated bone is keyed at every key frame (an unkeyed bone would leak
the previous action's pose in game). Running this file writes rat_actions_authored.json with the
fully expanded explicit tables that the live Lab session authors and bakes.

Conventions (see rlab.key_pose): fk values are [rx, ry, rz] degrees about the rest-world axes
(X = rat's left, Y = backward, Z = up; the rat faces -Y), relative to the parent bone. +rx tilts an
upward bone forward and swings a hanging bone backward. hips = root offset from rest (world units).
footL/footR = ankle target offset and rotation from rest (+rx lifts the heel). tail = tail-tip IK
target offset from its rest point. 30 fps.
"""
import copy
import json
import os

BASE = {
    "Hips": [8, 0, 0], "Spine02": [6, 0, 0], "Spine01": [6, 0, 0], "Spine": [5, 0, 0],
    "neck": [-14, 0, 0], "Head": [-12, 0, 0], "Jaw_1": [0, 0, 0],
    "LeftShoulder": [0, 0, 0], "LeftArm": [-30, 10, 0], "LeftForeArm": [-25, 0, 0], "LeftHand": [-10, 0, 0],
    "RightShoulder": [0, 0, 0], "RightArm": [-30, -10, 0], "RightForeArm": [-25, 0, 0], "RightHand": [-10, 0, 0],
    "LeftToeBase": [0, 0, 0], "RightToeBase": [0, 0, 0],
    "Tail_1": [25, 0, 0], "Tail_2": [10, 0, -8], "Tail_3": [5, 0, -8], "Tail_4": [0, 0, -6],
}
BASE_HIPS = [0, 0.10, -0.35]


def pose(hips=None, footL=None, footR=None, tail=None, **fk):
    k = {"hips": hips or BASE_HIPS, "fk": copy.deepcopy(BASE),
         "footL": footL or {"loc": [0, 0, 0], "rot": [0, 0, 0]},
         "footR": footR or {"loc": [0, 0, 0], "rot": [0, 0, 0]},
         "tail": tail or [0, 0, 0]}
    k["fk"].update(fk)
    return k


def foot(loc, rot=(0, 0, 0)):
    return {"loc": list(loc), "rot": list(rot)}


IDLE_START = pose()

ACTIONS = {}

# IDLE: hunched breathing with a heaving chest and shoulders (inhale 23 and 68), sniffing bursts
# with the snout raised and jaw twitching (12-20, 52-60), a slow look around to the left (34-45)
# and right (52-80), claws flexing, weight shifting foot to foot, the tail sweeping side to side.
# Loop 1-91.
ACTIONS["idle"] = {"frames": [1, 91], "loop": True, "keys": {
    1: IDLE_START,
    12: pose(hips=[0.04, 0.10, -0.30], Spine02=[4, 0, 2], Spine=[1, 0, 2], neck=[-20, 0, 6], Head=[-22, 0, 8], Jaw_1=[6, 0, 0],
             LeftHand=[-22, 0, 0], LeftForeArm=[-32, 0, 0], Tail_2=[10, 0, 2], Tail_3=[5, 0, 4], Tail_4=[0, 0, 4], tail=[-0.35, 0.25, 0]),
    16: pose(hips=[0.06, 0.10, -0.29], Spine02=[4, 0, 2], Spine=[1, 0, 2], neck=[-16, 0, 6], Head=[-12, 0, 8], Jaw_1=[0, 0, 0],
             LeftHand=[-22, 0, 0], LeftForeArm=[-32, 0, 0], Tail_2=[10, 0, 6], Tail_3=[5, 0, 7], Tail_4=[0, 0, 6], tail=[-0.5, 0.35, 0]),
    19: pose(hips=[0.07, 0.10, -0.28], Spine02=[3, 0, 2], Spine=[0, 0, 2], neck=[-21, 0, 7], Head=[-24, 0, 9], Jaw_1=[7, 0, 0],
             LeftHand=[-16, 0, 0], LeftForeArm=[-30, 0, 0], Tail_2=[11, 0, 9], Tail_3=[5, 0, 10], Tail_4=[1, 0, 8], tail=[-0.65, 0.45, 0]),
    23: pose(hips=[0.08, 0.10, -0.25], Spine02=[2, 0, 2], Spine01=[2, 0, 0], Spine=[-1, 0, 2], LeftShoulder=[0, -9, 0], RightShoulder=[0, 9, 0],
             neck=[-17, 0, 8], Head=[-15, 0, 10], LeftArm=[-33, 6, 0], RightArm=[-33, -6, 0], Jaw_1=[2, 0, 0],
             Tail_2=[12, 0, 12], Tail_3=[6, 0, 12], Tail_4=[2, 0, 10], tail=[-0.8, 0.5, 0]),
    34: pose(hips=[0.06, 0.10, -0.32], Spine=[4, 0, 8], neck=[-14, 0, 24], Head=[-12, 0, 26], LeftArm=[-36, 10, 6], RightArm=[-26, -10, 0],
             RightForeArm=[-35, 0, 0], RightHand=[-22, 0, 0], Tail_2=[10, 0, 14], Tail_3=[5, 0, 14], Tail_4=[0, 0, 12], tail=[-0.9, 0.45, 0]),
    45: pose(hips=[0.02, 0.10, -0.38], Spine02=[7, 0, 0], Spine01=[7, 0, 0], Spine=[6, 0, 6], neck=[-14, 0, 20], Head=[-12, 0, 20],
             LeftShoulder=[0, 3, 0], RightShoulder=[0, -3, 0], Tail_2=[10, 0, 6], Tail_3=[5, 0, 4], Tail_4=[0, 0, 0], tail=[-0.5, 0.25, 0]),
    52: pose(hips=[-0.04, 0.10, -0.31], Spine02=[4, 0, -2], Spine=[1, 0, -2], neck=[-20, 0, -8], Head=[-23, 0, -12], Jaw_1=[6, 0, 0],
             RightHand=[-24, 0, 0], RightForeArm=[-32, 0, 0], Tail_2=[10, 0, 0], Tail_3=[5, 0, -2], Tail_4=[0, 0, -2], tail=[-0.2, 0.15, 0]),
    56: pose(hips=[-0.06, 0.10, -0.29], Spine02=[4, 0, -2], Spine=[1, 0, -2], neck=[-16, 0, -10], Head=[-12, 0, -14], Jaw_1=[0, 0, 0],
             RightHand=[-24, 0, 0], RightForeArm=[-32, 0, 0], Tail_2=[10, 0, -4], Tail_3=[5, 0, -6], Tail_4=[0, 0, -5], tail=[0.05, 0.1, 0]),
    60: pose(hips=[-0.07, 0.10, -0.28], Spine02=[3, 0, -2], Spine=[0, 0, -2], neck=[-21, 0, -12], Head=[-24, 0, -16], Jaw_1=[7, 0, 0],
             RightHand=[-16, 0, 0], RightForeArm=[-30, 0, 0], Tail_2=[10, 0, -8], Tail_3=[5, 0, -10], Tail_4=[0, 0, -8], tail=[0.25, 0.05, 0]),
    68: pose(hips=[-0.08, 0.10, -0.25], Spine02=[2, 0, -2], Spine01=[2, 0, 0], Spine=[-1, 0, -4], LeftShoulder=[0, -9, 0], RightShoulder=[0, 9, 0],
             neck=[-15, 0, -24], Head=[-13, 0, -26], LeftArm=[-33, 6, 0], RightArm=[-33, -6, 0], Jaw_1=[2, 0, 0],
             Tail_2=[10, 0, -12], Tail_3=[5, 0, -13], Tail_4=[0, 0, -11], tail=[0.4, 0.0, 0]),
    80: pose(hips=[-0.04, 0.10, -0.34], Spine=[4, 0, -5], neck=[-14, 0, -10], Head=[-12, 0, -12], LeftArm=[-26, 10, 0], RightArm=[-36, -10, -6],
             LeftForeArm=[-35, 0, 0], LeftHand=[-22, 0, 0], Tail_2=[10, 0, -10], Tail_3=[5, 0, -10], Tail_4=[0, 0, -8], tail=[0.2, 0.0, 0]),
    91: IDLE_START,
}}


def move_hips(z, x=0.0):
    return [x, 0.15, z]


# MOVE: hunched loping walk in place, two strides per 1 s loop (1-31): heel strike, mid-stance,
# toe-off, high swing; pelvis bob and yaw with a counter-twisting chest, arms swinging opposite
# the legs with claws out, the tail streaming behind and swinging against the pelvis.
MV = dict(Spine02=[10, 0, 0], Spine01=[8, 0, 0], Spine=[6, 0, 0], neck=[-20, 0, 0], Head=[-14, 0, 0], Tail_1=[55, 0, 0])
ACTIONS["move"] = {"frames": [1, 31], "loop": True, "keys": {
    1: pose(hips=move_hips(-0.62), footL=foot([0, -0.9, 0.12], [-10, 0, 0]), footR=foot([0, 0.9, 0.45], [30, 0, 0]), tail=[-1.3, 2.3, 0.4],
            **dict(MV, Hips=[14, 0, -6], Spine02=[10, 0, 3], Spine01=[8, 0, 3], Spine=[6, 0, 2],
                   LeftArm=[10, 10, 0], LeftForeArm=[-45, 0, 0], RightArm=[-55, -10, 0], RightForeArm=[-30, 0, 0],
                   RightToeBase=[-30, 0, 0], Tail_2=[12, 0, 4], Tail_3=[6, 0, 4], Tail_4=[3, 0, 2])),
    5: pose(hips=move_hips(-0.50, 0.04), footL=foot([0, -0.45, 0.04], [-4, 0, 0]), footR=foot([0, 0.7, 0.65], [20, 0, 0]), tail=[-1.05, 2.3, 0.45],
            **dict(MV, Hips=[14, 2, -3], Spine02=[10, 0, 1], Spine01=[8, 0, 1], Spine=[6, 0, 1],
                   LeftArm=[0, 10, 0], LeftForeArm=[-40, 0, 0], RightArm=[-40, -10, 0], RightForeArm=[-35, 0, 0],
                   RightToeBase=[-10, 0, 0], Tail_2=[12, 0, 9], Tail_3=[6, 0, 8], Tail_4=[3, 0, 6])),
    9: pose(hips=move_hips(-0.40, 0.08), footL=foot([0, 0.0, 0], [0, 0, 0]), footR=foot([0, 0.0, 0.75], [5, 0, 0]), tail=[-0.8, 2.3, 0.5],
            **dict(MV, Hips=[14, 3, 0], Head=[-16, 0, 0], LeftArm=[-20, 10, 0], LeftForeArm=[-35, 0, 0], RightArm=[-20, -10, 0], RightForeArm=[-40, 0, 0],
                   Tail_2=[12, 0, 12], Tail_3=[6, 0, 10], Tail_4=[3, 0, 8])),
    13: pose(hips=move_hips(-0.50, 0.04), footL=foot([0, 0.45, 0], [0, 0, 0]), footR=foot([0, -0.75, 0.35], [-20, 0, 0]), tail=[-1.05, 2.3, 0.45],
             **dict(MV, Hips=[14, 2, 3], Spine02=[10, 0, -1], Spine01=[8, 0, -1], Spine=[6, 0, -1],
                    LeftArm=[-40, 10, 0], LeftForeArm=[-35, 0, 0], RightArm=[0, -10, 0], RightForeArm=[-40, 0, 0],
                    Tail_2=[12, 0, 9], Tail_3=[6, 0, 8], Tail_4=[3, 0, 6])),
    16: pose(hips=move_hips(-0.62), footL=foot([0, 0.9, 0.45], [30, 0, 0]), footR=foot([0, -0.9, 0.12], [-10, 0, 0]), tail=[-1.3, 2.3, 0.4],
             **dict(MV, Hips=[14, 0, 6], Spine02=[10, 0, -3], Spine01=[8, 0, -3], Spine=[6, 0, -2],
                    LeftArm=[-55, 10, 0], LeftForeArm=[-30, 0, 0], RightArm=[10, -10, 0], RightForeArm=[-45, 0, 0],
                    LeftToeBase=[-30, 0, 0], Tail_2=[12, 0, -4], Tail_3=[6, 0, -4], Tail_4=[3, 0, -2])),
    20: pose(hips=move_hips(-0.50, -0.04), footL=foot([0, 0.7, 0.65], [20, 0, 0]), footR=foot([0, -0.45, 0.04], [-4, 0, 0]), tail=[-1.55, 2.3, 0.45],
             **dict(MV, Hips=[14, -2, 3], Spine02=[10, 0, -1], Spine01=[8, 0, -1], Spine=[6, 0, -1],
                    LeftArm=[-40, 10, 0], LeftForeArm=[-35, 0, 0], RightArm=[0, -10, 0], RightForeArm=[-40, 0, 0],
                    LeftToeBase=[-10, 0, 0], Tail_2=[12, 0, -9], Tail_3=[6, 0, -8], Tail_4=[3, 0, -6])),
    24: pose(hips=move_hips(-0.40, -0.08), footL=foot([0, 0.0, 0.75], [5, 0, 0]), footR=foot([0, 0.0, 0], [0, 0, 0]), tail=[-1.8, 2.3, 0.5],
             **dict(MV, Hips=[14, -3, 0], Head=[-16, 0, 0], LeftArm=[-20, 10, 0], LeftForeArm=[-40, 0, 0], RightArm=[-20, -10, 0], RightForeArm=[-35, 0, 0],
                    Tail_2=[12, 0, -12], Tail_3=[6, 0, -10], Tail_4=[3, 0, -8])),
    28: pose(hips=move_hips(-0.50, -0.04), footL=foot([0, -0.75, 0.35], [-20, 0, 0]), footR=foot([0, 0.45, 0], [0, 0, 0]), tail=[-1.55, 2.3, 0.45],
             **dict(MV, Hips=[14, -2, -3], Spine02=[10, 0, 1], Spine01=[8, 0, 1], Spine=[6, 0, 1],
                    LeftArm=[0, 10, 0], LeftForeArm=[-40, 0, 0], RightArm=[-40, -10, 0], RightForeArm=[-35, 0, 0],
                    Tail_2=[12, 0, -9], Tail_3=[6, 0, -8], Tail_4=[3, 0, -6])),
}}
ACTIONS["move"]["keys"][31] = copy.deepcopy(ACTIONS["move"]["keys"][1])


# RETREAT: a low, quick scurry (0.8 s loop, 1-25) that keeps glancing back over its left
# shoulder, forearms drawn up to the chest, shorter steps, the tail dragging low on the ground.
RT = dict(Spine02=[12, 0, 4], Spine01=[10, 0, 4], Spine=[8, 0, 2], neck=[-18, 0, 22], Head=[-16, 0, 26],
          LeftArm=[-25, 18, 0], LeftForeArm=[-80, 0, 0], LeftHand=[-20, 0, 0], RightArm=[-25, -18, 0], RightForeArm=[-80, 0, 0], RightHand=[-20, 0, 0],
          Tail_1=[18, 0, 0], Jaw_1=[6, 0, 0])


def rt_hips(z, x=0.0):
    return [x, 0.25, z]


ACTIONS["retreat"] = {"frames": [1, 25], "loop": True, "keys": {
    1: pose(hips=rt_hips(-0.85), footL=foot([0, -0.7, 0.1], [-8, 0, 0]), footR=foot([0, 0.7, 0.4], [25, 0, 0]), tail=[-0.9, 1.5, 0.0],
            **dict(RT, Hips=[22, 0, -5], RightToeBase=[-25, 0, 0], Tail_2=[8, 0, 6], Tail_3=[4, 0, 6], Tail_4=[0, 0, 4], LeftArm=[-30, 18, 0], RightArm=[-18, -18, 0])),
    4: pose(hips=rt_hips(-0.76, 0.03), footL=foot([0, -0.35, 0], [-3, 0, 0]), footR=foot([0, 0.5, 0.55], [18, 0, 0]), tail=[-0.7, 1.5, 0.0],
            **dict(RT, Hips=[22, 2, -2], RightToeBase=[-10, 0, 0], Tail_2=[8, 0, 9], Tail_3=[4, 0, 8], Tail_4=[0, 0, 6])),
    7: pose(hips=rt_hips(-0.70, 0.06), footL=foot([0, 0.0, 0], [0, 0, 0]), footR=foot([0, 0.0, 0.55], [5, 0, 0]), tail=[-0.5, 1.5, 0.0],
            **dict(RT, Hips=[22, 3, 0], Head=[-18, 0, 30], Tail_2=[8, 0, 10], Tail_3=[4, 0, 9], Tail_4=[0, 0, 7])),
    10: pose(hips=rt_hips(-0.76, 0.03), footL=foot([0, 0.35, 0], [0, 0, 0]), footR=foot([0, -0.55, 0.25], [-15, 0, 0]), tail=[-0.7, 1.5, 0.0],
             **dict(RT, Hips=[22, 2, 2], Tail_2=[8, 0, 7], Tail_3=[4, 0, 6], Tail_4=[0, 0, 4])),
    13: pose(hips=rt_hips(-0.85), footL=foot([0, 0.7, 0.4], [25, 0, 0]), footR=foot([0, -0.7, 0.1], [-8, 0, 0]), tail=[-0.9, 1.5, 0.0],
             **dict(RT, Hips=[22, 0, 5], LeftToeBase=[-25, 0, 0], neck=[-18, 0, 18], Head=[-16, 0, 20], Tail_2=[8, 0, -4], Tail_3=[4, 0, -4], Tail_4=[0, 0, -2],
                    LeftArm=[-18, 18, 0], RightArm=[-30, -18, 0])),
    16: pose(hips=rt_hips(-0.76, -0.03), footL=foot([0, 0.5, 0.55], [18, 0, 0]), footR=foot([0, -0.35, 0], [-3, 0, 0]), tail=[-1.1, 1.5, 0.0],
             **dict(RT, Hips=[22, -2, 2], LeftToeBase=[-10, 0, 0], neck=[-18, 0, 20], Head=[-16, 0, 24], Tail_2=[8, 0, -8], Tail_3=[4, 0, -7], Tail_4=[0, 0, -5])),
    19: pose(hips=rt_hips(-0.70, -0.06), footL=foot([0, 0.0, 0.55], [5, 0, 0]), footR=foot([0, 0.0, 0], [0, 0, 0]), tail=[-1.3, 1.5, 0.0],
             **dict(RT, Hips=[22, -3, 0], Head=[-18, 0, 30], Tail_2=[8, 0, -9], Tail_3=[4, 0, -8], Tail_4=[0, 0, -6])),
    22: pose(hips=rt_hips(-0.76, -0.03), footL=foot([0, -0.55, 0.25], [-15, 0, 0]), footR=foot([0, 0.35, 0], [0, 0, 0]), tail=[-1.1, 1.5, 0.0],
             **dict(RT, Hips=[22, -2, -2], Tail_2=[8, 0, 2], Tail_3=[4, 0, 2], Tail_4=[0, 0, 1])),
}}
ACTIONS["retreat"]["keys"][25] = copy.deepcopy(ACTIONS["retreat"]["keys"][1])


# ATTACK: wind-up with the right claw raised high and out to the side as the body twists away
# (10, peak 16), lunge on a forward step raking the right claw down and across (20), head thrust
# and bite (jaw open 25, snapped shut 28) while the left claw winds across the chest, left-claw
# backhand outward (34), recover and step back into the idle stance (42-61).
ACTIONS["attack"] = {"frames": [1, 61], "loop": False, "keys": {
    1: IDLE_START,
    10: pose(hips=[0, 0.35, -0.75], footR=foot([0, 0.3, 0]), tail=[-0.8, 1.5, 0.3],
             Hips=[6, 0, -18], Spine02=[4, 0, -6], Spine01=[4, 0, -6], Spine=[2, 0, -4], neck=[-8, 0, 8], Head=[-14, 0, 8], Jaw_1=[8, 0, 0],
             RightArm=[-45, 70, 0], RightForeArm=[-95, 0, 0], RightHand=[-20, 0, 0], LeftArm=[-50, 15, 0], LeftForeArm=[-40, 0, 0],
             Tail_1=[40, 0, 0], Tail_2=[15, 0, 15], Tail_3=[8, 0, 10], Tail_4=[3, 0, 6]),
    16: pose(hips=[0, 0.42, -0.82], footR=foot([0, 0.3, 0]), tail=[-1.0, 1.5, 0.35],
             Hips=[4, 0, -22], Spine02=[2, 0, -8], Spine01=[2, 0, -8], Spine=[0, 0, -6], neck=[-10, 0, 10], Head=[-14, 0, 10], Jaw_1=[14, 0, 0],
             RightArm=[-60, 85, 10], RightForeArm=[-100, 0, 0], RightHand=[-25, 0, 0], LeftArm=[-55, 15, 0], LeftForeArm=[-45, 0, 0],
             Tail_1=[45, 0, 0], Tail_2=[16, 0, 18], Tail_3=[8, 0, 12], Tail_4=[3, 0, 8]),
    20: pose(hips=[0, -0.55, -0.85], footL=foot([0, -0.9, 0.08], [-8, 0, 0]), footR=foot([0, 0.45, 0.25], [15, 0, 0]), tail=[0.4, 1.4, 0.2],
             Hips=[22, 0, 10], Spine02=[10, 0, 6], Spine01=[10, 0, 6], Spine=[8, 0, 4], neck=[-16, 0, -4], Head=[-10, 0, -4], Jaw_1=[10, 0, 0],
             RightArm=[-75, 0, 30], RightForeArm=[-10, 0, 0], RightHand=[-20, 0, 0], LeftArm=[-25, 10, 0], LeftForeArm=[-60, 0, 0],
             RightToeBase=[-15, 0, 0], Tail_1=[40, 0, 0], Tail_2=[15, 0, -18], Tail_3=[8, 0, -12], Tail_4=[3, 0, -8]),
    25: pose(hips=[0, -0.75, -0.95], footL=foot([0, -0.9, 0.08], [-8, 0, 0]), footR=foot([0, 0.45, 0.25], [15, 0, 0]), tail=[0.3, 1.4, 0.15],
             Hips=[24, 0, 6], Spine02=[10, 0, 4], Spine01=[10, 0, 4], Spine=[12, 0, 0], neck=[-2, 0, 0], Head=[6, 0, 0], Jaw_1=[28, 0, 0],
             RightArm=[-50, 0, 40], RightForeArm=[-20, 0, 0], RightHand=[-20, 0, 0], LeftArm=[-45, 0, -25], LeftForeArm=[-70, 0, 0],
             RightToeBase=[-15, 0, 0], Tail_1=[38, 0, 0], Tail_2=[15, 0, -14], Tail_3=[8, 0, -10], Tail_4=[3, 0, -6]),
    28: pose(hips=[0, -0.75, -0.95], footL=foot([0, -0.9, 0.08], [-8, 0, 0]), footR=foot([0, 0.45, 0.25], [15, 0, 0]), tail=[0.1, 1.4, 0.15],
             Hips=[24, 0, 4], Spine02=[10, 0, 0], Spine01=[10, 0, 0], Spine=[12, 0, 2], neck=[0, 0, 0], Head=[10, 0, 0], Jaw_1=[0, 0, 0],
             RightArm=[-40, 0, 25], RightForeArm=[-40, 0, 0], RightHand=[-15, 0, 0], LeftArm=[-55, 0, -45], LeftForeArm=[-85, 0, 0], LeftHand=[-15, 0, 0],
             RightToeBase=[-15, 0, 0], Tail_1=[38, 0, 0], Tail_2=[15, 0, -6], Tail_3=[8, 0, -4], Tail_4=[3, 0, -2]),
    34: pose(hips=[0, -0.65, -0.9], footL=foot([0, -0.9, 0.08], [-8, 0, 0]), footR=foot([0, 0.45, 0.25], [15, 0, 0]), tail=[-0.6, 1.3, 0.2],
             Hips=[20, 0, -10], Spine02=[10, 0, -8], Spine01=[10, 0, -8], Spine=[10, 0, -6], neck=[-6, 0, 4], Head=[0, 0, 6], Jaw_1=[12, 0, 0],
             LeftArm=[-75, 0, 50], LeftForeArm=[-20, 0, 0], LeftHand=[-25, 0, 0], RightArm=[-30, -10, 0], RightForeArm=[-60, 0, 0],
             RightToeBase=[-15, 0, 0], Tail_1=[40, 0, 0], Tail_2=[15, 0, 18], Tail_3=[8, 0, 12], Tail_4=[3, 0, 8]),
    42: pose(hips=[0, -0.2, -0.6], footL=foot([0, -0.5, 0.25], [-5, 0, 0]), footR=foot([0, 0.2, 0.15], [5, 0, 0]), tail=[-0.4, 0.8, 0.1],
             Hips=[12, 0, 0], Spine02=[8, 0, 0], Spine01=[8, 0, 0], Spine=[6, 0, 0], neck=[-12, 0, 0], Head=[-12, 0, 0], Jaw_1=[6, 0, 0],
             LeftArm=[-45, 0, 0], LeftForeArm=[-35, 0, 0], RightArm=[-40, -12, 0], RightForeArm=[-35, 0, 0],
             Tail_1=[30, 0, 0], Tail_2=[12, 0, 6], Tail_3=[6, 0, 4], Tail_4=[1, 0, 0]),
    48: pose(hips=[0, 0.0, -0.45], footL=foot([0, -0.2, 0.3], [0, 0, 0]), footR=foot([0, 0.0, 0.0]), tail=[-0.2, 0.4, 0.05],
             Hips=[10, 0, 0], Jaw_1=[2, 0, 0], Tail_1=[27, 0, 0], Tail_2=[11, 0, 0], Tail_3=[5, 0, -2], Tail_4=[0, 0, -3]),
    54: pose(hips=[0, 0.08, -0.37], footL=foot([0, 0, 0]), tail=[-0.05, 0.1, 0]),
    61: IDLE_START,
}}


# SUPPORT ATTACK: a pounce and two-claw slam: deep crouch with both claws raised and a screech
# (12), spring up off the toes (20), both claws slam down in front (26), bite at the ground (30,
# snapped 33), rear up roaring with arms spread and the tail lashing (40), settle back (50-67).
ACTIONS["support_attack"] = {"frames": [1, 67], "loop": False, "keys": {
    1: IDLE_START,
    12: pose(hips=[0, 0.3, -1.25], tail=[0, 1.8, 1.4],
             Hips=[18, 0, 0], Spine02=[8, 0, 0], Spine01=[8, 0, 0], Spine=[8, 0, 0], neck=[-25, 0, 0], Head=[-20, 0, 0], Jaw_1=[22, 0, 0],
             LeftArm=[-150, -15, 0], LeftForeArm=[-40, 0, 0], RightArm=[-150, 15, 0], RightForeArm=[-40, 0, 0],
             Tail_1=[60, 0, 0], Tail_2=[20, 0, 0], Tail_3=[10, 0, 0], Tail_4=[5, 0, 0]),
    20: pose(hips=[0, -0.5, 0.1], footL=foot([0, 0.25, 0.45], [35, 0, 0]), footR=foot([0, 0.25, 0.45], [35, 0, 0]), tail=[0, 2.0, 1.2],
             Hips=[28, 0, 0], Spine02=[8, 0, 0], Spine01=[8, 0, 0], Spine=[8, 0, 0], neck=[-22, 0, 0], Head=[-16, 0, 0], Jaw_1=[6, 0, 0],
             LeftArm=[-165, -10, 0], LeftForeArm=[-30, 0, 0], RightArm=[-165, 10, 0], RightForeArm=[-30, 0, 0],
             LeftToeBase=[-30, 0, 0], RightToeBase=[-30, 0, 0], Tail_1=[60, 0, 0], Tail_2=[20, 0, 0], Tail_3=[10, 0, 0], Tail_4=[5, 0, 0]),
    26: pose(hips=[0, -1.2, -1.0], footL=foot([0, -0.4, 0], [-5, 0, 0]), footR=foot([0, -0.2, 0]), tail=[0, 2.3, 0.1],
             Hips=[38, 0, 0], Spine02=[12, 0, 0], Spine01=[12, 0, 0], Spine=[10, 0, 0], neck=[-5, 0, 0], Head=[0, 0, 0], Jaw_1=[0, 0, 0],
             LeftArm=[-75, 15, 0], LeftForeArm=[-10, 0, 0], LeftHand=[-25, 0, 0], RightArm=[-75, -15, 0], RightForeArm=[-10, 0, 0], RightHand=[-25, 0, 0],
             Tail_1=[35, 0, 0], Tail_2=[10, 0, 0], Tail_3=[5, 0, 0], Tail_4=[0, 0, 0]),
    30: pose(hips=[0, -1.25, -1.1], footL=foot([0, -0.4, 0], [-5, 0, 0]), footR=foot([0, -0.2, 0]), tail=[0.2, 2.3, 0.05],
             Hips=[40, 0, 0], Spine02=[12, 0, 0], Spine01=[12, 0, 0], Spine=[10, 0, 0], neck=[8, 0, 0], Head=[12, 0, 0], Jaw_1=[30, 0, 0],
             LeftArm=[-72, 15, 0], LeftForeArm=[-12, 0, 0], LeftHand=[-25, 0, 0], RightArm=[-72, -15, 0], RightForeArm=[-12, 0, 0], RightHand=[-25, 0, 0],
             Tail_1=[35, 0, 0], Tail_2=[10, 0, 4], Tail_3=[5, 0, 4], Tail_4=[0, 0, 2]),
    33: pose(hips=[0, -1.25, -1.1], footL=foot([0, -0.4, 0], [-5, 0, 0]), footR=foot([0, -0.2, 0]), tail=[0.3, 2.3, 0.05],
             Hips=[40, 0, 0], Spine02=[12, 0, 0], Spine01=[12, 0, 0], Spine=[10, 0, 0], neck=[8, 0, 0], Head=[14, 0, 0], Jaw_1=[0, 0, 0],
             LeftArm=[-72, 15, 0], LeftForeArm=[-12, 0, 0], LeftHand=[-25, 0, 0], RightArm=[-72, -15, 0], RightForeArm=[-12, 0, 0], RightHand=[-25, 0, 0],
             Tail_1=[35, 0, 0], Tail_2=[10, 0, 6], Tail_3=[5, 0, 6], Tail_4=[0, 0, 4]),
    40: pose(hips=[0, -0.6, -0.5], footL=foot([0, -0.4, 0], [-5, 0, 0]), footR=foot([0, -0.2, 0]), tail=[0.6, 1.6, 0.2],
             Hips=[10, 0, 0], Spine02=[0, 0, 0], Spine01=[-2, 0, 0], Spine=[-4, 0, 0], neck=[-25, 0, 0], Head=[-25, 0, 0], Jaw_1=[32, 0, 0],
             LeftArm=[-55, -60, 0], LeftForeArm=[-55, 0, 0], RightArm=[-55, 60, 0], RightForeArm=[-55, 0, 0], LeftHand=[-20, 0, 0], RightHand=[-20, 0, 0],
             Tail_1=[45, 0, 0], Tail_2=[15, 0, 15], Tail_3=[8, 0, 12], Tail_4=[3, 0, 8]),
    46: pose(hips=[0, -0.4, -0.45], footL=foot([0, -0.4, 0], [-5, 0, 0]), footR=foot([0, -0.2, 0]), tail=[-0.5, 1.4, 0.15],
             Hips=[10, 0, 0], Spine02=[2, 0, 0], Spine01=[0, 0, 0], Spine=[-2, 0, 0], neck=[-22, 0, 0], Head=[-20, 0, 0], Jaw_1=[24, 0, 0],
             LeftArm=[-50, -52, 0], LeftForeArm=[-50, 0, 0], RightArm=[-50, 52, 0], RightForeArm=[-50, 0, 0],
             Tail_1=[40, 0, 0], Tail_2=[14, 0, -14], Tail_3=[7, 0, -10], Tail_4=[3, 0, -6]),
    52: pose(hips=[0, -0.2, -0.4], footL=foot([0, -0.2, 0.2], [0, 0, 0]), footR=foot([0, -0.1, 0.0]), tail=[-0.2, 0.8, 0.1],
             Hips=[9, 0, 0], Jaw_1=[8, 0, 0], LeftArm=[-34, 0, 0], RightArm=[-34, 0, 0], Tail_1=[32, 0, 0], Tail_2=[12, 0, 4], Tail_3=[6, 0, 2], Tail_4=[1, 0, 0]),
    58: pose(hips=[0, 0.05, -0.37], footL=foot([0, 0, 0]), footR=foot([0, -0.05, 0.12]), tail=[-0.05, 0.2, 0]),
    62: pose(footR=foot([0, 0, 0])),
    67: IDLE_START,
}}


# DEFEND: a cornered, cowering guard: crouch back with forearms crossed before the face (8), hiss
# with the head pushed out between the arms (15), flinch from a hit (21), a quick defensive swat
# with the left claw (28), guard again (34) and ease back into the stance (40-49). Tail lashing.
GUARD = dict(Hips=[10, 0, 0], Spine02=[4, 0, 0], Spine01=[4, 0, 0], Spine=[6, 0, 0], neck=[-6, 0, 0], Head=[6, 0, 0],
             LeftArm=[-78, 0, -42], LeftForeArm=[-88, 0, 0], LeftHand=[-10, 0, 0], RightArm=[-72, 0, 42], RightForeArm=[-88, 0, 0], RightHand=[-10, 0, 0],
             Tail_1=[30, 0, 0], Tail_2=[12, 0, -15], Tail_3=[6, 0, -10], Tail_4=[2, 0, -6])
ACTIONS["defend"] = {"frames": [1, 49], "loop": False, "keys": {
    1: IDLE_START,
    8: pose(hips=[0, 0.35, -0.85], footR=foot([0, 0.5, 0.12], [5, 0, 0]), tail=[-0.7, 1.0, 0], **GUARD),
    15: pose(hips=[0, 0.3, -0.8], footR=foot([0, 0.5, 0.12], [5, 0, 0]), tail=[0.7, 1.2, 0.15],
             **dict(GUARD, neck=[-14, 0, 0], Head=[-6, 0, 0], Jaw_1=[30, 0, 0], Tail_2=[12, 0, 22], Tail_3=[6, 0, 18], Tail_4=[2, 0, 12])),
    21: pose(hips=[0, 0.6, -0.95], footR=foot([0, 0.5, 0.12], [5, 0, 0]), tail=[-0.8, 1.1, 0.1],
             **dict(GUARD, Hips=[4, 0, 0], Spine=[0, 0, 0], Head=[10, 0, -8], Jaw_1=[10, 0, 0], Tail_2=[12, 0, -22], Tail_3=[6, 0, -18], Tail_4=[2, 0, -12])),
    28: pose(hips=[0, 0.2, -0.8], footR=foot([0, 0.5, 0.12], [5, 0, 0]), tail=[0.5, 1.3, 0.1],
             **dict(GUARD, Hips=[12, 0, 8], Jaw_1=[18, 0, 0], LeftArm=[-80, 0, 50], LeftForeArm=[-20, 0, 0], LeftHand=[-25, 0, 0],
                    Tail_2=[12, 0, 15], Tail_3=[6, 0, 12], Tail_4=[2, 0, 8])),
    34: pose(hips=[0, 0.35, -0.85], footR=foot([0, 0.5, 0.12], [5, 0, 0]), tail=[-0.5, 1.0, 0.05], **dict(GUARD, Jaw_1=[12, 0, 0])),
    40: pose(hips=[0, 0.2, -0.55], footR=foot([0, 0.25, 0.1], [3, 0, 0]), tail=[-0.25, 0.5, 0],
             Jaw_1=[4, 0, 0], LeftArm=[-55, 20, 0], LeftForeArm=[-60, 0, 0], RightArm=[-55, -20, 0], RightForeArm=[-60, 0, 0],
             Tail_1=[28, 0, 0], Tail_2=[11, 0, -10], Tail_3=[5, 0, -8], Tail_4=[0, 0, -6]),
    49: IDLE_START,
}}


# TRAINING: a looping claw drill: bent low it rakes the ground with the right claw twice
# (16, 28), then the left claw twice (42, 54), straightens to sniff (60-66) and settles (73).
LOW = dict(Hips=[42, 0, 0], Spine02=[12, 0, 0], Spine01=[12, 0, 0], Spine=[10, 0, 0], neck=[-34, 0, 0], Head=[-16, 0, 0],
           Tail_1=[40, 0, 0], Tail_2=[12, 0, 6], Tail_3=[6, 0, 4], Tail_4=[2, 0, 2])
LOWH = [0, 0.55, -1.35]
ACTIONS["training"] = {"frames": [1, 73], "loop": True, "keys": {
    1: IDLE_START,
    10: pose(hips=LOWH, tail=[-0.4, 1.4, 0], **dict(LOW, RightArm=[-95, -10, 0], RightForeArm=[-10, 0, 0], RightHand=[0, 0, 0], LeftArm=[-45, 10, 0], LeftForeArm=[-40, 0, 0])),
    16: pose(hips=LOWH, tail=[-0.2, 1.4, 0], **dict(LOW, Head=[-14, 0, -4], RightArm=[-25, -5, 0], RightForeArm=[-5, 0, 0], RightHand=[-35, 0, 0],
                                                       LeftArm=[-45, 10, 0], LeftForeArm=[-40, 0, 0], Tail_2=[12, 0, 0], Tail_3=[6, 0, -2])),
    22: pose(hips=LOWH, tail=[-0.4, 1.4, 0], **dict(LOW, RightArm=[-95, -10, 0], RightForeArm=[-10, 0, 0], RightHand=[0, 0, 0], LeftArm=[-45, 10, 0], LeftForeArm=[-40, 0, 0],
                                                       Tail_2=[12, 0, -6], Tail_3=[6, 0, -6])),
    28: pose(hips=LOWH, tail=[-0.2, 1.4, 0], **dict(LOW, Head=[-14, 0, -4], RightArm=[-25, -5, 0], RightForeArm=[-5, 0, 0], RightHand=[-35, 0, 0],
                                                       LeftArm=[-45, 10, 0], LeftForeArm=[-40, 0, 0], Tail_2=[12, 0, -10], Tail_3=[6, 0, -8])),
    36: pose(hips=LOWH, tail=[0.2, 1.4, 0], **dict(LOW, LeftArm=[-95, 10, 0], LeftForeArm=[-10, 0, 0], LeftHand=[0, 0, 0], RightArm=[-45, -10, 0], RightForeArm=[-40, 0, 0],
                                                      Tail_2=[12, 0, -6], Tail_3=[6, 0, -4])),
    42: pose(hips=LOWH, tail=[0.4, 1.4, 0], **dict(LOW, Head=[-14, 0, 4], LeftArm=[-25, 5, 0], LeftForeArm=[-5, 0, 0], LeftHand=[-35, 0, 0],
                                                      RightArm=[-45, -10, 0], RightForeArm=[-40, 0, 0], Tail_2=[12, 0, 0], Tail_3=[6, 0, 2])),
    48: pose(hips=LOWH, tail=[0.2, 1.4, 0], **dict(LOW, LeftArm=[-95, 10, 0], LeftForeArm=[-10, 0, 0], LeftHand=[0, 0, 0], RightArm=[-45, -10, 0], RightForeArm=[-40, 0, 0],
                                                      Tail_2=[12, 0, 6], Tail_3=[6, 0, 6])),
    54: pose(hips=LOWH, tail=[0.4, 1.4, 0], **dict(LOW, Head=[-14, 0, 4], LeftArm=[-25, 5, 0], LeftForeArm=[-5, 0, 0], LeftHand=[-35, 0, 0],
                                                      RightArm=[-45, -10, 0], RightForeArm=[-40, 0, 0], Tail_2=[12, 0, 10], Tail_3=[6, 0, 8])),
    60: pose(hips=[0, 0.2, -0.6], tail=[0, 0.8, 0], Hips=[14, 0, 0], neck=[-18, 0, 6], Head=[-16, 0, 6], Jaw_1=[4, 0, 0],
             LeftArm=[-35, 10, 0], LeftForeArm=[-30, 0, 0], RightArm=[-35, -10, 0], RightForeArm=[-30, 0, 0], Tail_2=[10, 0, 4], Tail_3=[5, 0, 2]),
    66: pose(hips=[0, 0.15, -0.45], tail=[-0.1, 0.4, 0], Hips=[10, 0, 0], neck=[-16, 0, -4], Head=[-17, 0, -6], Jaw_1=[3, 0, 0],
             Tail_2=[10, 0, -4], Tail_3=[5, 0, -6]),
    73: IDLE_START,
}}


# DEATH: struck (5): thrown back with a squeal and arms flung out; staggers a step back (12),
# the knees buckle (20) and it drops to its knees (30), topples forward onto its left side (40),
# hits the ground (44), bounces and settles (50-58); the tail twitches twice and goes limp (60-76).
ACTIONS["death"] = {"frames": [1, 76], "loop": False, "keys": {
    1: IDLE_START,
    5: pose(hips=[0, 0.3, -0.3], tail=[0, 2.0, 1.0],
            Hips=[-4, 0, 0], Spine02=[-6, 0, 0], Spine01=[-8, 0, 0], Spine=[-6, 0, 0], neck=[-25, 0, 0], Head=[-20, 0, 0], Jaw_1=[32, 0, 0],
            LeftArm=[-20, -40, 0], LeftForeArm=[-20, 0, 0], RightArm=[-20, 40, 0], RightForeArm=[-20, 0, 0],
            Tail_1=[50, 0, 0], Tail_2=[20, 0, 0], Tail_3=[10, 0, 0], Tail_4=[5, 0, 0]),
    12: pose(hips=[0.15, 0.55, -0.7], footR=foot([0, 0.7, 0.1], [10, 0, 0]), tail=[-0.5, 1.6, 0.3],
             Hips=[12, 6, 0], Spine02=[10, 0, 0], Spine01=[10, 0, 0], Spine=[10, 0, 0], neck=[-10, 0, 0], Head=[-6, 0, 10], Jaw_1=[18, 0, 0],
             LeftArm=[-50, 10, 0], LeftForeArm=[-50, 0, 0], RightArm=[-35, -20, 0], RightForeArm=[-50, 0, 0],
             Tail_1=[35, 0, 0], Tail_2=[12, 0, 6], Tail_3=[6, 0, 4], Tail_4=[2, 0, 2]),
    20: pose(hips=[0.2, 0.6, -1.9], footL=foot([0, 0.9, 0.6], [70, 0, 0]), footR=foot([0, 1.3, 0.65], [70, 0, 0]), tail=[0, 1.8, 0.0],
             Hips=[18, 8, 0], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[5, 0, 0], Head=[10, 0, 0], Jaw_1=[12, 0, 0],
             LeftArm=[-15, 10, 0], LeftForeArm=[-15, 0, 0], RightArm=[-15, -10, 0], RightForeArm=[-15, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             LeftToeBase=[-60, 0, 0], RightToeBase=[-60, 0, 0], Tail_1=[30, 0, 0], Tail_2=[10, 0, 0], Tail_3=[5, 0, 0], Tail_4=[0, 0, 0]),
    30: pose(hips=[0.25, 0.7, -2.15], footL=foot([0, 1.8, 0.7], [85, 0, 0]), footR=foot([0, 2.0, 0.7], [85, 0, 0]), tail=[0.2, 1.9, 0.0],
             Hips=[25, 10, 0], Spine02=[10, 0, 0], Spine01=[10, 0, 0], Spine=[10, 0, 0], neck=[10, 0, 0], Head=[12, 0, 0], Jaw_1=[10, 0, 0],
             LeftArm=[-10, 8, 0], LeftForeArm=[-10, 0, 0], RightArm=[-10, -8, 0], RightForeArm=[-10, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             LeftToeBase=[-80, 0, 0], RightToeBase=[-80, 0, 0], Tail_1=[30, 0, 0], Tail_2=[10, 0, 0], Tail_3=[5, 0, 0], Tail_4=[0, 0, 0]),
    34: pose(hips=[0.5, 0.1, -2.8], footL=foot([0.15, 2.2, 0.55], [125, 0, 0]), footR=foot([0.0, 2.4, 0.55], [125, 0, 0]), tail=[0.4, 2.2, 0.0],
             Hips=[52, 18, 5], Spine02=[6, 0, 0], Spine01=[6, 0, 0], Spine=[6, 0, 0], neck=[0, 0, 0], Head=[0, 0, 14], Jaw_1=[16, 0, 0],
             LeftArm=[-120, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[-30, -10, 0], RightForeArm=[-20, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             LeftToeBase=[-40, 0, 0], RightToeBase=[-40, 0, 0], Tail_1=[25, 0, 0], Tail_2=[8, 0, 0], Tail_3=[4, 0, 0], Tail_4=[0, 0, 0]),
    40: pose(hips=[0.8, -0.6, -3.35], footL=foot([0.3, 2.6, 0.3], [160, 0, 0]), footR=foot([0.0, 2.8, 0.3], [160, 0, 0]), tail=[0.6, 2.5, 0.0],
             Hips=[80, 30, 10], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[-10, 0, 0], Head=[-15, 0, 28], Jaw_1=[20, 0, 0],
             LeftArm=[-150, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[5, -15, 0], RightForeArm=[-20, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             Tail_1=[20, 0, 0], Tail_2=[6, 0, 0], Tail_3=[3, 0, 0], Tail_4=[0, 0, 0]),
    44: pose(hips=[0.85, -0.65, -3.15], footL=foot([0.3, 2.6, 0.4], [160, 0, 0]), footR=foot([0.0, 2.8, 0.4], [160, 0, 0]), tail=[0.7, 2.5, 0.05],
             Hips=[78, 30, 10], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[-8, 0, 0], Head=[-8, 0, 28], Jaw_1=[22, 0, 0],
             LeftArm=[-150, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[5, -15, 0], RightForeArm=[-22, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             Tail_1=[22, 0, 0], Tail_2=[8, 0, 6], Tail_3=[4, 0, 4], Tail_4=[0, 0, 2]),
    50: pose(hips=[0.85, -0.65, -3.35], footL=foot([0.3, 2.6, 0.3], [160, 0, 0]), footR=foot([0.0, 2.8, 0.3], [160, 0, 0]), tail=[0.8, 2.5, 0.0],
             Hips=[80, 30, 10], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[-10, 0, 0], Head=[-15, 0, 28], Jaw_1=[14, 0, 0],
             LeftArm=[-150, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[5, -15, 0], RightForeArm=[-20, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             Tail_1=[20, 0, 0], Tail_2=[10, 0, 15], Tail_3=[5, 0, 10], Tail_4=[2, 0, 6]),
    58: pose(hips=[0.85, -0.65, -3.35], footL=foot([0.3, 2.6, 0.3], [160, 0, 0]), footR=foot([0.0, 2.8, 0.3], [160, 0, 0]), tail=[0.3, 2.5, 0.0],
             Hips=[80, 30, 10], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[-10, 0, 0], Head=[-15, 0, 28], Jaw_1=[10, 0, 0],
             LeftArm=[-150, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[5, -15, 0], RightForeArm=[-20, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             Tail_1=[20, 0, 0], Tail_2=[8, 0, -12], Tail_3=[4, 0, -8], Tail_4=[1, 0, -5]),
    66: pose(hips=[0.85, -0.65, -3.35], footL=foot([0.3, 2.6, 0.3], [160, 0, 0]), footR=foot([0.0, 2.8, 0.3], [160, 0, 0]), tail=[0.6, 2.5, 0.0],
             Hips=[80, 30, 10], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[-10, 0, 0], Head=[-15, 0, 28], Jaw_1=[8, 0, 0],
             LeftArm=[-150, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[5, -15, 0], RightForeArm=[-20, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             Tail_1=[20, 0, 0], Tail_2=[6, 0, 3], Tail_3=[3, 0, 2], Tail_4=[0, 0, 0]),
    76: pose(hips=[0.85, -0.65, -3.35], footL=foot([0.3, 2.6, 0.3], [160, 0, 0]), footR=foot([0.0, 2.8, 0.3], [160, 0, 0]), tail=[0.6, 2.5, 0.0],
             Hips=[80, 30, 10], Spine02=[2, 0, 0], Spine01=[2, 0, 0], Spine=[2, 0, 0], neck=[-10, 0, 0], Head=[-15, 0, 28], Jaw_1=[8, 0, 0],
             LeftArm=[-150, 0, 0], LeftForeArm=[-10, 0, 0], RightArm=[5, -15, 0], RightForeArm=[-20, 0, 0], LeftHand=[0, 0, 0], RightHand=[0, 0, 0],
             Tail_1=[20, 0, 0], Tail_2=[6, 0, 3], Tail_3=[3, 0, 2], Tail_4=[0, 0, 0]),
}}


if __name__ == "__main__":
    out = {role: {"frames": spec["frames"], "loop": spec["loop"], "keys": {str(f): k for f, k in spec["keys"].items()}}
           for role, spec in ACTIONS.items()}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rat_actions_authored.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print(path, {r: len(v["keys"]) for r, v in out.items()})
