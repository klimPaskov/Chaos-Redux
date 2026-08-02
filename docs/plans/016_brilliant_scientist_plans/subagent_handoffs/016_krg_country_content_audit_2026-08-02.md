# Event 016 Kruger State country-content audit

Date: 2026-08-02

Status: audit complete; no gameplay or model files were changed by this audit.

## Scope

This pass checked the current Event 016 Kruger State package against `docs/specs/016_brilliant_scientist_specs/matrices/016_country_package_matrix.md` and specification parts 5, 6, and 7.

The scope was limited to non-model country content, route wiring, map-safe setup, focus and decision surfaces, and asset/localisation references.

## Coverage checklist

| Surface | Current evidence | Result |
| --- | --- | --- |
| Tag, definition, and history | `common/country_tags/016_brilliant_scientist_country.txt`; `common/countries/Kruger State KRG.txt`; `history/countries/KRG - Kruger State.txt`; `history/units/016_brilliant_scientist_dormant.txt` | Covered. KRG is a dormant event-created country with valid empty OOB history. |
| Formation and map transaction | `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `brilliant_scientist_release_kruger_state_from_formation`, `brilliant_scientist_transfer_selected_state_to_kruger_state`, and `brilliant_scientist_transform_host_into_kruger_state`; `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` | Covered in source. The capital-core-before-`release = KRG` transaction repair is already present in the shared worktree and was not changed here. Live formation, ownership, supply, and cleanup remain user-owned validation. |
| Cores, claims, capitals, and territory sizing | `brilliant_scientist_transfer_selected_state_to_kruger_state`; bounded territory planner/triggers in `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` and `common/scripted_triggers/016_brilliant_scientist_territory_triggers.txt` | Covered by route-specific charter, rebellion, enclave, and takeover branches. No hardcoded Event 016 state list was found. |
| Country names, parties, ideologies, and cosmetics | `common/scripted_effects/016_brilliant_scientist_country_effects.txt` route identity helpers; `common/countries/016_brilliant_scientist_cosmetics.txt`; `localisation/english/016_brilliant_scientist_country_l_english.yml`; six KRG route flags | Covered for base and implemented route cosmetics. |
| Fixed leader and portraits | `common/characters/016_brilliant_scientist_characters.txt:10-44`; `common/scripted_effects/016_brilliant_scientist_effects.txt:2634-2810`; `interface/016_brilliant_scientist.gfx` | Covered for Doctor Warren Kruger and the machine continuity network. Portrait paths resolve to the existing stage assets. |
| Advisors, commanders, and route leaders | Kruger theorist/scientist roles in `common/scripted_effects/016_brilliant_scientist_effects.txt:2763-2792`; generated staff in `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt:107`; command choices in `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1198-1224` | Partial. The route flags and lifecycle ideas are wired, but there is no named route-specific advisor or commander roster beyond Kruger and `KRG_continuity_network`. See the substantive gap below. |
| Starting ideas and lifecycle | `common/scripted_effects/016_brilliant_scientist_country_effects.txt:apply_starting_country_ideas`; `common/ideas/016_brilliant_scientist_country_ideas.txt`, `016_brilliant_scientist_focus_ideas.txt`, and `016_brilliant_scientist_project_force_ideas.txt` | Covered. Formation-origin liabilities and route lifecycle ideas are defined and localized. |
| Conventional and project forces | `common/scripted_effects/016_brilliant_scientist_country_effects.txt:apply_conventional_guard_package`; `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`; `common/units/016_brilliant_scientist_project_forces.txt` | Covered in source with bounded conventional guard derivation and idempotent project-force runtime reconstruction. 3D entity packages remain outside this audit. |
| Equipment, manpower, supply, production, and technology | `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`; `common/technologies/016_brilliant_scientist_project_technologies.txt`; `common/technologies/016_brilliant_scientist_project_force_technologies.txt`; `common/script_enums.txt` | Covered in source. Six equipment families and variants are enum-registered, production-gated, and referenced by project-force effects. |
| Focus-tree assignment and route logic | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`; `brilliant_scientist_initialize_current_kruger_state` loads `brilliant_scientist_kruger_state_focus_tree` | Covered. The tree contains 100 authored focuses, opening trunk, command choices, project branches, diplomacy, expansion, crisis, and terminal routes. All 100 focus localisation keys and icon declarations were found. |
| Focus unlock consumers | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` and Event 016 decision/effect files | Covered in static scan. 163 distinct `brilliant_scientist_focus_unlock_*` producers were found and no producer-only flag was identified in the completed audit. |
| Decisions and missions | `common/decisions/016_brilliant_scientist_kruger_state_*.txt`; `common/decisions/categories/016_brilliant_scientist_*.txt`; `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml` | Covered. Static count is 134 decision/mission IDs and 10 categories. Primary and `_desc` localisation keys exist for all 134 IDs, and the 40 distinct decision icon tokens have GFX declarations. |
| AI strategy and templates | `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`; Event 016 templates and project-force effects | Covered in source. There are 19 KRG plans; 97 focus IDs are listed explicitly and the three omitted optional focuses have `ai_will_do` values, so they use normal fallback focus selection. |
| Classification, diplomacy, and cleanup | Event 016 scripted country triggers/effects, route identity helpers, diplomacy helpers, and evolution cleanup calls | Covered in source. Runtime scenario validation remains outstanding. |
| Localisation, flags, portraits, focus/idea/decision icons | Event 016 English localisation, `gfx/flags/KRG*.tga`, `interface/016_brilliant_scientist.gfx`, focus and decision GFX files | Covered for currently referenced assets. No country-package asset hole was found in this pass. |

## Substantive country-content gap

The matrix completion checklist requires `Advisors, commanders, and route leaders`, and the focus-tree specification calls for advisors, commanders, assistants, and institutional leaders as focus rewards.

The current implementation has only two fixed character definitions, `KRG_warren_kruger` and `KRG_continuity_network`, in `common/characters/016_brilliant_scientist_characters.txt:10-44`.

`brilliant_scientist_krg_count_and_recruit_surviving_staff` at `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt:107` generates an unnamed scientist and increments the roster variable, but does not add a named advisor or commander.

`brilliant_scientist_krg_coordinate_project_commanders` at `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt:609-625` rebuilds the project-force package and sets `brilliant_scientist_krg_project_command_coordination_active`; it does not recruit or promote commander characters.

The command route effects at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1198-1224` currently swap lifecycle ideas (`brilliant_scientist_general_staff_command`, `brilliant_scientist_machine_command_network`, `brilliant_scientist_clone_officer_corps`, and `brilliant_scientist_project_council_command`) rather than installing route-specific staff.

