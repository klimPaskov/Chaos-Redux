# Event 011 Secret Alliance

Event 011 is a Minor Fire-Once diplomatic trap. It selects a valid target country, creates a hidden compact of exactly three non-war founders, and lets the target uncover or fracture the pact before it becomes the public Anti-[target] Pact. The system tracks secrecy, cohesion, readiness, suspicion, evidence, counter-readiness, leverage, member confidence, founder roles, member exits, and reveal state.

## Runtime Flow

1. Event selection checks `secret_alliance_has_valid_target_available`; if no target can produce three valid founders, Event 011 is marked unavailable instead of creating dummy members.
2. `chaosx.nr11.1` calls `secret_alliance_initialize_pact` in the target scope. The helper saves `secret_alliance_target`, selects three founders, assigns Convener, Financier, and Provocateur roles, initializes values, records the fire-once event, and starts the protocol deadline mission.
3. Founder and member state lives in `global.secret_alliance_members`, `global.secret_alliance_founders`, role flags, member confidence variables, and persistent event targets for the three founders and the public leader.
4. The target chooses an opening response: courier tracing, rail/depots protection, or composure. Each path changes evidence, suspicion, secrecy, readiness, or counter-readiness.
5. A hidden pulse, `chaosx.nr11.90`, refreshes member validity, invites eligible members, applies AI counterplay for AI targets, checks evolutions, reports unlocked stages, and schedules the next pulse while the pact remains active.
6. Evolution II opens the counter-conspiracy dossier and the timed founder-handling achievement window.
7. Public crisis comes from evidence, protocol self-reveal, or Evolution III pressure. Investigation exposure can reveal some or all members and open crisis decisions without immediately forming the formal faction or firing the reveal super-event.
8. Formal reveal comes from target-member war or final counter-ultimatum pressure. It forms the Anti-[target] Pact from `faction_template_secret_alliance_anti_target_pact`, confirms all live members, emits super-event `111`, and joins all live members to the target-member war.
9. `on_peaceconference_ended` marks target victory when the target wins the reveal war, then runs achievement checks and cleanup.

## Values and Roles

Shared dynamic tuning lives in `common/script_constants/011_secret_alliance_constants.txt`. Static decision durations live as file-scoped `@secret_alliance_*` values in `common/decisions/011_secret_alliance_decisions.txt` because decision duration fields are safer with local constants.

Main target values:

- `global.secret_alliance_secrecy`
- `global.secret_alliance_cohesion`
- `global.secret_alliance_readiness`
- `secret_alliance_suspicion`
- `secret_alliance_evidence`
- `secret_alliance_counter_readiness`
- `secret_alliance_leverage`
- `secret_alliance_member_count`
- `secret_alliance_member_exit_count`

Member values and state:

- `secret_alliance_member_confidence`
- `secret_alliance_member_role`
- `secret_alliance_member_confirmed`
- `secret_alliance_confidence_broken`
- `secret_alliance_member_left_pact`

Founder roles:

- Convener: preferred public leader when the pact becomes visible.
- Financier: linked to payment audits and conflicting promises.
- Provocateur: contributes to the pressure and border-crisis fantasy through pact readiness and incident language.
- Patron: one eligible major or faction leader can join after Evolution II, tracked by `secret_alliance_major_patron_joined`.

## Decisions and Missions

Decision category: `secret_alliance_dossier_category`.

Category metadata lives in `common/decisions/categories/011_secret_alliance_categories.txt`, while decisions and missions live in `common/decisions/011_secret_alliance_decisions.txt`. The category is visible to the target while the pact is active and uses `secret_alliance_dossier_scripted_gui` for the animated dossier panel.

Decision families:

- Investigation: `secret_alliance_trace_couriers`, `secret_alliance_audit_payments`, `secret_alliance_decode_traffic`, and targeted `secret_alliance_embassy_registry_sweep`.
- Protection: `secret_alliance_guard_rail_nodes`, `secret_alliance_shield_factories`.
- Diplomacy: `secret_alliance_backchannel`, `secret_alliance_member_backchannel`, `secret_alliance_publish_narrow_dossier`, and targeted `secret_alliance_publish_member_dossier`.
- Border work: `secret_alliance_border_watch`, targeted `secret_alliance_watch_suspect_frontier`, and `secret_alliance_customs_corridor`; border work requires a real neighboring live pact member.
- False evidence: `secret_alliance_false_leak`; success requires the player to exploit the leak and force at least one member exit after the leak resolves.
- Exposure and public crisis: `secret_alliance_expose_protocol`, `secret_alliance_demand_member_lists`, `secret_alliance_counter_ultimatum`.
- War counterplay: `secret_alliance_strike_first`, `secret_alliance_disrupt_shipments`, `secret_alliance_fracture_signatory`, and targeted `secret_alliance_targeted_fracture_signatory`.

