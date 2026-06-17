# Event 012 Authority Atlas Macro-Region Guard Audit Handoff

Date: 2026-06-17

## Scope

Audited the bounded Event 012 Africa Authority Atlas decision/focus tranche from the parent handoff:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_authority_atlas_macro_region_guard_parent_handoff.md`
- `common/script_constants/012_africa_constants.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`

Also inspected the directly related scripted GUI dossier button because it calls into the same Authority Atlas decision surface.

## Patch Status

Patched small local issues.

Changed files:

- `common/scripted_effects/012_africa_effects.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/scripted_guis/012_africa_scripted_gui.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- this handoff

Changed ids and helpers:

- `africa_open_next_historical_dossier`
- `africa_gui_start_dossier_button_click`
- `africa_gui_start_dossier_button_click_enabled`
- `africa_continent_sponsor_readiness_available_tt`
- `africa_certify_continent_unifiers_for_world_is_one_req_tt`
- `africa_prepare_world_is_one_gate_req_tt`

## Issue List

High - patched: `common/scripted_guis/012_africa_scripted_gui.txt` had the old dossier-start gate and did not block `africa_gui_start_dossier_button_click_enabled` while `africa_archive_guard_mission_active` was set. The GUI click effect also called `africa_start_selected_dossier_survey` directly, so the decision button could be blocked while the GUI route still started a new survey during an active guard deadline. The shared `africa_open_next_historical_dossier` helper also lacked an internal guard check, leaving future non-decision callers unsafe.

Medium - patched: sponsor readiness, certification, World Is One gate localisation, and the event doc described historical dossier readiness without the all-six macro-region line requirement. Gameplay already used `has_africa_continental_register_dossier_coverage`; text now matches it.

Low - no patch: `AFR_first_nonhuman_envoys` still requires only `africa_minimum_historical_dossiers_ready`, not the macro-region trigger. This is outside the explicitly requested Continental Register / `AFR_africa_is_one` / World Is One readiness surface, but the parent should decide whether the high-chaos route may intentionally open after 24 dossiers even if all six macro-region lines are not settled.

## Before And After

Before:

- The normal `africa_open_next_historical_dossier` decision blocked a new survey during `africa_archive_guard_mission_active`.
- The scripted GUI dossier button did not block that state and called `africa_start_selected_dossier_survey` directly.
- The shared `africa_open_next_historical_dossier` helper did not enforce the guard deadline lock itself.
- Player-facing readiness text could imply that the dossier threshold alone was enough for late sponsor and World Is One readiness.

After:

- `africa_open_next_historical_dossier` now checks Authority Atlas access, dossier office, not-all-opened, no selected opened dossier, no active survey, and no active archive guard mission before starting the survey.
- The decision and scripted GUI dossier button both route through `africa_open_next_historical_dossier`.
- The scripted GUI dossier button is disabled while `africa_archive_guard_mission_active` is set.
- Sponsor readiness, certification, World Is One gate localisation, and docs explicitly mention all six macro-region lines.

## Decision Category Lifecycle Notes

Authority Atlas lifecycle is coherent after the patch:

