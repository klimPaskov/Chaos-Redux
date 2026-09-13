# Event 021 AI Probability Audit Continuation

Date: 2026-09-13, Europe/Kyiv.

Status: NOT CERTIFIED / INCOMPLETE.

This is an independent, read-only continuation audit. No gameplay file, AI file, event file, source file, workbook, manifest, or runtime file was changed. Hearts of Iron IV was not launched. No commit was created. No balance target was selected.

## Scope and required references

The audit used `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`, `docs/specs/021_random_civil_war_specs/subagent_prompts/chaosx_ai_probability_auditor.md`, `docs/plans/021_random_civil_war_plans/subagent_handoffs/probability_current_2026-09-12.md`, `docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_audit_2026-09-06.md`, and the three files under `docs/plans/021_random_civil_war_plans/probability_snapshots/sponsor_resource_guard_before_2026-09-02/`.

The required offline wiki pages were read from `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The relevant installed vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`, and `script_math_functions.md`, plus `common/script_constants/documentation.md`.

No `.tools/audit_event021*` file exists under `.tools` or its subdirectories. The requested snapshot directory contains only the three sponsor pre-change source snapshots, not a current executable scenario manifest.

## Current source identity

The following SHA-256 values were captured before this handoff was written.

| Surface | Current source | SHA-256 |
|---|---|---|
| Event root | `events/021_random_civil_war.txt` | `78d8eb2bb5e3cbb0a5e113789df73d03690b7fd895d1fe58bda43f8e72e33bd8` |
| Parent lifecycle and weighted dispatch | `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `9273fc5d6e97a88a6b33d8281a837e03ea40b00d95fb4d8b9e6ba6738af168d3` |
| Core target, archetype, severity, recurrence | `common/scripted_effects/021_random_civil_war_effects.txt` | `11df6be36053085e4007c34d02da0b6171f94ddba14108e532c59170ca7322ab` |
| Parent triggers | `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` | `a269db0c87ba4d6baafbc2e55768beef616c0bae570d1502df384a89044130fe` |
| Core triggers | `common/scripted_triggers/021_random_civil_war_triggers.txt` | `c8183e114eb34827745601bd69519a4e4fe44014e12c38a1706ff0136af54a68` |
| Evolution MTTH | `common/mtth/021_random_civil_war_mtth.txt` | `6a8c516e1a2625f3534995f6744ed373e5803ac981fd139ea95787f07b9ea71f` |
| Decisions and missions | `common/decisions/021_random_civil_war_decisions.txt` | `c1b63ae9ba32b7fd1b5d637b6e8686bedd32f105af46cd27912f309acc29ad65` |
| AI strategy | `common/ai_strategy/021_random_civil_war_ai_strategy.txt` | `6adbb93b2cd17665c4bd967368f08bc953738d81db7a2069171241f45c309dca` |
| Constants | `common/script_constants/021_random_civil_war_constants.txt` | `b02ae147ce8ce700792c2b9110d0bf34d5c65d1403ba15f685a968d8c1d09ec1` |
| Event 006 adapter effects | `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` | `cb03b1679380576f69dc6cf569bade109f6c79f8511fcf88c25644f3c1d99fb1` |
| Event 006 adapter triggers | `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt` | `3dde81d9845c74fef57d8d089256a69d682d4a937ce410d19600b34dfadcefc7` |
| Shared provider load | `common/scripted_effects/individual_crisis_targeting_effects.txt` | `903562c1dc27bf9367e5a8ab8a807047a798fb16de0bd8e1df2841f6a2c40b16` |
| Wars cluster | `common/scripted_effects/chaosx_event_cluster_effects.txt` | `cb8b1d2039b947a37185e7fc04da6aa84bd13ef3d647306fdf2a40bc4494fbfe` |
| Scenario registry | `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | `b3aad10569c3d47e40163dfa64a0106859cfb35fc20b32c908df41a042fd3a0f` |

