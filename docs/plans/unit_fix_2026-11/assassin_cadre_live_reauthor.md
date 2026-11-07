# Assassin Cadre (master_assassin): live re-authoring record

Disposition: `implemented`. Accepted by an independent fresh-context review on 2026-11-07 (full final review, `VERDICT: pass`, `DEFECTS: none`). In-game behaviour stays with the maintainer to check.

## What changed

Fixes target the audit findings. Clips that already read well (move, defend, support_attack, training, and the first 96 frames of death) are kept, with only quaternion key signs normalised.

- **mesh:** the repaired mesh is installed, which fixes winding.
- **attack:** re-authored live. The SMG is shouldered with the right hand on the grip and the left hand seated on the foregrip through a grip point stored in the weapon's frame. Three-shot bursts with recoil fire at frames 26, 52 and 82, and the torso turns between targets.
- **idle:** re-authored live as a low-ready stand. The unit shifts its weight, scans left and right with torso turns, and checks its weapon.
- **retreat:** re-authored live as a backpedal with the weapon at low ready in both hands. The unit looks back over each shoulder.
- **death:** the original fall is kept. From frame 92 on, the raised legs lie flat on the ground, and the weapon rests beside the hand with its muzzle off the ground.
- **entity:** in `gfx/entities/chaosx_assassin_cadre.asset`, the attack muzzle events now fire at the new burst frames. Shadow Company and Master Assassin share these actions.

## Evidence

- `check_unit_files.py` on `gfx/models/units/039_assassin_cadre`: 0 errors. The two warnings are the specular-map shininess (existing) and registration that the sparse worktree does not check.
- All clips are 30 fps at their original lengths (idle 420, move 91, attack 120, defend 111, support_attack 120, retreat 32, training 99, death 141).
- Per-frame max-turn audit: no joint exceeds 34.3 degrees per frame.
- Review history: 4 rounds (full, scoped retreat and death, scoped retreat, full final).
