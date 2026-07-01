# Event 011 - Secret Alliance

Event 011 is `Secret Alliance`, a fire-once random event rooted at `chaosx.nr11.1`. It creates a hidden anti-target compact without forming a public faction at start. The target sees indirect diplomatic pressure, suspicious incidents, and evidence trails before any member list is made public.

## Flow

The random-event dispatcher checks `secret_alliance_automatic_event_available` before Event 011 can enter the active pool. A valid target must have enough valid minor countries outside factions, outside subject relationships, outside direct war with the target, and outside special Chaos country state. If those candidates do not exist, the event does not fire.

The hidden root event clears stale Secret Alliance runtime state, saves the target as `secret_alliance_target`, records the active global state, chooses the opening strength from the current evolution tier, and selects the hidden core members. Baseline opening selects three valid minor core members. Evolution I pre-fire opening can start with a wider minor compact. Evolution II or III pre-fire opening starts from the Evolution II model: a major patron plus three minor core members, preserving a later escalation window before the public crisis.

Hidden formation never creates a faction. Core members receive hidden compact discipline and AI war-preparation strategies, while the target receives Unexplained Diplomatic Friction and the first report event. The target state owns the compact variables: secrecy, cohesion, readiness, hostility, recruitment, suspicion, evidence, preparedness, counter-network strength, known-member counts, and operation counters.

Operation pulses are scheduled with stage-sensitive randomized timing. Each pulse first checks whether any valid core member is at war with the target. If so, the pact reveals immediately. Otherwise it selects a staged pressure family: baseline courier and diplomatic pressure, Evolution I recruitment and propaganda pressure, Evolution II sabotage, intimidation, leaks, and provocations, or Evolution III war council and public crisis pressure. Operations adjust evidence, suspicion, secrecy, readiness, cohesion, hostility, recruitment, member exposure, and achievement predicates through shared scripted effects.

War-trigger reveal is handled from `on_war_relation_added` in both ROOT and FROM directions. The target reruns the reveal from its own scope, exposes all valid core members, chooses a public leader, creates the public Anti-[target] compact when the leader is not already in a faction, and brings every valid core member into war against the target immediately. Major patron and second-major participants also join the war if valid.

Resolution without war can occur through high-quality evidence, diplomacy, and cohesion pressure. Public reveal and preemptive strike paths convert the target from hidden-counterintelligence play into public war command play.

## Evolutions

Event 011 records three evolution stages through the Event Log system.

- Evolution I, Wider Minor Compact: expands the hidden minor-country network, increases recruitment pressure, and makes the pattern more visible without naming members publicly.
- Evolution II, Major Patron and Counter-Pact Desk: brings in a major patron when valid, opens the counter-pact decision system, raises operation severity, and gives the target evidence and preparedness tools.
- Evolution III, Public Crisis: can add a second major only when the target has not already split or overexposed the compact and lacks strong outside backing, opens public confrontation and war options, starts the final crisis mission, and pressures the pact toward reveal, dissolution, or war.

Active-event evolution effects update the existing pact. Pre-fire evolution changes the opening strength only when the stronger opening can be formed with valid candidates.

## Gameplay Surfaces