## Fresh probability MCP receipts

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The audit began with `hoi4.probability_inspect` on the current parent weighted source as required.

| Pass | Exact result | Candidate and input result | Artifact or blocker |
|---|---|---|---|
| Parent whole-source `random_list` inspect | `status=ok`, `code=PROBABILITY_SOURCE_INSPECTED` | `poolComplete=false`, `candidates=8`, `availableCandidates=0`, `requiredInputs=8`, `unresolved=1`, `diagnostics=[]`; source revision `062979bb2370063fbcc85fab9f1109905efcad09e7c53b9bfddb576209eb7116`; source hash `bffd0365a31eebc24ba36203f8664a7e97838f9ce2b135c579d1012d5922e5e1` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/222131f5e9b391af09deebc49dc24285b68f880ea731e9d7619511e8ef48a8a0/cabf0b8b2c959cc9fbaca29429e6f36d4e46d0414ddd435152af2b2f79b84335/probability-inspect-bffd0365a31e.json` |
| Parent six-route inspect with unqualified entry ids | `status=ok`, `code=PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=candidate_pool_not_found` | `availableCandidates=8`, `candidates=0`, `requiredInputs=0`, `unresolved=0`; examples identify the actual entries at `1126.entry.1` through `1126.entry.6` and incident entries at `5313.entry.1` and `5313.entry.2` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73c72aa2bdf6a2f047ea2b4622dbcb6ff66405108dd980e0cfa05f2351bfd340/5b51d7247794d73261add01cc2181862f7c6249d5d30a6adb2f8f4cfb18b804a/probability-inspect-bffd0365a31e.json` |
| Parent six-route inspect with source-qualified entries | `status=ok`, `code=PROBABILITY_SOURCE_INSPECTED` | `poolComplete=true`, `candidates=6`, `availableCandidates=0`, `requiredInputs=6`, `unresolved=0`; same source revision `062979bb2370063fbcc85fab9f1109905efcad09e7c53b9bfddb576209eb7116` and source hash `bffd0365a31eebc24ba36203f8664a7e97838f9ce2b135c579d1012d5922e5e1` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60a8e20c2cd1282224c9d6735922a4c32c95a3267ab374e147adbe1a7f84d964/3d6463465c6f497bd6c93da607284aff4d415757dacdea34be5ed3d81f19c6e8/probability-inspect-bffd0365a31e.json` |
| Event 006 adapter registry inspect | `status=ok`, `code=PROBABILITY_SOURCE_INSPECTED` | `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, `unresolved=0`, `diagnostics=[]`; source revision `062979bb2370063fbcc85fab9f1109905efcad09e7c53b9bfddb576209eb7116`; source hash `eb34f0f5ead1b751d595ca2c3eef141084ceb0b0111018768d0db539cba175cb` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/357683eb0faea62489398459a9563baeaf5b614d67544ec728955b51c1023dd1/eabe9c10a3b3c253484a5f4879c502dd7ab79946abd9c519c08dbabc0494c0bb/probability-inspect-eb34f0f5ead1.json` |
| Current target custom-pool inspect | `status=error`, `code=INTERNAL_ERROR` | No files scanned, no candidates, no scenario result | Blocker exactly reported as `Unexpected internal error`; no artifact |
| Current MTTH inspect | `status=error`, `code=INTERNAL_ERROR` | No files scanned, no candidates, no timing result | Blocker exactly reported as `Unexpected internal error`; no artifact |
| Current decision inspect | `status=error`, `code=INTERNAL_ERROR` | No files scanned, no candidates, no score result | Blocker exactly reported as `Unexpected internal error`; no artifact |
| Current event-option inspect | `status=error`, `code=INTERNAL_ERROR` | No files scanned, no candidates, no option result | Blocker exactly reported as `Unexpected internal error`; no artifact |
| Current AI-strategy inspect | `status=error`, `code=INTERNAL_ERROR` | No files scanned, no candidates, no strategy result | Blocker exactly reported as `Unexpected internal error`; no artifact |
| Current scenario-registry inspect | `status=error`, `code=INTERNAL_ERROR` | No files scanned, no candidates, no scenario-share result | Blocker exactly reported as `Unexpected internal error`; no artifact |

The parallel inspection batch returned the same explicit `INTERNAL_ERROR` blocker for the six surfaces above. No further retries were made after the parent requested immediate handoff completion.

No current `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, or `hoi4.probability_render` result is claimed. The current inspect failures, incomplete pools, missing scenario bodies, and missing transition manifest prevent a current exact or bounded matrix pass.

