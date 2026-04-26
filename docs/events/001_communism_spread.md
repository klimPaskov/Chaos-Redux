# 001 Communist Insurgency

## What The Event Is

`chaosx.nr1.1` starts a state-based communist insurgency. The national idea adds `+0.01` daily communist drift. State control is the real crisis layer, and every communist-controlled state adds another `+0.01` daily communist support through the `communism_state_control_pressure` dynamic modifier.

The event does not unlock World Revolution immediately. World Revolution enters the normal major-event pool only after the third communism evolution, `Whispers of the World Revolution`, is reached. World Revolution is not fired directly by this chain.

## Event Map And Subevents

- `chaosx.nr1.1`: starts the system, gives the national idea, seeds one Level 1 controlled state, and queues maintenance
- `chaosx.nr1.2`: state-based industry sabotage in a controlled state
- `chaosx.nr1.3`: emergency intervention outcome shell for manual/forced use
- `chaosx.nr1.4`: new state falls under communist control
- `chaosx.nr1.5`: controlled state escalates to a stronger level
- `chaosx.nr1.6`: local intervention succeeds
- `chaosx.nr1.7`: local intervention backfires
- `chaosx.nr1.8`: revolutionary war warning when control is severe
- `chaosx.nr1.9`: emergency intervention restores control without uprising
- `chaosx.nr1.10`: emergency intervention triggers a custom uprising
- `chaosx.nr1.11`: evolution milestone, Unstable Revolutionary Activity
- `chaosx.nr1.12`: evolution milestone, Dark Worker Rituals
- `chaosx.nr1.13`: evolution milestone, Whispers of the World Revolution
- `chaosx.nr1.14`: rare surprise revolt in a controlled state
- `chaosx.nr1.15`: rare worker ritual incident in a controlled state
- `chaosx.nr1.16`: rare World Revolution foreshadowing incident
- `chaosx.nr1.17`: country defeat popup when local control is gone and communist support falls below the spread threshold
- `chaosx.nr1.18`: red-banner surprise revolt variant
- `chaosx.nr1.19`: loyalist governor disappearance variant
- `chaosx.nr1.20`: hidden per-country maintenance event
- `chaosx.nr1.21` to `chaosx.nr1.25`: hidden cooldown clearers
- `chaosx.nr1.26`: hidden defeat-grace clearer after the 180-day minimum runtime
- `chaosx.nr1.27` to `chaosx.nr1.29`: dark worker ritual variants
- `chaosx.nr1.30` to `chaosx.nr1.32`: Lenin resurrection and World Revolution whisper variants

## Trigger And Runtime Flow

The root event remains fire-once event `1` in the Chaos Redux event system. When it fires, every non-communist country receives `communism_spread_idea`, a small initial communist popularity increase, one immediate Level 1 communist-controlled state, and a queued maintenance event. The initial state seed is explicit so the player immediately sees the state-control layer and the decision category.

Countries matching `is_special_chaos_country = yes` are excluded from the root event spread, maintenance, decisions, and World Revolution state handoff. This keeps the insurgency focused on regular countries instead of special Chaos actors.

The system does not rely on the old monthly on-action updater anymore. Each affected country self-schedules hidden maintenance every `40-70` days. Maintenance:

1. refreshes controlled state counts
2. recalculates dynamic national communist drift from controlled states
3. tries to add one new controlled state if under the soft support-based ceiling
4. tries to escalate one existing controlled state
5. checks for communist evolution milestones
6. may fire a state-based sabotage event
7. may fire one rare evolution incident if its incident cooldown is clear
8. may warn of revolutionary war if at least half the country is controlled or two Level 3 states exist
9. queues the next maintenance pulse

## Main Gameplay Effects

State control uses three levels:

- Level 1, `communism_control_level_1`: Agitation Zone. Mild factory, manpower, resources, supply, construction, and unrest penalties. Regular intervention can clear it.
- Level 2, `communism_control_level_2`: Insurgent Stronghold. Stronger penalties and harder local intervention. It can be reduced or cleared, but failure can push it to Level 3.
- Level 3, `communism_control_level_3`: Communist Lockdown. Severe penalties, blocked strategic redeployment, and a state-level demilitarized zone. Normal local intervention cannot clear it; emergency intervention is required. The demilitarized-zone status is only removed when this system clears the state control it added.

