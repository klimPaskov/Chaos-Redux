# Biowarfare Border Closure Decisions

## Overview

This mechanic adds targeted border-closure decisions to `chaosx_disease_containment_category` for neighboring countries with active biowarfare outbreaks.

The system is bilateral and per-target:
- You can close the border to a specific infected neighbor.
- You can reopen that specific border at any time.
- Closed borders are tracked in the country array `closed_bio_borders` (stored as target country IDs).

## Gameplay Flow

1. Decision visibility:
- The disease containment category now appears if:
  - your country has active biowarfare contamination, or
  - any neighboring country has active biowarfare contamination.

2. Close border decision:
- Targeted to `neighbors`.
- Only shown for neighbors that currently have active outbreak contamination.
- On completion:
  - applies a relation-rule override with `can_access_market = no` toward the selected target,
  - applies a relation-rule override with `can_send_volunteers = no` toward the selected target,
  - records the closed border target in `closed_bio_borders`.

3. Reopen border decision:
- Targeted to `neighbors`.
- Only shown for targets currently present in `closed_bio_borders`.
- On completion:
  - removes the target from `closed_bio_borders`,
  - relation-rule overrides remain installed globally but stop applying immediately because their trigger no longer matches that target,
  - market and volunteer interaction are therefore restored at once.

4. Spread interaction:
- Anthrax, plague, and smallpox spread state events now allow cross-border spread (not only same-controller spread).
- If a neighboring country has closed the border against the infected country, spread MTTH is increased by `constant:bio_border_controls.spread.closed_border_mtth_factor`.
- Result: closure lowers spread chance over time, but does not make spread impossible.

## Scripted Reuse Added

Added scripted triggers in `common/scripted_triggers/chaosx_scripted_triggers.txt`:
- `has_active_biowarfare_outbreak`
- `has_neighbor_with_active_biowarfare_outbreak`

These are used by category visibility and targeted decision filtering.

## Tuning Constants

Added `bio_border_controls` in `common/script_constants/biowarfare_constants.txt`:
- `spread.closed_border_mtth_factor`
- `ai.close_*`
- `ai.reopen_*`

These control both spread reduction strength and AI decision behavior.

## AI Behavior

Close-border AI increases with outbreak severity in target country:
- highest bias for smallpox,
- then plague,
- then anthrax/tularemia.

AI is less likely to close when:
- opinion is high,
- already at war with target.

AI is more likely to reopen once target has no active outbreak and less likely while outbreak remains active.

## Icons Needed

No new custom icons are required for this implementation.

Currently reused vanilla decision icons:
- `GFX_decision_generic_arrest` (close border decision)
- `GFX_decision_generic_industry` (reopen border decision)

If custom art is desired later:
- Sprite files path: `gfx/interface/goals/` (or your preferred decision icon folder).
- Register sprites in a decision sprite `.gfx` file under `interface/` (for example `interface/chaosx_decisions.gfx`).
- Suggested sprite names:
  - `GFX_decision_close_bio_border`
  - `GFX_decision_reopen_bio_border`
- Then replace icon keys in `common/decisions/chaosx_disease_containment_decisions.txt`.

## Future Extensions

- Add optional diplomatic penalties/opinion shifts when borders are closed.
- Add border-closure duration variants (short emergency closure vs. long strict closure).
- Add targeted intelligence requirement modifiers (better intel = stronger spread reduction).
- Add UI feedback listing all currently closed disease borders and their trade impact.