## Structural MCP receipts

The event root is `events/021_random_civil_war.txt:13`, selector `{ kind: event, eventId: chaosx.nr21.1 }`.

The broad `hoi4.event_inspect` `state_flow` pass returned `INTERNAL_ERROR` with no artifact.

The narrow all-four-chain event lint/trace returned `EVENT_INSPECTED_PARTIAL` at focused revision `3ac0bcfca142`, with helper coverage deferred and `counts.helpers=0`; validation was false. The trace artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a608eee7999949d4a07fd8da63b109ba269c66c4a47df474a9c428c072a5104e/0409962f673dfcc71ce9e64483fdadf886394fce07cd4e00fb9c13298f71520d/event-trace-3ac0bcfca142.json`.

The matching narrow render returned `EVENT_RENDERED_PARTIAL` at the same focused revision, with validation false and zero selected nodes despite the source root. The render artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18b16a478622461edd5b9a69c5bdfcff6f4a03b39b705c2e10cae65ef456f880/5fb1cc5ba9d6f1c12f1ef71ad75917ab4860eb46f6bbea5042d4ef49006916ab/event-targets-3ac0bcfca142.json`.

These structural results do not prove helper lifecycle, actor-territory, Event 006 package, or terminal coverage.

## Current source traces and queue findings

Target scoring is source-only at `common/scripted_effects/021_random_civil_war_effects.txt:429-499` and `common/script_constants/021_random_civil_war_constants.txt:232-249`. The trace initializes at `10`, adds `4` per fracture-pressure point, `90` for failing authority, `160` for collapsed authority, `80` for a valid actor route, `50` for a major-stage gate, `60` for nearby exposure, `-120` for recent memory, `20` for subject status, and `25` for the player marker, then applies a `0.35` major-target factor and clamps to `0..1000`. The target pool later divides by `100`, rounds, and caps at `10` in `event021_parent_add_target_to_selection_pool` at `4565-4578`. No complete country candidate pool or typed runtime fixture was available, so these are not selection probabilities.

The current archetype source at `common/scripted_effects/021_random_civil_war_effects.txt:508-539` initializes all six route weights to zero and assigns `80` to each route whose validity trigger is true. `event021_parent_select_archetype` at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1123-1134` samples all six through a `random_list`. The current MCP proves the six source-qualified entries and six required inputs, but no current named ARC evaluation or rank result was obtained.

Severity is a deterministic source ladder at `common/scripted_effects/021_random_civil_war_effects.txt:541-574`: Limited is the default, Serious follows exposed or serious-opening state, Severe requires a permitted major and fractured pressure, Critical requires a permitted major and critical pressure, and the one-state route forces Limited. There is no separate weighted severity pool. Scenario severity certification remains unresolved because the required state fixtures and structural route graph are incomplete.

Evolution MTTH source bases are `90` days for Evolution I, `135` days for Evolution II, and `120` days for Evolution III at `common/mtth/021_random_civil_war_mtth.txt:5-93`. Factors cover authority failure, large country, extra actor, near defeat, settlement progress, border exposure, sponsor commitment, Event 006 front, multi-front state, strong neighbor, no exposure, and severe war. The parent samples once and clamps each due delay to `60..180` days. The current MTTH adapter returned `INTERNAL_ERROR`, so no effective MTTH, timing distribution, threshold, or rank-reversal result is certified.

Neighbor spread is source-only at `event021_parent_propagate_exposure` and `event021_parent_expose_neighbor` at `common/scripted_effects/021_random_civil_war_parent_effects.txt:5203-5284`. It uses immediate neighbors, normal-human and load gates, and assigns major neighbors to the opportunistic sponsor profile, stable non-majors to mediation, and other eligible neighbors to containment. No complete neighbor geometry, sponsor pool, or exposure sequence was supplied.

The strange-incident source at `common/scripted_effects/021_random_civil_war_parent_effects.txt:5290-5324` has source constants `0.08` and `0.92`, requires active Evolution II, an active Event 021 side, no disabled log flag, and no recent incident, then applies a thirty-day exposure cooldown. The parent whole-source inspect exposed the two incident entries only as part of an eight-entry aggregate with one unresolved input. The earlier incident-specific inspect timed out with the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 180s`. The current 8/92 result is therefore source-only, not an exact runtime probability.

