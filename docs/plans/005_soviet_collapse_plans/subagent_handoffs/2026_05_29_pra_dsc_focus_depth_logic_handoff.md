# PRA/DSC Focus Depth Logic Handoff

Date: 2026-05-29

Scope: bounded focus-tree depth/logic patch for the Pale Railway Authority (PRA) and Dead Soldiers Congress (DSC) in `common/national_focus/005_soviet_collapse_custom_splinters.txt`, plus directly required localisation in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`.

## Changed Files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_pra_dsc_focus_depth_logic_handoff.md`

Note: the worktree already had unrelated/pre-existing edits in the same focus and localisation files before this patch, including FTH layout movement and two existing localisation description changes. Those were not reverted.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| PRA railway/supply gameplay | `PRA_omsk_station_guard`, `PRA_count_the_locomotives`, `PRA_coal_water_and_spare_parts`, `PRA_mobile_workshops`, `PRA_claim_the_branch_lines`, `PRA_flags_on_every_station` | Patched | Added clearer decision unlock tooltips, supply hubs, railways, rolling-stock gain, support equipment, trucks, and depot/supply helper use. |
| PRA decision progression | `pra_mobilize_station_guard`, `pra_repair_the_branch_lines`, `pra_raise_mobile_supply_yards`, `pra_drive_the_junction_columns`, `pra_declare_the_moving_state` | Patched | Existing decision visibility flags were kept; focus rewards now surface more unlocks with `unlock_decision_tooltip`. |
| DSC mass manpower/units | `DSC_voronezh_rearguard_archives`, `DSC_vote_by_regimental_dead`, `DSC_grave_ordnance_claims`, `DSC_field_hospital_memorials`, `DSC_rearguard_supply_bureau` | Patched | Shifted manpower/equipment support earlier and added military-consolidation helper calls to two shallow support focuses. |
| DSC decision progression | `dsc_verify_the_roll_call`, `dsc_raise_dead_regiment_columns`, `dsc_convene_the_dead_army` | Partially patched | Added another visible roll-call decision unlock; did not edit decision files or visibility gates by scope. |

## Changed Focus IDs

PRA:

- `PRA_omsk_station_guard`
- `PRA_count_the_locomotives`
- `PRA_coal_water_and_spare_parts`
- `PRA_mobile_workshops`
- `PRA_claim_the_branch_lines`
- `PRA_flags_on_every_station`

DSC:

- `DSC_voronezh_rearguard_archives`
- `DSC_vote_by_regimental_dead`
- `DSC_grave_ordnance_claims`
- `DSC_field_hospital_memorials`
- `DSC_rearguard_supply_bureau`

## Route Behavior Before and After

Before:

- PRA had several correct railway decisions, but some focus rewards that enabled them only set flags or gave generic supply/industry rewards without explicit unlock tooltip linkage.
- PRA rail/supply rewards were present but uneven, with some branch-line and mobile-workshop focuses still reading like ordinary factory/support rewards.
- DSC manpower and unit support was concentrated in `DSC_dead_regiment_columns`, `DSC_armies_that_do_not_demobilize`, and the endgame helper, leaving several middle focuses comparatively flat.

After:

- PRA railway focuses now visibly connect to station guard, branch-line repair, mobile supply yard, junction-column, and moving-state decisions.
- PRA now gets more direct rail/supply-map effects from locomotive counting, mobile workshops, and branch-line claims.
- DSC gets earlier emergency manpower, militia manpower, infantry equipment, support equipment, and military-consolidation unit support through its archives, roll-call, ordnance, hospital, and rearguard branches.

## Localisation Keys Changed

- `PRA_omsk_station_guard_desc`
- `PRA_count_the_locomotives_desc`
- `PRA_coal_water_and_spare_parts_desc`
- `PRA_mobile_workshops_desc`
- `PRA_claim_the_branch_lines_desc`
- `PRA_flags_on_every_station_desc`
- `DSC_voronezh_rearguard_archives_desc`
- `DSC_vote_by_regimental_dead_desc`
- `DSC_grave_ordnance_claims_desc`
- `DSC_field_hospital_memorials_desc`
- `DSC_rearguard_supply_bureau_desc`

