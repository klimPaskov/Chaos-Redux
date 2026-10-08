# Event 033 Acid Rain

Event 033 is a Major Chaos level 2 member of Severe Natural Disasters.
It can fire independently or as the sixth optional cluster member after Event 13's five logical slots, and both routes enter the same host-authoritative generation runtime.
A validated queue containing Event 33 reserves its launch and commits Major pacing once when the cluster launches successfully.
Its delayed Acid Rain member uses the stored batch receipt to record its own firing without another Major reset.

## Player loop

The runtime freezes the valid state set at formation, divides it into seven geographic regions, creates bounded front records, and schedules all future work through the event host.
A front announces its next region roughly one week ahead, visits 60 to 85 percent of the region's eligible states on its first pass, and clears the remainder on its second pass.
Target selection favours states that no front has touched, with an explicit island path and a deterministic endpoint after full frozen-set coverage.
The rain ordinarily disperses only after it has crossed every eligible state.

Countries manage Preparedness from 0 to 100 through four permanent projects: Expand the Shelter Network, Protect Water and Food, Expand Medical and Protective Capacity, and Harden Transport and Infrastructure.
Projects stay open and payable during warnings and exposure; a tier helps only after it completes.
Five urgent actions answer warnings, exposure and storm forecasts: Activate Shelter Protocols, Secure Emergency Water and Food, Open an Emergency Medical Surge, Reroute Transport and Repair Crews, and a state-targeted evacuation.
Four recovery decisions repair the aftermath once no warning, exposure or forecast covers the country: Restore Transport, Decontaminate, Repair Industry, and Demobilize the Emergency Apparatus.
Every decision shows its real cost, duration and blocked state from the same quote that the start transaction charges.

## Response operations

Each national urgent family runs at most once at a time, and different families run side by side.
Shelter Protocols, Water Distribution and Reroute Transport cannot be bought again while their protection is in force, and Medical Surge waits for medical fatigue to end.
Evacuations and state recovery work are per-state operations; the country may run 2, 2, 4 or 8 evacuations and 1, 1, 2 or 3 recovery operations at once by capacity band.
Each operation keeps its paid reservation, debits once and returns its temporary commitments once, and its completion callback resolves only that operation.
Running operations sum their civilian factory commitments into one `acid_rain_action_commitment` modifier.

Severe cells and superstorms name their target states nine days before impact, so an evacuation started on the forecast day or the day after finishes before the first severe pulse.
An evacuation that has run one full day gives half of its mortality reduction to severe and superstorm pulses, and a finished evacuation gives the full reduction; ordinary pulses are unaffected.
While it applies, `acid_rain_evacuation_disruption` lowers local factory output by 15 percent, construction speed by 25 percent and supply by 15 percent.

Restore Transport needs rain-recorded infrastructure or railway damage and clears it on completion, Repair Industry needs recorded factory damage and never restores more than the rain destroyed, and Decontaminate needs the environmental burden every rain impact leaves.
Demobilization opens when no warning, exposure or forecast covers the country, cancels unfinished projects without refunding consumed equipment, keeps paid recovery work running, and grants `acid_rain_demobilized_recovery` (10 percent repair speed, 5 percent construction speed) for 60 days.

## Consequences

Every positive Event 033 mortality pulse enters `apply_exact_state_civilian_population_loss` through one gateway.
The helper removes population first, reads back the observed decrease, and records that value once in the shared Deaths ledger; the same value feeds Event 033 totals, reports and achievement tracking.
A zero result records no deaths, while generation-aware pulse keys make a duplicate call a no-op.

Acute rain bands publish their supply, movement and attrition penalties as state variables; each band value shrinks by 10 percent per controller Transport tier and by another 20 percent while Reroute Transport protection is in force, never below 40 percent of the band value, and a change of controller republishes the band.
Aftermath records per-type damage points for infrastructure, railways and factories, and three aftermath tiers apply `acid_rain_aftermath_1` to `acid_rain_aftermath_3`.

