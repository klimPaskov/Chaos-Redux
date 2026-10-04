# Event 029 AI probability audit

## Audit status

Status: partial and unresolved. The connected HOI4 probability calls did not return a tool payload, so no scenario was evaluated, swept, rendered, simulated, sequenced, or compared. This handoff is not a balance signoff and does not claim completion.

The audit started with probability_inspect as required. Local source review supplies source identities and structural findings only. It does not replace the MCP probability evidence or establish score rankings, selection probabilities, or timing distributions.

Only this report was written by the auditor. No gameplay, AI, event, decision, mission, effect, trigger, constant, localisation, catalog, or runtime file was edited. HOI4 was not launched and logs were not searched. No commit was made.

## MCP calls and evidence state

The enabled tool metadata exposed probability_inspect, probability_evaluate, probability_sweep, probability_simulate, probability_sequence, probability_render, probability_compare, reference_context, event_inspect, event_render, and decision_inspect. Schema exposure did not confirm service health. No HOI4 agent-tools health/status route was exposed.

| Call | Exact request | Handle and elapsed result | Evidence returned |
| --- | --- | --- | --- |
| First weighted call | mcp__hoi4_agent_tools__hoi4_probability_inspect with source { path: events/029_riches_found.txt } and refresh true | functions.exec cell 33 remained running through repeated waits and was terminated by the auditor after about 124 seconds | No payload, service error, artifact URI, analysis ID, revision, or scenario hash |
| Focused decision inspect | mcp__hoi4_agent_tools__hoi4_probability_inspect with adapter decision_ai_will_do and source { path: common/decisions/029_riches_found_decisions.txt } | functions.exec cell 35 remained running through repeated waits and was terminated by the auditor after about 94 seconds | No payload, service error, artifact URI, analysis ID, revision, or scenario hash |
| Documentation context | mcp__hoi4_agent_tools__hoi4_reference_context with surface decision, limit 8, and a request for offline decision/AI weight semantics and citations | functions.exec cell 38 had entered a running state after 31.1 seconds; the user interrupted the subsequent wait after 13.6 seconds | No payload, service error, citation, source revision, or artifact URI; final request state is unknown |

These are pending/interrupted calls, not confirmed route failures. The exact stopping points are retained above. The user later directed the audit not to restart unchanged requests or wait on another long route.

No probability_evaluate, probability_sweep, probability_simulate, probability_sequence, probability_render, or probability_compare call was made. The required probability_inspect response was not available to define analyzer-accepted fixtures, candidate pools, analysis IDs, or scenario hashes. No hand arithmetic was used to substitute for the MCP results.

The structural event routes and decision inspection route were exposed but not called after the probability and documentation calls remained pending and the user requested a prompt partial handoff. Their evidence is unresolved. Offline wiki and installed vanilla documentation citations were not returned, so documentation coverage is also unresolved.

No MCP artifact URI, artifact revision, source revision, analysis ID, comparison ID, scenario hash, rendered evidence URI, workspace ID, complete flag, poolComplete flag, or tool-level final error was returned in this audit.

## Current repository state and source identities

The authoritative checkout was the current worktree. Git HEAD was observed as 5cb073ae0f4471f4a3330f8cdebb6d0b62a5c876 early in the audit and as de1ae251d69d94a61e442b6067ea23f3b39f2629 during the later hash capture. The worktree was changing during the audit. The final hashes below bind the source bytes at that capture, not an MCP source revision.

At the last scoped status check, common/scripted_effects/029_riches_found_effects.txt, common/scripted_effects/029_riches_found_incident_effects.txt, and common/achievements/chaos_redux_achievements.txt had concurrent modifications. The before-snapshot directory was untracked in Git. These files and snapshots were preserved.

