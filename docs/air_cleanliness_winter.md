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
3. `air_winter_finalize_monthly_cycle = yes` after the block.

The Air Winter helpers do not create another state or country iterator. Their date guards make repeated calls on the same date idempotent. Global pressure reads the completed contamination-state counts from the preceding monthly pass before the host rebuilds those counts.

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

Global pressure begins with `global.air_contamination_bp / 100`. That total includes the small capped wildfire-smoke and volcanic-ash contribution documented in `docs/air_cleanliness_natural_sources.md`. It adds bounded pressure from fallout states, chemical contamination states, Air Cleanliness thresholds, and Final Silence. Global mitigation is subtracted before clamping.

Local pressure adds nuclear fallout, nuclear intensity, chemical contamination, urban density, weak infrastructure, occupation disruption, and adjacency to phase 4 through 6. Adaptation, food, shelter, reclamation, and relief routes reduce pressure. Runtime pressure does not infer geography or climate.

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

Phases 1 through 6 apply one mutually exclusive state modifier. Each phase changes local manpower, supply, controller and enemy movement, controller and enemy attrition, building speed, state repair speed, resources, and air operations. Environmental movement and attrition effects apply to both operational sides.

Disease pressure is calculated separately so food, shelter, exposure, adaptation, water, and reclamation remain meaningful within a phase. The disease modifier reads bounded state variables for attrition and local manpower.

The repair fields use the documented `state_repair_speed_<Building>_factor` family for infrastructure, railways, civilian factories, military factories, air bases, dockyards, and supply nodes. Country-only industry repair fields are not used. Vanilla applies `attrition_for_controller` in state dynamic modifiers, but the generated modifier catalogue omits its state category. The unobserved runtime boundary is recorded in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_MODIFIER_AND_DEATHS_PROOF.md`.

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

Death reason 17 is integrated into the reason schema, country cause totals, detail arrays, sorting, map views, and localisation. Event-specific Air Winter losses use the same exact helper and reason. The monthly and event paths both stop population loss when `settings_chaos_deaths_disabled` is active, matching the player-facing Deaths setting.

### Operations and response decisions

The response category provides 17 state-target actions. Sixteen are timed projects. They cover reception-state designation, respirators, clinics, air sampling, crop protection, ash-route clearance, rail protection, airfield closure, evacuation planning, shelter law, greenhouse refuge, controlled evacuation, medical triage, abandonment vote, bunker sealing, final evacuation, and mass decontamination.

Costs use exact affordability triggers and exact payment effects. Timed projects set a state lock on selection, clear it on completion, and clear it on cancellation. AI weights respond to population, survival, war strain, resource strain, infrastructure role, and prior planning. Cooldowns and completion flags prevent reward loops.

Controlled and final evacuations subtract and add the same rounded state-population amount. The state-population route is documented, while its recruitable-manpower side effect remains unobserved and is not claimed. The exact observation plan is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_RESPONSE_DECISION_PROOF.md`.

The abandonment vote fires `chaosx.fallout.201`. Mass decontamination fires `chaosx.fallout.202`. Decontamination succeeds only when the selected state meets the disclosed Survival, Adaptation, and Water Security thresholds. Failure applies state damage and registers civilian losses through the Deaths system.

## Event pilot and scheduler

`events/fallout_world_end_events.txt` owns the namespace `chaosx.fallout`. The current Air Winter pilot contains 32 manually authored event blocks:

- 30 phase, regional, crisis, delayed-result, government, and recovery blocks.
- 2 terminal response result blocks for abandonment and decontamination.

The pilot covers every phase, all nine presentation classes through regional routing, city, food, transport, shelter, disease, government continuity, recovery, and several delayed deterministic results. Event text uses state names and government-aware authority terms.

`air_winter_schedule_phase_event` runs from the existing monthly state update. It applies one country event per worsening phase, a 46-day country cooldown, one recovery arc cap, and reviewed regional routing. A missed phase remains eligible after the cooldown expires. It saves regular event targets and uses `meta_effect` to inject the selected numeric event ID. No second country or state iterator is introduced.

Delayed events retain their originating state target through the event chain. Their event triggers require the saved state to remain owned by the saved country and require a live branch flag. State reset or ownership change cancels the branch and its stored owner. Country phase memories, cooldown flags, and recovery counts are cleared separately through `air_winter_reset_country`.

This pilot is not the Fallout living-world scheduler. It does not count toward a claim that the 660-event Fallout release floor is complete. The event-target and scheduler proof is in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_EVENT_SCHEDULER_PROOF.md`.

## Map modes and normal-map proof

Three registered map modes expose:

- Current phase, target phase, trend, regional class, damage, and death pressure.
- Immediate exposure and expected monthly exposure movement.
- Survival value and all major survival inputs.

Their files are:

- `common/map_modes/chaosx_state_map_modes.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- `localisation/english/chaosx_map_modes_l_english.yml`
- `interface/mapmodes_interface.gfx`
- `gfx/interface/mapmode/custom/air_winter_*`

The normal-map route has a bounded state 64 proof. A scripted effect creates and removes a dedicated state-bound entity that uses the vanilla `snow_small_particle` entity. A proof GUI drives the effect manually. Official effect signatures and an approved normal-mapped entity precedent establish the ordinary-map route. This is not final regional presentation, and no runtime visual observation is claimed.