- Event script: `events/011_secret_alliance.txt`
- News event: `events/_chaosx_news.txt`, event `chaosx.news.11`
- Constants: `common/script_constants/011_secret_alliance_constants.txt`
- Effects: `common/scripted_effects/011_secret_alliance_effects.txt`
- Triggers: `common/scripted_triggers/011_secret_alliance_triggers.txt`
- Decisions and missions: `common/decisions/011_secret_alliance_decisions.txt`
- Ideas: `common/ideas/011_secret_alliance_ideas.txt`
- On-actions: `common/on_actions/chaosx_on_actions.txt`
- Random-event integration: `common/scripted_effects/chaosx_logic_effects.txt`, `common/scripted_effects/chaosx_settings_effects.txt`, `common/scripted_triggers/chaosx_settings_triggers.txt`
- Event Log integration: `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Achievements: `common/achievements/chaos_redux_achievements.txt`
- Localisation: `localisation/english/011_secret_alliance_l_english.yml`, `localisation/english/chaosx_event_names_l_english.yml`
- Sprite registrations: `interface/011_secret_alliance.gfx`
- Asset package: `docs/assets/011_secret_alliance/`

## Decisions And AI

The Counter-Pact Desk appears once Evolution II is active or the target has enough suspicion or evidence to justify a dedicated response. It is not a political-power store: most actions combine command power, army or air experience, equipment, trains, trucks, manpower, stability, war support, diplomacy, known-member state, or evidence thresholds.

Investigation actions map courier routes, compare cipher traffic, raid safehouses, question intercepted liaison staff, compile dossiers, handle defectors, and publish evidence. Security actions harden procurement, rail offices, industrial districts, officers, contracts, ports, planning rooms, capitals, reserve depots, and border procedures. Diplomacy actions pressure exposed links, offer off-ramps, test rival patrons, call conferences, and attempt last talks. Border options search crossings, close routes, run patrols, prepare limited border war, and coordinate inspectors. Public confrontation actions demand dissolution, authorize publication, allow preemptive strike, and manage the final crisis window.

Several defensive actions are timed deployments rather than instant buttons. Rail offices, industrial districts, ports and cables, frontier watch, and capital command require fielded coverage or route-specific conditions, pay their equipment or command costs up front, then complete through follow-up deadline missions. Counter-network, exposed-border, and final-crisis missions track deeper strategic deadlines. Success raises preparedness, evidence, or counter-network strength; failure can compromise ministries, raise pact readiness, cohesion, hostility, or force the public crisis toward daylight.

AI uses the same category and equivalent target pulses respect the same resource and route gates instead of receiving free generic progress. Weights vary by evidence, preparedness, stage, war state, resource thresholds, known members, exposure, border coverage, and reveal state. Hidden core members and patrons receive antagonize, prepare-for-war, arms-factory, and border-defense strategy pressure through the pact stage. Revealed members switch to direct conquer and antagonize strategies against the target.

## Achievements

Event 011 adds eight achievements:

- `sa_every_thread_named`: expose every active core member before public reveal or war-trigger reveal.
- `sa_paper_collapse`: dissolve the pact without triggering the reveal war.
- `sa_turn_the_knife`: convince a member to defect and use the defector trail to expose another member.
- `sa_prepared_for_every_border`: identify enough neighbor members, cover an exposed compact-facing border with fielded divisions, and reach high border preparedness without a failed border deadline.
- `sa_small_country_large_shadow`: as a minor target, survive a revealed pact that included a major patron without joining a major faction route.
- `sa_ten_signatures`: resolve or defeat a pact that reached ten core or known members without target capitulation.
- `sa_bad_evidence_backfire`: recover from a failed public-dossier push that strengthens the pact.
- `sa_no_factory_lost`: complete the chain after Evolution II without target capitulation or successful major industrial sabotage.

Tracking uses flags and variables set by the actual route predicates. Eligibility can be lost by war reveal before all exposure, target capitulation, joining a major faction for the small-country route, successful major industrial sabotage, or other route-specific failure conditions.

## Assets

All Event 011 sprites are registered in `interface/011_secret_alliance.gfx`.

Event pictures:

- `GFX_report_event_011_secret_alliance_courier`: `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_courier.dds`
- `GFX_report_event_011_secret_alliance_sabotage`: `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_sabotage.dds`
- `GFX_report_event_011_secret_alliance_defector`: `gfx/event_pictures/011_secret_alliance/report_event_011_secret_alliance_defector.dds`
- `GFX_news_event_011_secret_alliance_reveal`: `gfx/event_pictures/011_secret_alliance/news_event_011_secret_alliance_reveal.dds`

Decision icons:

- `GFX_decision_category_secret_alliance`: `gfx/interface/decisions/011_secret_alliance/decision_category_secret_alliance.dds`
- `GFX_decision_secret_alliance_investigate`: `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_investigate.dds`
- `GFX_decision_secret_alliance_security`: `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_security.dds`
- `GFX_decision_secret_alliance_split`: `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_split.dds`
- `GFX_decision_secret_alliance_border_watch`: `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_border_watch.dds`
- `GFX_decision_secret_alliance_confront`: `gfx/interface/decisions/011_secret_alliance/decision_secret_alliance_confront.dds`

The operation-specific decision sprite aliases in the decision file intentionally resolve to these five generated decision icon families.

Ideas:

- `GFX_idea_secret_alliance_friction`: `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_friction.dds`
- `GFX_idea_secret_alliance_bureau`: `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_bureau.dds`
- `GFX_idea_secret_alliance_prepared_network`: `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_prepared_network.dds`
- `GFX_idea_secret_alliance_exposed_member`: `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_exposed_member.dds`
- `GFX_idea_secret_alliance_patron_shield`: `gfx/interface/ideas/011_secret_alliance/idea_secret_alliance_patron_shield.dds`

Final idea aliases registered for script use reuse those stable art families: `GFX_idea_secret_alliance_unexplained_friction`, `GFX_idea_secret_alliance_counter_pact_bureau`, `GFX_idea_secret_alliance_prepared_security_network`, `GFX_idea_secret_alliance_compromised_ministries`, `GFX_idea_secret_alliance_hidden_compact_discipline`, `GFX_idea_secret_alliance_exposed_pact_government`, `GFX_idea_secret_alliance_revealed_compact`, and `GFX_idea_secret_alliance_public_war_command`.

Scripted GUI and animated surfaces:

- `GFX_secret_alliance_pact_emblem`: `gfx/interface/011_secret_alliance/secret_alliance_pact_emblem.dds`
- `GFX_secret_alliance_board_bg`: `gfx/interface/011_secret_alliance/secret_alliance_board_bg.dds`
- `GFX_secret_alliance_suspect_card_frame`, `_selected`, `_dim`, `_locked`: `gfx/interface/011_secret_alliance/`
- `GFX_secret_alliance_evidence_meter_frame`, `_fill_low`, `_fill_mid`, `_fill_high`: `gfx/interface/011_secret_alliance/`
- `GFX_secret_alliance_hidden_seal` and `GFX_secret_alliance_hidden_seal_animated`: `gfx/interface/animated/011_secret_alliance/`
- `GFX_secret_alliance_evidence_meter_highlight` and `GFX_secret_alliance_evidence_meter_highlight_animated`: `gfx/interface/animated/011_secret_alliance/`
- `GFX_secret_alliance_crisis_frame` and `GFX_secret_alliance_crisis_frame_animated`: `gfx/interface/animated/011_secret_alliance/`

Achievement icons use base, grey, and not-eligible DDS triplets in `gfx/achievements/` for all `sa_*` achievement ids.

The asset source files, prompts, contacts, previews, DDS copies, and handoffs live under `docs/assets/011_secret_alliance/` and `docs/plans/011_secret_alliance_plans/subagent_handoffs/`.

## Future Plans

- Add a bespoke scripted GUI board that uses the existing board, suspect-card, seal, meter, and animation sprites as a richer Counter-Pact Desk view. The current implementation exposes the required desk values through the decision category.
- Add optional associate-member content that can leak clues without counting toward the required hidden core opening.
- Expand post-war settlement outcomes for a defeated revealed compact, especially for minor targets that survive a major-backed crisis.
