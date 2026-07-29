# Event 017 Random faction

Event 017 is an implemented Minor Repeatable diplomatic-pressure event. It selects an eligible independent minor, discovers faction leaders that exist in the current world, then forces the selected country to join one of one to four valid faction options. The event never names Axis, Comintern, Allies, or a fixed country tag as an option source.

The catalog status is `Needs Testing`. The gameplay, localisation, assets, achievements, Event Log, and cluster surfaces are implemented. The status records that user live-session validation is still outstanding rather than a missing content surface.

## Runtime Flow

1. Automatic timer firing, manual settings firing, Event Details firing, and cluster-member firing all reach the shared pre-fire route in `chaosx_settings_effects.txt`. That route calls `random_faction_prepare_runtime_context` before Event 17 is dispatched.
2. The helper builds a weighted world pool with `is_random_faction_eligible_country`. Evolution II can also admit `is_random_faction_wartime_candidate`. It randomly selects one eligible minor, saves that country as `random_faction_target_country`, and verifies that at least one valid faction leader exists. No supported dispatch route prefers the current player country.
3. `chaosx.nr17.1` runs in the selected country scope and routes player countries to `chaosx.nr17.10` and AI countries to `chaosx.nr17.20`.
4. `random_faction_collect_faction_options` builds up to four distinct saved leader targets from living faction leaders that can accept the selected country.
5. A player receives one to four visible faction options and no decline option. An AI country resolves `chaosx.nr17.20` against those same saved option targets. It does not rebuild or substitute its own option list.
6. `random_faction_join_selected_faction` revalidates the selected leader, joins its faction, stores the chosen leader, applies alignment shock, stores the aligned minor and faction leader in runtime arrays, binds the chosen leader to the exact Event Log history sequence, dispatches leader reaction `chaosx.nr17.40` when that leader is outside its 180-day reaction cooldown, pressures neutral neighbors, checks evolutions and achievements, and emits `chaosx.news.4`.
7. Regional pressure builds `random_faction_current_region_targets` from eligible neighbors, or from same-continent/coastal reach when the selected country has no land neighbor bucket. Evolution I schedules at most one regional follow-up from that bucket, Evolution II reuses it for wartime pressure, and Evolution III uses it for capped cascade resolution.

If all saved faction targets die between selection and choice display, `random_faction_reopen_dead_faction_file` re-collects live options in the same selected country scope. If no live faction remains, it clears obsolete pressure state instead of presenting a fake or hardcoded choice.

The chosen faction leader receives `chaosx.nr17.40` immediately after a successful accession only when it has no active `random_faction_rival_reaction_cooldown`. The first dispatch opens a 180-day reaction window; later accessions during that window still update member count, cohesion strain, last-member, and last-region memory but cannot farm another free response. Both visible responses require the recipient to remain a valid living faction leader and the stored target to remain a living, independent member of the same faction, outside direct war with that leader, with that leader still stored as its chosen sponsor. If that context is lost before the report resolves, the event exposes only a cleanup response and applies no liaison or radio reward. Sending staff officers gives the new member Faction Liaison Mission for 180 days, removes 12 pressure, improves mutual relations, and records that member as supported. Building the radio net adds 10 pressure to the new member, applies Bloc Polarization for 240 days, and records the member as supported. Both responses feed the Liaison Web proof. A leader at war or without multiple reachable pressure targets favors staff officers. Multiple reachable targets, peace, fascist or communist government, and high chaos favor radio networks. Democratic leaders are cautious about the radio route.

## Eligibility and Faction Discovery

Eligible selected countries must exist, be independent, non-major, alive, not already in a faction, not a special chaos/nonhuman country, and not have recent-alignment, selection-cooldown, or selection-pending state. Evolution II also permits countries at war, countries beside a faction at war, and countries under active Event 17 pressure through `is_random_faction_wartime_candidate`.

Valid faction leaders must exist, lead a faction, be independent, be alive, not be a special chaos/nonhuman country, and not be at war with the selected country through their direct country or any faction member. The selected country must pass `can_random_faction_join_faction` before the leader is offered. Once Evolution II is active, strategic reach is mandatory whenever the target is at war, beside a faction war, or under active pressure, or whenever the offered leader is already at war. The leader or one of its members must be adjacent or on the same continent, share an enemy with the target, or have a coastal route to a coastal target that controls at least 10 convoys. The gate is used during initial collection and click-time revalidation, so neither a human forced choice nor an AI positive base weight can select an impossible remote wartime bloc.

