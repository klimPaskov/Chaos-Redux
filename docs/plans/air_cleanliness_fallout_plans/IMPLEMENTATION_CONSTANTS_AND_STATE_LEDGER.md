# Implementation Constants and State Ledger

## Naming policy

Use short subsystem names without unnecessary project prefixes. The proposed names below are implementation labels, not final player-facing localisation.

Shared values belong in `common/script_constants/`. Values that must be injected into unsupported static fields may use file-local `@` constants or verified meta effects. Do not duplicate threshold tables across events, decisions, GUI, and effects.

## Global Air state

Existing values to preserve:

| Name | Role | Lifecycle |
| --- | --- | --- |
| `global.air_contamination_bp` | global contamination in basis points | persistent |
| `global.air_contamination_monthly_delta_bp` | last monthly net change | refreshed monthly |
| `global.air_contamination_chaos_buffer_bp` | sub-one-percent Chaos conversion remainder | persistent |
| `global.air_contamination_chemical_states` | current chemical-state count | refreshed monthly |
| `global.air_contamination_irradiated_states` | current nuclear fallout state count | refreshed monthly |
| `global.air_contamination_irreversible` flag or equivalent | contamination floor and terminal ecological decline | persistent after trigger |

New global values:

| Proposed name | Type | Role | Reset rule |
| --- | --- | --- | --- |
| `global.air_winter_generation` | variable | serial number for a new winter cycle | increments when a new global winter cycle begins |
| `global.air_winter_peak_phase` | variable | highest state phase currently present | refreshed monthly |
| `global.air_winter_active_state_count` | variable | states at phase 1 or above | refreshed monthly |
| `global.air_winter_severe_state_count` | variable | states at phase 4 or above | refreshed monthly |
| `global.air_winter_terminal_state_count` | variable | states at phase 6 | refreshed monthly |
| `global.air_winter_population_exposed` | variable | population in active winter states | refreshed monthly |
| `global.air_winter_global_pressure` | variable | global forcing used by each state | refreshed monthly |
| `global.air_winter_recovery_pressure` | variable | global recovery force | refreshed monthly |
| `global.air_winter_flavour_serial` | variable | prevents duplicate incident presentation | increments per incident |
| `global.air_winter_last_summary_date` | variable | controls summary event cadence | updated on summary |
| `global.fallout_eligibility_pressure` | variable | post-100-percent gradual trigger pressure | refreshed monthly |
| `global.fallout_request_source` | variable | cause enum for current request | set on request, cleared after transition or abort |
| `global.fallout_request_intensity` | variable | severity input from caller | set on request |
| `global.fallout_request_date` | variable | audit and countdown date | set on request |
| `global.fallout_transition_phase` | variable | blackout and rewrite state | set during transition, cleared after finish |
| `global.fallout_transition_dirty` | variable | scripted GUI update marker | increment on visible phase change |
| `global.fallout_rewrite_batch_index` | variable | persistent batch cursor | cleared on completion |
| `global.fallout_rewrite_error_count` | variable | safety counter for failed assignments | cleared on completion |
| `global.fallout_surviving_country_count` | variable | final survivor count | set after rewrite |
| `global.fallout_successor_country_count` | variable | final new successor count | set after rewrite |

Global flags:

| Proposed flag | Role | Clear rule |
| --- | --- | --- |
| `air_winter_active` | at least one state has winter phase | clear when no active state remains |
| `air_winter_severe_global` | severe share threshold reached | clear when share falls below hysteresis floor |
| `fallout_eligible` | normal contamination route may roll Fallout | clear only if reversible model allows contamination below threshold and no irreversible state exists |
| `fallout_requested` | a valid request is waiting | clear on transition start or abort |
| `fallout_transition_active` | player input locked by blackout | clear only after transition finish or recovery abort |
| `fallout_processing_states` | state grade and damage pass active | clear after state pass |
| `fallout_processing_countries` | country rewrite pass active | clear after country pass |
| `fallout_player_choice_required` | player needs successor selection | clear after valid choice or deterministic timeout choice |
| `fallout_active` | post-rewrite Fallout campaign mode | persistent |
| `world_end` | ordinary event system terminal guard | set at transition lock and retained |
| `world_end_fallout` | Fallout terminal branch marker | persistent |
| `fallout_manual_scenario_active` | manual launch owns the current request | clear after transition begins |
| `fallout_synthetic_strike_batch` | suppresses per-strike log and diplomatic spam | clear immediately after strike pass |

