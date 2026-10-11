# Event 23 ultimatum response probability retry, 2026-10-07

Disposition: unresolved. This is a read-only audit of the nine-option AI response pool in `events/023_soviet_nukes.txt`, parent event `chaosx.nr23.120`. Source identities and the option pool are verified. The required probability and structural MCP calls timed out without analysis artifacts, scenario hashes, source revisions, rankings, or renders, so no conditional probabilities or numeric before/after delta are claimed.

The only file written by this audit is this handoff. No gameplay, AI, balance, asset, workbook, skill, or Git changes were made. No game or desktop was launched and no logs were requested or searched. The shared worktree contains unrelated existing changes, which were preserved.

## Scope and source identity

The source event is a triggered-only country event with `id = chaosx.nr23.120` and event trigger `has_country_flag = sov_nuclear_bombs_ultimatum_pending` (`events/023_soviet_nukes.txt:577-582` in the final snapshot). The audit does not cover other Event 23 pools, the parent-owned native missile delivery contract, the other Event 23 systems, or player click behavior.

The repository `HEAD` during this retry was `b9e4e75401e203640ff289f847ec273f45c9f5fb`, later than the parent source commit `81be51988219740937d49a780b0a2f2c641f2539`. The target file was clean in the worktree, its SHA-256 was `f8c2bc971a688b64040dd71bbe047bce73f85d5d20228412fe14d7db6bade2e4`, and its Git blob matched the parent commit and final snapshot.

| Identity | Exact source | Size | SHA-256 | Git blob check |
| --- | --- | ---: | --- | --- |
| Before snapshot | `docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/before_2026-10-06_head_7fdcad9/023_soviet_nukes.txt` | 63,420 bytes | `48b84c4c2177219c1adc746eb0b9fce57760367ef6b928f2cbb7d20135f7247b` | Equals `7fdcad959192ada4d34f8cd28d19c0f98b0989a1:events/023_soviet_nukes.txt` blob `cea3cc7bb97bc761d33786820065aefa84867c7d` |
| Final after snapshot | `docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/after_2026-10-06_final_freeze_7fdcad9/023_soviet_nukes.txt` | 64,737 bytes | `f8c2bc971a688b64040dd71bbe047bce73f85d5d20228412fe14d7db6bade2e4` | Equals parent commit and worktree blob `fd745638b7bdae2152978418106877aeaf063853` |
| Parent source manifest | `docs/plans/023_sov_nuclear_bombs_plans/final_source_hashes_20261006.json` | 2,829 bytes | `d052e030e20af08e26f1f6d3fad41b90879570ca371e13779dc67e382f4b8581` | Manifest file identity only |

The matching snapshots contain the same nine parent-qualified option identifiers: `chaosx.nr23.120.a`, `.b`, `.c`, `.refuse`, `.e`, `.f`, `.g`, `.h`, and `.i`. The candidate pool passed to every probability call contained all nine. The before and after event blocks were compared locally in memory. Their only text difference inside `chaosx.nr23.120` is the added missile-backed acceptance modifier on `.a`.

The current `HEAD` being later than the parent source commit does not invalidate this event-file comparison: its current bytes match the named final snapshot and the event-file blob in `81be519…`. It does mean the audit identifies the event file by its verified bytes, not by claiming that the whole current worktree equals that parent commit.

## Named scenarios and completeness

The retained scenario-set ID is `P23_COERCE_MISSILE_ABSENT_PRESENT`, with `P23_COERCE_ISOLATED_LOSING_MINOR_MISSILE_ABSENT` and `P23_COERCE_ISOLATED_LOSING_MINOR_MISSILE_PRESENT`. The prior handoff records that the corrected schema input used empty state objects. No serialized fixture file for these IDs was found in the Event 23 plan tree. This retry therefore reused the two names with `state: {}` and introduced no actor, target, date, flags, variables, scopes, controller, event targets, or candidate overrides.

| Input | Declared in the scenario names | Supplied or observed in the retry | Completeness |
| --- | --- | --- | --- |
| Missile backing | Absent and present cases are named | Neither the backing trigger nor its underlying state was supplied or observed | Unresolved |
| Coercion actor | Prior handoff describes SOV as the intended actor | No actor scope or actor state in the retry payload | Unresolved |
| Target government and state | The names describe an isolated losing minor | No target tag, state ID, owner/controller binding, or state values | Unresolved |
| Ultimatum state | Valid pending ultimatum implied by the scenario intent | No pending flag, actor event target, demand, demand type, or public-knowledge state | Unresolved |
| War and protection | Losing, isolation, and guarantee factors are implied by the names | No war result, faction, protection, target nuclear capability, or foreign guarantor state | Unresolved |
| Soviet credibility and command | Needed by several source modifiers | No credibility, arsenal proof/use, readiness, integrity, route, or threat state | Unresolved |
| Candidate identifiers | All nine options listed above | Complete at the source-identifier level on both snapshot sides | Exact source pool, scenario eligibility unresolved |

