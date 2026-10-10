# Event 037: Mysterious People

## What the event is

Mysterious People is a repeatable Minor event (Chaos level 1, catalog cluster 15 Sudden Abundance at Medium severity).
Each firing adds real civilian population to every inhabited state in the world: people with homes, families and histories that their neighbours remember.
Each wave arrives unsettled, and every country has to house and employ its newcomers before the next wave.
Countries that settle them gain a larger workforce and, over time, more recruits, while countries that let them pile up slide into crowding, unrest, hunger and flight through the shared Famine and Migration systems.
The event never explains where the newcomers come from.

The design source is `docs/specs/037_mysterious_people_specs/`.
The legacy two-event stub (2,500,000 manpower for one random country, an enslavement option and an alien headline) is retired completely.

## Event map

| ID | Role |
| --- | --- |
| `chaosx.nr37.1` | Hidden entry that runs the world manifestation transaction |
| `chaosx.nr37.2` | Manifestation report, one per human country with newcomers, stage-specific text |
| `chaosx.nr37.3` to `.5` | Evolution reports to human players |
| `chaosx.nr37.6` | Hidden monthly host pulse, self-rescheduling every 30 days |
| `chaosx.nr37.7` | Hidden flavour dispatcher, one roll per country per firing, 20 to 60 days after it |
| `chaosx.nr37.8` | Hidden Newcomers modifier refresh when a timed workforce boost ends |
| `chaosx.nr37.10` to `.26` | Seventeen flavour events, each about one state (or one other country for `.17`) |
| `chaosx.news.42` | World news, first manifestation only |

## Runtime flow

### Firing

`mysterious_people_run_manifestation` (`common/scripted_effects/037_mysterious_population_effects.txt`) is the only world-wide pass in the design.

1. On the first firing above an evolution threshold, every enabled eligible evolution records in order before the grant (zero Chaos).
2. Country counts are reset for every country that held newcomers.
3. One `every_state` pass visits each state that holds newcomers or can receive them (`humanitarian_state_is_valid` and at least 5,000 people). For each state it settles the backlog for the days since its last settlement, applies one grant, refreshes the settlement rate and pressure, and adds the state to its owner's counts and hotspot candidates.
4. Each country with newcomers is finalized: hotspots are sorted and flagged, the rest-of-country backlog and rate are stored, pressure and the Newcomers modifier refresh, the country registers for the pulse when it has unsettled newcomers, the mission may start, achievements are checked, and the flavour dispatcher is scheduled.
5. World share, the four Chaos milestones, the Event Logs history row, the pulse chain and the reports follow.

The grant per state is `min(cap, max(P x ratio, min(floor, P x small-state ceiling)))` with the stage table in `mysterious_people_grant`.
It is applied through the new neutral gain helper `apply_state_population_gain_without_recruitable_manpower_gain`, and every ledger step uses the measured applied amount.

### Ledger

Each state stores a newcomer share (fraction of its living population) and an unsettled backlog in thousands.
Because the share is a fraction, every ordinary loss and every proportional move keeps the newcomer count inside real population without adapters in other systems.
The backlog is clamped to the derived newcomer count after every read.

Settlement per month is `population x 1% x (0.6 + 0.08 x infrastructure) x (1 + project bonuses) x hunger 0.5 x occupation 0.5 x flavour factor`, then the owner's national factor (Open Integration 1.25, Restricted Registration 0.75, Registration Drive 1.5, origin register 0.667, which together with Restricted Registration halves settlement).

### Monthly pulse

`chaosx.nr37.6` runs on the global host every 30 days and touches only `global.mysterious_people_countries` (countries with unsettled newcomers) and at most three hotspot states each.
Hotspots settle exactly, run the Famine and Migration adapters, and drop out when settled (a hotspot with a running project stays until the project ends).
The rest of each country's backlog falls by its stored rate.
Human countries with newcomers are also read for the Room for Everyone streak.
A duplicate chain exits without rescheduling, and a firing restarts a chain that has stopped.
Evolution pacing runs from the same pulse.