The current bounded queue source has a material audit gap. `event021_global_review_batch` at `common/scripted_effects/021_random_civil_war_effects.txt:1271-1279` sets `global.random_civil_war_critical_queue_budget` to `3`. `event021_queue_critical_country` at `1326-1352` decrements that variable on admission while the review batch is active. `event021_launch_critical_country` at `1377-1388` does not decrement it. `event021_finish_global_review_batch` at `1317-1321` resets it to `3` at batch end. The parent scheduler at `common/scripted_effects/021_random_civil_war_parent_effects.txt:351-520` independently caps review scanning at `6` and critical-queue scanning at `3`. `event021_global_review_current_country` at `692-753` also dispatches due registered countries outside the queue launch path.

`random_civil_war_critical_queue_entry_valid` at `common/scripted_triggers/021_random_civil_war_triggers.txt:495-499` delegates normal target validity and launch-lock checks but does not require the Critical pressure band. A queued country can therefore change out of Critical state before launch without a source-level Critical revalidation at the launch boundary. This is a source risk, not an inferred runtime count or probability.

The queue evidence does not establish whether the budget is intended as an admission budget or launch budget, whether launches can exceed the intended per-pulse budget when pre-existing queue entries are present, or how a non-Critical queued entry should transition. GLB-03 and GLB-04 remain unresolved.

The current source also shows the requested fixed-target shared helper remains absent from the executable shared surface. The existing handoff `individual_crisis_fixed_target_contract_2026-09-13.md` records that no declaration, invocation, or shared fixed-target pressure input exists. The release flag is intentionally open in the current test-release source at parent initialization line `27`; this does not certify the probability matrix.

Frozen secondary-front and scenario actor-territory plans were not found in the inspected current source or requested snapshot set. A country-only Maximum scenario pool must not be treated as a complete frozen actor, state, territory, force, collision, and cleanup plan.

## Named matrix coverage

The classifications below use `source-only`, `exact`, `bounded`, `sampled`, `score-only`, and `unresolved` exactly as audit result categories. No current matrix row is certified `exact` or `sampled`.