The case names alone do not establish that the conditions they describe were present. The source gates make the eligible subset scenario-dependent. No returned MCP result reports `poolComplete`, eligible count, unresolved input paths, or the effective source graph.

## Source bases, gates, and modifier traces

The response bases in `common/script_constants/023_sov_nuclear_bombs_constants.txt:sov_nuclear_bombs_response_ai` are identical in the before and final snapshots. Every option has an explicit `ai_chance` base. These are source weights, not a ranking or normalized share.

| Option | Base | Eligibility gate in `events/023_soviet_nukes.txt` | Conditional modifier constants and factors |
| --- | ---: | --- | --- |
| `.a` accept | 35 | `sov_nuclear_bombs_event_target_response_is_valid = yes` | `missile_compliance` 1.25 in the after source only; `credible_accept` 1.50; `doubted_accept` 0.50; `unproven_accept` 0.50; `employed_accept` 1.30; `losing_accept` 1.50; `collapsing_accept` 1.50; `winning_accept` 0.50; `no_war_accept` 0.70; `isolated_accept` 1.30; `protected_accept` 0.30; `nuclear_accept` 0.40; `fragile_accept` 1.20; `limited_demand_accept` 1.20; `raised_demand_accept` 0.60; `maximum_demand_accept` 0.60; `narrowed_demand_accept` 1.30; `protection_demand_accept` 0.50; `surrender_without_collapse_accept` 0.02; `low_readiness_accept` 0.70; `low_integrity_accept` 0.70; `unreachable_accept` 0.60; `empty_threats_accept` 0.50 |
| `.b` partial settlement | 25 | Valid response and target demand greater than the minimum | `credible_partial` 1.20; `losing_partial` 1.30; `collapsing_partial` 1.30; `protected_partial` 0.60; `signalled_partial` 1.30; `surrender_without_collapse_partial` 0.50 |
| `.c` delay | 20 | Valid response and `sov_nuclear_bombs_response_delayed` unset | `doubted_delay` 1.30; `unproven_delay` 2.00; `collapsing_delay` 0.70 |
| `.refuse` refusal | 20 | Valid response | `credible_refuse` 0.70; `doubted_refuse` 1.60; `unproven_refuse` 1.20; `losing_refuse` 0.60; `collapsing_refuse` 0.60; `winning_refuse` 1.50; `no_war_refuse` 1.30; `protected_refuse` 1.50; `nuclear_refuse` 1.30; `raised_demand_refuse` 1.30; `low_readiness_refuse` 1.20; `unreachable_refuse` 1.40; `empty_threats_refuse` 2.00 |
| `.e` expose the threat | 10 | Valid response | `unproven_expose` 1.30; `protected_expose` 1.50; `empty_threats_expose` 1.50 |
| `.f` seek foreign support | 10 | `sov_nuclear_bombs_event_target_has_valid_foreign_support = yes` | `isolated_support` 0.40; `protected_support` 2.00 |
| `.g` evacuate | 12 | Valid response and the saved coercion state is owned or controlled by the recipient | `credible_evacuate` 1.30; `nuclear_evacuate` 1.30 |
| `.h` retaliate | 8 | Valid response and the target has nuclear capability | `credible_retaliate` 1.50 |
| `.i` sabotage | 10 | Valid response, coercion actor target exists, and target is at war with that actor | `low_integrity_sabotage` 1.50; `collapsing_sabotage` 0.70 |

The base values and modifier values above are exact source constants. Whether each modifier applies, the effective raw weight, the eligible pool, the ranking, and any conditional share are unresolved because the scenario states and MCP traces did not return. Duplicate base values occur for semantically distinct options. No duplicate candidate ID, missing base, inline unbounded value, or zero base was found in the nine-option source pool.

The `missile_compliance = 1.25` factor is attached only to `.a` and only when `sov_nuclear_bombs_event_response_has_missile_backing` is true. That after-only trigger requires the coercion actor target and `sov_nuclear_bombs_event_has_missile_delivery_capability`. Its listed conditions are active special warheads, operational nuclear integration, a nuclear payload candidate, an active site, and operational reserve, launch readiness, and command control at their `missiles_tuning` minimums (`common/scripted_triggers/023_sov_nuclear_bombs_closure_triggers.txt:3-15`). The threshold definitions are in `common/script_constants/032_missiles_constants.txt`; the missile trigger definitions are in `common/scripted_triggers/032_missiles_triggers.txt`. Those missile-system files are outside the frozen Event 23 source set and were not bound to the MCP comparison.