### Ownership changes

`on_state_control_changed` moves a ledger state's counts from the credited owner to the new owner (`mysterious_people_on_state_owner_changed`).
The pulse catches hotspots that changed hands in a peace deal.
A non-hotspot state transferred at peace without a control change keeps counting for its old owner until the next firing recounts it exactly.

## Overpopulation Pressure and consequences

State pressure is `clamp(100 x unsettled / (population x 0.25))` plus 10, 20 or 30 at acute shortage, famine or catastrophic famine.
National pressure is the population-weighted base plus a quarter of the gap to the worst hotspot.
Stages: Absorbing below 20, Strained, Overcrowded from 40, Emergency from 60, Breakdown from 80.

The decision category header shows the newcomers living in the country, pressure with its stage, and the stance, followed by the unsettled newcomers and the most crowded state.

One dynamic modifier, Newcomers (`mysterious_people_newcomers`), carries every national effect:

- construction speed `+0.4 x settled share` up to 10% and factory output `+0.2 x settled share` up to 5%, full at Absorbing, half at Strained, none from Overcrowded, doubled by a mission success or The Country That Managed
- stability `-0.25%` per point above 40 up to `-15%`, halved under Restricted Registration
- construction `-0.5%` per point above 60 up to `-20%`
- `conscription_factor` equal to minus the unsettled share of the country population (see Recruitable manpower below)

### Famine and Migration

Hotspots at pressure 60 or more top up a food-need shock to `pressure - 40` through `famine_request_event_pressure` (8 to 24 food-security points, below supply strain alone).
Hotspots at 80 or more request flight for 2% of their unsettled newcomers a month through `migration_request_flight_pressure`, unless a flavour choice closed the station.
`mysterious_people_on_civilian_transfer`, called once in `civilian_transfer_finalize`, lowers the origin backlog by the measured departures and blends the destination share with the origin share for the measured survivors.
Event 037 writes no Famine or Migration ledger, food value, death record or Condemnation source.

The proposed `population_surge` pressure source is not added; the requests use the existing `event` source.

## Recruitable manpower

The spec asks whether recruitable manpower grows gradually once the instant gain from a positive state `add_manpower` is removed.

Evidence gathered:

- `effects_documentation.md` documents `add_manpower` in state scope only as adding manpower locally to the state.
- `00_defines.lua` defines `BASE_MOBILIZATION_SPEED`, and the modifier list has `mobilization_speed`, `conscription`, `conscription_factor`, `recruitable_population` and `recruitable_population_factor`. `dynamic_variables_documentation.md` describes `max_available_manpower` as including manpower still being drafted after a conscription change.
- Plain-text saves (`trailer_100` to `trailer_160`, 1936) store a `manpower_pool = { available locked total }` per state and no country pool. Over a year a Swiss state under a recruitable penalty modifier moved from 0.9 to 0.9344 to 0.9356 locked share toward its new target, so the engine converges a state's recruitable pool toward a modifier-defined target over time rather than at once.

No documentation states what happens to a pool that a script lowered below that target with a country-scope `add_manpower`, and agents may not run the game, so gradual recovery after the instant gain is removed cannot be proven from source.
The closest faithful mechanism is used, and it is the spec's recorded fallback: the Newcomers modifier carries `conscription_factor = -(unsettled newcomers / country population)`, so unsettled newcomers stay out of the engine's recruitable target and enter it as they settle, through the same convergence the save data shows.
The instant gain is still removed at the grant.
Live confirmation that recruits appear as the backlog falls is user-owned.

## Decisions and mission

Category `mysterious_people_category` (`common/decisions/037_mysterious_population_decisions.txt`), static picture, no scripted GUI.
It is visible while the country has newcomers and has unsettled newcomers, a running project or the mission.

