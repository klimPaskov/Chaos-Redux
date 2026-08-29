# Famine and Migration System: AI Probability Baseline

Audit date: 2026-08-24

> **Superseded historical snapshot (2026-08-25):** This baseline records a pre-separation source snapshot and is retained for historical comparison only. Its combined source path, counts, hashes, and unresolved-scenario status are not current instructions. Use [source_of_truth_map.md](source_of_truth_map.md), [completion_report.md](completion_report.md), and [ai_probability_current.md](ai_probability_current.md) for the current incomplete audit status and blockers.

Audit mode: read-only current-source baseline. No gameplay, localisation, asset, workbook, or source implementation file was edited by this audit. The pre-existing source change in common/decisions/famine_migration_decisions.txt was preserved.

## Outcome

The current source contains exactly seven uniform random_neighbor_state selections and 26 ai_will_do blocks across six missions and 26 decisions. The baseline defect is confirmed at source level: destination selection is uniform among states passing each limit, with no weighted candidate scoring or internal-first stage. The required probability adapters did not expose a complete candidate pool, so no exact selection probability, ranking, timing distribution, dominance, starvation, or rank-reversal claim is resolved by MCP.

## Audited surfaces and references

Primary gameplay source: common/decisions/famine_migration_decisions.txt.

Shared tuning source: common/script_constants/famine_migration_constants.txt.

Scenario source: docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv.

Prepared audit prompt: docs/specs/famine_and_migration_system_specs/subagent_prompts/03_ai_probability_auditor_baseline.md.

The full famine_and_migration_system_specs package, AGENTS.md, chaos-redux-subagents, chaos-redux-decisions-missions, chaos-redux-event-planning, the required offline Paradox wiki pages, and relevant vanilla documentation were reviewed. Event, focus, GUI, and technology structural adapters were not applicable to this decision/mission and random-state selection surface.

## Current MCP evidence

Workspace: mod_chaos_redux_ea3b2d67c2c0.

Source revision: 8c9fbec5c423574f1510dc711da1668c230279b2e825ae3255ddcb337acfb7dc.

Source hash: a1b7fda6b69c9429ae6151b98fc1e96b9556087b5d566ed6e126ab40c17b4728.

| Adapter or route | Result | Evidence |
| --- | --- | --- |
| decision_ai_will_do | Empty/suggested mission result; no usable decision pool | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37858f6b331cf501eae67a2da4e3f6a8c283562bedddd3d9c845a9a63673ffb5/4e73f2461095daa1ec0da04a9ce4a0672810e43aeb6ff6c8498500c2b05f798c/probability-inspect-a1b7fda6b69c.json |
| mission_ai_will_do | Inspect returned 26 candidates, poolComplete=false, availableCandidates=0, requiredInputs=12, unresolved=0 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4616445bd05406533ee2cebf407cff11a6cbebf500f0e100ce835ab8fbb2393a/ca8647c10ee04ee5111ac474514de0bc0e07032356daed94f2d06adcc7831e3b/probability-inspect-a1b7fda6b69c.json |
| direct_random | Adapter does not recognize random_neighbor_state | No artifact issued; exact blocker is unsupported construct |
| custom_weighted_pool | poolComplete=false and candidates=0 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3d38f26b020e9231db9df2e6e182abb6d3d73f0351a45d378e1cf728c0d8545/14ce8570c1c15ac779d578dec0a73eccec20f9d7db56713bce0fe94c555828c5/probability-inspect-a1b7fda6b69c.json |

The mission inspect above was the one short confirmatory probability_inspect call permitted for this recovery. No scenario hash, evaluation id, comparison id, or rendered evidence URI was produced. The artifact and source revision/hash must travel with the owner patch and later compare pass.

## Seven uniform selection sites

The following are the complete current random_neighbor_state sites. Each is a score-free random neighbor choice after its limit is applied; none has an internal-first stage or a weighted candidate pool.