Acid Rain registers humanitarian pressure through `famine_adapt_acid_rain_state`: each exact positive pulse loss, 0.5 percent of a state's population when its aftermath first reaches tier 2 and 1 percent at tier 3, and 2 percent when an evacuation of a state with at least 500,000 people finishes.
Evacuation counts as disaster pressure, not as a migration cohort.
A tier's submission is marked registered only after the famine owner accepts it, so a rejected or rounded-zero request cannot suppress a later valid retry.
This addition path reaches the famine owner's aggregate disaster-pressure channel.
A source-33 reversible pressure ledger and supported recovery-retirement call are not established, so source-specific Humanitarian removal remains unresolved under the consequence repair acceptance.

The dedicated Acid Rain Air source records actual lifetime contamination additions.
Formation requests 75 bp, and from one week after formation, every seven days of the regional and global phases the rain requests Air from the weather on the map: 4, 8, 12 or 16 bp for an active world share below 2, 5 and 10 percent or above, 4 to 16 bp for the average intensity band of the open fronts (Standard under the global layer), 4 bp for two or more fronts, 10 bp for the global layer, and 3 bp per active severe cell or superstorm up to 9 bp, clamped to 8 to 45 bp; a week without acute rain requests nothing.
Every request is clamped against the request itself, the unused share of the 1,500 bp event allowance, and the remaining distance below the 5,000 bp global contamination ceiling.
Dissipation ends the weather runtime but does not erase contamination already added to the shared Air ledger.

## Evolution path

The evolutions are cumulative and can activate while a generation is live.
The evolution log bridge forwards the caller's exact stage and tier to the shared row recorder, replacing any stale ambient context before recording.

- Severe Storm Cells unlock at Rising Chaos and add bounded local severe episodes with nine-day forecasts without replacing the parent front.
- Multiple Weather Fronts unlock at Chaos Tier and add independent second and possible third front records.
- Global Acid Rain unlocks at Totalen Chaos, exposes every frozen valid state through the same exact mortality gateway, retires regional fronts idempotently, allows bounded superstorms with nine-day forecasts, and still reaches guaranteed dissipation.

Evolution unlocks add no Chaos by themselves.
Direct Chaos is applied only at mapped gameplay impacts, and shared Chaos receipts are never counted a second time by Event 033.

## Runtime and save safety

`global.acid_rain_generation_id` separates consecutive generations.
Fronts, warnings, severe cells, superstorms, project jobs, operations, mortality receipts, coverage rows, and cleanup records carry or validate the current generation before changing state.
Every registry array is created at its bound before indexed writes.
The frozen registry carries a region index (`global.acid_rain_region_ordered_states` with per-region bounds), so front warnings, arrivals, departures, footprint growth and retirement, and severe-cell pools read only their region in registry order; the index rebuilds itself for a new generation or an older save.
Region cursors, per-region weights, weighted selection and front-assignment results use caller-owned temporary output storage at every nested return boundary.
The bounded retry uses temporary candidate storage, and selector entry removes its legacy saved scratch without changing recorded front or coverage state.
Cleanup is safe to call repeatedly after dissipation, interruption, host transfer, migration, or reload.
Every inspected base `world_end` setter calls `acid_rain_interrupt_for_world_end` immediately after that commitment and before its next downstream action, and the bounded host worker checks that same interruption entry point before doing weather work.
Terminal packets add no mortality, damage or Air, while administrative closure preserves the actual coverage, population-loss history, contamination and unresolved aftermath without natural-dissipation Chaos credit.
Native iteration helpers use separate reset break storage, so an inherited stop from another effect chain cannot truncate a region, state or participant pass.

## Reports

Each report reads facts stored on the recipient country, or globally for the final summary, just before it is sent.
An advance warning arrives once per front visit that reaches the country's controlled states, including a return to the same region; it names the destination region, the days until arrival, the controlled states there, National Preparedness and the weakest protection.
The arrival report names the front over the state, or the global layer, with its intensity band, and lists the national urgent measures that are not already running or recovering.
A forecast arrives once per severe cell or superstorm episode and names the most populous of the country's forecast states and their count.
The casualty report names the weakest protection and, when there are any, the exposed states the country holds but does not own; the preparation report names the strongest protection, ties going to the heavier component.
An impact report follows the first positive pulse of each episode in the country's territory, with the named state's evacuation status and the days left in the episode.
The departure report gives the length of the exposure that ended, the states still carrying aftermath and their highest tier, and becomes a temporary respite while a warning still covers the country.
The dissipation report lists duration, worldwide deaths, states reached, Air Contamination added, severe cells, superstorms and unresolved aftermath.
The world notices for concentrating rain, severe storm cells, a dividing front, the forming global layer and Global Acid Rain reach every player once per change, whichever country hosts the rain.

