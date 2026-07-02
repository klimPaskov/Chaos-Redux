# Event 014 Cannibalism Decision and Mission Audit Handoff

Date: 2026-07-01
Mode: patch-capable decision and mission audit
Scope: Event 014 only

## Sources Read

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Vanilla docs: `common/decisions/_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`
- Vanilla decision precedents for missions, `days_mission_timeout`, `complete_effect`, `timeout_effect`, `target_trigger`, and equipment/resource gates
- Event 014 primary files and `events/014_cannibalism.txt` for spread-response wiring verification

## Changed Files

- `common/script_constants/014_cannibalism_constants.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_event014_decision_mission_audit_handoff.md`

## Changed Identifiers

Decisions and triggers:

- `cannibalism_can_pay_truth_cost`
- `cannibalism_can_pay_exploit_cost`
- `cannibalism_can_pay_break_cult_cost`
- `cannibalism_country_has_outbreak`
- `cannibalism_response_visible`

Effects:

- `cannibalism_start_spread_outbreak`
- `cannibalism_spend_break_cult_cost`
- `cannibalism_spend_exploit_cost` through newly enforced cost gates
- `cannibalism_try_next_evolutions`
- `cannibalism_country_containment_failure`

Constants:

- Updated `cannibalism_deadline.guard_rail_days`
- Updated `cannibalism_deadline.hospital_audit_days`
- Updated `cannibalism_deadline.prison_kitchen_days`
- Updated `cannibalism_deadline.island_inspection_days`
- Updated `cannibalism_deadline.evacuation_days`
- Updated `cannibalism_deadline.ritual_cell_days`
- Updated `cannibalism_deadline.commune_retake_days`
- Updated `cannibalism_deadline.mainland_copying_days`
- Updated `cannibalism_deadline.terror_unit_days`
- Added `cannibalism_spread_default.*`
- Added `cannibalism_evolution_threshold.*`
- Added `cannibalism_death_toll.*`
- Added `cannibalism_decision_cost.truth_war_support_gate`
- Added `cannibalism_decision_cost.exploit_stability_gate`
- Added `cannibalism_decision_cost.exploit_war_support_gate`
- Added `cannibalism_decision_cost.break_cult_army_xp_gate`
- Added `cannibalism_decision_cost.break_cult_army_xp_spend`
- Added `cannibalism_decision_cost.break_cult_stability_gate`
- Added `cannibalism_decision_cost.break_cult_stability_spend`
- Added `cannibalism_decision_cost.break_cult_war_support_gate`
- Added `cannibalism_decision_cost.break_cult_war_support_spend`

Localisation:

- `cannibalism_secure_field_kitchens_available_tt`
- `cannibalism_secure_field_kitchens_cost_text`
- `cannibalism_rotate_compromised_units_available_tt`
- `cannibalism_rotate_compromised_units_cost_text`
- `cannibalism_run_ration_convoy_available_tt`
- `cannibalism_run_ration_convoy_cost_text`
- `cannibalism_audit_field_hospitals_available_tt`
- `cannibalism_audit_field_hospitals_cost_text`
- `cannibalism_military_police_sweep_available_tt`
- `cannibalism_military_police_sweep_cost_text`
- `cannibalism_prison_transfer_freeze_available_tt`
- `cannibalism_prison_transfer_freeze_cost_text`
- `cannibalism_chaplain_political_officer_work_available_tt`
- `cannibalism_chaplain_political_officer_work_cost_text`
- `cannibalism_public_truth_commission_available_tt`
- `cannibalism_public_truth_commission_cost_text`
- `cannibalism_inspect_silent_island_available_tt`
- `cannibalism_inspect_silent_island_cost_text`
- `cannibalism_emergency_evacuation_available_tt`
- `cannibalism_emergency_evacuation_cost_text`
- `cannibalism_break_ritual_cell_available_tt`
- `cannibalism_break_ritual_cell_cost_text`
- `cannibalism_retake_commune_available_tt`
- `cannibalism_retake_commune_cost_text`
- `cannibalism_stop_mainland_copying_available_tt`
- `cannibalism_stop_mainland_copying_cost_text`
- `cannibalism_dismantle_terror_units_available_tt`
- `cannibalism_dismantle_terror_units_cost_text`
- `cannibalism_exploit_terror_units_available_tt`
- `cannibalism_exploit_terror_units_cost_text`
- `cannibalism_break_with_cult_available_tt`
- `cannibalism_break_with_cult_cost_text`