| Action | Gate | Cost | Result |
| --- | --- | --- | --- |
| Open Integration / Restricted Registration | stance unlocked | 50 political power, 180-day lock | Settlement x1.25 with the full unrest, or x0.75 with half the unrest |
| Registration Drive | national pressure Strained | 30 to 90 political power by backlog, 180-day cooldown | Settlement x1.5 everywhere for 60 days |
| Requisition Empty Property | hotspot Overcrowded, once a year per state | none upfront | 20% of the state's backlog settles, stability -2% for 90 days |
| Emergency Housing | hotspot Strained, once per state | 25 political power, 2 to 6 civilian factories for 90 days | 30% settles and +25% settlement afterwards |
| Roads and Water | hotspot Strained, once per state | 25 political power, 3 to 8 civilian factories for 150 days | +1 infrastructure and +25% settlement afterwards |
| Build a New City | Evolution III, hotspot over 1,000,000 people, once per state | 100 political power, 8 to 15 civilian factories for 300 days | 50% settles, +1 infrastructure, +1 civilian factory, +1 building slot, +50% settlement |

Humans pick one hotspot from up to three rows, see its four values (newcomers, unsettled, crowding stage, the main thing slowing settlement or the hunger or flight that lowered it), and close it to return to the national view.
AI evaluates every hotspot directly.
At most three state projects run at once and one per state.
Project factory commitment is the `mysterious_people_projects` dynamic modifier (`civilian_factory_use` from the sum of running quotes), because a decision `modifier` block cannot scale with the backlog.
Projects fail closed without refund when their state changes owner or controller.

Absorb the Newcomers starts after a manifestation that leaves the country at Strained or worse, completes as soon as pressure falls below the lower bound of the starting stage, and lasts 180 days.
Success doubles the workforce bonus for 180 days and counts toward Three Censuses, failure costs 5% stability for 90 days.

## Flavour pool

After each firing every country with newcomers rolls once, 20 to 60 days later.
The dispatcher (`mysterious_people_dispatch_flavour`) builds the pool of events whose state trigger (`mysterious_people_flavour_state_<id>`) holds for an owned state, excludes the last four events the country saw, picks one uniformly and saves the state as `mysterious_people_flavour_state`.
Every option except the five plain declines (`.10b`, `.13b`, `.14b`, `.17b`, `.18b`) changes something visible: settlement in the state, a timed settlement factor, a project discount, stability, factory output, opinion, political power or world tension.
`.24` can switch a non-democratic country to Restricted Registration for free and slow settlement everywhere for a year.
`.26` fires once for a country that has kept pressure below Strained for 180 days at Evolution III with newcomers at least a quarter of its population.

## Evolutions

| Evolution | Chaos | Base delay | Change |
| --- | --- | --- | --- |
| I Population Surge | 200 | 90 days | grants 6% |
| II Overpopulation Crisis | 400 | 120 days | grants 12% |
| III Humanity Multiplies | 600 | 150 days | grants 25%, Build a New City, origin politics |

Delays come from `common/mtth/037_mysterious_population_mtth.txt`: x0.75 while any country is at Emergency, x0.75 when living newcomers exceed 5% (II) or 10% (III) of the world, x1.5 while no country is above Strained, then a random 0.75 to 1.25 spread with a 30-day floor.
A disabled stage never records, and a higher enabled stage carries the lower grant scales.

## Event-owned Chaos

| Milestone | Chaos |
| --- | --- |
| First manifestation | +2 |
| Living newcomers first reach 5% of world population | +3 |
| 10% | +5 |
| 25% | +10 |

Each is a one-shot global flag checked at the end of a firing, recorded through `add_chaos_meter_value` with reasons `mysterious_people_first` (230) and `mysterious_people_share` (231).
Deaths among newcomers reach Chaos through the owner of each cause.

## Event Logs

