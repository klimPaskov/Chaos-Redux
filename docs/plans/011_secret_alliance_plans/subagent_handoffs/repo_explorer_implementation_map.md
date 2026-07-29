# Event 011 Secret Alliance repository implementation map

## Disposition

Historical pre-implementation repository map. Its placeholder, provisional-file, and required-action statements describe the explorer's original freeze. Gameplay commit `407b9a05`, balance freeze `1c87d923`, `docs/events/011_secret_alliance/overview.md`, and the holistic `completion_audit.md` govern current behavior and status.

## Scope and authority

This is a read-only repository-exploration handoff for the main implementation agent. The explorer changed no gameplay, localisation, interface, asset, audio, spreadsheet, or binary file.

The accepted source of truth is the complete pack under `docs/specs/011_secret_alliance_specs/`, especially the five files under `specs/` and the six matrices under `matrices/`. Older design files under `docs/plans/011_secret_alliance_plans/` remain useful precedents, but their superseded assumptions must not override the source pack.

The implementation contract that matters most is:

- the player-controlled country at normal launch is the fixed target for the full event lifetime (`specs/011_secret_alliance_spec_part_1_core_and_hidden_pact.md:20-26`);
- normal launch needs exactly three valid minor founders, and fewer than three makes Event 011 unavailable with `N/A`, never an invalid substitute (`...part_1...:30-68`);
- the hidden pact is not a faction before reveal (`...part_1...:85-87`);
- Cohesion and Readiness are pact-side state; Evidence and Preparedness are target-side state, with the disclosure rules at `...part_1...:91-127`;
- Evolution I, II, and III use Gathering Storm, Rising Chaos, and Totalen Chaos respectively and must pace dynamically after their thresholds (`...part_2_progression_and_evolutions.md:123-250`);
- active membership bands are 4-6 minors at Evolution I, 6-9 with at most one major at Evolution II, and 8-12 with at most two majors at Evolution III (`...part_2...:80-91`);
- if any active pact member enters a normal hostile war with the target, reveal, faction formation, valid-member accession, and entry into the target war are one immediate transaction (`...part_4_reveal_war_and_scenario.md:11-15,82-93`);
- the public faction uses dynamic `Anti-[target adjective] Pact` localisation with a name-based fallback (`...part_4...:39`);
- the direct scenario, working label `Coalition Unmasked`, uses the selected player country, five composition types, four intensities, the existing scenario UI, the normal selection/reveal helpers, and immediate faction formation, super-event, and war (`...part_4...:208-249`);
- the final feature includes the six achievements in `matrices/011_secret_alliance_achievement_matrix.md:7-14`, all event-log/evolution/detail surfaces, the workbook, final assets, and the super-event package (`...part_5_ai_presentation_and_acceptance.md:139-175,227-243`).

There is explicitly **no Event 011 cluster registration**. Preserve single-event dispatch. Do not add Event 011 to `initialize_event_cluster_definitions`, `event_belongs_to_cluster`, `load_event_cluster_members`, `common/script_constants/event_cluster_constants.txt`, or `events/chaosx_event_clusters.txt`.

## Current repository state

### Tracked live state

Event 011 is still a placeholder in the tracked gameplay registry:

| Surface | Current state | Required action |
| --- | --- | --- |
| `common/scripted_effects/chaosx_logic_effects.txt:154-189` | Fire-once registry lists Event 011 as unavailable at line 158. | Replace the placeholder commentary/state only when the full launch path is atomic. |
| `common/scripted_triggers/chaosx_settings_triggers.txt:10-26` | Event 011 is already in the default-enabled allowlist at line 21. | Keep it enabled; availability must come from the candidate trigger, not a permanent disable. |
| `common/scripted_effects/chaosx_logic_effects.txt:488-531` | Active-pool construction hard-disables Event 011 at line 520. | Replace with `event id 11` plus the real three-founder availability trigger. |
| `common/scripted_effects/chaosx_settings_effects.txt:4539-4644` | The no-cluster dispatcher hard-blocks Event 011 at lines 4596-4599, although generic dynamic dispatch exists at 4615-4622 and fire-once bookkeeping at 4637-4639. | Prepare and revalidate the fixed target/founders before dispatch; do not consume the fire-once event on failed preparation. |
| `common/scripted_effects/chaosx_settings_effects.txt:4522-4536` | Generic dispatch checks cluster membership, then falls through to the no-cluster path. | Leave Event 011 unregistered so this fallback is used normally. |
| `common/scripted_effects/chaosx_events_log_effects.txt:2930-3116` | Event catalogue weight view has special `N/A` branches for other unavailable systems at 3063-3088, but none for Event 011. | Add Event 011 candidate unavailability as weight `-1`; do not show a normal numeric weight when fewer than three founders exist. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4202-4203` | Event 011 points to the unavailable-detail localisation. | Add spoiler-safe event detail and evolution routing. |
| `localisation/english/chaosx_event_names_l_english.yml:13` | `chaosx.event_name.11` is `Event 011 Unavailable`. | Replace with final player-facing naming; concealed/public variants need scripted routing where required. |
| `localisation/english/chaosx_gui_l_english.yml:495` | Event detail text says Event 011 is unavailable. | Replace and add event/evolution/scenario/detail keys. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:65-66` | Generic Event 011 name mapping already exists. | It can continue to resolve `chaosx.event_name.11`; add a dedicated dynamic name route if the public title must change after reveal. |
| `common/scripted_effects/chaosx_events_log_effects.txt:103-260` | Default actor mapping exists, with a global-target precedent for Fury at 141-148. | Snapshot the fixed target or chosen public leader as the actor according to the final log wording. |

No tracked `events/011_secret_alliance.txt`, `chaosx.nr11.*` event, Event 011 decisions, categories, ideas, on-actions, faction template, AI strategy, scripted GUI, event GUI/GFX, Event 011 localisation file, Event 011 achievements, scenario registration, event documentation, or workbook implementation was found.

### Concurrent Event 011 drafts

The following Event 011 scripts appeared as **untracked concurrent work** during exploration. They are not live, committed implementation and were not edited here:

- `common/script_constants/011_secret_alliance_constants.txt` — 388 lines; constants for event/evolutions, motives, doctrine, reveal routes, five scenario types, four scenario scales, meters, selection, missions, AI, super-event, and achievements.
- `common/scripted_effects/011_secret_alliance_effects.txt` — 427 lines; currently contains prefire selection, founder/major registration, doctrine, initialisation, abort, and cost refresh only. Despite the broad header, it does not yet contain the promised evolution runtime, operations, reveal transaction, faction/war, settlement, scenario, or achievements.
- `common/scripted_triggers/011_secret_alliance_triggers.txt` — 365 lines; candidate, phase, suspect, decision, war-end, and partial scenario/achievement gates.

These drafts provide useful identifiers, but require main-agent review before wiring:

1. `011_secret_alliance_effects.txt:99,103,107,198-203,208` uses hardcoded country-size, tension, motive-weight, and chance numbers despite the repository rule that tuning belongs in variables/constants.
2. `011_secret_alliance_effects.txt:351` passes a script constant directly to `country_event.days`. Duration fields must be checked against official parsing support; use a normal or temporary variable when the field rejects `constant:` tokens.
3. `011_secret_alliance_triggers.txt:33-39,96-102,121-127` accepts nonleader faction members, but no safe withdrawal transaction exists in the effect draft. A factioned exception is valid only when departure is safe and implemented; it is not a blanket substitute.
4. `011_secret_alliance_triggers.txt:148-165` uses `>` against constants named `*_min_pulses`; with integer pulses, this opens one pulse after an intuitive minimum. Confirm the intended threshold and use an explicit greater-than-or-equals comparison if equality must qualify.
5. `011_secret_alliance_triggers.txt:324-347` checks only a three-founder floor and whether a major exists for the sponsor type. It does not yet validate the requested type/intensity composition, member cap, major cap, or maximum-safe-candidate behavior.
6. `011_secret_alliance_constants.txt:90-101` includes 90/60/35/14 scenario preparation days, but the accepted scenario specification requires the reveal and war to begin immediately. These values need rejection or a narrowly documented non-delay use.
7. Hidden-member registration immediately adds `antagonize` and `prepare_for_war` strategies at `011_secret_alliance_effects.txt:221-240`. The final AI package must prevent obvious pre-reveal behavior, remove all temporary strategies on defection/invalidity/settlement, and add revealed-war front roles in a dedicated AI strategy surface.
8. Global targets and arrays are begun at `011_secret_alliance_effects.txt:20-39,221-370`, but terminal cleanup is not implemented yet. Every global event target, member/suspect array, country flag, AI strategy, modifier/idea, and scenario-origin flag needs a single idempotent cleanup contract.
9. The founder pool selects AI countries only (`011_secret_alliance_triggers.txt:18-40`). That safely avoids forced human recruitment, but the separate human invitation/consent route required for multiplayer still needs implementation if a human is ever invited later.

The tracked audio package is already present and documented in `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_audio_research.md`: public-domain U.S. Marine Band recording of William Paris Chambers's `Revelation`, proposed audio ID 43, with final WAV under `sound/011_secret_alliance/` and `sound/011_secret_alliance/`. Audio ID 43 remains independent of the visible super-event slot.

An untracked concurrent asset prompt pack is also present at `docs/assets/011_secret_alliance/prompts/generated_event_art_prompts.md`. It covers the seven report scenes, public-coalition news image, and reveal super-event image from the accepted asset register. Treat it as an asset-subagent draft until its handoff, generated sources, processing outputs, manifest, and final DDS wiring are complete.

An unrelated user/concurrent modification is present in `interface/013_natural_disasters.gui`. Do not touch, format, revert, stage, or include it in an Event 011 commit.

## Required implementation surfaces

### Event-owned files

Create or complete these files as the coherent Event 011 package:

| File | Ownership |
| --- | --- |
| `events/011_secret_alliance.txt` | Hidden `chaosx.nr11.1` entry; target-bound operation scheduler; invitations/consent; incident, evolution, reveal, settlement, and terminal events. Use delayed country events rather than a global daily/weekly iteration. |
| `common/script_constants/011_secret_alliance_constants.txt` | All shared tuning. Review the concurrent draft against the source pack before treating it as authoritative. |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | Target/founder/member safety, phase gates, reveal idempotence, scenario composition, decision/mission, achievement, and cleanup gates. |
| `common/scripted_effects/011_secret_alliance_effects.txt` | Weighted selection, membership/motives, meter updates, operations, evolutions, reveal transaction, faction/war, scenario, settlement, achievements, cleanup. |
| `common/on_actions/011_secret_alliance_on_actions.txt` | Two-sided `on_war_relation_added` reveal hook and narrow peace/capitulation cleanup hooks if required. No global periodic on-action. |
| `common/decisions/categories/011_secret_alliance_categories.txt` | Concealed Foreign Interference and public Coalition Crisis categories. |
| `common/decisions/011_secret_alliance_decisions.txt` | Investigation, protection, diplomacy, deception, emergency, and revealed-war decisions/missions from the accepted matrix. |
| `common/ideas/011_secret_alliance_ideas.txt` | Target pressure/preparedness and coalition opening/resolve modifiers. |
| `common/ai_strategy/011_secret_alliance.txt` | Concealed preparation, revealed front priorities, coalition coordination, settlement, and complete abort/cleanup logic. |
| `common/factions/templates/011_secret_alliance.txt` | Public coalition faction template created with `create_faction_from_template`. |
| `common/factions/rules/011_secret_alliance_rules.txt` and `common/factions/goals/011_secret_alliance_goals.txt` | Add only if the coalition needs meaningful public behavior not covered by an existing safe template. Do not create decorative rules/goals. |
| `common/scripted_guis/011_secret_alliance_scripted_gui.txt` | Counter-network visibility, Evidence/Preparedness meters, exactly three suspect cards, click/state/tooltip logic. |
| `interface/011_secret_alliance.gui` | Compact category-attached panel; no full intelligence-board window. |
| `interface/011_secret_alliance.gfx` | Event pictures, category/decision/idea/UI sprites, faction emblem, and genuine eight-frame warning animation plus static fallback. |
| `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` | Suspect confidence, broad hidden-state bands, dynamic faction name, phase-aware tooltips, and spoiler-safe actor/member text. |
| `localisation/english/011_secret_alliance_l_english.yml` | All Event 011 gameplay/UI/event/faction/AI-facing strings, UTF-8 BOM, no `:0`. |
| `docs/events/011_secret_alliance/overview.md` | Mechanic walkthrough, interactions, variable/state contract, complete icon/sprite/path list, scenario and achievement coverage, future plans. |