Timed missions:

- `secret_alliance_protocol_deadline_mission`
- `secret_alliance_rail_guard_mission`
- `secret_alliance_customs_corridor_mission`
- `secret_alliance_false_leak_mission`

Each active mission has a paired completion decision: `secret_alliance_secure_guarded_junctions`, `secret_alliance_close_customs_corridor`, `secret_alliance_exploit_false_leak`, or `secret_alliance_disrupt_protocol_deadline`. Timeouts now resolve as pact-favorable or partial outcomes, while completion decisions remove the mission and apply the target-favorable result.

## Evolutions

Event 011 records evolution detail rows through `common/scripted_effects/chaosx_events_log_effects.txt` and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.

- Baseline: three founders, hidden pact values, opening choices, protocol deadline, and member validity refresh.
- Evolution I, Coordinated Minor Expansion: raises the member cap, grows suspicion and cohesion, and allows additional minor invitations.
- Evolution II, Patroned Conspiracy: opens the dossier/counterplay surface, starts the founder-handling window, enables one safe major patron, and exposes values through the GUI.
- Evolution III, Exposed Pact Crisis: raises war pressure, opens the public pact crisis, shows known/suspected member cards, and unlocks the strike-first crisis option. The formal Anti-[target] Pact faction is created by war reveal or final counter-ultimatum pressure, not by every investigation reveal.

If Event 011 first fires after an evolution is already enabled, `secret_alliance_apply_prefire_evolution_openings` applies the relevant opening values and member invitations. Evolution III pre-fire starts from the Evolution II opening package and sets a dynamic `secret_alliance_prefire_evolution_iii_pending` delay before the public crisis can unlock.

## Reveal, Faction, and War

Public crisis uses `secret_alliance_open_public_pact_crisis`. It confirms known members and extra members based on evidence quality, lowers secrecy, raises pact readiness, applies exposed-signatory ideas to confirmed members, and opens public crisis decisions without forcing immediate war.

War reveal uses `secret_alliance_reveal_pact_by_war`. It snapshots member count and major-patron state for achievements, confirms all live members, forms or reuses the public leader's faction, emits super-event `111`, and calls `secret_alliance_pull_live_members_into_reveal_war`.

Faction wiring:

- Template: `common/factions/templates/011_secret_alliance_pact.txt`
- Rules: `common/factions/rules/011_secret_alliance_rules.txt`
- Rule group: `common/factions/rules/groups/011_secret_alliance_rule_groups.txt`
- Goals: `common/factions/goals/011_secret_alliance_goals.txt`
- Dynamic name key: `secret_alliance_anti_target_pact`

## Event Log and Details

Event 011 is registered as fire-once event ID `11` through existing Chaos Redux event settings logic. The default event-log actor is the saved target country. Event name localisation uses `chaosx.event_name.11`.

Event detail and evolution detail localisation keys live in `localisation/english/011_secret_alliance_l_english.yml`:

- `chaosx.events_log.window.event_details.secret_alliance`
- `chaosx.events_log.window.evolution_details.secret_alliance.*`

Scripted localisation dispatch for Secret Alliance evolution rows lives in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.

## Super-Event and Audio

Reveal super-event ID: `111`.

- Title: `The Pact Made Public`
- Main quote: Immanuel Kant, *Perpetual Peace*
- Button text: `Openly arrived at.`
- Image sprite: `GFX_super_event_secret_alliance_reveal`
- Runtime image: `gfx/super_events/011_secret_alliance/super_event_secret_alliance_reveal.dds`
- Runtime music: `music/super_event_secret_alliance_reveal.ogg`
- Runtime sound channel: `sound/chaosx_super_event_secret_alliance_reveal.wav`
- Source audio: `docs/super_events/source_audio/011_secret_alliance/beethoven_egmont_overture_source.ogg`
- Research note: `docs/super_events/011_secret_alliance_super_event_research.md`

