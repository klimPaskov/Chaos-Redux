# Event 020 rat country package builder handoff

> Superseded by the two-tag correction handoff dated 2026-07-29. This historical builder record describes the retired multi-carrier draft; the current source of truth keeps only reusable RTA and separate RTX, and its former RTB–RTM surfaces are no longer implementation targets.

## Scope

This handoff covers the finite Rat Nation country package surfaces requested from the country-package subagent. It registers the exact tags already referenced by Event 020, adds dormant country shells and history, defines zero-manpower equipment-independent rat battalions and locked templates, adds the referenced Rat Nation and Rat King spirits, adds archetype-aware AI profiles, and adds BOM-encoded English localisation. It does not edit `common/scripted_effects/020_black_plague_rat_effects.txt`, evolution files, scenario files, focus trees, decisions, maps, or asset wiring.

## Changed files and identifiers

### Country registration and history

- `common/country_tags/020_black_plague_rat_countries.txt` registers RTA, RTB, RTC, RTD, RTE, RTF, RTG, RTH, RTI, RTJ, RTK, RTL, RTM, and RTX. The first thirteen are finite brood slots and RTX is the separate Rat King shell.
- `common/countries/020_black_plague_rat_country.txt` supplies the shared eastern graphical culture shell and a dark plague-red map colour. Shared definition reuse follows the dormant Oth-Kesh country precedent while localisation keeps each tag distinct.
- `history/countries/RTA - Black Plague Urban Warren.txt`, `RTB - Black Plague Ash Burrow.txt`, `RTC - Black Plague Carrion Nest.txt`, `RTD - Black Plague Red Sump.txt`, `RTE - Black Plague Grain Teeth.txt`, `RTF - Black Plague Wharf Brood.txt`, `RTG - Black Plague Rail Warren.txt`, `RTH - Black Plague Drowned Wharf.txt`, `RTI - Black Plague Field Maw.txt`, `RTJ - Black Plague Sewer Crown.txt`, `RTK - Black Plague Trench Brood.txt`, `RTL - Black Plague Salt Dock.txt`, `RTM - Black Plague Bone Warren.txt`, and `history/countries/RTX - Rat King.txt` provide dormant capital 1, the shared Event 020 OOB, zero research slots, 0.35 stability, full war support, neutrality-only politics, and the rat spirit package.
- `history/units/020_black_plague_rat_1936.txt` supplies five locked, non-recruitable templates: Rat Brood, Rat Shock Brood, Rat Burrow Column, Rat Carrion Guard, and Rat Dock Stowaways.

### Military package

- `common/units/020_black_plague_rat_units.txt` defines `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, `rat_dock_stowaways`, and support `rat_tunnelers`.
- Every rat sub-unit has `manpower = 0`, `active = no`, and no `need` block. This prevents ordinary human recruitment and conventional equipment consumption. The Event 020 scripted pulse remains the intended creation path.
- The unit families map to the four origin archetypes and King priorities: swarm line bodies, slow shock brutes, difficult-terrain burrowers, defensive carrion guard, coastal stowaways, and a tunnel support body.

### Ideas, AI, and localisation

- `common/ideas/020_black_plague_rat_ideas.txt` defines `black_plague_rat_brood_instinct`, `black_plague_rat_no_civilian_economy`, `black_plague_rat_dominion`, and `black_plague_rat_king_dominion` with the modifier package used by the existing Event 020 initialisers and cleanup.
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` defines `black_plague_rat_common_ai`, `black_plague_rat_urban_ai`, `black_plague_rat_field_ai`, `black_plague_rat_dock_ai`, `black_plague_rat_war_ai`, and `black_plague_rat_king_ai`. Profiles are gated by the existing rat country and archetype flags and bias city, rural, coastal, frontline, royal-node, and rat-only template requests.
- `localisation/english/020_black_plague_rat_countries_l_english.yml` provides BOM-encoded names, adjectives, all four cosmetic ideology selectors, neutrality party names, institutional brood and King names, unit and template strings, and the four idea names/descriptions.

## Before and after

Before this patch, the Event 020 effects referenced RTA through RTM, RTX, `rat_swarm`, `rat_tunnelers`, the Rat templates, four rat ideas, and rat AI identifiers, but the repository had no registered tags, country history, unit definitions, idea definitions, AI strategy file, or rat localisation for those identifiers. After this patch, all of those static package identifiers resolve to concrete files, the country shells load dormant with no human research or conventional economy, and the sub-units cannot draw human manpower or normal equipment.

## Coverage checklist

