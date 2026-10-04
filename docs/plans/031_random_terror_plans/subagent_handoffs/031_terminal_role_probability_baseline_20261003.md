# Event 31 terminal-role probability baseline

Status: read-only source-contract baseline delivered for the owner patch; all probability results and MCP source revisions remain unresolved. This is not a balance-completion report for Event 31.

## Scope and evidence class

This audit is bounded to Event 31 final-actor classification, its final-jihad and False Revelation weighted consumers, the terminal defeat gate, and the requested scenarios `W01_preterminal_profile5_below1000`, `W02_preterminal_world_end_disabled`, `W03_preterminal_readiness_missing`, `W04_valid_terminal_actor`, `W05_ordinary_actor`, and `P10_maximum_scenario`.

The following are exact source-contract findings from the current repository files. The result for every score, ranking, normalized probability, scenario trace, timing distribution, and source comparison is unresolved because no probability evaluation returned.

The scenario fixture is [terminal_role_probability_scenarios_20261003.json](../evidence/terminal_role_probability_scenarios_20261003.json), SHA-256 `13AC75BB269307D21667738CCF2387F52D6CD32CEE3DD8A4F8559672C3738727`. It uses the existing Event31 fixture envelope (`schemaVersion`, `id`, `scenarios`, `state`). Scenario acceptance by the connected probability adapter, actor-scope binding, and interpretation of flag-valued entries have not been confirmed.

No simulation seed, uncertain-input distribution, cadence, or scheduled state transition is declared. These are static scenario snapshots, not sampled or sequence evidence. `W04_valid_terminal_actor` declares the post-transaction terminal state; the false-revelation-denied objective remains false in that snapshot.

## Source-contract findings

`common\scripted_triggers\031_random_terror_triggers.txt:25-28` defines `random_terror_is_final_actor` as `random_terror_is_actor = yes` plus `random_terror_actor_profile = final`. It does not require a committed revelation transaction, `random_terror_terminal_active`, a world-end flag, or any transaction receipt. `common\script_constants\031_random_terror_constants.txt:174-185` assigns `final = 5` and `jihadist = 4`.

`common\scripted_effects\031_random_terror_effects.txt:1499-1508` checks Maximum intensity and, if JMX is an actor, calls `random_terror_mark_final_actor` and saves JMX as `random_terror_final_actor`. This branch contains no Chaos 1000 check, readiness check, territorial check, or False Revelation transaction call. The call precedes later scenario setup steps in the same effect.

`common\scripted_effects\031_random_terror_effects.txt:3965-4003` shows the consequence of that call: it sets `random_terror_final_actor`, `random_terror_terminal_command`, and `random_terror_final_jihad_active`; sets actor profile to final and territorial control to its cap; replaces ordinary ideas with `random_terror_presence_of_the_entity`, `random_terror_world_in_revolt`, and `random_terror_supply_through_ruin`; enables the later religious-opposition registry; and applies forced-rule Condemnation.

`common\scripted_triggers\031_random_terror_triggers.txt:375-393` defines the normal False Revelation gate. It requires no existing world end, terminal activity, or resolved revelation; Evolution V unlocked; the branch enabled; the Global Jihad scenario trigger enabled; Chaos at least `1000`; Apocalyptic Readiness at least `80`; International Unity at least `70`; territorial control at least `60`; at least `2` territorial states, crisis states, and strategic victories; and a viable jihadist actor. `random_terror_is_jihadist_actor` accepts both profile 4 and profile 5, so this actor predicate is broader than actual terminal-transaction identity.

`common\scripted_effects\031_random_terror_effects.txt:3514-3536` validates a revelation transaction only when `random_terror_is_final_actor` and the complete normal gate both pass, then commits by scheduling False Revelation. The Maximum caller described above bypasses this transaction validator and calls the terminal marker directly.

`common\scripted_triggers\031_random_terror_triggers.txt:395-421` permits ordinary actor defeat only for a non-final actor after its ordinary collapse condition. A final actor is defeatable only after `random_terror_false_revelation_denied` and a terminal loss condition: no controlled states, territorial control below its gate, or network authority below its unity gate. Because profile 5 alone selects the final branch, a preterminal Maximum JMX loses the ordinary defeat path before the False Revelation transaction. This is an exact source-contract defect; runtime defeat behavior was not executed.

## Weighted consumers and candidate pools

The focus AI surface is `random_terror_lead_the_final_jihad` in `common\national_focus\031_random_terror_focus.txt:2640-2674`. Its `ai_will_do` has base `1`, factor `6` for `random_terror_is_final_actor`, factor `3` above the territorial gate, and factor `3` above the International Unity gate. This is a focus-selection score modifier, not a click probability. The complete available-focus pool, route prerequisites, bypasses, strategy factors, and external campaign state were not established, so its scenario ranking and any rank reversal remain unresolved.

