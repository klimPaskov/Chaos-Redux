# Event 016 Mengele conventional AI probability baseline

Date: 2026-09-08

Status: bounded read-only baseline complete for the existing Kruger weaponization adapter pair; added private Mengele candidates remain pre-AI and therefore have no weighted baseline. No gameplay, decision, trigger, AI, configuration, or runtime files were edited by this auditor, and no commit was created.

## Scope and ownership

The audited weighted surface is the existing Kruger board in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, limited to `brilliant_scientist_advance_rocketry_weaponization` and `brilliant_scientist_advance_high_energy_weaponization`. Their decision blocks are at lines 1606-1661 and 1777-1832. Deployment rows were not changed or used as a replacement comparison surface.

The proposed private surface is `common/decisions/016_mengele_conventional_stage_decisions.txt`. The owner has written 15 rows, not 20: electronics, materials, rocketry, high-energy, and biomedical, each with theory, deployment, and weaponization. The source rows are at lines 23-638 and contain no `ai_will_do` blocks at this baseline freeze. The prototype stage is intentionally absent because the owner confirmed that the five native prototype paths are used rather than redundant private prototype decisions.

The exact scenario fixture is [016_mengele_conventional_probability_baseline_2026-09-08.json](../testing/016_mengele_conventional_probability_baseline_2026-09-08.json). It preserves the complete two-ID Kruger score pool, all 20 named scenario identities sent to the full baseline evaluation, the 15-ID added-candidate boundary, and the declared native/predecessor gate expectations separately from the MCP score overrides.

## Required references read

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-event-planning/SKILL.md`. I also consulted the offline Paradox wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding`.

The relevant vanilla documentation consulted was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `dynamic_variables_documentation.md`. The installed game version reported by the probability adapter is Operation Postern 1.19.2.0, checksum d245.

## Added-candidate baseline boundary

The first mandatory inspect was issued before the private source existed for the proposed 20-ID Cartesian set `mengele_event016_<family>_<theory|prototype|deployment|weaponization>`. MCP returned `PROBABILITY_SOURCE_NOT_FOUND` for `common/decisions/016_mengele_conventional_stage_decisions.txt`; no artifact, source revision, source hash, or candidate comparison exists for that absent source. This is the explicit added-candidate baseline: the new IDs were not falsely compared with unrelated existing candidates.

After the owner wrote the source, the current 15-ID set was inspected again. Both requested `decision_ai_will_do` and the correctly discovered `mission_ai_will_do` routes returned `PROBABILITY_SOURCE_DISCOVERED`, zero weighted candidates, zero available candidates, and `no_weighted_surfaces`/empty discovery. The current source revision was `9462f377e5a93b3d2c8887a95159d48a2f388878ad7fca79a4c821b4f9f9a053`, source hash `891f7f7b01acb000caf6452e0bb24c58534e639d938a153f9c74bda3b4e681a4`.

Inspect artifacts:

- Decision request: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc28eb4f08725d2f761f8c42b12092e17d0600a40ae522a38ff9006aa97c679e/557351bcde17afa43eea27c7d49851b7eba19de64ce50e2c59b7d99263587f3d/probability-inspect-891f7f7b01ac.json`.
- Mission adapter: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5c4fdba0e7f2177cf619287db23a2f52327eaa0ba9369c481a9e1bec1368de8/7243beab43d2d6caebff589ff9a1a7c229db832a639fed2c831d39de33fbaf9d/probability-inspect-891f7f7b01ac.json`.