The valid-response helper requires an existing non-Soviet, non-subject, non-capitulated recipient with the pending flag and a live coercion-actor event target (`common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:384-391`). Foreign support additionally depends on a valid faction backer or an available foreign guarantor (`:398-404`). The actual target identity, state, flags, variables, and candidate eligibility were not present in the scenario payload.

## Before/after and helper-graph coverage

The final `chaosx.nr23.120` event block is one line longer than the baseline block because it adds `.a`'s missile compliance factor. The other eight option blocks and all nine option identifiers are unchanged between the frozen event files. The `sov_nuclear_bombs_response_ai` base and modifier block is text-identical in the two snapshots. The after-only factor constant is `common/script_constants/023_sov_nuclear_bombs_closure_constants.txt:sov_nuclear_bombs_closure_factor.missile_compliance = 1.25`.

The probability comparison request bound `events/023_soviet_nukes.txt` to each snapshot using the logical engine path, `snapshotPath`, and the verified copied-byte `expectedSourceHash`. It did not separately bind the helper files. No tool result reported `filesScanned` or source-graph coverage, so it is unknown whether the analyzer resolved helper references from the corresponding frozen snapshots or from the current workspace.

| Relevant dependency | Before snapshot identity | Final snapshot identity | Comparison coverage |
| --- | --- | --- | --- |
| `common/script_constants/023_sov_nuclear_bombs_constants.txt` | SHA-256 `d5a13b184180a0e8c7f854d4a4ce38b6e0a174e5ef79b7b9647d9e46caf55511` | SHA-256 `8cb396f28e2c5dd7a73743636649173bb65f9b65234c3f48d8a9a1ad1a392ec3` | The relevant response block was read on both sides and is identical. The files were not separately bound in MCP. |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` | SHA-256 `47c938477b3073f027f0ba67b2f587e4269d111d53c79b3c4a33fd546a0916e5` | SHA-256 `32cef7b459648db778113971f97cfa0584e33ac8a536d79fc1f6e7dd46bbeb9b` | The helper file revisions differ and were not separately bound in MCP. Their event-response inputs remain unresolved. |
| `common/script_constants/023_sov_nuclear_bombs_closure_constants.txt` | Absent | SHA-256 `459c0cc645be7118bccb27b42de61b9dbbe3004b855bcd2c91d3593335823c66` | Contains the new factor. It was not separately bound in MCP. |
| `common/scripted_triggers/023_sov_nuclear_bombs_closure_triggers.txt` | Absent | SHA-256 `021ece8c9838ec2b4f115b258c5ab5c7d8086952c546eeb12e8487379f37af91` | Contains the missile-backing predicate. It was not separately bound in MCP. |
| `common/scripted_triggers/032_missiles_triggers.txt` and `common/script_constants/032_missiles_constants.txt` | Not included in the named Event 23 snapshots | Not included in the named Event 23 snapshots | Their state and threshold dependencies are not snapshot-bound or MCP-verified in this comparison. |

## MCP attempts and artifacts

The required adapter calls used workspace `mod_chaos_redux_ea3b2d67c2c0`. An initial `probability_inspect` schema probe using `source: { relativePath: ... }` was rejected with `Unrecognized key: "relativePath" at source`. A probe without a source was rejected with `An adapter requires a source`. The corrected calls used `source: { path: ... }` as documented in the current repository skill. The source-shape errors were corrected and are not the blocker.

| Tool | Request | Returned evidence |
| --- | --- | --- |
| `hoi4.probability_inspect` | `event_option_ai_chance`, `source.path = events/023_soviet_nukes.txt`, all nine options, `refresh = true`, explicit workspace | Timed out awaiting `tools/call` after 600 seconds. No artifact URI, source revision, candidate coverage, or unresolved-input report returned. |
| `hoi4.probability_evaluate` | Final snapshot path and expected hash, both named scenarios with empty state objects, all nine options, `raw_value` and `conditional_probability`, ranking/matrix/waterfall/unresolved outputs | Timed out awaiting `tools/call` after 600 seconds. No analysis ID, scenario hash, trace, ranking, probability, or artifact URI returned. |
| `hoi4.probability_sweep` | Same source and scenarios, path `sov_nuclear_bombs_closure_factor.missile_compliance`, five steps, pairwise and rank-reversal request | Timed out awaiting `tools/call` after 600 seconds. No sensitivity, threshold, rank reversal, analysis ID, scenario hash, or artifact URI returned. |
| `hoi4.probability_compare` | Before and final snapshot paths with their exact `expectedSourceHash` values, the complete nine-option pool, the same two scenario IDs, `refresh = true` | Timed out awaiting `tools/call` after 600 seconds. No comparison ID, scenario hash, source coverage, numeric delta, or artifact URI returned. |
| `hoi4.event_inspect` | `mode = trace`, selector `{ kind: event, eventId: chaosx.nr23.120 }`, depth 1, explicit workspace | Timed out awaiting `tools/call` after 600 seconds. No structural artifact, source revision, or coverage report returned. |
| `hoi4.event_render` | `view = options`, the same event selector, depth 1, explicit workspace | Timed out awaiting `tools/call` after 600 seconds. No render URI or structural evidence returned. |
| `hoi4.probability_render` | Not called | No `analysisId` or comparison handle was returned by the required analysis tools, so the render schema had no valid target. No ranking, matrix, sensitivity, comparison, or unresolved render is available. |

The completed tool calls were polled to their terminal timeout responses. They exposed no live analysis or job handle to re-poll. The earlier 2026-10-06 handoff also records no comparison ID or artifact URI for this pool. No tool was restarted solely because of an expired observation. The exact tool timeout is the blocker for every numerical conclusion.

## Findings and classification

- Exact source finding: the event defines the complete nine-option source pool and every option has a finite constant base. The accept option alone gains the after-only conditional `missile_compliance` factor of 1.25.
- Exact source finding: `.b`, `.c`, `.f`, `.g`, `.h`, and `.i` have additional gates. The valid-response predicate also gates `.a`, `.refuse`, and `.e`. These source triggers define scenario-dependent eligibility.
- Bounded source finding: `.c` sets `sov_nuclear_bombs_response_delayed` and is unavailable while that flag is set. This bounds repeated delay selection at the option gate. Outcome cleanup, event delivery, and the wider ultimatum lifecycle are outside this pool audit.
- Unresolved: effective raw weights, eligible candidate counts per case, rank order, dominance, starvation, rank reversal, conditional selection probabilities, repetition frequency, and exploit or snowball risk. These require complete actor/target state and MCP traces.
- No sampled result: no uncertain-input distribution or seed was declared, and `probability_simulate` was not used.
- No sequence result: this is a native event-option pool, not a declared custom pool with cadence, recovery, caps, cooldowns, removals, resets, and terminal states. `probability_sequence` was not applicable.
- No timing result: the scope is the `.120` event-option pool, not Event 23 MTTH. The delay option references the existing `sov_nuclear_bombs_duration.ultimatum_response` constant, but this audit did not evaluate its timing distribution.

The offline AI modding and Event modding wiki sections describe event `ai_chance` as proportional selection among options, with the `trigger` determining option availability. They distinguish this from `ai_will_do` score races. The offline event page also describes d100 quantization. The installed `documentation/effects_documentation.md` documents `random_list` as a separate weighted effect, not event-option `ai_chance`. These references support the terminology distinction only. They do not fill the missing scenario state or prove this event's normalized outcomes.

The offline reference identities are `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`, lines 26-37, SHA-256 `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`; `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 151-179, SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`; and `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, random-list table line 894 and example lines 1052-1062, SHA-256 `18ef5249e4991f5427eca9ec4f2a66dd47f51e26a491c730adc622f1f5db1b49`. The installed vanilla reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 5413-5433, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. No web sources were used.

