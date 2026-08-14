# IW-050 Komi probability audit handoff

## Disposition

This is a read-only weighted-surface audit for IW-050 Komi. The source contains AI strategy factors, but the installed probability adapter does not expose an analyzable weighted surface for this file. No quantitative AI-balance, selection-probability, dominance, starvation, timing, or live-runtime claim is made.

## Audited surface and source identity

- Surface: IW-050 Komi AI strategy factors in `common/ai_strategy/006_independence_wave_komi.txt`.
- Related source-level gates reviewed: `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` and `common/scripted_effects/006_independence_wave_komi_package_effects.txt`.
- MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Fresh MCP source revision: `cb56bfea060d78c03fae842efa5e1fbee68071360840ebfd7ca343215f27583a`.
- Fresh MCP canonical source hash: `78be03b0b0740f9fcc47eceea8c20bad14a081d498d5ece83183b3befaf19f9c`.
- Local raw-file SHA-256 at audit: `10ed6c78ec6f3123db175900187c8d8aa68b4972cb911c4e21f9bdcb5957c465`.
- Local Git blob hash (computed without staging): `38808421a36a157ed0640ee07b8d7db8a4e73119`.
- The source is currently untracked (`git status --short` reports `?? common/ai_strategy/006_independence_wave_komi.txt`), so there is no Git commit revision for this file. The local raw hash is recorded separately from the MCP canonical hash and is not substituted for it.

## Required MCP probability evidence

### Source inspection

The mandatory first call was `hoi4.probability_inspect` with adapter `ai_strategy_factor`, source `{path: "common/ai_strategy/006_independence_wave_komi.txt"}`, and `refresh = true`.

