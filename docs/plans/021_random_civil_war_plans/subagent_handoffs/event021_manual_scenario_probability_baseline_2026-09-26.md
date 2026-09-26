# Event 021 Manual Scenario Country-Selection Pool Baseline

Date: 2026-09-26.

Disposition: `unresolved` for scenario probabilities and balance because the connected custom-pool adapter did not discover or represent the source's dynamic country pool. Source-level mechanics below are read-only findings, not a complete probability baseline and not balance approval.

No gameplay source was edited. This report is the only requested output artifact.

## Audited surface and source identity

The bounded surface is `random_civil_war_trigger_manual_scenario` and `event021_parent_add_scenario_target_to_weighted_pool` in `common/scripted_effects/021_random_civil_war_parent_effects.txt`, especially the dynamic pool build and draw around lines 5821-5874 and 6584-6730.

The exact-current source identity for the baseline is the parent-owned direct `hoi4.probability_inspect` result below. It takes precedence over earlier assistant-side inspection responses in this session that reported a different indexed revision.

- Adapter: `custom_weighted_pool`.
- Source object: `{ path: "common/scripted_effects/021_random_civil_war_parent_effects.txt" }`.
- Result: `PROBABILITY_SOURCE_INSPECTED`, status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`.
- MCP `sourceRevision`: `ea4669159bc268bcacb07b26a88c4b151990475a45248e401b6d1d6fd5936617`.
- MCP `sourceHash`: `6bd965bf376ee70c602e9fcd4f6d0e805be135d7ce10c2ed493c04566070c513`.
- Pool fields: `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, `unresolved=0`.
- Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cdae552a308846be0508861140f802cde624097fcfd0fb285c40c4598abad31/87eef4d593b895e9670c84cd6053075617b99cfa5bc8d5b7a8b039c4fd3aec49/probability-inspect-6bd965bf376e.json`.

`candidates=0` is adapter discovery output, not evidence that the live scenario has an empty candidate pool. `poolComplete=false` is the controlling coverage result. The returned `requiredInputs=0` likewise does not prove that runtime inputs are unnecessary.

## Supporting source files and identifiers

- `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`: `event021_parent_scenario_country_eligible`, `event021_parent_scenario_type_preflight_valid`, `event021_parent_scenario_opening_state_preflight_valid`, and Event 006 dormant-candidate gates.
- `common/scripted_triggers/021_random_civil_war_triggers.txt`: `random_civil_war_is_normal_human_country`.
- `common/scripted_effects/individual_crisis_targeting_effects.txt`: `adjust_individual_crisis_candidate_ticket_weight` and `individual_crisis_apply_candidate_ticket_curve`.
- `common/scripted_triggers/individual_crisis_targeting_triggers.txt`: `individual_crisis_load_is_below_cap` and the derived `individual_crisis_active_load` inputs.
- `common/script_constants/021_random_civil_war_constants.txt`: `random_civil_war_scenario` and `random_civil_war_scenario_target_weight`.
- `common/script_constants/individual_crisis_targeting_constants.txt`: `individual_crisis_targeting` load factors, cap, and ticket constants.
- `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt`: Event 006's Event 021 package allowlist and actor crosswalk.

The manual pool is dynamically assembled by `every_country` into temporary arrays. Its size follows live eligible countries and ticket weights. The maximum-intensity branch adds each eligible country once and bypasses weighted selection. This bounded audit does not assess the separate front-state sizing or full Event 021 route architecture.

## Source trace and exact source values

The source uses a ticket array, not an `ai_will_do` score race, an event-option `ai_chance`, or MTTH timing. `random_scope_in_array` selects an entry from the array, and repeated country scopes encode ticket multiplicity. No click probability or normalized probability was returned by MCP.

For non-maximum intensities, the source assigns these base ticket weights by country major status:

| Intensity | Minor base weight | Major base weight | Eligible-country share used for draw budget |
| --- | ---: | ---: | ---: |
| Low | 4 | 1 | 0.10 |
| Medium | 2 | 2 | 0.25 |
| High | 1 | 3 | 0.50 |
| Maximum | Weighted draw bypassed | Weighted draw bypassed | 1.00, with every eligible country copied once |

The shared ticket helper multiplies the base weight by the active-load ticket factor: load zero uses `individual_crisis_targeting.load_zero_tickets = 4`, load one uses `load_one_tickets = 2`, and load two uses `load_two_tickets = 1`. The shared eligibility cap is `active_cap = 3`, so eligible derived load must remain below three. These are source values only. MCP did not produce per-country adjusted weights or a ranking.

The scenario draw budget starts from the unique eligible-country count, applies the selected intensity share, rounds, enforces at least one draw when candidates exist, and caps the budget at the eligible-country count. It therefore has a live, campaign-sized bound rather than a fixed country-slot count.

After each draw, the selected country scope is appended to `event021_parent_scenario_selected_targets`. The source initializes `event021_parent_scenario_remove_tickets` from `constant:individual_crisis_targeting.load_zero_tickets` and calls `remove_from_temp_array` four times for that country. That constant is also the load-zero ticket multiplier.

The draw predicate rechecks `event021_parent_scenario_country_eligible`, but that trigger does not test whether the country is already in `event021_parent_scenario_selected_targets`. The draw-success flag is set on the controller scope, and the selected-country confirmation flag is applied only after the weighted selection loop. If a selected country's adjusted ticket multiplicity exceeds four and additional draws remain, the source therefore permits residual entries for that country to be drawn again. The conditional repeated-ticket risk is source-bounded. Its occurrence rate and downstream effect are unresolved without a complete scenario pool and MCP trace.

A singleton eligible pool is capped to at most one requested draw, even if residual tickets remain after the four removal calls. The repeated-selection concern applies when more than one draw is budgeted and the selected country remains eligible.

The base category weights reverse direction across intensity: Low gives minors the larger base weight, Medium gives both classes equal base weight, and High gives majors the larger base weight. This is an exact source-level preference change, not an MCP candidate ranking or probability result. Actual country ordering, dominance, starvation rates, and rank reversals after live load factors remain unresolved.

## Eligibility and external factors

`event021_parent_scenario_country_eligible` requires the rework-ready global state, a normal existing country, no terminal lock, a permitted successor-grace/manual-launch state, no external queue block, no active Event 021 crisis, no target or cluster reservation, shared crisis load below cap, at least one controlled state, and valid type and opening-state preflight.

`random_civil_war_is_normal_human_country` means `exists = yes` and not `is_actual_nonhuman_country = yes`. It does not require `is_ai = no`, so AI-controlled normal countries can be members of the candidate pool. The launch is manual, but candidate control status is not an eligibility gate in this trigger.

The shared active-load calculation derives state from 14 provider markers: Holy Realm, Soviet Collapse, Fury, Secret Alliance, Natural Disaster, Utopia Manifesto, Brilliant Scientist, Resources Found, Random Civil War, Video Game in Sweden, Riches Found, Time Traveler, Random Terror, and Murder Mystery. Every named provider marker, country flag, state condition, queue, reservation, controlled-state count, route/type preflight, and opening-state condition can change the candidate set or adjusted weight.

Event 006 does not appear as a direct term in the shared active-load ticket curve. For `independence_cascade`, Event 006 dormant-package availability can affect country eligibility through the type and opening-state preflight, so it remains a required external input for that scenario. After country selection, `event021_parent_find_event6_package` scans the Event 006 adapter registry from a cursor, skips reserved package IDs, and validates package actor and anchor state availability. That later package choice is not a weighted entry in the manual country-selection pool.

The source-declared Event 006 adapter package allowlist contains 32 IDs: `iw_001`, `iw_002`, `iw_004`, `iw_006`, `iw_007`, `iw_008`, `iw_009`, `iw_010`, `iw_012`, `iw_014`, `iw_017`, `iw_018`, `iw_019`, `iw_023`, `iw_024`, `iw_026`, `iw_027`, `iw_028`, `iw_029`, `iw_030`, `iw_031`, `iw_033`, `iw_038`, `iw_040`, `iw_041`, `iw_044`, `iw_045`, `iw_070`, `iw_071`, `iw_072`, `iw_173`, and `iw_184`. This static allowlist is source-complete. The currently usable package subset is campaign-dependent on initialization, reservations, actor readiness, and valid anchors.

## Named scenarios and completeness

These IDs name the requested audit cases. None was submitted to `hoi4.probability_evaluate`, `hoi4.probability_sweep`, or `hoi4.probability_sequence`, so there are no MCP scenario hashes or scenario outputs. Do not interpret the inspecter's zero discovered candidates as an evaluated empty pool.

| Scenario ID | Candidate-pool completeness | Required external inputs not represented | Result class |
| --- | --- | --- | --- |
| `E021-MANUAL-EMPTY-POOL-2026-09-26` | The scenario premise is an empty eligible set, but the adapter did not confirm or model that set. | Complete country enumeration and the values of every eligibility gate. | Unresolved. |
| `E021-MANUAL-SINGLE-HIGH-LOAD-2026-09-26` | Singleton is the requested premise; no actual country tag or candidate manifest was submitted. | Country tag, major status, explicit scenario type and intensity, derived active load, all eligibility flags, queue and reservation state, controlled states, and valid route/opening-state preflight. | Unresolved. |
| `E021-MANUAL-SEVERAL-UNEVEN-LOAD-2026-09-26` | Incomplete. The full eligible-country list and each country's ticket multiplicity are absent. | Every eligible tag, major status, provider markers and derived load, selected type/intensity, and all eligibility gates. | Unresolved. |
| `E021-MANUAL-SELECTED-COUNTRY-REMAINS-2026-09-26` | Incomplete. The complete pre-draw ticket array and draw budget are absent. | Every country and its adjusted ticket count, a budget with further draws after the first selection, and the same live eligibility inputs. | Unresolved probability. Conditional residual-ticket behavior is source-bounded. |
| `E021-MANUAL-EVENT006-PACKAGES-2026-09-26` | The 32 package IDs are statically enumerable from Event 006's allowlist, but the live usable package subset and country target pool are incomplete. | Package registry initialization, cursor, reserved IDs, package-specific actor readiness, valid anchor state and ownership, scenario type, and the complete country/load/eligibility inputs. | Unresolved. |

The installed scenario contract accepts an actor string, flat primitive state, flags, and primitive state under explicitly named scopes. It does not provide typed Clausewitz numeric-variable declarations or compound-trigger fixtures. The dynamic `every_country` candidate enumeration, derived shared-load trigger, arrays, and Event 006 package/anchor state cannot be reconstructed faithfully from the requested scenario descriptions without inventing unsupported fixture semantics. No such fixture or candidate manifest was invented.

## MCP outputs and classifications

| Tool | Result | Classification |
| --- | --- | --- |
| `hoi4.probability_inspect` on the exact Event 021 source | Parent-owned direct artifact above. Pool incomplete and zero candidates discovered. | Adapter/source discovery only, not a probability baseline. |
| `hoi4.probability_evaluate` | Skipped because the actual candidate pool and required live country state cannot be represented. | No score trace, probability, ranking, or timing result. |
| `hoi4.probability_sweep` | Skipped because per-candidate base status, active load, pool, and external gates are not represented. | No MCP sensitivity or rank-reversal result. |
| `hoi4.probability_sequence` | Skipped because there is no complete declared custom-pool manifest with all candidate tickets and state transitions. | No sampled or exact sequence result. |
| `hoi4.probability_simulate` | Skipped because no explicit distributions, seed, or uncertain-input model was declared and the candidate pool is incomplete. | No sampled result. |
| `hoi4.probability_compare` | Skipped because this is a baseline-only audit with no before/after source or complete candidate comparison under a shared scenario set. | No comparison ID or delta. |
| `hoi4.probability_render` | Skipped because there is no evaluated analysis ID to render; the inspect artifact is a source-discovery artifact. | No rendered probability evidence. |

`Exact` source evidence: the listed constants, eligibility clauses, dynamic pool construction, four removal iterations, and Event 006 allowlist. `Bounded` source finding: a selected country can remain eligible for another draw if its adjusted ticket multiplicity exceeds the four removal calls and the draw budget has more iterations. `Unresolved` MCP findings: actual ticket totals, per-country conditional probabilities, ranking, dominance, starvation, repetition frequency, and downstream duplicate-plan effects. `Sampled` and `score-only` outputs were not produced.

AI `ai_will_do`/`ai_chance` validity is not applicable to this manual selection surface. It contains no AI willingness score. Its country pool can include AI-controlled normal countries, as described above. No exact probability is asserted.

## Findings and recommended follow-up

The current removal step is a fixed four-ticket deletion coupled to `individual_crisis_targeting.load_zero_tickets`. If the intended contract is one selection per country, the source should exclude already-selected countries dynamically or remove all matching entries until none remain. A fixed ticket-removal count does not enforce country uniqueness. If fixed deletion is retained by design, its tuning constant should be separate from the load-zero weighting factor. These are recommendations only and were not applied.

Before balance approval, a future probability pass needs a supported complete scenario representation for the eligible country roster, each country's major/minor status and derived load, explicit type/intensity, all eligibility gates, and any Event 006 package/anchor state used by `independence_cascade`. The same named scenarios can then be evaluated and swept. A sequence pass additionally requires the complete ticket array and every draw/removal transition.

No balance target is approved by this baseline. The parent should review whether repeated selection is intended and whether duplicate selected-country entries can safely reach preparation and commit callbacks. The callback effects and live campaign behavior were outside this bounded pool audit.

## Process note and limits

The first source excerpt in this audit was opened after the required first MCP inspect but before the offline wiki consultation. The relevant offline Effects, Data Structures, Scopes, and Triggers material and vanilla array/loop/effect documentation were reviewed afterward. This ordering was a procedural deviation, with no source mutation.

The audit used `chaos-redux-subagents` and `chaos-redux-events`. It did not inspect or render the full Event 021 chain because the requested scope was the weighted country-selection pool, not event-chain structure. No gameplay source, localization, GUI, or Event 006 package file was changed.