| Site | Source line | Current limit summary | Baseline risk |
| --- | ---: | --- | --- |
| fm_famine_evacuation | 1417 | Valid state; no famine food-security, unsafe route, persecution, bombing, CBRN contamination, or trapped flag; controller not at war with ROOT; valid owner; reception capacity; load below capacity; border policy not closed | Uniformly selects among surviving neighbors; no route, relations, ties, ideology, danger, or donor score |
| fm_evacuate_vulnerable | 1577 | Same safe-neighbor and capacity/load/border-policy gate | Vulnerable priority is a mission score, not destination weighting; no internal-first guarantee |
| fm_evacuate_workers | 1729 | Same safe-neighbor and capacity/load/border-policy gate | Worker destination choice remains uniform and cannot prefer a safer or better-connected host |
| fm_requisition_safer_state | 1893 | State is owned and controlled by ROOT; no famine food-security, unsafe route, persecution, bombing, or contamination | No reserve/surplus, protected-state, route, or capacity scoring; a strained donor can pass |
| fm_distribute_arrivals | 2348 | Valid state owned by ROOT; no famine food-security or unsafe route | No reception capacity/load check, so an exhausted destination can remain eligible |
| fm_transit_only | 2511 | Valid foreign-owned state; valid owner; no famine food-security or unsafe route; controller not at war with ROOT | No border acceptance, capacity, onward route, relations, ties, ideology, danger, or forced-return scoring |
| fm_third_country_resettlement | 2886 | Valid safe state; controller not at war; valid foreign owner; reception capacity; load below capacity; no famine, unsafe route, persecution, bombing, or contamination | Capacity is gated but border, route, relations, ties, ideology, danger, and forced-return scores are absent |

These limits are eligibility filters, not weighted probabilities. A state that passes a limit has no source-level weight advantage over another passing state. If no state passes, the effect has no valid destination; MCP could not produce a direct random trace because direct_random does not support this construct.

## Source score values

The centralized constants provide ai_will_do score bases and factors, not click probabilities:

| Decision or mission | Base | Factors visible in constants |
| --- | ---: | --- |
| fm_famine_evacuation | 10 | factor_1=4, factor_2=3, factor_3=2 |
| fm_evacuate_vulnerable | 13 | factor_1=4, factor_2=3 |
| fm_evacuate_workers | 8 | factor_1=3, factor_2=2 |
| fm_requisition_safer_state | 5 | factor_1=3, factor_2=0.3 |
| fm_distribute_arrivals | 9 | factor_1=4, factor_2=3 |
| fm_transit_only | 6 | factor_1=3, factor_2=2 |
| fm_third_country_resettlement | 7 | factor_1=4, factor_2=3 |

The source review identifies these as score inputs only. MCP supplied no modifier traces because the candidate pool was incomplete and all 12 required inputs were unavailable. It is therefore invalid to normalize these bases into action probabilities or to infer a score race winner.

## Scenario baseline

All 20 scenario IDs from the probability CSV were registered for the requested baseline. Every row is unresolved for probability because the adapter did not return a complete candidate pool or external-factor trace. The expected behavior below is the CSV contract to test after the owner patch, not a result proved by this baseline.

