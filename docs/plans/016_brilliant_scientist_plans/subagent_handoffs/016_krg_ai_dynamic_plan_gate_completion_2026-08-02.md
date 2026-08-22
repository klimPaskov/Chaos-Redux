# Event 016 KRG dynamic AI plan gate completion

Date: 2026-08-02

Status: bounded follow-up patch complete; parent review and live AI/takeover validation remain outstanding.

## Scope and recommendation

This follow-up audited every remaining Event 016 KRG AI strategy plan after the two takeover plans were made dynamically eligible.

The offline AI modding reference documents that `allowed` is checked only at game start, while `enable` is checked each day and `abort` controls an active plan afterward.

The transformed-host route intentionally retains its original tag, sets `brilliant_scientist_host_transformed_into_kruger_state`, and sets `brilliant_scientist_formation_takeover` at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1041-1045`.

All nineteen KRG plan `enable` blocks require `brilliant_scientist_is_kruger_sovereign_country = yes`, and that trigger accepts only `original_tag = KRG` or the transformed-host flag at `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt:8-13`.

The remaining seventeen `allowed = { original_tag = KRG }` lines were therefore stale for transformed hosts and were removed.

No plan `enable`, `abort`, focus list, factor, weight, route condition, event, decision, country file, or model was changed.

## Changed file and plan identifiers

- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`
  - Removed `allowed = { original_tag = KRG }` from `KRG_charter_republic_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_rebellion_directorate_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_enclave_survival_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_clone_sovereignty_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_machine_ascendancy_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_paleogenetic_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_xenobiological_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_project_synthesis_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_portal_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_temporal_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_alien_arms_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_biological_containment_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_biological_last_resort_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_commonwealth_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_submission_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_laboratory_world_plan`.
  - Removed `allowed = { original_tag = KRG }` from `KRG_singularity_plan`.

The same source file contains an unrelated parent edit that reorders two entries in `KRG_project_synthesis_plan`; this follow-up does not alter that line.

## Plan-by-plan guard audit

| Plan | Daily `enable` guard | Existing `abort` guard | Dynamic safety result |
| --- | --- | --- | --- |
| `KRG_charter_republic_plan` | Sovereign KRG plus `brilliant_scientist_formed_by_charter`, before `KRG_complete_the_founding_audit` | Focus tree inactive or founding audit complete | Safe; formation-origin and audit gates remain. |
| `KRG_rebellion_directorate_plan` | Sovereign KRG plus `brilliant_scientist_formed_by_rebellion`, before the audit | Focus tree inactive or founding audit complete | Safe; formation-origin and audit gates remain. |
| `KRG_enclave_survival_plan` | Sovereign KRG plus `brilliant_scientist_formed_as_enclave`, before the audit | Focus tree inactive or founding audit complete | Safe; formation-origin and audit gates remain. |
| `KRG_takeover_consolidation_plan` | Sovereign KRG plus `brilliant_scientist_formed_by_takeover`, before the audit | Focus tree inactive or founding audit complete | Safe; this was the first previously patched takeover plan. |
| `KRG_takeover_post_audit_plan` | Sovereign KRG plus takeover origin, completed audit, and open identity | Focus tree inactive, takeover origin absent, identity locked, or founding policy committed | Safe; this was the second previously patched takeover plan. |
| `KRG_clone_sovereignty_plan` | Sovereign KRG, completed audit, operational cloning deployment, and no completed replicated-host terminal focus | Cloning operations cease or `KRG_the_replicated_host` completes | Safe; route and terminal guards remain. |
| `KRG_machine_ascendancy_plan` | Sovereign KRG, completed audit, operational robotics deployment, and no completed machine-army terminal focus | Robotics operations cease or `KRG_an_army_of_machines` completes | Safe; route and terminal guards remain. |
| `KRG_paleogenetic_plan` | Sovereign KRG, completed audit, operational paleogenetics deployment, and no completed dinosaur-host terminal focus | Paleogenetics operations cease or `KRG_the_dinosaur_host` completes | Safe; route and terminal guards remain. |
| `KRG_xenobiological_plan` | Sovereign KRG, completed audit, operational xenobiological deployment, and no completed engineered-legion terminal focus | Xenobiology operations cease or `KRG_the_engineered_legion` completes | Safe; route and terminal guards remain. |
| `KRG_project_synthesis_plan` | Sovereign KRG, completed audit, synthesis unlock trigger, and no completed synthesis focus | Synthesis completes, becomes unavailable, or focus tree becomes inactive | Safe; shared synthesis gate remains. |
| `KRG_portal_plan` | Sovereign KRG, completed audit, operational teleportation deployment, and no completed transit-corps focus | Teleportation operations cease or `KRG_the_strategic_transit_corps` completes | Safe; route and terminal guards remain. |
| `KRG_temporal_plan` | Sovereign KRG, completed audit, operational temporal deployment, and no completed continuity-guard focus | Temporal operations cease or `KRG_the_continuity_guard` completes | Safe; route and terminal guards remain. |
| `KRG_alien_arms_plan` | Sovereign KRG, completed audit, operational alien-arms weaponization, high-energy deployment, and rocketry or teleportation weaponization | Alien-arms operations cease or `KRG_arm_the_alien_cohorts` completes | Safe; high-energy and delivery gates remain. |
| `KRG_biological_containment_plan` | Sovereign KRG, completed audit, operational biological prototype, and no completed containment-doctrine focus | Biological operations cease or `KRG_make_containment_the_first_doctrine` completes | Safe; prototype and doctrine gates remain. |
| `KRG_biological_last_resort_plan` | Sovereign KRG, completed audit, containment doctrine, operational weaponization, valid delivery, high-energy deployment, and rocketry or teleportation weaponization | Biological operations cease or `KRG_authorize_agents_of_last_resort` completes | Safe; delivery, doctrine, and terminal gates remain. |
| `KRG_commonwealth_plan` | Sovereign KRG, former-host settlement focus complete, and neither commonwealth nor submission terminal focus complete | Either commonwealth or submission completes, or focus tree becomes inactive | Safe; settlement and terminal gates remain. |
| `KRG_submission_plan` | Sovereign KRG, former-host settlement focus complete, neither commonwealth nor submission complete, and military reach available | Either commonwealth or submission completes, or focus tree becomes inactive | Safe; military-reach and terminal gates remain. |
| `KRG_laboratory_world_plan` | Sovereign KRG, fourth-evolution focus complete, evolution-four availability, laboratory-world commitment available, and no laboratory-world completion | Laboratory World or Strategic Singularity completes, or laboratory-world availability closes | Safe; mutually exclusive terminal gates remain. |
| `KRG_singularity_plan` | Sovereign KRG, fourth-evolution focus complete, evolution-four availability, singularity commitment available, and no singularity completion | Laboratory World or Strategic Singularity completes, or singularity availability closes | Safe; mutually exclusive terminal gates remain. |

