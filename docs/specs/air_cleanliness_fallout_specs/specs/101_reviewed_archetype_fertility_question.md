# Reviewed Archetype: The Fertility Question

The Fertility Question is the year-two household and generation chain for the fictional Congo Green Basin mutant polity. It follows the closed Mixed Settlement Petition state memory. Population recovery is uncertain after the Fallout consequence, but the chain treats that uncertainty as a civic question about services, guardianship, trust, and migration. It does not present mutation as ordinary radiation science, a diagnosis, or a claim about real-world fertility.

The chain uses human and hidden AI events `chaosx.fallout.970` and `chaosx.fallout.971`, delayed result events `chaosx.fallout.972` and `chaosx.fallout.973`, review events `chaosx.fallout.974` and `chaosx.fallout.975`, and cleanup event `chaosx.fallout.976`. Its scheduler candidate id is `894`, transaction key `710099`, route `7230`, and Event Log history `9205`. Fallout remains a consequence and is not registered as an ordinary event, evolution, scenario log entry, or super-event.

## Candidate boundary

The candidate is eligible from campaign day `1200` through day `10000`. The country must retain the Congo Green Basin memory and mutant-polity government archetype, current country resource rows, Medicine, Cohesion, Recognition, family legitimacy, cohort pressure, and one affordable branch. The selected state must be controlled by the country, retain current survival identity and resource rows, living population, Shelter, Adaptation, bounded Exposure and Disease Pressure, a valid Air Winter phase, and a foreign neighbor. It must carry the closed `fallout_event_887_memory_closed` state flag from Mixed Settlement Petition.

The scheduler selects the lowest eligible state id. The registry freezes owner, controller, transition generation, state Air Winter values, Supply Access, the household ledgers, and the lowest eligible foreign witness state. Every delayed lane revalidates those receipts. A changed state, owner, controller, witness, or generation cancels the chain and authenticated cleanup releases reserved transaction rows.

## Branches

The four branches have distinct costs and social consequences.

- Voluntary Household Support spends Food `2`, Medicine `3`, and Recognition `2`. It funds warm rooms, food delivery, and medicine without a target, quota, or required family pattern.
- Public Cohort Services spends Scrap `2`, Power `2`, and Recognition `2`. It builds schools, food stores, and household services under a published civic charter that names services rather than a required family shape.
- Two-Witness Adoption Houses spends Fuel `1` and Recognition `2`, then accepts a Cohesion cost of `1`. It connects orphan care, kinship claims, and local guardians through named adoption houses.
- Emergency Register Only spends Food `1`, Medicine `1`, Fuel `1`, and Recognition `1`. It refuses a public family program while keeping a narrow register for emergency aid.

## Effects and memory

Each result grades state Supply Access, Shelter, Adaptation, Exposure, Disease Pressure, Reclamation, Medicine, Cohesion, Recognition, family legitimacy, cohort pressure, household cohesion, family trust, family migration pressure, generation fatigue, and demographic cause memory. Success, partial, and failure outcomes change Air Winter and Supply Access, write a distinct branch memory, apply bilateral opinion, and use bounded Deaths failure effects. The callback repeats grading after 365 days and closes the state memory only after both delayed transactions settle.

The human and hidden AI lanes use the same branch priorities, deterministic score, costs, result delay, callback delay, and cleanup. The chain never requests Fallout, changes the government archetype, creates a country, transfers population between states, or adds a recurring scheduler. It remains dormant and outside release-floor credit until the scheduler activation audit opens it.

## Wiring and assets

Runtime constants live in `common/script_constants/fallout_world_end_fertility_question_constants.txt`. Triggers and effects live in `common/scripted_triggers/fallout_world_end_fertility_question_event_triggers.txt` and `common/scripted_effects/fallout_world_end_fertility_question_event_effects.txt`. The candidate producer is `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.

Dynamic modifiers, opinion modifiers, Event Log routing, events, and localisation use dedicated Fertility Question names. The generated report art and manifest live under `docs/assets/894_fertility_question/`. Runtime art is `gfx/event_pictures/fallout/report_event_fallout_fertility_question.dds` registered as `GFX_report_event_fallout_fertility_question`.

## Review boundary

Static source review must verify event ids, candidate constants, predecessor memory gating, branch and delayed-result coverage, Event Log key coverage, dedicated art wiring, localisation encoding, and absence of stale Mixed Settlement branch tokens. Focused event inspection may document blocking diagnostics, but no HOI4 runtime claim is made in this tranche.
