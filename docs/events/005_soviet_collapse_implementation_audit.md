# Event 005 Soviet Collapse Implementation Audit

Audit date: 2026-05-20

## Source Inputs

Read and verified present before this audit:

- `tmp/005_soviet_union_collapse_serious_completion_audit_spec.md`
- `tmp/005_soviet_union_collapse_terminal_release_league_threat_correction_spec.md`
- `tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/`
- `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md`
- `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md`
- `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md`
- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`

Required offline references consulted: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding from `paradox_wiki/`, plus vanilla `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md`.

## Files Inspected

- `events/005_soviet_collapse.txt`
- `events/005_soviet_collapse_custom.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/mtth/005_soviet_collapse_mtth.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `docs/events/005_soviet_union_collapse*.md`

## Current Implementation Surface

Decision categories: 25 Event 005 category definitions are gated by `is_soviet_collapse_active = yes`.

Missions: 118 Soviet crisis missions are manually activated through the capped objective queue. Existing mission audit documents 118 mission blocks, 118 activation references, 118 terminal cleanup removals, timed non-selectable objective shape, hidden scripted requirements, complete mission localisation, and distinct success/failure bodies.

Threat variables and effects: `soviet_collapse_moscow_authority`, `soviet_collapse_republic_confidence`, `soviet_collapse_military_obedience`, `soviet_collapse_foreign_appetite`, `soviet_collapse_old_movement_pressure`, and `soviet_collapse_total_collapse_threat` are centrally recalculated and clamped through scripted effects and script constants.

Release effects: first-wave releases use structured pools; progressive releases use MTTH weights; terminal collapse releases ordinary supported republics and frees Soviet subjects. Custom high-chaos successors are separate activation packages.

Local league logic: Baltic, Caucasus, and Central Asian leagues now require explicit two-member quorums through `has_soviet_collapse_*_league_quorum`. Ordinary local league founding no longer calls super-event helpers; it uses news events `chaosx.nr5.30`, `.31`, and `.32`.

Union Unmade logic: `soviet_collapse_union_unmade_first_month_lock` gates ordinary early collapse, and `soviet_collapse_show_union_unmade_super_event` calls `soviet_collapse_apply_terminal_collapse`.

AI hooks: current focus checks report 1013 focuses with `ai_will_do`; route choices and regular decisions keep dynamic AI weighting instead of flat-only behavior.

Localisation: existing localisation audits report no missing focus, idea, or decision name/description localisation and no `:0` localisation entries in Event 005 files.

Event log/details: existing event-log audits report Event ID 5 event-log detail mapping, actor mapping, entry event mapping, seven scripted detail functions, and 25 detail output localisation keys.

News/report events: ordinary league formation uses news events, while Union Unmade and rare high-chaos endgames retain super-event packages.

## Change Made In This Audit Pass

- Added quorum triggers for Baltic, Caucasus, and Central Asian league founding so one free member cannot found a local league alone.
- Removed ordinary local league and normal League-route super-event calls from regional founding effects and republic focus rewards.
- Direct source inspection now confirms local league formation effects fire `news_event = { id = chaosx.nr5.30 }`, `.31`, and `.32`, and Moldova's Eastern Buffer Coalition route fires `news_event = { id = chaosx.nr5.35 }`.
- Corrected the remaining Central Asian extreme-route custom-country tooltips so Basmachi, Turkestan, and Alash route pushes announce the Steppe Federation in-world instead of referring to a retired Steppe Federation super-event.

## 2026-05-20 Continuation Correction

- Routed terminal threat-ceiling checks through `soviet_collapse_maybe_show_union_unmade_super_event` so recalculation and progressive release cannot bypass the first-month and severe-failure gates.
- Added Kazakhstan to ordinary Union Unmade terminal release and subject-freeing lists.
- Wired the existing high-chaos successor spawn effects into the terminal-collapse path and added a terminal anti-Soviet war pass for all breakaway countries that can declare.
- Added vanilla-supported internal republic tags to Union Unmade terminal release and subject-freeing lists: `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.
- Routed those internal republic tags to `soviet_collapse_internal_republic_focus_tree`, a 62-focus shared tree with legal, security, liaison, northern forest, deeper Komi Syktyvkar/Pechora/mine-and-timber/exile-camp/northern-accord content, Bashkir Ufa/oilfield/mobile-defense/Volga-Ural compact content, Volga-Ural, expanded Crimean Ukraine-settlement/Turkish-mediation/peninsula-fortress/Black Sea compact content, Yakut Aldan and Arctic resource content, Far Eastern Pacific harbor and Amur customs content, Buryat Baikal pass and Ulan-Ude relay content, Tuvan border-road and steppe compact content, tag-specific Karelian, Tatar, Crimean, Far Eastern, Yakut, Buryat, and Tuvan branches, high-chaos old-name, and common-front branches.
- Added terminal league formation after releases and high-chaos successor spawning, before the terminal anti-Soviet war pass.
- Terminal local leagues now auto-form without charging newly released republics when Baltic, Caucasus, or Central Asian quorum exists, then invite valid regional partners.
- Terminal Free Republics' League formation now invites ordinary republics, vanilla-supported internal republics, and unfactioned Siberian/Far Eastern/Idel-Ural style high-chaos successors.
- Current source inspection covers terminal release/freeing tags, terminal sequencing, league formation helpers, internal republic focus routing, mission wiring counts, and duplicate republic focus IDs without relying on a Python completion gate.

## 2026-05-21 Final Clean Ledger Correction

- Re-read the seven final clean merged specification parts, `AGENTS.md`, the Event 005 event/assets/super-event/focus/decision skills, the required offline wiki pages, the National focus modding page, and vanilla script/focus documentation before continuing the audit.
- Added the missing required ledger file at `docs/events/005_soviet_collapse_full_implementation_ledger.md` using the exact final-package table columns.
- The new ledger does not claim final completion. It separates source-proven complete surfaces from `partially_complete` surfaces that still need stronger direct audits, per-country package rows, per-splinter package rows, final achievement verification, and the full 28-scenario validation table before the active goal can be closed.
- Reconfirmed the ordinary local-league super-event replacement surface: Baltic, Caucasus, Central Asian, Eastern Buffer, and Steppe Federation/League route presentation uses news/report events, while retired local-league super-event art remains documented as preserved source history only.

## Verification

Current checkout commands:

```text
git diff --check
rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt
rg -n "country_event = \\{ id = chaosx\\.nr5\\.(30|31|32)" common events
rg -n "soviet_collapse_show_(baltic_restoration_pact|caucasus_defense_compact|eastern_buffer_coalition)_super_event" common events interface
rg -n "soviet_collapse_show_(league_equal_republics|steppe_federation)_super_event|GFX_super_event_(league_equal_republics|steppe_federation)|super_event\\.(23|24|25|26|27)\\." common interface localisation events
rg -n "Steppe Federation super-event|fires the Steppe Federation super-event" localisation/english/005_soviet_collapse_custom_countries_l_english.yml
```

Result: no whitespace errors, no forbidden comparison operators in the edited script/trigger files, no local-league formation calls still using `country_event`, no active local-league super-event helper calls, no remaining Free Republics' League, Steppe Federation, Baltic League, Caucasus League, or Eastern Buffer Coalition super-event localisation/sprite mappings, and no player-facing Steppe Federation tooltip still calling it a super-event.