A direct evaluation of the current 15 IDs was attempted with the source path, the exact two named private scenarios `E016_MENGELE_NEW_PRIVATE_PEACE` and `E016_MENGELE_NEW_PRIVATE_WAR`, and a complete declared 15-ID pool. MCP returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request` and `availableAdapters=[]`; it produced no artifact. No private AI score, rank, eligibility, dominance, starvation, or probability conclusion is claimed.

## Kruger source and gate review

The Kruger inspect was started with the requested `decision_ai_will_do` route. The source was discovered but classified as `mission_ai_will_do`; the mission inspect with the exact two-ID pool then returned `poolComplete=true`, `candidates=2`, `availableCandidates=0` (the supplied source path is the active weighted surface), and `requiredInputs=3` with no unresolved inspect diagnostics.

Inspect artifacts:

- Decision request/discovery: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0561b5c5d76a62be6d370904207a1416336af6b6d78d135e54a7411fd5dd0112/71180cfedb65c8b6c345ab57456dfe54914340a3bb851bc7afd7b8da56a28dcc/probability-inspect-c7038588658a.json`.
- Mission adapter/pool: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9c488471637120cbc943ad8931469d12ec96ac095cbb7cd38c4090d451473bc/761d0898539cb99218248fde3958aeacc2eb7fe7cc5847249545acc4ef0316bf/probability-inspect-c7038588658a.json`.
- Inspect source hash: `c7038588658afc29f36bc502277226d36171de0a74be4f678ad9b810e54d0d58`.
- Inspect source revision: `367f23966b850b83dcd3da1158d17c210f46e8b7c32159e5b80aecec0e3786e5`.

The source-backed availability defect is independently visible in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`. `brilliant_scientist_can_begin_rocketry_weaponization` at lines 577-589 requires board readiness, exact weaponization affordability, the deployment predecessor, and an OR of `sp:sp_rockets_long_range_ballistic_missile` or `sp:sp_air_supersonic_jet`. `brilliant_scientist_can_begin_high_energy_weaponization` at lines 667-679 requires the same board/cost/predecessor gates and an OR of `sp:sp_thermo_nuclear_bomb` or `sp:sp_nuclear_warheads`. The current no-DLC decision-owned predecessor state does not satisfy either native-only OR when no native completion exists. This is a source/gate finding, not a probability claim.

The paired cost helpers are also explicit. Rocketry weaponization at lines 557-575 checks civilian and military factories, support equipment, trucks, trains, fuel, manpower, army experience, air experience, political power, tungsten, rubber, and weaponization capacity. High-energy weaponization at lines 649-665 checks civilian and military factories, support equipment, trucks, trains, fuel, manpower, political power, tungsten, chromium, and weaponization capacity. The flat MCP scenario schema cannot type these compound resources, scopes, or special-project completion states.

## Baseline evaluation

The full requested scenario identity was `E016_MENGELE_CONVENTIONAL_ADAPTERS_2026_09_08`. It contained 20 scenarios covering private eligible peace/war, nonowner, current Kruger host, predecessor absent, exact affordability, support-equipment/fuel/manpower shortages, active other/same family, DLC native prototype label, no-DLC decision-prototype label, completed stage, and the explicit DLC/no-DLC plus correct/wrong predecessor plus native absent/complete combinations. The score fixture supplied both Kruger candidates as `candidateOverrides=true` in every row so the weighted race remains identical for the later same-scenario comparison; expected live availability is recorded separately in the fixture.

The mission adapter evaluation completed with zero unresolved rows and zero diagnostics:

