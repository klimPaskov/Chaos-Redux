# Event 006 Package Anchor Tranche Handoff

Date: 2026-05-30

## Scope

Hardened the reduced-release resolver so verified Event 006 starter packages release from their intended identity state when that state is still host-owned, host-controlled, candidate-cored, and not reserved for host survival.

No flag assets, flag definitions, country flag images, country history, country files, or Event 005 files were edited.

## Files changed

- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`

## Behavior changed

- Added `independence_wave_try_package_reduced_release_anchor`.
- `independence_wave_prepare_reduced_release_footprint` now calls the package-anchor helper before the generic anchor search.
- Preferred anchor order:
  - `OGB`: Kazan `249`, then Cheboksary `256`
  - `ASY`: Mosul `676`
  - `DNZ`: Danzig `85`
  - `UGA`: Uganda `548`
  - `SOK`: Sokoto `902`
- The generic factory, urban, infrastructure, and any-state anchor search remains in place when a package identity state is unavailable or protected.
- The existing masking and core restoration logic still handles extra candidate cores after the anchor is chosen.

## Validation

- Brace balance is clean for `common/scripted_effects/006_independence_wave_effects.txt`, `events/006_independence_wave.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, and `common/script_constants/006_independence_wave_constants.txt`.
- Unsupported pattern scan found no `<=`, `>=`, direct constant duration fields, or unary negative variable-token assignments in the checked Event 006 script files.
- Leading-space indentation scan found no space-indented script lines in the checked Event 006 script files.
- `git diff --check` passed for the touched tracked plan file; trailing-whitespace and final-newline scans covered the touched untracked Event 006 script, docs, and handoff files.
- No files under `gfx/flags`, `common/countries`, or `history/countries` were touched.

## Remaining gaps

- This does not create new packages, super-events, audio, GUI windows, animations, or final assets.
- Railway packages still use the generic infrastructure anchor because they do not yet have a verified fixed state list.