| Current source | Current SHA-256 | Immutable before snapshot | Before SHA-256 | Byte identity |
| --- | --- | --- | --- | --- |
| events/029_riches_found.txt | 618F87C3BF88F6791AD6785ED73FAF1C4D6D49332BEE47B3B078C476CB8604E4 | docs/plans/029_riches_found_plans/evidence/2026_10_03_before/events__029_riches_found.txt | 618F87C3BF88F6791AD6785ED73FAF1C4D6D49332BEE47B3B078C476CB8604E4 | Same |
| common/mtth/029_riches_found_mtth.txt | 32C989917B468B76C5A6A98A4190B0D490C38651F1BE429EADD667B2927ACB5F | docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__mtth__029_riches_found_mtth.txt | 32C989917B468B76C5A6A98A4190B0D490C38651F1BE429EADD667B2927ACB5F | Same |
| common/decisions/029_riches_found_decisions.txt | 1A485534B48A59D780A53C09642E4618659C69F8FCEDDA9F735CCA412F886A14 | docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__decisions__029_riches_found_decisions.txt | 1A485534B48A59D780A53C09642E4618659C69F8FCEDDA9F735CCA412F886A14 | Same |
| common/scripted_effects/029_riches_found_effects.txt | 1BC4A8AC4C8CF512BA5C5FD91421D7545D67F0CCD91E1D9C7C2EC67B4AE522DD | docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__scripted_effects__029_riches_found_effects.txt | A991DDE1DB89165CED86DBF714228975113D012163D073723C898873941E987C | Different |
| common/scripted_effects/029_riches_found_incident_effects.txt | 521CE7E756A352F2A6D24496B4BBCAF9D582F15EBB3A79C6219D03FF73498CAD | docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__scripted_effects__029_riches_found_incident_effects.txt | 01648014F105C149509F789BE9AE3D30E013545921203BA867CBBD16D5C2F9FC | Different |
| common/script_constants/029_riches_found_constants.txt | 499394210E8818A5D1F94C6153E27DC7D8C69F378DC871891622806975A610F0 | docs/plans/029_riches_found_plans/evidence/2026_10_03_before/common__script_constants__029_riches_found_constants.txt | 499394210E8818A5D1F94C6153E27DC7D8C69F378DC871891622806975A610F0 | Same |

Additional current-source hashes at capture:

- common/scripted_triggers/029_riches_found_triggers.txt: 01C6E98C08F5DD87DED870E4DE189F8A0E56503BAF8ADEC7467473850EB6B9CF
- common/scripted_effects/029_riches_found_log_effects.txt: F57E1015256836C53C6AA6B163149AC900DF61FC830005FAAE6174D4BB53FB24
- common/scripted_effects/029_riches_found_achievement_effects.txt: E0A1617B7E75AAB77BFA3748AAF99665EA3E56B3282D2F40A0788BCEC30F3618
- common/scripted_triggers/029_riches_found_achievement_triggers.txt: 7973AD1E7B89E2EFCD177A8E0E209113396F44AF1849AB9A931F1A07B726F47B
- common/achievements/chaos_redux_achievements.txt: 6CF880F0E3123908173F5DB5C4F22F0C0D09C54A697135E872E464F4CED7ED3B

Use the immutable before paths above and the current source paths above for the required probability_compare after the owner’s changes. The same scenario IDs and inputs must be reused. No compare was possible here.

## Audited weighted surfaces and local source evidence

### Event 029 opening policy options

events/029_riches_found.txt contains five ai_chance options for chaosx.nr29.1 at lines 128, 150, 174, 198, and 222. The local candidate set is structurally five options: Public Development, State Extraction, Concession Economy, Militarized Mine, and Predatory Extraction. The analyzer did not return poolComplete or effective availability evidence.

The authored raw score inputs in common/script_constants/029_riches_found_constants.txt:921-963 and events/029_riches_found.txt:128-222 are:

| Option | Base score | Authored conditional additions |
| --- | ---: | --- |
| Public Development | 150 | +100 for democratic government |
| State Extraction | 125 | +80 for fascist or communist government, +40 for a major, +60 at war |
| Concession Economy | 115 | +80 below the weak-factory threshold, +20 for a non-major |
| Militarized Mine | 90 | +100 at war, +50 for fascist or communist government |
| Predatory Extraction | 15 | +40 at war, +40 below the stability threshold, +20 for fascist or communist government |