## Dashboard

The Acid Rain world map opens from the decision category inlay and from the Event 33 page in Event Details.
When Acid Rain forms, it also opens once for every player whose territory is already warned or exposed.
While a map is open, the host's three-day worker refreshes the shared world view and each viewer's own national strip.
It shows the base map with seven region overlays, visited, ordinary and warning veils, three front markers with warning and severe variants, one severe-storm marker per listed superstorm at the region of its seed state, and the global rain layer.
Every animated marker and the global layer have a still partner that the motion toggle selects.
Hovering a region row shows the states reached, not yet reached and in the rain's path there, and the weather over it: the front over the region with its states under rain now, the states first reached on this visit out of the visit's quota and the states in its severe cells, a front on its way with the days until it arrives, or the global layer.
The Preparedness tooltip lists each component's tier and its points toward the total, and the category status line names exposure, a storm forecast or a warning with the country's counts.
The footer holds Refresh, Back (returning to the decision category or Event Details, whichever opened the map), Details (opening the Event 33 page in Event Details), and the motion toggle.
Opening or refreshing the map runs a read-only projection that cannot advance fronts, add contamination, apply losses, spend resources, or complete work.

## Event Details

Before Acid Rain forms, its Event Details page shows the description only.
While the rain is active, the page adds the formation date, the current phase, world coverage with the reached and total state counts, worldwide deaths, the Air Contamination added and the viewing country's Preparedness.
Once acute rain has closed, it shows the stored outcome instead: whether the rain dispersed or ended early, its duration, deaths, states reached, Air Contamination added, severe cells and superstorms, and the states still under aftermath.
After formation the page also lists the viewing country's ten Acid Rain achievements as earned, open or no longer possible; Under One Sky appears once Global Acid Rain begins, No Severe Ruins once the country records a tier-3 aftermath state, and Five States, Few Dead only once earned.

## Integration surfaces