## Before and After Behavior

Before:

- Several missions had 40 to 70 day deadlines, below the decision matrix's 90 to 180 day action window.
- `cannibalism_exploit_terror_units` was gated only by Army XP and Command Power even though the design requires exploitation to be dangerous and socially costly.
- `cannibalism_break_with_cult` spent only Command Power, while localisation implied broader institutional strain.
- Public truth costs spent stability but did not require war support capacity.
- Cost localisation advertised resources that were not actually consumed and omitted resources that were consumed.
- Event 014 response category visibility did not explicitly close under the `world_end` global flag.
- Spread default values, evolution thresholds, and death-toll increments used raw numbers inside scripted effects.

After:

- Timed missions use 95 to 140 day deadlines, aligned with the matrix and decision-mission skill guidance.
- Exploiting terror units now requires and spends stability and war support, and requires supplied divisions in addition to Army XP and Command Power.
- Breaking with the cult now requires and spends Army XP, stability, and war support in addition to Command Power.
- Public truth now requires enough war support before spending it.
- Player-facing cost and requirement text matches actual triggers and spend effects.
- World-end closure hides the response category and cancels outbreak-scoped mission availability through existing outbreak checks.
- Spread defaults, evolution thresholds, and death tallies are centralized in script constants.

## Issue List Sorted by Severity

High, fixed: Exploit route was too cheap and under-gated. It could be taken without supplied field commitment or enough stability/war support, making exploitation less dangerous than the spec requires. Fixed in `cannibalism_can_pay_exploit_cost`, `cannibalism_decision_cost.*`, and localisation.

High, fixed: Mission durations were too compressed for meaningful player action. The matrix expects extended deadlines; several implemented missions were 40 to 70 days. Fixed in `cannibalism_deadline.*`.

High, fixed: Cost and requirement localisation did not match implementation. Some tooltips listed phantom costs, while several actual costs were missing from the player-facing text. Fixed across Event 014 cost tooltip keys.

Medium, fixed: `break_with_cult` presented itself as a strategic rupture but only spent Command Power. Fixed with Army XP, stability, and war support gates/spends.

Medium, fixed: Event 014 response category did not explicitly close once world-end state exists. Fixed in `cannibalism_country_has_outbreak` and `cannibalism_response_visible`.

Medium, fixed: Spread starts, evolution thresholds, and death increments used raw magic numbers in effects. Fixed with `cannibalism_spread_default`, `cannibalism_evolution_threshold`, and `cannibalism_death_toll` constants.

Medium, remaining: Mission regions are mostly abstract country-level checks rather than named state, rail, island, prison, or commune targets. The implementation uses supplied divisions, controlled states, naval access, and outbreak meters, but does not maintain explicit target state/event-target mission geography. Fixing this would require a broader target-selection layer, so it was not patched.

Low, remaining: Outbreak-country AI relies on per-decision `ai_will_do` rather than a dedicated outbreak AI strategy file. CBL has strategy entries, and each decision has weights, but a broader AI production/supply posture would be outside a narrow audit patch.

Low, remaining: Some cost localisation values are static text. They now match constants, but future tuning still requires synchronizing localisation unless scripted localisation is added.

## Decision Category Lifecycle Notes

