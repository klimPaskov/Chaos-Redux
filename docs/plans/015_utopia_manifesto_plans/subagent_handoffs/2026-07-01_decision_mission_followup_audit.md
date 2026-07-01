# Event 015 Decision and Mission Follow-up Audit

Date: 2026-07-01
Agent: chaos-redux decision/mission subagent
Mode: bounded audit with small local patch

## Scope

Audited Event 015 `utopia_manifesto` decisions, missions, timed objectives, costs, tooltips, AI behavior, cleanup, balance, and exploit risk.

Primary files inspected:

- `docs/specs/015_utopia_manifesto_specs/`
- `docs/plans/015_utopia_manifesto_plans/2026-07-01_final_depth_audit_addendum.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_decision_mission_audit.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_scripted_system_architect.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_decision_idea_icon_regeneration.md`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
- `interface/015_utopia_manifesto_ledger.gui`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `docs/events/015_utopia_manifesto.md`
- `docs/assets/015_utopia_manifesto/manifest.md`

Required references consulted:

- Offline wiki pages for data structures, decisions, triggers, effects, modifiers, localisation, scopes, on actions, events, ideas, AI, scripted GUI, and interface modding.
- Vanilla decision documentation and precedents in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`, including decision docs, scripted GUI docs, formable decisions, border conflict decisions, foreign influence decisions, and Ethiopia decision precedents.

## Files Changed

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_decision_mission_followup_audit.md`

## Changed IDs

- `mission_utopia_harvest_rotation`
- `mission_utopia_household_guard`
- `mission_utopia_boundary_arbitration`
- `mission_utopia_marked_district_survey`
- `mission_utopia_league_aid_corridor`
- `mission_utopia_renunciation_vote`
- `decision_utopia_local_households`
- `utopia_manifesto_apply_storehouse_audit_decision`

## Patch Summary

### Timed missions now resolve through timeout handlers

Before:

- Five timed missions used `available = { utopia_manifesto_*_objective_ready = yes }`.
- `mission_utopia_renunciation_vote` had no `available` block.
- In HOI4 missions, `available` is the completion condition for non-selectable missions. These missions were written as if `available` were only an objective display, so they could complete before timeout or complete immediately without running the intended `timeout_effect` success/failure resolver.

After:

- All six timeout-driven missions use `available = { hidden_trigger = { always = no } }`.
- Their scripted objective checks remain in the corresponding timeout resolver effects.
- This preserves the intended timed-objective behavior: success/failure is evaluated at deadline.

Affected missions:

- `mission_utopia_harvest_rotation`
- `mission_utopia_household_guard`
- `mission_utopia_boundary_arbitration`
- `mission_utopia_marked_district_survey`
- `mission_utopia_league_aid_corridor`
- `mission_utopia_renunciation_vote`

### Household Councils no longer target arbitrary occupied non-core states

Before:

- `decision_utopia_local_households` allowed any controlled non-core state because `NOT = { is_core_of = ROOT }` was inside an `OR` with Needful Land and Common Administration flags.
- This bypassed the intended postwar administration lifecycle.

After:

- The state must be controlled, non-core, not already assigned Household Councils, and have either `utopia_manifesto_needful_land_claimed` or `utopia_manifesto_common_administration`.
- This blocks the exploit path where any occupied non-core state could receive councils without prior claim/admin work.

### Storehouse audit cooldown uses a file-local duration constant

Before:

- `utopia_manifesto_apply_storehouse_audit_decision` set a temp variable from a script constant and passed the temp variable into `set_country_flag days`.
- Timed flag `days` fields are a known weak parser surface for variable/constant injection.

After:

- Added `@utopia_storehouse_audit_cooldown_days = 60` in `common/scripted_effects/015_utopia_manifesto_effects.txt`.
- The timed flag now uses `days = @utopia_storehouse_audit_cooldown_days`.

## Severity-Sorted Findings

### Critical - Patched

1. Timeout mission completion semantics were wrong for six missions.
   - Owner: ROOT country.
   - Category: `utopia_manifesto_ledger_category`.
   - Risk: timed objective chains could resolve outside their intended success/failure effects.
   - Patch: all six timeout missions now have impossible hidden `available` and resolve through `timeout_effect`.

