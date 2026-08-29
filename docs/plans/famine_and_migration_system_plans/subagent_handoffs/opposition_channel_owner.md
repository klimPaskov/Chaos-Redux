# Famine and migration opposition channel owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and changed files

This owner patch adds a bounded catastrophic-famine opposition pool and its centralized tuning surface.

- `common/script_constants/famine_migration_opposition_constants.txt` adds channel enums, zero/maximum bounds, evidence and context coefficients, and dynamic consequence caps.
- `common/scripted_triggers/famine_migration_opposition_triggers.txt` adds the state/country validity gates and seven candidate eligibility predicates.
- `common/scripted_effects/famine_migration_opposition_effects.txt` adds pool initialization, context collection, candidate weights, deterministic terminal status, and existing political/resistance/autonomy consequences.
- `common/scripted_effects/famine_migration_opposition_effects.md` documents the helper contract and complete custom-pool manifest.
- `common/scripted_effects/chaosx_famine_migration_effects.txt` now contains the one exact caller inserted by the parent/decision owner at the live catastrophic stage transition; no other hunk in that concurrently owned file was changed here.

No decisions, localisation, events, mapmodes, GUI, assets, on-actions, specs, or unrelated systems were edited.

## Exact caller contract

The helper is state-scoped and is now called at the existing `famine_migration_transition_food_stage` catastrophic branch (current source line 3250), after the state is registered active and before catastrophic mortality interval handling, with these exact limits:

```text
check_variable = { var = famine_migration_requested_food_stage value = constant:famine_migration_food_stage.catastrophic_famine compare = equals }
has_state_flag = famine_migration_extraction_active
check_variable = { var = famine_migration_component_extraction > constant:famine_migration_food_component.zero }
famine_migration_resolve_opposition_channel = yes
```

This is the smallest responsibility-resolution call because `famine_migration_extraction_active` is set by the existing requisition/extraction decision, and the component is the already-computed live food-security contribution. The country-scoped `famine_migration_process_registered_displacement_country` cannot safely call this helper because it has no affected-state target and a state search would violate sparse-call/no-scan ownership.

## Candidate registry and formulas

The complete declared registry is `party_democratic`, `party_communism`, `party_fascism`, `party_neutrality`, `local_resistance`, `national_autonomy`, and `project_movement`.

Party candidates require positive current `party_popularity_100@<ideology>` support and `NOT = { has_government = <ideology> }`. Their weight is current support plus the bounded severity, responsibility, repression, country-context, and party-base contributions.

`local_resistance` requires `has_active_resistance = yes` and `resistance > 0`. Its weight adds live resistance, a proven-local bonus, severity, responsibility, and repression.

`national_autonomy` requires `is_core_of = OWNER` and owner `autonomy_ratio > -1`, the documented independent sentinel. Its weight adds bounded severity, responsibility, repression, and subject context.

`project_movement` has no authoritative project flag or scoped registry in the current source. Its authority constant is exactly zero and its candidate weight remains exactly zero; no project movement is fabricated.

Every candidate weight is initialized to `constant:famine_migration_opposition_weight.zero`, and only its candidate-valid branch can overwrite it. The total is the sum of all seven stored weights. A zero total leaves the selected channel at `none` and marks `fail_closed`.

The severity input is the current food-security score clamped to the catastrophic-to-maximum range. Responsibility starts with the current extraction component and adds the active requisition, atrocity-evidence, and active-camp bonuses. Repression uses the live governance and extraction components. No ideology multiplier can override severity, coercion, persecution/evidence, or a proven local movement.

## Effects, terminal state, and cleanup

One positive pool result selects exactly one existing channel through a deterministic engine `random_list` using the stored variable weights. A party result adds a capped popularity delta to the controller; local resistance adds a capped state resistance delta; national autonomy adds a capped autonomy score to the owner. All dynamic amounts come from the new constants file.

Every valid catastrophic responsibility resolution also applies a bounded negative controller stability delta and records `famine_migration_opposition_blame_memory`, preserving a general legitimacy/blame consequence even when no candidate is credible.