These are raw authored ai_chance scores and modifiers, not normalized click probabilities. No effective score, ranking, conditional option share, or option-probability result was returned. Availability is represented by the event and option logic, but the MCP gate and runtime conditions were not evaluated.

### Decision and mission willingness

common/decisions/029_riches_found_decisions.txt contains 102 ai_will_do blocks. The decision AI tuning table in common/script_constants/029_riches_found_constants.txt defines the raw score tiers never=0, very_low=0.25, low=1, medium=3, high=7, and very_high=12, with multipliers low_factor=0.50, high_factor=2, urgent_factor=4, and never_factor=0. No per-decision effective modifier traces or scenario rankings were returned.

The management category is riches_found_mine_management at common/decisions/029_riches_found_decisions.txt:32 and common/decisions/categories/029_riches_found_categories.txt:5. Its nine mission declarations are:

- mission_riches_found_secure_rush at common/decisions/029_riches_found_decisions.txt:7292
- mission_riches_found_open_railhead at common/decisions/029_riches_found_decisions.txt:7396
- mission_riches_found_protect_pay_train at common/decisions/029_riches_found_decisions.txt:7496
- mission_riches_found_break_claim_war at common/decisions/029_riches_found_decisions.txt:7618
- mission_riches_found_restore_shaft at common/decisions/029_riches_found_decisions.txt:7719
- mission_riches_found_hold_mine at common/decisions/029_riches_found_decisions.txt:7825
- mission_riches_found_public_settlement at common/decisions/029_riches_found_decisions.txt:7925
- mission_riches_found_audit_concession at common/decisions/029_riches_found_decisions.txt:8030
- mission_riches_found_evacuate_workforce at common/decisions/029_riches_found_decisions.txt:8134

Parent steering reports a full source parse confirming all nine are direct children of the category and their AI modifiers are structurally valid. This audit does not flag indentation as malformed syntax. Their AI scores remain unevaluated, and score ranks must not be described as click probabilities.

### Evolution MTTH timing

common/mtth/029_riches_found_mtth.txt defines exactly three entries: riches_found_evolution_i_interval at line 9, riches_found_evolution_ii_interval at line 52, and riches_found_evolution_iii_interval at line 76. Their authored base values in common/script_constants/029_riches_found_constants.txt:861-863 are each 90 days.

The three evolution gates and chaos thresholds are:

| Track | Evolution | Chaos threshold | Source |
| --- | --- | ---: | --- |
| I | The Resource Curse | 600 | common/script_constants/029_riches_found_constants.txt:1007; common/scripted_triggers/029_riches_found_triggers.txt:602 |
| II | Gold Disease | 800 | common/script_constants/029_riches_found_constants.txt:1008; common/scripted_triggers/029_riches_found_triggers.txt:624 |
| III | Demons Beneath the Mine | 1,000 | common/script_constants/029_riches_found_constants.txt:1009; common/scripted_triggers/029_riches_found_triggers.txt:643 |

Authored MTTH factor values include pressure_high=0.70, pressure_severe=0.45, low_order=0.70, low_legitimacy=0.75, war=0.80, multiple_mines=0.85, foreign_capture=0.75, failed_audit=0.70, managed_legitimacy=1.25, gold_disease_pressure=0.65, controlled_closure=1.35, deep_excavation=0.70, and sealed_integrity_low=0.60 in common/script_constants/029_riches_found_constants.txt:900-914. This is the source factor inventory, not a computed effective MTTH.

The scheduler stores the selected MTTH-derived delay and clamps it to configured review floor and ceiling values before scheduling chaosx.nr29.901, .902, or .903 in common/scripted_effects/029_riches_found_effects.txt:1241-1264. No timing distribution, cumulative chance, survival curve, effective MTTH, threshold sweep, or scheduled-state-change analysis was returned. The scenario descriptions do not provide MCP-confirmed complete external state schedules.

### Source, state, foreign-target, and incident selection

common/scripted_effects/029_riches_found_effects.txt:39-85 builds a temporary candidate array by visiting every country that passes the discovery-country trigger, chooses one country from that array, and then selects a valid state. The source comments describe country selection as uniform. The state selector has strong-target and broad-valid-state branches. common/scripted_effects/029_riches_found_effects.txt also contains a weighted commodity/profile random_list. These are two-stage source/state selections, so a single candidate-level probability cannot be inferred from one raw weight.

