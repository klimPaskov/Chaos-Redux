# Event 011 - Secret Alliance

Event 011 is `Secret Alliance`, a minor fire-once event rooted at `chaosx.nr11.1`. Secret Alliance begins with foreign coldness around one target country. Couriers change routes, embassy language starts to match, and minor governments learn how private distance can become shared pressure. As the pattern grows, the room gains more chairs, a larger sponsor, and a public `Anti-[target country] Pact`. War with a hidden member can tear the deniable phase open and turn the compact into a named coalition.

## Flow

The random-event dispatcher prepares Event 011 through `secret_alliance_prepare_random_event_fire`. The helper scores valid targets, chooses one target through weighted random selection, saves it as `event_target:secret_alliance_target`, and fires `chaosx.nr11.1` only when the target has at least three valid minor founder candidates.

The hidden root event calls `secret_alliance_start_from_root_event`. That effect marks the target as active, initializes dossier variables, picks exactly three minor founders, and schedules the hidden pulse. Founders must be independent minors, must not be subjects, must not already be members, must not share a faction with the target, and must not be at war with the target. Each founder receives confidence and exposure variables, enters the global member arrays, and remains hidden until exposure or public reveal. If the shared chaos tier has already unlocked the later Event 011 stages, the compact still opens hidden first. Evolution II or III starts add a valid major patron as a hidden patron-founder when one is available, then open the counterplay and public-pact stages through the evolved-start helpers.

The hidden pulse `chaosx.nr11.10` grows suspicion, evidence, infiltration, pressure, cohesion, and war preparation. It also exposes members through controlled incidents, opens the target dossier when the evidence gate is reached, and schedules the next relevant mission through the active-operation cap. Before Evolution II the pulse favors press pressure, courier movement, partial exposure, and wavering members. After Evolution II it can also produce sabotage attempts, border provocations, and assassination or abduction attempts.

- Evolution I, `Minor Expansion`: attempts two scored minor invitations and can produce joins, quiet refusals, leaks, private approaches, or wavering accessions before firing `chaosx.nr11.21`.
- Evolution II, `Major Patron`: scores valid major sponsors, chooses a patron, opens the counter-play category, applies stronger foreign subversion pressure, and fires `chaosx.nr11.31`.
- Evolution III, `Public Pact`: reveals the compact, creates the public faction, exposes remaining members, and fires the news and super-event surfaces.

If any hidden member enters war with the target before the planned public reveal, `secret_alliance_on_war_relation_added` immediately forces a war-caused reveal. The public faction is created only when at least one member is still valid for public faction service, valid public members are placed in the pact, and every valid public member is called into the target war through the shared war-join helper.

## Dynamic State

Target variables are centralized through `common/script_constants/011_secret_alliance_constants.txt` and helpers in `common/scripted_effects/011_secret_alliance_effects.txt`.

Target variables include:

- `pact_suspicion`
- `pact_evidence`
- `pact_preparedness`
- `pact_infiltration`
- `pact_pressure`
- `pact_cohesion`
- `pact_war_preparation`
- `pact_member_count`
- `pact_known_member_count`
- `pact_public_member_count`

Member state uses flags for true and false conditions, including `secret_alliance_member`, `secret_alliance_founder`, `secret_alliance_patron`, `secret_alliance_wavering`, `secret_alliance_exposed`, and `secret_alliance_public_member`. Member confidence and exposure remain numeric variables because they scale selection, exit, exposure, and reveal behavior.

The main arrays are:

- `global.secret_alliance_members`
- `global.secret_alliance_founders`
- `global.secret_alliance_known_members`
- `global.secret_alliance_public_members`

Scoring reads target threat, diplomacy, geography, claims on candidate territory, factories, divisions, diplomatic rivalry, and member readiness. Shared constants keep thresholds and decision costs tunable.

## Decisions And Missions

Secret Alliance uses two categories:

- `secret_alliance_dossier_category`, visible when the target has enough evidence to open the Dossier Board.
- `secret_alliance_counterplay_category`, visible after the major patron stage or public reveal.

The Dossier Board is a scripted GUI attached to the dossier category. It shows stage, suspicion, evidence, preparedness, infiltration, pact pressure, cohesion, estimated members, known members, the selected member file, and the latest incident. Evidence, pressure, and preparedness meters switch between thresholded fill states, so the board changes with the target's live variables rather than a fixed art layer. It uses member-card art, meter art, selected-card buttons, and animated danger accents with frame-sheet sprites plus static fallbacks. The button handlers can select an exposed member, wavering member, neighboring member, or suspected patron, and member-facing decisions use that selected card before falling back to another valid member.