- Event chain: `events/033_acid_rain.txt`
- Constants: `common/script_constants/033_acid_rain_constants.txt`
- Runtime, aftermath, preparedness, achievement and GUI effects: `common/scripted_effects/033_acid_rain_*.txt`
- Triggers: `common/scripted_triggers/033_acid_rain_*.txt`
- State and country modifiers: `common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt`
- National response decisions: `common/decisions/033_acid_rain_decisions.txt`
- Host scheduling and lifecycle hooks: Event 033 files under `common/on_actions/`
- Dashboard: `interface/033_acid_rain.gui`, `interface/033_acid_rain.gfx`, `common/scripted_guis/033_acid_rain_scripted_guis.txt`, and `common/scripted_localisation/033_acid_rain_scripted_localisation.txt`
- Event Details entry: `interface/chaosx_events_log_popup.gui` and `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- Humanitarian pressure: `famine_adapt_acid_rain_state` in `common/scripted_effects/famine_adapter_effects.txt`
- Achievements: the ten `acid_rain_033_*` entries in `common/achievements/chaos_redux_achievements.txt` with dedicated effects and triggers
- Super-event audio: `sound/033_acid_rain/` with registration in `sound/chaosx_sound.asset`
- Severe forecast cue: the six `chaosx_acid_rain_severe_forecast_cue_<volume>` sound effects in `sound/033_acid_rain_sound.asset`, built from the base game's one-shot thunder samples and listed in the Effects category of `sound/chaosx_sound.asset`; a player hears one with each forecast report for a severe cell or superstorm over their territory, at the super-event audio volume setting and never at x0
- Catalog source: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; the three catalog CSV files are generated exports, and pending row changes are listed in `docs/plans/033_acid_rain_plans/catalog_changes_pending.md`

## Visual asset inventory

All Event 033 sprites are registered in `interface/033_acid_rain.gfx`.

| Family | Files | Sprites and consumers |
| --- | --- | --- |
| Super-event, event, report and news pictures | `gfx/event_pictures/super_events/`, `gfx/event_pictures/033_acid_rain/`, `gfx/event_pictures/news/` | `GFX_super_event_033_acid_rain`; `GFX_event_033_acid_rain_{arrival,warning,severe,shelter,transport,dissipation,global}`; `GFX_report_event_033_acid_rain_{arrival,severe,shelter,transport,dissipation}`; `GFX_news_event_033_acid_rain` and `GFX_news_event_033_acid_rain_global` |
| Decision category and decisions | `gfx/interface/033_acid_rain/decisions/` | `GFX_decision_category_acid_rain` and one `GFX_decision_acid_rain_<group>_<name>` icon per decision, named after the decision identifier |
| Modifiers | `gfx/interface/033_acid_rain/modifiers/` | `GFX_modifier_acid_rain_{ordinary,strong,severe_cell,global_layer,global_superstorm}` and `GFX_modifier_acid_rain_aftermath_{1,2,3}` |
| Dashboard art | `gfx/interface/033_acid_rain/gui/` | `GFX_acid_rain_map_base`, `GFX_acid_rain_region_overlay_1` to `_7`, `GFX_acid_rain_{visited,warning,ordinary,global}_veil`, marker, card, coverage, Preparedness badge and component pip sprites |
| Animations | `gfx/interface/033_acid_rain/animation/` | `GFX_acid_rain_{front,warning,severe,global}_animated` frame sheets with `GFX_acid_rain_*_static` still partners |
| Achievements | `gfx/achievements/` | one normal, one grey and one not-eligible DDS for each of the ten `acid_rain_033_*` achievements |

The global rain layer is an eight-frame 4480x300 sheet at 4 FPS of three separated cloud banks that leaves the map readable, with frame 000 as its still partner.
The warning veil keeps defringed art at a mean alpha of about 46 so continents stay readable beneath the warning bands.
`GFX_acid_rain_global_veil` is registered but no window element displays it.
Source, generation, processing, alpha and checksum evidence lives under `docs/assets/033_acid_rain/`, which is a local working area outside Git; the durable record of the global layer and veil is agent decision D17 in `docs/plans/033_acid_rain_plans/agent_decisions_2026-10-04.md`.
The row-level record of retired prototype art is [prototype presentation retirement](../../plans/033_acid_rain_plans/validation/033_acid_rain_legacy_asset_retirement.md).

## Verification scope

`.tools/validation/validate_033_acid_rain.py` checks the source contracts, coverage and movement model, Air caps and the exact-loss helper contract.
The behavior described above records source contracts and implementation, with design authority recorded separately in `docs/plans/033_acid_rain_plans/agent_decisions_2026-10-04.md` and the accepted specs.
For the 2026-10-07 reconciliation, the parent reports current-source exact-helper replay and synthetic movement, Air and lifecycle passes.
Those fixtures do not execute HOI4, and no live-game evidence or clean error-log proof was furnished for this review.
Executed population removal, save and reload, multiplayer presentation, decision AI behavior, engine performance, dashboard presentation, animation playback, and listening to the super-event audio and severe forecast cue remain separate verification gates.
Earlier GUI renders recorded in D16/D17 were refused at 1920x1080 by the aggregate pixel budget and succeeded at 1366x768 for their named scenarios and source revisions.
That historical limit does not establish current route health, resolution support or final UI acceptance.
The 2026-10-04 decision-AI `hoi4.probability_inspect` attempts recorded in D13/D15 returned `INTERNAL_ERROR` and yielded no baseline or comparison.
The current probability and UI audits retain their own scenario-specific handoffs for parent review, and their results are not inferred here.
Humanitarian source-specific retirement remains unresolved even though the addition adapter exists in source.
See [the current documentation reconciliation](../../plans/033_acid_rain_plans/subagent_handoffs/documentation_current_reconciliation_2026_10_07.md) for claim dispositions and evidence limits.

## Future extensions

Future work could add region-specific diplomatic relief requests, country-specific atmospheric research responses, and post-event reconstruction stories keyed to retained aftermath tiers.
These are optional expansions and should preserve the frozen-state, exact-loss, Air-cap, generation, and host-authority contracts described above.