The live eligible-country and state membership for each scenario depends on actual ownership, control, country exclusions, site flags, suitability, geography, and campaign state. Those candidate memberships were not resolved by probability_inspect. Source-level enumeration is not analyzer evidence of a complete scenario pool.

The on-demand foreign partner selector in common/scripted_effects/029_riches_found_effects.txt:1304-1310 calls riches_found_prepare_scored_foreign_partner. Its implementation is in common/scripted_effects/029_riches_found_incident_effects.txt:301-341 and scans ordinary countries, excludes the current controller, special Chaos and nonhuman countries, capitulated countries, and countries at war with the controller, then admits candidates through neighbor, faction, opinion, or a major-power convoy and port/island condition before calculating a score and keeping the highest-scoring candidate.

Current acceptance gap: common/scripted_triggers/029_riches_found_triggers.txt:546-560 defines riches_found_foreign_target_is_valid using any_neighbor_state. That gate only accepts a foreign controller of a neighboring land state. It rejects a distant naval major even when the scored selector can admit that major for an island or port-route mine with convoys and interest. This contradicts RF_FOREIGN_02_DISTANT_NAVAL_POWER and can suppress an otherwise scored candidate. The source difference is structural evidence; no analyzer ranking or probability was produced.

common/scripted_effects/029_riches_found_effects.txt contains two random_list constructs and common/scripted_effects/029_riches_found_incident_effects.txt contains thirteen. The scenario spec requires complete candidate pools for claims incidents, rush incidents, development setbacks, corruption incidents, foreign interference, raids, collapse severity, Gold Disease incidents, supernatural incidents, and contract outcomes. Exact MCP poolComplete status, candidate weights after modifiers, invalid-target suppression, repetition rates, starvation, and catastrophic-result rates are all unresolved.

### Shared event registration and timing

common/scripted_effects/chaosx_logic_effects.txt:282-295 registers Event 029 through constant:riches_found_event.id in global.repeatable_events. The shared comment at line 282 describes repeatable events as starting at weight 1000 and recovering over time with diminishing caps. common/scripted_effects/chaosx_settings_effects.txt:4406 is a controlled event-dispatch call for chaosx.nr29.1. These shared surfaces were not inspected or evaluated by MCP, so no conclusion is made about Event 029's effective event-selection chance, cap-halving, recovery curve, or interaction with competing events.

## Required scenario coverage

The scenario specification defines 39 named scenarios across Surfaces A-L. Every scenario below remains unevaluated; candidate-pool completeness, external-factor completeness, availability, cost, cooldown, route memory, ranking, and unresolved state are unknown to the analyzer because no result was returned.

