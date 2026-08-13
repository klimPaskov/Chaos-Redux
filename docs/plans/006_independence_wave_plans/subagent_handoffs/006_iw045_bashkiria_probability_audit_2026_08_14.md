# IW-045 Bashkiria AI-strategy probability audit — 2026-08-14

## Disposition

**FAIL-CLOSED / UNRESOLVED.** The current Bashkiria (`BSK`) AI-strategy source was inspected through the mandatory HOI4 MCP probability route, but the installed `ai_strategy_factor` adapter reported no weighted surface. The follow-up named evaluation returned `PROBABILITY_SURFACE_EMPTY`, so this pass proves source discovery and an adapter limitation only. It does not prove strategy activation, effective factor accumulation, ranking, timing, dominance, starvation, repetition, or campaign balance.

No gameplay, AI, country, focus, decision, localisation, or runtime files were edited. This handoff is the only output of the read-only probability audit.

## Audited surface and source

- Event/package: IW-045 Bashkiria.
- Carrier: `BSK` / Bashkiria.
- Weighted surface: `common/ai_strategy/006_independence_wave_bashkiria.txt`.
- Requested MCP adapter: `ai_strategy_factor`.
- Current source contains four AI-strategy entries and twelve strategy assignments:
  - `independence_wave_bsk_frontier_survival` (lines 21–35).
  - `independence_wave_bsk_host_restraint` (lines 37–47).
  - `independence_wave_bsk_settled_frontier` (lines 49–59).
  - `independence_wave_bsk_emergency_frontier_guard` (lines 61–70).

Static source values are exact source facts, not engine-evaluated results. The four layers contain the following assignments:

| Layer | Static strategy assignments | Dynamic gates visible in source |
|---|---|---|
| Frontier survival | `build_army = 90`; infantry production `42`; artillery production `24`; support production `48`; infrastructure `78`; bunker `86` | `is_independence_wave_bashkiria_package`; `independence_wave_iw_045_setup_complete`; `independence_wave_bsk_ai_profile` |
| Host restraint | `avoid_starting_wars = -260` | BSK package; setup complete; living former host; host ledgers not settled |
| Settled frontier | `build_army = 90`; `avoid_starting_wars = -430`; infrastructure `78` | BSK package; `independence_wave_bsk_compact_stabilized` |
| Emergency frontier guard | `build_army = 120`; bunker `86` | BSK package; `independence_wave_bsk_emergency_government` |

All four entries use `allowed = { original_tag = BSK }` and `abort_when_not_enabled = yes`. The BSK package trigger also rejects Soviet-collapse origin (`soviet_collapse_active_origin` and `liberation_origin.soviet_collapse`).

## Required references consulted

Before the audit I read `AGENTS.md` and `.agents/skills/chaos-redux-subagents/SKILL.md`. I consulted the required offline wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki/`. The AI-modding reference distinguishes additive/negative AI-strategy values from event-option probabilities and explains the dynamic `enable`/`abort_when_not_enabled` lifecycle.

I also read the installed vanilla documentation files `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md`, plus vanilla AI-strategy precedents in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/default.txt` and `AUS.txt`. Vanilla confirms that `add_ai_strategy`/strategy entries apply AI strategy values; it does not turn these values into a normalized candidate-pool probability.

## MCP probability evidence

Workspace for all successful calls: `mod_chaos_redux_ea3b2d67c2c0`.

### Baseline inspect (mandatory first weighted call)

Call: `hoi4.probability_inspect` with `adapter = ai_strategy_factor`, `source = { path: common/ai_strategy/006_independence_wave_bashkiria.txt }`, `refresh = true`.

Result: `PROBABILITY_SOURCE_DISCOVERED` / `ok` with `discoveryReason = no_weighted_surfaces`.

