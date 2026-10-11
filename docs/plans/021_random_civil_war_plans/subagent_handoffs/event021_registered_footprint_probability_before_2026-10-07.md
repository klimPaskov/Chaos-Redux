# Event 021 registered release footprint probability audit, before patch

Disposition: pre-patch baseline captured. The requested footprint repair is not implemented or certified by this audit.

The audit is read-only against Event 021 native Event 006 release-footprint eligibility. Parent direction is to retain the existing registered packages, including larger human packages, and to add no balance or pool redesign.

No gameplay, AI, event, trigger, constant, localisation, workbook, runtime, Git, game, desktop, or log-search action was performed. The only repository writes are this handoff and the two JSON evidence files linked below.

The immutable fixture contract is [registered_footprint_fixtures_2026-10-07.json](../event021_registered_footprint_probability_2026-10-07/evidence/registered_footprint_fixtures_2026-10-07.json), SHA-256 `2F0AB6F96249F31B5554F6BB6A4AB5D82E1DA64A4A34885C2FE6ACEEB7CEC9A4`. It contains all eight requested fixture IDs, the one schema-accepted scenario payload, the six-branch archetype candidate pool, the complete 32-ID registered package array, declared roles, unresolved bindings, and raw source identities.

The exact MCP calls, revisions, scenario hash, source hashes, diagnostics, reference citations, and artifact URIs are in [mcp_evidence_2026-10-07.json](../event021_registered_footprint_probability_2026-10-07/evidence/mcp_evidence_2026-10-07.json).

## Baseline source identities

All six physical byte copies in `docs\plans\021_random_civil_war_plans\probability_snapshots\registered_footprint_before_2026-10-07` matched the parent-supplied SHA-256 values. A final recheck found the six current logical source files still byte-identical to those copies. The supplementary source identities and hashes are in the fixture JSON. Those supplementary files do not have physical before copies in the named snapshot folder.

The probability sources and identifiers reviewed were:

| Logical source | Identifiers and role |
| --- | --- |
| `common\scripted_effects\021_random_civil_war_parent_effects.txt` | `event021_parent_find_event6_package`, `event021_parent_select_archetype`, `event021_parent_prepare_target`, `event021_parent_score_anchor_state`, `event021_parent_add_target_to_selection_pool`, `event021_parent_append_front_plan_row`, and the Evolution I-III MTTH sampling sites. |
| `common\scripted_effects\021_random_civil_war_dynamic_front_candidate_effects.txt` | `event021_parent_append_dynamic_event6_front_candidate` and `event021_parent_collect_dynamic_event6_front_candidates`. The current Event 006 appender records its anchor with state count one. |
| `common\scripted_triggers\021_random_civil_war_parent_triggers.txt` | `event021_parent_event6_dormant_candidate`. |
| `common\scripted_triggers\021_random_civil_war_triggers.txt` | `random_civil_war_event6_route_valid`, `random_civil_war_has_valid_actor_route`, and automatic target admission. |
| `common\scripted_effects\021_random_civil_war_effects.txt` | `event021_prepare_archetype_weights` and `event021_random_civil_war_prepare_target`. |
| `common\scripted_triggers\006_independence_wave_event021_adapter_registry_triggers.txt` | `independence_wave_event021_dormant_package_available`. |
| `common\scripted_effects\006_independence_wave_event021_adapter_registry_effects.txt` | `independence_wave_initialize_event021_adapter_registry`, static package-to-actor mapping, and `independence_wave_release_event021_adapter_actor`. |
| `common\scripted_triggers\006_independence_wave_package_triggers.txt` | `is_independence_wave_dormant_country_scope`, used by the package admission table. |
| `common\scripted_triggers\021_random_civil_war_evidence_triggers.txt` | `random_civil_war_has_live_event6_evidence`, which can set the Event 006 route-ready flag from active evidence, strength, and expiry date. |
| `common\mtth\021_random_civil_war_mtth.txt` | `random_civil_war_evolution_i_days`, `random_civil_war_evolution_ii_days`, and `random_civil_war_evolution_iii_days`. |
| `common\scripted_triggers\021_random_civil_war_successor_triggers.txt` | `event021_evolution_has_active_event6_actor`, the Evolution II Event 006 modifier gate. |
| `common\scripted_effects\individual_crisis_targeting_effects.txt` and `common\scripted_triggers\individual_crisis_targeting_triggers.txt` | Shared candidate-ticket adjustment and load calculation used by the target ticket array. |
| `common\script_constants\021_random_civil_war_constants.txt`, `common\script_constants\021_random_civil_war_regional_constants.txt`, and `common\script_constants\individual_crisis_targeting_constants.txt` | Target score, anchor score, MTTH factors, ticket scaling, ticket load factors, and caps. |
| `events\021_random_civil_war.txt` | Hidden root `chaosx.nr21.1`, whose immediate dispatch calls `event021_parent_dispatch_opening`. The root itself has no options. |

