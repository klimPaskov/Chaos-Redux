# Non-camp scripted startup repair handoff

Status: local and Event021–029/032 source repairs frozen; Event027/031/035 final tranche in progress; parent startup loop validation pending.
Acceptance basis: root delegated all non-camp scripted effects and triggers for the explicitly authorized all-startup-errors repair pass.
No commit created.
Original bytes are retained under `baseline/scripts/<repository-relative path>` beside this handoff.

## Local architect changes

- `common/scripted_effects/006_independence_wave_effects.txt` and `006_independence_wave_iberian_package_effects.txt`: three GLC portrait calls use the documented ideology group `democratic`, retaining the Castelao portrait and surrounding receipt checks.
- `common/scripted_effects/012_africa_gods_effects.txt`: two resource amount checks inject their existing central threshold through documented `meta_trigger`; three building-damage calls inject the unchanged central damage through `meta_effect`.
- `common/scripted_triggers/012_africa_gods_triggers.txt`: three capacity predicates remove illegal effect-style `limit` wrappers from `any_owned_state` and evaluate the existing country capacity value before entering the state scope through `meta_trigger`.
- `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt`: the long-range strike injects the unchanged damage and repair-speed constants into its six building damage calls; building types, damage, target, cooldown and history are retained.
- `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt`: strategic-resource shortage uses its existing threshold through dynamic injection into all four resource checks.
- `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt`: two production manpower gates use installed `has_manpower` with unchanged threshold and strict operator.
- `common/scripted_effects/020_black_plague_weaponized_runtime_effects.txt` and matching markdown: bridge snapshots explicitly initialize the existing exposure defaults on every invocation and override them with provided caller inputs; unsupported temporary clears are removed after full identifier tracing.
- `common/scripted_effects/021_random_civil_war_decision_effects.txt`: railway recovery grants existing `train_equipment` archetype rather than the nonexistent `trains` identifier, with unchanged amount.
- `common/scripted_triggers/021_random_civil_war_triggers.txt`: Event006 admission delegates to the existing `is_independence_wave_runtime_package_preflight_ready` contract.
- `common/scripted_triggers/021_random_civil_war_successor_triggers.txt`: owned-state dynamic variable comparison uses `check_variable` with the same strict positive threshold.
- `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`: three manual scenario and four exposure viability existence checks use `any_character = { is_country_leader = yes }`, retaining the intended current-ruler-or-divisions alternatives.

## Bridge contract evidence

The exact private identifiers are `black_plague_weaponized_runtime_input_amount`, `black_plague_weaponized_runtime_input_route`, and `black_plague_weaponized_runtime_input_provenance`.
Repository-wide exact-token search found their only reads and writes inside `black_plague_apply_weaponized_exposure_runtime`; neither caller nor the initializer, shared exposure effect, or scheduler helper reads the private snapshots.
Both callers (`brilliant_scientist_dispatch_black_plague_release` and `black_plague_weaponization_deliver_to_state`) set amount, route and weaponized provenance before calling the bridge and read only the public bridge result afterward.
The optional amount and route defaults come directly from `black_plague_apply_exposure`: minimum exposure and land border.
Natural provenance is only a private default; the original weaponized target-validity gate still requires explicit valid weaponized provenance before bootstrap.
Every private snapshot is overwritten at entry, so a second invocation within the same chain cannot reuse a stale private value when an optional input is absent.
Public acceptance results and caller payment/provenance continuations remain intact.
No regular `clear_variable` is substituted for temporary cleanup.

## Constants, scopes and cleanup

No tuning values, AI weights or constants are added by the local architect changes.
Resource counts use integer-formatted literal injection; building damage and repair speed retain three-decimal fixed-point precision.
Temporary dynamic-injection scratch is written immediately before use and has no outside consumers.
No global target, on-action, event, GUI or periodic loop is introduced.

## Child handoffs

- `script_targets_handoff.md`: Event021/023 lifecycles and syntax, with additional selected-actor lifecycle handoff when finished.
- `script_middle_handoff.md`: Event024–029 and CBRN shelter payload extraction.
- `script_later_handoff.md`: Event027/031/033/035 repairs.
- `script_missile_handoff.md` and `script_missile_lifecycle_references.md`: Event032 lifecycle repair, exact identifier and continuation evidence.

## Validation and limits

Read AGENTS, offline core wiki references and relevant event/decision/data/scope sections, installed effect/trigger/script-concept/script-constant documentation, the dynamic-helper registry, and owning Event012/016/020 documentation.
Skills applied: chaos-redux-debug-playtest, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents.
No skill files modified.
Installed documentation confirms portrait ideology groups, has_manpower, current-leader character predicate, meta evaluation, and automatic regular-target lifetime.
MCP event inspection and rendering succeeded with partial focused evidence: revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`.
The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0b0c4e2cc14aa164f62911816a8f43dfcb2a4c45dd741048121a4e7704181f8/fefddd043d8c76c994552ba261b37ec0cf8b145333922365d3647991921872e2/event-trace-4bccb6ec7fe1.json`.
The neighborhood manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/902cabad010c5051fe01ace751589836ba1df8f2410a5272dfe34b5186b2e1be/0c9a8de409b6c3a367bfbe6e514a426e12c01c0abc0324edfc5725b149415fa6/event-neighborhood-4bccb6ec7fe1-manifest.json`.
The first trace selector used zero-padded nr020, so its existence is not claimed as proof of actual root reachability; the subsequent render used real `chaosx.nr20.1`.
MCP explicitly deferred workspace-wide helper/lifecycle projection; it is not runtime proof of these helper repairs.
Comparison attempts returned `EVENT_COMPARISON_BASELINE_REQUIRED` without a baseline and `EVENT_GRAPH_ARTIFACT_INVALID` when given the linked trace artifact; comparison remains blocked by required full-graph artifact schema.
The parent owns fresh launch validation; no process or computer control was performed by this worker.

## Remaining work

Root released the exact weighted eligibility repairs after the probability auditor captured baselines and explicit adapter limitations.
The source patches preserve ticket counts, values and threshold operators; root owns mandatory post-patch comparison.
Full child lifecycle evidence and later fresh-log repair results must be reviewed by root before completion.
No mechanic removal or intentional simplification was used; startup completion is not claimed.

Task-specific constant-reference comparison is recorded in `script_local_constant_contract_check.json`.
All existing constant identifiers are retained across the 12 local files; the bridge additionally references exactly the three defaults from the existing shared exposure helper.

## Weighted-surface repair release

Root released the held exact syntax repairs after the probability auditor captured source discovery/baselines and explicit unavailable-adapter limitations.
Four Event021 exposure viability ruler checks now use the documented existential active-character predicate.
Named comparison scenarios: `EVENT021_VIABILITY_WITH_CURRENT_RULER_NO_FACTORIES`, `EVENT021_VIABILITY_WITHOUT_RULER_NO_FACTORIES`, and `EVENT021_VIABILITY_FACTORIES_PRESENT`.
The expected outcomes retain the original OR contract: a current ruler or positive factory count satisfies this part of viability; neither does not.
Before source is `baseline/scripts/common/scripted_triggers/021_random_civil_war_parent_triggers.txt`; after source is the current same repository-relative file.
No numeric score, threshold, candidate count or weight was changed.

Local Event021 exposure comparison packet: `script_local_weighted_scenarios.json`.
Event024–029 comparison packets: `script_middle_weighted_manifest.json` and `script_middle_weighted_validation.json`.
Event021 lifecycle comparison snapshot and scenario names are recorded in `script_targets_handoff.md`.