## Transition ledger schemas

| Ledger | Live schema | Contract |
| --- | --- | --- |
| Fallout world transition | 4 | fail-closed save recovery and phase ownership |
| Government classifier | 1 | frozen-input signal aggregation and provisional archetype |
| Successor pre-allocation inventory | 1 | live countries, possible-country scopes, states, reservations, and package conflicts |
| Successor allocation output | 1 | consumed source receipt, unique assignments, package layers, conflicts, capitals, and cleanup |
| Manual province sweep runtime | 2 | generation-bound batch, verifier, and exact seven-day callback provenance |

## State winter values

| Proposed name | Type | Range | Role |
| --- | --- | --- | --- |
| `air_winter_phase` | variable | 0 to 6 | visible state phase |
| `air_winter_pressure` | variable | 0 and above | current monthly escalation force |
| `air_winter_exposure` | variable | 0 to configured cap | persistent cumulative exposure |
| `air_winter_phase_months` | variable | 0 and above | consecutive months in current phase |
| `air_winter_recovery_months` | variable | 0 and above | consecutive months with recovery force above escalation |
| `air_winter_adaptation` | variable | 0 to 100 | shelter, governance, food, and infrastructure adaptation |
| `air_winter_monitoring` | variable | 0 to 3 | forecast and tooltip precision |
| `air_winter_food_reserve` | variable | 0 to configured cap | local survival stock |
| `air_winter_shelter_capacity` | variable | 0 to configured cap | protected population and administration |
| `air_winter_category_damage` | variable | 0 to configured cap | sustained category degradation progress |
| `air_winter_building_damage_pressure` | variable | 0 to configured cap | bounded building loss progress |
| `air_winter_population_loss_memory` | variable | 0 and above | cumulative winter deaths for map and events |
| `fallout_state_grade` | variable | 0 to 5 | monotonic physical-damage severity class |
| `fallout_state_subtype` | variable | 0 to 1 | separate fictional altered-biosphere overlay |
| `fallout_survival_value` | variable | 0 to 100 | independent continuation and successor viability ledger |
| `fallout_state_survival_value` | variable | 0 to 100 | successor viability and player choice score |
| `fallout_state_direct_strike_count` | variable | 0 and above | manual or live direct-strike memory |
| `fallout_state_cause_mask` | variable or flags | implementation-defined | cause memory for regional content |
| `fallout_pretransition_air_winter_original_category` | variable | Air Winter category enum | frozen category memory for Fallout classification |

State flags:

| Proposed flag family | Role |
| --- | --- |
| `air_winter_phase_1` through `air_winter_phase_6` | optional cached flags if phase comparisons are too expensive in modifier triggers |
| `air_winter_original_category_*` | remembers original category band before permanent degradation |
| `air_winter_recent_phase_change` | gates phase-change flavour and map emphasis |
| `air_winter_recent_building_loss` | prevents repeated incident spam |
| `air_winter_recent_population_crisis` | prevents repeated incident spam |
| `air_winter_relief_route_active` | current foreign or treaty relief project |
| `air_winter_evacuation_active` | current local evacuation action |
| `fallout_state_processed` | state rewrite completed |
| `fallout_state_reserved_for_player` | cannot be assigned away before player handoff |
| `fallout_state_wasteland` | terminal uninhabitable class |
| `fallout_state_mutant_candidate` | fictional high-chaos package may use this region |

Do not store true or false state as numeric variables unless an engine surface requires it.

## Country Fallout values

