# Air Cleanliness Winter

## Purpose and ownership

Air Cleanliness Winter is the state-scoped survival lifecycle that precedes Fallout. It turns global Air Contamination into persistent local phases and ledgers for exposure, recovery, adaptation, food, shelter, reclamation, water, refugees, disease, supply, building damage, state-category damage, and civilian deaths.

Air Winter does not own the Fallout request coordinator, blackout presentation, world rewrite, successor allocation, or living-world scheduler. Those systems remain separate Fallout work. Air Winter supplies state condition, memory, migration, and terminal-choice inputs to them.

The implementation is distributed across:

- `common/script_constants/air_cleanliness_winter_constants.txt`
- `common/script_constants/air_cleanliness_winter_presentation_states.txt`
- `common/script_constants/air_cleanliness_winter_event_constants.txt`
- `common/script_constants/air_cleanliness_winter_response_constants.txt`
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt`
- `common/scripted_effects/air_cleanliness_winter_effects.txt`
- `common/scripted_effects/air_cleanliness_winter_event_effects.txt`
- `common/scripted_effects/air_cleanliness_winter_response_effects.txt`
- `common/dynamic_modifiers/air_cleanliness_winter_dynamic_modifiers.txt`
- `common/decisions/categories/air_cleanliness_winter_categories.txt`
- `common/decisions/air_cleanliness_winter_decisions.txt`
- `events/fallout_world_end_events.txt`

## Monthly integration

`air_contamination_monthly_update` in `common/scripted_effects/chaos_meter_effects.txt` is the only world-state pass used by Air Winter. The host country runs:

1. `air_winter_begin_monthly_cycle = yes` before the existing `every_state` block.
2. `air_winter_update_state = yes` once inside that existing block.
3. `air_winter_response_refresh_evacuation_cache_cycle = yes` after the block.
4. `air_winter_dispatch_phase_events = yes` after quote refresh.
5. `air_winter_finalize_monthly_cycle = yes` after bounded dispatch.

The Air Winter helpers do not create another state-wide or country-wide iterator. Post-pass work enters only owner arrays assembled during the existing state pass. The monotonic cycle id, per-state cycle id, and finalization cycle id make repeated calls idempotent. Global pressure reads a snapshot of the completed contamination-state counts from the preceding monthly pass before the host rebuilds those counts. Severe-neighbor pressure reads the opening state of every neighbor regardless of iterator order.

When ordinary Air Cleanliness is disabled, runtime phase and disease modifiers are removed while persistent state history remains available. `air_contamination_final_silence_locked` keeps Air Winter enabled under the existing Air Cleanliness contract.

## Phase model

`air_winter_phase`, `air_winter_target_phase`, and `air_winter_trend` are persistent state variables. Trend is `-1` for recovery, `0` for stable conditions, and `1` for worsening conditions.

| Phase | Identity | Entry pressure | Retention pressure | Baseline monthly civilian loss |
| ---: | --- | ---: | ---: | ---: |
| 0 | Clear | n/a | n/a | 0 |
| 1 | Dimming | 25 | 22 | 0 |
| 2 | Crop Shock | 50 | 46 | 0 |
| 3 | Hard Freeze | 65 | 60 | 0.005% |
| 4 | Black Harvest | 75 | 70 | 0.015% |
| 5 | Ash Winter | 90 | 84 | 0.040% |
| 6 | Terminal Winter | 100 | 94 | 0.100% |

Entry and retention thresholds provide hysteresis. A state changes by at most one phase during one monthly update. Escalation requires the minimum phase duration unless an explicit emergency escalation flag is present. Recovery requires a lower target phase, the configured recovery margin, three consecutive qualifying recovery updates, and the minimum time in the current phase.

The optional variables `air_winter_minimum_phase`, `air_winter_pressure_modifier`, `air_winter_recovery_bonus`, `global.air_winter_global_mitigation`, and `global.air_winter_global_recovery_bonus` are public integration inputs.

## Pressure and survival ledgers

Global pressure begins with `global.air_contamination_bp / 100`. That total includes the small capped wildfire-smoke and volcanic-ash contribution documented in `docs/air_cleanliness_natural_sources.md`, including the once-per-disaster settled-ash receipt created when a qualifying aftermath card opens. It adds bounded pressure from fallout states, chemical contamination states, Air Cleanliness thresholds, and Final Silence. Global mitigation is subtracted before clamping.

Local pressure adds nuclear fallout, nuclear intensity, chemical contamination, urban density, weak infrastructure, occupation disruption, and adjacency to phase 4 through 6. The severe-neighbor check reads the opening snapshot for the current cycle. A neighbor already processed on `global.date` exposes `air_winter_previous_phase`, while an unprocessed neighbor exposes its current phase. State iteration order therefore cannot change adjacency pressure. Adaptation, food, shelter, reclamation, and relief routes reduce pressure. Runtime pressure does not infer geography or climate.

The persistent state ledgers are:

- Lifecycle: phase, target phase, trend, previous phase, phase months, and recovery months.
- Survival: exposure, recovery, adaptation, food reserve, shelter capacity, reclamation, water security, refugee pressure, disease pressure, and survival value.
- Damage: building pressure, building cooldown, building-family cursor, category damage, and category cooldown.
- History: population-loss memory, original category, last phase change, last building loss, last category change, and last update.
- Presentation: presentation class and presentation-ledger version.
- Response: response cooldown, rail-protection duration, airbase-closure duration, project flags, and completed-action memory.
- Events: phase memory, chain memory, pending owner, delayed-result memory, event cooldown, and recovery arc count.

Boolean state uses flags. Normalization clamps every bounded ledger from 0 through 100 and preserves reviewed presentation assignments.

## Reviewed regional classification

`common/script_constants/air_cleanliness_winter_presentation_states.txt` is the authoritative typed state-ID ledger. It covers state IDs 1 through 1081 exactly once. It includes impassable states for presentation audit coverage, while gameplay effects still skip invalid states.

| Value | Class | Reviewed state count |
| ---: | --- | ---: |
| 1 | Boreal continental | 244 |
| 2 | Temperate maritime | 76 |
| 3 | Mediterranean | 58 |
| 4 | Desert and arid plateau | 202 |
| 5 | Tropical coast and monsoon | 152 |
| 6 | Equatorial rainforest | 47 |
| 7 | Mountain and highland | 176 |
| 8 | Island and oceanic | 77 |
| 9 | Polar and subpolar | 49 |

`air_winter_refresh_presentation_class_from_ledger` resolves the reviewed state ID before gameplay validity is checked. `air_winter_refresh_presentation_class` then validates the value and records class 0 if a missing or invalid assignment is encountered. The aggregate `global.air_winter_unclassified_state_count` and flag `air_winter_has_unclassified_states` keep classification gaps visible.

The exact-cover review and integration proof live in:

- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_STATE_CLASSIFICATION_REVIEW.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_STATE_LEDGER_INTEGRATION_PROOF.md`

