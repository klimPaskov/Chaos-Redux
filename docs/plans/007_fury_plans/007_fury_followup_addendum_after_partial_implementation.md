# Event 007 Fury follow-up addendum after partial implementation

## Purpose

Event 007 Fury has a full implementation surface: actor selection, Fury actor package, self-scheduled weekly loop, scored target selection, first-conquest news `chaosx.news.7007`, decisions and missions, a 52-focus shared tree, triggerable scenario `The World in Fury`, event-log detail mapping, ten achievement definitions, final Fury-specific asset triplets, major slot `59` super-event wiring, terminal slot `60` world-end wiring, and docs/assets manifests.

Recent patches also fixed the old news-id conflict, slot `59` image sprite wiring, decision cost gate mismatches, cooperation/rivalry mutual exclusion, settlement control and compliance gates, depot reward dumping, `var:fury_current_target` war declaration, evolution unlock flag sync, Evolution I misapplication, and the world-end focus setting only `fury_world_end_candidate`.

This addendum is retained as the implementation checklist and audit ledger for the Fury buildout. Its phase requirements have been implemented or explicitly bounded below, with final completion judged by the current audit reports and validation evidence rather than this document alone.

No broad new premise is queued from this addendum. Future work should come from focused audit findings or live-session balance evidence.

Implementation progress note:

- Phase 1 has been implemented as a 52-focus shared tree with route gates, localisation, icons, AI weights, and focus-auditor fixes for evolved/scenario actors.
- Phase 2 has been implemented with scored neighbor handling covering size, industry, divisions, manpower, war state, faction state, major status, rough terrain, supply nodes, Fury momentum, overextension, target preparation, evolution state, and last-target churn.
- Phase 3 has been implemented for occupation pressure, garrison capacity, register work, rail registry work, crisis mission, and two coring methods.
- Phase 4 has been implemented with terminal eligibility, visible seed blocking, world-end flags, Fury-only faction setup, continent-first seeding, player warning/grace, a terminal-only player-linked targeting helper, terminal reserve decisions, world-threat integration, slot `60` super-event text/final image/audio wiring, defeat cleanup for the Fury threat source, and three-continent world-end achievement tracking.
- Phase 5 has been implemented as a staged anti-Fury response surface with Border Watch, Emergency Aid, Firebreak Staff Talks, Supply Denial, Recognition Denial, and mission failure checks tied to capital, border, and active-war pressure.
- Phase 6 has been implemented with achievement tracking tied to containment contribution, scenario intensity/type, all-safe-candidate Maximum fallback, Fury-on-Fury war declarations, major-Fury defeat, no-coring containment, and terminal world-end defeat.
- Phase 7 has been implemented with final report/news/UI/focus/idea/decision/category/achievement/super-event assets, sourced audio, quote/audio ledgers, and GFX registrations.

## Prior addendum status

No prior addendum exists under `docs/plans/007_fury_plans/` at the time of this pass. This file remains as the Fury follow-up audit ledger; new Fury expansion work should come from focused audit findings or live-session balance evidence.

## Implementation phases

### Phase 1: Expand Fury into a real shared focus tree

Current status: the shared tree has been expanded into a 52-focus route tree with opening, army, expansion, occupation, cooperation, rivalry, evolution, and world-end branches. Key branch icons are wired through `interface/007_fury.gfx`.

Replace the skeleton with a compact but real shared tree of roughly 35 to 45 focuses. Do not bulk-generate filler. The tree should keep the existing `fury_focus_tree` id and preserve existing focus ids where they already unlock implemented systems, but add route depth around them.

Required route families:

| Route family | Existing anchor | New focus groups to add | Mechanical purpose |
| --- | --- | --- | --- |
| Opening trunk | `fury_open_the_war_office`, `fury_count_the_rifles`, `fury_capital_guard` | `fury_war_office_without_a_door`, `fury_first_war_office_orders` | establish the War Office, unlock category, create first-war readiness without generic PP rewards |
| Army of the March | `fury_field_columns`, `fury_forward_depots` | `fury_depot_cadres`, `fury_storm_columns`, `fury_logistics_under_movement`, `fury_officer_tables` | vary templates, weekly unit quality, trains/trucks/support equipment use, commander or army XP rewards |
| Expansion | `fury_first_target_files`, `fury_all_borders` | `fury_one_border_at_a_time`, `fury_weak_neighbor_doctrine`, `fury_capital_first_plans`, `fury_cut_the_rail_before_the_war`, `fury_the_next_neighbor` | improve target scoring, target-prep decisions, capital focus, no-war spam safety |
| Occupation and integration | `fury_occupation_registers`, `fury_conquest_coring` | `fury_census_of_taken_states`, `fury_new_registry_offices`, `fury_rail_and_registry`, `fury_garrison_the_names`, `fury_core_by_administration`, `fury_core_by_march` | make overextension and coring a living occupation loop |
| Cooperation | `fury_second_war_table` | `fury_the_other_fire_answers`, `fury_shared_war_tables`, `fury_partition_before_victory`, `fury_joint_cadre_transfers`, `fury_fury_pact_command` | deepen pact route and shared aid |
| Rivalry | `fury_rival_column` | `fury_no_second_fury`, `fury_claim_the_same_map`, `fury_absorb_the_rival_fire`, `fury_last_fury_standing` | deepen hostile Fury route and Fury-on-Fury payoff |
| Evolution I | `fury_hardened_doctrine` | `fury_harden_the_columns`, `fury_depot_officers_without_leave`, `fury_forced_march_tables`, `fury_occupation_as_recruitment` | make Hardened Fury visible beyond one idea swap |
| Evolution III | `fury_all_borders` | `fury_three_war_offices`, `fury_storms_on_all_fronts`, `fury_no_target_is_first`, `fury_all_roads_are_front_roads` | support all-neighbor declaration with supply and overextension costs |
| World-end candidate | `fury_world_in_fury` | `fury_the_last_neighbor_has_fallen`, `fury_carry_the_orders_overseas`, `fury_continental_ignitions`, `fury_main_fury_pact`, `fury_no_neutral_map` | prepare terminal branch, but do not activate it before eligibility |

Focus rewards must be varied:

- decision and mission unlocks for target prep, depot conversion, border watch, settlement, and world-end preparation.
- template upgrades and route-specific units only where they are not repeated free-unit dumps.
- equipment, support equipment, trucks, trains, army XP, command power, rail repair, supply support, garrison cadres, compliance, and overextension changes.
- staged idea lifecycle: `fury_national_fury`, `fury_hardened_fury`, `fury_overextension`, `fury_compliance_drive`, `fury_pact_command`, `fury_rival_doctrine`, and a new terminal idea `fury_world_fury` if Phase 4 is implemented.

Focus AI must respect route state:

- opening trunk first.
- army focuses when divisions, equipment, or current war pressure are weak.
- occupation focuses when `fury_overextension` is high or a settlement state exists.
- expansion focuses when a valid target exists and overextension is below the hard gate.
- cooperation focuses only when Evolution II is applied and pact type or cooperation route is active.
- rivalry focuses only when hostile type, rival route, or pact collapse is active.
- Evolution III focuses only when `fury_evolution_iii_applied`.
- world-end branch only when the country is a real `fury_world_end_candidate` and terminal eligibility trigger passes.

Acceptance for this phase:

- The tree is no longer a 13-focus skeleton.
- Every promised route family has several focuses or focus groups with distinct effects.
- Cooperation and rivalry branches remain mutually exclusive.
- Route rewards are not mostly PP/stability/war support/tiny modifiers.
- Focus filters, icons or registered placeholders, localisation, AI weights, and docs are updated with the final focus list.
- A route coverage table compares this addendum against implemented focus ids.

### Phase 2: Replace simplified target selection with scored target handling

