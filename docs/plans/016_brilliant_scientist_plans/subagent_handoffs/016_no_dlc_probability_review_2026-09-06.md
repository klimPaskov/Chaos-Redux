# Event 016 no-DLC project-board probability review

Date: 2026-09-06.

Status: read-only baseline for parent review. No gameplay, AI, decision, trigger, effect, constant, localisation, fixture, or runtime file was edited. The required probability service calls were attempted, but the current service timed out before returning an artifact, so engine ranking and probability conclusions remain unresolved.

## Audited surface and source identity

The audited surface is the no-DLC Event 016 Directorate board fallback tranche in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`.

The weighted surface contains exactly 15 fallback Prototype decisions and six fallback Singularity component decisions, for 21 unique source IDs:

```text
brilliant_scientist_fallback_computation_prototype
brilliant_scientist_fallback_electronics_prototype
brilliant_scientist_fallback_materials_prototype
brilliant_scientist_fallback_rocketry_prototype
brilliant_scientist_fallback_high_energy_prototype
brilliant_scientist_fallback_biomedical_prototype
brilliant_scientist_fallback_teleportation_prototype
brilliant_scientist_fallback_cloning_prototype
brilliant_scientist_fallback_robotics_prototype
brilliant_scientist_fallback_paleogenetics_prototype
brilliant_scientist_fallback_xenobiological_synthesis_prototype
brilliant_scientist_fallback_biological_weapons_prototype
brilliant_scientist_fallback_alien_arms_prototype
brilliant_scientist_fallback_temporal_prototype
brilliant_scientist_fallback_singularity_prototype
brilliant_scientist_fallback_singularity_command_core
brilliant_scientist_fallback_singularity_power_link
brilliant_scientist_fallback_singularity_containment_lattice
brilliant_scientist_fallback_singularity_temporal_authenticator
brilliant_scientist_fallback_singularity_delivery_architecture
brilliant_scientist_fallback_singularity_fail_deadly_governor
```

The source-level candidate count is 15 Prototype IDs plus six component IDs, with no duplicate IDs. The fixture `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_NO_DLC_PROJECT_FALLBACK_2026_09_05.scenarios.json` declares the same 21-candidate pool.

The source files reviewed were:

- `common/decisions/016_brilliant_scientist_directorate_project_board.txt` (SHA-256 captured during this audit: `22AC7C1509DC59B528A2B8F659F35C626F5B046AD43419C2EADBEF9F11BEB27E`).
- `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` (SHA-256: `CD3A83D68580FA7C3F39B5E69017316B6A33A70C43AF0EBCBEA00F8DB9039729`).
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt` (SHA-256: `D44FC830193305033F5A6695C9D0CB7C1B519F15157E787632413FBFD93AECFA`).
- `common/script_constants/016_brilliant_scientist_project_constants.txt` and `common/script_constants/016_brilliant_scientist_constants.txt`.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_no_dlc_project_progression_fallback_2026-09-05.md`.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_NO_DLC_PROJECT_FALLBACK_2026_09_05.scenarios.json` (SHA-256: `799DD56EF11FDE9294935CCE1A6D95F17FA260135E3E130B017A1932C04F4C10`).

The decision entries are at approximately lines 5028-5694 for the 15 Prototype adapters and lines 5705-5882 for the six component adapters in the captured source. The exact line numbers are source-version-sensitive; the hashes above identify the audited snapshot.

## MCP probability workflow and evidence

The `chaos-redux-subagents` and `chaos-redux-decisions-missions` skills were applied. Offline Paradox wiki decision/AI pages, the required core wiki pages, and the relevant vanilla documentation pages for decision availability, AI weights, DLC triggers, resource/equipment triggers, variables, and timed decision removal were read before source review.

The required opening call was made first with `hoi4.probability_inspect` for the requested `decision_ai_will_do` adapter, the Event 016 board source, the complete 21-ID pool, and workspace `mod_chaos_redux_ea3b2d67c2c0`. It timed out after 180 seconds with `tool call failed ... timed out awaiting tools/call after 180s`; no current artifact, revision, scenario hash, or render URI was returned.

Because the prior handoff recorded an adapter mismatch, `hoi4.probability_inspect` was retried with `mission_ai_will_do`, once with refresh and once without refresh, using the same source and complete 21-ID pool. Both calls timed out after 180 seconds with the same service-boundary error.

The required named-scenario evaluation was then attempted with `hoi4.probability_evaluate` using `mission_ai_will_do`, the complete 21-ID pool, all six fixture scenarios, raw-value and conditional-probability metrics, ranking/matrix/unresolved outputs, and dominance/starvation/rank-reversal diagnostics. It timed out after 180 seconds and returned no artifact.

