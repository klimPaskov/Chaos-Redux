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
- `.tools/verify_event005_completion_gate.py`

## Current Implementation Surface

Decision categories: 25 Event 005 category definitions are gated by `is_soviet_collapse_active = yes`.

Missions: 118 Soviet crisis missions are manually activated through the capped objective queue. The verifier reports 118 mission blocks, 118 activation references, 118 terminal cleanup removals, timed non-selectable objective shape, hidden scripted requirements, complete mission localisation, and distinct success/failure bodies.

Threat variables and effects: `soviet_collapse_moscow_authority`, `soviet_collapse_republic_confidence`, `soviet_collapse_military_obedience`, `soviet_collapse_foreign_appetite`, `soviet_collapse_old_movement_pressure`, and `soviet_collapse_total_collapse_threat` are centrally recalculated and clamped through scripted effects and script constants.

Release effects: first-wave releases use structured pools; progressive releases use MTTH weights; terminal collapse releases ordinary supported republics and frees Soviet subjects. Custom high-chaos successors are separate activation packages.

Local league logic: Baltic, Caucasus, and Central Asian leagues now require explicit two-member quorums through `has_soviet_collapse_*_league_quorum`. Ordinary local league founding no longer calls super-event helpers; it uses normal country events `chaosx.nr5.30`, `.31`, and `.32`.

Union Unmade logic: `soviet_collapse_union_unmade_first_month_lock` gates ordinary early collapse, and `soviet_collapse_show_union_unmade_super_event` calls `soviet_collapse_apply_terminal_collapse`.

AI hooks: focus and decision audits report 775 focuses with `ai_will_do`; route choices and regular decisions keep dynamic AI weighting instead of flat-only behavior.

Localisation: verifier reports no missing focus, idea, or decision name/description localisation and no `:0` localisation entries in Event 005 files.

Event log/details: verifier reports Event ID 5 event-log detail mapping, actor mapping, entry event mapping, seven scripted detail functions, and 25 detail output localisation keys.

News/report events: ordinary league formation remains in normal events, while Union Unmade and rare high-chaos endgames retain super-event packages.

## Change Made In This Audit Pass

- Added quorum triggers for Baltic, Caucasus, and Central Asian league founding so one free member cannot found a local league alone.
- Removed ordinary local league and normal League-route super-event calls from regional founding effects and republic focus rewards.
- Tightened `.tools/verify_event005_completion_gate.py` so `local_league_surface` proves quorum triggers and absence of ordinary local-league super-event calls.

## 2026-05-20 Continuation Correction

- Routed terminal threat-ceiling checks through `soviet_collapse_maybe_show_union_unmade_super_event` so recalculation and progressive release cannot bypass the first-month and severe-failure gates.
- Added Kazakhstan to ordinary Union Unmade terminal release and subject-freeing lists.
- Wired the existing high-chaos successor spawn effects into the terminal-collapse path and added a terminal anti-Soviet war pass for all breakaway countries that can declare.
- Added vanilla-supported internal republic tags to Union Unmade terminal release and subject-freeing lists: `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.
- Routed those internal republic tags to `soviet_collapse_internal_republic_focus_tree`, a 20-focus shared tree with legal, security, liaison, northern forest, Volga-Ural, Crimea, and Siberian/Far Eastern/inner Asian branches.
- Added terminal league formation after releases and high-chaos successor spawning, before the terminal anti-Soviet war pass.
- Terminal local leagues now auto-form without charging newly released republics when Baltic, Caucasus, or Central Asian quorum exists, then invite valid regional partners.
- Terminal Free Republics' League formation now invites ordinary republics, vanilla-supported internal republics, and unfactioned Siberian/Far Eastern/Idel-Ural style high-chaos successors.
- Restored `.tools/verify_event005_completion_gate.py` with deterministic gates for terminal release/freeing tags, terminal sequencing, league formation helpers, internal republic focus routing, mission wiring counts, and duplicate republic focus IDs.

## Verification

Historical command recorded by the previous audit:

```text
python3 .tools/verify_event005_completion_gate.py
```

Current checkout commands:

```text
python3 -m py_compile .tools/verify_event005_completion_gate.py
python3 .tools/verify_event005_completion_gate.py
git diff --check
rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt
```

Result: verifier exit 0, no whitespace errors, and no forbidden comparison operators in the edited script file.