- Analysis id: `probability-07549106fa411f7bcdd36d84`.
- Source hash: `c7038588658afc29f36bc502277226d36171de0a74be4f678ad9b810e54d0d58`.
- Evaluation source revision: `c834f98283cbf3d38f0aa633788522266db29f3d222986efc34f992b27b61b88`.
- Scenario hash: `0554685fc1eca42c6fa8be6dfb7773ce9226a038e3a193c9e936bdef906c3971`.
- Candidate rows: 40 across 20 scenarios; `poolComplete=true` within the declared two-ID weighted surface.
- Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1832a5fbace9c7d4151991c09730c45f908072c3c558c58cdb26d9279163149c/85c5d24c3da523f8845dee73c2f59d1d2feee5608a30153f1610f84e84cf9506/probability-07549106fa411f7bcdd36d84.json`.
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24add72a774dab27f2af742a65cb8cb5fdc00a25434b6a78fc6f862744af6d8a/6869e2db56c0903d2e330feea46e28e7cc6bb1afecb507b077ba652ea78823c4/probability-probability-07549106fa411f7bcdd36d84-ranking.svg`.
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2548eb3f90e52c4363b575cd5e040049eb633534661e35ea492bda9d716d8fbc/5edac9d634965050511a57383f2580677788eebea76e3acfd08f300386067973/probability-probability-07549106fa411f7bcdd36d84-ranking.png`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23f6926b67b5c81ff35972b263bbfddfbfbc7304f7b43058ab7c37d992b793c2/ac52724ff62791a011eb67244ce03ca2d2f28b9aa15126248188829564877c28/probability-probability-07549106fa411f7bcdd36d84-matrix.svg`.
- Matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/488feff0ed28382749bddce45a145fe98326de8ea03b1b92d8f3b57687fdea80/e466a1b86be73d2fc9e35025b4b86aa2bf5ebe73e068a4df461e203602f23c23/probability-probability-07549106fa411f7bcdd36d84-matrix.png`.
- Unresolved SVG/PNG were emitted with the JSON and both report zero unresolved rows.

The MCP authoritative score traces are stable across the returned scenario rows and the two-scenario sanity evaluation:

| Candidate | Base constant | Source factors in trace | Raw score in returned rows | Rank |
| --- | --- | --- | ---: | ---: |
| `brilliant_scientist_advance_rocketry_weaponization` | `brilliant_scientist_project_board.ai_high` = 10 | `preferred_factor` = 2; `cautious_factor` = 0.5 | 10 | 1 |
| `brilliant_scientist_advance_high_energy_weaponization` | `brilliant_scientist_project_board.ai_medium` = 5 | `preferred_factor` = 2; `cautious_factor` = 0.5 | 5 | 2 |

The score gap is 5 in the returned rows, with rocketry ahead. `conditionalProbability` is null by design. The adapter declares `selectionRule=score_only` and `normalizedProbability=false`, so these are willingness scores and must not be presented as click or selection percentages.

The flat scenario probe is itself a boundary finding. The adapter marked the `has_war` and low-capacity modifier trace entries applied even in the `E016_FLAGS_NONE` and peace rows, yielding the same 10/5 result as the war row. The source conditions are visible, but the accepted flat state/flags schema did not bind those compound runtime states reliably. Therefore no war preference, capacity response, or cost-shortage behavior is certified from the returned score matrix; only the source-local arithmetic trace and stable rank in the supplied score boundary are exact.

## Sweep and rendering

The bounded mission sweep used paths `has_war` and `capacity`, two supplied numeric scenario endpoints, pairwise interaction, and rank-reversal search. It completed with zero unresolved rows, two sweep points, no breakpoints, no local elasticities, no pairwise interactions, and no rank reversals. Both points returned rocketry 10 / high-energy 5. Because the flat state did not bind the source conditions, this is a bounded adapter result, not proof that the live game has no war/capacity threshold.

- Sweep analysis id: `probability-c2911fecbbb55fe942e8f45d`.
- Sweep scenario hash: `0e28a0b5405a7cc301194b57c055cf49a0c567b304fa37e5703e87cdfabc7001`.
- Sweep JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e65b29fe84dd1de4386a88c17c8c6f4a80fdc9f0f2b5402351963fcb80166f9/3350c5376fa8af34bdd7254f0b51d57212e5c983ce1957c781984f10178933b3/probability-c2911fecbbb55fe942e8f45d.json`.
- Sweep sensitivity SVG/PNG and threshold SVG/PNG were emitted in the same result; the unresolved SVG/PNG are also preserved there.

An explicit `probability_render` request was attempted for both the 20-scenario evaluation and the sweep with their exact analysis ids and scenario hashes. The server returned `PROBABILITY_ANALYSIS_NOT_CACHED` because rendering requires an analysis id produced by the current server process. The evaluation and sweep already emitted ranking, matrix, sensitivity, threshold, and unresolved artifacts, so no visual evidence was substituted or fabricated.

## Findings by audit category

- Candidate pool: exact and complete only at the declared two-ID Kruger weighted surface. The all-board source contains other unrelated Kruger rows, which were intentionally not mixed into this same-candidate baseline. The new private 15-ID source currently has no weighted blocks; the original 20-ID absent-source request and current 15-ID no-AI source are separate states.
- Eligibility: source-gate conclusion is bounded to the native OR and the visible board/cost/predecessor checks. Private owner, active-family, exact-cost, capacity, DLC, native completion, and decision-owned predecessor states are not all executable through the flat probability scenario schema.
- Dominance: rocketry has the higher base and remains rank 1 by five score points in returned traces. This is an observed existing shared-family constant result, not a tuning recommendation.
- Starvation: unresolved for live choice because no complete runtime candidate availability and no normalized selection rule were provided.
- Rank reversal: none in the bounded two-point sweep; not certified for live gate changes because the relevant states were not bound.
- Repetition, timing, cooldown, reset, recovery, terminal-state behavior: not modeled by this `mission_ai_will_do` score adapter and no custom weighted-pool cadence was declared.
- Exploit risk: the two weaponization `can_begin` triggers have a native-only OR that blocks the no-DLC decision-owned predecessor state when no native project is complete. This is the concrete source defect held for the parent’s narrow patch. No claim is made that the deployment rows need the same substitution; the parent confirmed the vanilla deployment alternatives remain available without Gotterdammerung.