### Shared integration files

| System | Exact integration files and insertion surfaces |
| --- | --- |
| Fire-once and normal dispatch | `common/scripted_effects/chaosx_logic_effects.txt:154-189,488-531`; `common/scripted_effects/chaosx_settings_effects.txt:4522-4644`; existing allowlist `common/scripted_triggers/chaosx_settings_triggers.txt:10-26`. |
| Event catalogue/log/details | `common/scripted_effects/chaosx_events_log_effects.txt:103-260,2930-3116`; all Event 011 event/evolution mappings in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`; `localisation/english/chaosx_event_names_l_english.yml:13`; `localisation/english/chaosx_gui_l_english.yml:495`. |
| Direct scenario | Allocate next stable scenario ID **9** in `common/script_constants/chaosx_triggerable_scenarios_constants.txt:9-35`; add defaults, registry, all four name/id ordering rebuild branches, five-type previous/next cycling, and launch dispatch in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:9-50,54-403,543-749`; add exact launch eligibility in `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt:16-82`; add selected name, entry name/id, description, type, and warning branches in `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:1-146,175-354,382-551,554+`; add localisation keys in `localisation/english/chaosx_gui_l_english.yml:175-177,183+`. The generic list/confirmation GUI already exists at `common/scripted_guis/chaosx_scripted_gui_settings.txt:2709-2869`. |
| Reveal super-event | Allocate visible slot **73**, because the tracked visible catalogue ends at 72. Add slot 73 to all four `defined_text` mappings in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` (current insertion ends include 407, 633, 859, and 1085-1242); add image sprite to `interface/chaosx_super_events.gfx`; add final title/body/quote/button localisation; wire audio 43 through `sound/chaosx_sound.asset`, `sound/chaosx_sound.asset`, and the settings-aware helpers at `common/scripted_effects/chaosx_settings_effects.txt:4646-4715`; update `docs/super_events/`. Do not reuse visible slot 11: it belongs to Holy Realm Divine Sovereignty. |
| Achievements | Add the six exact IDs from `matrices/011_secret_alliance_achievement_matrix.md:7-14` to `common/achievements/chaos_redux_achievements.txt`; add completed/grey/not-eligible triplets to `interface/chaosx_achievements.gfx`; add final localisation to `localisation/english/chaosx_achievements_l_english.yml`; add all 18 final DDS files under `gfx/achievements/`. Snapshot valid membership immediately before reveal, record major-at-reveal status, and use an immutable Maximum-scenario origin/intensity flag. |
| Workbook | Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` only after gameplay identifiers and final localisation are stable. Event detail, evolution detail, scenario detail, and achievement wording must match in-game localisation. Coordinate ownership because the workbook may be touched by other event work. |

### Asset obligations

The stable proposed paths and sprite names are enumerated in `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_asset_register.md`. At minimum the final implementation needs:

- seven 210x176 report images (`:15-27`);
- one 397x153 black-and-white news image and one 457x328 super-event image (`:29-34`);
- two decision-category icons, one panel, two meter frames, two meter fills, one suspect-card state asset, and four status/warning icons (`:38-53`);
- one eight-real-frame coalition-closure animation, static fallback, source frames, sheet, preview, contact sheet, manifest, and `.gfx`/`.gui` handoff (`:55-78`);
- seventeen separate 32x32 decision-icon compositions (`:80-102`);
- seven 64x64 idea icons (`:104-116`);
- one procedural faction emblem (`:118-122`);
- six achievement families with three final DDS states each (`:126-135`).

Final DDS files must live in the listed game folders, not only under `docs/assets/011_secret_alliance/`. Asset production must use the event-assets skill; the warning loop additionally requires the frame-animation skill and cannot be produced by transforming one still.

## Engine and project precedents

Use these live structures rather than inventing parallel systems:

1. **Weighted country selection:** `common/scripted_effects/007_fury_effects.txt:145-198` clamps a computed score, duplicates a country into a temporary ticket array, and selects with `random_scope_in_array`; candidate validity is in `common/scripted_triggers/007_fury_triggers.txt:22-38`. Event 011 must also exclude already-selected founders and prefer factionless states strongly.
2. **Evolution settings and logging:** `common/scripted_effects/007_fury_effects.txt:32-80` uses `is_current_evolution_enabled`; `:1221-1277` snapshots actor, event/type/stage/tier, then calls `record_events_log_evolution_entry`. Event 011 should record an evolution only when the paced transition actually applies.
3. **Target-bound scheduling:** `events/007_fury.txt:23-35,74-90` prepares and self-reschedules a country event; `events/010_death.txt:7-25` is a compact hidden launcher. This avoids forbidden world-wide periodic on-actions.
4. **War reveal:** `common/on_actions/010_death_on_actions.txt:34-50` checks both ROOT/FROM directions. Vanilla `common/on_actions/05_lar_on_actions.txt:432-479` confirms `on_war_relation_added` gives ROOT attacker and FROM defender. Set `secret_alliance_reveal_in_progress` before adding any member to the war, because each `add_to_war` can retrigger the on-action.
5. **Immediate war accession:** vanilla `events/LaR_Spain.txt:9148-9185`, especially `:9177-9181`, uses `add_to_war` with `targeted_alliance`, `enemy`, and `hostility_reason`. The hostile-war reveal may not use delayed-member entry.
6. **Faction creation:** vanilla `common/decisions/BALTIC.txt:32-53` uses `create_faction_from_template` and loops countries into the faction. Chaos Redux `common/scripted_effects/003_holy_realm_effects.txt:1347-1371` safely leaves a faction, creates from template, saves its leader target, and refreshes state. Do not copy Fury's deprecated `create_faction` calls at `007_fury_effects.txt:1361-1363,2320-2334`.
7. **Faction definitions:** `common/factions/templates/holy_realm_mandala_of_nations.txt:6-28`, `common/factions/rules/holy_realm_rules.txt:11-111`, and `common/factions/goals/holy_realm_goals.txt:12-151` show local file structure.
8. **AI strategy:** `common/ai_strategy/003_holy_realm.txt:5-21,227-245` shows allowed/enable/abort and emergency response. Vanilla `common/ai_strategy/ENG.txt:489-520,1271-1288,1771-1781` covers alliance/protect, front control, and allied-border defense.
9. **Timed missions:** `common/decisions/007_fury_decisions.txt:394-450,478-498,547-575` shows decision-to-mission activation, timeout, cancellation, and outcomes. Vanilla `common/decisions/AST.txt:44-105,3424-3485` provides further mission structure.
10. **Country/state target decisions:** `common/decisions/japan_chemical_campaign_decisions.txt:36-84` shows a dynamic target decision and FROM state scope.
11. **Three suspect cards:** use the fixed-card click/index pattern in `common/scripted_guis/013_natural_disasters_scripted_gui.txt:42-59` and `interface/013_natural_disasters.gui:46-103`, but create Event 011-owned files and do not edit the dirty Event 013 GUI.
12. **Animation registration:** `interface/013_natural_disasters.gfx:5-17` shows a static sprite plus a genuine eight-frame sprite.
13. **Achievements:** `common/achievements/chaos_redux_achievements.txt:625-703` contains Fury and Maximum-scenario precedents; `interface/chaosx_achievements.gfx:950-1067` shows the three-state sprite pattern; `localisation/english/chaosx_achievements_l_english.yml:290-319` shows localisation structure.
14. **Super-event launch:** `common/scripted_effects/007_fury_effects.txt:1281-1295` sets visible/audio IDs and calls the settings-aware playback helper. Shared playback derives the track/sound key from `global.current_super_event_audio_id` at `common/scripted_effects/chaosx_settings_effects.txt:4646-4715`.