2. `decision_utopia_local_households` could be applied to any controlled non-core state.
   - Owner: ROOT country with a state target.
   - Category: `utopia_manifesto_ledger_category`.
   - Risk: bypassed Needful Land and Common Administration lifecycle.
   - Patch: target now requires Needful Land claim or Common Administration plus non-core status.

### High - Not Patched

1. Boundary, marked district, and League aid missions use global event targets.
   - Files/ids: `utopia_manifesto_start_boundary_arbitration_mission`, `utopia_manifesto_start_marked_district_survey_mission`, `utopia_manifesto_start_league_aid_mission`.
   - Risk: if more than one country can run Event 015, global event targets can be overwritten by another country's mission before timeout.
   - Impact: wrong state/target could be resolved, cleared, claimed, or rewarded.
   - Recommended fix: replace global event targets with per-root target storage. Use keyed state/country flags or arrays and resolve by scanning the rooted active mission owner, or add a narrow scripted target-storage helper designed for concurrent countries.

2. Relationship flags are generic instead of keyed to the acting ROOT.
   - Files/ids: `utopia_manifesto_apply_foreign_aid_decision`, `utopia_manifesto_apply_send_magistrates_decision`, `utopia_manifesto_apply_friend_recognition_decision`, `utopia_manifesto_resolve_league_aid_mission`.
   - Flags: `utopia_manifesto_aid_from_root`, `utopia_manifesto_magistrates_from_root`, `utopia_manifesto_friend_of_root`, `utopia_manifesto_league_aid_from_root`.
   - Risk: target-country flags can misrepresent which Utopia acted when multiple Utopian countries exist.
   - Current mitigating factor: per-ROOT arrays are used for some gating, so this is more cleanup/identity/tooltip risk than an immediate repeat-decision blocker.
   - Recommended fix: use the existing relationship helper pattern from the architect handoff or add keyed targeted flags by `@ROOT`.

3. Timeout objective conditions are now hidden from the mission `available` block.
   - This is correct for timeout-only behavior, but the UI now relies on description/timeout text to communicate objectives.
   - Localisation keys needing a wording pass:
     - `mission_utopia_harvest_rotation_desc`
     - `utopia_harvest_rotation_timeout_tt`
     - `mission_utopia_household_guard_desc`
     - `utopia_guard_shore_timeout_tt`
     - `mission_utopia_boundary_arbitration_desc`
     - `utopia_boundary_arbitration_timeout_tt`
     - `mission_utopia_marked_district_survey_desc`
     - `utopia_marked_district_timeout_tt`
     - `mission_utopia_league_aid_corridor_desc`
     - `utopia_league_aid_corridor_timeout_tt`
     - `mission_utopia_renunciation_vote_desc`
     - `utopia_renunciation_vote_timeout_tt`
   - Recommended fix: explicitly describe success requirements in mission descriptions, because the success checks no longer appear as `available` tooltips.

### Medium - Not Patched

1. `decision_utopia_guard_shore` uses the foreign aid cost helper.
   - Files/ids: `decision_utopia_guard_shore`, `utopia_manifesto_start_guard_mission`, `utopia_manifesto_can_pay_foreign_aid`, `utopia_manifesto_pay_foreign_aid_cost`.
   - Current cost: convoys, support equipment, and war support through the foreign-aid helper.
   - Risk: the cost may be intentional for shore patrol logistics, but it reads as a copied aid cost rather than a guard-specific cost.
   - Recommended fix: either rename/clarify localisation around convoy-supported sea-road guard cost, or create a guard-shore cost helper using convoy, infantry equipment, manpower, or command power.

2. League aid corridor has a double-stockpile requirement but a single spend.
   - Files/ids: `utopia_manifesto_start_league_aid_mission`, `utopia_manifesto_league_aid_objective_ready`.
   - Behavior: cost is paid at start, but success at timeout requires the country to still satisfy `utopia_manifesto_can_pay_league_aid`.
   - Risk: this can be a legitimate reserve objective, but it needs clearer tooltip wording because the player may read it as paying once while the mission silently requires maintained reserves.

3. Project cleanup can leave active project counters stale if invoked directly.
   - File/id: `utopia_manifesto_cleanup_project_state`.
   - Behavior: clears active project state flags but does not decrement `utopia_manifesto_active_storehouse_projects` or `utopia_manifesto_active_integration_projects`.
   - Recommended fix: either only call completion helpers for cleanup, or make cleanup decrement counters when the corresponding active flag was present.

