# Fallout The Last Transformer event addendum

## Status and improvement decision

This is the reviewed implementation addendum for the next dormant global-survival family after The Door List.
It replaces the initial short draft in this file with a complete transaction contract.
The Door List identities and candidate route are present in current implementation files, so this plan does not stack another pass on an unresolved Last Transformer addendum.

The chain remains dormant.
It does not add a caller, set either scheduler activation flag, create a public scenario row, or change the orientation live ledger.
The event treats the transformer as a narrative grid component represented by the existing Power resource, current Air Winter state values, and documented vanilla building evidence.
It does not claim that HOI4 has a specialized transformer, hospital, microgrid, or distribution-grid building.

## Fixed identities

| Surface | Value |
| --- | ---: |
| Human opening | `chaosx.fallout.243` |
| Hidden AI opening | `chaosx.fallout.244` |
| Human cannibalize result | `chaosx.fallout.245` |
| Human hospital result | `chaosx.fallout.246` |
| Human microgrid result | `chaosx.fallout.247` |
| Human neighbor result | `chaosx.fallout.248` |
| Hidden AI cannibalize result | `chaosx.fallout.249` |
| Hidden AI hospital result | `chaosx.fallout.250` |
| Hidden AI microgrid result | `chaosx.fallout.251` |
| Hidden AI neighbor result | `chaosx.fallout.252` |
| Human callback | `chaosx.fallout.253` |
| Hidden AI callback | `chaosx.fallout.254` |
| Cleanup | `chaosx.fallout.255` |
| Candidate identity | `243` |
| Transaction key | `710011` |
| Candidate route | `7111` |
| Candidate route upper bound after registration | `7112` |
| Event Log history | `9116` |
| Primary family | `global_survival_and_society` |
| Cooldown family | `power` |
| Event class | `crisis_incident` |
| Preferred phase | `first_season` |
| Secondary phase | `first_winter_year` |
| Result delay | `10` days |
| Callback delay | `120` days after result |
| Visible budget cost | `3` |

The event, candidate, transaction, route, and history search found no conflict in their own identity domains.
Unrelated province ids `7111` and `9116` do not conflict with candidate routes or Event Log histories.
All event definitions belong in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

## Playable promise

One state still has a working industrial feeder, but its final serviceable transformer cannot carry every load.
The player chooses what kind of institution inherits the grid.
The choice can strip an operating factory, establish a protected clinical circuit, distribute authority among local feeder crews, or accept technical dependence on an AI-controlled neighbor.
The callback turns that emergency allocation into a durable industrial, medical, municipal, or diplomatic memory.

## Technical and historical basis

The United States Department of Energy describes large power transformers as critical, difficult to transport, expensive, and slow to replace.
That evidence supports treating a serviceable unit as scarce equipment that cannot be conjured by a generic repair reward.
National Laboratory material describes microgrids as bounded systems able to preserve critical services during wider outages.
It also identifies hospitals as high-priority resilience sites.

Research anchors:

