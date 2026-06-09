# Event 006 Strange Focus Follow-through Tranche Handoff

Scope: bounded Event 006 Independence Wave strange/containment focus follow-through after the Sealed Dossier decision surface.

## Files changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_strange_focus_followthrough_audit_patch_handoff.md`

No flag assets, country setup files, country history files, Event 005 files, or `gfx/flags` files were edited.

## Implemented focus module

The hidden strange focus follow-through module now appears only after the sealed-dossier runtime state justifies it:

- `independence_wave_sealed_bureau_charter`
- containment recovery side:
  - `independence_wave_moral_tribunal`
  - `independence_wave_quarantine_bureau`
  - `independence_wave_restore_public_registry`
- revealed strange-doctrine side:
  - `independence_wave_unmarked_ministry`
  - `independence_wave_census_without_names`
  - `independence_wave_border_office_of_absence`

The contained and revealed sides are mutually exclusive at their root focus. The branch roots use `allow_branch` so the wrong outcome branch stays hidden until the relevant flag exists.

## Script and tuning

- Added focus constants for occult pressure gains/relief and strange AI threshold gates.
- Added scripted focus rewards for the seven new focus ids.
- Added `mark_focus_tree_layout_dirty = yes` to sealed-dossier effects that set the audit, containment, or reveal flags, so branch visibility can refresh mid-session.
- Corrected strange package setup to raise occult pressure with `constant:independence_wave_focus.occult_pressure_gain_medium`.

## Localisation and docs

- Added English name and description localisation for all seven focus ids.
- Updated `docs/events/006_independence_wave.md` to describe the new hidden follow-through module and its current limits.
- Generic vanilla focus icons are used and documented; no new art files were created.

## Audit

`chaosx_focus_tree_auditor` reviewed this tranche and made two narrow patches:

- converted `independence_wave_moral_tribunal` and `independence_wave_unmarked_ministry` from `available` route gates to `allow_branch` route visibility gates
- corrected the strange-package occult-pressure setup constant

Audit handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_strange_focus_followthrough_audit_patch_handoff.md`

## Validation

- Brace balance is clean for touched script/localisation/docs files.
- No unsupported less-than-or-equal / greater-than-or-equal operators are present in the touched Event 006 code/docs files.
- `localisation/english/006_independence_wave_l_english.yml` keeps UTF-8 BOM and has no `:0` keys.
- Focus localisation coverage check found 54 focus ids, no duplicate ids, and no missing name/description keys.
- All seven new icon ids resolve to vanilla `interface/goals.gfx`.
- `git diff --check` is clean for the scoped touched files.
- No whitespace errors were found by no-index checks on the untracked scoped Event 006 files.
- `git status --short -- gfx/flags common/countries history/countries` produced no output.

## Simplifications, omissions, and blockers

- This is a first strange focus module, not the full strange route family.
- It does not add strange country tags, strange formables, super-event claims, final strange assets, or a broad world-threat system.
- The broader AI strategy is still generic for strange-package posture; contained recovery and revealed escalation do not yet have separate AI strategy overlays.
- The module still sits behind `independence_wave_recognition_desk`; moving it earlier would be a separate route-design decision.
