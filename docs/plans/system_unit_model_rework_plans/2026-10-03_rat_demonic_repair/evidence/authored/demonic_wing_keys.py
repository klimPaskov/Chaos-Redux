"""Authored wing keys for the demonic zombie's rebuilt wing chains (2026-10-03 repair).

The body motion of every action stays the receipt-verified provider motion already in the
checkpoint; only the wing bones (WingX_Arm and the four finger struts A outer, B, C, D inner) are
re-keyed. Values are [rx, ry, rz] degrees about the rest-world axes, relative to the parent
(rlab.key_pose), written for the LEFT wing; the right wing mirrors ry and rz. For the left wing:
+ry tilts the wing arm outward, -ry fans a hanging finger outward, +rz sweeps the spread wing
backward and -rz forward, +rx tilts the wing arm toward the body's front. Each named pose below is a deliberate wing shape chosen from
rest and spread pose renders; the per-action tables place them on the measured body phases noted
in the entity (claw slashes, leap, pin, scream, stomps, dodges, fall). SPLAY was chosen by a
measured search (splay_search2.json) as the shape that lets the fallen body and both wings rest on
the floor together (torso/wing lowest-point gap 0.01-0.12 units at frames 55-68).

Running this file writes demonic_wing_keys.json with the explicit per-frame values.
"""
import json
import os

BONES = ["Arm", "A1", "A2", "A3", "B1", "B2", "C1", "C2", "D1", "D2"]


def shape(arm=(0, 0, 0), A=(0, 0, 0), A2=0, A3=0, B=(0, 0, 0), B2=0, C=(0, 0, 0), C2=0, D=(0, 0, 0), D2=0):
    return {"Arm": list(arm), "A1": list(A), "A2": [0, A2, 0], "A3": [0, A3, 0], "B1": list(B), "B2": [0, B2, 0],
            "C1": list(C), "C2": [0, C2, 0], "D1": list(D), "D2": [0, D2, 0]}


FOLD = shape()
REST_OPEN = shape(arm=(0, 2, 2), A=(0, -3, 0), B=(0, -3, 0), C=(0, -2, 0))
BREATHE = shape(arm=(0, 6, 4), A=(0, -8, 0), A2=-2, B=(0, -10, 0), C=(0, -6, 0), D=(0, -3, 0))
HALF = shape(arm=(-4, 18, 14), A=(0, -15, 0), A2=-5, B=(0, -28, 0), B2=-4, C=(0, -18, 0), C2=-3, D=(0, -8, 0))
HALF_HI = shape(arm=(-6, 25, 18), A=(0, -20, 0), A2=-7, A3=-3, B=(0, -38, 0), B2=-6, C=(0, -25, 0), C2=-4, D=(0, -11, 0))
FLARE = shape(arm=(-8, 40, 28), A=(0, -25, 0), A2=-12, A3=-6, B=(0, -60, 0), B2=-10, C=(0, -40, 0), C2=-8, D=(0, -18, 0), D2=-5)
FLARE_UP = shape(arm=(-15, 48, 22), A=(0, -28, 0), A2=-14, A3=-8, B=(0, -65, 0), B2=-12, C=(0, -44, 0), C2=-9, D=(0, -20, 0), D2=-6)
SOFT_FLARE = shape(arm=(-6, 30, 20), A=(0, -20, 0), A2=-8, A3=-4, B=(0, -45, 0), B2=-7, C=(0, -30, 0), C2=-6, D=(0, -13, 0), D2=-3)
MANTLE = shape(arm=(-35, 25, -25), A=(-10, -20, 0), A2=-6, B=(-10, -35, 0), B2=-6, C=(-8, -25, 0), C2=-4, D=(0, -10, 0))
SHIELD = shape(arm=(-45, 15, -40), A=(-25, -15, 0), A2=-5, B=(-25, -25, 0), B2=-5, C=(-20, -15, 0), C2=-3, D=(-10, -5, 0))
SHIELD_LITE = shape(arm=(-28, 12, -22), A=(-15, -12, 0), A2=-4, B=(-15, -20, 0), B2=-4, C=(-12, -12, 0), C2=-2, D=(-6, -4, 0))
# FALL: during the backward landing the wing arms tilt toward the body's front and sweep forward
# (+rx, -rz) and the inner struts fold up, so the membranes stay above the floor while the torso lands.
# Chosen by measured searches (fall_search3.json, fall_search4.json): the remaining lowest wing point
# is the membrane root on the shoulder blade, within 0.07 units of the torso's lowest point.
FALL = shape(arm=(60, 0, -90), A=(0, -20, 0), A2=-8, A3=-4, B=(45, -45, 0), B2=-7, C=(90, -50, 0), C2=-6, D=(90, -30, 0), D2=-3)
# SETTLE and LIE: after the torso is down, the inner struts open again (SETTLE, wings 0.24-0.31 above the
# floor) and the wings sink onto the ground beside the body (LIE, within 0.07 units of the torso's lowest
# point at frames 60-68). Both chosen by measured searches (settle_search.json, settle_search2.json).
SETTLE = shape(arm=(60, 0, -90), A=(0, -22, 0), A2=-9, A3=-4, B=(0, -50, 0), B2=-8, C=(0, -45, 0), C2=-6, D=(0, -25, 0), D2=-4)
LIE = shape(arm=(30, 30, -60), A=(0, -22, 0), A2=-9, A3=-4, B=(0, -50, 0), B2=-8, C=(0, -45, 0), C2=-6, D=(0, -25, 0), D2=-4)
SPLAY = shape(arm=(-20, 60, -30), A=(0, -25, 0), A2=-10, A3=-5, B=(0, -55, 0), B2=-8, C=(0, -38, 0), C2=-6, D=(0, -16, 0), D2=-4)