The minor-selection ticket weight starts at 4. Every valid non-major receives 4 more tickets. A faction neighbor adds 6, war or an adjacent war adds 4, Stability below 45% adds 3, and War Support below 42% adds 2. Existing pressure subtracts 6, a selection cooldown subtracts 20, resilience below 35 adds 5, and resilience above 70 subtracts 3. The final weight is rounded and clamped from 1 to 24. These values live in `random_faction_selection_weight`.

Faction options are also weighted before the four unique targets are drawn. A leader starts at weight 5, gains 10 when one of its faction members borders the selected country, gains 2 while at war, and is clamped from 2 to 15. Each selected leader is excluded from later draws.

The option list is stored with regular event targets:

- `random_faction_option_1_leader`
- `random_faction_option_2_leader`
- `random_faction_option_3_leader`
- `random_faction_option_4_leader`
- `random_faction_selected_leader`

## Values and Constants

Shared Event 17 tuning lives in `common/script_constants/chaosx_random_faction_constants.txt`. Fixed delayed `country_event` fields and decision `days_re_enable` fields consume script constants directly. Computed delays, timed flags, and timed ideas receive a temporary-variable bridge from the relevant script constants. The two mission timeout fields read country variables initialized from script constants immediately before `activate_mission`.

Only two parser-static cases remain file-scoped. `ai_hint_pp_cost` rejects variables and script-constant tokens, so the decision file keeps three `@random_faction_ai_hint_pp_*` mirrors of the shared low, medium, and high Political Power costs. `random_select_amount` has no proven variable or script-constant form, so the effects file keeps `@random_faction_maritime_reach_targets = 3` for the designed maritime bucket.

Main values:

- `global.random_faction_fire_count`
- `global.random_faction_pressure_count`
- `random_faction_option_count`
- `random_faction_pressure_score`
- `random_faction_neutrality_resilience`
- `random_faction_supported_minors`
- `random_faction_chosen_leader`, which preserves the current alignment sponsor on the joined country
- `random_faction_region_id`, which stores one of the seven continent-based regional identities
- `random_faction_evo3_candidate_count`, `random_faction_evo3_cascade_count`, and the related Evolution III budget values, which are country-scoped to the active cascade anchor and cleared after that cascade

Main runtime arrays:

- `global.random_faction_aligned_minors`
- `global.random_faction_pressured_neutrals`
- `global.random_faction_pressure_targets`
- `global.random_faction_faction_leaders`
- `random_faction_current_region_targets` on the country currently anchoring a regional pressure/cascade chain
- `random_faction_corridor_targets` on faction leaders with an active corridor mission
- `random_faction_supported_minor_targets` on faction leaders for distinct liaison-web support proof
- `random_faction_liaison_web_candidate_targets` on a faction leader for the exact three-country Liaison Web proof, with reciprocal `random_faction_liaison_candidate_leaders` entries on those countries
- `random_faction_frontier_core_state_targets` on a Frontier Commitment candidate for the launch capital and every national core state bordering a non-core state
- `random_faction_not_everyone_survivor_targets` on an Evolution III anchor for the original neutral-survivor cohort, with reciprocal `random_faction_not_everyone_candidate_owners` entries on those countries
- `global.events_log_history_secondary_actor_entries` and `global.events_log_history_has_secondary_actor_entries` for the exact leader stored on each Event 17 history sequence

## Decisions and Missions

Decision category: `random_faction_bloc_pressure_category`. Its description calls `GetRandomFactionBlocPressureStatus` from `common/scripted_localisation/017_random_faction_scripted_localisation.txt` so aligned minors, pressured neutrals, and faction leaders see a current pressure/resilience/support status line instead of a static header.

Category metadata lives in `common/decisions/categories/017_random_faction_categories.txt`, decisions live in `common/decisions/017_random_faction_decisions.txt`, helper effects live in `common/scripted_effects/017_random_faction_effects.txt`, and availability/cost triggers live in `common/scripted_triggers/017_random_faction_triggers.txt`.

