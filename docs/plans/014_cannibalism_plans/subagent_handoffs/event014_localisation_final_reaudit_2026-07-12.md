# Event 014 Final Localisation and Secrecy Reaudit

## Verdict

**Completion-ready from the localisation, scripted-localisation, terminology, and secrecy scope.**

The live Event 014 implementation has no remaining P0, P1, P2, or P3 localisation findings. Pre-reveal text does not expose Hannibal Lecter, the Wendigo merge, the final portrait, or terminal-route wording. Post-reveal public text consistently identifies the leader as **Hannibal Lecter** without an ancient-general disclaimer. Event Details terminal rows and the staged achievement tracker use the required public-state gates.

This was a read-only audit. The only file written by this auditor is `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_localisation_final_reaudit_2026-07-12.md`.

## Findings by Priority

### P0

None.

### P1

None.

### P2

None.

### P3

None.

## Required Reference Basis

Repository guidance and skills read in full:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Offline Paradox wiki references consulted:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`

Vanilla documentation and precedents consulted:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_objects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_formatter_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`

No online Paradox wiki page was used.

## Audited Localisation Surfaces

Primary Event 014 text:

- `localisation/english/014_cannibalism_l_english.yml`
- `localisation/english/014_cannibalism_objectives_l_english.yml`
- `localisation/english/014_cannibalism_super_events_l_english.yml`
- `localisation/english/zz_014_cannibalism_focus_closure_l_english.yml`

Shared visible surfaces:

- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- `localisation/english/chaosx_characters_l_english.yml`

Scripted-localisation and caller surfaces:

- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`
- `common/scripted_localisation/014_cannibalism_achievement_tracker_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`
- `interface/014_cannibalism_frontline_hunger.gui`

Gameplay identifiers checked against localisation included every Event 014 event, decision, decision category, mission, national focus, idea, dynamic modifier, opinion modifier, leader trait, country name, character name, achievement, tracker entry, objective, and terminal-row selector in the live files.

## Structural and Reference Evidence

- All 137 files under `localisation/english/` retain UTF-8 BOM encoding.
- No localisation file under `localisation/english/` uses `:0`.
- Event 014 has zero cross-file duplicate localisation keys. The unrelated repository duplicate groups do not include Event 014 or its affected shared keys.
- `localisation/english/014_cannibalism_l_english.yml`, `localisation/english/014_cannibalism_objectives_l_english.yml`, `localisation/english/014_cannibalism_super_events_l_english.yml`, and `localisation/english/zz_014_cannibalism_focus_closure_l_english.yml` contain zero malformed non-comment localisation rows.
- The inspected Event 014 and shared caller set contains 1,139 explicit localisation references and zero missing keys.
- The visible Event 014 text contains 260 distinct `constant:category.key` references and zero missing script-constant entries.
- `interface/014_cannibalism_frontline_hunger.gui` contains 64 localisation references and zero missing keys.
- Event 014 visible text calls 33 `GetCannibalism...` scripted-localisation selectors and all 33 are defined.
- `common/scripted_localisation/` contains zero duplicate `defined_text` names and no literal `§` or `£` formatting characters in the audited Event 014 scripted-localisation files.
- The three Event 014 focus trees expose 208 focus identifiers; every focus has its title and description.
- The Event 014 decision files expose 129 decision or mission identifiers and 13 category identifiers; every identifier has its title and description.
- The Event 014 idea, trait, modifier, and opinion surfaces expose 39 ideas, 30 traits, 50 dynamic modifiers, and one opinion modifier; every required localisation key exists.
- `common/achievements/chaos_redux_achievements.txt` contains 18 Event 014 achievements; all 18 have `_NAME`, `_DESC`, and matching tooltip localisation in `localisation/english/chaosx_achievements_l_english.yml`.
- `common/scripted_localisation/014_cannibalism_achievement_tracker_scripted_localisation.txt` calls 18 completion triggers; all 18 exist in `common/scripted_triggers/014_cannibalism_achievement_triggers.txt`.

## Secrecy Evidence

### Pre-reveal wording

- `localisation/english/014_cannibalism_l_english.yml:138` uses the pre-reveal Event Details description and names only the military breakdown, evidence, concealment, containment, and terror choices.
- `localisation/english/014_cannibalism_l_english.yml:141` now states only that achievement objectives justified by the current public record are shown.
- `localisation/english/014_cannibalism_l_english.yml:184` says no shared headquarters appears in the records.
- `localisation/english/014_cannibalism_l_english.yml:186` says captured records identify no common headquarters.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4407` selects the pre-reveal Event Details description while `cannibalism_reveal_complete` is absent.
- `common/scripted_effects/chaosx_events_log_effects.txt:1960` inserts Event 014 Evolution III into the Event Details preview only after `cannibalism_reveal_complete`.
- The Evolution III title and body selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` require `cannibalism_reveal_complete` at every history, row, selected-title, and selected-body surface.

No pre-reveal visible string names Hannibal Lecter, Wendigo, a hidden master, a supreme leader, a unifier, the final portrait, or either terminal ending.

### Public reveal and portrait-facing identity

- `localisation/english/014_cannibalism_l_english.yml:359` defines `CBL_hannibal_name` as `Hannibal Lecter`.
- `localisation/english/014_cannibalism_l_english.yml:360` defines `ZZZ_hannibal_wendigo_name` as `Hannibal Lecter`.
- `common/scripted_effects/014_cannibalism_unification_effects.txt:491` sets `cannibalism_reveal_complete` before CBL, its leader, portrait, country package, focus tree, or public threat can be exposed.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:440` sets `cannibalism_reveal_complete` before the transformed cosmetic identity, character, portrait, focus overlay, decisions, report event, news event, or audio-facing super event is applied.
- `common/scripted_effects/zombie_special_project_effects.txt:2633` restores the Hannibal Wendigo name and portrait only when both `cannibalism_reveal_complete` and `cannibalism_wendigo_hannibal_country` are present.
- `common/scripted_guis/014_cannibalism_scripted_gui.txt:210` requires `cannibalism_reveal_complete` for Hannibal's ordinary revealed-command panel.
- `common/scripted_guis/014_cannibalism_scripted_gui.txt:239` requires `cannibalism_reveal_complete`, the Wendigo route, and the Hannibal-Wendigo country identity for the transformed panel.
- `common/national_focus/014_cannibalism_wendigo_focus.txt:18` and `common/national_focus/014_cannibalism_wendigo_focus.txt:46` gate the Wendigo focus overlay behind the revealed transformed country.

