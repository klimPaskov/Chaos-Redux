# Event 31 Random Terror

## Identity and pacing

Random Terror is Event `31`, enters through `chaosx.nr31.1`, remains a Minor Repeatable event at Chaos level `1`, and records one pacing event even though one bounded global wave can affect several eligible countries and exact states.

The hidden entry event calls `random_terror_run_global_wave`, refreshes the global ledgers, schedules eligible evolution or world-end work, and sends local report callbacks without allowing those callbacks to increment pacing again.

The accepted evolution names are Organized Cells, Transnational Terror Network, Territorial Insurgency, The Jihadist International, and The Final Jihad.

Global Jihad remains a scenario owned by Event 31, and The False Revelation remains the terminal world-end branch.

The accepted proposal for `SCN-014` collided with the live Fallout registry entry, while `SCN-015` is occupied by Missile Age. Global Jihad therefore uses the next free triggerable-scenario slot, `SCN-016`; its separate world-end registry remains on its independently verified slot. Internal Fracture is not registered because its member package has not been accepted.

## State model

Every affected government maintains Terror Pressure, Response Legitimacy, incident count, response history, and mission locks.

Every affected state maintains activity, pressure, incident memory, exact civilian-loss accounting, cooldown state, territorial readiness, and action or mission commitments.

Later evolutions add Network Reach, International Unity, territorial-control values, actor authority, external supply, strategic victories, and hidden apocalyptic readiness without changing the identity-neutral baseline targeting rules.

Religion, ethnicity, nationality, refugee status, and ordinary ideology never increase baseline target or recruitment weight.

Evolution IV alone opens the wholly fictional jihadist branch, and its content includes opposition from Muslim governments, communities, clerics, soldiers, civic organizations, and fictional religious authorities.

The final entity is presented as an unexplained presence whose followers make a claim; the game never confirms that it is Allah or any divine being.

## Outcomes and containment

The baseline supports containment, continued spread, coups, civil war, state partition, territorial takeover, negotiated surrender, territorial actor formation, and final defeat.

Disabled evolutions leave the ordinary incident, containment, state-response, surrender, and defeat paths available.

The terminal transaction requires the normal Chaos and territorial-readiness gates even when Maximum Global Jihad activates The Final Jihad.

The terminal actor safely resolves prior faction membership, creates the Final Command, records player choices, re-adds consenting subordinates, preserves multiplayer country scopes, and leaves coalition counterplay and defeat aftermath active.

## Decisions, missions, and exact states

The system uses the compact government-response, actor-command, and False Revelation decision categories defined in `common/decisions/categories/031_random_terror_categories.txt`.

Government and actor actions use standard state-targeted decision presentation, concrete variable-backed costs, exact state flags, target locks, outcome helpers, AI weights, and cleanup hooks.

No Event 31-specific scripted GUI exists.

Global Jihad is registered in the shared `chaosx_scenarios_window` list with all five deployment types, all four intensities, dynamic descriptions and impact warnings, fail-closed launch status, and the Event 31 preflight transaction. Maximum enables The Final Jihad but only schedules The False Revelation through the ordinary `1000+` Chaos, readiness, unity, territorial-control, crisis-state, strategic-victory, and viable-actor gates.

## Territorial actors

Eight predeclared carrier tags provide bounded territorial-country capacity without dynamic tags, custom units, Event 19 providers, 3D models, custom unit sounds, or bespoke counters.

The country package supplies valid capitals, fictional leaders and councils, existing unit templates, compatible technologies, equipment and manpower, economy and reinforcement routes, diplomacy, AI, focus loading, surrender, and cleanup.

The actor focus tree is `random_terror_actor_focus_tree` in `common/national_focus/031_random_terror_focus.txt`.

Its 114 focuses cover opening survival, Shadow Council, War Directorate, Ideological Secretariat, captured economy, armed movement, network and diplomacy, expansion, crisis, Jihadist International, Final Jihad, and False Revelation routes.

## Visual assets and wiring

The authoritative visual audit is `docs/plans/031_random_terror_plans/031_random_terror_visual_asset_audit.md`.

Base sprites are registered in `interface/031_random_terror.gfx` and the 114 focus shine sprites are registered in `interface/031_random_terror_shine.gfx`.

Focus icons live under `gfx/interface/goals/031_random_terror/` and use `GFX_goal_random_terror_*` plus exact `_shine` counterparts.

Idea icons live under `gfx/interface/ideas/031_random_terror/` and use `GFX_idea_random_terror_*`.

Decision and mission icons and the three category pictures live under `gfx/interface/decisions/031_random_terror/` and use `GFX_decision_random_terror_*`, `GFX_mission_random_terror_*`, and the three consumed `GFX_decision_category_031_random_terror_*` sprites.

Six news pictures and sixteen accepted report pictures live under `gfx/event_pictures/031_random_terror/`.

`GetRandomTerrorIncidentReportPicture` selects baseline report art from the incident type preserved by the global wave, while evolution, diplomacy, terminal, and defeat events use fixed report consumers.

Portraits live under `gfx/leaders/031_random_terror/`.

The ten-frame entity sheet lives at `gfx/interface/animated/031_random_terror/false_revelation_entity_sheet.dds`, is registered as `GFX_Portrait_Random_Terror_Entity_Animated`, and is consumed by Evolution V in the shared Event Details portrait selector.