`famine_migration_opposition_last_resolution_stage_date` prevents duplicate selection while the same catastrophic stage is active. Recovery changes `famine_migration_food_stage_started_date`, permitting one later resolution. No global event target, periodic scan, or new registry is created. Candidate status/weights remain state-local audit memory and the existing state-registration retirement owns eventual state cleanup.

## Probability MCP artifacts and blockers

The mandatory first route was attempted with `hoi4.probability_inspect` and `adapter = custom_weighted_pool`; the tool returned the exact validation blocker: `An adapter requires a source; provide a source alone to discover compatible adapters`.

Source-only discovery then used `source.path = common/scripted_effects/chaosx_famine_migration_effects.txt` and returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, `candidates = 0`, and no available adapters because the new owner files were not yet present in that source snapshot. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/099137284e04ef1994288d29fe2c3090ebd30085e271ad17e75ea2effe304128/1309fe5cac9dc7a549bdce4fc8a8167cdfe3053c56951c5e4a16ea31d9b206ba/probability-inspect-1036274a63eb.json`.

After the helper source became visible, `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=false`, `candidates=0`, and `unresolved=7` because the MCP adapter does not discover this script-declared manifest. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bdde55ced8dfd97d828e6174f1dee6e2898f70c3eaa8ac5e6b5f21bac261640/7ee4a8e18e4649124c890c0734719b41181366e09a05c460e29c15041ad41063/probability-inspect-e6c622cb613d.json`.

The one-scenario `prob_opposition_channel` evaluate route returned `PROBABILITY_ANALYZED_PARTIAL`, `candidates=0`, `unresolved=7`, with no normalized probabilities; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68866f78716bfe75b6e09b41b2e178b024bc46db5cc1c370b3afb468fe2b49b9/e4fd695a3f49137200a4aa8b8d3e9de92219d55730cfd985f4b0198e79d0d2e5/probability-99ddfb07bf35446dfaa613a9.json`. The render route was attempted and returned `PROBABILITY_ANALYSIS_STALE` after the parent caller edit changed the workspace revision; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43be31ebcdc2aad681ea91213cd089ed2b8937b75dc7c69ddba93d41e0070b5f/6ad5a9d5a95a02723830af8112727c10ae8072809341d7ef1290c1d61fe52783/probability-99ddfb07bf35446dfaa613a9.json`.

The callable tool inventory has no `chaosx_ai_probability_auditor` route. A direct same-scenario `hoi4.probability_compare` was nevertheless attempted against the no-pool source and helper source; it returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=0`, `candidates=0`, and `unresolved=7`, with comparison artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1813e4e16d8114a8d39ee4f59b11226622f4f27213ea67951e4ea2f4783dd3cf/7668b96c1822f066869844e02e61e1922cf2f09e0f5631c2a9e08c3a73370da7/probability-fb7d3dbd7b74f54d1ed40af9.json` and comparison rendering `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/bf9e358b975ebbdd1a0d038c4b69978bc331510777792168615e07d236df419f/probability-probability-fb7d3dbd7b74f54d1ed40af9-comparison.svg`. This is not a final probability or balance claim because the MCP adapter withheld a complete candidate pool; the parent/audit owner must rerun the same scenario after the source settles and after an auditor route becomes available.

## Validation and residual gaps

Source review covered the offline wiki trigger/effect/scope/data-structure pages, vanilla trigger/effect/dynamic-variable documentation, the vanilla `random_list` precedent, and existing Chaos Redux `party_popularity_100`, `has_active_resistance`, `autonomy_ratio`, resistance, autonomy, and famine stage contracts.

The seven candidate formulas, zero initialization, no-scan state scope, same-stage guard, terminal status, and bounded consequences are present in the new files. A live game launch is intentionally not performed by this agent.

Residual gaps are limited to a fresh MCP probability pass after the complete source is visible and the unavailable `chaosx_ai_probability_auditor` route. No fallback movement, fake actor, or unsupported project registry was substituted.