The required sensitivity pass was attempted with `hoi4.probability_sweep` over the same six scenarios and pool, varying `state.political_power`, `state.num_of_available_civilian_factories`, `state.brilliant_scientist_project_capacity`, and `state.brilliant_scientist_singularity_component_count`. It timed out after 180 seconds and returned no artifact.

`hoi4.probability_render` was attempted against the prior evaluation analysis ID recorded by the 2026-09-05 handoff, `probability-e91b869c8ba5f1e0fd2c89d9`, for ranking, matrix, and unresolved views. It also timed out after 180 seconds and produced no current render.

No fresh `hoi4.probability_compare` call was made because this audit found no owner-applied AI or weighted-gate patch during the current pass. A compare is mandatory if the owner changes any AI score, availability gate, or weighted candidate logic. The current service timeout also prevents a fresh compare. I could not send the requested direct coordination message to `/root/no_dlc_closure_review` because no collaboration `send_message` route was exposed in this runtime; the parent must relay that compare requirement.

The prior handoff records historical, partial artifacts that must not be treated as current engine proof: inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21f5a3286049219afb74d34ed3a41b79e0eb4b1bc66c8f7db4369a394d4b4d8d/944e253c2f69d86dea755dc6a46f118a7b3d74d56182a0a1bec2fa5731143bba/probability-inspect-cf98b6f7becc.json`; evaluation analysis `probability-e91b869c8ba5f1e0fd2c89d9` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7967e5ed3a070eedd786ac4438cbe5c4ef5a2679187bc50048eaf2eb239ed91b/5bf8ce2492e90270891bf7702bf85b13c568f857843c79f588c5d819161c0b3a/probability-e91b869c8ba5f1e0fd2c89d9.json`; and historical compare `probability-7709ebee871c3aee7658972f` with JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/676b3a24f3c9aa06af95a1825d9426d0b671fb0d4dad4719f70bbdfb53d238e2/488588d58a152fabef3130cc936d205298edcda5a9e33f7757a3793732851763/probability-7709ebee871c3aee7658972f.json` and comparison render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd959714c19fcc0f1325af171a8b8a1d43bab258106cd1edeae95823055fc460/80d67acb70b37ed56caf4b09013a1dd8f83e2b56e130b3df8ce2b941bc884e3b/probability-probability-7709ebee871c3aee7658972f-comparison.svg`. The historical evaluation was `PROBABILITY_ANALYZED_PARTIAL` with six scenarios, 126 candidate rows, 57 unresolved inputs, and zero diagnostics, but the historical compare used a different pool and an earlier source snapshot.

No simulation or custom sequence was run. No uncertain input was declared for sampling, and the fixture does not define the complete cadence, cooldown, recovery, reset, or terminal-state transition contract required for a custom sequence.

No dedicated decision structural inspector or renderer was exposed, so `event_inspect`, `event_render`, focus, GUI, and technology structural routes were not applicable to this decision-only surface.

## Scenario contract and completeness

The six named scenario IDs are `E016_NO_DLC_ALL_FAMILIES_THEORY`, `E016_DLC_PRESENT_NATIVE_AUTHORITATIVE`, `E016_NO_DLC_SINGULARITY_ZERO_COMPONENTS`, `E016_NO_DLC_SINGULARITY_PARTIAL_THREE_COMPONENTS`, `E016_NO_DLC_SINGULARITY_COMPLETE_COMPONENT_CHAIN`, and `E016_NO_DLC_SINGULARITY_TERMINAL_LOCK`.