| Matrix family | Named scenarios | Candidate-pool and external-factor completeness | Current disposition |
|---|---|---|---|
| Target selection | `TGT-01`–`TGT-10` | Incomplete country pool. Pressure, authority, route validity, controlled territory, recent-target memory, active wars, incompatible locks, player/AI state, major stage, shared provider load, and target reservation were not available as one typed runtime fixture. | Source-only score trace; selection probability, dominance, starvation, and rank reversal unresolved. |
| Severity | `SEV-01`–`SEV-06` | No weighted severity pool. Pressure band, major gate, one-state route, external war, authority, and actor/front state are not available through a current evaluator. | Source-only deterministic ladder; scenario certification unresolved. |
| Archetype selection | `ARC-01`–`ARC-08` | Current source-qualified random-list pool is complete for six entries and six inputs, but route flags, Event 006 package identity, actor completeness, same-tag state, and collision state are not supplied for named scenarios. | Exact current pool inventory only; conditional route selection unresolved. Historical 2026-09-12 evaluation is not current certification. |
| Event 006 selection | `ARC-04`, `ARC-08`, `FRT-05` | Current Event 006 adapter inspect returned zero discoverable candidates with `poolComplete=false`; frozen package, secondary actor, and actor-territory planning are absent from the supplied executable manifest. | Event 006 choice and exact-zero behavior unresolved. |
| Front count and actors | `FRT-01`–`FRT-05` | Source caps are visible: baseline fronts `4`, Evolution I `6`, Evolution II `8`, Evolution III `10`, major belligerents `5`, minor belligerents `3`, multi-front states `2..5`, review scan `6`, critical scan `3`. No complete front candidate or transition sequence exists. | Bounded source caps only; front counts, composition, starvation, and collision outcomes unresolved. |
| Evolution timing | `EVO1-01`–`EVO3-02` | MTTH source bases and factors are visible, but current MTTH inspection failed and no complete state transition fixture exists. | Source-only timing design with `60..180` day clamp; effective timing and duplicate-evolution behavior unresolved. |
| Spread and neighbors | `TGT-07`, `EVO2-01`, `EVO2-02`, `SPN-01`–`SPN-05` | Immediate-neighbor traversal is source-visible, but neighbor geometry, sponsor resources, alignment, commitment caps, recognition, mediation, and load state are incomplete. | Source-only neighbor/profile mapping; ranking, spread timing, and sponsor selection unresolved. |
| Strange incidents | `STR-01`–`STR-05` | Two source entries and `0.08/0.92` constants are visible, but the current inspect aggregates them with other random lists and the prior narrow inspect timed out. | Source-only chance declaration; exact incident probability, cooldown, and repetition unresolved. |
| Global review and queue launch | `GLB-01`–`GLB-07` | Persistent registry, review dates, queue contents, queue admission budget, launch budget, critical revalidation, capacity, removal, reset, and terminal state are not supplied as a complete current sequence manifest. | Bounded source structure only; GLB-03/04 and full launch lifecycle unresolved. |
| Recurrence | `REC-01`–`REC-06` | Source computes pressure plus post-war memory `10`, failed settlement `20`, authority-collapse contribution, and settlement relief `-20`, clamps `0..100`, checks threshold `45`, and schedules a minimum review after `60` days with successor grace. No postwar candidate sequence or timing fixture exists. | Score-only/source-only; recurrence timing, repetition, and successor exclusions unresolved. |
| Settlement | `SET-01`–`SET-06` | Source precedence covers Event 006 independence, opposition victory, same-tag leverage/autonomy/coalition/government, partition, merger, and negotiated terms. No complete postwar topology or weighted outcome pool exists. | Source-only deterministic precedence; settlement ranking, timing, and durable outcome frequency unresolved. |
| Sponsor decisions | `SPN-01`–`SPN-05` | Current decision inspect failed with `INTERNAL_ERROR`. Source base action is `1`, major priority is `1.5`, and concession discouragement is `0.75`; action gates require resources and target validity. Decision adapter evidence is score-only, not normalized probability. | Historical score-only comparison retained; current sponsor rank and probability unresolved. |
| Wars cluster | `CLU-01`–`CLU-05` | Event 004, Event 007, and Event 021 membership rows are source-visible, but live member availability, reservations, collision state, cooldown, and cluster candidate pool are incomplete. Current scenario-registry/cluster-adjacent inspect failed with `INTERNAL_ERROR`. | Source-only cluster integration; overlap, skip, reroll, and target-share probability unresolved. |
| Scenario selection | `SCN-01`–`SCN-07` | Source shares are `0.10`, `0.25`, `0.50`, and `1.0` for Low, Medium, High, and Maximum. No complete country, actor, state, territory, force, collision, recovery, or terminal manifest exists. | Source-only share constants; country-only Maximum evidence is not a full scenario plan, and all named scenario selection results remain unresolved. |