Official documentation consulted alongside the offline wiki confirms: regular event targets survive into events fired in the same effect chain but auto-clear; global event targets persist and must be cleared; `create_faction` is deprecated in favor of `create_faction_from_template`; `on_war_relation_added` fires whenever a new country pair becomes at war; `add_to_war` supports targeted alliance; missions use `days_mission_timeout`, `activation`, `cancel_trigger/effect`, and `timeout_effect`; scenario/faction AI should use the documented strategy types rather than bespoke numeric flags.

## Transaction and lifecycle design

The following order avoids the highest-risk scope and recursion failures:

1. **Availability check:** in player scope, validate the fixed target and count at least three safe AI minor founders. Event catalogue uses the same trigger for `N/A`.
2. **Prefire selection:** save the target globally, build the weighted ticket pool, select three distinct founders, assign motives, and validate the final set. Do not consume Event 011 from the fire-once pool if validation fails.
3. **Entry event:** `chaosx.nr11.1` commits the context, starts baseline state and a target-bound operation pulse, records the normal event log entry, and exposes no forbidden member identities.
4. **Concealed runtime:** use the target's delayed event loop for operation pulses, recruitment, invalid-member pruning, and paced evolution eligibility. Human invitations must be asynchronous with explicit join/refuse/leak/expose choices.
5. **Evolution application:** compute eligibility from current settings and state, apply after a real delay/pulse, then record the evolution log and UI/state changes. Pre-fire Evolution III starts at the major-led Evolution II package and approaches the public threshold; it must not begin as instant unexplained war.
6. **Reveal transaction:** set an in-progress guard; prune invalid members; snapshot membership, major status, target starting capital, known members, Evidence, and Preparedness; choose leader by designated major, strongest major, strongest founder, then hostile trigger; safely withdraw allowable factioned members; create faction from template; add every valid member; apply dynamic faction name; convert meters into wartime state; synchronously add every valid member to the target war for the hostile-war route; fire news/super-event; mark revealed; clear the in-progress guard.
7. **Revealed runtime:** use resolve, motive, and turned-channel state for delayed/refused entry only on non-hard reveal routes, wartime fracture, separate terms, AI front roles, and settlement.
8. **Terminal cleanup:** remove all event ideas/modifiers/AI strategies, cancel missions, clear arrays and global event targets, clear transient flags/variables, preserve only required achievement/history snapshots, close UI/categories, and mark terminal. The cleanup effect must be safe to call more than once.

Leader selection must occur before faction creation. Tag switching must never retarget the conspiracy. A target that ceases to exist or becomes invalid must enter the defined terminal closure, not silently move the event to the new human tag.

## Recommended implementation dependency order

