# Council pledge and speech AI/probability baseline

Status: **Partial baseline and bounded AFTER attempt.** The frozen-source inspection and raw fixtures are preserved.
The specialist reported that the final exact-alias comparison ended with `INTERNAL_ERROR` and no live analysis handle.
No effective score, ranking, canonical comparison result or numeric delta is claimed.
The parent completed the evidence disposition below after verifying that no native tool call remained active.

This is a read-only audit of only `gods_of_africa_council_pledge` and `gods_of_africa_council_speech` in Event 012, Decision L27. No gameplay, AI, event, localisation, or runtime source was edited; no game was launched and no Git operation was run.

## Source identity

The parent-provided immutable manifest is `docs\plans\012_africa_plans\subagent_handoffs\012_gods_council_receipts_2026-10-07_evidence\before\manifest.json`. All eight copies match the manifest hashes. The current logical working files now match only one of those eight copies; the other seven have diverged while this branch contains concurrent work. Their authorship and change purpose were not determined, so all baseline source conclusions below use the frozen copies or the probability-inspect revision.

| Frozen source | SHA-256 |
|---|---|
| `common\decisions\012_africa_gods_decisions.txt` | `a37d5bf0b1fcdd7a361f7bb27a9ec9b2bda855f6de944af5f76e3070e03b9c87` |
| `common\scripted_effects\012_africa_gods_focus_payoff_effects.txt` | `d9e2dae689e93c1f5bb24fc723364c397d6b3cb65829b2f0d098e68d6bb30fe4` |
| `common\scripted_triggers\012_africa_gods_focus_payoff_triggers.txt` | `17b96936ea3e49ee6c4ecfbae55edf08f5b7207dd9ee598c614e3421a55a081e` |
| `common\scripted_effects\012_africa_gods_contribution_effects.txt` | `f89f5c6b4214f339dacd717ea3d734aa12e20a681c91dd544cdffa27ac0fe398` |
| `common\scripted_triggers\012_africa_gods_contribution_triggers.txt` | `44ff852c2d71433b38d44a89fc93477981b2f81de311e773df0b9b04e6848a24` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `720f1cb91a1c36e73254954f08b08bd5e2b241770b022d310aaea16b8b6d9332` |
| `localisation\english\012_africa_gods_l_english.yml` | `f81ea6a2059d54766f23c1a316d53525bdf5f73d5d7f6a7d0483695c7c77d2fb` |
| `common\scripted_localisation\012_africa_gods_scripted_localisation.txt` | `67fd4744b911e1b7c38a0c25e4063a1a521f7b6da534dd1519b34a2dd48e4b7b` |

The two decision blocks are in the frozen decision copy at lines 214–249 and 251–286. Their open and affordability helpers are in the frozen payoff trigger copy at lines 46–64; the effects are at lines 55–94 in the frozen payoff effect copy.

The AI tuning constants are outside the supplied eight-file manifest. I captured their source during this baseline in `012_gods_council_probability_2026-10-07_evidence\dependencies_before\common__script_constants__012_africa_gods_constants.txt`, SHA-256 `be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e`. The participant/AI trigger, epoch-binding, host-recovery, and ultimatum trigger sources are also captured under `dependencies_before\`; their hashes are listed in `dependency-snapshots.json`.

The successful inspection bound the logical source path to the frozen copy using `source.path`, `source.snapshotPath`, and `source.expectedSourceHash`. MCP candidate provenance reports the raw decision-copy SHA above. Its separate MCP source hash is `c40c57c82795ff57659ec94481c0bc292e5960317091bbad71d177c7748bbccb`, with source revision `41c98312a4173902c3f3257006b8f70db100551b4a792c5ae839f2409b6e5db4`.

## MCP evidence and result classes

`mcp__hoi4_agent_tools__hoi4_probability_inspect` was the first weighted-surface call. It returned `ok` for adapter `decision_ai_will_do`, discovered the exact two requested candidates, marked that bounded candidate pool complete, and reported zero required input paths and zero unresolved parser items. The linked adapter contract supports raw scores and eligibility, but `normalizedProbability=false`, `timeDistribution=false`, and `selectionRule=score_only`.

The full inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/102ff01287c3552f8b745e78f8aa4c29ac4cec0636b20912295b96221095d736/1e934c599f40264f4d43bfd94b8ce3885f37d9008ab917c505acf95ab1485ce9/probability-inspect-c40c57c82795.json`. Its declared 101,736 bytes were recovered in 17 byte ranges and verified against artifact SHA-256 `102ff01287c3552f8b745e78f8aa4c29ac4cec0636b20912295b96221095d736`. The artifact records game version `Operation Postern v1.19.2.0.a729 (d245)`.