## Findings by risk type

Validity: normal-human, terminal-lock, load-cap, route, reservation, Event 006, same-tag, one-state, and target-gate predicates are visible in source. Their combined runtime candidate validity is unresolved because the current target, Event 006, decision, scenario, and shared-load adapters did not provide complete typed fixtures.

Dominance and duplication: all valid archetype routes receive the same `80` source weight. This can be acceptable as an equal conditional route race, but no current scenario evaluation proves that route-specific evidence produces the intended dominance relationships. The historical 2026-09-12 archetype evaluation reported 45 warnings from intentional one-route fixtures and must not be treated as current balance certification.

Starvation: invalid archetype routes are initialized to zero, the target helper fail-closes at zero, and historical GLB-03 admission evidence excluded all candidates at saturated capacity. No current exact pool proves that impossible Event 006, nonhuman, no-route, no-target, or no-capacity choices remain excluded in the complete campaign candidate set.

Rank reversal: the historical archetype sweep reported no rank reversal, and the historical sponsor surrender sweep reported zero observed reversals, but both were tied to older revisions or partial unresolved inputs. No current rank-reversal claim is made.

Repetition and timing: source includes recent-target memory, target cooldown, successor grace, incident cooldown, recurrence windows, and bounded review dates. There is no current sequence evaluation of cadence, reset, recovery, removal, or terminal transitions, so repetition and timing are unresolved.

Exploit and safety risk: the queue budget is decremented on admission but not on launch, the queue validity trigger does not recheck the Critical band, and the parent has a separate due-review dispatch path. These are source-level review findings requiring an owner decision about budget semantics and launch revalidation. They are not a claim of a measured runtime exploit.

Score versus probability: target weights, archetype weights, MTTH modifiers, decision `ai_will_do`, and scenario shares are not interchangeable. Decision values in particular are willingness scores. No current numeric score is presented as a click probability.

## Historical MCP evidence retained without current certification

The following receipts are historical evidence only because their source revisions, manifests, scenario hashes, or current-checkout identities differ from this continuation.

The 2026-09-12 parent-owned archetype inspect reported `status=ok`, `code=PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, six candidates, six required inputs, and zero unresolved at source revision `2c799900fb7ae0d0e45f37fe7dfc7ce2927b547294d57eeca3cd298afe4f94c5` and source hash `ac4d84b98a34cfc4b7cde74ac8849cadc6c30e06f06664ab12c4d1744901c70b`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741705cc7f70606b09a879b65477be222924deecc5cd5e323867548d7b46469b/3162987153d14ef316202d27cc925f56ede734241469e880d56d04bf34e59648/probability-inspect-ffe0c7fe9093.json`.

Its named evaluation `event021_archetype_current_complete_2026_09_12` returned analysis `probability-53cc39be84893b94175e5eed`, 48 candidate rows, zero unresolved inputs, validation passed, and 45 warnings. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d24e9a7b1b18d4d42e659f175d75d40050cf8a25aa1d88f84286d2f816de5cbe/6e05222b99140abe8f2010f588e4a966a752854a9f474b068ddfacfd1713656a/probability-53cc39be84893b94175e5eed.json`.

Its named sweep `event021_archetype_sweep_2026_09_12` returned analysis `probability-b2ea2bbce037cf44d49864b7`, 16 points, zero unresolved inputs, and no reported rank reversal. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e304bc2156238b0e7de9ce81f5c1d1262b29db5192f0148acd8adc52e928c324/2bbd1beea2dfc77074284a8cec63e332dee225e703b851dd8472cd5ec07e23f8/probability-b2ea2bbce037cf44d49864b7.json`.

