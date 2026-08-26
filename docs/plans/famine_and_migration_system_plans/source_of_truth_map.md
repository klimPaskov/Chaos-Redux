# Famine and Migration Source-of-Truth Map

Status: current split-source map. This document does not itself certify completion.

## Authority order

1. `docs/specs/famine_and_migration_system_specs/` contains the binding eight-part design, prompts, matrices, routing, bibliography, and closure review.
2. Famine implementation is owned by `famine_*` files and identifiers.
3. Migration implementation is owned by `migration_*` files and identifiers.
4. Exact physical civilian movement is owned by `civilian_transfer_*`; humanitarian corridors, shared scheduling/validation, and achievement infrastructure may use narrow neutral `humanitarian_*` names.
5. `docs/systems/famine_system.md`, `docs/systems/migration_system.md`, and `docs/systems/civilian_transfer_system.md` are permanent mechanic documentation.
6. `namespace_separation_validation.md` records the zero-match runtime namespace audit and the historical-document exception.
7. `event_free_validation.md` records source absence plus the partial negative-selector event inspect/render artifacts for the two forbidden incident IDs and Event 149 replacement ID.
8. `handoff_dispositions.md` records one disposition for each reviewed handoff file. Historical handoff identifiers are not current APIs.
9. `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable catalog source; the three CSV files are exports only.

## Famine mechanic

| Surface | Canonical source | Contract |
| --- | --- | --- |
| Constants and tuning | `common/script_constants/famine_core_constants.txt`, `famine_adapter_constants.txt`, `famine_decision_constants.txt`, `famine_mission_constants.txt`, `famine_relief_constants.txt`, `famine_opposition_constants.txt` | Food-stage thresholds, component weights, mortality, reserves, relief, AI, opposition, and bounded scheduling. |
| Core state model | `common/scripted_effects/famine_core_effects.txt`, `common/scripted_triggers/famine_core_triggers.txt` | Dynamic Food Security, five stages including stable, reserves, blockade proof, mortality, historical profiles, and sparse state lifecycle. |
| Decisions and category | `common/decisions/famine_decisions.txt`, `common/decisions/categories/famine_decision_category.txt` | Independently hidden/revealed famine category and famine-only actions/missions. |
| Relief and opposition | `common/scripted_effects/famine_relief_effects.txt`, `famine_opposition_effects.txt` and paired trigger files | Donor-backed conservative relief and bounded catastrophic-famine political responses. |
| Adapters | `common/scripted_effects/famine_adapter_effects.txt` | Food-security inputs and exact famine-owned mortality contexts only. |
| Presentation | `common/dynamic_modifiers/famine_state_modifiers.txt`, `common/scripted_localisation/famine_scripted_localisation.txt`, `localisation/english/famine_l_english.yml` | Food Security primary value, Food Reserves, Relief Access/recovery direction, famine phases, reports, and tooltips. |
| Report carrier | `common/scripted_guis/famine_report_header_scripted_gui.txt`, `interface/famine_report_header.gui`, `common/scripted_effects/famine_report_effects.txt`, `interface/famine_report_pictures.gfx` | Compact famine-owned category header; not a shared full scripted GUI. |
| Mapmode | `famine_state_map_mode` in `common/map_modes/chaosx_state_map_modes.txt` | Always available map explanation of food stage and famine-owned complementary status. |

## Migration mechanic

| Surface | Canonical source | Contract |
| --- | --- | --- |
| Constants and tuning | `common/script_constants/migration_core_constants.txt`, `migration_adapter_constants.txt`, `migration_decision_constants.txt`, `migration_mission_constants.txt`, `migration_destination_selection_constants.txt`, `migration_custody_constants.txt`, `migration_presentation_constants.txt` | Cohorts, load/capacity/policy, routes, movement, reception, return, custody, and AI tuning. |
| Core cohort model | `common/scripted_effects/migration_core_effects.txt`, `common/scripted_triggers/migration_core_triggers.txt` | Sparse aligned cohorts, current-host identity, flight/trapped obligations, reception, integration, resettlement, voluntary/forced return, and retirement. |
| Decisions and category | `common/decisions/migration_decisions.txt`, `common/decisions/categories/migration_decision_category.txt` | Independently hidden migration category revealed only by repeated, large, or sustained live migration evidence; durable resettlement/return history cannot reopen it. |
| Destination and movement | `migration_destination_selection_*`, `migration_spontaneous_movement_*`, `migration_forced_movement_*` | Safe weighted destination choice, bounded ideology, exact movement requests, and responsible-actor receipts. |
| Capacity and policy | `migration_capacity_effects.txt`, `migration_decision_owner_effects.txt`, `migration_decision_phase_effects.txt` and paired triggers/docs | Live reception capacity and separate internal departure/reception policy behind one player-facing Border Policy. |
| Persecution and custody | `migration_persecution_effects.txt`, `migration_adapter_effects.txt` and paired triggers | Exact owner projections only; ideology, war, site presence, or quotas are not persecution proof. |
| Presentation and history | `migration_presentation_effects.txt`, `migration_cohort_history_effects.txt`, `common/dynamic_modifiers/migration_state_modifiers.txt`, `common/scripted_localisation/migration_scripted_localisation.txt` | Displacement Load primary value, Reception Capacity and Border Policy support, phase modifiers, endpoint projections, and visit-cycle prevention. |
| Report carrier | `common/scripted_guis/migration_report_header_scripted_gui.txt`, `interface/migration_report_header.gui`, `common/scripted_effects/migration_report_effects.txt`, `interface/migration_report_pictures.gfx` | Compact migration-owned category header; not shared with famine. |
| Mapmode | `migration_state_map_mode` in `common/map_modes/chaosx_state_map_modes.txt` | Always available migration lifecycle/load map; it does not render famine relief as migration state. |

## Neutral shared primitives

| Surface | Canonical source | Boundary |
| --- | --- | --- |
| Exact transfer | `common/scripted_effects/civilian_transfer_effects.txt`, `common/scripted_triggers/civilian_transfer_triggers.txt`, `common/script_constants/civilian_transfer_constants.txt` | Origin debit equals route deaths plus survivor credit plus restored residual. Movement is never itself a Deaths cause. |
| Humanitarian corridor | `common/scripted_effects/humanitarian_corridor_effects.txt`, paired triggers/constants | Exact route contract usable by famine relief and migration evacuation without merging their ledgers or categories. |
| Runtime scheduler | `common/scripted_effects/humanitarian_runtime_effects.txt`, `common/on_actions/humanitarian_runtime_on_actions.txt` | Dispatches only registered famine states and migration states/countries; no recurring whole-world scan. |
| Validation | `common/scripted_triggers/humanitarian_validation_triggers.txt` | Narrow shared state/country validity and nonhuman exclusions. |
| Achievements | `common/scripted_effects/humanitarian_achievement_effects.txt`, paired triggers/constants, `common/achievements/chaos_redux_achievements.txt` | Eight stable achievement IDs with exact famine or migration predicates and shared one-time framework. |

## Explicit connection seams

Famine and migration connect only through causally proven calls:

- famine stage/mortality may submit a survivor-based migration pressure request after the famine transaction;
- famine publishes a versioned, fail-closed destination food-safety projection that migration consumes only for registered reception states and bounded adjacent candidates;
- migration publishes trapped-population reception demand with an exact amount, cause, schema, generation, revision, and proof; famine consumes only its validated famine-owned copy;
- famine evacuation crosses migration-owned availability, trapped-obligation, cohort-staging, exact-transfer, and mission-finalization seams; famine consumes only the neutral transaction receipt;
- migration and evacuation may otherwise alter famine need, production, transit, or relief components only through exact state/cohort receipts;
- a humanitarian corridor may carry famine relief or migration evacuation through separate action receipts;
- shared achievements may observe both mechanics without owning their simulation.

No category, registry, stage variable, primary player value, cleanup path, or mapmode is combined.

The famine registered-state job and retirement trigger contain no migration reconciliation, migration category refresh, migration obligation gate, or migration cleanup call. The migration job retains sole ownership of cohort reconciliation and ordinary migration retirement. A valid state leaving migration displacement uses migration-local cleanup; the neutral dual-owner cleanup wrapper is used only when the physical state itself is invalid.

The former migration `safe_food_reserve_donor` weighted pool was removed because it had no runtime caller and duplicated famine ownership. General famine relief retains the foreign-donor `famine_relief_select_donor` pool. The same-country safer-state requisition uses the separate famine-owned `famine_select_safe_food_reserve_donor` selector, which deterministically chooses the adjacent safe state with the largest already existing positive reserve and does not initialize or fabricate candidates.

## Canonical player-facing value count

Famine has exactly three canonical player-facing values: Food Security, Food Reserves, and Relief Access.

Migration has exactly three canonical player-facing values: Displacement Load, Reception Capacity, and Border Policy.

Internal ledgers, conceptual components, receipts, generations, revisions, scheduler state, raw variables, flags, and temporary values explain implementation but are not additional player-facing mechanics.

## Historical profiles

The fifteen famine profile IDs are `hist_soviet_1932_memory`, `hist_china_henan_1942`, `hist_china_policy_famine`, `hist_bengal_1943`, `hist_vietnam_1944`, `hist_java_1944`, `hist_greece_1941`, `hist_leningrad_siege`, `hist_dutch_hunger_winter`, `hist_spain_early_1940s`, `hist_ireland_memory`, `hist_brazil_ceara`, `hist_congo_interaction`, `hist_ethiopia_policy`, and `hist_nuclear_winter_global`.

They select component profiles and historical memory; they do not inject fixed deaths or fixed migration totals.

## Assets and localisation

- Famine runtime sprites: `interface/famine_system.gfx`, `interface/famine_report_pictures.gfx`, `gfx/interface/decisions/famine/`, `gfx/interface/state_modifiers/famine/`, `gfx/event_pictures/famine/`, and famine achievement/texticon files.
- Migration runtime sprites: `interface/migration_system.gfx`, `interface/migration_report_pictures.gfx`, `gfx/interface/decisions/migration/`, `gfx/interface/state_modifiers/migration/`, `gfx/event_pictures/migration/`, and migration achievement/texticon files.
- Production evidence: the 50-row root `docs/assets/famine_and_migration_system/manifest.csv`, the seven-image report-art manifest, and the four-button mapmode manifest cover exactly 61 declared DDS assets. The category-asset closure reconciles all four category consumers into the authoritative root manifest; source, processing, provenance, DDS round-trip, and parent contact-sheet review are complete, while live runtime consumer validation remains user-owned. This historical package directory is not a runtime namespace.
- English localisation: separate famine, migration, mission, humanitarian-cost, and humanitarian-achievement files, all with runtime names aligned to their owning mechanic or the approved narrow neutral infrastructure.

## Event 149 and event boundary

Event 149 `Immigrations` has no competing gameplay source. The workbook marks it retired, absorbed into migration, and unavailable. No replacement ID, event-pool registration, event log row, evolution, or pacing weight is permitted.

Famine and migration state pulses are scheduled system jobs and must never be counted as event pacing.

`famine_register_initial_incident` and `migration_register_initial_incident` are accounting and presentation seams only. They select bounded report/state presentation after proven transitions and do not create event objects, event IDs, event-pool entries, event-log rows, random events, or pacing pulses; state/accounting pulses do not count as event pacing. `events/famine_incidents.txt`, `events/migration_incidents.txt`, and their constants were deliberately deleted, and every earlier incident-event or incident-option probability claim is superseded.

Events 118, 120, and 131 are separate missing external owners, not famine or migration event IDs. A current-tree and Git-object recovery pass found no authoritative root scripts, and the catalog marks all three unavailable. Event 013's volcanic families are an already connected natural-disaster owner, while Event 019's General Mutiny is a separate manual scenario; neither is an alias for a missing numbered event. No adapter may fabricate those roots or reuse dispatcher identity, scenario intensity, current occupation-law reads, bombing recency, or country war/peace state as an exact people receipt.

## Evidence limits

- The fresh isolated `chaosx_ai_probability_auditor` routes parsed complete declared source lists of 10 famine and 18 migration decision/mission candidates at the current source revision. Final-source flat-fact matrices cover 40 famine rows with 15 unresolved and 198 migration rows with 60 unresolved, improving the historical counts of 23 and 77. A bounded probe proves that schema-valid `eventTargets = { FROM = "state:1" }` still does not bind the special decision target. The adapter is score-only and exposes neither normalized probability nor a time distribution, so no numeric balance certification is claimed.
- Destination, opposition, and relief-donor custom-pool inspections remain incomplete dynamic registries. The current destination surface has four live declared entries, the opposition surface has seven declared channels, and the relief-donor registry produced zero discovered dynamic candidates. Exact current artifacts, hashes, and historical partial traces are recorded in `ai_probability_current.md`.
- Owner-applied weighted changes have genuine distinct-path before/current evidence. The famine comparison found no modeled score delta with 46 unresolved items across four named scenarios; the migration comparison found the intended two corridor modifier changes across three scenarios, producing six comparison rows with 134 unresolved items and four information diagnostics. Later final-source flat-fact evaluations reduce current-evidence unresolved counts to 15 famine and 60 migration rows but do not replace the comparison. Provenance ambiguity is closed, while special/scoped trigger and complete-pool certification remain blocked.
- The exact state-control callback is not an occupation-pressure receipt. It exposes the changed state, old controller, new controller, and readable current occupation law, but not hostile-versus-peaceful/liberation cause, affected people, or replay identity. `state_control_occupation_adapter_0826.md` therefore retains cleanup/reassessment only and rejects both normalized profile points and whole-state population as fabricated request amounts.
- No current relief owner exposes a people-denominated obstruction receipt. Successful foreign and corridor relief measure reserve debit and credit; corridor rejection preserves route/cohort identity but lacks exact affected people and the full condemnation proof/revision/request envelope. `relief_obstruction_receipt_0826.md` rejects reserve units, trapped aggregates, evacuation amounts, survivors, and deaths as proxies and keeps `famine_condemn_relief_obstruction` fail-closed.
- The current completion re-audit found two undefined migration-side constant paths and the parent closed both without duplicating tuning: all eight corridor/destination route-damage gates use neutral `civilian_transfer_route_projection.damage_threshold`, while the destination-history loop uses shared `humanitarian_runtime.array_index_increment`. The post-patch census contains zero references to the undefined names.
- The installed map route validates map substrate, not dynamic scripted-mapmode branches.
- The current `MapmodesInterface_Ingame` GUI route inspected 101 elements and rendered the linked button-window layout at two resolutions and four presentation states. It cannot inject an active custom mapmode or execute state-scoped scripted colors and tooltips, so it is static layout evidence rather than dynamic mapmode or live click proof.
- The current probability auditor route completed with the adapter and fixture limitations above. Other requested specialist evidence and handoff dispositions remain recorded in `handoff_dispositions.md`.
