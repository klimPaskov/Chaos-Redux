# Event 006 shared decision cost-gate repair — 2026-08-03

## Scope

This audit was limited to one high-impact source defect in the shared Event 006 decision and mission availability path.

The accepted non-political-power cost model, generic-tree scope, category structure, focus layout, and decision effects were preserved.

## Issue list

| Severity | Status | Issue | Source and identifiers |
| --- | --- | --- | --- |
| Critical | Resolved | The shared security and strategic availability gates tested army experience, stability, and war support through generic variable-style checks rather than the documented engine-value triggers, which could fail closed and make every caller unavailable despite the country possessing those resources. | `common/scripted_triggers/006_independence_wave_decision_triggers.txt`: `can_pay_independence_wave_security_standard_cost`, `can_pay_independence_wave_security_major_cost`, and `can_pay_independence_wave_strategic_cost` |

No other local defect was changed or newly asserted by this narrow audit.

## Patch and behavior

Changed `common/scripted_triggers/006_independence_wave_decision_triggers.txt` only.

- `can_pay_independence_wave_security_standard_cost` now uses `has_army_experience > constant:independence_wave_decision_cost.army_experience_standard`.
- `can_pay_independence_wave_security_major_cost` now uses `has_army_experience > constant:independence_wave_decision_cost.army_experience_major`.
- `can_pay_independence_wave_strategic_cost` now uses `has_stability > constant:independence_wave_decision_cost.stability_standard` and `has_war_support > constant:independence_wave_decision_cost.war_support_minor`.

Before the repair, the shared gates could read ordinary script-variable state instead of the country's engine-backed army experience, stability, and war support values.

After the repair, callers use the documented HOI4 engine triggers while retaining the existing centralized Event 006 cost constants and all existing payment effects.

The surrounding file contains pre-existing uncommitted constant-compatibility edits, which were preserved and are not claimed by this handoff.

Representative core callers now unblocked by the repaired shared gates include `independence_wave_integrate_militias`, `independence_wave_raise_emergency_units`, `independence_wave_prepare_border_ultimatum`, `independence_wave_convene_founding_congress`, `independence_wave_coordinate_reclamation_fronts`, `independence_wave_demand_recognition_by_force`, and `independence_wave_transform_league_charter`.

## Decision category lifecycle notes

Existing categories retain their origin, phase, route, and cleanup gating.

The repaired helpers are availability checks only, so they do not reveal hidden categories, reopen completed routes, alter category cancellation, or change decision cooldown ownership.

Focus-to-decision integration was read-only checked in `common/national_focus/006_independence_wave_focus.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt` for the existing economy capstone, League congress, formable discovery, and high-chaos unlock flags.

## Mission quality notes

| Surface | Owner and category | Region and requirement | Duration, success, and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| Shared security and strategic availability | Event 006 origin country across the existing security, host, patron, League, borders, formables, and high-chaos decision surfaces | Individual decisions retain their own target-region, phase, route, origin, and cost requirements, with army XP, stability, and war support now read correctly | No mission duration, success, or failure effect changed | Unchanged because no repeatability flag, cooldown, target, mission, or payment effect changed |

No mission definition was edited by this repair.

## Cost and requirement clarity

The repair preserves the accepted non-PP cost design.

The existing effects in `common/scripted_effects/006_independence_wave_decision_effects.txt` remain the sole owners of manpower, equipment, civilian-capacity, stability, war-support, diplomatic, and other resource deductions.

The availability checks now test the same engine values the associated cost effects consume, and every threshold continues to come from `independence_wave_decision_cost` script constants.

No player-facing localisation key or custom cost tooltip changed because cost labels and amounts were already correct.

## AI validity and route-lock notes

AI callers still pass through the same availability gates, so they no longer receive a false resource rejection caused by a generic script-variable lookup.

No AI weights, target selection, route flags, borders, evolution checks, or formable checks changed.

Existing focus-unlock flags remain the route-lock authority, and this patch does not bypass them.

## Scripted GUI evidence

The decision-owned Statehood Ledger surface was inspected read-only with `hoi4.gui_inspect`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81380020037e945819fadcea48e219bb1a06bc830a832f2b39777a089a063752/74e096bec6ed1aedb7550c9adf97eabe486151fd1bda1e9845bcbfbb4b5ff1a9/gui-inspect.368f94db5a8e196d.json`.

No GUI source was changed because the defect is entirely in shared availability triggers.

Fidelity remains unresolved for a live scenario because no GUI state scenario was supplied, and this audit does not claim runtime rendering or save/load evidence.

## Cleanup and exploit-risk notes

No stale flag, event target, variable, cooldown, refund, or mission cleanup hook was added because the patch creates none.

No free-unit, equipment-farming, war-goal, core, or cooldown exploit was introduced because costs, effects, and repeatability were unchanged.

## Meaningful validation

- Confirmed all four repaired conditions are present with their existing `independence_wave_decision_cost` constants and that no `check_variable` use remains for `army_experience`, `stability`, or `war_support` in the shared trigger file.
- Enumerated core Event 006 callers for the three helpers to verify the repair covers the intended shared decision surfaces.
- Ran `python -B .tools\audit_event6_gui_matrix.py`, which passed the Statehood Ledger semantic source matrix with five mutually exclusive tab contracts, existing frame cleanup coverage, and four static/animated sibling pairs.
- Checked the implementation against `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` for `has_army_experience`, `has_stability`, and `has_war_support`, plus vanilla `documentation/triggers_documentation.md` and vanilla decision documentation and precedent files.

Skipped meaningful validation: no Clausewitz runtime evaluation or state-specific GUI render was claimed because this was a source-only shared-trigger repair and no GUI scenario was supplied.

## Remaining issues and handoff

This does not certify the wider Event 006 implementation as complete, and existing broader Event 006 completion findings remain outside this narrow patch.

No fallback or simplification was used.

No new plan handoff was needed because the concrete local defect was resolved directly.

No commit was created, so the parent remains responsible for final diff review and any task-level commit.