- Source revision: `971802997ee2c1aa7afb4822f839f6ac307bde1adde39beae5de3355960e1e15`.
- Source hash: `38b83abe93f18b1a122521e57bbab27885bd648caca37949a755c8c26ac745fc`.
- Candidates: `0`.
- Available candidates: `0`.
- Available adapters: empty.
- Required inputs: `0`.
- Inspect unresolved inputs: `0`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e75220f305c08b97f89882646c9ae6226d91a4711545207feb36813654edd4a6/02282b537cf42d5e3b4a3cdf9cae9ced47926c0f5c60f521e207d0c2f91227bb/probability-inspect-38b83abe93f1.json`.

This is an exact adapter/source-discovery result. `no_weighted_surfaces` must not be interpreted as proof that the four scripted strategy entries are ignored by the game; it means this MCP weighted adapter cannot expose them for analysis.

### Named evaluation

Call: `hoi4.probability_evaluate` with `adapter = ai_strategy_factor`, the same current source, `metrics = [raw_value]`, `horizonDays = 600`, and scenario set `IW045_BSK_STRATEGY_EMPTY_CURRENT_2026_08_14` containing `BSK_STRATEGY_EMPTY` with an explicitly empty `state = {}` fixture.

Result: `PROBABILITY_SURFACE_EMPTY` / error. Exact blocker: `No weighted blocks matched this request` (`adapterId = ai_strategy_factor`, source path as above). No analysis artifact, scenario hash, candidate rows, or rendered evidence was emitted.

The empty fixture was used only to make the scenario explicit; it is not a typed campaign state. Candidate-pool completeness is **not applicable at the adapter level because the adapter returned zero candidates**, and external-factor completeness is **incomplete/unresolved** because no strategy surface was exposed. No exact or bounded runtime value is claimed.

## Compare, sweep, render, simulation, and sequence status

- `hoi4.probability_compare`: skipped. The inspect returned `no_weighted_surfaces`, so there is no MCP weighted surface to compare, and this newly created source has no identifiable pre-patch source revision. A same-source comparison would be only a capability receipt and would not establish a patch effect.
- `hoi4.probability_sweep`: skipped. There is no candidate/range-bearing analysis; the adapter returned zero candidates before threshold or rank-reversal analysis.
- `hoi4.probability_render`: skipped. No analysis ID or rendered analysis artifact exists. The inspect JSON is the only probability artifact.
- `hoi4.probability_simulate`: skipped. No uncertain inputs or supported candidate distribution can be declared when the adapter exposes no surface; no seed or sample result exists.
- `hoi4.probability_sequence`: skipped. This source is not a declared custom weighted pool and no cadence, cooldown/recovery, removal/reset, cap, timer, or terminal-state manifest was supplied.

## Findings and risk boundaries

1. **Adapter limitation, not a dead-strategy proof.** The only engine-backed result is `no_weighted_surfaces` followed by `PROBABILITY_SURFACE_EMPTY`. Treating the four blocks as zero-valued or inactive would exceed the evidence.
2. **Static layer overlap is possible.** The survival layer remains enabled from `independence_wave_iw_045_setup_complete` while the settled layer keys only on `independence_wave_bsk_compact_stabilized`; emergency keys only on `independence_wave_bsk_emergency_government`. The package effects clear these lifecycle flags during setup/cleanup, but this source alone does not prove whether settled or emergency layers are intended to stack with survival during intermediate states. Effective additive overlap is unresolved without a working adapter and typed fixtures.
3. **Static values are not probabilities.** Values such as `90`, `120`, `-260`, and `-430` are strategy-factor inputs. They are not normalized click probabilities, selection chances, or timing distributions.
4. **No balance claim.** Dominance, starvation, rank reversal, repetition, unsafe snowball behavior, and war-restraint effectiveness remain unresolved. The BSK package remains fail-closed for quantitative AI acceptance.

## Recommended owner follow-up (not applied)

1. Preserve the current source revision/hash as the post-owner-patch reference. If the package owner changes any strategy value or gate, retain a valid pre-change source path and rerun this exact inspect-first workflow before a true same-scenario compare.
2. Repair or extend the installed MCP `ai_strategy_factor` adapter so these four strategy entries can be exposed with activation gates and additive traces. Until then, do not tune numbers based on this receipt.
3. Once the adapter is available, supply typed BSK fixtures for at least `setup/frontier`, `living former host/unsettled ledgers`, `settled compact`, `emergency government`, and cleanup/terminal states. Declare package identity, setup/profile flags, former-host existence and war, compact stabilization, route government, state/capital ownership, and generation/origin guards.
4. Re-evaluate the same scenarios and inspect whether survival, settled, host-restraint, and emergency layers intentionally overlap. If stacking is unintended, the owner should make the gates mutually exclusive in `common/ai_strategy/006_independence_wave_bashkiria.txt` or clear superseded strategy flags in `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt`; this is a conditional design recommendation, not a proven defect.
5. After a real owner-applied AI change, run `hoi4.probability_compare` with the same complete scenarios and preserve the comparison ID, scenario hash, source revisions, and rendered ranking/matrix/sensitivity/unresolved artifacts.

## Remaining uncertainty and simplifications

- No simplification or fallback was applied.
- No quantitative AI conclusion is made because the required adapter surface is unavailable.
- No live HOI4 session, save/load test, or runtime strategy-dump validation was performed; live validation remains parent/user-owned.