Event 37 is registered as repeatable and in the reworked default-enabled list.
The shared recorder calls `mysterious_people_bind_history_sequence`, and the transaction stores one history row per firing (people created, regions, stage, living newcomers).
`mysterious_people_load_open_history_payload` loads a selected row for Event Details, which shows the viewer's own count when the row is the latest firing.
Evolution titles and bodies are wired on all five Event Logs surfaces.

## Achievements

`037_room_for_everyone`, `037_a_billion_more` and `037_three_censuses` are in `common/achievements/chaos_redux_achievements.txt`, set by flags from the pulse, the firing and the mission.

## AI

- Stance: `mtth:mysterious_people_ai_open_stance` and `..._restricted_stance` (democracy x3, fascism x0.2 or x3, stability above 60% or below 40% while Overcrowded). A country that already chose a stance scores zero for the other one unless it is a stable democracy (switching to Open) or fascist or unstable and crowded (switching to Restricted), so the stance does not flip every lock period.
- Projects weigh capital x3, urban x2, industrial x1.5, Emergency x2. Roads and Water leads below infrastructure 5 and Emergency Housing above it. A country at war with fewer than 10 free civilian factories takes no project and favours the drive and requisition. New City needs 25 civilian factories.
- Requisition is x0.1 above 50% stability and x3 at Emergency.

## Assets

| Sprite | File |
| --- | --- |
| `GFX_report_mysterious_people_manifestation` | `gfx/event_pictures/037_mysterious_population/mysterious_people_manifestation.dds` (210x176) |
| `GFX_news_mysterious_population` | `gfx/event_pictures/037_mysterious_population/news_mysterious_population.dds` (397x153, replaced: the old picture showed an alien figure) |
| `GFX_mysterious_people_category_picture` | `gfx/interface/decisions/037_mysterious_population/mysterious_people_category_picture.dds` (114x101) |
| `GFX_mysterious_people_category` | `.../mysterious_people_category.dds` (52x40) |
| stance, action, mission and modifier icons | `.../mysterious_people_<name>.dds` (32x32) |
| achievement triplets | `gfx/achievements/037_<id>(_grey, _not_eligible).dds` (64x64) |

All sprites are registered in `interface/037_mysterious_population.gfx`.
Flavour events also use vanilla report pictures.

## Supporting files

- Constants: `common/script_constants/037_mysterious_population_constants.txt`
- Effects: `037_mysterious_population_effects.txt`, `037_mysterious_population_decision_effects.txt`, `037_mysterious_population_cxt_effects.txt`
- Triggers, scripted localisation, dynamic modifiers, MTTH, opinion modifiers, on_actions, CXT carrier idea and localisation under the `037_mysterious_population` stem
- Shared: `chaosx_dynamic_effects.txt` (gain helper), `civilian_transfer_effects.txt` (one hook), Event Logs effects and scripted localisation, settings triggers, Chaos Meter constants and localisation, achievements

## Limitations

- Recruitable manpower recovery is designed through the engine's recruitable target and is not live-verified (see above).
- Per-state settlement between firings is applied lazily at the owner's current national factor, so a stance or drive change affects non-hotspot states from the next settlement onward.
- Sudden Abundance (`event_cluster_id.sudden_abundance`, runtime ID 15 as in the workbook) is registered as a repeatable cluster at Chaos level 1 with a 120-day cooldown. Event 037 is its only runtime member (required, Medium, so the cluster opens from Chaos tier 1), and one activation runs one world transaction through the normal dispatcher. Events 19, 29, 32, 42, 56 and 64 join when their own packages register member rows.

## Open tuning notes and future ideas

- Tune the inhabited threshold, grant table and settlement rate against observed campaigns.
- A `population_surge` pressure source would let Famine and Migration reports name crowding, if their owners accept it.
- Cross-event callback lines for Events 019 and 030 in the flavour pool remain a possible addition.
