# Event 006 small-file consolidation

## Scope

This bounded source-layout cleanup consolidates definition-only Event 006 files without changing identifiers, triggers, effects, category visibility, package gates, or runtime call sites.

The 47 Event 006 decision-category files, including the existing central category file, are now one compact parser surface at `common/decisions/categories/006_independence_wave_categories.txt`.

The 11 dormant compatibility effect files are now one compact parser surface at `common/scripted_effects/006_independence_wave_compatibility_effects.txt`.

The 11 matching dormant compatibility trigger files are now one compact parser surface at `common/scripted_triggers/006_independence_wave_compatibility_triggers.txt`.

Each merged section retains a source filename marker and its original filename order, and every executable definition keeps its original identifier.

## Preservation checks

The merged category registry contains 87 unique top-level category definitions, matching the 11 core definitions plus 76 definitions from the 46 former small files.

The merged compatibility effect registry contains 22 unique top-level scripted effects, matching two effects from each of the 11 former files.

The merged compatibility trigger registry contains 53 unique top-level scripted triggers, matching the former 11 files with no duplicate identifiers.

The retired `006_independence_wave_vanilla_formable_compatibility_triggers.txt` file remains separate because it is a distinct vanilla-formable compatibility surface rather than one of the 11 dormant IW package adapters.

Event 006 on-action files remain separate because several of them define the same engine callback keys, and concatenating those blocks without an explicit effect-composition audit could replace or reorder callbacks.

Package decisions, package effects, focus trees, and localisation remain separate because their file boundaries carry package ownership and audit scope. A follow-on definition-registry pass is recorded in `subagent_handoffs/006_event6_definition_registry_consolidation_2026-08-24.md`; it merges only the Event 006 ideas, characters, and country-leader-trait containers after preserving their unique identifiers and identical file-scoped constants.

## Size and file-count result

The consolidation removes 68 old small parser files and leaves three compact registries in their place, for a net reduction of 66 files.

Compared with the committed source snapshot, the three merged registries reduce the source bytes by 44,235 bytes after repeated banner prose is removed while the executable definitions remain intact.

## Validation boundary

The merge is a source-layout change only and does not claim live game loading, tooltip observation, or runtime compatibility acceptance.

Run the Event 006 allocator, country API, strict flag-family, and scenario-matrix audits after this commit, and use the merged registry paths for future source searches.
