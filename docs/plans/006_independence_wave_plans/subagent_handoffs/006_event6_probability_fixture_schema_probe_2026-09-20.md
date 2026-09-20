# Event 006 probability fixture schema probe — 2026-09-20

## Disposition

`UNRESOLVED / read-only adapter-schema confirmation`.

This probe covers the admitted IW-040 KUB mission AI surface and the shared scenario schema used for the matching IW-044 TAT surface. It does not change source weights, triggers, decisions, missions, package admission, central attestation, or Join.

## Confirmed scenario shape

The current probability adapter accepts the strict scenario-set shape `scenarioSet = { id, scenarios = [ ... ] }`.

Each scenario accepts `actor` as a country-tag string, `flags` as an array of flag strings, `state` as a flat primitive map, and `scopes` as a record whose values use `{ id = string, state = primitive-map }`.

The accepted scope keys include `root`, `target`, `capital_scope`, `event_target:independence_wave_setup_anchor_state`, and `event_target:independence_wave_setup_former_host` when supplied with exact scope identifiers.

The adapter rejected country-scope objects using `tag`, `country`, or `kind`, rejected string scope values, rejected array-valued scope collections, and rejected unrecognized scope members such as `owner` and `controlled_by`.

Primitive scope-state probes for `is_owned_by` and `is_controlled_by` were accepted and reduced the unresolved result. This confirms that named scope slots can be addressed by the current adapter, but it does not prove that the complete campaign event-target ledger is representable.

The adapter accepts top-level scenario `flags` only as an array of strings. A boolean flag map was rejected. Scenario-level `fixture`, `actors`, `targets`, `scopeExpectations`, `variables`, `vars`, `values`, `inputs`, and `factors` were rejected as unrecognized keys, and a root-level `scenarioSet.fixture` object was also rejected.

A final root-level `scenarioSet.variables` probe was rejected with `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_evaluate: Unrecognized key: "variables" at scenarioSet`.

## KUB evaluation receipt

The exact one-candidate probe used `independence_wave_kub_secure_mounted_depots` from `common/decisions/006_independence_wave_frontier_decisions.txt` with source revision `fde186f5365f9b2345afea68841353d8b4c867777365b30c2bd8597e00fdf477` and source hash `6ae0124991b3742ae8b7a856c8207ea9d755335dac9a79cbe848ac8fc88785c1`.

The accepted scenario supplied `actor = KUB`, exact anchor, capital, target, and former-host scope slots, the existing setup flag, and primitive comparator strings `">=10"`, `">=100"`, and `">=100000"` for the civilian-factory, command-power, and manpower checks.

MCP returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-e4a4f2c3b93879bca1dc5819`, scenario hash `0c648e773f727220c41846775fe83b944148ec186a868b6a1274a2263de9eccc`, `data.unresolved = 13`, one diagnostic, and the authoritative JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d301e9a0a869e70708671b10dbae0708893c410703e3b2a01268b1c7e5520c0/29d21d0442570d32e696cb051a5210b57b0eb3cdfd1de005bbf66a8369a569cf/probability-e4a4f2c3b93879bca1dc5819.json`.

The three comparator strings removed the resource/capacity unresolved messages from the candidate trace, but the candidate remained ineligible with raw value `0` and the diagnostic `PROBABILITY_OUTCOME_NEVER_ELIGIBLE`.

The scenario and candidate trace still contain unresolved `check_variable` declarations, all seven numeric Event 006 setup variables, and direct comparisons for `has_variable`, `has_active_mission`, and `has_decision`. The adapter messages are `check_variable requires declared var and value`, `Scenario does not declare numeric variable <name>`, and `Trigger <name> cannot compare the declared scenario value`.

The direct primitive state values for `independence_wave_setup_package_id`, `independence_wave_setup_region`, `independence_wave_setup_depth`, `independence_wave_setup_territory_level`, `independence_wave_setup_force_level`, `independence_wave_setup_chaos_band`, and `independence_wave_setup_archetype` therefore do not declare Clausewitz numeric variables for `check_variable` evaluation.

## Evidence boundary

The exact KUB and TAT source pools remain complete at 11/11 candidates with the 17/18 required-input counts recorded in `006_event6_kub_tat_probability_inspect_refresh_2026-09-20.md`.

The accepted scope and flag fields do not constitute a typed campaign fixture. Package ledgers, route and government state, equipment and manpower values, active decision and mission membership, former-host validity, event-target values, and setup-variable comparisons remain quantitatively unresolved.

No `probability_compare`, complete sweep, simulation, sequence, normalized probability, dominance, starvation, rank-reversal, or numeric balance conclusion is valid from this probe. The result is score-only and remains unsuitable for a KUB/TAT ten-scenario baseline.

No gameplay source, AI weight, decision, mission, admission, registry, localisation, asset, or workbook file was edited.

## Next gate

The next probability tranche requires either a documented adapter extension that declares typed variables and named campaign collections or an existing supported fixture contract that binds the missing inputs without inventing trigger keys or weakening package gates.

Until that gate exists, KUB and TAT remain source-complete but quantitatively unresolved, and their existing package admission and source weights must not be widened or reweighted from partial or empty-fixture output.