Seventeen decision actions in `common\decisions\031_random_terror_decisions.txt` directly gate visibility or availability on `random_terror_is_final_actor`: `random_terror_raise_local_militia`, `random_terror_integrate_defectors`, `random_terror_repair_captured_depot`, `random_terror_open_external_corridor`, `random_terror_seek_sponsor`, `random_terror_support_foreign_cell`, `random_terror_relocate_network`, `random_terror_convert_militia`, `random_terror_ideological_mobilization`, `random_terror_absorb_actor`, `random_terror_contest_network_leader`, `random_terror_prepare_state_offensive`, `random_terror_build_civil_administration`, `random_terror_force_extraction`, `random_terror_recruit_foreign_fighters`, `random_terror_join_jihadist_international`, and `random_terror_accelerate_revelation`.

The first sixteen are ordinary actor actions gated against profile 5, creating a preterminal action-starvation risk for a Maximum JMX. The False Revelation action remains visible for a profile-5 actor when its branch flags allow it, but `available` calls the full normal gate. Its AI weight therefore cannot make an invalid preterminal launch available. The whole actor-category candidate pool was not inspected by MCP and is incomplete for selection or ranking claims.

`common\decisions\categories\031_random_terror_categories.txt:72-83` also exposes the False Revelation category based on final-actor classification and the terminal/branch-enabled flags. This can expose a terminal category before a transaction when Maximum has marked the actor and the branch flag is enabled; actual action availability still uses the gate above.

The event-option AI surface is `chaosx.nr31.7` in `events\031_terrorist_attack.txt:155-205`. Its complete source-local option set is `chaosx.nr31.7.a`, `.7.b`, `.7.c`, and `.7.d_option`. The final-actor option `.7.a` has raw `ai_chance` base `100`; the subordinate and resistance options `.7.b` and `.7.c` have raw bases `60` and `40` and exclude final actors; the government option `.7.d_option` has raw base `100` and excludes actors. These are source weights, not normalized probabilities. The event itself is triggered by `random_terror_false_revelation_pending`, so this downstream pool is not evidence that Maximum may fire the event before its transaction.

The `random_terror_can_defeat_actor` trigger is a gate, not a weighted selection surface. The scenario-specific terminal outcome is bounded by the explicit `random_terror_false_revelation_denied` objective state, but its timing and success probability are unresolved.

## Scenario completeness

| Scenario | Declared state | Candidate pool and external factors | Baseline classification |
| --- | --- | --- | --- |
| `W01_preterminal_profile5_below1000` | JMX profile 5, all non-Chaos gates satisfied, Chaos `999`, no committed transaction. | State map declares the relevant source variables and flag values. Actor-scope and flag interpretation are unverified by MCP. Focus pool incomplete; decision pool incomplete; event 31.7 is not pending. | Exact source says the normal False Revelation gate blocks on Chaos, while source classification still treats JMX as final. Probability result unresolved. |
| `W02_preterminal_world_end_disabled` | JMX profile 5, Chaos `1000`, all numeric gates satisfied, branch disabled, no transaction. | State map declares the relevant source variables and flag values. Actor-scope and flag interpretation are unverified by MCP. Focus and decision pools incomplete. | Exact source says the normal gate fails on the enable flag, while source classification still treats JMX as final. Probability result unresolved. |
| `W03_preterminal_readiness_missing` | JMX profile 5, Chaos `1000`, all other gates satisfied, readiness `79`, no transaction. | State map declares the relevant source variables and flag values. Actor-scope and flag interpretation are unverified by MCP. Focus and decision pools incomplete. | Exact source says the normal gate fails the readiness threshold of `80`, while source classification still treats JMX as final. Probability result unresolved. |
| `W04_valid_terminal_actor` | JMX profile 5, transaction committed/resolved, terminal/world-end flags active, terminal denial not earned. | State map declares terminal flags and gate values. Exact actor binding and live target validity are unverified. Event option source pool has four entries, but eligible options depend on recipient scope. | Exact source says the final classification is appropriate and ordinary defeat stays gated until terminal objectives set denial and weaken the actor. Probability result unresolved. |
| `W05_ordinary_actor` | Ordinary profile 4 actor, no final/terminal flags, one state, below ordinary defeat thresholds. | State map declares the relevant source values. Complete actor-decision and focus candidate pools were not supplied. | Exact source says profile 4 is not final under this predicate and follows the ordinary defeat branch. Probability result unresolved. |
| `P10_maximum_scenario` | Maximum intensity `4`, JMX profile 5, Final Jihad active, maximum readiness `75`, unity `85`, Chaos `999`, no committed transaction. | Source constants support the intensity and scenario readiness/unity anchors. Actor-scope, post-setup state, and complete focus/decision pools remain unverified by MCP. | Exact source shows the Maximum caller marks JMX final before the normal gate. The source gate still requires Chaos `1000` and readiness `80`; no numerical probability or selection ranking was produced. |