1. Review and finalize the concurrent constants/triggers/effects identifiers against the source spec; resolve the scenario-delay and factioned-founder issues first.
2. Implement fixed-target prefire selection, normal dispatch integration, `.1` entry, operation scheduler, and complete cleanup. Verify the unavailable/`N/A` path without consuming the fire-once event.
3. Implement baseline operations, motives, member pruning/recruitment, Cohesion/Readiness/Evidence/Preparedness updates, and spoiler-safe log/detail localisation.
4. Implement the three paced evolutions with membership/major caps and evolution log entries.
5. Implement response categories, decisions/missions, compact scripted GUI, ideas, dynamic costs, AI use, and exact trigger/effect tooltips.
6. Implement the idempotent reveal/faction/war transaction, faction template/rules, dynamic name, public news, super-event slot 73/audio 43, revealed AI, resolve, fracture, settlement, and cleanup.
7. Register direct scenario ID 9 across all existing scenario registry/sort/localisation/eligibility/launch surfaces; reuse normal selection and reveal helpers, but launch faction/super-event/war immediately and record immutable origin/intensity.
8. Add the six achievements and their exact snapshots/disqualifiers.
9. Produce/wire all visual assets and the genuine frame animation; update Event 011 and super-event documentation.
10. Run specialised event, decisions/missions, localisation, and asset audits; only then align the workbook wording and commit the complete plan without unrelated Event 013 changes.

## Known conflicts and decisions still requiring closure

1. `docs/plans/011_secret_alliance_plans/011_secret_alliance_scripted_system_architecture.md:3-9,348` and `011_secret_alliance_improvement_addendum.md:19,805-806` predate the accepted source pack. Their prohibition on a manual scenario is superseded by `...part_4_reveal_war_and_scenario.md:208-249`. Their no-cluster conclusion remains correct.
2. `docs/plans/011_secret_alliance_plans/011_secret_alliance_decision_mission_handoff.md:879` says no source spec existed. That statement is stale; follow the complete source pack.
3. The older text research in `docs/plans/011_secret_alliance_plans/011_secret_alliance_super_event_text_research.md:123-145,230` chooses Luke 8:17 and `In battalions`. The newer source research in `docs/specs/011_secret_alliance_specs/research/011_secret_alliance_super_event_text_research.md:25-29,83-85,113-117` chooses Sun Tzu's `All warfare is based on deception` and `Look about you.` Final super-event text remains gated in the source README and needs one explicit selection through the super-event workflow.
4. The concurrent constants choose visible super-event slot 73 and audio ID 43 (`common/script_constants/011_secret_alliance_constants.txt:367-375`). Those allocations are collision-free in the current catalogue, but only audio 43 is already backed by a delivered package.

## Completion/audit gates

Do not claim Event 011 complete until all of the following are evidenced:

- normal dispatch, `N/A`, failed-prefire, tag-switch, target-invalidity, and no-cluster paths are aligned;
- three distinct valid founders are selected, factioned exceptions can actually withdraw safely, and humans cannot be recruited without consent;
- all baseline and Evolution I-III content, operation families, decisions/missions, AI behavior, and disclosure rules exist;
- hard hostile-war reveal creates the public faction and places every remaining valid member into the same target war immediately, without recursion or duplicate super-events;
- other reveal routes, resolve/fracture/settlement, terminal cleanup, and postwar faction behavior are complete;
- scenario ID 9 supports five types and four intensities, blocks impossible composition, uses the maximum safe pool without invalid substitutes, and starts the coalition war immediately;
- super-event display 73/audio 43, news, dynamic faction name, event/evolution logs, event details, and all final localisation are wired;
- all asset-register entries, six achievement triplets, exact achievement tracking/disqualifiers, Event 011 docs, super-event docs, and workbook rows are final;
- the appropriate event-completion, decision/mission, localisation, and asset audits have reviewed the result.

## Blockers and simplifications

There is no repository-discovery blocker. Two design choices still require explicit closure during implementation: the final super-event quotation/button pairing, and whether the concurrent scenario preparation-day constants are deleted or repurposed without delaying the mandated immediate war.

No cluster registration is required or permitted. No implementation fallback or invalid-country substitution was identified as acceptable. This exploration made no simplification to the accepted scope.
