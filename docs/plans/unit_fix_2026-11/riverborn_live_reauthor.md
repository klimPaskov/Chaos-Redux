# Riverborn: live re-authoring record

Disposition: `implemented`. Accepted by an independent fresh-context review on 2026-11-07 (full final review, `VERDICT: pass`, `DEFECTS: none`). Live in-game behaviour is not checked here; that stays with the maintainer.

## What changed

- **Weights.** The feather mantle and water cloak were weighted mostly to the arms, so they flapped like wings and stretched up to about 25% of the unit's height. Cloak skin (the texture-colour mask plus any skin more than 0.45 from the arm bone segments, ramped over 0.35) now follows the spine chain and shoulders, with a small thigh share at the hem. The worst per-frame stretch is now 4 to 12%.
- **Actions.** All eight roles were re-authored live in Blender through the Blender Lab MCP, under decision 3D-5, with the spear on the right hand and the shield on the left forearm:
  - idle: weight shifts, a look around and a spear tap.
  - move: a spear walk.
  - attack: a coil, a stepping lunge thrust, a second coil and thrust.
  - defend: a low spear and a shield brace and drive.
  - support_attack: an overhead raise, a long step and a downward drive.
  - retreat: backing away behind the shield.
  - training: a shield punch, a spear-butt strike, an overhead flourish and a salute.
  - death: a stagger with the spear held up at the side, then a fall to lie face down.
- **Clip lengths.** The clip lengths are unchanged.
- **Entity.** `gfx/entities/chaosx_riverborn.asset` event times and comments now match the new key frames.

## Evidence

- `check_unit_files.py` on `gfx/models/units/012_africa_riverborn`: 0 errors. One warning: registration is not checked in the sparse worktree.
- Every clip is 30 fps. The sample counts are idle 300, move 36, attack 117, defend 90, support_attack 136, retreat 39, training 117 and death 85.
- In the per-frame max-turn audit of the exported `.anim` files, no joint exceeds 38 degrees per frame. The bar is about 40.
- Review history: 11 rounds. Findings narrowed from cloak stretch and props through the body to spear clearance at single frames. Rounds 7 to 11 used the fixed checklist and the cloak-tatter note.