Pre-existing localisation changes in the file remain present:

- `pra_moving_state_authority_desc`
- `dsc_dead_army_politics_desc`

## Icon Coverage Table

| Tag/tree | Focus icon refs checked | Missing icon refs | Notes |
| --- | ---: | ---: | --- |
| PRA | 22 | 0 | All `GFX_focus_PRA_*` references are present in `interface/*.gfx`. |
| DSC | 18 | 0 | All `GFX_focus_DSC_*` references are present in `interface/*.gfx`. |

No icon ids were changed.

## Localisation and Reward Mismatch List

- PRA descriptions were updated where rewards now explicitly support rail repair, supply yards, branch-line control, trucks, and moving-state station authority.
- DSC descriptions were updated where rewards now explicitly support emergency reserves, recruitment, depot stores, reserve musters, and replacement drafts.
- No missing PRA/DSC focus name or description keys were found after the patch.

## AI Behavior Gaps

- Existing `ai_will_do` blocks were preserved. They already react to war state, chaos tier, SOV depot pressure, SOV military obedience, and stability.
- I did not add new route-specific AI weights for the strengthened rewards because that would risk broader balance changes outside the narrow patch scope.

## High-Priority Fixes Applied

1. PRA decision clarity: added missing `unlock_decision_tooltip` calls for key railway/supply decisions where existing flags already made those decisions visible.
2. PRA rail/supply depth: added direct supply hubs, railways, infrastructure, rolling-stock, trucks, and depot/supply helper linkage to existing railway focuses.
3. DSC manpower/units: added earlier manpower/equipment rewards and military-consolidation helper calls to mid-branch DSC focuses.
4. Localisation alignment: updated focus descriptions so names, text, and rewards tell the same story.

## Missing or Simplified Content

- No new route family, focus branch, formable chain, ideas, decisions, scripted helpers, icons, or assets were added.
- DSC decision depth remains limited by the existing three-decision surface; this patch only strengthens focus linkage and rewards.
- PRA/DSC broader route design may still need a parent-level improvement pass if the parent wants more than compact reward/logic hardening.

## Validation Run

- Read required repo instructions and skills: `AGENTS.md`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`.
- Consulted offline wiki pages required by AGENTS, including Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.
- Consulted vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`.
- Inspected vanilla precedent for focus/decision reward syntax including `unlock_decision_tooltip`, `add_building_construction`, `add_equipment_to_stockpile`, `add_manpower`, and unit creation patterns.
- Ran brace balance check on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `brace_balance 0`.
- Counted scoped focus ids: `pra_dsc_focus_ids 42 unique 42`.
- Checked PRA/DSC focus localisation keys: `missing_focus_loc_keys []`.
- Checked PRA/DSC focus icon references: `icon_refs 40 missing []`.
- Checked localisation BOM: first bytes `ef bb bf`.
- Ran `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: no whitespace errors.
- Ran `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt`: no unsupported operators found.

## Skipped Validation and Why

- No full game launch or error-log validation was run from this subagent environment.
- No decision/scripted-effect/idea files were edited by request, so I did not validate or patch those systems beyond reading the directly relevant decision and helper surfaces.
- No commit was created because the repository already contains many unrelated dirty files, and the two scoped files also had pre-existing same-file edits not made by this subagent.

## Remaining Route Risks

- `DSC_republic_of_roll_calls` still uses a visible route line from `DSC_league_of_old_fronts` with an `available` gate on `DSC_rearguard_supply_bureau`; this avoids a long crossing prerequisite line, but the UI may not visually show the full dependency.
- PRA and DSC still rely on existing helper effects for several deeper payoffs. If those helpers change, the focus reward feel may shift.
- The patch increases PRA supply construction and DSC manpower/equipment availability; parent should review balance in the full Soviet Collapse pass.

## Plan Handoff Path

No broad improvement plan was written. The requested changes fit inside a narrow, safe focus/localisation patch.