Newly aligned minor decisions:

- `random_faction_stabilize_alignment`: snapshots its cost at accession. Political Power is 25 plus 2 per controlled state, clamped from 25 to 70. Support equipment is 60 plus 10 per controlled state, clamped from 60 to 180. A wartime accession also costs 15 Command Power and 2% War Support. Completion removes Alignment Shock and Emergency Defensive Coordination, adds 3% Stability, removes 10 pressure, improves mutual relations, and removes 5 cohesion strain from the stored leader.
- `random_faction_request_liaison`: targeted at the current faction leader. The minor pays 15 Command Power while the leader provides 60 support equipment. The 180-day liaison improves relations and coordination, records distinct supported-minor progress, and creates visible faction dependency through additional pull and lower resilience.
- `random_faction_quiet_opposition`: spends 25 Political Power, 450 infantry equipment, 2% Stability, and 2% War Support while at war. It removes Alignment Shock and removes 12 pressure. Backlash starts at 10%, adds 15 percentage points below 62% Stability, adds 10 after Evolution II, and adds 15 after Evolution III. Backlash restores 12 pressure and applies Bloc Polarization.

Pressured neutral decisions:

- `random_faction_convene_neutrality_council`: spends 45 Political Power, 15 Command Power, and 2% Stability, adds 18 resilience, removes 6 pressure, snapshots a border objective, and starts the border-post mission.
- `random_faction_reinforce_border_posts`: names one controlled frontier state, or the capital for a country without a controlled land frontier, records its current garrison, and requires at least one additional division there while the capital stays controlled and 450 infantry equipment remains in reserve. Success adds 15 resilience and 2% Stability and removes 10 pressure. Timeout adds 18 pressure, removes 15 resilience, and applies Neutrality Exhaustion for 180 days.
- `random_faction_invite_observers`: targets a reachable faction leader, spends 15 Command Power and 15 convoys, records that leader as the pressure source, adds 10 pressure, removes 10 resilience through dependency, adds 1% War Support, improves mutual relations, and angers a valid rival leader when one exists.
- `random_faction_publish_neutrality`: spends 25 Political Power and 2% Stability, adds 8 resilience, and removes 8 pressure. Its one-use pressure-cycle flag prevents spam.

Faction leader decisions:

- `random_faction_offer_staff_mission`: spends 30 Command Power and 120 support equipment on a reachable target, then applies a 180-day target cooldown. A faction member loses 12 pressure, Alignment Shock, and Emergency Defensive Coordination and gains 2% Stability. A pressured neutral gains 12 leader-specific pressure and loses 8 resilience. Both routes improve mutual relations and record a distinct supported minor.
- `random_faction_radio_networks`: spends 25 Political Power and 120 support equipment, then iterates only the existing Event 17 pressure-target array. It applies pressure and polarization only to reachable valid targets, records them as supported, and performs no world scan.
- `random_faction_guarantee_corridor`: spends 15 Command Power, 450 infantry equipment, and 15 convoys on a reachable target. It snapshots the leader's train stockpile and starts `random_faction_guarantee_corridor_mission` only after the target and objective are stored.
- `random_faction_guarantee_corridor_mission`: a 120-day active objective that requires the target and route to remain valid, at least 15 convoys to remain in reserve, and the leader to add five trains after mission launch. Success lowers immediate pressure, creates leader-specific dependency, and improves relations. Failure raises pressure, damages relations, and can redirect the target toward a rival. Invalid targets or routes cancel immediately without granting success.
- `random_faction_demand_commitment`: spends 70 Political Power and 30 Command Power after Evolution II. It adds 18 pressure and opens a valid faction choice at the 80-point collapse threshold. A refusal adds 10 resilience, damages relations with the demanding leader, and can redirect the pressure source toward another valid faction leader.

All visible decisions have concrete custom cost text, exact resource gates, effect-time target revalidation, and effect tooltips matching the scripted outcomes. AI weights evaluate ideology, relations, war and threat state, target reach, neutrality resilience, and route-specific aggression. Radio and multi-target AI checks use Event 17 arrays rather than periodic country-wide scans.

## AI Behavior