The deterministic Event 006 package array contains 32 IDs: `iw_001`, `iw_002`, `iw_004`, `iw_006`, `iw_007`, `iw_008`, `iw_009`, `iw_010`, `iw_012`, `iw_014`, `iw_017`, `iw_018`, `iw_019`, `iw_023`, `iw_024`, `iw_026`, `iw_027`, `iw_028`, `iw_029`, `iw_030`, `iw_031`, `iw_033`, `iw_038`, `iw_040`, `iw_041`, `iw_044`, `iw_045`, `iw_070`, `iw_071`, `iw_072`, `iw_173`, and `iw_184`.

## Weighted surface traces

The archetype selector is `event021_parent_select_archetype` in `common\scripted_effects\021_random_civil_war_parent_effects.txt:1325-1335`. Its `random_list` has six candidates in this order: ideological, legal, regional, Event 006, command, and same-tag. `event021_prepare_archetype_weights` initializes each route weight to `random_civil_war_target_weight.minimum` and changes a route to `random_civil_war_target_weight.valid_actor_route` only when its route trigger is true. The source constants are zero and 80 respectively. These are raw `random_list` weights, not `ai_will_do` scores and not click probabilities.

The offline AI modding reference distinguishes `ai_will_do` score races from `ai_chance` proportional option sampling, while the Effects reference describes `random_list` as proportional effect selection by weight. The hidden root `chaosx.nr21.1` has no event options, so option `ai_chance` is outside this footprint slice. No separate AI-strategy-factor surface was found in the exact route-selection source closure.

For Event 006, `random_civil_war_event6_route_valid` accepts either `random_civil_war_event6_route_ready` or the conjunction of package admission and identity-adapter validity. The route-ready flag is recomputed from current route evidence, including `random_civil_war_event6_evidence_active`, minimum evidence strength, and the evidence expiry date. The package branch separately requires a dormant package and an owned, controlled, populated, infrastructured registered anchor. The current admission predicate does not enumerate every source-owned carrier core, uncontrolled core, current source capital, or complete transfer set.

The exact six-branch `probability_inspect` returned `poolComplete = true`, six candidates, and six required route-weight inputs. The full-source inspection reported 13 entries across separate random lists and was incomplete. The six-candidate evaluation for `RF_SCO_PRIMARY` returned six unresolved route weights. It returned no numerical ranking or normalized shares. The analyzer generated ranking, matrix, and unresolved visual artifacts, but the ranking view contains unresolved weights and establishes no candidate order.

Target selection has a separate score and ticket path. `event021_random_civil_war_prepare_target` starts from base 10, scales fracture pressure by 4, adds 90 for failing authority, 160 for collapsed authority, 80 when any actor route is valid, 50 for a major with major severity allowed, 60 for nearby conflict exposure, negative 120 for recent civil-war memory, 20 for subject status, and 25 for a player target. A major target then receives factor 0.35. Non-candidates and reserved targets are set to the zero minimum, and the result is clamped from 0 through 1000.

`event021_parent_add_target_to_selection_pool` divides that target score by 25, rounds it, clamps the ticket count from 1 through 40, applies the shared individual-crisis ticket rule, and inserts the target scope that many times. `random_scope_in_array` later draws from this repeated-scope array. Source tracing establishes the ticket construction, while an exact probability requires the complete due target set, each candidate score, active-crisis load, capacity and reservation state, and the full target pool. `custom_weighted_pool` inspection of the parent effects returned zero candidates and `poolComplete = false`, so the analyzer did not model this pool.

`event021_parent_find_event6_package` is a deterministic, rotating first-valid scan of the complete 32-ID package array. It wraps a persistent cursor, skips reserved package IDs, loads each candidate's registered anchor and package preflight, then accepts the first candidate whose anchor is currently owned and controlled by the host, meets population and infrastructure gates, is not the source capital, and is not reserved or already used by another front. It does not use probability-proportional package selection. Its current candidate test does not prove the full native release footprint.

The parent dynamic Event 006 appender records only the selected anchor and increments the state count once. This is inconsistent with the native `release = TAG` footprint established by source references, which transfers every source-owned state cored by the released carrier, including uncontrolled ownership. The candidate can therefore reach the 0-or-80 Event 006 archetype branch on an anchor check while the complete native transfer set is unsafe or larger than the stored row.