Post-reveal event, news, super-event, achievement, country, leader, world-tension, focus, idea, and GUI text consistently uses Hannibal Lecter or a clear subsequent reference to Lecter/Hannibal. No ancient-general disclaimer appears.

## Achievement Tracker Evidence

`common/decisions/014_cannibalism_achievement_tracker_decisions.txt` exposes the 18 read-only tracker entries at these public stages:

- Entries 01-05: Event 014 system start; all five titles and tooltips are non-spoilery.
- Entry 06: `achievement_cannibalism_exploitation_visibility_open`.
- Entry 07: `achievement_cannibalism_island_host_visibility_open`.
- Entry 18: `achievement_cannibalism_evolution_ii_visibility_open`.
- Entry 12: `achievement_cannibalism_convergence_visibility_open`; its title is `Break the Empty Frame` and its text names only the likely convergence host and command consolidation.
- Entries 08-11, 13, and 15: `cannibalism_reveal_complete`.
- Entries 14 and 16: `achievement_cannibalism_wendigo_merge_occurred`.
- Entry 17: `cannibalism_global_defeat_aftermath_eligible`.

`common/scripted_effects/014_cannibalism_achievement_effects.txt` clears every staged visibility flag during initialization and opens each early stage only when its matching public gameplay state occurs. `common/scripted_effects/014_cannibalism_wendigo_effects.txt:440` sets the reveal flag before `achievement_cannibalism_wendigo_merge_occurred`.

The real registry in `common/achievements/chaos_redux_achievements.txt:2061` leaves entries 01-05 public and entries 06-18 statically hidden, while the dedicated tracker supplies the required staged public surface without changing achievement completion logic.

## Event Details Terminal-Row Evidence