| Surface | Required scenario IDs | MCP result |
| --- | --- | --- |
| A. Initial policy | RF_POLICY_01_STABLE_DEMOCRACY; RF_POLICY_02_AUTHORITARIAN_MAJOR_AT_WAR; RF_POLICY_03_POOR_MINOR; RF_POLICY_04_COLONIAL_OCCUPIER | Not evaluated |
| B. Development projects | RF_DEV_01_INLAND_DEEP_REEF; RF_DEV_02_ISLAND_GEMSTONE; RF_DEV_03_COLLAPSE_WARNING | Not evaluated |
| C. Revenue policy | RF_REV_01_HIGH_LEGITIMACY_DEMOCRACY; RF_REV_02_WARTIME_FINANCIAL_CRISIS; RF_REV_03_LOW_LEGITIMACY_NON_CORE | Not evaluated |
| D. Foreign concession target | RF_FOREIGN_01_NEAR_ALLIED_MAJOR; RF_FOREIGN_02_DISTANT_NAVAL_POWER; RF_FOREIGN_03_HOSTILE_RIVAL; RF_FOREIGN_04_EXISTING_EXCLUSIVE_CONCESSION | Not evaluated |
| E. Security response | RF_SEC_01_CIVILIAN_CRIME; RF_SEC_02_ARMED_RAID_WARTIME; RF_SEC_03_WORKER_CLAIM_WAR; RF_SEC_04_PRIVATE_ENCLAVE | Not evaluated |
| F. Evolution I | RF_EVO1_01_MANAGED_MINE; RF_EVO1_02_CAPTURED_CONCESSION; RF_EVO1_03_MULTIPLE_MINES | Not evaluated |
| G. Evolution II | RF_EVO2_01_HIGH_PRESSURE_GEMSTONE; RF_EVO2_02_SHARED_REVENUE_CONTROLLED_ACCESS; RF_EVO2_03_CLOSED_MINE | Not evaluated |
| H. Evolution III | RF_EVO3_01_AGGRESSIVE_DEEP_MINE; RF_EVO3_02_PARTIALLY_SEALED; RF_EVO3_03_GOLD_DISEASE_MASS_VIOLENCE | Not evaluated |
| I. Gold Disease response | RF_GOLD_01_STABLE_HIGH_LEGITIMACY; RF_GOLD_02_AUTHORITARIAN_WARTIME; RF_GOLD_03_COLLAPSE_IMMINENT | Not evaluated |
| J. Demonic response | RF_DEMON_01_STABLE_DEMOCRACY_PEACE; RF_DEMON_02_COLLAPSING_AUTHORITARIAN_WAR; RF_DEMON_03_EVACUATION_COMPLETE | Not evaluated |
| K. Gilded Sovereignty | RF_GILDED_01_WEALTHY_REFORMIST; RF_GILDED_02_WEAK_DEPENDENT_STATE; RF_GILDED_03_MILITARY_MAJOR | Not evaluated |
| L. Bottomless Account | RF_ACCOUNT_01_STABLE_STATE; RF_ACCOUNT_02_DESPERATE_WAR_STATE; RF_ACCOUNT_03_LOW_STABILITY_HIGH_DEPENDENCE | Not evaluated |

Surface M additionally requires complete candidate-pool inspection of the ten incident families listed above. Surface N requires the repeat-recipient selection pool check: equal country weights for all valid ordinary recipients, zero and N/A for a country without a suitable state, and separate state suitability selection. Neither surface received an MCP result.

The 15 aggregate balance scenarios in the AI/balance spec and the RF_TEST_* acceptance scenarios also have no probability result in this handoff. Their source and live-play acceptance remains with the parent implementation and validation workflow.

## Baseline defects, current corrections, and remaining gap

The immutable pre-change snapshot common__scripted_effects__029_riches_found_effects.txt has riches_found_contract_exclusive_request checked with compare greater_than at line 1366. The unchanged decision source sets that request to constant:riches_found_value.one at common/decisions/029_riches_found_decisions.txt:2325. A strict greater-than-one condition therefore fails to recognize the caller's one-valued exclusive request. The current worktree source now compares the request to one with equals at common/scripted_effects/029_riches_found_effects.txt:1377. This is a baseline defect with an apparent owner-applied current correction. It still needs the same-scenario probability_compare result before any post-change weighted-behavior claim.

The immutable pre-change snapshot has the STATE-scoped riches_found_extend_limited_contract call the COUNTRY-scoped riches_found_refresh_mine_state directly at line 1395. The current worktree wraps that refresh in CONTROLLER scope at common/scripted_effects/029_riches_found_effects.txt:1410, matching the COUNTRY scope declaration at line 1142. This is a baseline scope-contract defect with an apparent owner-applied current correction. It still requires the post-change MCP comparison and structural review.

The foreign target validity mismatch remains in current source at common/scripted_triggers/029_riches_found_triggers.txt:549-560. Recommendation to the parent: align the target-validity gate with the selector's intended access and convoy conditions so RF_FOREIGN_02_DISTANT_NAVAL_POWER can remain valid where the spec allows it, while retaining invalid-target suppression. No target or weight value is proposed here.

The source snapshot set was supplied for the later compare. Since the current effects and incident files differ from the snapshots and the worktree was changing, the exact after hashes above must be refreshed at comparison time. No source patch was made by this auditor.

## Evolutions, missions, achievements, and exclusions