The anchor scorer `event021_parent_score_anchor_state` starts at 10, adds population tier, civilian factory, military factory, infrastructure, supply node, naval base, coastal, host-core, and capital values, then clamps to 1 through 100 and rounds. The exact constants are in the fixture identity record. The score is a deterministic score, not a selection probability. Dynamic front code stores it beside candidate rows. The opening allocator uses weighted shares for ordinary optional claimant rows. The Event 006 carrier actor type follows a distinct package path, so its stored anchor score is not used as an ordinary-claimant share in the current allocation branch.

The custom MTTH entries are sampled when a stage delay is assigned, clamped by the existing 60-to-180-day constants, and stored as due dates. Evolution II has base 135 days and an Event 006 factor of 0.80 when `event021_evolution_has_active_event6_actor` finds a registered, active, same-crisis Event 006 opposition actor still at war with its immediate opponent. Its other factors are border exposure 0.75, sponsor 0.75, multifront 0.85, settlement 1.40, strong neighbor 1.25, and no exposure route 1.25. Evolution I has base 90 days and Evolution III has base 120 days. The `event_mean_time_to_happen` adapter found zero weighted surfaces in the custom MTTH file, so no effective delay or timing distribution is claimed. This is a stored-delay scheduler, not a native daily event MTTH hazard.

The offline wiki describes `release` as making a free nation and transferring all target-core states, including states the source owns but does not control, while removing source cores on transferred states. Installed `effects_documentation.md:5724-5732` describes `release` as creating a puppet using owned states. The subject status conflicts. Transfer footprint evidence is source-backed, but native release behavior remains unresolved without runtime evidence.

## Scenario completeness and results

Only `RF_SCO_PRIMARY` was sent to the evaluator. Its schema-accepted payload binds actor ENG and `ROOT` to ENG. It does not bind the declared SCO cores, anchor, owner/controller state roles, capital, remnant, route flags, package reservations, or cursor. The other seven fixture definitions remain in the immutable JSON with their declared roles and exact missing bindings.

| Scenario | Declared source and package roles | Candidate-pool completeness | External-factor completeness and classification |
| --- | --- | --- | --- |
| `RF_SCO_PRIMARY` | ENG, package `iw_001`/SCO, anchor 121, source-owned SCO cores 120, 121, 133, 136, 933, source capital 126. | The six archetype entries and 32 registered package IDs are source-complete. The runtime target ticket pool is not complete. | Partial schema binding only. Six route weights, package eligibility, state owner/controller/core roles, source remnant, reservations, actor identity, and current world are unresolved. Full-pool result is unresolved, with six missing route-weight values. |
| `RF_WLS_PRIMARY` | Package `iw_002`/WLS, registered anchor 122. The actual count is derived only if 122 is the complete current footprint. | Registered package IDs are complete. Scenario-specific candidate eligibility is unresolved. | Source country, full current WLS core set, owner/controller, source capital, remnant, and route state are unspecified. Unresolved. |
| `RF_MULTI_OPTIONAL_RHI_AJX` | RHI package `iw_008`, anchor 51, cores 42 and 51, overlapping AJX package `iw_010`, anchor 42. | Registered package IDs are complete. Cross-package state conflict is declared, but current target pool is not. | Current owner/controller, source capital/remnant, reservations, other active rows, and living identity are unspecified. Unresolved. |
| `RF_MULTI_OPTIONAL_TRA` | TRA package `iw_023`, anchor 84, source-owned TRA cores 76, 82, 83, 84, 764. | Registered package IDs are complete. Current target pool is not. | Owner/controller, source capital/remnant, occupation, reservations, and current row capacity are unspecified. Unresolved. |
| `RF_CAPITAL_OVERLAP` | Source capital is placed in a non-anchor native core. No package or concrete state is named. | Static package registry complete. Fixture target identity unresolved. | Exact package, state, source country, owner/controller, and capital binding absent. Unresolved. |
| `RF_OCCUPIED_CORE` | A source-owned uncontrolled carrier core is third-party occupied, with a separate same-crisis occupant case. | Static package registry complete. Fixture target identity unresolved. | Exact state, controller, source and crisis identities, core roles, and held-resource state absent. Unresolved. |
| `RF_ORIGINAL_TAG_REUSE` | Original tags AFX, AGX, AJX, ARX, ASX, and HBX each require one registered living original-tag actor with the static tag absent. | Static package registry complete. Living actor set is not bound. | Current actor tags, `original_tag` values, registry rows, package provenance, and baseline actor territory/content absent. Unresolved. |
| `RF_FROZEN_CURRENT_WORLD` | After-freeze core, owner/controller, capital, and recipient changes must reject stale consumption. | Static package registry complete. Transition candidate set is not represented. | The accepted scenario schema has no temporal state-transition or receipt-nonce fields. Unresolved. |