The hidden AI resolver has one option for each saved player-facing leader target. Every slot starts from weight 5 and applies the same slot-neutral factor set. Matching ideology and strong bloc strength double the weight. Regional pull and a wartime common enemy triple it. Strategic reach and positive relations multiply it by 1.5. High leader cohesion strain, a recent patron failure, or war without a common enemy halve it. A nonregional leader without strong pressure and a failing patron without low target resilience reduce it to one quarter. High chaos can make a remote baseline option more competitive, but it cannot bypass the Evolution II wartime reach gate.

The pressured-neighbor event uses the stored source leader as its first choice, one saved rival leader as its counterweight when available, and a separate resist option. High resilience, peace, and Stability above 62% favor resistance. Low resilience, war, nearby source-faction members, common enemies, and higher chaos favor accession or counter-alignment.

Decision AI shares the script constants `random_faction_ai_weight` and `random_faction_ai_factor`. Newly aligned minors prioritize stabilization when unstable. Pressured neutrals favor councils and public neutrality when stable and favor observers when threatened or low in resilience. Faction leaders favor staff, corridor, and commitment actions for threatened or low-resilience targets. Democratic leaders are cautious about coercive commitment and radio pressure, while fascist and communist leaders are more willing to use them.

## Evolutions

Evolution rows are recorded through `random_faction_record_current_evolution` and dispatched in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.

- Baseline: every successful accession adds one to `global.random_faction_fire_count`, applies 150 days of Alignment Shock, opens a 365-day recent-alignment and selection-cooldown window, and applies 270 days of regional pressure to valid nearby neutrals. If the chosen leader is at war, the new member also receives 120 days of Emergency Defensive Coordination.
- Evolution I, Regional Bloc Race: unlocks when Event 17 has fired three times, the current regional bucket contains at least two targets, or the chaos meter reaches tier 1. It schedules at most one pressured-neutral response from the regional bucket after 7 to 21 days. That country can copy the source bloc, counter-align with another saved leader, or resist and take Neutrality Exhaustion.
- Evolution II, Pressured Neutrality: unlocks after Evolution I when the current country is at war, a neighbor is at war, a neighbor belongs to another faction, or the chaos meter reaches tier 2. It admits countries at war, beside a faction at war, or under active Event 17 pressure only when at least one non-enemy faction has land, continental, common-enemy, or convoy-backed coastal reach. It schedules one valid Evolution II pressure target after 10 to 30 days and unlocks Demand Commitment.
- Evolution III, Collapse of Neutrality: unlocks after Evolution II when at least three pressure targets and at least two current regional targets exist, plus one of four escalation conditions. Those conditions are current war, a neighboring faction at war, five Event 17 fires, or chaos tier 3. It schedules the regional cascade after 10 to 31 days.

Evolution III uses the following bounded resolution:

1. It builds a unique candidate array from the anchor's `random_faction_current_region_targets` and refuses to start with fewer than two candidates.
2. The response budget is the smallest of half the candidates rounded up, the candidate count minus one, and the absolute cap of five.
3. The guaranteed faction-choice budget is two or the smaller response budget. Remaining countries inside the response budget use a 35 join and 65 resist base weighting. Low or high resilience, war, a neighboring source faction, and high chaos shift those weights.
4. Every handled candidate receives a 365-day `random_faction_evo3_handled` flag. At least one starting candidate therefore remains outside the cascade response budget.
5. The anchor stores `random_faction_evo3_cascade_count` and the related budget values only for this cascade, then clears them at completion. There is no global cascade counter.
6. The anchor's region is one of Europe, North America, South America, Australia, Africa, Asia, or the Middle East. A dynamic global flag named `random_faction_evo3_region_<id>_active` locks that region for 45 days so a second anchor cannot receive an overlapping full budget.

If Event 017 fires after an evolution has already unlocked, the runtime helpers use the current global flags and schedule the correct follow-ups from the baseline join.

## Event Log, Cluster, and News

Event 017 is registered as repeatable event ID `17` with `chaosx.event_name.17: "Random faction"`.

