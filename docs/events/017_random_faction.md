# Event 017 Random faction

Event 017 is a Minor Repeatable diplomatic-pressure event. It selects an eligible independent minor, discovers faction leaders that exist in the current world, then forces the selected country to join one of one to four valid faction options. The event never names Axis, Comintern, Allies, or any fixed country tag as an option source.

## Runtime Flow

1. Event dispatch calls `random_faction_prepare_runtime_context` from the settings/event pool helper.
2. The helper builds a weighted pool of eligible minors with `is_random_faction_eligible_country`, prefers wartime and pressure-adjacent situations, saves `random_faction_target_country`, and verifies that at least one valid faction leader exists.
3. `chaosx.nr17.1` runs in the selected country scope and routes player countries to `chaosx.nr17.10` and AI countries to `chaosx.nr17.20`.
4. `random_faction_collect_faction_options` builds up to four distinct saved leader targets from living faction leaders that can accept the selected country.
5. The player receives one to four visible faction options and no decline option. AI countries use the same saved option targets with AI weights based on ideology, regional reach, common enemies, leader relations, bloc strength, war status, and neutrality pressure.
6. `random_faction_join_selected_faction` joins the selected leader's faction, applies alignment shock, stores the newly aligned minor and faction leader in runtime arrays, fires leader reaction `chaosx.nr17.40` in the same effect chain so `[random_faction_target_country.GetName]` can render, pressures neutral neighbors, checks evolutions and achievements, records event-log actor context, and emits `chaosx.news.4`.
7. Regional pressure builds `random_faction_current_region_targets` from eligible neighbors, or from same-continent/coastal reach when the selected country has no land neighbor bucket. Evolution I schedules at most one regional follow-up from that bucket, Evolution II reuses it for wartime pressure, and Evolution III uses it for capped cascade resolution.

If all saved faction targets die between selection and choice display, `random_faction_reopen_dead_faction_file` re-collects live options in the same selected country scope. If no live faction remains, it clears obsolete pressure state instead of presenting a fake or hardcoded choice.

## Eligibility and Faction Discovery

Eligible selected countries must exist, be independent, non-major, alive, not already in a faction, not a special chaos/nonhuman country, and not inside recent Event 17 cooldown or pressure exclusion windows. Evolution II also permits wartime or war-adjacent minors through `is_random_faction_wartime_candidate`.

Valid faction leaders must exist, lead a faction, be independent, be alive, not be a special chaos/nonhuman country, and not be at war with the selected country through their direct country or any faction member. The selected country must pass `can_random_faction_join_faction` before the leader is offered.

The option list is stored with regular event targets:

- `random_faction_option_1_leader`
- `random_faction_option_2_leader`
- `random_faction_option_3_leader`
- `random_faction_option_4_leader`
- `random_faction_selected_leader`

## Values and Constants

Shared tuning lives in `common/script_constants/chaosx_random_faction_constants.txt`. Duration fields that reject script constants use file-scoped `@random_faction_*` values in the relevant decision/effect files, mirroring the script-constant table.

Main values:

- `global.random_faction_fire_count`
- `global.random_faction_pressure_count`
- `global.random_faction_evo3_cascade_count`
- `random_faction_option_count`
- `random_faction_pressure_score`
- `random_faction_neutrality_resilience`
- `random_faction_supported_minors`

Main runtime arrays:

- `global.random_faction_aligned_minors`
- `global.random_faction_pressured_neutrals`
- `global.random_faction_pressure_targets`
- `global.random_faction_faction_leaders`
- `random_faction_current_region_targets` on the country currently anchoring a regional pressure/cascade chain
- `random_faction_corridor_targets` on faction leaders with an active corridor mission
- `random_faction_supported_minor_targets` on faction leaders for distinct liaison-web support proof

## Decisions and Missions

Decision category: `random_faction_bloc_pressure_category`. Its description calls `GetRandomFactionBlocPressureStatus` from `common/scripted_localisation/017_random_faction_scripted_localisation.txt` so aligned minors, pressured neutrals, and faction leaders see a current pressure/resilience/support status line instead of a static header.

Category metadata lives in `common/decisions/categories/017_random_faction_categories.txt`, decisions live in `common/decisions/017_random_faction_decisions.txt`, helper effects live in `common/scripted_effects/017_random_faction_effects.txt`, and availability/cost triggers live in `common/scripted_triggers/017_random_faction_triggers.txt`.

Newly aligned minor decisions:

- `random_faction_stabilize_alignment`: spends Political Power and support equipment, reduces pressure, and improves stability after the accession shock.
- `random_faction_request_liaison`: targeted at the current faction leader, spends Command Power and support equipment, applies the liaison spirit, and records distinct supported-minor progress.
- `random_faction_quiet_opposition`: spends Political Power, infantry equipment, stability, and wartime war support strain to reduce opposition pressure.

Pressured neutral decisions:

- `random_faction_convene_neutrality_council`: spends Political Power, Command Power, and stability, raises neutrality resilience, starts the border-post mission, and uses the animated bloc-pressure seal icon.
- `random_faction_reinforce_border_posts`: timed mission that succeeds when the country controls its capital, keeps infantry equipment reserves, and stations divisions in the capital or a border state. Timeout failure raises pressure. The mission uses the animated warning-border icon.
- `random_faction_invite_observers`: targeted at a valid faction leader, spends Command Power and convoys, and raises one faction's pull.
- `random_faction_publish_neutrality`: spends Political Power and stability strain to raise resistance and lower immediate pressure.

Faction leader decisions:

- `random_faction_offer_staff_mission`: targeted support action for a pressured or newly aligned minor that spends Command Power and support equipment and records a distinct supported minor.
- `random_faction_radio_networks`: regional support action that raises faction pull and records distinct supported minors across valid pressure targets.
- `random_faction_guarantee_corridor`: targeted action that starts `random_faction_guarantee_corridor_mission` and stores the guaranteed country in the leader's local corridor target array.
- `random_faction_guarantee_corridor_mission`: timed credibility check that succeeds while the leader keeps a valid guaranteed target, enough convoys, and a plausible land, faction-neighbor, or coastal route. Success, failure, and cancellation only resolve that leader's stored target list; the target's guarantee flag is timed and expires naturally so overlapping leader missions cannot clear each other's guarantees. The mission uses the animated warning-border icon.
- `random_faction_demand_commitment`: Evolution II/III pressure action that can force a pressured country into a valid faction choice if resistance collapses.

All visible decisions have concrete costs, visible custom cost text, availability tooltips, effect tooltips, and AI weights. Conditional risk costs are kept in the effects, including wartime war-support strain for quieting opposition and stability strain for neutrality/corridor failures.

## Evolutions

Evolution rows are recorded through `random_faction_record_current_evolution` and dispatched in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.

- Evolution I, Regional Bloc Race: unlocks one regional follow-up per baseline pressure chain and the first neutral response decisions. Regional pressure can copy the nearby bloc, counter-align, or resist.
- Evolution II, Pressured Neutrality: unlocks wartime and war-adjacent minor eligibility and stronger leader pressure through commitment demands. Wartime pressure uses the same regional bucket as the baseline chain when available.
- Evolution III, Neutrality Collapse: lets pressure cascades choose more regional neutrals from `random_faction_current_region_targets`, but each cascade is capped by the shared constant table so the region changes through pressure rather than instant conversion.

If Event 017 fires after an evolution has already unlocked, the runtime helpers use the current global flags and schedule the correct follow-ups from the baseline join.

## Event Log, Cluster, and News

Event 017 is registered as repeatable event ID `17` with `chaosx.event_name.17: "Random faction"`.

Event-log actor mapping uses `event_target:random_faction_target_country` when dispatch context exists. The event detail and evolution detail keys live in `localisation/english/017_join_faction_l_english.yml`.

