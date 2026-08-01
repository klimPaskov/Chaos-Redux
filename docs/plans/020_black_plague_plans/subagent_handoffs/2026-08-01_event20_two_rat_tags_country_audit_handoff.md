# Event 020 two-tag rat country-package audit handoff

## Scope and source of truth

This audit covers the Event 020 Rat Nation and Rat King runtime package only.

The package was compared against `docs/specs/020_black_plague_specs/matrices/country_package_matrix.md` and the superseding two-tag correction at `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`.

The correction is applied as the identity rule: exactly two tags exist, `RTA` is the reusable Rat Nation carrier, and `RTX` is the separate Rat King.

No 3D model surface was added or expected for this audit.

## Coverage checklist

| Surface | Result | Evidence and remaining risk |
| --- | --- | --- |
| Tag registration | Covered | `common/country_tags/020_black_plague_rat_countries.txt:8-11` registers only `RTA` and `RTX`, and no collision was found in the mod, vanilla country-tag surface, or installed Workshop country-tag files. |
| Country definition and history | Covered with runtime shell | `common/countries/020_black_plague_rat_country.txt:9-11` is a shared graphical shell, while `history/countries/RTA - Rat Nation.txt:2-9` and `history/countries/RTX - Rat King.txt:2-9` hold dormant setup. Both histories use `capital = 1` as a placeholder that runtime must rebind. |
| Spawn and capital | Patched scenario path | `common/scripted_effects/020_black_plague_rat_effects.txt:482-528` requires `black_plague_rat_spawn_state` and sets the emergence capital; the scenario path now saves that target at `common/scripted_effects/020_black_plague_scenario_effects.txt:250-255`. |
| State and map safety | Covered dynamically | Spawn eligibility is gated by `black_plague_rat_state_can_spawn` in `common/scripted_triggers/020_black_plague_rat_triggers.txt:63-69`, and state transfer preserves the rat phase and adds only a valid starting core. Read-only map inspection of state 1 passed all five map validation checks; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c28f37edee7b73e9a701705fe7a9efb91ac4abbe8c4d460db093e860d405245/2573981b7db5f5142537804a38ee1af34950ded75ef564c5ebc05995b1f6f4ed/map-inspect.b34b07ad729b6b7b7.json`. |
| Politics and classification | Covered | Both histories use neutrality-only politics with elections disabled, and runtime flags `black_plague_rat_country` or `black_plague_rat_king_country` feed `is_special_chaos_country` and `is_actual_nonhuman_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt:22-64`. |
| Leaders | Partial | RTA creates the institutional `The Brood Voice` with one of four collective portraits at `common/scripted_effects/020_black_plague_rat_effects.txt:414-444`; RTX creates `The Rat King` at `common/scripted_effects/020_black_plague_rat_effects.txt:773-780`. The King name is a title rather than an actual-like fictional name and epithet pool. |
| Portraits and flags | Static coverage present | Five 156x210 RGBA DDS portraits exist under `gfx/leaders/020_black_plague/`, and normal, medium, and small `RTA` and `RTX` flags exist under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. The matrix-required ten-to-twelve-frame animated King package is not present. |
| Parties and localisation | Covered for current identifiers | `localisation/english/020_black_plague_rat_countries_l_english.yml:4-43` covers both country identities, ideology variants, party names, and leader keys, and lines 46-72 cover rat unit and idea names. |
| Ideas and mechanics | Partial | `common/ideas/020_black_plague_rat_ideas.txt` defines the four currently used ideas, and runtime tracks Brood Mass, division caps, Dominion, Sentience, Cohesion, and Hunger. The matrix names a staged `Fractured Instinct` lifecycle spirit and route-specific failure forms that are not defined in this package. |
| Decisions | Present, separate audit needed | `common/decisions/020_black_plague_rat_decisions.txt` and `common/decisions/categories/020_black_plague_rat_categories.txt` provide brood and King actions with AI weights, but their duplicate category surfaces should remain under the decision auditor. |
| Focus trees | Runtime assignment present, icons incomplete | RTA loads `black_plague_rat_focus_tree` at `common/scripted_effects/020_black_plague_rat_effects.txt:445-446`, and RTX loads `black_plague_rat_king_focus_tree` at lines 779-780. Read-only MCP focus inspection found 39 blocking icon diagnostics for the RTA tree and 60 for the King tree; the focus auditor owns those fixes. |
| Army and equipment | Covered for scripted forces | `common/units/020_black_plague_rat_units.txt` defines six inactive rat sub-units with zero manpower and no `need` equipment blocks, and `history/units/020_black_plague_rat_1936.txt` provides five locked templates without starting divisions. Runtime creates 10-70 opening divisions with zero manpower and equipment factors at `common/scripted_effects/020_black_plague_rat_effects.txt:458-479` and `:326-380`. |
| Supply, industry, research | Partial but intentional | Rat ideas disable ordinary civilian production and recruitment, and both packages set zero research slots. The matrix's captured-knowledge and nest-industry progression is not represented as a conventional technology or factory package. |
| AI and playability | Patched target-role surface | Existing strategy IDs in `common/ai_strategy/020_black_plague_rat_ai_strategy.txt:24-159` referenced rat roles without any AI template definitions. `common/ai_templates/020_black_plague_rat_templates.txt` now defines RTA/RTX-only target roles for `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, and `rat_dock_stowaways`. |
| Scenario and cleanup | Patched spawn target and retirement array | Triggerable scenario creates one RTA before Evolution III and transfers one RTX through Evolution IV, then expands the Royal Basin in `common/scripted_effects/020_black_plague_scenario_effects.txt:376-422`. Retirement now clears the stale RTA controlled-state array and count at `common/scripted_effects/020_black_plague_rat_effects.txt:647-669`. |