Current status: target selection uses scored neighbor handling, stale-target cleanup, Evolution III all-neighbor declarations, and a split rule where player-linked countries cannot become Fury actors but can be Fury targets under normal target rules.

Add a target-scoring layer around the existing `fury_choose_next_target`, `fury_declare_on_current_target`, and `fury_declare_all_valid_neighbors` helpers.

Required target data:

- `fury_target_score`: temporary score while evaluating candidates.
- `fury_best_target_score`: current best score for the scan.
- `fury_current_target`: existing country variable storing selected target id.
- `fury_target_preparation`: country variable raised by focus/decision preparation.
- `fury_failed_target_scans`: country variable for repeated no-target state.
- `fury_last_target_id`: country variable to avoid instant retarget churn after invalidation.

Required script constants:

- `fury_target_score.base_neighbor`
- `fury_target_score.one_state_bonus`
- `fury_target_score.weak_industry_bonus`
- `fury_target_score.target_at_war_bonus`
- `fury_target_score.faction_penalty`
- `fury_target_score.terrain_supply_penalty`
- `fury_target_score.player_link_blocker`
- `fury_target_score.overextension_penalty`
- `fury_target_score.momentum_bonus`
- `fury_target_score.evolution_i_bonus`
- `fury_target_score.evolution_iii_multi_target_gate`
- `fury_target_score.minimum_score`

Target scoring rules:

- Always exclude player countries, player subjects, player faction members, Fury actors, subjects, allies, and countries already at war with Fury through normal loop.
- Prefer one-state and low-industry AI minors.
- Penalize faction-backed targets, bad supply approach, rough terrain, target military strength, and high Fury overextension.
- Use `fury_momentum` and evolution state to widen the target set gradually.
- Evolution III all-neighbor declarations must still run each target through the score gate.
- Do not let ordinary target selection attack a local major unless Fury has reached major threshold or terminal state.
- Keep player-linked targeting relaxed only for terminal Phase 4 and only after warnings.

Decision and focus integration:

- `fury_first_target_files`, `fury_weak_neighbor_doctrine`, and `fury_capital_first_plans` should improve scoring or preparation, not bypass safety.
- `fury_select_new_target` should call the scored helper and only declare if a valid target was saved.
- `fury_survey_beyond_the_border` should increase reach and retry scoring, not erase the no-neighbor condition without consequence.

Acceptance for this phase:

- Fury target choice is deterministic enough to audit through variables and dynamic scoring.
- A strong protected neighbor is not selected just because it borders Fury.
- All-neighbor declarations filter every target individually.
- The player and player-linked countries cannot become Fury actors, but they can be selected as Fury targets when the normal target rules allow it.
- No stale `fury_current_target` survives target death, subject changes, faction changes, or Fury cleanup.

### Phase 3: Deepen occupation, settlement, and overextension gameplay

Current status: occupation pressure, garrison capacity, register work, rail registry work, crisis mission, and two coring methods are implemented.

Turn occupation into a pressure system around state groups, compliance work, garrison capacity, and administrative method.

Required values and flags:

- Existing: `fury_overextension`, `fury_compliance_drive`, state flag `fury_settlement_registered`, global `fury_coring_completed`.
- Add `fury_occupation_pressure`: country variable for active non-core strain.
- Add `fury_garrison_capacity`: country variable affected by focuses, missions, manpower, and support equipment.
- Add `fury_registered_state_count`: country or temp variable for current settlement workload.
- Add state flags `fury_settlement_admin_path`, `fury_settlement_march_path`, `fury_integration_failed_recently`, `fury_rail_registry_complete`.
- Add country flags `fury_admin_coring_unlocked`, `fury_march_coring_unlocked`, `fury_occupation_crisis_active`.

Required constants:

- `fury_occupation.overextension_per_conquered_state`
- `fury_occupation.overextension_per_active_war`
- `fury_occupation.overextension_high_gate`
- `fury_occupation.overextension_extreme_gate`
- `fury_occupation.compliance_admin_gate`
- `fury_occupation.compliance_march_gate`
- `fury_occupation.garrison_capacity_per_unit`
- `fury_occupation.resistance_failure_pressure`
- `fury_occupation.rail_registry_bonus`
- `fury_occupation.core_overextension_reduction`

Decision and mission families to add:

| Family | Owner | Decisions or missions | Result |
| --- | --- | --- | --- |
| Registry work | Fury | `Count the Captured Registers`, `Rail and Registry Survey` | raises compliance drive, marks rail/supply readiness |
| Garrison work | Fury | `Garrison the Names` mission | requires control/supply in registered states; success lowers pressure, failure raises resistance and overextension |
| Admin coring | Fury | `Core by Administration` | higher compliance gate, lower risk, larger overextension reduction |
| March coring | Fury | `Core by March` | lower compliance gate, higher equipment/manpower/stability/resistance cost |
| Occupation crisis | Fury | `Restore the Registers` mission when pressure is extreme | pauses new target selection until resolved or creates stall report |

Weekly loop integration:

- Weekly tick should recalculate or update occupation pressure from non-core controlled states, active wars, supply problems, and registered states.
- High overextension should weaken weekly unit quality, slow target selection, and push AI into occupation focuses.
- Extreme overextension should block ordinary target selection unless Evolution III or terminal state explicitly overrides it with extra penalties.
- Coring and compliance should reduce overextension and pressure, not just add cores.

Acceptance for this phase:

- Settlement is no longer a one-click state marker plus core button.
- Coring has two methods with different gates and costs.
- Overextension affects target selection, weekly units, focus AI, and mission availability.
- Fury can stall or fail through occupation pressure without requiring a hidden rollback.
- State flags are cleaned when Fury actor cleanup runs, when state is cored, or when ownership/control becomes invalid.

### Phase 4: Implement the terminal World in Fury branch

Current status: the focus calls `fury_try_start_world_end`, which checks terminal eligibility, counts safe seed candidates, starts the terminal branch when enough safe AI minors remain, or reports `fury_world_end_seed_blocked` when seeding cannot be done safely. The branch sets world-end/world-threat flags, creates `The World in Fury` faction, seeds other continents first, warns players, fires slot `60`, adds terminal reserve decisions, keeps post-grace player-linked targeting behind the terminal-only `fury_terminal_can_threaten_player_linked_country` helper, and reports terminal defeat through `chaosx.nr7.53`.

Implement terminal escalation as a separate branch from the triggerable scenario. Keep the scenario `The World in Fury` as manual setup; the world-end branch is a campaign state.

Required eligibility trigger:

Create a scripted trigger such as `can_start_fury_world_end = yes` that requires:

- `NOT = { has_global_flag = world_end }`
- chaos meter above the world-end threshold through the existing Chaos Redux world-end gate
- at least one active Fury actor
- the scoped actor has `fury_world_end_candidate`
- actor is major, controls at least `constant:fury_balance.world_end_actor_state_threshold` states, or has no valid continental AI neighbors
- overextension below `constant:fury_occupation.overextension_extreme_gate` or a completed world-end preparation focus that pays the cost
- enough safe AI candidates on other continents or a documented blocked outcome that delays terminal branch rather than selecting unsafe countries

Required opening effect:

Create `start_fury_world_end = yes` or equivalent. It must:

1. set `world_end`
2. set `fury_world_end_active`
3. set `world_threat_source_fury`
4. refresh the shared `world_in_threat` state through the shared framework
5. save the main Fury actor as a global event target such as `fury_world_end_leader`
6. create or strengthen the Fury faction under the main actor
7. seed Fury actors in other continents
8. make seeded actors join the main Fury faction
9. apply Evolution III or terminal package to all terminal Fury actors
10. set `super_event_visible` for the World in Fury slot and a unique audio id
11. fire player-facing warning events before any player-linked targeting gate is relaxed