- `AFR_authority_atlas` opens the category and registers the catalog.
- `AFR_dossier_selection_office` selects the first unopened historical dossier.
- The dossier start decision and GUI button both start only one survey at a time and now respect active guard deadline state.
- Survey success opens the dossier, stores guard mission context, and starts the guard deadline.
- Local office, guard, and settlement decisions resolve the selected opened dossier.
- Settlement records macro-region progress and selects the next unopened dossier, but the next survey remains blocked until the active guard mission completes or times out.
- `AFR_continental_register`, `AFR_africa_is_one`, sponsor readiness, certification, and the final gate all route through the reusable macro-region coverage trigger where expected.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_selected_dossier_survey_mission` | Africa unifier | `africa_authority_atlas_category` | selected historical dossier representative old-seat state | keep selected dossier seat controlled or Charter-protected | 120 days | opens/surveys selected dossier and starts guard context | marks survey failed, raises Restoration Debt and Local Sovereignty pressure | low; it is a setup mission, not a duplicate of the guard deadline |
| `africa_archive_guard_deadline_mission` | Africa unifier | `africa_authority_atlas_category` | stored mission dossier id and stored representative seat state | mission dossier local office, guard, settlement flag, stored seat secured, plus preserved global secured-seat proof | 180 days | raises Archive Mandate and Old-Seat Legitimacy, clears active context | raises Restoration Debt and Local Sovereignty pressure, clears active context | low after patch; exact dossier flags prevent aggregate-office/guard/settlement completion |

## Cost And Requirement Clarity Notes

- Dossier start uses PP plus support equipment through the decision and scripted GUI surfaces. The helper itself only starts the survey and is now guarded against unsafe direct calls.
- Authority Atlas category localisation exposes opened dossiers, macro-region count, secured seats, active dossier, active profile, active seat, and direct Archive seal status.
- Guard deadline tooltip is concise and correctly describes the mission-specific office, guard, settlement, and representative seat requirement.
- Late sponsor and World Is One tooltips now mention all six macro-region lines.

## AI Validity And Route-Lock Notes

- No invalid country targets found in the audited guard mission surface.
- `has_africa_archive_guard_mission_dossier_work_ready` uses stored country variables and generated flags, not stale `FROM`/target scope.
- The route lock for the next dossier survey is now present in the decision, shared helper, and scripted GUI enablement.
- `AFR_continental_register` and `AFR_africa_is_one` use the macro-region trigger; `AFR_the_world_is_one` uses `can_africa_start_world_is_one_gate`, which inherits it through `can_africa_prepare_world_is_one_gate`.

## Localisation And Tooltip Gaps

Patched:

- `africa_continent_sponsor_readiness_available_tt`
- `africa_certify_continent_unifiers_for_world_is_one_req_tt`
- `africa_prepare_world_is_one_gate_req_tt`
- `docs/events/012_africa_foundation.md` Authority Atlas, mission, sponsor readiness, and certification wording.

Remaining:

- The scripted GUI value card still shows dossier count and Bestiary count but not macro-region count. The Authority Atlas category header does expose macro-region progress, satisfying the parent request. Adding macro-region progress to the GUI card would be a UI layout choice for the parent, not required for this tranche.

## Cleanup And Exploit-Risk Notes

- Survey success stores `africa_archive_guard_mission_dossier_id` and `africa_archive_guard_mission_seat_state`.
- Guard mission cancel, success, and failure all call `africa_clear_archive_guard_mission_context`.
- Starting a guard mission clears stale success/failure flags.
- The deadline cannot be satisfied solely by aggregate `africa_dossier_local_office_count`, `africa_dossier_guard_count`, or `africa_dossier_settlement_count`; it checks generated flags for the stored dossier id.
- The remaining persistent `africa_dossier_seat_secure_count` proof is not sufficient by itself because the stored representative seat state must also currently be secured.
- No free unit, equipment farming, war-goal spam, or core spam issue was found in this bounded guard/macro-region tranche.

## Validation

Meaningful checks run:

- Confirmed both dossier-start call sites now use `africa_open_next_historical_dossier = yes` and no decision or scripted GUI call still invokes `africa_start_selected_dossier_survey = yes` directly.
- Confirmed `africa_gui_start_dossier_button_click_enabled` and `africa_open_next_historical_dossier` both block `africa_archive_guard_mission_active`.
- Confirmed `AFR_continental_register`, `AFR_africa_is_one`, sponsor readiness, certification, and final World Is One gate route through `has_africa_continental_register_dossier_coverage` directly or through `can_africa_prepare_world_is_one_gate`.
- Confirmed localisation file still has UTF-8 BOM after patch.
- `git diff --check -- common/scripted_effects/012_africa_effects.txt common/decisions/012_africa_decisions.txt common/scripted_guis/012_africa_scripted_gui.txt localisation/english/012_african_union_l_english.yml docs/events/012_africa_foundation.md` returned clean.

Skipped:

- No in-game run was performed.
- No broad Event 012 validation was attempted because the worktree contains extensive unrelated dirty parent/peer changes.

## Residual Risks

- The direct helper now no-ops if called while blocked, but scripted GUI effects spend costs before calling it. The GUI enable trigger prevents normal player clicks during an active guard mission; if another caller bypasses scripted GUI enabled-state checks, it could still spend before the helper no-ops. I found no such caller in the bounded search.
- `AFR_first_nonhuman_envoys` remains tied to opened dossier count only. Parent should confirm whether high-chaos envoys intentionally do not require all six macro-region lines.
- I did not commit because this is a subagent audit handoff inside a heavily dirty shared worktree.
