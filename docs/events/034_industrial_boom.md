# Event 34 Industrial Boom

Industrial Boom is a Minor Repeatable event at Chaos level 1 and the Low member of the Positive Economy cluster.
One major power or player government receives an industrial acceleration far beyond what its factories, railways and workers should allow.
The country manages one public value, Overheating, and lands the boom deliberately, is forced down, or crashes into Event 35 Great Depression 2.0.
The design source is [docs/specs/034_industrial_boom_specs/](../specs/034_industrial_boom_specs/034_industrial_boom_spec_index.md).

## Event map

| Event | Role |
| --- | --- |
| `chaosx.nr34.1` | Hidden entry on the selected country. Opens the boom |
| `chaosx.nr34.2` | Opening report (baseline and three evolved-opening texts), queues `chaosx.news.39` |
| `chaosx.nr34.3` | Hidden crash: fills the live snapshot fields, freezes, ends the package and delivers to Event 35 |
| `chaosx.nr34.4` | Bounded private delivery retry |
| `chaosx.nr34.5` | Hidden weekly pulse of one active boom |
| `chaosx.nr34.6` to `.8` | Band reports for Strained, Dangerous and Critical, one per upward entry |
| `chaosx.nr34.9` to `.11` | Controlled, rough and forced landing reports |
| `chaosx.nr34.12` | Foreign orders accepted (human supplier) |
| `chaosx.nr34.13` to `.15` | Evolution reports. `.15` chooses the Evolution III spread policy |
| `chaosx.nr34.16` | Industrial project choice for a region |
| `chaosx.nr34.17` | Declare a Miracle Region choice |
| `chaosx.nr34.18` | Hidden deferred shock from an incident response |
| `chaosx.nr34.20` to `.24` | Baseline incidents: Rail Congestion, Material Shortfall, Plant Accident, Labour Dispute, Maintenance Failure |
| `chaosx.nr34.25` to `.27` | Speculative Mania incidents: Order-Book Frenzy, The Profitable Shell, Restraint Backlash |
| `chaosx.nr34.28` to `.30` | Industrial Miracle incidents: The Railway Completed Overnight, Materials That Should Not Exist, The Impossible Schedule |
| `chaosx.nr34.31` to `.33` | Runaway incidents: The Unplanned Works, The Railway That Keeps Growing, Network Cascade |

## Trigger and runtime flow

`fire_event_by_temp_id_no_cluster` calls `industrial_boom_prepare_random_event_fire` before history is recorded.
It builds a weighted pool of every major or player country passing `industrial_boom_is_valid_target` (viable civilian economy, a region candidate, no active boom, frozen snapshot, pending delivery or depression) and saves `industrial_boom_prefire_target`, which is both the dispatch target and the Event History actor.
Weights (`industrial_boom_target_weight`) rise with a large industrial base, high stability, war with a major and a player who has not recently received the event, and fall sharply for a recipient of the last two years, after a recent crash, under blockade and at very low stability. Every valid country keeps at least weight 1.
With no valid country the pool reports `industrial_boom_target` and the event shows N/A.
Normal firing, manual firing from Event Details and a Positive Economy cluster dispatch all use this path.

`industrial_boom_open` then allocates the episode receipt, resolves an evolved opening, ranks one to three Industrial Regions, derives the starting Overheating, applies the package, joins an active worldwide depression as a supplier, and starts the weekly pulse.

The pulse (`industrial_boom_pulse`, one chain per boom guarded by `industrial_boom_next_pulse_day`) updates region control and damage, project progress, the spread, the four drivers and the drift, national shocks, the lifecycle, counters and trend, evolution pacing, speculative offers, incidents, the AI profile, costs, the contract market flag, the package and civilian commitments.
No whole-world on-action is used.

## Overheating