- `localisation/english/chaosx_gui_l_english.yml:516` defines `The World Is the Larder` and its details.
- `localisation/english/chaosx_gui_l_english.yml:518` defines `No Thaw Will Come` and its details.
- `common/scripted_effects/chaosx_events_log_effects.txt:999` excludes both Event 014 terminal rows from the rebuilt Event Details array until `cannibalism_reveal_complete`.
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt:1365` suppresses the empty terminal-row state for Event 014 before the reveal, avoiding an indirect hint that hidden endings exist.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9473` maps each live row to its exact title.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9533` maps each selected row to its exact details text.
- `common/scripted_effects/chaosx_events_log_effects.txt:921` evaluates `cannibalism_world_end_ordinary` and `cannibalism_world_end_wendigo` independently, so each row reports its own active state.

Both terminal rows are absent before reveal and available as separate rows after reveal, with separate titles, details, toggle state, availability state, and active-state evaluation.

## Objective and Focus-Closure Evidence

- `localisation/english/014_cannibalism_objectives_l_english.yml` contains no implementation-facing tag, generation, lifecycle, runtime, or fallback wording.
- The island, convergence, and transformation missions describe continuity through the same living command or recorded Host without exposing engine identity bookkeeping.
- `localisation/english/zz_014_cannibalism_focus_closure_l_english.yml` describes terminal hunts, defender counterpressure, enemy-loss receipts, inherited cells, Pack progression, inherited formations, and commander progression with live constant-backed costs and outcomes.
- `common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt:9` gates the entire Wendigo command surface behind reveal, the Wendigo route, the transformed country identity, the live merge host, and the pre-lock state.
- `common/national_focus/014_cannibalism_wendigo_focus.txt:24` gates the Wendigo focus overlay behind `cannibalism_reveal_complete`.
- All tunable numbers in the four primary Event 014 localisation files use live variables or script constants. The only remaining literal numeric identifier is the semantic scenario label `SCN-010` at `localisation/english/014_cannibalism_l_english.yml:1523`.
- The Event 014 player-facing files contain no `capped`, `hardcoded`, `reworked`, `newly added`, `implementation`, `debug`, `placeholder`, `fallback`, `player-safe`, recycled-tag, generation, or tag-lifecycle wording.

## In-Run Remediation Reverified

The live files were re-read after the main agent's concurrent remediation. The following formerly observed defects are absent in the final snapshot:

- `localisation/english/014_cannibalism_l_english.yml:405` now supplies `cannibalism_wendigo_reveal_world_tension` for `common/scripted_effects/014_cannibalism_wendigo_effects.txt:303`.
- `localisation/english/014_cannibalism_objectives_l_english.yml:48`, `localisation/english/014_cannibalism_objectives_l_english.yml:62`, and `localisation/english/014_cannibalism_objectives_l_english.yml:81` use in-world command-continuity wording.
- `localisation/english/014_cannibalism_l_english.yml:680` uses in-world chosen-Host continuity wording.
- `localisation/english/014_cannibalism_l_english.yml:698` and `localisation/english/014_cannibalism_l_english.yml:1343` describe paid Wendigo recruitment/muster contracts accurately after queue recruitment is disabled at transformation.
- `common/script_constants/014_cannibalism_warlord_focus_constants.txt:117` centralizes the four warlord consumption-yield values, and `common/scripted_effects/014_cannibalism_warlord_focus_effects.txt` uses those shared constants.
- The primary Event 014 localisation files contain no remaining tunable numeric literals or forbidden `capped` wording.

## Simplifications, Omissions, and Blockers

None. The requested localisation, scripted-localisation, achievements, Event Details terminal rows, tracker staging, objectives, focus closure, events, ideas, country names, character names, portrait-facing labels, constant-token validity, encoding, duplicate-key, missing-key, terminology, and secrecy surfaces were all included in the audit.

## Skill Use

- Used `.agents/skills/chaos-redux-events/SKILL.md` for Event 014 integration, player-facing writing, Event Details, event-log, and secrecy requirements.
- Used `.agents/skills/chaos-redux-subagents/SKILL.md` for read-only audit ownership, evidence standards, and handoff structure.
- No skill was created or updated.