The fixture is a static declared set, not a claim that the adapter accepted or resolved every value. Candidate pools are complete only for the four source-local `chaosx.nr31.7` options. The focus and decision candidate pools are intentionally bounded to named affected consumers and are incomplete for selection races or normalized shares.

## MCP ledger and compare contract

The mandatory first request was `hoi4.probability_inspect` with adapter `national_focus_ai_will_do`, source `{path:"common/national_focus/031_random_terror_focus.txt"}`, and `refresh:true`. It returned a tool error after the server timeout: `timed out awaiting tools/call after 600s`. It produced no artifact, source revision, scenario hash, or candidate-pool evidence.

A narrower retry used the same adapter and exact source plus `candidatePool:["random_terror_lead_the_final_jihad"]`. At interruption it had returned no response. Its transport/server outcome is unverified, not cancelled, and no artifact or revision is claimed.

A narrow `hoi4.probability_inspect` request for `event_option_ai_chance` on `events/031_terrorist_attack.txt` with the four `chaosx.nr31.7` options was also submitted and had returned no response at interruption. Its transport/server outcome is unverified, not cancelled, and no artifact or revision is claimed.

A `hoi4.source_lookup` request for the exact `random_terror_is_final_actor` definition, with `includeReferences:false` and `maxDefinitions:1`, had also returned no response at interruption. Its transport/server outcome is unverified, not cancelled, and no MCP source artifact or revision is claimed.

No `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_render`, or `hoi4.probability_compare` request completed. No numerical probability, score trace, ranking, timing result, sensitivity, rank reversal, comparison ID, or rendered evidence exists. These findings remain unresolved.

Matching structural `hoi4.event_inspect`/`event_render`, `focus_inspect`/`focus_render`, and `decision_inspect` calls were deferred for this interim handoff at the parent's direction to deliver the source-contract baseline before the owner patch. Their structural MCP evidence remains open.

The connected `probability_evaluate` schema exposes `scenarioSet` as `unknown`, so the fixture envelope, actor binding, and flag-valued inputs require live adapter acceptance before their scenario hashes can be treated as analyzer evidence.

For the owner patch's mandatory later comparison, use the exact same scenario fixture and nonempty real source paths. The immutable before paths are `docs\plans\031_random_terror_plans\evidence\terminal_role_before_20261003\common\scripted_triggers\031_random_terror_triggers.txt`, `...\scripted_effects\031_random_terror_effects.txt`, `...\national_focus\031_random_terror_focus.txt`, `...\decisions\031_random_terror_decisions.txt`, and `...\script_constants\031_random_terror_constants.txt`. The matching after paths are the real current paths under `common\scripted_triggers`, `common\scripted_effects`, `common\national_focus`, `common\decisions`, and `common\script_constants`. Do not compare a current source path to itself.

The before-copy SHA-256 values were verified against the supplied identities: triggers `9F565363E15C4F8D9EBE55A29A5F65ACD645EF224920DF9E9888BE6BFDF491C2AE`; effects `0FFB0B284B492AE08213A0E29565ECFB91ED0F2A34F5653736CF97061A224096`; focus `D3082BA4F338E9CF399E8B0EF37FE89BE48F7A402DA3F66F0E516A738254954E`; decisions `FEC966EE89D9E468F46FD049EC67B9272EA0BC9CC2364D15F02CBAFF3C8C5933`; constants `03487126B78BE11CEC5B11BA1C727360C855BC7F8820F2F9A8C5C33D1AF40701`.

Repository `HEAD` was `a8d7e47ed2ff2bc51eea44acb7dd61193ec741b1` when checked. `common\scripted_effects\031_random_terror_effects.txt` was already dirty in the shared worktree; it was not edited by this audit. The other four in-scope live source files were clean in the scoped status check. The parent-reported research-slot correction commit `24c3697126c406541f707f981ab844f98212cf95` does not change the immutable before-copy authority.

## Recommendations for the owner

1. Make terminal identity depend on the committed/resolved False Revelation transaction or an equally specific transaction receipt, not profile 5 alone.
2. Keep the Maximum scenario's Final Jihad activation separate from the False Revelation transaction and do not let the early JMX setup call grant terminal ideas or terminal defeat immunity.
3. Preserve the normal Chaos, readiness, unity, territory, crisis, strategic-victory, branch-enable, and viable-actor gates for False Revelation.
4. Keep terminal defeat objective-based after the actual transaction, and preserve the ordinary defeat branch for preterminal JMX.
5. Review the 16 ordinary actor-decision gates and the `random_terror_lead_the_final_jihad` factor-6 score after the classification repair; the same-scenario probability comparison remains mandatory.

No gameplay or weight changes were applied. Event31 completion, numeric balance, normalized choice probabilities, live AI behavior, full candidate-pool completeness, and post-patch comparison remain open.