| Scenario ID | Expected contract | Pool and external-factor completeness | Baseline result |
| --- | --- | --- | --- |
| prob_famine_relief_dense | Relief/route repair should outrank concealment/extraction; invalid recovered state is zero | Pool incomplete; reserves, route, state validity, and competing actions unavailable | Unresolved |
| prob_famine_relief_blocked_island | Escorted convoy/airlift should beat generic imports; evacuation rises as reserves fall; generic import is zero without route | Pool incomplete; route, reserves, airlift, and import candidates unavailable | Unresolved |
| prob_soviet_extraction | Extraction/concealment can lead early; relief rises with collapse/republic pressure/exposure; no concealment benefit after exposure | Pool incomplete; exposure, pressure, collapse, and strategy factors unavailable | Unresolved |
| prob_humanitarian_border | Open/controlled entry should beat closure; forced return near zero; no destination without a receiver | Pool incomplete; border policy, route, receiver, and return candidates unavailable | Unresolved |
| prob_capacity_exhausted_border | Transit/distribution/resettlement should beat unlimited open entry; closure may rise; famine destination cannot be ignored | Pool incomplete; capacity/load and policy states unavailable | Unresolved |
| prob_outbreak_reception | Controlled medical reception should beat closure and ordinary open entry; no outbreak penalty without exposure | Pool incomplete; outbreak exposure and reception controls unavailable | Unresolved |
| prob_nuclear_evacuation | Organized evacuation should beat hold; vulnerable priority rises; no return while fallout is high | Pool incomplete; fallout, vulnerability, evacuation, and return factors unavailable | Unresolved |
| prob_genocide_escape | Entry should beat closure; forced return near zero; ideology cannot override persecution | Pool incomplete; persecution, ideology, border, and return factors unavailable | Unresolved |
| prob_authoritarian_pushback | Controlled/closure can lead; violent pushback stays below closure absent extreme flags; zero without policy | Pool incomplete; policy and pushback candidates unavailable | Unresolved |
| prob_destination_selection_internal | Safe internal destination should beat foreign when capacity/route are adequate; unsafe internal is zero | Pool incomplete; internal/foreign candidates, route, and capacity unavailable | Unresolved |
| prob_destination_selection_persecution | Safe different-ideology host should beat same-ideology persecutor; persecutor is zero | Pool incomplete; persecution, ideology, route, and host candidates unavailable | Unresolved |
| prob_corridor_acceptance | Acceptance rises with condemnation/observers and low military cost; invalid geometry is zero | Pool incomplete; corridor geometry, observers, condemnation, and cost unavailable | Unresolved |
| prob_forced_return | Voluntary return rises when origin is safe; forced return near zero when unsafe; no voluntary return without route/safety | Pool incomplete; origin safety, route, and return modes unavailable | Unresolved |
| prob_integration | Integration should beat temporary status as duration rises; no repeat after integrated | Pool incomplete; duration, status, and terminal state unavailable | Unresolved |
| prob_opposition_channel | Credible local movement should beat absent ideologies; absent/invalid is zero | Pool incomplete; movement, ideology, and validity factors unavailable | Unresolved |
| prob_disaster_flight | Severe destruction should beat minor damage; zero damage should not create mass flow | Pool incomplete; damage and flow candidates unavailable | Unresolved |
| prob_bombing_exodus | Persistent heavy damage should beat a single raid; shelters reduce flow; cooldown blocks duplicates | Pool incomplete; damage persistence, shelters, and cooldown unavailable | Unresolved |
| prob_requisition_donor | Safe high-surplus donor should beat strained/occupied donor; famine/protected donor is zero | Pool incomplete; surplus, occupation, famine, and protected-state factors unavailable | Unresolved |
| prob_relief_donor | Reachable stock plus relations should beat distant/blocked donor; no donor without route/capacity | Pool incomplete; stock, route, relations, and capacity unavailable | Unresolved |
| prob_cleanup | Annexation, destination loss, route change, and reload should pause/redirect/trap safely without duplicate debit | Pool incomplete; terminal states, timers, and ledger transitions unavailable | Unresolved |

No row has an exact, bounded, sampled, or score-race result from MCP. The classification for all scenario conclusions is unresolved; the seven source site descriptions and constant values are score/source-only evidence.

## Findings and risks

The 26 ai_will_do blocks are willingness scores. They are not probability-proportional selections. Vanilla AI guidance distinguishes score races from ai_chance/random-list sampling; the seven random_neighbor_state calls have no per-candidate weights at all.

The dominant systemic risk is destination flatness. A passing foreign neighbor can be selected exactly like a safer internal state unless the caller has already constrained the pool. There is no proof that internal destinations are exhausted before foreign migration.