Audio definitions are wired in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, `sound/chaosx_sound.asset`, and `localisation/english/chaosx_music_l_english.yml`.

## Achievements

Event 011 achievements are registered in `common/achievements/chaos_redux_achievements.txt`, localised in `localisation/english/011_secret_alliance_l_english.yml`, and wired in `interface/chaosx_achievements.gfx`.

- `011_secret_alliance_empty_chair`
- `011_secret_alliance_all_names`
- `011_secret_alliance_three_knocks`
- `011_secret_alliance_lone_target`
- `011_secret_alliance_counter_protocol`
- `011_secret_alliance_wrong_room`
- `011_secret_alliance_no_patrons`
- `011_secret_alliance_paid_in_promises`

Achievement tracking is tied to pact outcomes rather than event firing: member exits, confirmed live members, founder handling during the Evolution II window, reveal-war victory, strike-first timing, major-patron prevention, and false-leak expulsion.

## Cleanup

`secret_alliance_cleanup_after_resolution` removes active target ideas, active mission flags, member ideas, member role flags, member arrays, founder arrays, and persistent event targets after peaceful collapse or reveal-war victory. Achievement and historical result flags remain on the target for completion checks and player-facing history.

Member invalidation is handled by `secret_alliance_refresh_member_validity`, which removes invalid countries from the live array and collapses the pact if it falls below the active pre-reveal floor.

## Asset Wiring

Runtime sprite registry: `interface/011_secret_alliance.gfx`.

Decision/category sprites:

- `GFX_decision_category_secret_alliance_dossier`
- `GFX_decision_secret_alliance_courier`
- `GFX_decision_secret_alliance_rail_guard`
- `GFX_decision_secret_alliance_expose`
- `GFX_decision_secret_alliance_backchannel`
- `GFX_decision_secret_alliance_border_watch`
- `GFX_decision_secret_alliance_factory_shield`
- `GFX_decision_secret_alliance_false_leak`
- `GFX_decision_secret_alliance_strike_first`

Idea sprites:

- `GFX_idea_secret_alliance_dossier_pressure`
- `GFX_idea_secret_alliance_counter_network`
- `GFX_idea_secret_alliance_protocol_discipline`
- `GFX_idea_secret_alliance_patron_liaisons`
- `GFX_idea_secret_alliance_exposed_signatory`
- `GFX_idea_secret_alliance_war_coordination`
- `GFX_idea_secret_alliance_credibility_restored`

Report and UI sprites:

- `GFX_report_event_secret_alliance_meeting`
- `GFX_report_event_secret_alliance_sabotage`
- `GFX_report_event_secret_alliance_protocol`
- `GFX_secret_alliance_dossier_bg`
- `GFX_secret_alliance_pact_emblem`

Animated dossier sprites:

- `GFX_secret_alliance_evidence_pulse_animated`; fallback `GFX_secret_alliance_evidence_pulse_static`
- `GFX_secret_alliance_readiness_warning_animated`; fallback `GFX_secret_alliance_readiness_warning_static`
- `GFX_secret_alliance_exposed_card_glow_animated`; fallback `GFX_secret_alliance_exposed_card_glow_static`
- `GFX_secret_alliance_war_countdown_ticker_animated`; fallback `GFX_secret_alliance_war_countdown_ticker_static`
- `GFX_secret_alliance_hidden_protocol_overlay_animated`; fallback `GFX_secret_alliance_hidden_protocol_overlay_static`

Source and validation manifests live in `docs/assets/011_secret_alliance/`. Final DDS assets live under `gfx/event_pictures/011_secret_alliance/`, `gfx/interface/decisions/011_secret_alliance/`, `gfx/interface/ideas/011_secret_alliance/`, `gfx/interface/animated/011_secret_alliance/`, `gfx/interface/secret_alliance/`, `gfx/super_events/011_secret_alliance/`, and `gfx/achievements/`.

## Future Plans and Suggestions

- Add more specialised role incident chains for the targeted dossier cards if later testing shows the current country-targeted decisions need more variety.
- Add focused incident events for convener diplomacy, financier payments, and provocateur border theatre so each role has more distinctive pressure before reveal.
- Tune the existing AI pulse, decision weights, and faction-goal priorities further if live testing shows pact members under-prepare for the reveal war.
- Add more event-log evolution entries for major patron arrival and peaceful public collapse if the event log UI gains room for outcome subentries.