4. Rejection cleanup clears ledger variables and some global targets but does not clear every active mission flag.
   - File/id: `utopia_manifesto_clear_acceptance_state`.
   - Risk: if this helper can run after decisions have started, stale active mission flags can remain.
   - Recommended fix: clear all Event 015 active mission flags in the acceptance-state cleanup helper.

5. AI weights are present but mostly broad.
   - Current strengths: many decisions have `ai_will_do`, target validity blocks majors, unsafe war/capitulation targets, stronger neighbors, and route-unsafe states.
   - Remaining risk: country-target decisions rely on target triggers and simple base/factor weights. The AI does not deeply compare route pressure, mission congestion, or whether reserve-objective missions would starve other Event 015 projects.

## Decision Category Lifecycle Notes

- `utopia_manifesto_ledger_category` appears after `utopia_manifesto_has_ledger = yes` and uses `visible_when_empty = yes`.
- The category correctly attaches `utopia_manifesto_ledger_scripted_gui`.
- The ledger GUI is display-only. There are no scripted GUI buttons, so there are no missing scripted-GUI button costs/effects/AI equivalents in the current implementation.
- Decisions are gated by completed focuses and ledger flags. Storehouse and integration projects use active project caps.
- Route-aware decisions exist for Needful Land, Marked Bounds, League behavior, and renunciation.

## Mission Quality Notes

### `mission_utopia_harvest_rotation`

- Owner: ROOT.
- Category: `utopia_manifesto_ledger_category`.
- Region/target: country mission.
- Requirement: mission active flag; timeout resolver checks ledger, reserve resources, and full control of core states.
- Duration: `@utopia_harvest_rotation_days` / 110.
- Success: lowers Need and improves Surplus.
- Failure: raises Need and lowers Consent.
- Duplicate risk: low; active flag blocks duplicate mission.

### `mission_utopia_household_guard`

- Owner: ROOT.
- Category: `utopia_manifesto_ledger_category`.
- Region/target: country mission.
- Requirement: mission active flag; timeout resolver checks ledger, Overreach safety, and war/defense pressure.
- Duration: `@utopia_guard_mission_days` / 120.
- Success: records contained defense and improves ledger state.
- Failure: raises Foreign Suspicion.
- Duplicate risk: low; active flag blocks duplicate mission.
- Remaining risk: start cost uses the foreign-aid helper.

### `mission_utopia_boundary_arbitration`

- Owner: ROOT.
- Category: `utopia_manifesto_ledger_category`.
- Region/target: neighbor country and selected target-owned state.
- Requirement: Need proof, safe target, valid state, Overreach/Suspicion safety or supporting focus.
- Duration: `@utopia_arbitration_days` / 150.
- Success: adds a witnessed claim only; no core.
- Failure: raises Need, Foreign Suspicion, and Overreach.
- Duplicate risk: medium-high in multi-Utopia games due global event targets.

### `mission_utopia_marked_district_survey`

- Owner: ROOT.
- Category: `utopia_manifesto_ledger_category`.
- Region/target: neighbor country and selected target-owned state.
- Requirement: Marked Bounds route, safe target, valid state.
- Duration: `@utopia_marked_survey_days` / 120.
- Success: adds a risky claim and forced-settlement risk; no core.
- Failure: raises Need and Foreign Suspicion.
- Duplicate risk: medium-high in multi-Utopia games due global event targets.

### `mission_utopia_league_aid_corridor`

- Owner: ROOT.
- Category: `utopia_manifesto_ledger_category`.
- Region/target: neighbor country.
- Requirement: League unlocked, target valid, Surplus stable, suspicion and League Confidence safe.
- Duration: `@utopia_league_aid_days` / 150.
- Success: adds aid, League member tracking, Consent, and League Confidence.
- Failure: raises Foreign Suspicion and lowers League Confidence.
- Duplicate risk: medium-high in multi-Utopia games due global event target.

### `mission_utopia_renunciation_vote`

- Owner: ROOT.
- Category: `utopia_manifesto_ledger_category`.
- Region/target: country mission.
- Requirement: starts only while Overreach is high enough to need renunciation; succeeds if Consent is stable and Overreach is contained at timeout.
- Duration: `@utopia_renunciation_vote_days` / 120.
- Success: sets renunciation and exits the hard clause.
- Failure: marks failed vote and raises Consent/Overreach pressure.
- Duplicate risk: low; active flag blocks duplicate mission.

