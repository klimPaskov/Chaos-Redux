# Air Cleanliness and Fallout source of truth map

Status: current implementation map, reconciled 2026-07-23. Fallout remains incomplete and dormant where the proof ledger says so.

## Authority order

1. Direct user constraints in the active task.
2. Accepted source specifications under `docs/specs/air_cleanliness_fallout_specs/`.
3. Accepted proposals and resolved plans under `docs/plans/air_cleanliness_fallout_plans/`.
4. Live repository code, assets, manifests, and localisation as implementation evidence.
5. Historical notes only when they do not contradict the sources above.

## Ownership boundaries

| Surface | Source of truth | Owned implementation path |
| --- | --- | --- |
| Air Contamination and natural smoke or ash pressure | `docs/systems/air_contamination_mechanic.md` and `AIR_CONTAMINATION_NATURAL_SOURCE_PROOF.md` | `common/scripted_effects/air_contamination_effects.txt`, `events/013_natural_disasters.txt`, Air constants, and Air UI |
| Air Winter phases and consequences | `docs/air_cleanliness_winter.md` and tranche proofs | `common/scripted_effects/air_winter_effects.txt`, Air Winter constants, decisions, mapmodes, and ordinary-map entities |
| Fallout request and transition | `FALLOUT_TRANSITION_ARCHITECTURE.md` and current status | `common/scripted_effects/fallout_world_end_effects.txt`, `common/scripted_triggers/fallout_world_end_triggers.txt`, and `events/fallout_world_end_events.txt` |
| Fallout event scheduler | `01_living_world_event_ecosystem.md`, `FALLOUT_EVENT_SCHEDULER_NUMERICAL_CONTRACT_PROPOSAL.md`, and `FALLOUT_EVENT_SCHEDULER_PROOF.md` | Fallout constants, coordinator effects and triggers, candidate registry, delayed queue, ordinary receipt, and dispatch envelope |
| Fallout event content | `fallout_event_library_master_matrix.md`, event id ledger, and accepted event specs | `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`, Fallout scripted content, event localisation, logs, and details |
| Reviewed global-survival pilot contract | `specs/13_reviewed_global_survival_pilots.md`, `specs/14_reviewed_global_survival_generation.md`, `specs/15_reviewed_global_survival_education.md`, `specs/16_reviewed_global_survival_institutions.md`, and the reviewed addenda | candidate 269, 282, 289, and 296 constants, registry rows, delayed effects, event blocks, Event Log histories, localisation, and dedicated asset packages |
| Manual Fallout scenario | `MANUAL_FALLOUT_SCENARIO_PLAN.md`, sweep proof, and population contract | manual scenario constants, sweep effects, scenario dispatch, and Fallout request handoff |
| Blackout presentation | `FALLOUT_BLACKOUT_GUI_PROOF.md` and super-event ownership reconciliation | Fallout scripted GUI, interface GFX, blackout events, dedicated Fallout audio, and Fallout asset manifests |
| Successor allocation and player continuation | `FALLOUT_SURVIVAL_NUMERICAL_CONTRACT_PROPOSAL.md`, transition architecture, and allocation proofs | transition ledgers, conflict inventory, package receipts, player reservation, allocation, and map-return validation |
| Country and focus packages | `fallout_successor_country_matrix.md`, `09_country_package_templates.md`, and focus-tree audit records | country history, flags, leaders, ideas, units, focuses, decisions, AI, localisation, and package manifests |

## Dedicated Fallout event ownership

All Fallout event definitions belong in `events/fallout_world_end_events.txt` under `chaosx.fallout`. Fallout is a terminal transition with its own blackout and scheduler. It is not an ordinary super-event. Zombie Apocalypse retains its own ids, files, assets, audio, sprites, and paths. New Fallout work must not borrow them.

The reviewed global-survival pilot currently includes Shelter Marriage Law candidate `303`, Black Start candidate `310`, First Streetlight candidate `317`, Working Elevator candidate `324`, Sealed Warehouse candidate `331`, Dead City Permit candidate `338`, Manual Nobody Read candidate `345`, Working Machine candidate `352`, Vault of Voices candidate `359`, and their dedicated specs, proofs, localisation, Event Log, and asset packages.
The current documented pilot total is twenty-five rows and 247 defined blocks, all dormant and outside release-floor credit.

The current Fallout content boundary is dormant by design where the activation gates are unset. Defined blocks, reserved ids, and candidate rows are not release-floor credit until their callers, human and hidden AI paths, effects, memory, cleanup, localisation, assets, and audits are complete.

## Proof index