def both(left, right=None):
    right = right or left
    out = {}
    for b in BONES:
        out[f"WingL_{b}"] = left[b]
        rx, ry, rz = right[b]
        out[f"WingR_{b}"] = [rx, -ry, -rz]
    return out


ACTIONS = {
    # IDLE (1-237 loop): slow breathing opens and closes the membranes; a stretch at 95-140
    # half-raises and fans the wings before they settle, the left leading the right.
    "idle": {1: both(REST_OPEN), 40: both(BREATHE), 80: both(REST_OPEN), 95: both(HALF, BREATHE), 110: both(SOFT_FLARE, HALF),
             125: both(HALF, SOFT_FLARE), 140: both(BREATHE, HALF), 160: both(REST_OPEN, BREATHE), 200: both(BREATHE), 237: both(REST_OPEN)},
    # MOVE (1-261 loop): wings carried half open like a cloak, pulsing wider on the foot plants
    # (right 22, 64, 109, 152, 195, 241) and easing between them, so the membranes face the camera.
    "move": {1: both(HALF), 22: both(HALF_HI), 43: both(HALF), 64: both(HALF_HI), 87: both(HALF), 109: both(HALF_HI), 130: both(HALF),
             152: both(HALF_HI), 174: both(HALF), 195: both(HALF_HI), 218: both(HALF), 241: both(HALF_HI), 261: both(HALF)},
    # RETREAT (1-50 loop): wings drawn forward around the body as a cloak with a quick flutter open.
    "retreat": {1: both(SHIELD_LITE), 13: both(HALF), 26: both(SHIELD_LITE), 38: both(HALF), 50: both(SHIELD_LITE)},
    # DEFEND (1-44 loop): the wings snap forward into a shield on the side-step dodges (10, 22)
    # and open between them.
    "defend": {1: both(BREATHE), 10: both(SHIELD), 16: both(SHIELD_LITE), 22: both(SHIELD), 33: both(HALF), 44: both(BREATHE)},
    # ATTACK (3-122): wings drawn up in the crouch, flared wide on each claw slash (35, 65-71, 105).
    "attack": {3: both(REST_OPEN), 20: both(HALF), 35: both(FLARE), 45: both(HALF), 65: both(FLARE), 71: both(FLARE_UP), 80: both(HALF),
               105: both(FLARE), 115: both(HALF), 122: both(REST_OPEN)},
    # SUPPORT ATTACK (3-122): wings half raised for the spring, fully spread in the leap (43-46),
    # mantled forward over the pinned prey (55-63), flared high for the scream (80), then folded.
    "support_attack": {3: both(REST_OPEN), 30: both(HALF), 43: both(FLARE_UP), 47: both(FLARE), 55: both(MANTLE), 63: both(MANTLE),
                       72: both(HALF), 80: both(FLARE_UP), 95: both(HALF), 110: both(BREATHE), 122: both(REST_OPEN)},
    # TRAINING (1-43 loop): angry stomps (9, 25, 40) each with a wing flare.
    "training": {1: both(HALF), 9: both(FLARE), 17: both(HALF), 25: both(FLARE), 34: both(HALF), 40: both(SOFT_FLARE), 43: both(HALF)},
    # DEATH (1-68): thrown back, the wings fling open (8) and flail up (20), half close (32),
    # fold forward and up over the body while it falls and the torso lands (36-46), open their struts
    # as the body bounces and settles (52), then sink onto the ground beside it (58-68).
    "death": {1: both(REST_OPEN), 8: both(FLARE), 20: both(FLARE_UP), 32: both(HALF), 36: both(FALL), 46: both(FALL), 52: both(SETTLE), 58: both(LIE), 68: both(LIE)},
}

if __name__ == "__main__":
    out = {role: {str(f): v for f, v in keys.items()} for role, keys in ACTIONS.items()}
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demonic_wing_keys.json")
    json.dump(out, open(p, "w", encoding="utf-8"), indent=1)
    print(p, {r: len(v) for r, v in out.items()})