Continental seeding design:

- First pass: select at most one safe candidate per continent or macro-region where no Fury actor exists.
- Second pass: add extra actors only if the required terminal pressure count is not met and safe candidates remain.
- Store `fury_world_end_seed_count` globally.
- Set `fury_world_end_seeded_actor` on seeded actors.
- Do not select the player, player subject, player faction, special chaos countries, non-standard countries, or majors unless the terminal design is explicitly extended later.
- If too few candidates exist, do not silently pick bad candidates. Set `fury_world_end_seed_blocked` and create a report/plan follow-up.

Faction rules:

- Reuse or create `The Fury Pact` only for Fury actors.
- Player cannot join through Fury logic.
- Fury actors receive `fury_pact_member` and `fury_world_end_actor`.
- Cooperation decisions become terminal shared-reserve decisions.
- Rivalry decisions are disabled inside the terminal pact unless the hostile terminal route is explicitly implemented.

Player warnings and targeting:

- Before player-linked targeting relaxes, fire warning report events to player countries bordering Fury, guaranteeing a Fury target, controlling strategic route states, or being near a terminal Fury actor.
- Add a delay variable or timed flag such as `fury_player_warning_grace_active`.
- During grace, ordinary player-link exclusions remain hard blockers.
- After grace, terminal targeting can threaten the player only through a separate terminal helper, never through ordinary `fury_is_valid_target`.

World-end super-event:

- Use a distinct super-event slot or formally extend slot `59` if the repo convention requires one Fury slot. Do not reuse the major-Fury title/image/audio for the terminal branch.
- Required keys: title, description, button, quote.
- Required image: final or placeholder explicitly documented as placeholder.
- Required audio: unique verified final track before the branch can be called complete. If no final audio exists, keep the branch incomplete and report blocker.

Defeat and cleanup:

- When all Fury actors are defeated during terminal branch, set `fury_world_end_defeated`, clear `world_threat_source_fury`, refresh `world_in_threat`, close terminal decisions, and optionally fire defeat aftermath only if Fury held enough states or lasted long enough.
- Do not clear `world_end` unless shared Chaos Redux world-end rules allow it.

Acceptance for this phase:

- World-end branch is not a focus flag only.
- The branch sets `world_end`, `fury_world_end_active`, `world_threat_source_fury`, and super-event visibility.
- Other continents receive valid seeded Fury actors or the branch blocks visibly with a documented reason.
- Fury faction membership is Fury-only.
- Player warning and grace exist before terminal player threat.
- Triggerable scenario and terminal world-end branch remain separate.

### Phase 5: Replace the anti-Fury button with a mission layer

Current status: anti-Fury response is a staged decision and mission layer with Border Watch, Emergency Aid, Firebreak Staff Talks, Supply Denial, and Recognition Denial.

Keep `anti_fury_response_category`, but turn it into a staged response surface that appears only after `fury_major_super_event_fired` or `fury_world_end_active`.

Required non-Fury systems:

| System | Type | Who sees it | Requirement | Success | Failure |
| --- | --- | --- | --- | --- | --- |
| Border Watch | timed mission | direct Fury neighbors | supplied divisions in border states, capital controlled | defense bonus, target deterrence, achievement path | Fury confidence rises |
| Emergency Aid to Target | decision plus mission | regional powers, majors, player near Fury | equipment, support equipment, convoys/trains, current Fury target exists | target receives aid, Fury momentum gain reduced if target survives | equipment partly lost, target morale/war support hit |
| Firebreak Staff Talks | decision | neighbors, regional powers, majors | CP, army XP, relations/faction compatibility | temporary anti-Fury planning idea, AI defense weight | no direct failure, cooldown and cost |
| Supply Denial | timed mission | countries bordering Fury or target | hold rail/supply hubs, commit divisions | Fury weekly unit quality reduced temporarily | overextension pressure on target rises |
| Recognition Denial | decision | majors/regional powers | PP as small diplomatic cost plus spy/convoy/relations gate | lowers `fury_pact_cohesion` or delays pact aid | Fury pact cohesion rises if ignored during terminal |

