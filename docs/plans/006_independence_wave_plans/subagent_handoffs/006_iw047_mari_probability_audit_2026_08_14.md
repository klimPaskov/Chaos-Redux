# IW-047 Mari El AI-strategy probability audit — 2026-08-14

## Disposition

**FAIL-CLOSED / UNRESOLVED.** The current Mari El (`MEL`) AI-strategy source was inspected through the mandatory HOI4 MCP probability route, but the installed `ai_strategy_factor` adapter reported no weighted surface. A named empty-state evaluation returned `PROBABILITY_SURFACE_EMPTY`, so this pass proves source discovery and an adapter limitation only. It does not prove strategy activation, effective factor accumulation, ranking, timing, dominance, starvation, repetition, or campaign balance.

No gameplay, AI, country, focus, decision, localisation, or runtime files were edited. This handoff is the only output of the read-only probability audit.

## Audited surface and source

- Event/package: IW-047 Mari El.
- Carrier: `MEL` / Mari El.
- Weighted surface: `common/ai_strategy/006_independence_wave_mari.txt`.
- Requested MCP adapter: `ai_strategy_factor`.
- Current source contains four AI-strategy entries and twelve strategy assignments:
  - `independence_wave_mel_forest_survival` (lines 21–35).
  - `independence_wave_mel_host_restraint` (lines 37–47).
  - `independence_wave_mel_settled_compact` (lines 49–59).
  - `independence_wave_mel_emergency_guard` (lines 61–70).

Static source values are exact source facts, not engine-evaluated results. The four layers contain the following assignments:

| Layer | Static strategy assignments | Dynamic gates visible in source |
|---|---|---|
| Forest survival | `build_army = 74`; infantry production `34`; artillery production `18`; support production `52`; infrastructure `66`; bunker `78` | `is_independence_wave_mari_package`; `independence_wave_iw_047_setup_complete`; `independence_wave_mel_ai_profile` |
| Host restraint | `avoid_starting_wars = -245` | MEL package; setup complete; living former host; host ledgers not settled |
| Settled compact | `build_army = 74`; `avoid_starting_wars = -405`; infrastructure `66` | MEL package; `independence_wave_mel_compact_stabilized` |
| Emergency guard | `build_army = 108`; bunker `78` | MEL package; `independence_wave_mel_forest_emergency_government` |

All four entries use `allowed = { original_tag = MEL }` and `abort_when_not_enabled = yes`. The package trigger additionally requires Event 006 origin (`liberation_origin.independence_wave`) and rejects Soviet-collapse origin/flags. The source therefore has explicit identity and lifecycle gates, but the MCP adapter does not expose them as a weighted strategy surface.

## Required references consulted

Before the audit I read `AGENTS.md` and `.agents/skills/chaos-redux-subagents/SKILL.md`. I consulted the required offline wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki/`. The AI-modding reference distinguishes additive/negative AI-strategy values from event-option probabilities and explains the dynamic `enable`/`abort_when_not_enabled` lifecycle.

I also read the installed vanilla documentation files `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md`, plus vanilla AI-strategy precedents in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/default.txt` and `AUS.txt`. Vanilla confirms that AI-strategy entries apply strategy values; it does not turn these values into a normalized candidate-pool probability.

## MCP probability evidence

Workspace for all successful calls: `mod_chaos_redux_ea3b2d67c2c0`.

### Initial missing-source probe

Before the strategy file landed, the required source path was probed once with `hoi4.probability_inspect` (`adapter = ai_strategy_factor`, `source = { path: common/ai_strategy/006_independence_wave_mari.txt }`, `refresh = true`). It returned `PROBABILITY_SOURCE_NOT_FOUND` with the exact blocker `Probability source path was not found`, no artifact, and no data. This is superseded by the successful current-source inspect below and is retained only to document the transient file-availability blocker.

### Baseline inspect (authoritative current-source result)

Call: `hoi4.probability_inspect` with `adapter = ai_strategy_factor`, `source = { path: common/ai_strategy/006_independence_wave_mari.txt }`, `refresh = true`.

Result: `PROBABILITY_SOURCE_DISCOVERED` / `ok` with `discoveryReason = no_weighted_surfaces`.