| Proposed name | Type | Role |
| --- | --- | --- |
| `fallout_country_survival_score` | variable | determines survival, fracture, or extinction |
| `fallout_country_legitimacy` | variable | starting government cohesion |
| `fallout_country_food_security` | variable | starting survival loop |
| `fallout_country_shelter_network` | variable | population protection and recovery |
| `fallout_country_command_cohesion` | variable | military package quality |
| `fallout_country_science_capacity` | variable | research and decontamination route |
| `fallout_country_mutation_pressure` | variable | fictional high-chaos route value |
| `fallout_country_origin_archetype` | variable | archetype enum |
| `fallout_country_region_overlay` | variable | regional enum |
| `fallout_country_memory_overlay` | variable | memory package enum |
| `fallout_country_package_version` | variable | migration and audit version |
| `fallout_government_archetype` | variable | provisional classifier identity and later final package identity |
| `fallout_government_classifier_generation` | variable | binds classification to the active transition |
| `fallout_government_classifier_schema_version` | variable | binds classification to classifier schema 1 |
| `fallout_successor_assignment_generation` | variable | binds the final assignment row to the active transition |
| `fallout_successor_conflict_result` | variable | records the reviewed tag-conflict outcome |
| `fallout_successor_cleanup_owner` | scope variable | records the country that owns assignment cleanup |

Country flags:

- `fallout_surviving_old_government`
- `fallout_successor_country`
- `fallout_warlord_country`
- `fallout_mutant_country`
- `fallout_refuge_government`
- `fallout_technical_enclave`
- `fallout_agricultural_survivor`
- `fallout_maritime_survivor`
- `fallout_bunker_regime`
- `fallout_country_package_applied`
- `fallout_focus_tree_loaded`
- `fallout_player_candidate`
- `fallout_ai_package_initialized`

Actual archetype flags should follow the final accepted archetype identifiers from the matrix.

## Cause enum

Proposed stable enum values:

| Value | Cause |
| --- | --- |
| 1 | gradual Air Contamination collapse |
| 2 | concentrated nuclear exchange |
| 3 | Final Silence or another scripted terminal strike |
| 4 | chemical atmosphere collapse |
| 5 | biological and agricultural systems collapse |
| 6 | manual Fallout scenario |
| 7 | mixed or unknown terminal cause |

The enum affects state grading, regional flavour, successor package weighting, achievements, and post-rewrite memory. It does not replace detailed cause flags when several causes coexist.

## Winter phase enum

| Phase | Working implementation label | Mechanical identity |
| --- | --- | --- |
| 0 | clear | no active winter pressure |
| 1 | dimming | visibility, aviation, and local confidence begin to fail |
| 2 | crop shock | agriculture, food reserves, and rural stability decline |
| 3 | hard freeze | supply, construction, repairs, and population health deteriorate |
| 4 | black harvest | severe population loss, building decay, and migration pressure |
| 5 | ash winter | state category damage, industrial collapse, and warlord pressure |
| 6 | terminal winter | wasteland conversion risk and direct Fallout trigger pressure |

These are working labels only. Final player-facing names are written during implementation after localisation research and UI fit checks.

## State grade enum

| Grade | Working label | Rewrite role |
| --- | --- | --- |
| 0 | intact enclave | old government or strong successor can survive |
| 1 | damaged administration | state remains governable with severe penalties |
| 2 | fractured zone | local successor or contested ownership likely |
| 3 | collapse belt | warlord, commune, military district, or refuge package likely |
| 4 | dead infrastructure | sparse survivor identity, technical enclave, or abandoned ownership |
| 5 | irradiated wasteland | no normal state package, special access and salvage only |
| 6 | terminal exclusion zone | sealed wasteland with extreme entry and population rules |

## Lifecycle invariants

1. A state has one visible winter phase at a time.
2. Phase changes use hysteresis. A single good month cannot instantly erase a severe phase.
3. Exposure can remain high while phase falls.
4. Category damage never progresses without sustained severe exposure.
5. A category can only degrade one step per configured minimum interval.
6. Population loss is registered once through the shared death pipeline.
7. Every Fallout state is processed exactly once per transition version.
8. Every active successor receives exactly one country package version.
9. No player state is transferred before player-continuation reservation is resolved.
10. Transition flags and cursors survive save-load.
11. Any abort path clears the blackout and leaves the pre-transition world intact or reports an unrecoverable blocker.
12. Manual synthetic strikes suppress repeated global event logs and apply one aggregate history entry.