The live schema accepted only actor, flat state values, flags, and scope entries containing an id and state. No typed state scope was accepted in this audit. No `candidateOverrides` were sent. The empty state and flags in the one accepted payload do not establish that any eligibility predicate is true or false.

## Validity, dominance, starvation, and repetition

The current source has a positive Event 006 route weight whenever its route predicate passes, but the registered dormant-package trigger checks the anchor and dormant-carrier preflight rather than the complete native transfer set. This is a source-backed risk that an unsafe multi-state footprint can receive positive route weight. It is not a measured campaign selection probability.

No dominance, starvation rate, rank reversal, repetition rate, or snowball rate was measured. The six route weights are unresolved in the complete archetype pool. The runtime target ticket pool is not exposed by the custom weighted-pool adapter. A rank reversal is possible if adding or removing the Event 006 branch changes which route has the highest or sole positive weight, but the other five route-validity values are absent. The unsafe-footprint mismatch also presents a source-level snowball risk because native release can move more territory than the anchor-only front and resource receipts currently represent.

The package scan itself is deterministic. Its cursor advances past each scanned package and the loop stops at the first accepted candidate. If the owner adds full-footprint validation after the finder marks a package found, a rejected first package could prevent later valid packages from being considered in that transaction. Put full footprint validation inside the candidate admission predicate, before the found result and reservation, and continue scanning after a rejection. Preserve the 32 registered packages and cursor order.

The shared candidate-ticket helper caps active crisis load at three and applies four, two, or one tickets at derived load zero, one, or two. The load trigger counts the listed active crisis providers, including an active Event 021 crisis. This is a source trace only. Because the complete due-target set and each country’s live load are absent, no repetition or starvation conclusion follows.

## Recommended owner changes

Before setting a candidate found or reserving it, calculate and validate the exact native core set and authorized explicit anchor transfer for that package. Include uncontrolled source-owned carrier cores, current owner/controller and core roles, source capital, protected remnant, capacity and reservation conflicts, and exact living-recipient mode. Make the route weight become positive only after this full eligibility proof, while keeping existing numeric weights and the 32-ID package pool unchanged.

Store the complete verified transfer membership and aligned owner/controller/core snapshots in primary, optional, active, and frozen receipts. A failed package footprint must continue the cursor scan without charging state, actor, capacity, or resource receipts. Keep larger registered packages eligible when their exact footprint passes. The RHI/AJX overlap and TRA five-core cases must reject or pass on the actual state set, not on anchor count.

After the owner patch, rerun inspect and evaluate with this same fixture file and scenario hash. Compare real saved before bytes against actual after source paths. Do not compare current source with itself. Keep the complete six-route archetype pool and declare the missing route/campaign inputs where the adapter supports them. If the adapter still cannot bind typed state roles or route flags, keep the probability conclusion unresolved and retain the exact tool diagnostic.

## Skipped analyses and remaining uncertainty

`probability_sweep` was called for `var:event021_event6_weight` under `RF_SCO_PRIMARY` and returned `PROBABILITY_SWEEP_RANGE_REQUIRED`. The connected route required a scenario range, numeric alternatives, or a numeric state value. No numeric override was supplied because it would not establish live footprint eligibility, and the full route pool remains unresolved.

`probability_compare` is deferred until the owner applies the footprint patch. `probability_simulate` was not appropriate without declared uncertain-input distributions and seeds. `probability_sequence` was not appropriate because Event 006 package choice is a deterministic first-valid scan and no custom-pool cadence/transition manifest was declared.

The focused `event_inspect` and `event_render` calls returned partial graphs with zero indexed helpers, one blocking diagnostic, 10,447 unresolved nodes, and 45,968 omitted render nodes. They do not certify Event 021 lifecycle behavior. The linked trace and unresolved render are retained in the MCP evidence file.

Native release behavior, state rollback, package initialization side effects, exact map topology, current owner/controller state, living original-tag actor resolution, full target-country candidate coverage, and runtime force/resource allocation remain unresolved. The analyzer did not provide a numeric normalized probability for any named footprint fixture.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-mtth`. No skill was created or updated.