- `AIR_CONTAMINATION_NATURAL_SOURCE_PROOF.md` records low, capped wildfire, volcanic eruption, ashfall, massive-eruption, and settled-ash aftermath pressure.
- `AIR_WINTER_NORMAL_MAP_PROOF.md` and `subagent_handoffs/air_winter_normal_map_static_reaudit_2026-07-22.md` record the ordinary-map visual route.
- `FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md` records the pinned installed-map sweep and its strict engine-native blocker.
- `FALLOUT_MANUAL_POPULATION_CONTRACT_PROOF.md` records the generation-bound 90 to 95 percent manual population contract.
- `FALLOUT_BLACKOUT_GUI_PROOF.md` records full-screen input blocking and blackout surface ownership.
- `FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md` records the accepted numerical survival transaction.
- `FALLOUT_EVENT_SCHEDULER_PROOF.md` records the dormant scheduler substrate and activation gates.
- `FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md` records the twenty-three reviewed ordinary candidate rows and their correction sections. `FALLOUT_WELL_QUEUE_TUNING_AND_REGISTRY.md` records the fourth Well Queue candidate, state gate, branch tuning, callback deferral, and dedicated asset. `FALLOUT_ANIMAL_FEED_TUNING_AND_REGISTRY.md` records the fifth Animal Feed candidate, native food snapshot gate, branch tuning, callback deferral, and reused food art. `FALLOUT_FEVER_DORMITORY_CHAIN_PROOF.md` records the twelfth Fever Dormitory candidate, state gate, four policy lanes, delayed callback, Deaths route, Event Log payloads, and runtime proof boundary. `FALLOUT_NAMES_FOR_THE_MISSING_CHAIN_PROOF.md` records the thirteenth country candidate, four policy lanes, deterministic grading, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary. `FALLOUT_FIRST_SAFE_BIRTH_CHAIN_PROOF.md` records the fourteenth country candidate, generation-change grading, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary. `FALLOUT_SCHOOL_VENT_ROOM_CHAIN_PROOF.md` records the fifteenth country candidate, four curricula, education grading, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary. `FALLOUT_EMPTY_WARD_CHAIN_PROOF.md` records the sixteenth country candidate, four institution policies, ward grading, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary.
- `FALLOUT_BLACK_START_CHAIN_PROOF.md` records the eighteenth Black Start candidate, four grid policies, deterministic delayed result, maintenance callback, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary.
- `FALLOUT_FIRST_STREETLIGHT_CHAIN_PROOF.md` records the nineteenth First Streetlight candidate, four urban priorities, deterministic delayed result, public maintenance callback, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary.
- `FALLOUT_WORKING_ELEVATOR_CHAIN_PROOF.md` records the twentieth Working Elevator candidate, four grain-storage priorities, deterministic delayed result, storehouse maintenance callback, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary.

- `FALLOUT_SEALED_WAREHOUSE_CHAIN_PROOF.md` records the twenty-first Sealed Warehouse candidate, four salvage policies, deterministic delayed result, warehouse claim callback, contamination ledgers, Deaths route, Event Log payloads, dedicated report art, and dormant runtime boundary.
- `FALLOUT_DEAD_CITY_PERMIT_CHAIN_PROOF.md` records the twenty-second Dead City Permit candidate, four expedition policies, deterministic state selection, delayed permit result, city callback, Deaths route, Event Log payloads, dedicated report art, and the `EVENT_ISSUE_LIMIT` engine-inspector boundary.
- `FALLOUT_MANUAL_NOBODY_READ_CHAIN_PROOF.md` records the twenty-third Manual Nobody Read candidate, four technical-facility policies, deterministic state selection, delayed result, maintenance callback, Deaths route, Event Log payloads, dedicated report art, and the `EVENT_ISSUE_LIMIT` engine-inspector boundary.
- `FALLOUT_WORKING_MACHINE_CHAIN_PROOF.md` records the twenty-fourth Working Machine candidate, four automated-facility policies, deterministic state selection, delayed machine result, inspection callback, Deaths route, Event Log payloads, dedicated report art, and its bounded engine-inspector result.
- `FALLOUT_VAULT_OF_VOICES_CHAIN_PROOF.md` records the twenty-fifth Vault of Voices candidate, four archive and broadcast policies, deterministic state selection, delayed result, archive callback, Deaths route, Event Log payloads, dedicated report art, and its bounded engine-inspector result.

The historical pilot-count wording above is superseded by the Dead City Permit, Manual Nobody Read, and Working Machine corrections.
The current reviewed total is twenty-five rows and 247 defined blocks, all dormant and outside release-floor credit.

- `FALLOUT_CALLBACK_CLEANUP_ORDER_PROOF.md` records authenticated result and callback cleanup ordering for the food, water, and rail pilots.
- `FALLOUT_ASH_WEEK_CAPITAL_CHARACTER_EVENT_PROOF.md` records the dormant capital-condition and character-or-institution event surfaces at `chaosx.fallout.66` through `.81`.
- `FALLOUT_ASH_WEEK_ORIENTATION_EVENT_LOG_PROOF.md` records history `9110`, the 45-payload orientation matrix, and its dormant idempotent Event Log writer.
- `FALLOUT_TRIAGE_WALL_CHAIN_PROOF.md` records the dormant medicine candidate at suffixes `175` through `187`, history `9111`, state gate, four human and hidden-AI policies, doctor's callback, cleanup, and dedicated report asset.
- `FALLOUT_SEED_VAULT_CHAIN_PROOF.md` records the dormant seed candidate at suffixes `188` through `200`, history `9112`, Air Winter seed provenance, four policy lanes, agronomist callback, cleanup, and dedicated report asset.
- `FALLOUT_BAD_BATCH_CHAIN_PROOF.md` records the dormant crop-trial candidate at suffixes `204` through `216`, history `9113`, generation-bound seed or greenhouse provenance, four delayed policy lanes, callback, cleanup, and dedicated report asset.
- `docs/specs/air_cleanliness_fallout_specs/specs/13_reviewed_global_survival_pilots.md` promotes the normalized Names severity, visible-budget envelope, and separate callback Deaths rate. `docs/assets/air_cleanliness_fallout/fallout_names_missing/manifest.md` is the active asset crosswalk.

## Current blockers

The strict engine-native all-valid-land-province enumerator is undocumented. The pinned map ledger is static evidence only. Native strike acceptance, callback timing, save behavior, multiplayer ownership, and the vanilla news-event load remain unobserved because HOI4 is not launched.

Successor package production, player materialization, general allocation, country and focus content, complete diplomacy reset, full orientation coverage, event logs and details, dedicated content assets, and the 660 manually reviewed living-world event floor remain incomplete. No fallback or placeholder is approved for those gaps.