- Result: `PROBABILITY_SOURCE_DISCOVERED`, status `ok`, `discoveryReason = no_weighted_surfaces`.
- Candidates: `0`; available candidates: `0`; available adapters for this source: `[]`.
- Required inputs: `0`; unresolved inputs: `0`; diagnostics: `[]`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1113eb67f4cbcc233c451213f77f2001c8db81927f0163ad0793c01bb0795c7/3c7f93f637e74b4bccb1edc2c91a1d1deaaa79c2cff19d746376ad85cb1fa972/probability-inspect-78be03b0b074.json`.
- Interpretation: this is an adapter coverage result, not evidence that the source file has no `ai_strategy` entries.

### Named scenario evaluation

The named empty fixture was `IW050_KOM_STRATEGY_EMPTY_CURRENT_2026_08_14` with scenario `KOM_STRATEGY_EMPTY` and empty state `{}`. The fresh repeat used adapter `ai_strategy_factor` and the same source path.

- Result: `PROBABILITY_SURFACE_EMPTY`, status `error`.
- Exact blocker: `No weighted blocks matched this request`.
- No evaluation artifact, analysis ID, scenario hash, ranking, modifier trace, or rendered evidence was produced.
- Candidate-pool completeness: not established; the adapter exposed no candidate pool, and `availableCandidates = 0` must not be read as an empty engine pool.
- External-factor completeness: not evaluated; the empty fixture does not provide a typed Komi package state, and evaluation stopped before factor tracing.
- Classification: unresolved for probability; source facts below are score-only/source-attestation facts.

### Intentionally skipped MCP routes

- `hoi4.probability_sweep` was skipped because no analyzable surface, complete candidate pool, or declared threshold/sensitivity paths exist.
- `hoi4.probability_compare` was skipped because no before/after source or candidate comparison was supplied and the current surface is empty to the adapter.
- `hoi4.probability_simulate` was skipped because no uncertain inputs were declared.
- `hoi4.probability_sequence` was skipped because this is not a declared custom weighted pool with cadence, recovery, cooldown, caps, removals, resets, timers, and terminal states.
- `hoi4.probability_render` was skipped because no analysis ID or renderable MCP analysis artifact exists.
- No matching structural MCP route is defined for AI strategy-factor blocks; no event, focus, GUI, technology, or doctrine surface was audited here.

## Source-level strategy inventory

The source has four named strategy blocks and twelve `ai_strategy` rows. The literals below are copied from the file and are not normalized probabilities or balance judgments.

| Block | Gate summary | Strategy rows and literal values |
| --- | --- | --- |
| `independence_wave_komi_taiga_survival` (lines 19-33) | `original_tag = KOM`, Komi package, IW-050 setup, and `independence_wave_komi_ai_profile` | `build_army = 86`; `equipment_production_factor infantry = 38`; `artillery = 20`; `support = 52`; `build_building infrastructure = 82`; `bunker = 92` |
| `independence_wave_komi_host_restraint` (lines 35-45) | Komi package, IW-050 setup, living former host, and host ledgers not settled | `avoid_starting_wars = -250` |
| `independence_wave_komi_settled_northern_republic` (lines 47-57) | Komi package and `independence_wave_komi_compact_stabilized` | `build_army = 86`; `avoid_starting_wars = -420`; `build_building infrastructure = 82` |
| `independence_wave_komi_emergency_taiga_command` (lines 59-68) | Komi package and `independence_wave_komi_taiga_emergency_government` | `build_army = 116`; `build_building bunker = 92` |

The file uses file-scoped `@CR_SC_IW_KOM_*` aliases at lines 2-10. No dynamic modifier trace is available from the MCP adapter. Vanilla AI documentation confirms that `equipment_production_factor` changes perceived equipment need, `build_building` values participate in the building strategy selection pool, and negative `avoid_starting_wars` values are additive with other strategy values; those engine semantics do not supply a Komi-specific ranking without the missing candidate and state inputs.

## Validity and lifecycle review

- `is_independence_wave_komi_package` in `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-19` checks `original_tag = KOM`, active-country status, IW-050 package identity, Independence Wave origin, and excludes Soviet Collapse origins.
- `independence_wave_refresh_komi_compact_lifecycle` in `common/scripted_effects/006_independence_wave_komi_package_effects.txt:33-47` sets or clears `independence_wave_komi_compact_stabilized` from the compact variables.
- Setup sets `independence_wave_komi_ai_profile` and `independence_wave_iw_050_setup_complete` in `common/scripted_effects/006_independence_wave_komi_package_effects.txt:309-375`; cleanup clears those flags and route flags at `common/scripted_effects/006_independence_wave_komi_package_effects.txt:400-432`.
- Emergency installation sets `independence_wave_komi_taiga_emergency_government` at `common/scripted_effects/006_independence_wave_komi_package_effects.txt:218-232` and only blocks an already-selected Komi route through `has_independence_wave_komi_route_government`.
- No source-level mutual exclusion is present between the survival, settled, host-restraint, and emergency strategy blocks. Because `abort_when_not_enabled = yes` follows each block's own gate, overlapping true flags could cause additive strategy contributions. This is a source-level overlap observation only; the MCP adapter did not prove whether the engine applies these rows cumulatively in the relevant consumers.
- No positive strategy is proven impossible or dead by this audit. `infrastructure`, `bunker`, `infantry`, `artillery`, and `support` are recognized vanilla strategy identifiers, but target validity and available production/building state were not evaluated.

## Findings and risk classification

- Adapter coverage blocker: `ai_strategy_factor` returns `no_weighted_surfaces` for the source and `PROBABILITY_SURFACE_EMPTY` for the named empty evaluation. Probability result: unresolved.
- Candidate pool: unavailable, not complete. No exact or bounded normalized result is valid.
- Base values: source literals are recorded above. Modifier traces, active-state traces, ranking, timing, and selection frequencies: unavailable.
- Dominance, starvation, rank reversal, repetition, and snowball/exploit risk: unresolved. The possible additive overlap is a review lead, not a measured finding.
- Score-versus-probability distinction: these are AI strategy-factor inputs and downstream AI scores/need weights. They are not click probabilities; `build_building` has a separate internal weighted build-selection consumer, but its full pool is not exposed here.

## Recommended owner follow-up, not applied

1. Keep the current source unchanged until the probability adapter can expose `ai_strategy_factor` rows or a supported equivalent. Re-run `hoi4.probability_inspect` and the same named empty fixture first, then add only parent-declared typed Komi package states with a complete strategy consumer pool and external factors.
2. Once the route is available, test the exact lifecycle boundary where compact stabilization, former-host settlement, and emergency government can coexist. Use the result to decide whether survival and settled infrastructure/army rows, or host and settled restraint rows, should be explicitly mutually exclusive or intentionally additive.
3. If the owner wants centralized tuning, consider moving the nine Komi tuning aliases to `common/script_constants/006_independence_wave_komi_constants.txt` where the affected field supports script constants, while preserving parser-safe local aliases for unsupported fields. This is a maintainability recommendation, not a balance target.
4. Any source change to these strategy values or gates requires a fresh baseline audit followed by a same-scenario `hoi4.probability_compare`; this handoff supplies no patch and no target values.

## References consulted

- Offline wiki: `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` and the required core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, and idea modding.
- Vanilla documentation: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\ai_strategy\_documentation.md`, `common/ai_strategy/default.txt`, and the installed documentation markdown for triggers, effects, modifiers, script concepts, dynamic variables, script math, localisation formatting/objects, and script collections.

## Remaining uncertainty and blockers

The installed `ai_strategy_factor` probability route is the sole blocking evidence gap for quantitative Komi strategy analysis. No rendered ranking, matrix, sensitivity, timing, comparison, or unresolved-view artifact exists for this surface. The parent must carry the unresolved status and must not present the literal source values as normalized probabilities or campaign balance evidence.