- Owner: every active outbreak country.
- Category: `cannibalism_frontline_hunger_category`.
- Visibility: now requires outbreak visibility and not `world_end`.
- Empty visibility: `visible_when_empty = yes`, which is acceptable because the category is the response surface while outbreak flags exist.
- Start: origin and spread effects call outbreak setup and activate the containment mission.
- Local defeat: `cannibalism_country_containment_success` clears outbreak flags, removes containment mission, removes outbreak ideas, clears pressure on controlled states, updates global counters, and checks global defeat.
- Failure/escalation: `cannibalism_country_containment_failure` evolves the outbreak, increases death and spread pressure, and can attempt spread.
- Spread-country response: verified in `events/014_cannibalism.txt`; `chaosx.nr14.4` calls `cannibalism_start_spread_outbreak`, so each spread country receives its own response variables and containment mission.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cannibalism_containment_deadline_mission` | Outbreak country | Frontline hunger | Country outbreak | Raise containment and keep hunger/cult below crisis thresholds | 95 days | Local containment success, outbreak cleanup | Evolution, spread/deaths pressure | Low; one active flag controls mission |
| `cannibalism_guard_ration_rail_mission` | Outbreak country | Frontline hunger | Abstract supply/rail surface | Maintain supplied field commitment | 100 days | Hunger and fear pressure reduced | Transfer zone/spread pressure | Low; one active flag |
| `cannibalism_audit_field_hospitals_mission` | Outbreak country | Frontline hunger | Abstract hospital network | Keep supplied commitment and prevent cult/spread failure threshold | 105 days | Cult/network pressure reduced | Hospital network worsens | Low; one active flag |
| `cannibalism_seal_prison_kitchens_mission` | Outbreak country | Frontline hunger | Controlled response territory | Maintain controlled state while suppressing cult pressure | 95 days | Prison kitchen vector suppressed | Cult/spread pressure worsens | Low; one active flag |
| `cannibalism_inspect_silent_island_mission` | Outbreak country | Frontline hunger | Naval-access island surface | Preserve naval access | 120 days | Island network suppressed | Island branch worsens | Low; one active flag |
| `cannibalism_evacuation_mission` | Outbreak country | Frontline hunger | Naval or supplied evacuation corridor | Keep naval access or supplied divisions | 105 days | Evacuation reduces fear/hunger pressure | Evacuation failure worsens deaths/spread | Low; one active flag |
| `cannibalism_break_ritual_cell_mission` | Outbreak country | Frontline hunger | Abstract ritual cell | Maintain supplied field commitment and prevent cult threshold | 110 days | Ritual cell broken | Cult route worsens | Low; one active flag |
| `cannibalism_retake_commune_mission` | Outbreak country | Frontline hunger | Controlled response territory | Maintain controlled response state | 140 days | Commune pressure reduced | Commune route worsens | Low; one active flag |
| `cannibalism_stop_mainland_copying_mission` | Outbreak country | Frontline hunger | Mainland copying network | Keep spread below failure threshold | 120 days | Copying network suppressed | New spread attempt | Low; one active flag |
| `cannibalism_dismantle_terror_units_mission` | Outbreak country | Frontline hunger | Field units | Maintain supplied field commitment and stop resonance failure | 100 days | Terror units dismantled | Terror unit route worsens | Low; one active flag |

The `is_good = yes` missions intentionally use `available` as the failure condition and `timeout_effect` as success. This matches the vanilla documentation behavior for good missions, where the player must prevent the failure condition until the timer expires.

## Cost and Requirement Clarity Notes

- No passive political power store was found in the Event 014 decision surface.
- Concrete costs now cover Command Power, Army XP, infantry equipment, support equipment, trains, convoys, fuel, manpower, stability, war support, supplied divisions, controlled state access, naval access, and mission deadlines.
- The core resource gates are centralized through `cannibalism_decision_cost.*`.
- The mission deadlines are centralized through `cannibalism_deadline.*`.
- Remaining clarity gap: static localisation numbers must be manually kept in sync with constants unless scripted localisation is added later.

## AI Validity and Route-Lock Notes

- Every active decision inspected has an `ai_will_do` block.
- Exploit behavior remains route-locked and now requires deeper resource/state commitment; democratic AI is weighted down and fascist/low-stability patterns remain more likely.
- World-end route remains CBL-only and gated by global table pressure, cult nodes, communes, and Hannibal or an accepted unifier.
- Spread targets exclude special subjects, nonhuman/special countries, defeated/resolved countries, capitulated countries, existing active outbreak countries, and `world_end`.
- CBL has dedicated AI strategy entries in `common/ai_strategy/014_cannibalism.txt`.
- Remaining AI gap: outbreak countries do not have a dedicated AI strategy that changes production, convoy, train, or supply priorities during response. This was not patched because it would be a broader balance/AI pass.

## Localisation and Tooltip Gaps

- Cost text and availability text were patched to match actual gates and spend effects.
- Existing custom trigger tooltip keys are used for long decision availability blocks.
- No scripted GUI buttons were found in the Event 014 decision surface.
- Remaining gap: mission text does not name concrete state/rail/island targets because the decision implementation does not persist those target scopes.

## Cleanup and Exploit-Risk Notes

- Local containment can defeat the outbreak through `cannibalism_country_containment_success`.
- Successful containment removes outbreak ideas, clears the containment mission, clears outbreak state pressure on controlled states, increments contained-country counters, and rechecks global defeat.
- Side missions are gated by outbreak visibility and their active flags; they stop being available after containment/world-end state.
- Exploitation is now more dangerous: it costs Army XP, Command Power, stability, war support, supplied field commitment, adds deaths, increases resonance, and is route flagged.
- Commune reinforcement loops appear blocked from the decision/mission route because commune creation requires `cannibalism_can_form_commune_from_country`, which excludes existing CBL.
- Remaining cleanup risk: state pressure cleanup loops over controlled states only. If contaminated states changed controller before cleanup, stale modifiers/flags could remain with the new controller until their own expiry or later cleanup. A robust fix would need a state-control cleanup hook or target registry and is outside this narrow patch.

## Concrete Recommended Fixes

Applied:

- `common/script_constants/014_cannibalism_constants.txt`: lengthened mission deadlines and centralized spread defaults, evolution thresholds, death tallies, and missing cost gates/spends.
- `common/scripted_triggers/014_cannibalism_triggers.txt`: tightened truth, exploit, and break-cult cost gates; closed outbreak visibility under `world_end`.
- `common/scripted_effects/014_cannibalism_effects.txt`: spent the new break-cult costs and replaced raw Event 014 threshold/death/default values with constants.
- `localisation/english/014_cannibalism_l_english.yml`: aligned all decision availability and cost tooltip keys with actual implementation.

Recommended but not patched:

- Add explicit mission target-state selection for rail, prison, island, commune, and hospital surfaces if the parent wants more map-readable missions.
- Add an outbreak-country AI strategy package for supply, trains, convoys, and support equipment if AI response needs to be more systemic than per-decision weights.
- Add a state-control cleanup hook or target registry for stale Event 014 pressure cleanup if state ownership churn becomes a tested issue.
- Consider scripted localisation for cost values if the constants are expected to change frequently.

## Validation

- Verified Event 014 spread response wiring in `events/014_cannibalism.txt`; spread event `chaosx.nr14.4` starts the outbreak in the receiving country.
- Checked touched Event 014 scripts for unsupported `<=` and `>=`; none were present.
- Checked touched Event 014 script brace balance; all inspected script files balanced.
- Checked patched constant references for mission deadlines, spread defaults, evolution thresholds, and death tallies.
- Checked patched localisation cost lines for the Event 014 decision surface.
- Confirmed `localisation/english/014_cannibalism_l_english.yml` still has UTF-8 BOM.

Skipped:

- No in-game validation was run.
- No log-based validation was performed or requested.
- No full-repo validation or commit was performed because the workspace contains unrelated Event 013 and Event 015 dirty work, and this audit was scoped to Event 014.

## Residual Risks

- Event 014 primary script files are currently untracked in this workspace, so the exact pre-audit file diff for those files is not available from Git.
- Localisation already had broad uncommitted Event 014 changes before this audit; the patched scope here is the decision cost and requirement text listed above.
- Mission geography remains abstract rather than target-state driven.
- Side missions cancel through outbreak/world-end gating rather than all being forcibly removed in the containment success effect.
- Outbreak-country AI may still underspend on the right production/supply categories without a broader AI strategy pass.