| Scenario | Candidate-pool completeness | External-factor completeness | Source-backed expectation and classification |
|---|---|---|---|
| `E016_NO_DLC_ALL_FAMILIES_THEORY` | The declared 21-ID tranche is complete, but this state does not declare all family prerequisite inputs. | Host/facility scopes, capacity, payment burdens, reserves, DLC state, war state, and all 15 stage entries are declared. Tech gates for electronics, rocketry, high energy, and biological weapons and the xeno-control state are not declared. | The no-DLC gate is source-exact. Fourteen non-Singularity families can be evaluated only when their family-specific prerequisites are supplied. The Singularity Prototype is ineligible at component count zero. The fixture expectation is conditional rather than an executable all-15 state. Classification: bounded/source-only, not an exact probability result. |
| `E016_DLC_PRESENT_NATIVE_AUTHORITATIVE` | The fallback 21-ID tranche is complete for the hidden-gate question. | DLC state, stage entries, payment burdens, and host/facility scopes are mostly declared, but native special-project completion/availability inputs are not declared. | Every fallback Prototype and component entry has `NOT = { has_dlc = "Gotterdammerung" }`; the native entries have the positive DLC gate. Fallback exclusion is source-exact. Native choice ranking and exact availability remain unresolved. Classification: exact source gate, unresolved engine/native state. |
| `E016_NO_DLC_SINGULARITY_ZERO_COMPONENTS` | The six-component subpool is complete; the full 21-ID pool is not state-complete for unrelated families. | Component count, stage, host/facility flags, no-DLC state, capacity, four spendable burdens, four reserve types, incident state, and terminal booleans are declared. | All six component rows have distinct completion guards and individually satisfy the source-level visibility/payment shape when their helper inputs are valid. The Singularity Prototype is blocked by the six-component count. Classification: bounded/source-only because MCP did not resolve helper state. |
| `E016_NO_DLC_SINGULARITY_PARTIAL_THREE_COMPONENTS` | The six-component subpool is complete with three recorded IDs and three completion flags. | The partial array, count, payment burdens, reserve types, stage, context flags, and terminal booleans are declared. | The three recorded component rows are hidden and the remaining three component rows are the source-level eligible subset. The Prototype remains blocked at count three. No automatic partial-chain transition is present in the reviewed finish/registry effects. Classification: bounded/source-only. |
| `E016_NO_DLC_SINGULARITY_COMPLETE_COMPONENT_CHAIN` | The six-component subpool is complete with all six recorded IDs and flags. | The complete array, count, payment burdens, reserve types, stage, context flags, and terminal booleans are declared. | All six component rows are source-hidden by their completion flags. The Singularity Prototype passes the count gate and remains paid/timed, subject to the board-ready and payment helpers. Classification: bounded/source-only. |
| `E016_NO_DLC_SINGULARITY_TERMINAL_LOCK` | The declared 21-ID tranche is present, but the terminal fixture does not declare the six completion flags or an active receipt variable/flag. | Terminal/global terminal flags and `world_end` are declared, but the active-receipt state required to exercise cleanup is absent. | The source `visible` gates do not include `brilliant_scientist_project_context_is_valid`; therefore terminal rows can remain visible while their `available` gates fail. With the fixture's missing completion flags, the six component rows are not source-hidden merely by count six. Cleanup cannot be observed with no active receipt. Classification: exact source contradiction against the expected hidden view, engine outcome unresolved. |

The fixture's `externalFactors` correctly declares the no-DLC/native gates, shared stage ledger, 10-point Prototype capacity delta, four spendable burden types, and reserve-only steel/tungsten/chromium/rubber checks. It does not fully declare all technology, scripted-helper, target-resolution, native special-project, or AI-population inputs needed for an exact normalized race across all 21 IDs.

## Source-backed score and timing trace

Decision `ai_will_do` is a willingness score/race, not a click probability. The offline AI documentation describes score comparison semantics; no exact selection probability is claimed here.

All 15 fallback Prototype rows use the same trace at decision lines 5070-5700: base `constant:brilliant_scientist_project_board.ai_high = 10`; wartime modifier `preferred_factor = 2`; low-capacity modifier `cautious_factor = 0.50`. The source-only score is therefore 10 in peace with sufficient capacity, 20 at war with sufficient capacity, 5 in peace with low capacity, and 10 at war with low capacity, assuming all listed modifiers multiply as declared. This is score-only evidence, not engine-ranked evidence.

All six component rows use the same trace at decision lines 5732-5882: base `ai_medium = 5` and wartime `preferred_factor = 2`, yielding source-only scores 5 in peace and 10 at war. They have no low-capacity caution modifier, no component-count urgency modifier, and no cost-sensitive modifier.

The flat traces create a potential tie/starvation/repetition risk whenever multiple candidates are simultaneously visible and available. Dominance, starvation ratio, tie resolution, and rank reversal are unresolved because the required inspect/evaluate/sweep service calls timed out. No claim is made that any row has a particular click probability.

The Prototype `days_remove` values reference centralized duration constants: computation 180 days, electronics 210, materials 240, rocketry 270, high energy 360, biomedical 240, teleportation 360, cloning 330, robotics 300, paleogenetics 330, xenobiological synthesis 390, biological weapons 300, alien arms 420, temporal 540, and Singularity 900. Component durations are command core 180, power link 180, containment lattice 210, temporal authenticator 240, delivery architecture 240, and fail-deadly governor 270 days. These are deterministic configured timers, not timing distributions; callback ordering, interruption timing, and engine removal behavior remain unresolved without MCP evidence.

## Gate and progression findings

### F-01: terminal exclusion is missing from fallback visibility gates