The shared dispatcher supplies `event_target:random_faction_target_country` as the primary Event Log actor, marks that country with `random_faction_history_result_pending`, queues `chaosx.nr17.1`, then records the repeatable history row. `random_faction_bind_history_sequence` stores the new `global.events_log_history_sequence` only while that baseline-result marker is present. A successful baseline join stores the chosen leader as `random_faction_pending_history_leader`; follow-up pressure and Evolution III joins do not touch history-result state. The bind and finalize helpers can arrive in either order, so human and AI resolution both wait until the sequence and leader exist. Finalization scans for the exact sequence and Event ID 17, writes the leader into `global.events_log_history_secondary_actor_entries` at that index, and clears the marker and both pending variables. It never assumes that the newest row is still index zero.

History rebuilds copy the secondary actor into the derived history view and open Event Details arrays. Event 17 uses three exact result branches:

- Bound result: both stored countries still exist. History and Event Details name the selected minor and the leader that led the chosen faction at the time of that firing.
- Lost leader result: the history row still records that a secondary actor existed, but that country no longer exists. The text preserves the selected minor and states that the country which led the faction at accession no longer exists.
- Unresolved result: the primary actor and history row exist, but no successful faction signature has been bound yet. The text names the selected minor and does not substitute a later leader.

The exact result text and all Event 17 evolution text live in `localisation/english/017_join_faction_l_english.yml`. Event Details exposes exactly three ordered previews through `events_log_add_event_detail_evolution_preview`: Regional Bloc Race at tier 1, Pressured Neutrality at tier 2, and Collapse of Neutrality at tier 3. Logged evolution history still contains only stages that actually unlocked.