## Gameplay consequences

### Phase and disease modifiers

Phases 1 through 6 apply one mutually exclusive state modifier. Each phase changes local manpower, supply, controller and enemy movement, controller and enemy attrition, building speed, state repair speed, and resources. Environmental movement and attrition effects apply to both operational sides.

Disease pressure is calculated separately so food, shelter, exposure, adaptation, water, and reclamation remain meaningful within a phase. The disease modifier reads bounded state variables for attrition and local manpower.

The repair fields use the documented `state_repair_speed_<Building>_factor` family for infrastructure, railways, civilian factories, military factories, air bases, dockyards, and supply nodes. Country-only industry repair fields are not used. Vanilla applies `attrition_for_controller` in state dynamic modifiers, but the generated modifier catalogue omits its state category. The unobserved runtime boundary is recorded in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_MODIFIER_AND_DEATHS_PROOF.md`.

### Air operations

General air-operation modifiers have documented country scope, but no supported runtime state or strategic-region dynamic scope. The monthly state pass therefore builds a controller-owned national burden from working airfields. Each valid state with undamaged air-base capacity contributes its final Air Winter phase once. The country result is the mean phase divided by phase 6. Phase 0 airfields remain in the mean, while fully damaged or closed airfields do not contribute.

The country modifier changes mission efficiency, detection, accident rate, and the weather penalty. The full-burden values are reached only when the mean phase across every contributing airfield state is 6.

| Mean airfield phase | Mission efficiency | Base detection | Accident rate | Weather penalty |
| ---: | ---: | ---: | ---: | ---: |
| 1 | -5 percent | -0.0417 | +3.33 percent | +2.5 percent |
| 3 | -15 percent | -0.125 | +10 percent | +7.5 percent |
| 6 | -30 percent | -0.25 | +20 percent | +15 percent |

`air_detection` changes the base detection value rather than multiplying the existing value. The table therefore records a flat value reduction for detection and percentage changes for the other three fields.

The aggregate is commutative and uses the existing state pass. Controllers enter the persistent Air Winter country registry without duplication. A cycle-stamped finalizer removes stale burden when a country loses its last working airfield, loses control of every contributing state, reaches mean phase 0, or disables Air Cleanliness. The committed Fallout transition lock removes the country modifier through that bounded registry before blackout scheduling and before the monthly Air Winter pass pauses. Active snapshot retries keep it absent. A failed prelock snapshot does not remove it.

This country result affects all air operations owned by the country. The engine exposes the required general air fields at country scope, so the modifier cannot be confined to the originating strategic regions through a runtime dynamic modifier. Exact state pressure from active ordinary land combat remains blocked by the absence of a documented state predicate or callback. Recent strategic bombing has a documented state trigger, but a second winter multiplier would compound the existing strategic-bombing Deaths tick and requires a separate balance decision.

### Survival output

`air_winter_calculate_survival_value` produces a clamped 0 through 100 output for AI, decisions, events, and map modes. Its current formula is:

`survival = 0.25 * food + 0.20 * shelter + 0.15 * water + 0.18 * adaptation + 0.12 * reclamation + 0.10 * recovery + infrastructure bonus + port bonus - occupation penalty - 0.35 * exposure - 0.20 * refugee pressure`

### Building and supply damage

Phase 3 through 6 states accumulate mitigated building pressure. When the threshold, sustained duration, and cooldown permit, the deterministic cursor checks infrastructure, civilian factories, military factories, air bases, dockyards, supply nodes, and railways. At most one available family is damaged per state update.

Supply nodes and railways receive extra protection before a sustained phase 5. State supply penalties also scale through the phase modifier and `air_winter_local_supply_factor`.

### State-category degradation

Phase 4 through 6 states accumulate category damage. The deterministic ladder is:

`megalopolis -> metropolis -> large_city -> city -> large_town -> town -> rural -> pastoral`

Pastoral states become wasteland only after a sustained phase 6. Enclaves, island categories, existing wastelands, and unknown custom categories are excluded. Original known categories are recorded. Restoration is an explicit administrative helper because another system may own a later category change.

### Civilian deaths

Phase 3 through 6 population losses use the shared exact state civilian-loss helper. The request is based on current state population and the phase rate, then modified by exposure, food, shelter, infrastructure, occupation, and adaptation. Applied losses enter the shared Deaths system with reason `constant:chaos_meter_deaths_reason.air_winter_exposure`.

A successful mountain-capital tunnel-school result writes durable state protection. After the normal monthly winter calculation, that state uses 90 percent of the resulting civilian death percentage. This makes the accepted population-loss benefit exact even when the shelter gain does not cross the separate low-shelter threshold.

Death reason 17 is integrated into the reason schema, country cause totals, detail arrays, sorting, map views, and localisation. Event-specific Air Winter losses use the same exact helper and reason. The monthly and event paths both stop population loss when `settings_chaos_deaths_disabled` is active, matching the player-facing Deaths setting.

### Operations and response decisions

The response category contains twenty state-target decision blocks. One selects the response-priority state, one selects the reception state, two show read-only designation summaries, and sixteen are timed projects. The operational layer covers respirators, clinics, air sampling, crop protection, ash-route clearance, rail protection, airfield closure, evacuation planning, shelter law, greenhouse refuge, controlled evacuation, medical triage, abandonment vote, bunker sealing, final evacuation, and mass decontamination.

Costs use exact affordability triggers and exact payment effects. Timed projects set both a state lock and a one-country lock on selection, then clear both on completion, cancellation, or reset. AI weights respond to population, survival, war strain, resource strain, infrastructure role, and prior planning. Cooldowns and completion flags prevent reward loops.

Controlled and final evacuations derive their transfer, transport, equipment, staff, stability, and pressure quote from source and receiver population. Formula work uses overflow-safe `state_population_k`. The transfer converts to people and rounds once before the quote is cached. The paid values, source, and receiver are locked for the delayed result. Source and receiver receive equal and opposite state-population changes. A country-scope deduction neutralizes the recruitable-manpower credit documented for negative state `add_manpower`. That compensation is statically supported but remains unobserved and is not claimed as a runtime guarantee. The proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_RESPONSE_DECISION_PROOF.md`.