Required values:

- `anti_fury_border_watch_active`
- `anti_fury_border_watch_success`
- `anti_fury_aid_route_active`
- `anti_fury_staff_talks_active`
- `anti_fury_supply_denial_active`
- `global.anti_fury_response_pressure`
- `global.fury_target_aid_pressure`

AI behavior:

- Direct neighbors prioritize Border Watch if Fury borders them and Fury has momentum.
- Majors use Emergency Aid only if Fury is near their region, current target is not player-linked, and equipment reserve is healthy.
- AI should not use anti-Fury actions while Fury is weak, far away, or already collapsing.
- AI should avoid spending equipment into lost targets unless world-end is active.

Acceptance for this phase:

- `anti_fury_border_watch` becomes or starts a mission, not just an instant idea purchase.
- At least three anti-Fury response families exist after major-Fury threshold.
- Missions require real map action and meaningful costs.
- Achievement hooks read mission success, aid contribution, and containment contribution rather than only cleanup sweep proximity.
- Stale anti-Fury missions cancel when Fury threat ends.

### Phase 6: Make achievements depend on real systems

Current status: achievements are wired to Fury containment, anti-Fury mission contribution, scenario intensity/type, all-safe-candidate Maximum fallback, major-Fury, pact, no-neighbor, coring, Fury-on-Fury war declarations, factionless major containment, and world-end outcome flags. Completion audits cleared the remaining scenario-state and ordinary-selection blockers after the implementation patches.

Update achievement tracking after Phases 3 to 5 so achievements are earned through actual Fury systems.

Required tracking changes:

- `achievement_fury_firebreak_holds` should require Border Watch mission success, capital held, and Fury defeated or deterred.
- `achievement_fury_pact_breaker_path` should require at least two Fury pact members and defeat of pact leader or faction dissolution.
- `achievement_fury_ten_fires` supports the Maximum scenario if the current maximum actor count spawns or if `fury_triggerable_scenario_used_every_safe_candidate` records that every safe eligible candidate was used before the maximum count could be created.
- `achievement_fury_last_neighbor_path` should require Fury no-neighbor state before world-end begins, not merely cleanup after the no-neighbor flag was set.
- `achievement_fury_world_without_fury` should require terminal Phase 4: world-end super-event fired, at least three continent seeds or every safe continent attempted, world-threat source cleared, and all Fury actors defeated.
- `achievement_fury_rivals_burn` should require a recorded Fury-on-Fury war and defeat of both involved actors.
- `achievement_fury_major_without_faction_path` is recorded while a factionless player is at war with a major Fury actor, and the achievement also requires the player to be outside any faction at completion.
- `achievement_fury_no_cores_path` should require Fury first conquest plus no `fury_coring_completed` before final containment.

Acceptance for this phase:

- No achievement is satisfied only because a shallow placeholder flag happened to be set.
- Player-as-Fury disqualification remains present.
- Triggerable-scenario achievements read intensity and type from the confirmed scenario launch state.
- Achievement localisation, docs, and asset manifest reflect final conditions.

### Phase 7: Final assets, audio, and documentation alignment

Current status: Fury-specific report, news, idea, decision, key focus, achievement, major-super-event, and world-end super-event assets are wired. The major-Fury and World in Fury super-event audio tracks are sourced and documented.

This phase was not queued; final Fury-specific assets, audio, source notes, and registrations are implemented.

Asset families:

- report image for Fury start or War Office report: final DDS at `gfx/event_pictures/fury/fury_war_office.dds`
- news image for `chaosx.news.7007`: final DDS at `gfx/event_pictures/fury/fury_first_conquest.dds`
- major-Fury super-event image: generated final art is wired at `gfx/super_events/fury_becomes_a_state.dds`; source and processed PNGs live under `docs/assets/007_fury/super_events/fury_becomes_a_state/`.
- World in Fury terminal super-event image: generated final art is wired at `gfx/super_events/super_event_world_in_fury.dds`; source and processed PNGs live under `docs/assets/007_fury/super_events/world_in_fury/`.
- Fury decision category icon and decision icons: final DDS files under `gfx/interface/decisions/fury/`
- idea icons: final DDS files under `gfx/interface/ideas/fury/`
- key focus icon family for War Office, depots, target files, occupation registers, pact, rivalry, all borders, and world-end: final DDS files under `gfx/interface/goals/fury/`
- ten achievement triplets: final DDS files under `gfx/achievements/`
- optional faction emblem for Fury Pact
- optional generated institutional council portrait if the War Directorate leader route is implemented

Audio:

- major-Fury super-event audio is wired as ID `59` with `music/fury_becomes_a_state.ogg` and `sound/chaosx_super_event_fury_becomes_a_state.wav`; source and license are documented in `docs/super_events/super_event_audio_packages.md`.
- World in Fury terminal super-event audio is wired as ID `60` with `music/super_event_world_in_fury.ogg` and `sound/chaosx_super_event_world_in_fury.wav`; source and license are documented in `docs/super_events/super_event_audio_packages.md`.

Documentation and spreadsheet:

- Promote accepted route/focus/decision/world-end changes into `docs/specs/007_fury_specs/`.
- Update `docs/events/007_fury.md` with final mechanics, not implementation history.
- Update `docs/assets/007_fury/manifest.md` and `gfx_handoff.md` with final assets.
- Update triggerable scenario docs if scenario flags/achievement handling changes.
- Update the event catalog workbook after implementation facts are final.

Acceptance for this phase:

- No placeholder asset or audio is reported as final.
- Every in-game visible id added by phases 1 to 6 has localisation and icon coverage or registered placeholder with explicit handoff.
- Super-event quote/audio/image docs name sources, license status, final paths, and slot use.

## File surfaces affected by implementation

The main agent should expect to touch these surfaces if this addendum is accepted:

- `common/national_focus/007_fury_focus_tree.txt`
- `common/decisions/007_fury_decisions.txt`
- `common/decisions/categories/007_fury_categories.txt`
- `common/scripted_effects/007_fury_effects.txt`
- `common/scripted_triggers/007_fury_triggers.txt`
- `common/script_constants/007_fury_constants.txt`
- `common/ideas/007_fury_ideas.txt`
- `common/ai_strategy/` if route-level AI strategies are added outside focus/decision weights
- `events/007_random_expansion.txt` or the current Event 007 event file path in repo
- `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` if Fury world-threat refresh needs shared helper changes
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` if scenario challenge wording changes
- `common/scripted_guis/chaosx_scripted_gui_settings.txt` only if scenario UI state changes
- `interface/chaosx_super_events.gfx`
- `interface/chaosx_achievements.gfx`
- `interface/007_fury.gfx`
- `localisation/english/007_random_expansion_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/007_fury.md`
- `docs/specs/007_fury_specs/` promoted spec files
- `docs/assets/007_fury/manifest.md`
- `docs/assets/007_fury/gfx_handoff.md`
- `docs/super_events/` or equivalent Fury super-event research note
- `docs/systems/triggerable_scenarios.md` if scenario achievement/launch semantics change
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after final implementation

Do not add a whole-world `on_weekly`, `on_daily`, or `on_monthly` scan for these systems. Fury already has a self-scheduled actor loop; keep actor updates scoped to active Fury actors and explicit scenario/world-end setup effects.

## Validation and audit checklist

Before the main agent can claim Fury complete, run task-specific validation and audits:

- Focus route coverage table: each route family in Phase 1 maps to implemented focus ids, rewards, AI logic, and localisation.
- Decision/mission audit: every decision family in Phases 2, 3, and 5 has costs, visibility, availability, AI, cleanup, success/failure where relevant, and no duplicate passive missions.
- Target safety audit: actor selection excludes player/player-linked countries, target selection permits them only through normal target validity, and all-neighbor declarations still filter each target.
- World-end audit: terminal branch sets required flags, seeds other continents, creates/strengthens Fury faction, triggers super-event, warns player, and does not conflate with triggerable scenario.
- Overextension audit: high and extreme overextension influence weekly units, target selection, focus AI, occupation missions, and coring.
- Achievement audit: each achievement is tied to implemented systems, with player-as-Fury disqualification and scenario type/intensity checks intact.
- Localisation audit: new focus, decision, mission, idea, event, achievement, tooltip, cost, scenario, and super-event keys exist and avoid implementation-history phrasing.
- Asset audit: every placeholder is either replaced or explicitly reported as placeholder/blocker.
- Super-event audit: quote, audio, image, slot, scripted localisation, player localisation, docs, and spreadsheet align.
- Documentation/spreadsheet audit: `docs/events/007_fury.md`, accepted specs, asset manifest, super-event research note, scenario docs, and workbook agree with implementation.

Recommended scenario checks:

- One-state AI Fury wins first war, records news, then must choose between settlement/next target based on overextension.
- Fury with no valid local targets enters no-neighbor state but does not start world-end without eligibility.
- Evolution II pact creates cooperation route and blocks rivalry route.
- Evolution II hostile route permits Fury-on-Fury path only under intended conditions.
- Evolution III all-neighbor declaration filters invalid targets while allowing player-linked targets that satisfy normal target rules.
- Major-Fury threshold unlocks anti-Fury response missions.
- World-end branch seeds other continents and warns the player before terminal target relaxation.
- Maximum scenario creates ten actors when safe candidates exist and records actor count correctly.

## What to queue or reject if not in the next tranche

If the next implementation tranche is limited, prioritize Phases 1 to 5. The following may remain queued only with an explicit note in the completion report:

- Final asset replacement and final audio research can be queued if gameplay implementation is the tranche goal, but all placeholders must remain documented as placeholders.
- Optional terminal defeat aftermath super-event can be queued unless Fury world-end is implemented and already creates a long, costly global crisis.
- War Directorate leader replacement and generated institutional portrait can be queued if the focus tree avoids a visible leader-change route.
- A fully custom scripted GUI for Fury is not recommended for the next tranche. The decision/mission layer is enough unless later testing proves the values cannot be understood through category text, scripted localisation, and tooltips.
- Additional country-specific Fury variants should be rejected for now. Fury is a shared behavior for dynamic AI minors; country-specific routes would add bloat before the core loop is complete.
- A new global anti-Fury faction should be rejected unless the terminal world-end branch proves the limited staff-talks layer is insufficient. Use missions, aid, and world-threat integration first.

If any of Phases 1 to 5 are skipped, do not mark Event 007 complete. Report the skipped phase as an unresolved blocker and leave this plan open.

## Promotion note

Accepted portions are represented in the current implementation, event docs, and touched source specs. Keep this section as a map for future spec maintenance:

- Focus route changes into `docs/specs/007_fury_specs/specs/007_fury_focus_tree_spec.md`.
- Decision and mission changes into `docs/specs/007_fury_specs/specs/007_fury_decisions_missions_spec.md`.
- World-end and super-event changes into `docs/specs/007_fury_specs/specs/007_fury_spec_part_2_evolutions_world_end.md`.
- Achievement condition changes into `docs/specs/007_fury_specs/specs/007_fury_achievements_spec.md`.
- AI and balance tuning into `docs/specs/007_fury_specs/matrices/007_fury_ai_balance_matrix.md`.
- Final pass/fail criteria into `docs/specs/007_fury_specs/acceptance/007_fury_acceptance_criteria.md`.

This file remains under `docs/plans/007_fury_plans/` as the audit ledger for implemented Fury follow-up work and bounded caveats.