## Recommendations without applying them

1. Keep the owner’s private 15-row boundary. After AI is attached, use the accepted shared constants: electronics/materials/rocketry/biomedical `ai_high`, high-energy `ai_medium`, and the shared at-war `preferred_factor`. Do not infer a private Capacity factor from the Kruger rows; the private owner is active and the accepted intent is no Capacity modifier.
2. In `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, add the approved decision-owned predecessor alternative only to `brilliant_scientist_can_begin_rocketry_weaponization` and `brilliant_scientist_can_begin_high_energy_weaponization`. Preserve board readiness, exact stage cost, deployment predecessor, and the genuinely available native OR branch. Leave deployment gates unchanged.
3. After the owners finish their patches, rerun `probability_inspect` first on the current source, then evaluate the same fixture scenario-set id and candidate-pool boundaries. Run `probability_compare` only with the frozen before/after source pair and the exact baseline scenario identity; preserve both source hashes/revisions, scenario hash, comparison id, and emitted evidence. Do not normalize the mission scores.

## Skipped analyses and exact blockers

- New private candidate evaluation: skipped as a balance result because MCP returned `PROBABILITY_SURFACE_EMPTY` for the current no-AI source. There is no private score artifact.
- Direct structural decision inspect/render: no decision-specific structural MCP route was exposed in this runtime; probability inspect/evaluate and source review were used for the weighted surface.
- Explicit render: blocked by `PROBABILITY_ANALYSIS_NOT_CACHED` for both completed analysis ids; emitted render resources from evaluate/sweep are preserved.
- Simulation: not run; no uncertain input distributions or approved seed were declared.
- Sequence: not run; no complete custom-pool cadence, cooldown, recovery, cap, removal, reset, timer, or terminal-state manifest exists.
- Same-scenario compare: not run in this baseline because no owner-applied after source exists. A current-vs-current or unrelated-ID comparison would violate the requested baseline contract.
- Live HOI4 launch/gameplay validation: not performed; it belongs to the user.

## Handoff conclusion

The parent can safely release the two-gate patch with a frozen, source-backed baseline: the exact existing Kruger pool is discovered by the mission adapter, the full named 20-scenario score evaluation is complete and artifacted, the raw trace is rocketry 10 versus high-energy 5 with score-only semantics, and the native-only no-DLC gate defect is visible in the two scripted triggers. The added private source is present at 15 rows but has no weighted AI surface, so there is no truthful new-candidate probability baseline yet. No balance target or weight patch was chosen by this auditor.

## Post-patch bounded MCP evidence

The parent attached AI to all fifteen private rows after the frozen baseline. Electronics, Materials, Rocketry, and Biomedical use `brilliant_scientist_project_board.ai_high`; High Energy uses `brilliant_scientist_project_board.ai_medium`; all rows use the existing at-war `brilliant_scientist_project_ai.preferred_factor`; no Capacity modifier was added.

The required post-patch inspect was rerun before evaluating the private pool. The requested `decision_ai_will_do` route returned `PROBABILITY_SOURCE_DISCOVERED` with zero decision candidates and suggested `mission_ai_will_do`; the mission route returned `PROBABILITY_SOURCE_INSPECTED`, a complete fifteen-candidate pool, zero available candidates under the un-overridden source discovery state, two required inputs, and zero unresolved diagnostics. The current private source revision is `8534fb9cbdab6aa346c1e8938feb02e19d2e8c72594b8d8dc803a234803a7b6f`, and its MCP source hash is `d3db0309078973288f62c3c0723906f777200e3db113aa21529766d52d7b0581`.

The bounded private evaluation used the same twenty named scenario identities as the frozen fixture, a separate `_NEW15_POST_AI` scenario-set label, the complete fifteen-ID candidate pool, and explicit true candidate overrides solely to expose the score expressions. It returned analysis `probability-cfc6f29fe5d9c3cd8dc74fdc`, scenario hash `dafc71f0af25178c3231f76b64f22d4f965469e9b50ab6fd5db54e81cc13c410`, 20 scenarios, 300 candidate rows, zero unresolved rows, and zero diagnostics. The authoritative JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46c32336fab6e35836d17cee40f3874496b05a5bd186b54440a38a431c79c97e/d30c3c57452a7b20aee1ecb2d593e9763ce0a09e060f8cd1170ee5a5b1027a68/probability-cfc6f29fe5d9c3cd8dc74fdc.json`, with ranking and matrix render resources recorded in [the post-patch fixture](../testing/016_mengele_conventional_probability_postpatch_2026-09-08.json).