The old weekly stability and weekly war support penalties were removed from the national idea. The old generic industry damage event was replaced by `chaosx.nr1.2`, which always targets a specific controlled state.

## Defeating The Event

The event can be defeated country by country. A country drops out of the communism spread runtime and receives `chaosx.nr1.17` when all of these are true:

- at least `180` days have passed since the country entered the communism spread system
- it has no communist-controlled states
- it is not currently marked as fighting communist rebels
- communist party support is below `min_support_for_state_spread`

Local intervention clears or reduces Level 1 and Level 2 states. Level 3 states require emergency intervention. `Disrupt Communist Organizing` is a national support-reduction decision that remains available while the country has the insurgency idea, so the player can push communist popularity down after local control is contained. If emergency intervention does not trigger an uprising, controlled states are cleared or reduced and communist support is cut. If it does trigger an uprising, the country must defeat the communist rebel state in war; the existing annex hook clears the `fighting_communist_rebels` marker.

The global `communism_spread` flag is cleared once no non-special country has active communism spread state, controlled states, evolution flags, or rebel fighting state, and no communist rebel country remains. When this happens, the World Revolution unlock flag is also cleared and World Revolution weight is reset to `0`.

## Evolutions

The communist insurgency uses three global evolution stages. Chaos tier and state-control conditions make a stage eligible, but the stage does not fire immediately when the tier changes. Active countries roll for global progression through the maintenance system, with `evolution_progression_cooldown_days = 90` between attempts and `progression_roll_chance = 25`.

- Stage 1, Unstable Revolutionary Activity: unlocked at Gathering Storm tier once a country has at least one communist-controlled state. It enables rare surprise revolts, including very rare one-state breakaway revolts.
- Stage 2, Dark Worker Rituals: unlocked at Rising Chaos tier once at least one state reaches Level 2. It enables strange worker ritual incidents that add temporary state disruption, increase intervention cost, increase conversion risk, and slightly increase communist support.
- Stage 3, Whispers of the World Revolution: unlocked at Chaos Tier once at least one state reaches Level 3. It sets `communism_spread_world_revolution_unlocked`, allows World Revolution into the major-event pool, and enables foreshadowing incidents that add `200` World Revolution weight.

When an evolution stage unlocks, it is recorded once in the event log without a country actor and then applied to all non-special countries currently running the communism spread system.

Evolution incidents share `evolution_incident_cooldown_days = 180`, so the added flavor should stay occasional rather than becoming another constant popup stream.

## Rebel Army Generation

Communist rebel armies are generated by state score rather than a single generic unit type. Each converted or breakaway state calculates unit count from:

- control level
- civilian and military industry
- state population
- local industry, population, and developed infrastructure
- national communist support
- whether the owner is at war
- whether the owner is a major
- national manpower and division count
- worker ritual or World Revolution whisper flags
- local breakaway context

The rebel country receives a pool of templates covering worker militias, red guards, revolutionary infantry, factory battalions, railway guards, urban insurgents, partisan brigades, armored defectors, motorized revolutionary columns, armored revolutionary columns, revolutionary cavalry, elite revolutionary guards, and red cossacks. Motorized and armored templates are deliberately stronger than baseline militia formations and include cavalry elements where appropriate. Unit names use country-flavored pools for all vanilla majors plus Estonia, and shared regional/language pools for Hispanic, Portuguese-speaking, Nordic, Benelux, Polish, and central/eastern/southeastern European countries, with a generic naming pool for unsupported countries. Shared pools are selected through reusable scripted triggers in `common/scripted_triggers/001_communism_spread_triggers.txt`, not inline tag lists in the spawn effects.

## Supporting Systems Touched