- Source revision: `6152cfa39ec59335c506da90bb6a3f3377de921c4401cdca8da5723567d0de0e`.
- Source hash: `1ebebf8cc5f53ba2f3fa1e8a615f5c6413557179b9baafe4f8b7ec63fb5392bd`.
- Candidates: `0`.
- Available candidates: `0`.
- Available adapters: empty.
- Required inputs: `0`.
- Inspect unresolved inputs: `0`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/754a7015fd11f12a7851f1b1cc7a1e2ba303d572bfe8b7a9a7bd26fb022cbed9/75dde7347fb8406d33922284d1f5f88094d3c535ab60e187bb071da88d844566/probability-inspect-1ebebf8cc5f5.json`.

This is an exact adapter/source-discovery result. `no_weighted_surfaces` must not be interpreted as proof that the four scripted strategy entries are ignored by the game; it means this MCP weighted adapter cannot expose them for analysis.

### Named evaluation

Call: `hoi4.probability_evaluate` with `adapter = ai_strategy_factor`, the same current source, `metrics = [raw_value]`, `horizonDays = 600`, and scenario set `IW047_MEL_STRATEGY_EMPTY_CURRENT_2026_08_14` containing `MEL_STRATEGY_EMPTY` with an explicitly empty `state = {}` fixture.

Result: `PROBABILITY_SURFACE_EMPTY` / error. Exact blocker: `No weighted blocks matched this request` (`adapterId = ai_strategy_factor`, source path as above). No analysis artifact, scenario hash, candidate rows, or rendered evidence was emitted.

The empty fixture was used only to make the scenario explicit; it is not a typed campaign state. Candidate-pool completeness is **not applicable at the adapter level because the adapter returned zero candidates**, and external-factor completeness is **incomplete/unresolved** because no strategy surface was exposed. No exact or bounded runtime value is claimed.

## Compare, sweep, render, simulation, and sequence status

- `hoi4.probability_compare`: skipped. The inspect returned `no_weighted_surfaces`, and this newly landed source has no identifiable pre-patch source revision. A same-source comparison would be only a capability receipt and would not establish a patch effect.
- `hoi4.probability_sweep`: skipped. There is no candidate/range-bearing analysis; the adapter returned zero candidates before threshold or rank-reversal analysis.
- `hoi4.probability_render`: skipped. No analysis ID or rendered analysis artifact exists. The inspect JSON is the only probability artifact.
- `hoi4.probability_simulate`: skipped. No uncertain inputs or supported candidate distribution can be declared when the adapter exposes no surface; no seed or sample result exists.
- `hoi4.probability_sequence`: skipped. This source is not a declared custom weighted pool and no cadence, cooldown/recovery, removal/reset, cap, timer, or terminal-state manifest was supplied.

## Findings and risk boundaries

1. **Adapter limitation, not a dead-strategy proof.** The only current engine-backed result is `no_weighted_surfaces` followed by `PROBABILITY_SURFACE_EMPTY`. Treating the four blocks as zero-valued or inactive would exceed the evidence.
2. **Static layer overlap is possible.** The forest-survival layer remains enabled from `independence_wave_iw_047_setup_complete`, while settled compact keys only on `independence_wave_mel_compact_stabilized` and emergency guard keys only on `independence_wave_mel_forest_emergency_government`. The source alone does not prove whether settled or emergency layers are intended to stack with survival during intermediate states. Effective additive overlap is unresolved without a working adapter and typed fixtures.
3. **Static values are not probabilities.** Values such as `74`, `108`, `-245`, and `-405` are strategy-factor inputs. They are not normalized click probabilities, selection chances, or timing distributions.
4. **No balance claim.** Dominance, starvation, rank reversal, repetition, unsafe snowball behavior, and war-restraint effectiveness remain unresolved. The MEL package remains fail-closed for quantitative AI acceptance.

## Recommended owner follow-up (not applied)

1. Preserve the current source revision/hash as the post-owner-patch reference. If the package owner changes any strategy value or gate, retain a valid pre-change source path and rerun this exact inspect-first workflow before a true same-scenario compare.
2. Repair or extend the installed MCP `ai_strategy_factor` adapter so these four strategy entries can be exposed with activation gates and additive traces. Until then, do not tune numbers based on this receipt.
3. Once the adapter is available, supply typed MEL fixtures for at least `setup/forest survival`, `living former host/unsettled ledgers`, `settled compact`, `forest emergency government`, and cleanup/terminal states. Declare package identity, setup/profile flags, former-host existence and war, compact stabilization, route government, state/capital ownership for state 833, and generation/origin guards.
4. Re-evaluate the same scenarios and inspect whether survival, settled, host-restraint, and emergency layers intentionally overlap. If stacking is unintended, the owner should make the gates mutually exclusive in `common/ai_strategy/006_independence_wave_mari.txt` or clear superseded strategy flags in the package effects; this is a conditional design recommendation, not a proven defect.
5. After a real owner-applied AI change, run `hoi4.probability_compare` with the same complete scenarios and preserve the comparison ID, scenario hash, source revisions, and rendered ranking/matrix/sensitivity/unresolved artifacts.

## Remaining uncertainty and simplifications

- No simplification or fallback was applied.
- No quantitative AI conclusion is made because the required adapter surface is unavailable.
- No live HOI4 session, save/load test, or runtime strategy-dump validation was performed; live validation remains parent/user-owned.