Decision costs are varied by action and do not rely on a flat political power button model. Costs include command power, political power, stability, army XP, air XP, support equipment, infantry equipment, trucks, trains, fuel, and manpower. Cost gates and spends are stored in `secret_alliance_decision_cost`.

Core decision lanes:

- Evidence work: trace diplomatic pouches, turn a courier, break a radio net, audit foreign missions, and build the public dossier.
- Defensive preparation: guard rail and port nodes, vet military staff, harden munitions plants, and secure capital ministries.
- Diplomacy and member pressure: quiet talks with a member, face-saving exit, pressure neutrals, and controlled leak.
- Public crisis response: sweep safehouses, seal a courier pass, limited border reprisal, contingency plans, fuel reserve security, local defense committees, rally friendly governments, prepare the public war case, demand pact disbandment, and launch a preemptive strike when evidence and preparedness are high.

Timed missions test whether preparation holds:

- `guard_capital_network_mission`
- `secure_industrial_belt_mission`
- `keep_foreign_route_watched_mission`
- `expose_patron_hand_mission`
- `hold_border_public_crisis_mission`

Mission success requires the player to complete the stated objective before the timer expires. Capital defense checks the controlled capital state, its route or city value, local divisions, and a completed security action. Industrial defense checks a controlled factory state with local divisions and a plant-security action. Foreign route watch checks trains, an audited or sealed route, and a guarded rail, port, air, or frontier route when one exists. Patron exposure checks high evidence, a known patron, diplomatic or leak work, and the same route file logic. Public border defense checks fuel, a defense plan, and local divisions on a neighboring public-pact border when there is one. Success raises preparedness, evidence, public credibility, or achievement predicates. Failure on timeout increases exposure risk, infiltration, pressure, or public crisis cost. The scheduler keeps the board to one active operation at a time and then offers the next relevant mission.

## AI

AI behavior is defined in decision `ai_will_do` blocks, role flags, and supporting scoring constants. The target AI favors evidence work while the compact is hidden, defensive preparation when infiltration or pressure rises, patron exposure when the patron stage is active, and public war-case preparation after reveal. AI use is biased by stability, command resources, divisions, evidence, preparedness, public stage, and direct war danger. Member and patron countries receive antagonize and prepare-for-war strategies toward the target when they join the compact.

Compact member selection and patron selection are also dynamic. Minor invitations prefer countries with useful geography, target rivalry, military weight, factories, and no direct disqualifying war or faction state. Patron selection prefers majors with a reason to back the compact and excludes the target, existing members, subjects, and countries already at war with the target.

## Public Pact And Super-Event

The public faction uses `common/factions/templates/secret_alliance_public_pact.txt` with the visible name `Anti-[secret_alliance_target.GetName] Pact`. Public reveal can be caused by Evolution III, the target building a public dossier, or war with a hidden member. War-caused reveal saves the member that exposed the compact and first tries to add all valid public members to that existing war. The lifecycle refresh repairs an invalid public leader by choosing the patron, a founder, or another valid public member before war calls are made, and capitulation refreshes the target-side lifecycle so a collapsed public member does not leave stale leadership. If no valid public member exists when reveal is attempted, or if the public member pool later collapses, the compact closes and leaves the defeated-state achievement flags behind.

The super-event uses slot `28` and the direction researched in `docs/super_events/011_secret_alliance_super_event_research.md`. The final title direction is `Anti-[target country] Pact`. The quote is a short Thucydides excerpt, and the remark is `The understanding is now public.` Audio research and licensing are recorded in `docs/super_events/011_secret_alliance_audio_research.md`. The final music file is `music/super_event_secret_alliance_reveal.ogg`, with sound wiring in `sound/chaosx_sound.asset`. The reveal helper only emits the super-event when the reveal has campaign weight through war, high evidence, high pressure, a patron, public stage progression, or a large enough member count.

## Event Log And Details

Event 011 writes a normal event log row with the target as actor. Event Details describe the hidden compact, the three-founder launch requirement, member expansion, major patron, public pact, and war-caused reveal behavior. Evolution detail rows cover the hidden compact, minor expansion, major patron, public pact, and war reveal. The related integration is in:

- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/011_anti_player_pact_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`

## Gameplay Surfaces

- Event script: `events/011_anti_player_pact.txt`
- Constants: `common/script_constants/011_secret_alliance_constants.txt`
- Triggers: `common/scripted_triggers/011_secret_alliance_triggers.txt`
- Effects: `common/scripted_effects/011_secret_alliance_effects.txt`
- On-action hook: `common/on_actions/chaosx_on_actions.txt`
- Decisions: `common/decisions/categories/011_secret_alliance_categories.txt`, `common/decisions/011_secret_alliance_decisions.txt`
- Faction template: `common/factions/templates/secret_alliance_public_pact.txt`
- Ideas: `common/ideas/011_secret_alliance_ideas.txt`
- Scripted GUI: `common/scripted_guis/011_secret_alliance_dossier_board_scripted_gui.txt`, `interface/011_secret_alliance_dossier_board.gui`
- Scripted localisation: `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- Player localisation: `localisation/english/011_anti_player_pact_l_english.yml`
- Sprite registry: `interface/011_secret_alliance.gfx`
- Achievement registry: `common/achievements/chaos_redux_achievements.txt`, `interface/chaosx_achievements.gfx`, and `localisation/english/chaosx_achievements_l_english.yml`

## Assets

Final asset records are in `docs/assets/011_secret_alliance/manifest.md`, `docs/assets/011_secret_alliance/gfx_handoff.md`, and the related subagent handoffs in `docs/plans/011_secret_alliance_plans/subagent_handoffs/`.

Report, news, and super-event sprites:

- `GFX_report_event_secret_alliance_meeting`
- `GFX_report_event_secret_alliance_courier`
- `GFX_report_event_secret_alliance_sabotage`
- `GFX_news_event_secret_alliance_reveal`
- `GFX_super_event_secret_alliance_reveal`

Dossier Board and pact sprites:

- `GFX_secret_alliance_board_bg`
- `GFX_secret_alliance_member_unknown`
- `GFX_secret_alliance_member_known`
- `GFX_secret_alliance_founder_badge`
- `GFX_secret_alliance_patron_badge`
- `GFX_secret_alliance_wavering_badge`
- `GFX_secret_alliance_pact_emblem`
- `GFX_secret_alliance_evidence_meter` and fill variants
- `GFX_secret_alliance_pressure_meter` and fill variants
- `GFX_secret_alliance_preparedness_meter` and fill variants

Animated sprites with static fallbacks:

- `GFX_secret_alliance_radio_pulse_static` and `GFX_secret_alliance_radio_pulse`
- `GFX_secret_alliance_thread_glow_static` and `GFX_secret_alliance_thread_glow`
- `GFX_secret_alliance_seal_crack_static` and `GFX_secret_alliance_seal_crack`
- `GFX_secret_alliance_border_warning_static` and `GFX_secret_alliance_border_warning`

Decision and idea icons:

- `GFX_decision_category_secret_alliance_dossier`
- `GFX_decision_secret_alliance_trace_pouches`
- `GFX_decision_secret_alliance_turn_courier`
- `GFX_decision_secret_alliance_radio_net`
- `GFX_decision_secret_alliance_guard_rail`
- `GFX_decision_secret_alliance_harden_plants`
- `GFX_decision_secret_alliance_quiet_talks`
- `GFX_decision_secret_alliance_exit_offer`
- `GFX_decision_secret_alliance_safehouses`
- `GFX_decision_secret_alliance_war_case`
- `GFX_idea_secret_alliance_coldness`
- `GFX_idea_secret_alliance_subversion`
- `GFX_idea_secret_alliance_counter_office`
- `GFX_idea_secret_alliance_public_hostility`

Achievement icons use the achievement id filenames in `gfx/achievements/`, for example `secret_alliance_open_file.dds`, with `_grey` and `_not_eligible` variants.

## Achievements

Event 011 adds ten achievements:

- `secret_alliance_open_file`
- `secret_alliance_empty_chairs`
- `secret_alliance_no_one_came`
- `secret_alliance_border_knife`
- `secret_alliance_patron_exposed`
- `secret_alliance_counter_pact`
- `secret_alliance_alone_against_room`
- `secret_alliance_last_signature`
- `secret_alliance_clean_reveal`
- `secret_alliance_war_case`

The achievement predicates are set by event, decision, mission, reveal, cleanup, and war helpers rather than by visible button counts alone. They track founder exposure before Evolution II, founding-member exits before reveal, weak public opening turnout, successful limited border reprisal before reveal, patron isolation before public stage, two friendly-government rallies plus survival of the first public crisis, minor-target isolation against a patron-backed public pact, founding-member removal inside the post-reveal deadline, clean evidence reveal without fatal sabotage, and a prepared war-case victory without core-state loss.

## Future Plans

- Add a post-reveal diplomatic congress lane for neutral countries that want to mediate without joining the pact.
- Add a public faction rule package for pact members if the faction system later needs more bespoke rule behavior.
- Add more Dossier Board member portraits or country-slot markers if future scripted GUI work supports repeated dynamic country entries cleanly.
- Add extra patron-specific incidents for major powers with strong ideology or trade ties to the target.