- Finite tag registration: complete for the thirteen brood slots and RTX, with no collision found in the mod, vanilla, or installed Workshop `common/country_tags` surfaces during the registration scan.
- Country definition and history: complete as dormant shared-shell files with the Event 020 OOB and runtime-reset-compatible politics.
- Politics and parties: neutrality-only setup and per-tag neutrality party localisation are present. Runtime leader creation remains in the existing effect file.
- Starting military: complete static zero-resource sub-unit and locked-template definitions. No conventional production lines, stockpiles, research, or human manpower were added.
- AI: common and four archetype profiles plus King profile are present and reference the registered custom unit identifiers.
- Localisation: tag names, adjectives, ideology selectors, party names, leader display strings, units, templates, and spirit text are covered in English with UTF-8 BOM.
- Focus access: no focus source was edited. The existing base and King focus files remain outside this handoff and are noted below because their runtime loaders now have registered country targets but still carry independent icon and gameplay diagnostics.

## Map, state, and runtime boundaries

No state ownership, controller, capital transfer, core, plague-state flag, Royal Basin, scenario, cleanup, or evolution effect was changed. The existing Event 020 runtime is still responsible for assigning a selected state, creating a leader, applying runtime flags, loading a focus tree, creating pulse units, and retiring or reusing a slot. The extra locked archetype templates remain available for future pulse unlock work, but the current cleanup effect only deletes Rat Brood and Rat Shock Brood; parent runtime work should extend cleanup before relying on those extra templates across slot reuse.

## Politics, leader, portraits, flags, and ideas

The existing effect still creates `The Brood Voice` and `The Rat King` with `GFX_portrait_europe_generic_land_13`. This patch intentionally does not change that forbidden effect surface and does not add a generic substitute. Dedicated collective portraits for Urban, Field, Dock, and War broods and a dedicated sentient RTX portrait are blocked pending the approved asset workflow. The exact expected portrait surface is a new `gfx/leaders/020_black_plague/` package plus `.gfx` sprite definitions; no files were fabricated here.

The four new idea definitions use dedicated `picture` identifiers but no unrelated generic icon. Final 64 by 64 idea DDS assets and their `interface/020_black_plague.gfx` registrations are therefore still blocked. The exact expected asset surface is `gfx/interface/ideas/020_black_plague/`.

All RTA through RTM and RTX normal, medium, and small flags are still blocked. The exact expected surface is `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga` for every registered tag. No placeholder or generic flag was created.

## Focus and technology findings

Read-only `hoi4.focus_inspect` confirmed that `black_plague_rat_focus_tree` and `black_plague_rat_king_focus_tree` now have source files, but the base tree reports 56 blocking diagnostics and the King tree reports 83 blocking diagnostics, primarily missing focus sprites plus one missing King idea and a malformed prerequisite group. The useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fac7d514d2dfe9823cdf05390c2e71552ed566c785d13e36a518f610166c995a/fdfff57b3f43e600ebc0814a7b07f5f17a7584d3d347e4a2b71da3f7ecee6536/focus-inspect.853554f6b2a0ec9f.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c77c5ec2e048a4c0d642ba59a9259750171ecc60f40811c41b23d44d34595a/91144ca33329cfee5711f0abae6334e156cbeea3c562f3f3a0f66068471f8b6d/focus-inspect.853554f6b2a0ec9f.json`. Those files were not edited because the requested scope excludes focus-tree and asset work.

No rat technology package was added. The installed HOI4 MCP package exposes no Technology Tree Viewer, so technology-tree inspection remains an unresolved limitation. The country histories deliberately keep research slots at zero until the parent chooses a documented focus-driven or captured-knowledge route.

## Validation performed

- Confirmed all fourteen tags are present exactly once in the new country-tag file and that RTA through RTM and RTX were clear in the mod, vanilla, and installed Workshop country-tag collision scan.
- Confirmed all fourteen history files point to `020_black_plague_rat_1936`, use the expected dormant political setup, and apply the correct brood or King idea set.
- Confirmed all six custom sub-unit IDs are defined, all six are inactive, every manpower value resolves to the zero constant, and no `need` block is present in the rat unit file.
- Confirmed all five static template names resolve to the unit IDs defined in the rat unit file, and all templates are locked with `force_allow_recruiting = no`.
- Confirmed all four idea IDs and all six AI profile IDs are defined and localised identifiers are unique in the new BOM file. The first three bytes of the localisation file are `239,187,191`.
- Ran read-only focus inspection for both existing rat trees to record the remaining focus and asset diagnostics without mutating focus source.

## Skipped meaningful validation and remaining risks

No full game parse or live scenario was run because the parent runtime package still has forbidden effect and evolution surfaces in flight, the final flags and portraits are not available, and focus assets and King-tree references are unresolved. Map safety, state transfer, pulse scheduling, leader metadata, retirement slot clearing, and King transfer remain parent-owned runtime work. The package is therefore static-country complete but not a complete playable Event 020 system until those blockers are addressed.

No commit was created from this shared worktree. The parent agent should review these files with the other Event 020 changes and commit the cohesive plan as one unit.