- `common/script_constants/001_communism_spread_constants.txt`: all timing, drift, intervention, emergency, rebel, and evolution values
- `common/scripted_effects/001_communism_spread_effects.txt`: state control, spread, escalation, sabotage, emergency, uprising, evolution, and World Revolution handoff effects
- `common/scripted_triggers/001_communism_spread_triggers.txt`: reusable state-control availability triggers
- `common/dynamic_modifiers/chaosx_dynamic_modifiers.txt`: national pressure, three state control levels, crackdown scars, worker ritual fear, and emergency disruption
- `common/ideas/chaosx_ideas.txt`: simplified `communism_spread_idea`
- `common/decisions/chaosx_communism_fight_decisions.txt`: national counter-agitation, state intervention, factory protection, and emergency intervention
- `common/scripted_guis/chaosx_scripted_guis.txt`: decision-category dashboard registration
- `common/scripted_localisation/chaosx_scripted_localisation.txt`: dashboard sprite, threat status, and state-control level text
- `interface/chaosx_decisions.gui`: dashboard layout above the communism decisions
- `interface/001_communism_spread.gfx`: communism idea sprites, threat meter sprites, and communism event-picture sprite names
- `common/on_actions/chaosx_on_actions.txt`: removed the obsolete monthly communism updater
- `events/091_the_great_revolution.txt`: uses communist-controlled states as the World Revolution territorial basis, then cleans up state-control flags
- Event log and GUI localisation now describe the new system and show locked World Revolution weight as red `N/A`

## AI Behavior

AI will use local intervention more aggressively against Level 2 states, but backs off when it is in a dangerous war or has low stability. AI will consider emergency intervention when Level 3 states exist or controlled states exceed the computed half-country threshold, with caution during major wars.

## Emergency Intervention And Uprising

The national emergency decision becomes available when at least one state is Level 3 or controlled states exceed 50% of owned states. It costs political power, command power, manpower, infantry equipment, stability, war support, and temporary national economic disruption.

Emergency intervention rolls for uprising risk from:

- base chance: `15`
- each controlled state: `+3`
- each Level 3 state: `+12`
- communist party support scaled by `45`
- maximum chance: `90`

If an uprising happens, this system does not use vanilla `start_civil_war`. It marks states for conversion by level:

- Level 1: `40%`
- Level 2: `80%`
- Level 3: `100%`

Capital states are excluded from emergency and local breakaway conversion so the original country remains valid for the rebel war declaration.

A dynamic communist rebel country is created, receives its own communist politics and leader, receives spawned division templates, and takes only the converted controlled states. It does not inherit half the original country's stockpile.

## Decisions

The decision category includes a crisis dashboard above the decisions. The dashboard shows:

- the Revolutionary Threat Meter from 0% to 100%
- a short status line: Contained, Growing Unrest, Dangerous, Revolutionary Crisis, or Collapse Imminent
- controlled-state totals split by Agitation Zone, Insurgent Stronghold, and Communist Lockdown icons
- current daily communist support from controlled states, shown as the raw daily support value

The dashboard threat value is rebuilt by `refresh_communism_spread_dashboard_values`. It combines communist party support, the number and level of communist-controlled states, active evolution stages, and open rebel war pressure. The visual meter uses the nearest 10% progress sprite through `GetCommunismThreatMeterSprite`.

State-targeted intervention decisions reuse the Norwegian communist preparation dot icons:

- one dot: Communist Agitation Zone
- two dots: Communist Insurgent Stronghold
- three dots: Communist Lockdown

The level icons in the dashboard have tooltips showing how many controlled states are currently in that level. The same dot treatment is used on the local intervention and factory protection state-targeted decisions so the player can distinguish control levels directly from the map decision icons. Controlled states also receive a passive state-map icon through `communism_control_state_mapicon_scripted_gui`, while intervention decisions use the engine's predefined yellow-style state outline color for hover highlights.