Event 017 belongs to the Diplomatic Panic cluster as an optional low-danger member with a 65% participation chance and dynamic Event 17 availability. Cluster wiring lives in:

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`

News event `chaosx.news.4` reports the selected country joining its current faction using live faction localisation.

## Achievements

Achievements are registered in `common/achievements/chaos_redux_achievements.txt`, localised in `localisation/english/chaosx_achievements_l_english.yml`, and sprite-registered in `interface/chaosx_achievements.gfx`.

Country achievements use country flags set by timed hidden checks. Witness-style hidden achievements use global flags when the condition is regional rather than owned by one player country.

- `017_random_faction_four_doors`: selecting a minor with four valid saved faction options starts a 365-day proof after the join. `random_faction_alignment_memory_is_valid` requires the stored `random_faction_chosen_leader`, or its transferred successor, to exist and remain in the same faction as the candidate. The country must also remain independent and uncapitulated. `on_leave_faction` clears the candidate before the check can award it.
- `017_random_faction_hold_the_line`: after Evolution I, a pressured neutral must convene the neutrality council, complete Reinforce Border Posts, and then remain alive, independent, uncapitulated, in control of its capital, and outside all factions for 365 days.
- `017_random_faction_crowded_border`: a one-off check after an accession looks inside Event 17's active regional-pressure population for a living, independent, non-major neutral country whose neighbors include members of at least three distinct live factions. The qualifying country must carry regional-bucket state, active bloc pressure, or membership in the pressured-neutral ledger. This witness achievement uses a global completion flag.
- `017_random_faction_liaison_web`: when a faction leader records at least three distinct supported minors, the system snapshots exactly three into `random_faction_liaison_web_candidate_targets` and registers that leader in each target's reciprocal `random_faction_liaison_candidate_leaders` array. For 180 days, subject conversion, capitulation, annexation, special-country or other base-validity loss, or direct war with the supporting leader permanently breaks the candidate. Joining or changing faction membership does not break Liaison Web because newly aligned minors remain valid support targets. The end check still requires all three original targets to be alive, independent, uncapitulated, and outside direct war with the same valid leader; no replacement target can enter the proof.
- `017_random_faction_frontier_commitment`: an Evolution II candidate that joins while already at war, or while bordering a member of a faction at war with the chosen faction, snapshots its launch capital plus every national core state bordering a non-core state into `random_faction_frontier_core_state_targets`. The proof refuses to start unless the candidate already controls every stored state. During the next 180 days, `on_state_control_changed` permanently cancels the candidate as soon as it loses control of any stored state, so later recovery cannot restore eligibility. At the end it must still be alive, independent, uncapitulated, in a faction, and in control of the unchanged launch snapshot.
- `017_random_faction_not_everyone`: an Evolution III anchor snapshots every immediately eligible neutral survivor in its resolved regional bucket into `random_faction_not_everyone_survivor_targets` and registers reciprocal owner entries on those original countries. A survivor is permanently removed if it joins a faction, becomes a subject, capitulates, is annexed, converts into an invalid special country, or otherwise loses base validity. After 180 days the witness achievement is awarded only if at least one member of that original cohort remained a valid independent non-major outside every faction; countries that enter or re-enter the region later cannot substitute for a removed survivor.

## Cleanup

Cleanup helpers remove obsolete spirits, active mission flags, active missions, local cascade budgets, stored scope pointers, and stale array entries. `random_faction_refresh_runtime_arrays` keeps leader and pressure arrays from pointing at dead faction leaders, invalid countries, former pressure targets, or countries that no longer satisfy the current visibility surface. It rebuilds global arrays from temporary live lists, clears invalid target state separately from array removal, prunes each live leader's supported-minor array, and strips invalid faction leaders of active corridor and radio state.

`random_faction_schedule_current_country_cleanup` schedules `chaosx.nr17.85` after every country-owned timed pressure or liaison application, plus the two-day cleanup buffer. The initial join therefore probes after the 365-day recent-alignment window, regional pressure probes after 270 days, and later Neutrality Exhaustion, Bloc Polarization, and Faction Liaison Mission applications each create a probe for their own final duration. A probe that wakes while another pressure source is active leaves the country tracked; the probe attached to that later source performs the final cleanup. Pending human and AI choices are also registered in the compact pressure-target array so world-end cleanup can retire an unresolved selection without scanning every country.

Ordinary pressure expiry does not destroy an active timed achievement proof. Four Doors, Hold the Neutral Line, Frontier Commitment, Liaison Web, and Not Everyone Signed candidates keep their reciprocal ledgers and target-array membership until their hidden proof event resolves. Events `.81`, `.82`, `.83`, `.84`, and `.86` immediately re-enter the cleanup check after closing that proof. Invalidating lifecycle and world-end paths still clear the proof at once. Expired countries retain valid alignment memory when appropriate and lose obsolete pressure state, missions, pointers, and pressure-array membership.

Targeted lifecycle cleanup is handled through `on_offer_join_faction`, `on_join_faction`, `on_leave_faction`, `on_assume_faction_leadership`, capitulation and uncapitulation, subject conversion and release, annexation, government change, `on_state_control_changed`, and `on_war_relation_added`. The two-day `random_faction_join_in_progress` guard distinguishes Event 17's own faction entry from an unrelated external entry. Faction entry removes a country only from Not Everyone survivor ledgers; it does not invalidate Liaison Web. Subject, capitulation, annexation, exile, invalid-government, and special-country conversion paths disqualify both continuous registries, while direct war breaks only the affected Liaison Web leader-target relationship and stored-state loss breaks only the affected Frontier Commitment candidate. Candidate completion or cleanup unregisters both sides of each reciprocal ledger. Faction-leader succession transfers supported-minor, recent-member, cohesion-strain, alignment-leader, and pressure-source memory to a valid successor. Special-country conversion effects explicitly disqualify achievement ledgers before calling the generic country cleanup helper.

World-end launchers call `random_faction_cleanup_after_world_end`, which clears the seven active regional flags, tracked country state, leader state, Event 17 arrays, and missions. Event 17 has no daily, weekly, or monthly world-iteration on action. Its broad country scans occur only during bounded firing, maritime-region construction, achievement checks, regional reporting, or open Event Log rebuilds.

The invalidation path never creates dummy factions or hardcoded choices. It re-collects live faction leaders or clears obsolete pressure state.

## Asset Wiring

Runtime sprite registry: `interface/017_random_faction.gfx`.

Event pictures:

- `GFX_report_event_random_faction_cabinet` on the player faction file
- `GFX_report_event_random_faction_border` on the pressured-neighbor event and Evolutions I and II
- `GFX_report_event_random_faction_liaison` on the faction-leader reaction and news event
- `GFX_report_event_random_faction_regional_cascade` on Evolution III and its regional report

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

- `GFX_random_faction_bloc_pressure_seal_animated` is an eight-frame, 64 by 64, 8 FPS looping sprite used by `random_faction_convene_neutrality_council`. `GFX_random_faction_bloc_pressure_seal_static` is the registered frame-000 static companion.
- `GFX_random_faction_border_warning_animated` is an eight-frame, 64 by 64, 8 FPS looping sprite used by `random_faction_reinforce_border_posts` and `random_faction_guarantee_corridor_mission`. `GFX_random_faction_border_warning_static` is the registered frame-000 static companion.

Achievement sprites:

- `GFX_achievement_017_random_faction_four_doors`
- `GFX_achievement_017_random_faction_hold_the_line`
- `GFX_achievement_017_random_faction_crowded_border`
- `GFX_achievement_017_random_faction_liaison_web`
- `GFX_achievement_017_random_faction_frontier_commitment`
- `GFX_achievement_017_random_faction_not_everyone`

Every achievement has completed, grey, and not-eligible sprite variants in `interface/chaosx_achievements.gfx`. Source frames, processed frames, contact sheets, GIF previews, static companions, sprite sheets, manifests, and handoff notes live under `docs/assets/017_random_faction/`. Runtime DDS files live under `gfx/event_pictures/017_random_faction/`, `gfx/interface/decisions/017_random_faction/`, `gfx/interface/ideas/017_random_faction/`, `gfx/interface/animated/017_random_faction/`, and `gfx/achievements/`.

Read-only asset validation on 2026-07-10 confirmed expected dimensions for all 44 Event 17 runtime DDS files, eight unique source-frame hashes in each eight-frame animation package, and an existing file for every one of the 26 texture paths in `interface/017_random_faction.gfx`.

## Implementation File Map

| Surface | Files |
| --- | --- |
| Event chain and news | `events/017_join_faction.txt`, `events/_chaosx_news.txt` |
| Event-owned tuning and logic | `common/script_constants/chaosx_random_faction_constants.txt`, `common/scripted_triggers/017_random_faction_triggers.txt`, `common/scripted_effects/017_random_faction_effects.txt` |
| Decisions and spirits | `common/decisions/categories/017_random_faction_categories.txt`, `common/decisions/017_random_faction_decisions.txt`, `common/ideas/017_random_faction_ideas.txt`, `common/opinion_modifiers/017_random_faction_opinion_modifiers.txt` |
| Lifecycle hooks | `common/on_actions/017_random_faction_on_actions.txt` |
| Automatic, manual, and availability dispatch | `common/scripted_effects/chaosx_settings_effects.txt`, `common/scripted_effects/chaosx_logic_effects.txt` |
| Event Log result, previews, and click context | `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_guis/chaosx_scripted_gui_events_log.txt` |
| Cluster integration | `common/script_constants/event_cluster_constants.txt`, `common/scripted_effects/chaosx_event_cluster_effects.txt` |
| Event and decision localisation | `localisation/english/017_join_faction_l_english.yml`, `localisation/english/chaosx_event_names_l_english.yml`, `common/scripted_localisation/017_random_faction_scripted_localisation.txt` |
| Achievements | `common/achievements/chaos_redux_achievements.txt`, `localisation/english/chaosx_achievements_l_english.yml`, `interface/chaosx_achievements.gfx` |
| Event-owned sprite registry | `interface/017_random_faction.gfx` |
| Special-country cleanup callers | `common/scripted_effects/003_holy_realm_effects.txt`, `common/scripted_effects/007_fury_effects.txt`, `common/scripted_effects/010_death_effects.txt` |
| World-end cleanup callers | `events/002_zombie_outbreak.txt`, `events/chemical_warfare_events.txt`, `common/scripted_effects/003_holy_realm_effects.txt`, `common/scripted_effects/007_fury_effects.txt`, `common/scripted_effects/010_death_effects.txt`, `common/scripted_effects/germany_mengele_effects.txt` |
| Design, plans, and asset records | `docs/specs/017_random_faction_specs/`, `docs/plans/017_random_faction_plans/`, `docs/assets/017_random_faction/` |
| Catalog workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` |

## Future Plans and Suggestions Not Implemented

- Add optional country-specific flavour events for pressured neutrals with especially contested geography.
- Add more faction-leader follow-up reports after repeated staff missions or failed corridors.
- Add event-log subentries for repeated successful neutrality defenses if the Event Log UI gains more room for outcome detail.
- Tune AI weights after live observation of how often neutral councils successfully resist the regional cascade.