The tool found `gods_of_africa_council_pledge` at frozen lines 214–249 and `gods_of_africa_council_speech` at 251–286. The helper provenance includes `gods_of_africa_council_is_open`, both affordability triggers, participant host/generation checks, epoch binding, and the AI posture triggers. The inspect receipt preserves their paths and hashes.

A valid one-scenario `hoi4.probability_evaluate` request for `COUNCIL_READY` was submitted with the complete two-candidate score pool and the frozen decision binding. It remained pending for about 151 seconds and was stopped without an analysis ID, score trace, artifact, or canonical MCP scenario hash. A valid one-path `hoi4.probability_sweep` request for `scopes.ROOT.state.num_equipment@infantry_equipment` also remained pending for about 151 seconds and was stopped without a threshold, sensitivity, ranking, rank reversal, artifact, or scenario hash.

The two narrow `hoi4.decision_inspect` calls were started with an earlier bounded evaluation request and stopped with that pending cell after about 182 seconds; neither returned a structural artifact. This leaves source review as the only structural evidence for the two exact decision blocks.

The raw nine-case scenario set has file SHA-256 `9bfddaa2d9ec858032a1053846e5bdeac3983e685846441fe0549cf61e09711f`. The MCP canonical scenario hash is **unavailable** because no evaluate or sweep result returned. `COUNCIL_READY` is the only scenario sent to those tools; the other eight are prepared in the fixture but unanalysed.

Classification: the candidate discovery and source provenance are **exact** for the frozen file. The source-defined weight structure is **score-only**. All nine named scenario results, effective score traces, and rankings are **unresolved**. There is no sampled result. No result is a click probability.

The two-candidate pool is complete for these two willingness scores only. It is not the whole country decision race, and the adapter does not normalize an `ai_will_do` score into a selection probability. The offline AI modding reference describes these MTTH-shaped AI weights as score inputs typically compared in a highest-score race, with possible strategy modifiers; event `ai_chance` and `random_list` use probability-proportional sampling instead. These decision weights are not timing distributions. The scenario facts below are synthetic model inputs, not an observed save or live campaign. AI strategy factors outside the two blocks, diplomatic opinion for the friendly modifier, complete African-core state ownership, and runtime event-target state were not established.

| Scenario ID | Prepared model difference | Frozen-source gate fact | MCP result |
|---|---|---|---|
| `COUNCIL_READY` | GER/ETH generation 27 and authority epoch 4; GER has 2,000 infantry equipment and 50 political power. | Baseline state for both decisions. | Unresolved; one valid evaluation request stalled without output. |
| `COUNCIL_ACTIVE_DEMAND` | Adds an active ordinary demand with matching generation and authority epoch. | The frozen Council-open trigger does not test demand state. | Unresolved; prepared, not evaluated. |
| `COUNCIL_NEGOTIATION` | Adds the source-recognized negotiation-open flag. | The frozen Council-open trigger does not test negotiation state. | Unresolved; prepared, not evaluated. |
| `COUNCIL_RECONCILIATION` | Adds pending reconciliation, matching reconciliation identity, and the route’s defiant flag. | The frozen Council-open trigger already rejects a defiant participant; it has no separate reconciliation check. | Unresolved; prepared, not evaluated. |
| `COUNCIL_ULTIMATUM` | Adds a current final ultimatum with a future due day. | The frozen Council-open trigger does not test ultimatum state. | Unresolved; prepared, not evaluated. |
| `COUNCIL_PART_PAID` | GER has 1,400 infantry equipment, leaving 900 above the 500 donor reserve. | The frozen pledge affordability helper requires the full pledge plus reserve; there is no active-pledge progress token in the before source. | Unresolved; prepared stock analogue, not evaluated. |
| `COUNCIL_EMPTY_RETRY` | GER has exactly the 500-equipment reserve. | The frozen pledge affordability helper rejects a pledge with no stock above reserve. | Unresolved; prepared, not evaluated. |
| `COUNCIL_STALE_AUTHORITY` | GER participant generation 26 while ETH host generation remains 27. | The current-generation helper fails, closing the Council gate. | Unresolved; prepared, not evaluated. |
| `COUNCIL_COMPLETE` | GER has the existing Council voice and pledge-complete flags. | The Council-open helper rejects an already-recorded voice. | Unresolved; prepared, not evaluated. |