## File-surface checklist

- `common/country_tags/020_black_plague_rat_countries.txt` contains exactly `RTA` and `RTX`.
- `common/countries/020_black_plague_rat_country.txt` contains only the shared graphical shell and color.
- `history/countries/RTA - Rat Nation.txt` and `history/countries/RTX - Rat King.txt` are the only rat country history files.
- `history/units/020_black_plague_rat_1936.txt` and `common/units/020_black_plague_rat_units.txt` cover locked templates and inactive non-human battalions.
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` and `common/ai_templates/020_black_plague_rat_templates.txt` cover the two-tag AI surface.
- `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/scripted_effects/020_black_plague_scenario_effects.txt`, and `common/scripted_triggers/020_black_plague_scenario_triggers.txt` cover allocation, spawn, pulses, King transfer, scenario creation, and cleanup.
- `common/ideas/020_black_plague_rat_ideas.txt`, `common/decisions/020_black_plague_rat_decisions.txt`, and `common/decisions/categories/020_black_plague_rat_categories.txt` cover current ideas and actions.
- `common/national_focus/020_black_plague_rat_focus_tree.txt` and `common/national_focus/020_black_plague_rat_king_focus_tree.txt` are assigned by runtime.
- `localisation/english/020_black_plague_rat_countries_l_english.yml`, `localisation/english/020_black_plague_rat_decisions_l_english.yml`, and `localisation/english/020_black_plague_rat_focus_l_english.yml` cover current player-facing identifiers.
- `interface/020_black_plague_rat_identity.gfx` registers focus, idea, and portrait sprites.
- `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`, and `gfx/leaders/020_black_plague/` contain the current static identity package.

## Missing or stale country-package surfaces

- The matrix-required animated RTX portrait package is missing; only `gfx/leaders/020_black_plague/portrait_rat_king_static.dds` is wired.
- Natural Evolution III currently transfers one selected state to RTA rather than establishing the matrix's one-to-three connected-state basin; subsequent Rat Nation growth is unit-only because `black_plague_rat_try_absorb_adjacent_brood` is intentionally a no-op.
- The matrix-required route-specific or staged `Fractured Instinct` national spirit is missing from `common/ideas/020_black_plague_rat_ideas.txt`.
- The matrix's captured-knowledge progression and explicit nest-industry progression are not represented as country technologies or buildings.
- The current RTX leader text `The Rat King` is an institutional title and does not satisfy the stronger actual-like fictional sovereign name-and-epithet requirement.
- Historical handoffs under `docs/plans/020_black_plague_plans/subagent_handoffs/` still mention retired `RTB`-`RTM` tags, but those records are explicitly marked superseded and no current runtime file references those tags.

## Map and state setup issues

- Static country history uses state 1 only as a safe dormant capital placeholder.
- Natural spawn and scenario creation select an established, severe, or collapsed human state and transfer exactly that state before rebinding the capital.
- The scenario creation bug was that `black_plague_rat_create_from_state` saw no `black_plague_rat_spawn_state`; the new scoped `save_event_target_as` fixes archetype selection and `set_capital` for triggerable bootstrap.
- The natural King path has an explicit no-Royal-Basin failure flag at `common/scripted_effects/020_black_plague_rat_effects.txt:836-838`; scenario expansion assumes Evolution IV successfully established RTX first.
- No map write was performed by this audit.

## Politics, leader, portrait, flag, advisor, and party issues

- `RTA` and `RTX` are separate tags sharing one safe country definition file, with distinct localisation and flags.
- RTA's four archetype portraits are collective and use the institutional name `The Brood Voice`.
- RTX has a static generated-looking portrait but lacks the required animated package and actual-like sovereign name/epithet pool.
- No rat advisors or high-command roles are defined; this is a matrix coverage gap rather than a narrow tag or runtime defect.
- Neutrality party names are present for both tags, and ordinary election or subject behavior is disabled by history and runtime.

## Focus, decision, idea, and asset issues

- RTA and RTX focus trees are loaded by their respective runtime initializers, but the MCP focus inspections reported missing generic sprite references in both trees.
- Current idea IDs resolve to `black_plague_rat_brood_instinct`, `black_plague_rat_no_civilian_economy`, `black_plague_rat_dominion`, and `black_plague_rat_king_dominion`.
- Decision categories and localisation exist, but duplicate category declaration surfaces should be reviewed by the decision auditor.
- Static flags, portraits, focus sprites, and idea sprites are registered; animated RTX frames are absent.

## Starting military, technology, industry, supply, and production issues

- Rat battalions are inactive, have zero manpower, and omit ordinary equipment requirements.
- Locked templates and scripted `create_unit` calls keep reinforcement outside the normal recruit-and-deploy interface.
- Opening force sizing is clamped to the 10-70 matrix range, and pulses add one scripted division after the Brood Mass cost and cap checks.
- Both tags start with zero research slots and no conventional production package; the country ideas suppress ordinary civilian economy behavior.
- Supply consumption remains explicit on each rat battalion and is modified by the current Dominion ideas.

## AI and playability issues

- Before this patch, `template_prio` and `role_ratio` IDs in `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` had no corresponding `common/ai_templates` roles.
- The new `common/ai_templates/020_black_plague_rat_templates.txt` is available only to `RTA` and `RTX` and targets the existing rat sub-unit IDs, including `rat_tunnelers` support where the locked templates use it.
- AI expansion and front-control strategy remains archetype-aware through existing flags and state triggers.
- Normal faction, subject, and rat-rat diplomacy is not introduced; King absorption is scripted state transfer after the grace period.
- Triggerable scenario launch still requires a free RTA slot via `black_plague_scenario_has_free_rat_slot` at `common/scripted_triggers/020_black_plague_scenario_triggers.txt:89-94`; a natural active RTA therefore blocks launch instead of preserving that carrier, which remains a scenario-design risk for the parent.

## Changes made

### Changed files

- `common/ai_templates/020_black_plague_rat_templates.txt` was added.
- `common/scripted_effects/020_black_plague_scenario_effects.txt` was changed at the scenario RTA creation block.
- `common/scripted_effects/020_black_plague_rat_effects.txt` was changed in retired RTA cleanup.
- `common/script_constants/020_black_plague_rat_constants.txt` changed the `black_plague_rat_pool` schema from `int` to `fixed_point`.
- This handoff was added at `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_two_rat_tags_country_audit_handoff.md`.

### Before and after behavior

- Before: triggerable scenario selected a state but called `black_plague_rat_create_from_state` without `black_plague_rat_spawn_state`, so archetype detection and capital rebinding could fail.
- After: the selected scenario state is saved as `black_plague_rat_spawn_state` before creation, matching the natural Evolution III path.
- Before: RTA and RTX AI strategy references had no target roles.
- After: five rat-only role-level AI template entries resolve every strategy role used by the package.
- Before: the rat pool constants declared integer data while containing decimal stability tuning.
- After: `fixed_point` accepts both the decimal stability values and the integer tuning values used by the runtime.
- Before: retired RTA cleanup removed the country from the active array but retained the global controlled-state array and count.
- After: cleanup clears that stale array and resets its count before the carrier is reusable.

## Validation performed

- Read-only MCP map inspection of state 1 returned `MAP_INSPECTED` with all five map validation checks passed.
- Read-only MCP focus inspections returned source-linked diagnostics for both rat trees; no focus file was modified in this country audit.
- Static identifier cross-check confirmed exactly two registered rat tags, both country histories, all six rat sub-units, and all five new AI roles.
- Static brace-count checks matched for all changed Clausewitz files.
- The changed files contain no 3D model or runtime entity references.
- No Hearts of Iron IV process was launched.

## Skipped meaningful validation

- No live save or in-game AI test was run because live consumer validation belongs to the parent and user.
- No technology-tree inspection was run because the installed MCP package exposes no Technology Tree Viewer; this remains an unresolved limitation.
- No focus rewrite or icon patch was run because those surfaces belong to the focus-tree audit scope.

## Remaining setup and identity risks

- RTX still needs an approved actual-like fictional sovereign name/epithet decision, gender metadata review if a personal portrait is adopted, and an animated portrait package with static fallback.
- Both focus trees need their missing sprite references resolved before focus completion can be claimed.
- The matrix's Fractured Instinct lifecycle spirit, captured-knowledge progression, and advisor package remain unimplemented or unresolved.
- Triggerable scenario launch should be reviewed for the case where natural RTA already exists, because the current free-slot gate blocks that launch.
- Royal Basin selection has a failure flag but no parent-level fallback plan beyond the scenario's preselected expansion path.

## Review handoff

Parent should review the four changed gameplay files and the new AI-template file, then route focus icon diagnostics to the focus auditor and RTX identity/animated portrait gaps to the asset and identity owners.