- `communism_national_counter_agitation`: national. Reduces communist party support by `2%` after a timed operation, costs command power, political power, and stability, and can trigger country-level defeat once no controlled states remain.
- `communism_local_military_intervention`: state-targeted. Works only on Level 1 and Level 2 states. Costs and outcome risk scale by level.
- `communism_factory_protection`: state-targeted. Reduces sabotage pressure in an industrial controlled state but does not clear communist control.
- `communism_emergency_intervention`: national. Affects all controlled states and may trigger the custom uprising.

The old generic military, industrial, propaganda, economic, and emergency suppression loop was removed from the active decision file.

## World Revolution Handoff

World Revolution is unlocked only after `Whispers of the World Revolution`. Once World Revolution fires later, it uses existing communist-controlled states instead of randomly selecting states from national communist popularity.

World Revolution strength by state level:

- Level 1 states transfer as weak local revolutionary cells and mostly spawn worker militias, partisan brigades, and red guards.
- Level 2 states transfer as organized strongholds and add stronger militia, railway, urban, and factory formations.
- Level 3 states transfer as prepared revolutionary bases and can spawn elite guards, motorized columns, armored defectors, armored revolutionary columns, revolutionary cavalry, and strong revolutionary infantry.

Industrial, high-population, developed-infrastructure, high-support, at-war, and major-country contexts add extra REV units. Countries with no communist-controlled states do not provide a territorial basis to REV.

## Asset Wiring

Gameplay currently runs with registered placeholder idea sprites and event pictures in `interface/001_communism_spread.gfx`. Decision icons reuse existing assets:

- category: `GFX_decision_category_generic_communism`
- local intervention: `GFX_decision_generic_military`
- factory protection: `GFX_decision_generic_factory`
- emergency intervention: `GFX_decision_generic_protection`
- national pressure: `GFX_idea_communist_state_control_pressure`
- Level 1 state control: `GFX_idea_communist_agitation_zone`
- Level 2 state control: `GFX_idea_communist_insurgent_stronghold`
- Level 3 state control: `GFX_idea_communist_lockdown`
- post-crackdown scars: `GFX_idea_communist_post_crackdown_scars`
- worker ritual fear: `GFX_idea_communist_worker_ritual_fear`
- emergency disruption: `GFX_idea_communist_emergency_disruption`

The Revolutionary Threat Meter uses these DDS assets in `gfx/interface/revolutionary_threat/`:

- `GFX_revolutionary_threat_meter_000`: `revolutionary_threat_meter_000.dds`
- `GFX_revolutionary_threat_meter_010`: `revolutionary_threat_meter_010.dds`
- `GFX_revolutionary_threat_meter_020`: `revolutionary_threat_meter_020.dds`
- `GFX_revolutionary_threat_meter_030`: `revolutionary_threat_meter_030.dds`
- `GFX_revolutionary_threat_meter_040`: `revolutionary_threat_meter_040.dds`
- `GFX_revolutionary_threat_meter_050`: `revolutionary_threat_meter_050.dds`
- `GFX_revolutionary_threat_meter_060`: `revolutionary_threat_meter_060.dds`
- `GFX_revolutionary_threat_meter_070`: `revolutionary_threat_meter_070.dds`
- `GFX_revolutionary_threat_meter_080`: `revolutionary_threat_meter_080.dds`
- `GFX_revolutionary_threat_meter_090`: `revolutionary_threat_meter_090.dds`
- `GFX_revolutionary_threat_meter_100`: `revolutionary_threat_meter_100.dds`

Dedicated art should replace the placeholder `idea_unknown.dds` paths later. Place sprites in `gfx/interface/ideas/` and keep these stable sprite names:

- `GFX_idea_communist_agitation_zone`
- `GFX_idea_communist_insurgent_stronghold`
- `GFX_idea_communist_lockdown`
- `GFX_idea_communist_state_control_pressure`
- `GFX_idea_communist_post_crackdown_scars`
- `GFX_idea_communist_worker_ritual_fear`
- `GFX_idea_communist_emergency_disruption`

Unique event pictures should replace the placeholder DDS files in `gfx/event_pictures/communism_spread/`. Keep the existing filenames and GFX names:

- `GFX_report_event_communist_insurgency_start`: `communist_insurgency_start.dds`; depict red pamphlets, organizers, or a strike crowd as the first visible outbreak of the crisis.
- `GFX_report_event_communist_industry_sabotage`: `communist_industry_sabotage.dds`; depict factory machinery, rail depots, damaged warehouses, or workers disrupting production.
- `GFX_report_event_communist_emergency_intervention`: `communist_emergency_intervention.dds`; depict loyal troops or police entering a factory district under emergency powers.
- `GFX_report_event_communist_state_control`: `communist_state_control.dds`; depict revolutionary committees or red banners taking over local administration.
- `GFX_report_event_communist_control_escalates`: `communist_control_escalates.dds`; depict barricades, militia checkpoints, or a municipal building under red control.
- `GFX_report_event_communist_intervention_success`: `communist_intervention_success.dds`; depict seized weapons, arrests, or loyal authority restored after a crackdown.
- `GFX_report_event_communist_intervention_backfire`: `communist_intervention_backfire.dds`; depict street clashes, angry workers, or a failed police sweep.
- `GFX_report_event_communist_war_warning`: `communist_war_warning.dds`; depict red militias mobilizing before open civil conflict.
- `GFX_report_event_communist_emergency_success`: `communist_emergency_success.dds`; depict exhausted loyal troops holding a cleared factory or railway hub.
- `GFX_report_event_communist_uprising`: `communist_uprising.dds`; depict armed revolutionary columns, barricades, and a public rebel proclamation.
- `GFX_report_event_communist_unstable_activity`: `communist_unstable_activity.dds`; depict a secret cell, hidden weapons cache, or raid preparation.
- `GFX_report_event_communist_dark_worker_rituals`: `communist_dark_worker_rituals.dds`; depict workers in a night-shift factory ritual with red cloth, tools, and dim industrial light.
- `GFX_report_event_communist_world_revolution_whispers`: `communist_world_revolution_whispers.dds`; depict clandestine World Revolution pamphlets, foreign cells, or a hidden revolutionary portrait.
- `GFX_report_event_communist_surprise_revolt`: `communist_surprise_revolt.dds`; depict sudden barricades, improvised red flags, or police being pushed out of a district.
- `GFX_report_event_communist_worker_ritual`: `communist_worker_ritual.dds`; depict workers gathered around machinery, burned ledgers, or oath-taking in a factory.
- `GFX_report_event_communist_world_revolution_foreshadowing`: `communist_world_revolution_foreshadowing.dds`; depict coded railway couriers, international revolutionary maps, or red symbols spreading across borders.
- `GFX_report_event_communist_insurgency_defeated`: `communist_insurgency_defeated.dds`; depict a cleared committee hall, removed banner, or restored local government office.

## Limitations

State selection is priority-tiered. It first looks for vulnerable states neighboring existing communist control with industry, population, arms factories, or developed infrastructure, then neighboring states, then strategic industrial/population states, and finally any eligible non-capital owned state when no strategic target exists.

Map highlighting uses state-targeted decisions and highlighted controlled-state triggers. There is no custom map mode in this pass.

## Open Tuning Notes And Future Expansion

- `maintenance_min_days` and `maintenance_max_days` control the broad pacing of the system.
- `state_spread_cooldown_days`, `state_escalation_cooldown_days`, and `sabotage_cooldown_days` are the main anti-spam controls.
- `defeat_grace_days = 180` prevents a country from defeating the system immediately through early suppression.
- `evolution_incident_cooldown_days`, `surprise_revolt_chance`, `worker_ritual_chance`, and `world_revolution_whisper_chance` control how often evolution incidents appear.
- `communism_spread_drift.per_controlled_state = 0.01` is fixed to the spec.
- Emergency uprising risk may need live-session tuning for large majors; `per_controlled_state_uprising_chance` and `communism_support_uprising_scale` are the first values to adjust.
- Rebel unit counts are score-based, but the exact thresholds will need live-session tuning. The first values to adjust are `level_1_units`, `level_2_units`, `level_3_units`, industry bonuses, and the evolution conversion bonuses.