## Before and after behavior

Before this follow-up, transformed hosts could only activate the two takeover plans whose `allowed` lines had already been removed; all route, project, diplomacy, and terminal plans remained permanently unavailable because their start-only `allowed` checks required the host's original tag to be KRG.

After this follow-up, all nineteen plans are eligible for daily `enable` evaluation, allowing a transformed host to activate the applicable route, project, diplomacy, and terminal plan once the existing sovereign, focus, route, facility, history, and completion triggers become true.

No plan is enabled merely because it is parsed: every plan's `enable` block contains the sovereign trigger, and no source outside the Event 016 country trigger defines the transformed-host sovereign flag.

The engine may parse and check these nineteen plan definitions for all countries, but no non-KRG country can enable them without the Event 016 sovereign trigger evaluating true.

## Static counts and validation

- The source contains 19 top-level `KRG_*_plan` blocks.
- The source contains 0 remaining `allowed` blocks in the Event 016 AI plan file.
- The source contains 0 remaining `original_tag = KRG` references in the Event 016 AI plan file.
- All 19 plan `enable` blocks contain `brilliant_scientist_is_kruger_sovereign_country = yes`.
- All 19 plans retain an `abort` block; no abort condition was edited.
- All 19 focus lists, factor blocks, weights, route conditions, terminal conditions, and policy modifiers remain present.
- Repository scans confirm the sovereign trigger is defined at `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt:8-13`, while the transformed-host flag is set only by `brilliant_scientist_transform_host_into_kruger_state` at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1041`.
- `git diff --check -- common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` returned no whitespace errors.
- The previously captured read-only `hoi4_focus_inspect` artifact remains valid because the focus tree source was not changed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ba30159db7ddc31b1430b61dcf28e3ecb17ea749e124da8f83d5d94a5a7723e/8287d2c89c2e5ccff8fdaa8697eab03e52e70b3b8999283460cbd56ad6606645/focus-inspect.cc58941aa91bd941.json`.

## Risks and parent checks

1. Removing all `allowed` blocks increases the number of daily plan eligibility checks globally from the parser's perspective, but each plan remains inert unless the sovereign trigger and its route-specific guards are true. No new world iteration or on-action was added.
2. Multiple AI strategy plans may be active at once by design; this change allows transformed hosts to join the same route/project/terminal plan set already available to original KRG. Existing `weight`, `focus_factors`, and `abort` logic remains the balance boundary.
3. A malformed or stale Event 016 country flag could still make a non-KRG country satisfy a sovereign trigger; the source audit found only the intended transform assignment, but live flag cleanup remains unproved.
4. The transformed-host cosmetic-tag identity issue is unchanged: `drop_cosmetic_tag = yes` is still used without a base KRG cosmetic assignment. This AI patch does not resolve map name or flag presentation.
5. Live route selection, AI plan activation, focus order, terminal competition, formation transfer, and balance remain user-owned checks because no Hearts of Iron IV process was launched.

## Skipped validation

- No live takeover, route, project, or terminal scenario was run because agents must not launch Hearts of Iron IV.
- No map rewrite was attempted because this patch changes no state or province data.
- No technology-tree viewer validation was run because the installed package exposes no Technology Tree Viewer.
- No weighted simulation was run because the change removes static plan eligibility gates and does not alter numeric weights; the available read-only probability adapters do not model AI strategy-plan lifecycle activation directly.

No models were created or referenced, no fallback assets were introduced, and no commit was created.