## Cost and Requirement Clarity Notes

- The decision surface is not a political-power store. No Event 015 decision inspected uses political power as the main exchange.
- Costs are varied and concrete: support equipment, infantry equipment, motorized equipment, trains, convoys, manpower, command power, army XP, stability, war support, compliance/resistance, state control, project caps, and timed missions.
- Some actions intentionally have no direct material cost (`decision_utopia_storehouse_audit`, `decision_utopia_collect_petitions`, `decision_utopia_recognize_friend`). These are acceptable as ledger/social actions, but should remain limited by cooldowns, focus gates, arrays, or ledger conditions.
- Needful Land claims are not instant free cores. Arbitration and marked survey add claims only after timed mission resolution. Cores are only possible through integration completion and compliance/Consent/Overreach gates.

## AI Validity and Route-Lock Notes

- Needful Land target triggers block majors, special/nonhuman countries, capitulated countries, unsafe wars, subjects of ROOT, and stronger factory/division targets.
- Marked Bounds has separate route pressure and higher Overreach/Suspicion impact.
- League behavior uses League Confidence in ledger variables and gates League aid target validity.
- Active mission caps are present for the main timed mission families.
- Remaining AI improvement: add more resource-aware and route-aware `ai_will_do` modifiers for missions that require maintained reserves at timeout.

## Localisation and Tooltip Gaps

- Ledger values are visible in `interface/015_utopia_manifesto_ledger.gui` through:
  - `utopia_manifesto_ledger_gui_values_left`
  - `utopia_manifesto_ledger_gui_values_right`
  - `utopia_manifesto_ledger_gui_footer`
- The ledger includes Need, Consent, Surplus, Overreach, Vocation Balance, Foreign Suspicion, and League Confidence.
- Because mission success checks now remain in timeout effects, the mission descriptions should explicitly list what must remain true until timeout. Exact keys are listed in the high-severity localisation finding above.

## Cleanup and Exploit-Risk Notes

- Patched exploit: `decision_utopia_local_households` can no longer skip Needful Land/Common Administration state lifecycle.
- Patched timing risk: timeout missions no longer resolve through `available` before their timeout effects.
- Remaining cleanup risk: global event targets and generic relationship flags are unsafe for concurrent Event 015 countries.
- Remaining cleanup risk: active project counters can desync if `utopia_manifesto_cleanup_project_state` is used outside normal completion.
- Remaining exploit risk: generic relationship flags can make target countries appear to have been helped/friended by an unspecified Utopia.

## Validation Run

Task-specific checks performed:

- Confirmed no Event 015 mission still uses `available = { utopia_manifesto_*_objective_ready = yes }`.
- Confirmed all six timeout missions now have `available = { hidden_trigger = { always = no } }`.
- Confirmed `mission_utopia_renunciation_vote` now has a blocked `available` block.
- Confirmed all `activate_mission = ...` IDs in Event 015 effects resolve to defined mission IDs in Event 015 decisions.
- Confirmed the old `utopia_manifesto_storehouse_audit_days` variable path no longer exists.
- Confirmed the inspected decision/effect surface has no political-power exchange.

Skipped validation:

- No in-game runtime validation was performed.
- No full repository parser/load validation was performed from this subagent audit.
- Localisation was not patched because the task scope explicitly barred localisation edits.
- The global-event-target rewrite was not patched because it is broader than a small local decision fix and needs a designed per-root target-storage pattern.

## Remaining Recommended Fixes

1. Replace global event targets in boundary arbitration, marked district survey, and League aid corridor with per-root mission target storage.
2. Convert generic relationship flags to keyed targeted flags or helper calls tied to the acting ROOT.
3. Add explicit mission objective wording to the mission description/timeout localisation keys listed above.
4. Decide whether `decision_utopia_guard_shore` should keep foreign-aid costs or receive a dedicated guard-shore cost helper.
5. Make `utopia_manifesto_cleanup_project_state` counter-safe, or restrict it to contexts where active project counters are handled elsewhere.
6. Add cleanup for every active Event 015 mission flag in the acceptance-state cleanup helper if that helper can run after decision activation.
7. Add more AI reserve-awareness for League aid and other missions that require maintained resources at timeout.

This handoff does not claim overall Event 015 completion.