The current constants and triggers confirm exactly three evolution thresholds: Resource Curse at 600, Gold Disease at 800, and Demons Beneath the Mine at 1,000. The source defines three corresponding MTTH entries, each with a 90-day authored base.

The current decision file contains the nine named missions listed above under riches_found_mine_management. Parent steering reports a full parse of their nesting and AI modifiers. The source review does not report malformed braces based on indentation.

The source specification defines exactly seven achievements: 029_public_fortune, 029_claim_jumper, 029_the_pay_train_runs, 029_all_that_glitters, 029_no_man_owns_the_mountain, 029_close_the_account, and 029_the_last_shift. Current achievement tracking triggers include seven route predicates plus the multi-mine helper predicate in common/scripted_triggers/029_riches_found_achievement_triggers.txt:40-217. However, a search of the captured common/achievements/chaos_redux_achievements.txt for those seven exact IDs returned no matches. The seven achievement registry entries therefore remain unconfirmed in the captured implementation and should be reconciled by the parent; the root registry was concurrently modified.

The scoped source search found no direct chaosx.nr18 event call, no biological outbreak call, and no unrelated special or nonhuman actor in the weighted selection sources. The trigger file does reference resources_found_* state flags at lines 32-45 to exclude states already used by Event 018, and excludes special Chaos/nonhuman countries from recipient and foreign candidate pools. This is an exclusion check, not an Event 018 cave/resource call. The decision file header at line 6 likewise states the intended system separation.

The current package uses the ordinary decision category and a static category image. No Event029-owned scripted GUI file appeared in the scoped file inventory, so a dedicated event-ui worker is not indicated by this audit.

## MCP classifications, recommendations, and remaining uncertainty

| Evidence class | Result |
| --- | --- |
| Exact | Source constants define three evolution thresholds (600/800/1,000), three 90-day MTTH bases, five opening ai_chance options with the raw score constants above, 102 decision/mission ai_will_do blocks, nine mission declarations, and the listed source random_list counts. |
| Bounded | The foreign selector's source-level candidate gate and the neighbor-only validity contradiction are bounded findings from current source. The two exclusive-request and refresh-scope defects are confirmed in the immutable before snapshots and appear corrected in current source. |
| Sampled | None. probability_simulate was not called and no sample distributions or seed were specified. |
| Score-only | Raw source score constants are listed above. No evaluated effective score or rank is available. |
| Unresolved | All normalized shares, candidate pool completeness, external-factor completeness, option and decision rankings, threshold sensitivity, rank reversals, dominance, starvation, repetition, effective MTTH/timing, repeatable-event recovery, valid-target suppression in scenarios, and before/after deltas. |

The decision ai_will_do scores are willingness scores, not direct click probabilities. Event-option shares, if later returned by the analyzer, must be labelled conditional on the event firing unless the tool explicitly includes firing chance. No exact selection probability is stated in this handoff.

Recommended next evidence for the parent is to let the existing MCP requests resolve or use their final service error without resubmitting identical calls, then inspect every source listed above, evaluate the 39 named scenarios plus complete Surface M/N pools, sweep specified thresholds, render useful rankings/timing/matrix views, and compare the immutable before sources against the exact current after paths under the same scenario IDs. Keep all results unresolved until the MCP returns complete/poolComplete and scenario-specific evidence.

## Simplifications, omissions, and blockers

- Probability MCP results are absent. This is the principal blocker, not proof that the route is permanently unavailable.
- No offline wiki or installed vanilla documentation citation was returned.
- No event_inspect, event_render, or decision_inspect result was returned.
- No candidate pool, external factor, cost, availability, cooldown, route-memory, seed, cadence, or time-varying state fixture received analyzer validation.
- No evaluator result exists for any of the 39 named scenarios or the Surface M/N pools.
- No sweep, simulation, sequence, render, or compare evidence exists.
- Event029 achievement registry coverage is not confirmed in the captured root registry.
- The worktree contained concurrent parent edits and advanced to a different observed HEAD during this audit; source hashes are capture-time identities only.

No gameplay simplification or fallback was applied by the auditor. This handoff remains partial and unresolved.