The complete model fixture is in `012_gods_council_probability_2026-10-07_evidence\scenario-set.json`; the exact narrow evaluate and sweep requests are in `ready-probe-request.json` and `sweep-probe-request.json`. `fixture-notes.md` records the synthetic assumptions and unbound inputs.

## Frozen-source findings

`gods_of_africa_council_is_open` requires an active current host, a current participant generation/epoch, the host’s Final Council focus unlock, no defiance, no committed final outcome, no prior Council voice, and no war with the host. The frozen helper contains no demand-open, negotiation-open, or ultimatum-pending condition. Reconciliation is excluded only when its legitimate defiant state is present.

`gods_of_africa_council_pledge_is_affordable` computes the 1,000-equipment pledge plus the 500 donor reserve and requires that stock to be available. The effect sends a fixed 1,000 infantry equipment to `event_target:africa_host`, then adds the same nominal 1,000 to `africa_common_defence_stockpile` if the variable exists. It records the Council voice and aid history, but does not call the existing measured contribution receipt path.

The frozen contribution package already exposes `gods_of_africa_begin_material_transfer`, `gods_of_africa_record_paid_contribution`, `gods_of_africa_complete_material_transfer`, `gods_of_africa_begin_voluntary_receipt`, and `gods_of_africa_complete_payment_receipt` in `common\scripted_effects\012_africa_gods_contribution_effects.txt`. The receipt completion publishes measured donor delivery and measured host credit, clamping host credit to no more than donor loss. These are concrete integration candidates for the parent; I did not call or modify them.

`gods_of_africa_council_speech_is_affordable` requires 25 political power. The speech effect spends 25, records a Council voice and speaker, applies reciprocal opinion, and updates history. The frozen decision/helper has no guard for a pledge currently underway; successful pledge completion closes the Council through the shared voice flag, but there is no partial-payment lifecycle in the baseline.

The decision weight blocks have source-defined bases of 10 for pledge and 8 for speech. Pledge applies a zero factor when the Council is closed or unaffordable, a factor of 3 for `gods_of_africa_ai_is_loyal_ally`, and 0.1 for `gods_of_africa_ai_is_defiant_rival`. Speech applies a zero factor when closed or unaffordable, a factor of 2 for `gods_of_africa_ai_is_friendly_to_africa`, and 0.1 for a defiant rival. The constants are in the captured `common\script_constants\012_africa_gods_constants.txt` at lines 966–971. These are source values, not MCP-evaluated effective scores.

The loyal/rival/friendly modifiers are independent source modifiers, and the rival and friendly conditions are not structurally exclusive. Their reachable overlap and score impact need the named-case evaluator and sweep; no arithmetic substitute is claimed. The adapter found eligibility and weight blocks for both candidates, so the source does not show a missing or flat `ai_will_do` block or a duplicate candidate in this exact pool.

`fire_only_once = no` is bounded by the Council voice gate after a successful pledge or speech. A guarded no-op that fails before setting voice could remain retryable, but this probability pass did not evaluate effect execution or retry cadence. No dominance, starvation, rank reversal, repetition rate, snowball, or exploit outcome is proven.

## Recommended owner fixes

1. Extend `common\scripted_triggers\012_africa_gods_focus_payoff_triggers.txt::gods_of_africa_council_is_open` to defer Council access while an ordinary demand, negotiation, reconciliation, or final ultimatum is outstanding, with each state bound to the current authority epoch.

2. Replace nominal pledge accounting in `common\scripted_effects\012_africa_gods_focus_payoff_effects.txt::gods_of_africa_council_pledge` with the measured material-transfer/receipt helpers in the frozen contribution package. Count actual donor loss into contribution, voluntary-aid, and campaign history; credit the host reserve only by measured gain; preserve the 500 donor reserve and the 1,000 pledge target.

3. Give partial positive payments a remaining balance and keep the pledge active until the balance reaches zero. Empty or rejected transfers must produce no credit. Set pledge-complete voice/history only on full completion, and preserve already-recorded contribution history when authority loss clears live pledge terms.

4. Add an exact current-pledge-underway guard to the speech availability/effect path so speech cannot pre-empt an active pledge; keep speech’s 25 political-power cost and grant speech credit only after the pledge is fully complete.

