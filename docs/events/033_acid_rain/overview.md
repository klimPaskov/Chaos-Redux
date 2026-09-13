# Event 033 Acid Rain

Event 033 is a Major Chaos level 2 member of Severe Natural Disasters. It can fire independently or as the sixth optional cluster member after Event 13's five logical slots, and both routes enter the same host-authoritative generation runtime.

## Player loop

The runtime freezes the valid state set at formation, divides it into seven geographic regions, creates bounded front records, and schedules all future work through the event host. A front announces its next region roughly one week ahead, visits 60 to 85 percent of the region's eligible states on its first pass, and clears the remainder on its second pass. Target selection favors states that no front has touched, with an explicit island path and a deterministic endpoint after full frozen-set coverage.

Countries manage Preparedness from 0 to 100 through four permanent projects: shelter networks, protected water and food, medical and protective capacity, and transport and infrastructure resilience. Five urgent actions answer warnings or active exposure, while four recovery actions reduce the retained aftermath after the weather dissipates. Project commitments, cancellations, refunds, durations, valid-target proofs, and AI reserve checks use the decision matrix in the Event 033 specification package.

The dedicated Acid Rain Air source records actual lifetime contamination additions in basis points. Every request is clamped against the request itself, the unused share of the 1,500 bp event allowance, and the remaining distance below the 5,000 bp global contamination ceiling. Dissipation ends the weather runtime but does not erase contamination already added to the shared Air ledger.

## Mortality contract

Every positive Event 033 mortality pulse enters `apply_exact_state_civilian_population_loss` through one gateway. The helper's `state_civilian_population_loss_applied` result is the only accepted death receipt: the affected state's population falls by that value, and that same value is recorded once in the shared Deaths ledger, Event 033 totals, reports, and achievement tracking. A zero result records no deaths, while generation-aware pulse keys make a duplicate call a no-op.

## Evolution path

The evolutions are cumulative and can activate while a generation is live.

- Severe Storm Cells unlock at Rising Chaos and add bounded local severe episodes without replacing the parent front.
- Multiple Weather Fronts unlock at Chaos Tier and add independent second and possible third front records.
- Global Acid Rain unlocks at Totalen Chaos, exposes every frozen valid state through the same exact mortality gateway, retires regional fronts idempotently, allows bounded superstorms, and still reaches guaranteed dissipation.

Evolution unlocks add no Chaos by themselves. Direct Chaos is applied only at mapped gameplay impacts, and shared Chaos receipts are never counted a second time by Event 033.

## Runtime and save safety

`global.acid_rain_generation_id` separates consecutive generations. Fronts, warnings, severe cells, superstorms, project jobs, actions, mortality receipts, coverage rows, and cleanup records carry or validate the current generation before changing state. Registries are bounded by frozen-state, front, action, and storm limits, and cleanup is safe to call repeatedly after dissipation, interruption, host transfer, migration, or reload.

The scripted GUI reads projected values only. Opening the Acid Rain dashboard from its decision category or Event Details runs a read-only refresh that cannot advance fronts, add contamination, apply losses, spend resources, or complete work.

## Integration surfaces

- Event chain: `events/033_acid_rain.txt`
- Constants: `common/script_constants/033_acid_rain_constants.txt`
- Runtime effects and triggers: `common/scripted_effects/033_acid_rain_*.txt` and `common/scripted_triggers/033_acid_rain_*.txt`
- National response decisions: `common/decisions/033_acid_rain_decisions.txt`
- Host scheduling and lifecycle hooks: Event 033 files under `common/on_actions/`
- Dashboard: `interface/033_acid_rain.gui`, `interface/033_acid_rain.gfx`, and `common/scripted_guis/033_acid_rain_scripted_guis.txt`
- Event Details entry: `interface/chaosx_events_log_popup.gui` and `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- Achievements: Event 033 entries in `common/achievements/chaos_redux_achievements.txt` with dedicated effects and triggers
- Super-event audio: `sound/033_acid_rain/` with registration in `sound/chaosx_sound.asset`
- Catalog source: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; the three catalog CSV files are generated exports

## Visual asset inventory

Event, report, news, and super-event scenes live under `gfx/event_pictures/` and are registered by `interface/033_acid_rain.gfx`. Their stable consumers include `GFX_super_event_033_acid_rain`, the arrival, warning, severe, shelter, transport, dissipation, and global event sprites, and the regional and global news sprites.

The Acid Rain dashboard uses `gfx/interface/033_acid_rain/gui/` for the base map, seven region overlays, coverage and phase veils, front and warning markers, card backgrounds, coverage meters, the Preparedness badge, and component pips. Animated source frames and final sheets live under `gfx/interface/033_acid_rain/animation/`; their registered sprite identifiers retain static DDS fallbacks for consumers that cannot animate.

National-response decision icons live with the Event 033 interface assets and use stable per-decision identifiers. Achievement art consists of one normal, one grey, and one not-eligible DDS for each of the ten `acid_rain_033_*` achievement identifiers under `gfx/achievements/`.

Source, rights, generation, processing, alpha, checksum, uniqueness, and handoff evidence belongs under `docs/assets/033_acid_rain/`.

## Future extensions

Future work could add region-specific diplomatic relief requests, country-specific atmospheric research responses, and post-event reconstruction stories keyed to retained aftermath tiers. These are optional expansions and should preserve the frozen-state, exact-loss, Air-cap, generation, and host-authority contracts described above.