The abandonment vote fires `chaosx.fallout.201`. Mass decontamination fires `chaosx.fallout.202`. Decontamination succeeds only when the selected state meets the disclosed Survival, Adaptation, and Water Security thresholds. Failure applies state damage and registers civilian losses through the Deaths system.

## Event pilot and scheduler

`events/fallout_world_end_events.txt` owns the namespace `chaosx.fallout`. The current Air Winter pilot contains 52 manually authored event blocks, 191 options, 190 effect-bearing options, and 67 delayed-result schedules:

- 49 phase, regional, seasonal, crisis, delayed-result, government, and recovery blocks.
- 2 terminal response result blocks for abandonment and decontamination.
- 1 stale-choice recovery block.

The pilot covers every phase, all nine presentation classes through regional routing, city, food, transport, shelter, disease, seed and livestock policy, island refugee admission, Desert City water logistics, ruined major-city salvage, mountain-capital tunnel schools, hydroelectric dams, oil and synthetic refineries, coal workings and heavy industry, reactors, government continuity, recovery, and several delayed deterministic results. The Phase 2 seed ledger diverts local factory availability for guarded storage and returns after 45 days with flourishing or failed trial plots, fixed herd depletion, or a conditional breeding-stock result. The island-refugee chain selects a real foreign coastal source through a bounded registry, moves exactly balanced state population, and returns after 30 days with one of six policy-specific results. The exact Desert City chain assigns frozen mains and ward cisterns to municipal works, railway tankers, or motor columns, then returns after 30 days through nine deterministic water-route results. The tunnel-school chain trades temporary local factory availability for shelter and a durable Deaths reduction. The Phase 3 infrastructure chains use state coal and oil output, operational factory counts, repairable building damage, state energy demand, the country energy ratio, low reactor-accident fallout, and civilian losses through the Deaths system. The Phase 5 salvage chain uses original urban identity, a persistent loss receipt, current damaged-building evidence, concrete equipment, Deaths, conditional repairable damage, and exhausted-site memory. The recurring seasonal layer records first frost, dark harvest, ash thaw, second winter, and terminal season. Event text uses state names and government-aware authority terms.