Its seeded simulation `event021_archetype_simulation_2026_09_12` used seed `21021`, `2000` samples, and a `180` day horizon. Analysis: `probability-33fff2831771945b5f7757fc`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50958d46e6bebc3c511a70bbf15c886d0cf448e8bffe4ac3a397121e70ab0bfa/793c0594670402e4efd943840482fa3037682e84961e8b6f843bd8b4068c27ce/probability-33fff2831771945b5f7757fc.json`.

The 2026-09-12 sponsor comparison reported a complete three-candidate score-only pool at old source revision `a6e750bba8366c9665e9863cec65323e0af02bbd39e46ab742f3823d6278eb87` and old source hash `ffe0c7fe9093ea2e125ea0ef6eaac03cf66e91395d057cd5682e694233e6f89a`. Analysis: `probability-245b599b71315c1bb338e11a`. It reported 15 rows, zero unresolved, zero diagnostics, and five changes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c1d669058245dc4652b7229bc34783aaaa2b7b79127f67226d854b5c8447f56/9354dafbb14c11695a33c4f3fb977d084135ca1b99618db2ae743fc0b8238380/probability-245b599b71315c1bb338e11a.json`.

The historical sponsor raw score observations were SPN-01 government support `1.6875`, mediation `0.75`, opposition `0`; SPN-02 all zero; SPN-03 government and opposition `1.6875` tied with mediation `0.75`; SPN-04 mediation `1` with support rows zero; and SPN-05 mediation `1.5` with support rows hard-zeroed. These were score-only observations, not action probabilities. The historical sponsor scenario hashes were `07c2af48de65561b2ab83dffa776a1c0ff70f36780b6a6158b96daa609e021d3` for the five-row evaluation and `08d00630206417d93ffd8dc60285334cb2b4a5d06a1e1fe2e20c2a91316b3155` for its sweep.

Historical sponsor renders include the ranking artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2eb8792b2d835cdd300e25962188fa42bb5a4838a0189c2bf15c23b17e84392d/e27d6b7466b44a0ec0153cfd41f7211a745ae764e9b434951a4e14b755b8f427/probability-probability-4e1958dacabd56d2217cd407-ranking.svg`, matrix artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/833b55fc1353107167d56f011d9d8e322bbd5a425427eec98e1c024e8ae07e16/4e4894a2cc3c3020c592272eec6d7788b0cfb05de3dd475bb9a638865eacef27/probability-probability-4e1958dacabd56d2217cd407-matrix.svg`, waterfall artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc70c27c59156136434045e0a2b14e0e8ed0aa27c7a1f154bf5efc9738051335/3f77c63c5e919767ef1969b569e314207def715c73324a60cf208c72f954c747/probability-probability-4e1958dacabd56d2217cd407-waterfall.svg`, and unresolved artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/107cb06cec462704c6605621a1769dd55dfc3ef1a5cf4b6b942e1ae8c6dcc0fe/0fdee13f0e7de194776d819fd9cb30df56734d4f3fa9cb359698906d3374a3ac/probability-probability-4e1958dacabd56d2217cd407-unresolved.svg`.