- [Department of Energy on transformer security and replacement constraints](https://www.energy.gov/oe/addressing-security-and-reliability-concerns-large-power-transformers)
- [Department of Energy Transformer Resilience and Advanced Components program](https://www.energy.gov/oe/transformer-resilience-and-advanced-components-trac-program)
- [National Laboratory overview of microgrids for critical services](https://www.nrel.gov/news/detail/program/2025/microgrids-could-enhance-grid-resilience)
- [National Laboratory hospital resilience study](https://www.nrel.gov/reopt/projects/case-study-wip)

These sources guide scarcity, prioritization, and decentralization.
They do not justify adding a modern grid simulation or asserting that any vanilla factory level is literally a transformer.

## Candidate eligibility

The producer runs only from the accepted country-owned Fallout scheduler behind both dormant activation gates.
It adds no on-action and no world iterator.
The event is nonrepeatable for the current country generation.

The current country must satisfy all of the following:

1. It has the current Fallout runtime generation and durable current Survival resource row.
2. It is in `first_season` or `first_winter_year`.
3. Current Power is at least `5` and below `55`.
4. It can pay at least one branch, with Medicine at least `4` or Scrap at least `6`.
5. It has no current Last Transformer candidate, pending transaction, result, callback, cleanup, issued tombstone, or completion memory.
6. It has at least one eligible target state.

An eligible target state must:

1. Be owned and controlled by the current country.
2. Carry the exact current-generation Fallout state identity.
3. Carry the current produced Air Winter snapshot.
4. Have current Air Winter Supply Access.
5. Have at least one operational infrastructure level.
6. Have at least one operational civilian or military factory level.
7. Have Air Winter Exposure above `20`.
8. Have Air Winter Reclamation above `15`.
9. Lack a current-generation Last Transformer state memory.

Operational levels use `non_damaged_building_level@infrastructure`, `non_damaged_building_level@industrial_complex`, `non_damaged_building_level@arms_factory`, `non_damaged_building_level@air_base`, and `non_damaged_building_level@dockyard`.
Retained but fully damaged levels do not satisfy operational evidence.

The producer calculates target priority as:

`operational infrastructure * 4 + operational civilian factories * 3 + operational military factories * 3 + operational air bases + operational dockyards`

It chooses the highest priority.
An exact tie chooses the lowest state id.
It writes one reviewed candidate row and never retargets after selection.

The scheduler candidate receipt uses frozen Power pressure as the resource crisis input, frozen Exposure as severity, and target priority clamped from `0` through `100` as state value.
The authored adjustment is `0`.
Region, government, cause, war, character, relationship, and previous-choice match inputs remain neutral unless an accepted current-generation receipt exists.
The normal family fatigue, target repetition, cadence, visible-envelope, and crisis-break rules still apply.
There is no minimum-score rescue.

## Optional neighbor technician receipt

The neighbor lane never imposes an event, cost, opinion modifier, resource change, or memory on another human country.
Its partner receipt may select only an AI-controlled country that shares a land-state border with the host, is not at war with the host, carries the current Fallout country identity and Survival row, has Power at least `25`, and has Reclamation at least `20`.

The partner score is frozen Power plus frozen Reclamation.
The highest score wins and a tie uses the scheduler's lowest stable partner index.
Freeze partner country identity, generation, Power, Reclamation, and display name.
The opening describes technicians as dispatched after the choice commits, so later partner destruction does not reroll the result or authorize a new partner.
If no eligible AI partner exists, the neighbor option remains visible but unavailable.

## Frozen opening receipt

Before the opening becomes pending, freeze:

- runtime generation, control mode, candidate id, transaction key, route, family, cooldown family, event class, issue day, result due day, callback due day, and visible budget cost
- target state id, owner, controller, state generation, Air Winter snapshot generation, and state memory generation
- Power, Medicine, Scrap, Recognition, Exposure, Reclamation, Shelter, and Supply Access
- operational infrastructure, civilian factory, military factory, air-base, and dockyard levels
- normalized infrastructure score, normalized industry score, auxiliary load score, base grid viability, every branch score, projected outcome for every branch, and branch affordability
- selected partner receipt when the neighbor lane is valid

Normalized inputs are:

`infrastructure score = clamp(operational infrastructure * 20, 0, 100)`

`industry score = clamp((operational civilian factories + operational military factories) * 10, 0, 100)`

`auxiliary load = clamp((operational air bases + operational dockyards) * 10, 0, 100)`

The result and callback never reread mutable resources, Air Winter values, or building levels to reclassify outcome.
All coefficients, gates, costs, delays, building amounts, Deaths fractions, and result deltas belong in `common/script_constants/fallout_consolidated_constants.txt`.

## Four branch commitments

| Token | Branch | Exact opening commitment | Required evidence |
| ---: | --- | --- | --- |
| `1` | Cannibalize industry | Power `2` and one permanent operational factory level | At least one operational civilian or military factory |
| `2` | Protect hospital power | Power `5` and Medicine `4` | Frozen Medicine at least `4` |
| `3` | Decentralize microgrids | Power `4` and Scrap `6` | Frozen Scrap at least `6` |
| `4` | Request neighbor technicians | Power `3` and Recognition `4` | Authenticated eligible AI partner |

Payments and the cannibalized factory apply once after the ordinary slot, delayed row, target identity, and selected branch are authenticated.
Cannibalization selects an operational civilian factory when one exists, otherwise an operational military factory.
It uses two static, reviewed `remove_building` branches and removes exactly one level.
The selected building type and application token are stored before the result is scheduled.
The result never removes a second level and never substitutes a different building.

If the selected factory ceases to be operational between opening display and branch commit, the transaction is rejected before payment.
It closes through cleanup without choosing another state or building.
Other branches do not claim that a hospital, microgrid, or transformer is a HOI4 building.

## Deterministic outcome contract

The frozen base grid viability is:

`30% Power + 20% Supply Access + 15% infrastructure score + 10% industry score + 10% Reclamation + 5% Shelter + 5% Recognition + 5% Medicine - 20% Exposure - 10% auxiliary load`

Round once and clamp from `0` through `100`.

Branch scores are:

- cannibalize score equals base viability plus `10` when a civilian factory is selected or `6` when a military factory is selected
- hospital score equals base viability plus `20%` of frozen Medicine
- microgrid score equals base viability plus `20%` of frozen Scrap plus `10%` of frozen Reclamation
- neighbor score equals base viability plus `15%` of frozen Recognition plus `10%` of partner Power plus `10%` of partner Reclamation

Round each branch score once and clamp from `0` through `100`.

| Branch | Success | Partial | Failure |
| --- | ---: | ---: | ---: |
| Cannibalize industry | `58` or more | `38` through `57` | below `38` |
| Protect hospital power | `62` or more | `42` through `61` | below `42` |
| Decentralize microgrids | `60` or more | `40` through `59` | below `40` |
| Request neighbor technicians | `60` or more | `40` through `59` | below `40` |

The projected result is frozen before payment.
No random list, MTTH roll, `ai_chance`, alternate state, alternate building, alternate partner, or affordable-branch substitution is permitted.

## Result consequences

Opening costs and the cannibalized factory are separate from these delayed result deltas.
Power, Medicine, Scrap, and Recognition use the sole Survival resource mutation helper.
Exposure, Reclamation, Shelter, and Supply Access use the authenticated Air Winter state-delta helper and refresh its native modifier.

| Branch and result | Exact delayed consequences | Durable result memory |
| --- | --- | --- |
| Cannibalize success | Power `+12`, Scrap `+5`, Reclamation `+3`, Supply Access `+4` | `transformer_from_the_line` |
| Cannibalize partial | Power `+7`, Scrap `+3`, Recognition `-2`, Supply Access `+1` | `factory_stripped_for_a_weak_grid` |
| Cannibalize failure | Power `+2`, Scrap `+1`, Reclamation `-3`, Supply Access `-5`, Exposure `+3`, one repairable infrastructure damage, Deaths fraction `0.0004` | `factory_lost_with_the_transformer` |
| Hospital success | Recognition `+6`, Shelter `+2`, Supply Access `+2` | `protected_clinical_circuit` |
| Hospital partial | Recognition `+2`, Shelter `+1`, Supply Access `-1` | `ward_by_ward_power` |
| Hospital failure | Medicine `-2`, Recognition `-5`, Supply Access `-5`, Exposure `+2`, Deaths fraction `0.0006` | `darkened_wards` |
| Microgrid success | Power `+8`, Reclamation `+6`, Supply Access `+6`, Recognition `+3`, Shelter `+2` | `feeder_councils` |
| Microgrid partial | Power `+4`, Reclamation `+3`, Supply Access `+2`, Recognition `+1` | `uneven_microgrids` |
| Microgrid failure | Reclamation `-4`, Supply Access `-6`, Exposure `+4`, one repairable infrastructure damage, Deaths fraction `0.0003` | `burned_local_feeders` |
| Neighbor success | Power `+9`, Reclamation `+4`, Supply Access `+4`, Recognition `+2` | `technician_compact` |
| Neighbor partial | Power `+5`, Supply Access `+1`, Recognition `-2` | `borrowed_switchgear` |
| Neighbor failure | Recognition `-5`, Supply Access `-3`, Deaths fraction `0.0002` | `crew_arrived_too_late` |

Repairable infrastructure damage uses the documented state-scoped `damage_building` effect with static type `infrastructure`, damage `1`, and an operational-level check immediately before application.
If the level is already damaged or absent, the effect records a building-application shortfall and does not damage another building.
The frozen result token remains unchanged.

Failure casualties call `apply_exact_state_civilian_population_loss` against the authenticated target state with the shared minimum-remaining population, `fallout_aftermath` reason, and state population application disabled after the mutation is observed.
The helper's applied amount is then recorded exactly once through the shared Deaths API.
No direct negative manpower effect or duplicate Deaths record is allowed.

The event must not add fields to the orientation pretransition, transition, or posttransition ledgers.
The permanent factory loss is owned by this event transaction, its state memory, and Event Log history.
Current Survival and Air Winter values change only through their accepted owner helpers.

## Callback and future consumption

The callback is due exactly `120` days after the result commits.
It applies no second building mutation and no second casualty transaction.
It converts the result into one branch-aware institution:

- cannibalization creates a stripped-works memory that can support industrial grievance, salvage doctrine, or a later repair demand
- hospital priority creates a clinical circuit charter that can support medical legitimacy and future ration disputes
- microgrids create feeder councils that can support municipal autonomy and the later Black Start family
- neighbor assistance creates a technician compact or technical debt memory without changing the partner country

Successful or partial cannibalization, microgrid, and neighbor branches may set an `engineer_candidate` consumer memory.
This chain does not create a character.
A later reviewed character event may consume that memory and must receive its own ids, localisation, AI, and asset contract.

## Country and state memory

The country stores branch token, result token, callback token, target state id, selected building type, factory removal applied, infrastructure damage applied, resource payments, result deltas, Deaths applied, partner id when used, issue day, result day, callback day, and completion generation.
The state stores current-generation grid allocation, building consequence, result, and callback institution memories.
Operational score variables, candidate inputs, and partner selection variables clear during cleanup.
Only accepted durable memories survive a later generation reset.

## Hidden AI parity

The hidden opening uses the same target, optional partner, frozen values, affordability, score formulas, projected results, opening commitments, delayed result effects, Deaths, callback, Event Log, and cleanup as the human opening.
Invalid branches are not scored.
Each valid branch starts at `10`, adds `8` for projected success or `3` for projected partial, and applies:

| Condition | Cannibalize | Hospital | Microgrids | Neighbor |
| --- | ---: | ---: | ---: | ---: |
| Continuity Council | `+2` | `+5` | `+5` | `+2` |
| Bunker Directorate | `+4` | `+6` | `+1` | `0` |
| Warlord Seat | `+7` | `-2` | `0` | `-3` |
| Food Compact | `0` | `+7` | `+3` | `0` |
| Maritime Authority | `0` | `+2` | `+5` | `+5` |
| Quarantine Board | `-2` | `+8` | `+4` | `0` |
| Scavenger Freehold | `+8` | `-1` | `+5` | `0` |
| Nomad Compact | `-3` | `+2` | `+7` | `+4` |
| Machine Directorate | `+3` | `-2` | `+9` | `+2` |
| Technate | `0` | `+2` | `+8` | `+5` |
| Mutant Communion | `-2` | `+3` | `+6` | `+1` |
| Religious Refuge | `-2` | `+7` | `+2` | `+3` |
| Power below `20` | `+5` | `-2` | `+4` | `+3` |
| Exposure at least `60` | `0` | `+4` | `+3` | `0` |
| Country at war | `+3` | `+4` | `0` | `-2` |
| Only one operational factory remains | `-8` | `0` | `+2` | `+2` |
| Operational dockyard exists | `0` | `0` | `+2` | `+2` |

The evaluator selects the highest final score and replaces the current winner only on a strictly higher score.
Exact ties resolve cannibalize industry, protect hospital power, decentralize microgrids, then request neighbor technicians.

## Transaction timing, authentication, and cleanup

The human opening is visible and the AI opening is hidden.
The selected branch reserves one result row due exactly `10` days after opening commit.
The result reserves one callback row due exactly `120` days after result commit.
Opening, human result, and human callback consume a visible envelope cost of `3`.
The hidden AI opening reserves the same narrative envelope so AI chains cannot evade cadence.

Result authentication requires exact generation, owner, controller, target state id, state identity, Air Winter snapshot, transaction key, route, branch, projected result, result due day, opening-payment token, and unconsumed result tombstone.
Callback authentication requires the committed result token, exact callback due day, and unconsumed callback tombstone.
Neither row may retarget or reclassify.

Cleanup releases the callback row before the result row, then releases the pending receipt, writes callback and result tombstones, writes the candidate tombstone, clears state operational markers, and clears country operational variables.
Cleanup is idempotent and callable from every rejected commit.
The factory-removal token, Deaths token, result token, and callback token prevent double application after retry or save recovery.

Literal multiplayer lobby-host identity remains an accepted scheduler blocker.
This chain relies on the current deterministic country coordinator and does not claim to solve host detection.

## Event Log and localisation

History `9116` receives result payloads `11` through `43` for four branches across success, partial, and failure, plus callback payloads `51` through `53`.
The Event Log actor is the choosing country.
The detail receipt includes target state, frozen Power, selected branch, removed building type, removal application, infrastructure damage application, partner display name when used, result, resource deltas, Supply Access delta, Deaths applied, and callback institution.

Human opening text must name the state, current Power, the operating factory line, the clinic circuit, the proposed feeder districts, and the eligible neighbor when present.
It must explain that only one load plan can inherit the transformer without exposing score thresholds.
Cannibalization text must identify whether the selected level is civilian or military industry.
Hospital text must describe a protected circuit without implying a hospital building.
Microgrid text must describe local feeder separation without claiming a new building type.
Neighbor text must identify technical dependence and remain unavailable when no authenticated AI partner exists.
Results and callbacks must describe concrete rooms, switches, workshops, wards, and authorities rather than broad ruin language.
Hidden AI events need no player-facing prose.

Localisation belongs in the existing Fallout English localisation family with UTF-8 BOM.
It needs opening, four option, twelve result, branch-aware callback, custom trigger tooltip, effect tooltip, Event Log, event detail, and scripted-localisation keys.

## Dedicated asset handoff

The generated fictional package already exists and is ready for parent review:

- sprite `GFX_report_event_fallout_last_transformer`
- GFX target `interface/fallout_consolidated.gfx`
- runtime DDS `gfx/event_pictures/fallout/report_event_fallout_last_transformer.dds`
- manifest `docs/assets/air_cleanliness_fallout/fallout_last_transformer/manifest.json`
- handoff `docs/assets/air_cleanliness_fallout/fallout_last_transformer/gfx_handoff.md`

The image shows one damaged transformer, anonymous maintenance workers, ash, a clinic, and a workshop.
Human opening, result, and callback may share this dedicated family image.
Hidden AI events use no picture.
Implementation must register the sprite and verify the manifest-linked DDS.
The asset package does not authorize a generic report image if wiring fails.

## Engine-sensitive review points

1. Freeze raw operational levels from `non_damaged_building_level@type`, not retained `building_level@type`.
2. Implement the cannibalization type with two static `remove_building` branches because dynamic building type injection is unnecessary and would create avoidable risk.
3. Prove that permanent post-transition factory removal does not require or mutate any orientation live-ledger field.
4. Use only the current Air Winter authenticated state-delta helper for Supply Access, Reclamation, Shelter, and Exposure.
5. Prove that the optional partner index is stable and that human-controlled partners are excluded before the option becomes valid.
6. Preserve the accepted scheduler rule that the three visible events cost `3`.
7. The installed package has no Technology Tree Viewer.
8. No technology or doctrine change belongs to this chain.

These points are implementation or activation checks.
They do not authorize substitute mechanics.

## Acceptance checks

1. IDs `243` through `255`, candidate `243`, transaction `710011`, route `7111`, upper bound `7112`, and history `9116` are unique in their own domains.
2. The event remains under `chaosx.fallout` and has no public caller.
3. Both scheduler activation flags remain unset.
4. The target carries exact current Fallout state identity, durable Survival ownership, produced Air Winter snapshot, Supply Access, operational infrastructure, and operational industry.
5. Target selection uses highest authored priority and lowest state id on ties.
6. Power is at least `5` and below `55`, and Medicine or Scrap affordability is proven.
7. Every requested country, state, Air Winter, and operational building value is frozen before payment.
8. Exactly four human and four hidden AI branches use matching shared effects.
9. Branch costs are distinct, authenticated, and charged once.
10. Cannibalization removes exactly one authenticated factory level before scheduling and never retargets.
11. No branch claims or creates a specialized power, transformer, hospital, or microgrid building.
12. Outcome arithmetic rounds once, clamps once, and uses no random selection.
13. Human and AI results arrive exactly `10` days after opening.
14. Human and AI callbacks arrive exactly `120` days after result.
15. Visible budget cost is `3`.
16. Failure building damage is repairable, operationally gated, limited to one infrastructure level, and idempotent.
17. Failure population loss uses the exact state helper and records applied Deaths once.
18. Survival and Air Winter changes use their accepted owner helpers.
19. No orientation live-ledger field is added or mutated.
20. The neighbor branch excludes human partners and applies no effect to the selected AI partner.
21. Hidden AI selects the highest valid score with the documented strict tie order.
22. Country and state memories are branch-aware, outcome-aware, generation-bound, and cleaned correctly.
23. Event Log history `9116` records branch, outcome, building application, partner display, resource changes, Supply Access, Deaths, and callback.
24. Localisation distinguishes industrial, clinical, municipal, and technical-dependence routes without exposing arithmetic.
25. The dedicated manifest-linked report image is registered and wired.
26. Every stale, duplicate, invalid, or unaffordable transaction reaches idempotent cleanup without retargeting.

## Scope limits and promotion

This tranche needs no decision category, scripted GUI, focus route, formable, achievement, super-event, technology, doctrine, new building type, or completed engineer character.
Those surfaces would add maintenance before the grid-memory callbacks have proved campaign value.

Keep this addendum under `docs/plans/air_cleanliness_fallout_plans/` until implementation, Event Log routing, localisation, asset wiring, exact transaction scenarios, and cleanup proof pass review.
If accepted, promote its fixed identities, eligibility, four branches, building rules, numerical outcomes, AI scoring, memory, and presentation contract into the global survival and society event bible and the global event family matrix.