The five Phase 1 regional openings now commit one of ten owner-bound policy branches and schedule `chaosx.fallout.6` after 21 days. The shared result reads live Air Winter ledgers and operational buildings even if the state has moved beyond Phase 1. Exactly one success or inverse failure is available for the selected branch. Casualty failures use Deaths. Early failures change Building Damage Pressure but issue no direct building damage. Three mutually exclusive 21-day state modifiers represent factory access loss, supply disruption, or marked-corridor relief. Opening-only stale rejection cannot clear a newer transaction.

Within one selected Phase 3 state, route order is reactor, hydroelectric dam, oil or refinery, coal or heavy industry, transport, then clinic and heat. The heavy-industry identity requires positive coal or a combined total of at least four operational factories through the exact five-case ladder: at least 4 military, at least 3 military and 1 civilian, at least 2 military and 2 civilian, at least 1 military and 3 civilian, or at least 4 civilian. `chaosx.fallout.36` offers full furnace shifts or full shutdown. Full shifts resolve after 30 days at Adaptation 40 and Building Damage Pressure 55, with repairable military-factory, civilian-factory, then infrastructure damage on failure and explicit no-target exhaustion. Shutdown applies separate 31-day factory and coal-output modifiers only where their surfaces exist. `chaosx.fallout.37` removes both modifiers when the day-30 report is delivered and every result option repeats that cleanup. The chain uses the existing Deaths, pending-owner, refresh, reset, and Fallout snapshot contracts.

Within Phase 2, the mountain-capital route remains first. A destination matching `is_island_state` or `is_one_state_island` routes next. An exact arid urban state then routes to the `desert_city` interface of `chaosx.fallout.13` before the generic city choice. Municipal works, railway tankers, and motor columns repeat their exact target, building, and affordability gates at click time. `chaosx.fallout.49` resolves the three branches into nine exhaustive success, partial, and failure outcomes after 30 days. Failures use Deaths and conditional repairable building damage. Success and failure apply opposing timed local supply modifiers. Generic non-city arid and Mediterranean event 13 rows retain the original immediate choices and shared Phase 2 picture. `chaosx.fallout.38` separately defers its island Phase 2 receipt until a live foreign coastal source is found and a positive transfer succeeds. Rescue, quarantine, and exclusion move 2 percent, 1 percent, or 0.25 percent of current destination population, subject to 40,000, 20,000, or 5,000-person ceilings and a protected 1,000-person source remainder. The exact source loss is the exact destination gain. `chaosx.fallout.39` resolves the three branches into six deterministic outcomes after 30 days. Local failure casualties enter Deaths, while the migration itself does not.