Eligibility is incomplete at several high-impact sites. distribute_arrivals has no capacity/load gate. requisition_safer_state has no donor reserve/surplus or protected-state gate. transit_only lacks border acceptance, capacity, onward route, relations, ties, bounded ideology, danger, and forced-return checks. The other foreign destination sites lack most of those score dimensions even when capacity is present.

Persecution, bombing, contamination, food security, unsafe route, nuclear fallout, outbreak exposure, and controller war are partly represented as binary limits, but they are not a complete danger or route score. The source cannot prove that an invalid or unsafe candidate receives zero under every scenario.

Because cadence, cooldown, recovery, removal, reset, timer, and terminal-state traces were not available, repetition, duplicate debit, starvation, dominance, timing drift, and reload/annexation exploit risks remain unresolved.

## Accepted owner-patch requirements

These are required owner changes, not changes applied by this auditor:

1. Build a complete weighted candidate pool for each of the seven destination surfaces. The pool must enumerate every candidate considered by the action and expose the weights and modifier trace to the probability adapter.
2. Give impossible, dead, hidden, blocked, occupied-incompatible, route-incompatible, capacity-exhausted, famine, protected, persecuting, or otherwise invalid candidates weight exactly 0. Do not hide invalid candidates behind a positive fallback.
3. Implement internal-first selection: score safe ROOT-controlled destinations first, and permit foreign fallback only when the declared internal stage has no valid candidates or the scenario explicitly requires external migration.
4. For foreign routes, require and score route reachability, border/entry policy, controller-at-war status, receiving capacity/load, onward route, and destination food security. Open entry must not imply unlimited reception.
5. Add bounded relations and tie factors, including diplomatic relations and declared humanitarian, historical, ethnic, alliance, or observer ties. Ties may influence a valid pool but must not override persecution, danger, route, or capacity invalidation.
6. Add bounded ideology and persecution scoring. Same ideology must not override an unsafe or persecuting host; a persecutor must be zero in the persecution scenarios.
7. Add bounded danger and forced-return scoring for route danger, bombing, contamination, fallout, outbreak exposure, persecution, and return safety. Forced return must be near zero or zero when the origin remains unsafe, and voluntary return must require a safe reachable route.
8. Add donor reserve/surplus and relief-stock scoring. Strained, occupied, famine, protected, unreachable, or capacity-exhausted donors must be zero; reachable stock and relations must be visible modifiers.
9. Centralize tuning in the existing constants surface or an explicitly documented shared constants file. Keep mission/decision willingness scores separate from destination probabilities.
10. Declare cadence, cooldown, recovery, removal, reset, timer, reload, annexation, destination-loss, route-change, and terminal-state behavior for every custom pool or ledger-consuming action. Prevent repeated selection and duplicate debit.
11. Add complete scenario fixtures for all 20 IDs, including candidate lists, route/border state, capacity/load, reserves/stock, relations/ties, ideology/persecution, danger, forced-return safety, cooldowns, seeds, cadence, and terminal state.
12. After the owner patch, rerun probability_inspect and the named evaluate/sweep/compare workflow with the same scenario IDs. Use sequence only after a complete declared custom pool exists, and render ranking/timing/sensitivity evidence. A probability claim remains prohibited while poolComplete is false or required inputs are missing.

## Skipped analyses and exact blockers

probability_evaluate, probability_sweep, probability_simulate, probability_sequence, probability_render, and probability_compare were not run. The mission pool had zero available candidates and 12 required inputs missing; decision_ai_will_do was empty/suggested; direct_random does not recognize random_neighbor_state; custom_weighted_pool returned zero candidates. The parent also prohibited long sweeps for this recovery. No replacement hand arithmetic or source-only probability claim was used.

There is no rendered evidence path, scenario hash, evaluation id, or comparison id to report for this baseline. The four inspect artifacts, workspace, source revision, and source hash above are the complete current MCP evidence.

## Handoff

Changed file: docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md.

No gameplay or source implementation file was changed by this audit. The report is ready for the owner patch, but the baseline remains unresolved for probability until the seven destination pools are complete and the same 20 scenarios can be evaluated through MCP.
