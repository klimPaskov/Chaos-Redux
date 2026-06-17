# Event 012 Authority Atlas Macro-Region and Guard Mission Parent Handoff

Date: 2026-06-17

## Scope

The parent patch tightens the Authority Atlas / Archive of Old Seats decision layer so the guard deadline mission is tied to the exact dossier that created it, and so the Continental Register / World Is One route requires all six historical macro-region lines rather than only the minimum opened-dossier count.

## Changed Files

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/scripted_guis/012_africa_scripted_gui.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`

## Implementation Notes

- Added `constant:africa_authority_atlas.minimum_historical_macro_regions = 6`.
- Registered `global.africa_authority_atlas_minimum_historical_macro_regions` for visible decision-category localisation.
- Added `has_africa_continental_register_dossier_coverage`, requiring both `africa_minimum_historical_dossiers_ready` and a macro-region dossier count of at least six.
- Added `africa_archive_guard_mission_dossier_id` and `africa_archive_guard_mission_seat_state` as mission-context variables.
- Added helpers:
  - `africa_start_archive_guard_mission_for_selected_dossier`
  - `africa_clear_archive_guard_mission_context`
- The survey mission now starts the guard deadline with the helper, instead of setting only `africa_archive_guard_mission_active`.
- `africa_open_next_historical_dossier` is blocked while `africa_archive_guard_mission_active` is set.
- `africa_archive_guard_deadline_mission` now checks the stored dossier's local office, guard, settlement flag, and stored representative seat state.
- The deadline mission still requires at least one secured representative dossier seat through `africa_dossier_seat_secure_count`, preserving the existing global proof requirement while preventing aggregate dossier work from satisfying the mission.
- `AFR_continental_register`, `AFR_africa_is_one`, and the World Is One certification/preparation triggers now use `has_africa_continental_register_dossier_coverage`.
- Localisation now displays macro-region coverage in the Authority Atlas header.
- Post-audit follow-up wrapped the scripted GUI dossier click effect in the same gate used by its enabled trigger, so a direct effect call cannot spend PP or support equipment while the guard deadline lock is active.

## Parent Validation

- Touched Clausewitz/localisation files brace-balanced.
- No unsupported comparison-operator tokens in touched script files.
- `git diff --check` returned clean for this patch's touched files.
- Localisation BOM remained intact.
- Targeted text audit confirmed the guard deadline mission block no longer contains `africa_dossier_local_office_count`, `africa_dossier_guard_count`, or `africa_dossier_settlement_count`.
- Post-audit validation confirmed the decision and scripted GUI no longer call `africa_start_selected_dossier_survey` directly, and that the GUI effect checks `africa_archive_guard_mission_active` before spending dossier costs.

## Auditor Request

Audit the changed decision/focus/trigger/effect/localisation/doc surfaces for:

- deadline mission context correctness,
- repeatable mission lifecycle behavior,
- stale flag/variable cleanup,
- Continental Register and World Is One gate alignment,
- localisation accuracy,
- exploit or deadlock risks.

Small patch-capable fixes are allowed if they are local to this tranche.