Proof files are:

- `gfx/entities/air_cleanliness_winter_proof.asset`
- `common/scripted_effects/air_cleanliness_winter_visual_effects.txt`
- `common/scripted_guis/air_cleanliness_winter_visual_proof_scripted_gui.txt`
- `interface/air_cleanliness_winter_visual_proof.gfx`
- `interface/air_cleanliness_winter_visual_proof.gui`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_NORMAL_MAP_PROOF.md`

Regional snow, frost, cold rain, ash, dead vegetation, frozen water, dim light, and thaw remain pending. Universal snow and a mapmode-only substitute are not approved.

## Visual assets and sprite registry

All current final Air Winter art is Fallout-owned and uses dedicated paths.

| Use | Sprite identifiers | Runtime path | Registry |
| --- | --- | --- | --- |
| Phase modifiers | `GFX_air_winter_phase_1` through `GFX_air_winter_phase_6` | `gfx/interface/air_cleanliness_winter/modifiers/` | `interface/air_cleanliness_winter.gfx` |
| Disease modifier | `GFX_air_winter_disease_pressure_state` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_disease_pressure_state.dds` | `interface/air_cleanliness_winter.gfx` |
| Report events | `GFX_report_event_air_winter_phase_1` through `GFX_report_event_air_winter_phase_6`, plus `GFX_report_event_air_winter_recovery` | `gfx/event_pictures/fallout/air_winter/` | `interface/air_cleanliness_winter.gfx` |
| Map mode buttons | Selected and deselected sprites for phase, exposure, and survival | `gfx/interface/mapmode/custom/` | `interface/mapmodes_interface.gfx` |
| Response decisions | `GFX_decision_air_winter_*` | `gfx/interface/air_cleanliness_winter/decisions/` | Pending registration in `interface/air_cleanliness_winter.gfx` |

Sources, processed PNGs, contact sheets, provenance, and handoffs live under `docs/assets/air_cleanliness_fallout/`. The central manifest is `docs/assets/air_cleanliness_fallout/manifest.md`.

## Cleanup and reset

- `air_winter_suspend_state` removes runtime phase pressure while preserving long-term state ledgers.
- `air_winter_reset_state` removes runtime variables, response state, phase modifiers, event memories, and state flags. It preserves the reviewed numeric presentation assignment.
- `air_winter_reset_country` clears the calling country's reception-state array and country event memory without an iterator.
- `air_winter_reset_global` invokes the country reset for the existing host and clears Air Winter global state without performing a state loop.
- Category restoration is explicit and must run before reset when the caller has confirmed category ownership.

## Engine-sensitive proof status

The proof set is:

- `docs/plans/air_cleanliness_fallout_plans/ENGINE_SURFACE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_STATE_LEDGER_INTEGRATION_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_MODIFIER_AND_DEATHS_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_RESPONSE_DECISION_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_NORMAL_MAP_PROOF.md`

Static documentation and vanilla precedents support the implemented script surfaces. Runtime behavior remains unobserved for normal-map presentation, controller-side attrition, meta-generated event dispatch, delayed regular event-target retention, timed response decisions, state-population migration side effects, and dynamic localisation rendering. Those observations are not claimed as passing evidence.

## Current completion boundary

Implemented in the Air Winter tranche:

- Deterministic phases 0 through 6 and survival ledgers.
- Population loss through the shared Deaths system.
- Building, supply, operations, disease, and category consequences.
- Exact 1081-state regional classification.
- Three winter map modes.
- Thirty-two manually authored Air Winter pilot events.
- Seventeen response decisions with AI, costs, cooldowns, outcomes, and cleanup.
- Dedicated modifier, report-event, and map-mode assets.
- Static engine proof documents and audit hooks.

Incomplete and not claimed:

- Final regional normal-map visuals. The documented route is proven, while its visual runtime checklist remains unobserved.
- Dedicated decision icon registration until the current asset tranche completes.
- Fallout request coordinator and request ownership cleanup.
- Fallout full-screen blackout, input blocking, recovery, authority, and sound.
- Manual thermonuclear scenario and exact every-valid-province strike ledger.
- Seven-day post-strike handoff.
- Deterministic Fallout rewrite, government change, successor allocation, player continuation, conflict ledger, and migration.
- Fallout living-world scheduler and the 660 manually reviewed event floor.
- Survivor focus content, decisions, leaders, units, diplomacy, and AI layers.
- Fallout audio, blackout, successor, focus, character, and living-world asset packages.

## Future plans and extension suggestions

1. Implement distinct regional normal-map packages for the nine presentation classes and phase transitions, including thaw cleanup, through the documented state entity route.
2. Preserve the normal-map runtime observation checklist and do not report its visual items as tested.
3. Use event memory from the Air Winter pilot as an input to the Fallout cause-memory and successor schedulers.
4. Connect evacuation reception states and refugee pressure to post-rewrite migration without adding another world iterator.
5. Expand Air Winter event depth only after the pilot audit and accepted improvement addendum are resolved.
6. Add country and regional response variation through the future survivor content layers without replacing state condition with generic national modifiers.

## References consulted

The implementation follows the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, states, and buildings. It also follows the installed official documentation for effects, triggers, modifiers, script concepts, script constants, map modes, and the relevant vanilla decision, event, dynamic modifier, state-category, and entity precedents recorded in the proof files.