Severity: medium/high review finding.

The shared `brilliant_scientist_project_context_is_valid` trigger in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` rejects the country terminal flag, Laboratory World terminal flag, Singularity terminal flag, and `world_end`. `brilliant_scientist_project_board_is_ready` calls that trigger, so the `available` and payment path is blocked at terminal state.

The 15 Prototype `visible` blocks at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:5028-5694` instead check host, no DLC, and the family `brilliant_scientist_can_research_*_prototype` trigger, with an additional active-receipt branch. The family research triggers at `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:1820-2041` reject active incidents but do not call `brilliant_scientist_project_context_is_valid` or directly reject terminal flags. The six component `visible` blocks at lines 5705-5882 similarly call `brilliant_scientist_can_research_singularity_component`, which has no terminal context check.

Consequently, a terminal state can leave fallback rows visible but unavailable, and the supplied terminal fixture lacks the six component completion flags that would otherwise hide completed component rows. This directly conflicts with the fixture's expected hidden terminal view. The recommended source-level fix is for the owner to add a shared terminal/context validity gate to each fallback visibility path, while preserving the active-receipt path only if terminal cleanup is guaranteed to run before the next decision refresh. No fix was applied by this auditor.

### F-02: DLC separation is source-exact, but native state was not engine-proven

The native integration entries use positive `has_dlc = "Gotterdammerung"` gates at the existing native decision blocks, while every fallback Prototype and component entry uses the negative gate. The two presentations are mutually exclusive at source level. Exact native special-project availability and completion inputs are not represented in the fixture, and no current MCP artifact was returned, so native ranking is unresolved.

### F-03: no-DLC family and payment gates are structurally mapped

Each Prototype payment trigger checks no DLC, the family research trigger, civilian-factory capacity, support equipment, fuel, political power, and mapped reserve resources. The reserve checks are prerequisites and are not consumed by the fallback begin effect. Family research gates include the shared host/facility/theory/capacity/incident checks plus the family-specific technology or scenario controls where applicable.

Each component payment trigger checks no DLC, board readiness, component research validity, its own completion flag, civilian-factory capacity, support equipment, fuel, political power, and all four mapped reserve resources. The six completion flags and component array registry are idempotent, so a completed component does not re-add its count. The canonical component finish effect records the component and does not auto-advance the no-DLC Prototype on a partial chain.

### F-04: terminal cleanup is source-wired but not probabilistically or temporally verified

`brilliant_scientist_close_active_project_stage_on_terminal` cancels an active no-DLC component receipt and cancels an active fallback stage unless the active stage is native-owned. `brilliant_scientist_finish_project_stage` requires a valid nonterminal context before advancing the ledger or applying output, so a terminal callback does not receive the normal reward on the source path. The terminal fixture has no active receipt state, so the cleanup expectation cannot be exercised, and callback ordering remains unresolved.

## Recommendations for the owner

- Add a shared context/terminal negative gate to the fallback `visible` triggers, or make the family research helpers include `brilliant_scientist_project_context_is_valid = yes`, then rerun all six named scenarios with the complete 21-ID pool.
- Make the terminal fixture declare the six completion flags and an active component or Prototype receipt when the intended cleanup branch is being tested; otherwise distinguish hidden-view and cleanup scenarios.
- Keep the 21-ID candidate pool explicit in the next MCP run and declare all family technology, xeno-control, native special-project, scripted target, and AI-population inputs needed for a complete race.
- Review whether flat Prototype base-10 and component base-5 traces are intentional. Any AI-weight or gate patch requires a same-scenario `hoi4.probability_compare` against this baseline through `/root/no_dlc_closure_review` or another available probability auditor. This auditor does not select replacement balance targets.

## Skipped analyses, blockers, and remaining uncertainty

- Fresh `probability_inspect`, `probability_evaluate`, `probability_sweep`, and `probability_render` calls all timed out after 180 seconds and produced no current artifacts, revisions, scenario hashes, ranking matrices, sensitivity results, or render URIs.
- Fresh `probability_compare` is pending because no owner patch occurred during this audit and the service was unavailable. It becomes mandatory immediately after any owner patch to AI weights, availability, or weighted gates.
- Direct coordination with `/root/no_dlc_closure_review` was blocked because this runtime exposed no collaboration send-message route. The parent must relay the compare requirement and this service blocker.
- No exact or bounded normalized selection probability, dominance ratio, starvation ratio, rank reversal, or timing distribution is asserted. Source score traces are classified `score-only`; source gate/progression findings are `exact source` or `bounded/source-only`; engine ranking and terminal visibility are `unresolved`.
- No game was launched and no gameplay edits were made.