This is a real content-depth gap, but it is not a safe narrow patch. Creating route-specific advisors or commanders would require approved identity design, role traits, character ownership, portrait decisions, localisation, route reward wiring, and balance review. I did not invent those identities or assets.

## Ranked next content tranche

1. Design and implement a route-specific staff roster for the general-staff, machine-command, clone-officer, and project-council branches, with institutional names where a role is non-personal and approved portraits only where a visible character exists.
2. Add commander/advisor reward wiring to `KRG_form_the_provisional_command`, `KRG_count_the_surviving_staff`, and `brilliant_scientist_krg_coordinate_project_commanders`, then audit retirement and route-transition cleanup.
3. Run parent-owned live formation and takeover scenarios covering capital core, release/transform, selected-state ownership, leader and idea initialization, inherited technology, guard/project forces, focus assignment, diplomacy, and cleanup.
4. Review the opening `recruit_character = KRG_warren_kruger` call at `common/scripted_effects/016_brilliant_scientist_effects.txt:2659` with the role owner before changing it; replacement would affect the parent-wide character transaction.
5. Run a focused quantitative AI/project-force balance pass and rerun the technology-tree inspection when a Technology Tree Viewer is available. The installed package exposes no Technology Tree Viewer, so that validation remains unresolved.

## Validation and limitations

- Offline Paradox wiki pages required by `AGENTS.md` and the relevant vanilla documentation pages were read before this audit.
- Static focus, decision, localisation, icon, character, equipment, and scripted-reference checks were run against the current Event 016 files.
- A previous focused `hoi4.focus_inspect` pass reported 100 nodes, 0 diagnostics, and 108 connectors. A current workspace-wide call hit `SCAN_BYTE_LIMIT`, so the earlier focused result is retained as the useful artifact reference.
- `hoi4.tech_inspect` returned `TECH_INSPECTED_PARTIAL` for `brilliant_scientist_portal_warfare_tech`; direct source checks remain the stronger evidence until the technology viewer limitation is resolved.
- No Hearts of Iron IV process was launched and no live scenario claim is made.

## Worktree note

This audit changed only this handoff file.

The shared worktree contains an unrelated uncommitted Event 016 convoy-trigger normalization in `common/decisions/016_brilliant_scientist_directorate_facilities.txt` (`convoy > ...` changed to `has_equipment = { convoy > ... }` in two trigger sites). That change was not authored, reviewed, or committed by this audit.

No gameplay fallback or model simplification was introduced here. The missing staff roster is explicitly queued for design rather than represented by a placeholder.