Within Phase 5, ruined major-city salvage routes before the generic city, low-shelter abandonment, and archive choices. The candidate must retain an original `large_city`, `metropolis`, or `megalopolis` category, a persistent building-loss receipt, current damage in one of seven building families, and owner control. `chaosx.fallout.47` assigns the site to survey engineers, military quartermasters, or licensed district crews. Survey and military choices repeat exact affordability at display and click time. Licensed salvage remains executable without a payable resource gate. Event `.48` resolves each branch into success, partial, or disaster after 30 days. A tenth altered result replaces only a disaster when final-tier Chaos, positive active nuclear fallout, and chemical or biological contamination coexist. This is fictional high-Chaos content and not ordinary radiation science. All results exhaust the site. Ownership or control loss cancels the branch.

`air_winter_event_prepare_candidate_cycle` snapshots the documented current engine year once when the existing monthly cycle opens. `air_winter_schedule_phase_event` then runs from the existing monthly state update. Before the country cooldown gate, it can freeze a complete state marker for each of the five seasonal families. A marker records origin year, origin cycle, origin owner, presentation class, score, and typed event id. First frost also stores the typed route subtype that separates exact and generic event 13 rows. Markers remain eligible across cooldowns and year boundaries until a validated dispatch consumes them.

The owning country records one deterministic candidate through typed family priority, earliest origin cycle, highest frozen score, and lowest state id. The bounded post-pass owner array dispatches one event per eligible country, applies a 46-day cooldown, preserves the existing one-recovery-arc cap, and uses reviewed regional routing. Annual country receipts prevent a seasonal family from firing twice for the same recorded year. Second winter also uses nine presentation-class memories. The first severe year seeds that regional memory, while a later severe year can create the recurring event. The regional year advances only after a validated second-winter dispatch.

First frost reuses eight Phase 2 route identities, including the exact mountain-capital, engine-island, and Desert City routes. Event id and route subtype must both match before an ordinary event coalesces an exact first-frost observation. Dark harvest reuses the food-collapse opening and result. Ash thaw reuses the recovery opening and result. Terminal season reuses the Phase 6 terminal incident and its delayed result. Second winter uses the dedicated `chaosx.fallout.60` choice event and deterministic `chaosx.fallout.61` result. Dispatch saves regular event targets and uses `meta_effect` to inject the selected numeric event id. The island route also saves its selected source country and state as regular event targets. No second country-wide or state-wide iterator is introduced.

Delayed events retain their originating state target through the event chain. The island chain also retains the frozen source targets and durable latest-source scalars. Delayed event triggers require the saved destination to remain owned by the saved country and require a live branch flag. When the generic pending flag exists, target validation also requires the stored original owner. The Phase 1 result independently requires the complete pending-owner row and exactly one of ten branch flags. Its opening-only stale path displays event 203 without clearing transaction data, while stale result handling may cancel only the matching owner-bound row. The Desert City result independently requires the complete pending-owner row, and monthly reconciliation cancels a Desert City branch that lacks its pending receipt. The dead-city result additionally requires continued control by its original owner. Its dedicated state-control-change hook immediately reconciles a live branch without a periodic world scan. Every successful delayed-result choice refreshes the 46-day country cooldown immediately before its child timer begins. State reset, ownership change, control loss for dead-city salvage, Fallout transition, or active Fallout cancels or invalidates the branch. The existing Fallout snapshot pass freezes the Air Winter row before cancelling pending branches and their temporary modifiers, including the Desert City waterworks modifier and both furnace-shutdown modifiers. Country phase memories, cooldown flags, recovery counts, island source receipts, pending offers, migration memories, Phase 1 policy and outcome memories, Desert City policy and outcome memories, and dead-city policy and outcome memories are cleared separately through `air_winter_reset_country`.

This pilot is not the Fallout living-world scheduler. It does not count toward a claim that the 660-event Fallout release floor is complete. The event-target and scheduler proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_EVENT_SCHEDULER_PROOF.md`. The Phase 1 regional return transaction proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_1_REGIONAL_RETURN_EVENT_PROOF.md`. The seasonal marker and annual receipt proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_SEASONAL_RECURRENCE_PROOF.md`. The island source registry and balanced-population proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_2_ISLAND_REFUGEE_SOURCE_AND_POPULATION_PROOF.md`. The exact Desert City subtype, owner-bound water transaction, nine delayed results, and dynamic-picture proof are in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_PROOF.md`. The seed-ledger transaction proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_2_SEED_LEDGER_EVENT_PROOF.md`. The mountain-capital route, industry, Deaths, and ownership proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_2_TUNNEL_SCHOOL_EVENT_PROOF.md`. The coal-or-heavy-industry identity, furnace transaction, shutdown modifiers, repairable damage, and proof boundary are in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_3_HEAVY_INDUSTRY_EVENT_PROOF.md`. The ruined major-city identity, deterministic salvage transaction, control-loss cleanup, and dedicated asset proof are in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_PROOF.md`.

## Map modes and normal-map proof

Three registered map modes expose information through four viewer-specific monitoring levels:

- None reveals only the current phase.
- Basic sampling reveals the current phase and one-month trend to the state owner, controller, and treaty members.
- An Atmospheric Office reveals exact cause readings and the likely phase next season after one roof-sampler project completes.
- Terminal Modelling reveals a possible Fallout classification after global contamination reaches 90 percent, or to a major power with an Atmospheric Office.

The phase, exposure, and survival layers all use the same gate. Terminal text calls the result an atmospheric classification and warns that direct strikes or blast history can change the final grade. It does not commit the Fallout grading ledger.

Their files are:

- `common/map_modes/chaosx_state_map_modes.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- `localisation/english/chaosx_map_modes_l_english.yml`
- `interface/mapmodes_interface.gfx`
- `gfx/interface/mapmode/custom/air_winter_*`