Across all twenty scenario rows, each Electronics, Materials, Rocketry, and Biomedical row scored 20 before any unbound live-gate interpretation, with ranks 1-12 occupied by those twelve IDs; each High Energy row scored 10 with ranks 13-15. The trace is base 10 or 5 followed by the preferred factor 2. Every row reports `eligibility=true` only because the score fixture explicitly overrode each candidate, and every `conditionalProbability` is null. This is an exact MCP score result and not a live eligibility or normalized probability result.

The mandatory Kruger compare used the two exact Weaponization IDs and all twenty named scenario identities. Path-only before and after board-source selectors were accepted by MCP; identifier or historical source pinning was rejected at the tool boundary. The compare returned analysis `probability-0fe892fa51efde812ddbcd79`, 20 scenarios, 40 rows, zero unresolved rows, zero diagnostics, zero comparison changes, source hash `c7038588658afc29f36bc502277226d36171de0a74be4f678ad9b810e54d0d58`, and source revision `6e71a8cc28dd4e7b5281f6bd144d52427f0c92bd7a0f8d52a067ef382f990f5b`. JSON, ranking, matrix, comparison, and unresolved artifacts are preserved in the post-patch fixture.

The current compare hash is `34cdc8b3e288c8809796a331f94b6106ccfc9f59d078803d9c7706aeef4619c0`, while the frozen baseline analysis records `0554685fc1eca42c6fa8be6dfb7773ce9226a038e3a193c9e936bdef906c3971`. The 20 scenario IDs and two-ID candidate boundary are preserved, but the current MCP canonical hash does not equal the frozen hash. This exact-hash mismatch is left unresolved rather than relabeled; the compare's zero-change result therefore proves only that the compared mission score source did not change, not that the trigger-file patch was quantitatively compared.

## Separate source-eligibility truth matrix for the two Kruger Weaponization gates

The matrix below is source logic, not probability evidence. It assumes `board_ready=true` and varies DLC, native completion, valid Deployment predecessor, and exact affordability. Both triggers require the board gate, their exact cost helper, and the valid Deployment predecessor before the native OR. After the owner patch the OR is `native_completion OR NOT has_dlc = Gotterdammerung`.

| DLC | Native completion | Deployment predecessor | Exact affordability | Source gate |
| --- | --- | --- | --- | --- |
| yes | yes | valid | yes | true |
| yes | yes | valid | no | false |
| yes | yes | invalid | yes | false |
| yes | yes | invalid | no | false |
| yes | no | valid | yes | false |
| yes | no | valid | no | false |
| yes | no | invalid | yes | false |
| yes | no | invalid | no | false |
| no | yes | valid | yes | true by source logic; native runtime realizability is not asserted |
| no | yes | valid | no | false |
| no | yes | invalid | yes | false |
| no | yes | invalid | no | false |
| no | no | valid | yes | true through the approved no-DLC alternative |
| no | no | valid | no | false |
| no | no | invalid | yes | false |
| no | no | invalid | no | false |

If `board_ready=false`, all sixteen rows are false. Rocketry's native alternatives are `sp:sp_rockets_long_range_ballistic_missile` and `sp:sp_air_supersonic_jet`; High Energy's are `sp:sp_thermo_nuclear_bomb` and `sp:sp_nuclear_warheads`. This matrix does not infer runtime eligibility from score-only output and does not change the unchanged Deployment controls.

The complete structured evidence, artifact URIs, source hashes, score summary, matrix rows, and limitations are in [016_mengele_conventional_probability_postpatch_2026-09-08.json](../testing/016_mengele_conventional_probability_postpatch_2026-09-08.json). No gameplay source was edited by this auditor.