Event 017 belongs to the Diplomatic Panic cluster as an optional low-danger member. Cluster wiring lives in:

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`

News event `chaosx.news.4` now reports the selected country joining its current faction using live faction localisation.

## Achievements

Achievements are registered in `common/achievements/chaos_redux_achievements.txt`, localised in `localisation/english/chaosx_achievements_l_english.yml`, and sprite-registered in `interface/chaosx_achievements.gfx`.

- `017_random_faction_four_doors`
- `017_random_faction_hold_the_line`
- `017_random_faction_crowded_border`
- `017_random_faction_liaison_web`
- `017_random_faction_frontier_commitment`
- `017_random_faction_not_everyone`

Country achievements use country flags set by timed hidden checks. Witness-style hidden achievements use global flags when the condition is regional rather than owned by one player country.

`017_random_faction_four_doors` uses `common/on_actions/017_random_faction_on_actions.txt` to clear the one-year candidate flag if the country leaves its Event 17 faction before the scheduled survival check resolves.

`017_random_faction_hold_the_line` requires Evolution I to be active, the neutrality council and border-post success to have happened, and the country to remain independent, uncapitulated, and outside factions for the one-year check.

`017_random_faction_liaison_web` counts distinct supported target countries stored in the faction leader's `random_faction_supported_minor_targets` array. Once a leader has three valid targets, `random_faction_start_liaison_web_candidate` snapshots those countries into `random_faction_liaison_web_candidate_targets`, waits 180 days, and only awards the achievement if the same snapshot still has three valid, uncapitulated, non-subject targets that are not direct enemies of the leader.

`017_random_faction_frontier_commitment` requires a Pressured Neutrality candidate to remain in a faction, alive, independent, in control of its capital, and in control of every core border state for the 180-day check.

`017_random_faction_not_everyone` checks the country-local cascade bucket that produced the Neutrality Collapse report, so the survivor must belong to that regional cascade rather than an unrelated global pressure target.

## Cleanup

Cleanup helpers remove obsolete spirits, active mission flags, active missions, and stale array entries for invalid pressure targets. `random_faction_refresh_runtime_arrays` keeps leader and pressure arrays from pointing at dead faction leaders, invalid countries, former pressure targets, or countries that no longer satisfy the current visibility surface. It rebuilds global arrays from temporary live lists, clears invalid target state separately from array removal, prunes each live leader's supported-minor array, and strips invalid faction leaders of active corridor/radio state.

Targeted lifecycle cleanup is handled through vanilla `on_leave_faction`, `on_capitulation`, `on_uncapitulation`, `on_puppet`, release, subject-annexation, annexation, and government-change hooks rather than a broad daily or weekly pulse. World-end launchers call `random_faction_cleanup_after_world_end`, which clears only Event 17's own arrays and missions.

The invalidation path never creates dummy factions or hardcoded choices. It re-collects live faction leaders or clears obsolete pressure state.

## Asset Wiring

Runtime sprite registry: `interface/017_random_faction.gfx`.

Event pictures:

- `GFX_report_event_random_faction_cabinet`
- `GFX_report_event_random_faction_border`
- `GFX_report_event_random_faction_liaison`
- `GFX_report_event_random_faction_regional_cascade`

Decision/category sprites:

- `GFX_random_faction_bloc_pressure_bg`
- `GFX_decision_category_random_faction_bloc_pressure`
- `GFX_decision_random_faction_stabilize_alignment`
- `GFX_decision_random_faction_liaison`
- `GFX_decision_random_faction_opposition`
- `GFX_decision_random_faction_neutrality_council`
- `GFX_decision_random_faction_border_posts`
- `GFX_decision_random_faction_observers`
- `GFX_decision_random_faction_neutrality_press`
- `GFX_decision_random_faction_staff_mission`
- `GFX_decision_random_faction_radio_networks`
- `GFX_decision_random_faction_corridor`
- `GFX_decision_random_faction_commitment`

Idea sprites:

- `GFX_idea_random_faction_alignment_shock`
- `GFX_idea_random_faction_border_pressure`
- `GFX_idea_random_faction_bloc_polarization`
- `GFX_idea_random_faction_neutrality_exhaustion`
- `GFX_idea_random_faction_liaison_mission`

Animated UI sprites:

- `GFX_random_faction_bloc_pressure_seal_animated`; static fallback `GFX_random_faction_bloc_pressure_seal_static`; used by `random_faction_convene_neutrality_council`
- `GFX_random_faction_border_warning_animated`; static fallback `GFX_random_faction_border_warning_static`; used by `random_faction_reinforce_border_posts` and `random_faction_guarantee_corridor_mission`

Achievement sprites:

- `GFX_achievement_017_random_faction_four_doors`
- `GFX_achievement_017_random_faction_hold_the_line`
- `GFX_achievement_017_random_faction_crowded_border`
- `GFX_achievement_017_random_faction_liaison_web`
- `GFX_achievement_017_random_faction_frontier_commitment`
- `GFX_achievement_017_random_faction_not_everyone`

Source, processed, validation, contact-sheet, and final handoff files live under `docs/assets/017_random_faction/`. Runtime DDS files live under `gfx/event_pictures/017_random_faction/`, `gfx/interface/decisions/017_random_faction/`, `gfx/interface/ideas/017_random_faction/`, and `gfx/achievements/`.

## Future Plans and Suggestions

- Add optional country-specific flavour events for pressured neutrals with especially contested geography.
- Add more faction-leader follow-up reports after repeated staff missions or failed corridors.
- Add event-log subentries for repeated successful neutrality defenses if the Event Log UI gains more room for outcome detail.
- Tune AI weights after live observation of how often neutral councils successfully resist the regional cascade.