5. Leave numeric `ai_will_do` tuning unchanged as directed. After the parent patch, run `hoi4.probability_compare` through this auditor with the same named cases and candidate pool, bound to the immutable before source and the current after source. If the patch introduces a new pledge-progress flag or variable, add that exact source identifier to the shared fixture and rerun the before and after with the same revised fixture hash.

No balance target was selected and no source fix was applied.

## Skipped analyses, blockers, and references

The named-case evaluate and sweep results are blocked by calls that remained pending beyond the bounded wait and returned no analysis artifact. I stopped after the single narrowed evaluate and the single narrow stock sweep; I did not issue further retries.

`hoi4.probability_render` was not called because no successful analysis ID existed. `hoi4.probability_simulate` was not used because no explicitly uncertain-input distribution was declared. `hoi4.probability_sequence` is out of scope because these decisions are not a declared custom weighted pool with cadence and transitions. `hoi4.probability_compare` is deferred until the parent supplies the patch, as requested.

The MCP inspector artifact points to `docs\research\probability-adapter-evidence.md` and `fixtures\probability`; those local repository paths were absent when checked. The live artifact itself supplied the adapter capability contract. The separately read prior defiance confirmation audit was used only for observed scenario-field shape; its scenario values were not reused.

Offline references read: `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:357-374`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md:26-37`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`; and installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.

Skills used: `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, and `.agents\skills\chaos-redux-mtth\SKILL.md`.

The baseline statements above retain their original phase scope.
The subsequent AFTER requests use the implemented progress fields and remain qualified by the disposition below.

## Parent disposition of the bounded AFTER work

The preserved current decision source has SHA-256 `b39073b4370a8f7508ddc7902a6d9f4e5907942375313257fd063268a60fc6e8`.
The final saved request descriptor is `012_gods_council_probability_2026-10-07_evidence/matching-compare-parent-aliases-v2-request.json`, SHA-256 `9a64fa5926757a937170ce4b840d72af08fadc8bd4524dd8dcef9190b2a476d7`.
Its raw fixture is `scenario-set-v2-parent-aliases.json`, SHA-256 `db2e5711432546deddb865f74576fabaddfd2285f205c906ae1d2d9c6444294c`.
The descriptor records both Council candidate IDs, immutable before-decision identity, current after identity, requested outputs and the same fixture on each side.
The fixture is a declared synthetic model, not observed campaign state.
Intermediate v2, bound-v2 and alias-v2 files are retained as provenance, not interchangeable completed analyses.

The original baseline did not bind the event-target alias in the form expected by the inspected decision model.
The parent supplied the exact `event_target:africa_host` and normal-variable aliases for the same declared ETH scope, after a bounded artifact read exposed that missing input.
The specialist incorporated those aliases in the saved final fixture and reported the corresponding comparison's terminal `INTERNAL_ERROR`.
The parent read that status from the owned auditor chat and verified its latest turn had no active MCP or command call before closing the drafting agent.
The error outcome is retained as reported tool evidence; no numeric result or analysis artifact was returned for the final attempt.

Freezing only the decision root is insufficient to establish a complete old environment because `gods_of_africa_council_pledge_is_affordable` and contribution helper dependencies changed.
Before helper copies and hashes are retained, but successful application of a complete frozen-helper overlay by the comparison adapter was not established.
Therefore neither a zero delta nor a clean old-versus-new eligibility comparison follows from these requests.
Remaining binding and native-type limitations must not be replaced with invented country ordinals or forced helper results.

The parent's separate decision inspection with the corrected aliases remained `DECISION_ANALYZED_PARTIAL` and its bounded report still listed existence/capital, authority/origin identity, typed `THIS.id`, exclusion-family and participant-array inputs.
Its false projections are unresolved model outcomes, not proof that the live Council is unavailable.
The exact report URI and limited read coverage are recorded in `012_gods_council_receipts_implementation_2026-10-07.md`.

Separately, `.tools/validation/test_012_gods_council_receipts.js` passed 12 executed production-helper scenarios and one successful-settlement cleanup source assertion.
Those source-model checks inject native stock/send observations and external authority/history/world boundaries; they are not this probability result and do not prove engine behavior.
Native stock movement, complete AI eligibility/willingness, actual row appearance and long-run behavior remain open acceptance boundaries.
No gameplay simplification or balance tuning is authorized by this failed comparison.
