# Event 013 achievement registry handoff

> Parent disposition, 2026-07-10: the intentionally locked registry described below was completed by later runtime, asset, localisation, and re-audit tranches. All ten achievements have live sequence hooks, disqualifiers, accepted icon triplets, final localisation, and a clean final achievement audit. This file remains the original strict-route design handoff.

Date: 2026-07-10

## Result and scope

The root achievement registry now contains the accepted ten Event 013 achievements, including `013_natural_disasters_no_global_announcer`. The achievement localisation file now contains final player-facing names, descriptions, and override tooltips. The working labels from the source specs were not used as final titles.

Files changed:

- `common/achievements/chaos_redux_achievements.txt`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/013_achievement_registry_handoff.md`

No Event 013 engine, constants, events, decisions, assets, interface files, documentation outside this handoff, or spreadsheet files were edited. No commit was created.

Before this patch, the Event 013 registry and localisation sections were empty. After this patch, all ten accepted achievement IDs have strict `happened` conditions and complete localisation. The runtime does not yet set any of the new `achievement_nd_*` state. The achievements therefore remain intentionally locked until the engine hooks below are implemented. No easier unlock fallback was added.

## Registered achievement IDs and final titles

| Achievement ID | Final title |
| --- | --- |
| `013_natural_disasters_after_the_sirens` | All Clear, All Accounted For |
| `013_natural_disasters_no_second_wave` | The Tide Stops Here |
| `013_natural_disasters_every_bridge_counts` | The Trains Came Through |
| `013_natural_disasters_ashes_without_famine` | Bread Beneath the Ash |
| `013_natural_disasters_no_global_announcer` | No World Weather Office |
| `013_natural_disasters_under_the_falling_sky` | Keep the Runways Lit |
| `013_natural_disasters_shake_the_world_back` | Brace the Broken Earth |
| `013_natural_disasters_disaster_barrage_maximum` | All Sirens at Once |
| `013_natural_disasters_not_one_more_camp` | Every Cot Accounted For |
| `013_natural_disasters_catalogue_of_ruin` | An Atlas Bound in Dust |

## Registry tracker contract

All tracker state below is country-scoped. Attempt state must reset when a fresh qualifying route starts, but a later route must not overwrite an unresolved active attempt. Catalogue and report-group flags are campaign memory and must never reset.

| Achievement | Required start and success state | Counters | Disqualifiers |
| --- | --- | --- | --- |
| All Clear, All Accounted For | `achievement_nd_severe_season_started`, `achievement_nd_severe_season_ended`, `achievement_nd_severe_recovery_closed`, no open aftermath, and no active chain mission | `achievement_nd_severe_cards_expected`, `achievement_nd_severe_cards_recovered`, with recovered greater than or equal to expected | `achievement_nd_severe_recovery_deadline_failed`, `achievement_nd_severe_aftermath_abandoned`, or capitulation |
| The Tide Stops Here | `achievement_nd_tsunami_prevention_started`, `achievement_nd_tsunami_chain_prevented` | `achievement_nd_tsunami_preventions` greater than zero | `achievement_nd_second_wave_arrived`, `achievement_nd_second_wave_death_spike`, or capitulation |
| The Trains Came Through | `achievement_nd_transport_recovery_started`, `achievement_nd_transport_recovery_complete` | `achievement_nd_transport_cards_expected`, `achievement_nd_transport_cards_recovered`, with recovered greater than or equal to expected | `achievement_nd_capital_supply_route_failed` or capitulation |
| Bread Beneath the Ash | `achievement_nd_major_ashfall_started`, `achievement_nd_ashfall_recovery_complete` | `achievement_nd_ashfall_states_affected`, `achievement_nd_ashfall_states_recovered`, with recovered greater than or equal to affected | `achievement_nd_ash_famine_matured` or capitulation |
| No World Weather Office | `achievement_nd_report_group_ground`, `achievement_nd_report_group_water`, `achievement_nd_report_group_weather`, `achievement_nd_report_group_climate` | None. The four named group flags are the explicit variety requirement. | `achievement_nd_global_announcer_used` |
| Keep the Runways Lit | `achievement_nd_meteor_shower_started`, `achievement_nd_meteor_shower_ended`, `achievement_nd_skyfall_capital_operational`, `achievement_nd_skyfall_supply_route_operational`, `achievement_nd_skyfall_airfield_network_operational` | `achievement_nd_skyfall_survived_hits` at or above `constant:natural_disaster_achievement.skyfall_survival_hits` | `achievement_nd_skyfall_capital_failed`, `achievement_nd_skyfall_supply_route_failed`, `achievement_nd_skyfall_airfield_network_failed`, or capitulation |
| Brace the Broken Earth | `achievement_nd_rupture_recovery_started`, `achievement_nd_rupture_recovery_closed` | `achievement_nd_rupture_regions_recovered` at or above `constant:natural_disaster_achievement.aftershock_successes` | `achievement_nd_rupture_aftershock_matured`, `achievement_nd_rupture_tsunami_matured`, or capitulation |
| All Sirens at Once | `achievement_nd_barrage_maximum_started`, `achievement_nd_barrage_maximum_ended`, `achievement_nd_barrage_capital_route_preserved`, one of `achievement_nd_barrage_port_corridor_preserved` or `achievement_nd_barrage_rail_corridor_preserved`, no open aftermath, and no active chain mission | `achievement_nd_barrage_recovery_cards` at or above `constant:natural_disaster_achievement.barrage_maximum_recovery_cards` | `achievement_nd_barrage_country_collapsed`, `achievement_nd_barrage_aftermath_unresolved`, or capitulation |
| Every Cot Accounted For | `achievement_nd_refugee_protection_started`, `achievement_nd_refugee_pressure_resolved` | `achievement_nd_refugee_routes_completed` greater than zero | `achievement_nd_refugee_death_threshold_failed`, `achievement_nd_refugee_camp_disease_failed`, `achievement_nd_refugee_border_camp_failed`, or capitulation |
| An Atlas Bound in Dust | All eight `achievement_nd_catalogue_*_recovered` flags listed below | None. Each family-group flag is idempotent campaign memory. | None |

## Exact engine hooks required

The following call sites already exist and should receive narrow achievement helpers. No daily, weekly, or monthly world iteration is needed.

1. `natural_disaster_call`
   - After an accepted sequence receives `natural_disaster_last_sequence_id`, initialize eligible severe-season, meteor-shower, and rupture attempt state.
   - Persist the relevant sequence ID on the affected country so delayed impacts and recovery cards cannot count toward the wrong attempt.
   - Do not reset an unresolved active attempt. Begin a replacement attempt only after the earlier attempt succeeded or acquired a disqualifier.

2. `natural_disaster_execute_impact`
   - Before family data can be overwritten by a follow-up, call an achievement impact tracker with the state `natural_disaster_sequence_id`, `natural_disaster_family`, `natural_disaster_severity`, and owner.
   - Increment expected-card or affected-state counters only once per state and tracked sequence. State-scoped sequence guards are required for severe, transport, ashfall, skyfall, rupture, and barrage counters.
   - A severe-season card qualifies at `constant:natural_disaster_severity.severe` or higher.
   - A transport card qualifies at `constant:natural_disaster_severity.regional` or higher, with family earthquake, flood, tropical cyclone, or blizzard, and only when `natural_disaster_damage_transport` is positive.
   - A major ashfall card qualifies for family `constant:natural_disaster_family.ashfall` at `constant:natural_disaster_severity.regional` or higher. Massive-eruption child ashfall cards may count only when their persisted family is ashfall.
   - Meteor-shower and whole-earth-rupture tracking must use the originating sequence ID because later hits can resolve as related families.

3. `natural_disaster_fire_family_report`
   - For affected-country reports, set the report-group flag that contains `natural_disaster_current_family`.
   - Ground group: earthquake, dry mass movement, wet mass movement, volcanic eruption, ashfall, and lahar.
   - Water group: flood, tsunami, and storm surge.
   - Weather group: tropical cyclone, extreme wind, tornado outbreak, thunderstorm, hailstorm, blizzard, and cold wave.
   - Climate group: heat wave, drought, dust and sandstorm, and wildfire.
   - If report policy is `constant:natural_disaster_report_policy.global` during an active attempt, set `achievement_nd_global_announcer_used`. News cooldown flags and global family-seen flags are not valid substitutes because they are not player-country report history.

4. `natural_disaster_schedule_chain_followup`
   - When the original family is earthquake, volcanic eruption, or meteor impact and the resolved chain is tsunami, set `achievement_nd_tsunami_prevention_started` on the affected owner and bind the state or sequence to that attempt.
   - Persist the pre-follow-up family and chain type before any follow-up changes `natural_disaster_family`.

5. `natural_disaster_stabilize_chain_prevention` in `common/decisions/013_natural_disasters_decisions.txt`
   - Immediately before setting `natural_disaster_chain_risk` to none, inspect the old risk.
   - For a tracked tsunami risk, set `achievement_nd_tsunami_chain_prevented`, increment `achievement_nd_tsunami_preventions`, and leave both second-wave disqualifiers clear.
   - This is the authoritative prevention hook. The timed state flag `natural_disaster_chain_prevented` alone is insufficient because it expires and does not identify the player-country route.

6. `natural_disaster_execute_chain_followup`
   - On a tracked tsunami arrival, set `achievement_nd_second_wave_arrived` before changing the family.
   - After population loss resolves, set `achievement_nd_second_wave_death_spike` when the accepted major-spike threshold is met.
   - On tracked ashfall famine arrival, set `achievement_nd_ash_famine_matured`.
   - On tracked rupture aftershock or tsunami arrival, set `achievement_nd_rupture_aftershock_matured` or `achievement_nd_rupture_tsunami_matured`.
   - On severe refugee-pressure arrival, initialize the refugee-protection attempt before any later death, disease, or border-camp outcomes.

7. `natural_disaster_execute_reassessment`
   - When a tracked phase misses its deadline and receives `natural_disaster_phase_failed`, set the matching attempt disqualifier.
   - A failed late reconstruction deadline sets `achievement_nd_severe_recovery_deadline_failed`.
   - A refugee card failure sets `achievement_nd_refugee_border_camp_failed` when shelter, evacuation, and route protection were not completed. A disease follow-up on a tracked refugee card sets `achievement_nd_refugee_camp_disease_failed`.
   - Call the operational-state checker for capital, supply route, airfield network, port corridor, and rail corridor tracking.

8. `natural_disaster_close_aftermath_card`
   - Count a recovered card only when the state has `natural_disaster_reconstruction_success`. The existing partial-cleanup close path must not count as a full recovery and should set `achievement_nd_severe_aftermath_abandoned` for a tracked severe attempt.
   - Increment the matching severe, transport, ashfall, skyfall, rupture, or barrage recovery counter once per state and tracked sequence.
   - When all expected cards for an attempt are recovered and the country has no open aftermath, set the appropriate completion flag.
   - For a successfully reconstructed normal-family card, set the catalogue group flag from the exact mapping below.
   - For a successfully resolved refugee-pressure card, set `achievement_nd_refugee_pressure_resolved`. Increment `achievement_nd_refugee_routes_completed` only when at least one qualifying action was completed on that tracked card.

9. `natural_disaster_process_due_job`
   - When the country queue becomes empty, set the relevant `*_ended` flag for its tracked sequence.
   - This hook ends the impact sequence. It must not claim recovery closure while aftermath cards remain open.
   - Run the operational-state checker here so the final skyfall and barrage route state is recorded after the last queued impact.

10. `trigger_disaster_barrage_scenario`
    - After `call_natural_disaster = yes`, require `natural_disaster_call_result = constant:natural_disaster_call_result.accepted` and `triggerable_scenarios_intensity = constant:triggerable_scenario_intensity.maximum` before setting `achievement_nd_barrage_maximum_started`.
    - Persist `natural_disaster_last_sequence_id`, clear old barrage attempt flags and counters, and schedule the unresolved-aftermath check for `constant:natural_disaster_sequence.season_expiry_days`.
    - At that check, set `achievement_nd_barrage_aftermath_unresolved` if any aftermath card or chain mission remains.

11. Event-owned capitulation hook
    - While `achievement_nd_barrage_maximum_started` is active and completion is absent, capitulation must set `achievement_nd_barrage_country_collapsed`.
    - This should use the normal capitulation on-action path, not a daily country scan.

12. Refugee action hooks
    - On tracked refugee cards, successful completion of `natural_disaster_rescue_open_shelters`, `natural_disaster_rescue_emergency_evacuation`, `natural_disaster_rescue_medical_triage`, or `natural_disaster_rescue_clear_one_route` should increment `achievement_nd_refugee_routes_completed` once per action and card.
    - Repeated timed action flags must not increment the same action twice for the same card.

## Operational-state checks required

No current Event 013 helper proves the capital supply route, primary supply route, airfield network, or surviving port and rail corridors across an entire attempt. `natural_disaster_state_has_strategic_transport` only describes one state's present transport value. A reusable country-scope operational checker is required and should be called at qualifying impact, reassessment, card close, queue empty, and attempt completion.

The checker should use existing Event 013 tuning where applicable:

- `constant:natural_disaster_threshold.strategic_infrastructure`
- `constant:natural_disaster_threshold.strategic_naval_base`
- `constant:natural_disaster_threshold.strategic_railway`
- `natural_disaster_state_has_strategic_transport`

The accepted source does not define how many surviving airfields constitute an operational network or the exact building threshold for a primary supply route. Those definitions are unresolved design blockers. The engine must not set positive operational flags until one canonical rule is chosen and applied at every lifecycle check.

## Catalogue family-group mapping

Award a group flag only after a card closes with full reconstruction success.

| Campaign flag | Families |
| --- | --- |
| `achievement_nd_catalogue_seismic_recovered` | earthquake |
| `achievement_nd_catalogue_water_coastal_recovered` | flood, tsunami, storm surge |
| `achievement_nd_catalogue_fire_drought_recovered` | heat wave, drought, wildfire |
| `achievement_nd_catalogue_winter_recovered` | blizzard, cold wave, hailstorm |
| `achievement_nd_catalogue_storm_recovered` | tropical cyclone, extreme wind, tornado outbreak, thunderstorm |
| `achievement_nd_catalogue_mass_movement_recovered` | dry mass movement, wet mass movement |
| `achievement_nd_catalogue_volcanic_ash_recovered` | volcanic eruption, ashfall, lahar |
| `achievement_nd_catalogue_dust_sand_recovered` | dust and sandstorm |

Meteor impact, meteor shower, whole-earth rupture, massive eruption, and moving storm corridor are abnormal families and do not replace a normal-family group.

## Constants

The registry reuses these existing constants:

- `constant:natural_disaster_achievement.skyfall_survival_hits`
- `constant:natural_disaster_achievement.aftershock_successes`
- `constant:natural_disaster_achievement.barrage_maximum_recovery_cards`
- `constant:natural_disaster_sequence.season_expiry_days`
- existing family, severity, report-policy, chain, and transport-threshold constants

Two accepted disqualifiers still need central thresholds in `natural_disaster_achievement` before their engine hooks can be completed:

- `second_wave_major_death_spike`
- `refugee_death_failure_threshold`

The accepted specs describe both thresholds but provide no numeric values. Selecting values is a balance decision and remains a blocker. No values were invented in this patch.

The existing `natural_disaster_achievement` keys `firebreak_successes`, `global_relief_countries`, `no_deaths_min_hits`, `prepared_capital_min_severity`, and `no_world_end_abnormal_seasons` belong to the obsolete eight-achievement package. They are not used as substitutes for the accepted routes.

## Expected achievement icon basenames

Each basename requires completed, `_grey`, and `_not_eligible` DDS files in `gfx/achievements/`:

```text
013_natural_disasters_after_the_sirens
013_natural_disasters_no_second_wave
013_natural_disasters_every_bridge_counts
013_natural_disasters_ashes_without_famine
013_natural_disasters_no_global_announcer
013_natural_disasters_under_the_falling_sky
013_natural_disasters_shake_the_world_back
013_natural_disasters_disaster_barrage_maximum
013_natural_disasters_not_one_more_camp
013_natural_disasters_catalogue_of_ruin
```

None of these exact accepted triplets exists. The live folder still contains the obsolete eight-id icon set identified in `docs/plans/013_natural_disasters_plans/013_asset_audit.md`. Achievement presentation is blocked until all ten accepted triplets are produced and installed.

## Localisation keys added

For every registered achievement, the matching `<achievement_id>_NAME`, `<achievement_id>_DESC`, and `achievement_nd_<slug>_tooltip` key was added. The file retains UTF-8 BOM encoding and uses localisation keys without `:0`.

## Validation

- The registry contains exactly ten Event 013 IDs and no duplicate top-level achievement ID.
- All ten IDs have one name, one description, and one override tooltip. The thirty Event 013 localisation keys occur exactly once across the localisation tree.
- The Event 013 registry section has 83 opening braces and 83 closing braces. The full shared registry has 723 opening braces and 723 closing braces.
- The achievement localisation file still begins with the UTF-8 BOM.
- No `achievement_nd_*` tracker exists in Event 013 engine files yet, which confirms the runtime blockers below.
- None of the thirty required accepted icon DDS files is present under the accepted basename triplets.
- Runtime unlock validation was not possible because the tracking hooks are outside this task and remain unimplemented.

## Remaining blockers and skipped work

- All ten achievements are blocked from runtime completion because no Event 013 engine file currently sets the required `achievement_nd_*` flags or variables.
- The major second-wave death-spike threshold has no accepted numeric value.
- The severe refugee death threshold has no accepted numeric value, and the current refugee-pressure follow-up does not apply or record a dedicated refugee death tick.
- The current engine has no canonical operational-state helper for capital supply, primary supply, airfield network, port corridor, and rail corridor continuity.
- The current engine has no Event 013 capitulation tracker for a live Maximum Barrage attempt.
- None of the ten accepted achievement icon triplets exists under its final basename.
- Engine wiring, constant additions, asset production, `.gfx` or `.gui` work, Event 013 docs, and spreadsheet alignment were outside this task and were not performed.
- No simplification or fallback was used. The registry stays strict and locked until every required hook is real.