Overheating runs from 0 to 100 in `industrial_boom_overheating`.
Bands are Sustainable (below 40), Strained (40), Dangerous (70) and Critical (90), with five points of downward hysteresis, and 100 crashes the boom.
The category header shows the value, band, trend (rising, steady or falling against the previous pulse), the next threshold, the leading cause, the reserve state and a landing outlook.
The four internal drivers are output intensity, supply and materials, regional strain, and finance and maintenance (`industrial_boom_drift` constants). The largest positive driver becomes the leading-cause phrase.
Drift is halved during the Opening state.
Shocks come from occupied, lost, bombed or damaged regions (scaled by the region's share of national industry), fuel collapse and blockade. A protected region absorbs most of its own local shock and a held reserve absorbs most of a severe shock, and each is spent by the shock it absorbs.
Unabsorbed severe shocks in the last 180 days enter the Event 35 snapshot.

## Package

The dynamic modifier `industrial_boom_package` reads country variables refreshed by `industrial_boom_refresh_package`: factory output, efficiency growth, a modest efficiency cap, construction, dockyard output and line conversion.
The output share erodes by a third in Strained and two thirds from Dangerous, construction halves from Dangerous, Speculative Mania raises the output share by a quarter, cooling suppresses most of it, running hot adds output and efficiency growth, and spread states add output.
Civilian factories committed by a building reserve, Building-stage projects and recent protection works sit in `industrial_boom_commitment`.

## Decisions and missions

Category `industrial_boom_category` is a simple category with a static picture.

| Row | Visible | Cost | Effect |
| --- | --- | --- | --- |
| Run the Economy Hot | Opening and Running up to Dangerous (locked there) | Overheating | 60 days of extra output, efficiency growth and project pace, higher drift, 30-day cooldown |
| Stabilize Supply Chains | Always | Trains, fuel, convoys when sea dependent | Relief scaled to the supply problem, stronger and dearer from Dangerous with a 30-day supply shield, halved under heavy blockade |
| Build an Industrial Reserve | Up to Strained, no reserve | 90 days of lower output and a civilian commitment | One held reserve |
| Cool the Expansion / Impose Credit Restraint | Running (Opening only after a hot start), not landing | Opportunity cost, stability under Speculative Mania | Large immediate relief, 60 days of suppressed output and slower drift |
| Prepare a Controlled Landing | Running up to Strained | None | Starts the Controlled Landing mission |
| Controlled Landing (mission) | Active | | 120 days (90 after an earlier controlled landing, 150 under Evolution III). Cancelled at 70 or when every project region is lost |
| Prevent the Crash (mission) | Entering Critical | | Below 80 within 60 days, or crash |
| Emergency Production Halt | Dangerous and Critical | None | Forced landing with a held reserve, or below 90 with a protected region, otherwise crash |
| Approve a Speculative Expansion | Evolution I offer | None | Named project starts at Integrating with stronger legacy and heavy finance pressure |
| Declare a Miracle Region | Evolution II, a region with a project | None | Event `.17` upgrades one project |
| Contain the Spread | Evolution III spreading | Stability and temporary output | Ends the spread for this boom |
| Close the Order Books / Accept Foreign Orders | A depressed market exists or books are closed | None | Refuses or accepts Event 35 supply contracts |
| Designate an Industrial Project (per region) | Region without project, up to Strained, not landing | Trains or support equipment, civilian commitment | Event `.16` chooses the profile |
| Protect an Industrial Region (per region) | Project, unprotected | Support equipment, trains, civilian commitment for 60 days | Absorbs the next local shock. Renewable 90 days after it is spent |
| Abandon a Project (per region) | Protected project when threatened or from Dangerous | None | Relief after the first month (large for speculative), unfinished works for a year |

Each region shows one row at a time in the order Designate, Protect, Abandon.

## Regions, projects and legacy

Regions are ranked by factories, infrastructure, capital, port and resources, and lowered on an active front, after a strong earlier legacy and under unfinished works (`industrial_boom_score_region`).
Small countries get one region, medium two, large majors three.
Projects are Production Practices, Rail and Supply Integration and Factory Conversion with stages Building (90 days), Integrating (60 days) and Secured.
Building pauses from Dangerous and Integrating advances only below 70. Running hot speeds progress, cooling slows it, Miracle doubles it. Occupation, damage, famine and contamination pause it.
Legacy is granted only at a controlled or rough landing: controlled converts Secured in full and Integrating at half, rough converts Secured at half, and Miracle or speculative projects convert one step stronger.
Practices give a timed efficiency and line-conversion legacy (Automated Production Control lasts longer and slows later booms), Rail gives infrastructure and a railway to the capital plus a timed resource-shortage reduction (National Rail Spine extends to a neighbour), and Conversion gives a building slot and a factory (Machine-City two each).
Factory levels and slots stay inside a campaign budget of a tenth of the factories at the first boom and one strong legacy per state. Past it, Conversion grants faster construction crews instead.

## Outcomes and repeatability

| Outcome | Result |
| --- | --- |
| Controlled | Legacy, 180 days of reconversion, closes this boom's own recorded Chaos |
| Rough | Half legacy, one year of exhaustion, Event 35 recent-expansion target signal |
| Forced | No legacy, two years of exhaustion, Event 35 target signal |
| Crash | Snapshot, package removed, Event 35 starts or deepens for the same country |

An active supplier contract upgrades one rough landing to controlled.
Campaign memory holds boom, controlled and crash counts, the highest evolution, the legacy budget and state legacy receipts. An earlier crash adds 10 starting Overheating (cap 20) and lowers selection weight for two years, and an earlier controlled landing shortens the Opening state and the landing mission.

## Evolutions

| Stage | Name | Tier | Change |
| --- | --- | --- | --- |
| I | Speculative Mania | Rising Chaos | Output share up a quarter, speculation in the finance driver, Credit Restraint replaces Cooling, speculative offers, three incidents |
| II | The Industrial Miracle | Chaos Tier | Miracle Regions, fragile from 70 Overheating, three incidents |
| III | Runaway Industrialization | Total Chaos | Spread policy (Direct, Let It Run, Contain), Contain the Spread, three incidents |

Active entry uses `mtth:industrial_boom_evolution_interval` (90 days, faster under pressure, slower when cool) during the Running state only and pauses while landing. It records one evolution log row with the country as actor.
An evolved opening starts at the highest unlocked and enabled stage with higher starting Overheating and records no row.
Disabled stages never apply.
The stage passes unchanged as the Event 35 evolution floor.

## Event-owned Chaos

The first Secured Miracle project and the first integrated spread state each add a small gain through `industrial_boom_add_event_chaos` (`industrial_boom_chaos` constants), once per boom.
A controlled landing removes exactly the gains this boom recorded.
Firing, actions, evolutions and crashes add no Event 34 Chaos.

## Connections

- Event 35: crash handoff through `industrial_boom_prepare_collapse_fields`, the shared freezer and `industrial_boom_deliver_extra_regions`, which registers every further region and spread state under its own receipt after the national call is accepted.
- Event 35 supply contracts: two choices on the Event 34 side, open or closed order books, with automatic refusal from 70 Overheating. An accepted contract adds Overheating, `industrial_boom_export_orders` and the landing upgrade.
- Famine: a region whose state passes `famine_food_stage_requires_mortality` pauses its project and adds supply pressure.
- Migration: `migration_state_has_recent_local_integration` (180 days after Local Integration) lowers output pressure for that region.
- Contamination: fallout or severe chemical contamination blocks region and spread selection and pauses projects.
- Event 39 reads `industrial_boom_active`.

## AI

`industrial_boom_update_ai_profile` picks balanced, cautious, wartime, desperate or fragile each pulse.
National decision willingness lives in `common/mtth/034_industrial_boom_mtth.txt`. Region rows and event options weight inline.
Scores are weights, not click chances.

## Achievements

`chaos_redux_034_the_long_fall` (proven by Event 35), `chaos_redux_034_managed_expansion`, `chaos_redux_034_miracle_holds`, `chaos_redux_034_redline_nation` and `chaos_redux_034_built_to_last`, set by `industrial_boom_evaluate_landing_achievements` and `industrial_boom_evaluate_redline` for player booms only.

## Files

- `events/034_industrial_boom.txt`
- `common/scripted_effects/034_industrial_boom_effects.txt` (selection, opening, pulse, drift, bands, package, costs, AI profile, evolutions)
- `common/scripted_effects/034_industrial_boom_region_effects.txt` (regions, projects, spread, offers, Chaos)
- `common/scripted_effects/034_industrial_boom_action_effects.txt` (actions, outcomes, legacy, achievements, snapshot producer, cleanup)
- `common/scripted_effects/034_industrial_boom_incident_effects.txt`
- `common/scripted_effects/034_industrial_boom_collapse_handoff_effects.txt`, `034_industrial_boom_adapter_effects.txt`
- `common/scripted_triggers/034_industrial_boom_triggers.txt`, `034_industrial_boom_adapter_triggers.txt`
- `common/script_constants/034_industrial_boom_constants.txt`, `034_industrial_boom_handoff_constants.txt`
- `common/dynamic_modifiers/034_industrial_boom_dynamic_modifiers.txt`
- `common/decisions/034_industrial_boom_decisions.txt`, `common/decisions/categories/034_industrial_boom_categories.txt`
- `common/mtth/034_industrial_boom_mtth.txt`
- `common/scripted_localisation/034_industrial_boom_localisation.txt`
- `localisation/english/034_industrial_boom_l_english.yml`, `034_industrial_boom_requirement_flags_l_english.yml`
- `interface/034_industrial_boom.gfx`

## Assets

| Sprite | File |
| --- | --- |
| `GFX_report_event_034_industrial_boom_opening` | `gfx/event_pictures/034_industrial_boom/report_event_034_industrial_boom_opening.dds` |
| `GFX_decision_cat_picture_034_industrial_boom` | `gfx/interface/decisions/034_industrial_boom/decision_cat_picture_034_industrial_boom.dds` |
| `GFX_decision_category_034_industrial_boom` | `gfx/interface/decisions/034_industrial_boom/decision_category_034_industrial_boom.dds` |
| `GFX_decision_034_industrial_boom_<stem>` | `gfx/interface/decisions/034_industrial_boom/decision_034_industrial_boom_<stem>.dds` for run_hot, stabilize_supply, build_reserve, cool_expansion, designate_project, protect_region, abandon_project, controlled_landing, prevent_crash, emergency_halt, speculative_expansion, miracle_region, contain_spread |
| `GFX_idea_034_industrial_boom_<stem>` | `gfx/interface/ideas/034_industrial_boom/idea_034_industrial_boom_<stem>.dds` for boom, speculative_mania, industrial_miracle, runaway, export_orders, reconversion, exhaustion |
| `GFX_modifiers_034_industrial_boom_<stem>` | `gfx/interface/state_modifiers/034_industrial_boom/modifiers_034_industrial_boom_<stem>.dds` for region, protected, secured, fragile_miracle, spreading, unfinished_works |
| `GFX_achievement_chaos_redux_034_<name>` with `_grey` and `_not_eligible` | `gfx/achievements/` for managed_expansion, miracle_holds, redline_nation, built_to_last |

All sprites are registered in `interface/034_industrial_boom.gfx`. The Long Fall triplet stays in `interface/035_great_depression_achievement_aliases.gfx`.

## Limitations

- No shock-request adapter for other event owners exists, because no owner submits one. Event 34 observes bombing, disaster and corrosion damage, occupation and loss in its regions itself.
- Stabilize Supply Chains always pays trains. There is no truck alternative.
- Band and trend words use colour plus text, with no separate texticons.
- The Event 35 consumers of the extra region and corridor rows are queued on the Event 35 side.

## Future expansion

- A shock-request adapter once another owner (Acid Rain, Natural Disasters) wants to name a boom region directly.
- Country-flavoured opening text for the major powers.
- A Speculative Mania offer chain that names real consortia and banks of the target country.