The explicit static fallback is `GFX_Portrait_Random_Terror_Entity_Static_Fallback`, consumed by the final actor character.

Four large two-frame faction emblems and four miniature emblems live under `gfx/interface/emblems/031_random_terror/` and are consumed by the regional coordination, network confederation, Jihadist International, and Final Command faction transactions.

Thirty-seven fictional cosmetic identities provide 111 normal, medium, and small TGA files under the standard `gfx/flags/` roots.

Deterministic ordinary, transnational, and jihadist cycles expose all active identities over carrier generations, while cleanup assigns all eight dormant identities and the terminal actor uses the unique final identity.

Achievement states live directly under the engine-facing `gfx/achievements/` root as twelve colored, twelve grey, and twelve not-eligible DDS files whose basenames match their achievement IDs.

## Achievement coverage

The single root registry in `common/achievements/chaos_redux_achievements.txt` exposes the twelve accepted Event 031 IDs below.

| Achievement ID | Persistent proof flag | Visibility | Runtime icon aliases |
| --- | --- | --- | --- |
| `031_no_second_blast` | `random_terror_achievement_no_second_blast` | Visible | `GFX_achievement_031_no_second_blast[_grey|_not_eligible]` |
| `031_the_long_watch` | `random_terror_achievement_the_long_watch` | Visible | `GFX_achievement_031_the_long_watch[_grey|_not_eligible]` |
| `031_the_city_still_stands` | `random_terror_achievement_the_city_still_stands` | Visible | `GFX_achievement_031_the_city_still_stands[_grey|_not_eligible]` |
| `031_cut_every_route` | `random_terror_achievement_cut_every_route` | Visible | `GFX_achievement_031_cut_every_route[_grey|_not_eligible]` |
| `031_the_false_claim_rejected` | `random_terror_achievement_false_claim_rejected` | Visible | `GFX_achievement_031_the_false_claim_rejected[_grey|_not_eligible]` |
| `031_no_collective_punishment` | `random_terror_achievement_no_collective_punishment` | Visible | `GFX_achievement_031_no_collective_punishment[_grey|_not_eligible]` |
| `031_enemy_of_my_enemy` | `random_terror_achievement_enemy_of_my_enemy` | Visible | `GFX_achievement_031_enemy_of_my_enemy[_grey|_not_eligible]` |
| `031_fracture_from_within` | `random_terror_achievement_fracture_from_within` | Hidden | `GFX_achievement_031_fracture_from_within[_grey|_not_eligible]` |
| `031_maximum_survivor` | `random_terror_achievement_maximum_survivor` | Visible | `GFX_achievement_031_maximum_survivor[_grey|_not_eligible]` |
| `031_false_revelation_denied` | `random_terror_achievement_false_revelation_denied` | Hidden | `GFX_achievement_031_false_revelation_denied[_grey|_not_eligible]` |
| `031_victims_before_victory` | `random_terror_achievement_victims_before_victory` | Visible | `GFX_achievement_031_victims_before_victory[_grey|_not_eligible]` |
| `031_war_without_a_capital` | `random_terror_achievement_war_without_a_capital` | Hidden | `GFX_achievement_031_war_without_a_capital[_grey|_not_eligible]` |

Completion predicates live in `common/scripted_triggers/031_random_terror_triggers.txt` and read proof flags produced by `common/scripted_effects/031_random_terror_achievement_effects.txt`.

The existing `on_daily` country pass calls `random_terror_achievement_daily_tick` only for Event 031 affected countries, actors, or initialized ledgers, so historical counters survive ordinary save and reload without adding a second world iteration.

Event 031 thresholds use the existing `random_terror_tuning` script constants, including the 180-day crisis window, pressure gates, legitimacy gates, corridor count, route stage size, movement duration, capital recovery window, and major-loss threshold.

The Network Authority text icon lives under `gfx/texticons/031_random_terror/`.

Two super-event pictures live under `gfx/super_events/031_random_terror/`, are registered in `interface/chaosx_super_events.gfx`, and use a public-domain or licensed WAV package played through the shared settings-aware super-event audio helper.

## Validation surfaces

The HOI4 focus route resolves one 114-focus tree with 114 titles, zero connector crossings, and zero same-row spacing violations. Its structural render is 8,752 by 3,136; the post-fix decoded-icon raster route timed out after 180 seconds, so the earlier decoded raster remains icon evidence but is not claimed as post-fix topology proof.

The event inspector accepts the Event 31 root and returns a partial artifact without an Event 31-specific blocker.

The installed event renderer accepted an exact namespace selector but expanded into a full-workspace render and did not complete after more than six minutes, so namespace-scoped renderer evidence remains an exact tool-route blocker rather than being replaced by source-only proof.

The mandatory GUI inspector and renderer both completed for `chaosx_scenarios_window` with Event 31’s selected ID, Random Pattern type, and Maximum intensity. The renderer produced the shared-window SVG at 1920x1080 and UI scale 1. The inspector reported no missing GUI fields; inherited shared-window overlap and alignment diagnostics remain shared-layout findings rather than Event 31-owned GUI work.

## Future extensions

Optional future work can add more fictional incident compositions or additional non-weighted cosmetic identities only when they receive exact consumers, complete source and rights evidence, and the same native-scale audit.

Optional work must not add real extremist identities or symbols, sacred hostile branding, a dedicated Event 31 GUI, a custom unit, an Event 19 provider, a 3D model, a custom unit sound, or a bespoke counter.