The retired state-64 proof established stable state-bound entity creation and cleanup before final art production. The live route uses five deterministic slots per state inside the existing monthly state update. It creates one class-and-phase ground mesh, primary and secondary weather entities, dead vegetation when regional phase or food damage requires it, and one frozen-water or thaw entity. Warm classes retain rain, ash, frost, wetness, and runoff rather than receiving universal snow. No runtime visual observation is claimed.

Proof files are:

- `gfx/entities/air_cleanliness_winter_proof.asset`
- `common/scripted_effects/air_cleanliness_winter_visual_effects.txt`
- `common/script_constants/air_cleanliness_winter_visual_constants.txt`
- `gfx/entities/air_cleanliness_winter_regional_visuals.asset`
- `gfx/entities/air_cleanliness_winter_regional_particles.asset`
- `common/scripted_guis/air_cleanliness_winter_visual_proof_scripted_gui.txt`
- `interface/air_cleanliness_winter_visual_proof.gfx`
- `interface/air_cleanliness_winter_visual_proof.gui`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_NORMAL_MAP_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_REGIONAL_VISUAL_WIRING_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_CLEANLINESS_TREATY_LIFECYCLE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_CLEANLINESS_TREATY_INSPECTION_PROOF.md`

Regional snow, frost, cold rain, ash, dead vegetation, frozen water, phase-material dim light, and thaw are wired. The full-screen grade and static accessibility setting remain unpromoted because their UI and selection surfaces are not proven.

## Visual assets and sprite registry

All current final Air Winter art is Fallout-owned and uses dedicated paths.

| Use | Sprite identifiers | Runtime path | Registry |
| --- | --- | --- | --- |
| Phase modifiers | `GFX_air_winter_phase_1` through `GFX_air_winter_phase_6` | `gfx/interface/air_cleanliness_winter/modifiers/` | `interface/air_cleanliness_winter.gfx` |
| Country air operations | `GFX_air_winter_phase_2` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_2.dds` | `interface/air_cleanliness_winter.gfx` |
| Disease modifier | `GFX_air_winter_disease_pressure_state` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_disease_pressure_state.dds` | `interface/air_cleanliness_winter.gfx` |
| Report events | `GFX_report_event_air_winter_phase_1` through `GFX_report_event_air_winter_phase_6`, `GFX_report_event_air_winter_recovery`, `GFX_report_event_air_winter_island_refugee_harbor`, `GFX_report_event_air_winter_desert_water_convoy`, and `GFX_report_event_air_winter_dead_city_salvage` | `gfx/event_pictures/fallout/air_winter/` | `interface/air_cleanliness_winter.gfx` |
| Map mode buttons | Selected and deselected sprites for phase, exposure, and survival | `gfx/interface/mapmode/custom/` | `interface/mapmodes_interface.gfx` |
| Response decisions | `GFX_decision_air_winter_*` | `gfx/interface/air_cleanliness_winter/decisions/` | `interface/air_cleanliness_winter.gfx` |
| Regional ground and props | `air_winter_class_<class>_phase_<phase>_entity` and class prop aliases | `gfx/models/air_cleanliness_winter/regional/` | `gfx/entities/air_cleanliness_winter_regional_visuals.asset` |
| Regional weather | Snow, cold-rain, ash, and thaw particle entities | `gfx/particles/air_cleanliness_winter/` | `gfx/entities/air_cleanliness_winter_regional_particles.asset` |
| Registered grade and static alternatives | `GFX_air_winter_regional_*` | `gfx/interface/air_cleanliness_winter/regional_grades/` and regional static textures | `interface/air_cleanliness_winter_regional_visuals.gfx` |

The refinery-output and reactor-power dynamic modifiers both use `GFX_air_winter_phase_3`. No additional modifier icon is required for the infrastructure tranche.

The two furnace-shutdown dynamic modifiers use `GFX_air_winter_phase_3`, and `chaosx.fallout.36` and `.37` use `GFX_report_event_air_winter_phase_3`. The heavy-industry tranche requires no new icon, report image, sprite definition, audio, or runtime path.

The two tunnel-school industry modifiers use `GFX_air_winter_phase_2`, and both tunnel-school event blocks use `GFX_report_event_air_winter_phase_2`. No additional icon, report image, sprite definition, or runtime path is required for the mountain-capital tranche.

The guarded-seed industry modifier also uses `GFX_air_winter_phase_2`, and both seed-ledger blocks use `GFX_report_event_air_winter_phase_2`. No additional visual asset or runtime path is required for the seed-ledger tranche.

The island-refugee opening and result use the dedicated `GFX_report_event_air_winter_island_refugee_harbor`. Its source, processed PNG, final DDS, contact-sheet entry, manifest row, and sprite handoff are all stored under the dedicated Fallout asset paths recorded in `docs/assets/air_cleanliness_fallout/manifest.md`.

The Desert City waterworks, supply-relief, and supply-disruption modifiers use `GFX_air_winter_phase_2`. The exact event 13 receipt and event 49 use `GFX_report_event_air_winter_desert_water_convoy`. Generic event 13 routes retain `GFX_report_event_air_winter_phase_2` through the vanilla-style scripted picture selector. The fictional source, processed PNG, 210x176 DDS, ten-image contact sheet, generation prompt, manifest row, and sprite handoff remain inside the dedicated Fallout paths. No zombie file, asset, sprite, audio, or path is used.

The dead-city salvage opening and result use the dedicated `GFX_report_event_air_winter_dead_city_salvage`. Its fictional source, processed PNG, 210x176 DDS, final contact-sheet entry, generation prompt, manifest row, and sprite handoff remain inside the dedicated Fallout paths. No zombie file, asset, sprite, audio, or path is used.

Sources, processed PNGs, contact sheets, provenance, and handoffs live under `docs/assets/air_cleanliness_fallout/`. The central manifest is `docs/assets/air_cleanliness_fallout/manifest.md`.

## Cleanup and reset

- `air_winter_suspend_state` removes runtime phase pressure while preserving long-term state ledgers.
- `air_winter_reset_state` removes runtime variables, response state, phase modifiers, event memories, seasonal marker rows, and state flags. It preserves the reviewed numeric presentation assignment.
- `air_winter_reset_country` removes the country air-operations modifier and clears its cycle receipt, airfield aggregate, bounded reception-state array, Atmospheric Office capability, annual seasonal receipts, nine regional severe-year memories, and country event memory without a world iterator.
- `air_winter_reset_global` resets the existing host and every country retained in the bounded owner and controller registry. It clears the current-year snapshot, transient candidate arrays, and requests state cleanup during the next existing monthly state pass. The monotonic cycle id is retained so old state stamps cannot collide with a restarted cycle.
- Category restoration is explicit and must run before reset when the caller has confirmed category ownership.

## Engine-sensitive proof status

The proof set is:

- `docs/plans/air_cleanliness_fallout_plans/ENGINE_SURFACE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_STATE_LEDGER_INTEGRATION_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_MONTHLY_DETERMINISM_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_2_ISLAND_REFUGEE_SOURCE_AND_POPULATION_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_3_INFRASTRUCTURE_EVENT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_3_HEAVY_INDUSTRY_EVENT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_SEASONAL_RECURRENCE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_MODIFIER_AND_DEATHS_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_RESPONSE_DECISION_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_MAPMODE_MONITORING_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_NORMAL_MAP_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_REGIONAL_VISUAL_WIRING_PROOF.md`

Static documentation and vanilla precedents support the script surfaces. Runtime behavior remains unobserved for the country air-operations modifier, normal-map presentation, controller-side attrition, meta-generated event dispatch, delayed regular event-target retention, exact Desert City subtype routing, scripted event-picture selection, timed response decisions, state-population migration side effects, damaged-building route selection, equipment readback, repairable damage, control-loss cancellation, viewer-specific monitoring scope, and dynamic localisation rendering. Those observations are not claimed as passing evidence.

## Current completion boundary

Implemented in the Air Winter tranche:

- Deterministic phases 0 through 6 and survival ledgers.
- Population loss through the shared Deaths system.
- Building, supply, operations, disease, and category consequences.
- Exact 1081-state regional classification.
- Three winter map modes.
- Four monitoring levels across every winter mapmode tooltip.
- A bounded Air Cleanliness Treaty lifecycle with deterministic formation, invitation receipts, violation memory, and non-periodic annex cleanup.
- A paid Joint Filter Convoy that applies existing response values to one exact Phase 3 or worse priority state and opens a pressure-reducing relief route for up to six months.
- A paid secretariat Verification Mission that offers full access, records-only access, or refusal, then returns an exact seven-day result with government-aware AI and durable memory. Refusal enforces the accepted treaty expulsion, relief-loss, opinion, and embargo consequences without changing Winter or Fallout tuning formulas.
- Invalid treaty routes reconcile before the monthly state pressure pass. Membership loss, annexation, dissolution, and Fallout release active donor projects and exact state reservations through bounded receipts.
- Membership loss, war, founder succession, annexation, dissolution, schema migration, and Fallout release paired inspection receipts through a separate bounded cancellation queue.
- Fifty-two manually authored Air Winter pilot events, including the Phase 1 regional return chain, five durable seasonal recurrence families, the island-refugee migration chain, the exact Desert City water-convoy chain, the ruined major-city salvage chain, the seed-ledger continuation, the mountain-capital tunnel-school chain, and four Phase 3 infrastructure chains.
- Twenty response decision blocks with AI, dynamic costs where state scale applies, one-country ownership, cooldowns, outcomes, and cleanup.
- Dedicated modifier, report-event, map-mode, and response-decision assets.
- Dedicated nine-class regional ground, two-channel weather, vegetation, frozen-water, and thaw assets with a synchronized five-slot lifecycle.
- Static engine proof documents and audit hooks.

Incomplete and not claimed:

- The wider treaty catalogue remains incomplete. Pooled decontamination, seed archive exchange, evacuation corridors, relief votes, major-burner sanctions, and forecast precision beyond shared basic sampling are not implemented.
- Seed-ledger outcomes do not change post-Fallout food recovery. That consumer depends on the approval-gated Fallout numerical contract and remains unimplemented.
- Island-refugee policy and migration memories do not yet feed post-Fallout focuses, successor identity, or migration allocation. Those consumers remain part of the incomplete Fallout country packages and rewrite.
- Additional local Air Winter pressure from active ordinary land combat and an additional winter multiplier on recent strategic-bombing pressure or deaths. Chaos already routes strategic-bombing deaths separately. General air operations use the documented country-scoped aggregate, while exact regional confinement remains unavailable through runtime dynamic modifiers.
- Runtime proof for regional ordinary-map placement, layering, animation, save reconstruction, multiplayer behavior, and performance. The full-screen grade and static accessibility setting also remain unwired.
- Runtime proof for the Phase 1 delayed callback, timed-modifier display and expiry, multiplayer popup presentation, and save recovery remains unobserved.
- The Fallout request coordinator and formula-neutral transition ledgers exist, but the full rewrite, government change, successor allocation, player continuation, and migration are not complete.
- The blackout skeleton exists, while exact input blocking and literal lobby-host authority remain engine blockers.
- The dormant manual scenario substrate has an exact province manifest and seven-day ledger, but the native every-valid-province sweep is not proven and the scenario is not live.
- The Fallout scheduler contracts exist without living-world event content or progress toward the 660-block release floor.
- Survivor focus content, decisions, leaders, units, diplomacy, AI layers, and their remaining dedicated assets are incomplete.

## Future plans and extension suggestions

1. Preserve the normal-map runtime observation checklist and do not report its visual items as tested.
2. Promote the full-screen grade or static accessibility setting only after its interface parent, click behavior, selection rule, and performance contract are proven.
3. Use event memory from the Air Winter pilot as an input to the Fallout cause-memory and successor schedulers.
4. Connect evacuation reception states and refugee pressure to post-rewrite migration without adding another world iterator.
5. Continue Air Winter event depth through manually reviewed tranches, with a depth audit and accepted addendum before each expansion.
6. Add country and regional response variation through the future survivor content layers without replacing state condition with generic national modifiers.
7. Extend the proven treaty registry and state-route transaction into the remaining accepted treaty projects without adding another periodic world scan.

## References consulted

The implementation follows the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, states, and buildings. It also follows the installed official documentation for effects, triggers, modifiers, script concepts, script constants, map modes, and the relevant vanilla decision, event, dynamic modifier, state-category, and entity precedents recorded in the proof files.