Historical scheduler admission receipts were bounded and no-transition only. GLB-01 reported exact next-selection values `0.50` normal, `0.25` Critical, and `0.25` nested at artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fb1f31d9c4c9cccf674881c7f6fca96ca907df34e98867b3395a9314cf4df2e/c28316200889992182aedf2b5174c487ffdcf09e4103fa4b3c6044caefe5f4ba/probability-e92c6847cbe87f754b5dbe5a.json`. GLB-02 excluded Critical at the front-cap boundary and reported `2/3` normal versus `1/3` nested at artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b90da3712d8fb7c1642f596def1664afc361425dedd80dad6bc00308ca4bebf/1031da3cf759eaac00ca1563832951e6ac9932abf33a4d400855fcb6c591b99c/probability-6ba0dc4de1d04f0e56e28a73.json`. GLB-03 excluded all candidates at saturated capacity at artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80fcf04ec3a04dccaa6bc3fd86649beb3372602a0e4b471e0b21794c1dc5563b/a5a46b3956c7bd7a95b12f0e4f28cd398a3bf003de35c80f75caa308b77d7cba/probability-833e70aaf8cedd0b34d2e63a.json`.

Those scheduler manifests did not prove selected-target transitions, launch budget consumption, non-Critical queue behavior, recurrence, settlement, cleanup, or gameplay effects. They cannot override the current source findings above.

The 2026-09-06 independent audit recorded the earlier whole-source parent inspect as `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=false`, eight candidates, eight required inputs, one unresolved, source revision `345d...`, source hash `f38a...`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2e17e090686661ddaecc6f7d7cfce76fa2513e411a5bb58a99434ed406b5b0c/ed022d3115c7cb7f59b2a25311e30b869ca9183b85f05deb641df54d57a19b5c/probability-inspect-f38a5c004f35.json`. Its target custom-pool inspect found zero candidates with `poolComplete=false`, and its shared individual-crisis and narrow strange-incident calls timed out with the exact 180-second `timed out awaiting tools/call` error recorded above. Its MTTH and AI strategy discovery calls returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, no candidates, and no artifacts suitable for a current certificate.

The synthetic target formula recovery remains historical only. It used scenario hash `642f4c730dff64583cd284e89d25d60c80360120d124c18f941a16c3e6ffe419`, analysis `probability-07001ea34f50e09e19322ee7`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb036b6ba615aa3aa97b5fdb36765d1e1ec311b167c70f2ed7825575b15c2c64/e72f0d694aaba8822fa44ec14b581cfa09f6c009d5568f2cd86fa16a3fe53f7e/probability-07001ea34f50e09e19322ee7.json`. It is a formula probe, not the Event 021 country pool.

## Recommendations without applying them

1. Provide a current, complete source-qualified country target manifest and typed fixtures for `TGT-01` through `TGT-10`, including every eligible and ineligible country, route gate, target reservation, cooldown, shared provider load, actor route, and external factor.
2. Provide a complete Event 006 package manifest with selected actor, secondary actor, states, territory, capital, force, collision, cleanup, and exact-zero cases before certifying `ARC-04`, `ARC-08`, or `FRT-05`.
3. Resolve queue semantics explicitly. Either make the variable an admission budget and document that boundary, or add a dedicated launch budget with launch-side consumption. Require Critical-band revalidation at launch and demonstrate the interaction with the separate due-review dispatch path.
4. Supply complete MTTH, neighbor, sponsor, recurrence, settlement, cluster, and scenario transition manifests before using evaluate, sweep, simulate, sequence, compare, or render for current certification.
5. Repeat the historical named scenario sets on the current revision and preserve scenario bodies, scenario hashes, analysis IDs, source revisions, comparison IDs, and rendered unresolved views.
6. Keep the test-release flag and catalog acceptance boundary separate. An open test-release flag is not probability, lifecycle, or live-campaign certification.

## Skipped analyses and remaining blockers

Current evaluate and sweep were skipped because the current target, MTTH, decision, event-option, AI-strategy, and scenario-registry inspections either returned `INTERNAL_ERROR` or lacked a complete typed candidate pool. Current compare was skipped because the current scenario bodies and a stable current before/after manifest were not available. Current simulation was skipped because no uncertain input distribution and seed contract was declared. Current sequence was skipped because no complete custom pool with cadence, cooldown, recovery, cap, removal, reset, transition, and terminal-state definitions was available. Current probability rendering was skipped because no current analysis ID was produced.

The required current Event 021 probability certificate therefore remains blocked by incomplete candidate pools, unavailable adapter responses, absent frozen actor-territory plans, incomplete lifecycle transitions, and partial structural graph coverage. Historical artifacts are preserved above for parent review but do not close any current matrix gap.

Skills applied: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-event-planning`. No skill was created or updated.

This handoff is the only file written by this audit.