## Recommendations without source edits

1. Do not change a response weight from this retry. The only directly scoped tuning key introduced between the event snapshots is `common/script_constants/023_sov_nuclear_bombs_closure_constants.txt:sov_nuclear_bombs_closure_factor.missile_compliance`. No target value is selected.
2. Retain complete named fixtures for both scenario IDs, including the actual SOV actor, recipient tag and state, pending-event and actor-target bindings, demand and credibility state, war result, target protection and nuclear state, foreign support/guarantor eligibility, and observed missile-backing state. Do not infer those values from the scenario names.
3. Before another comparison, use a schema-supported way to bind the matching before/after helper sources by logical engine path and copied-byte hash, including the Event 23 event triggers and constants. State explicitly whether the external `032_missiles` trigger and constants files are also frozen. If the adapter cannot isolate that graph, keep the numeric comparison unresolved.
4. If a complete comparison later supports a tuning change, send the same named cases and all nine candidates through the owner-applied patch and mandatory post-patch `probability_compare`. The parent retains the native delivery-contract review.

No recommendation is made about the user's stated Event 23 grant tiers of 100/175/275/400/600 or timing values of 120/120/180/90. They were not changed or audited here. No new clusters, scenarios, world-end rows, GUI, tags, focuses, portraits, flags, units, models, counters, or animation were created. The full Event 23 goal remains incomplete until the parent-owned native review and required MCP evidence are complete.

Skills read and applied: `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md`. No skill was edited.
