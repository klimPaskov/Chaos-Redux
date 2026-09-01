# IW-050 Komi country-package audit and roster guard — 2026-08-30

## Disposition

`PATCHED PACKAGE-LOCAL / CENTRAL ADMISSION STILL HOLD-FAIL-CLOSED`.

IW-050 remains the vanilla `KOM` carrier, package ID `iw_050`, anchor state `397` (Syktyvkar), and reservation group `RG-397`.

One narrow source defect was confirmed and repaired: the package-local roster checkpoint could publish `independence_wave_command_roster_ready` and `independence_wave_komi_roster_checkpoint` from the exact vanilla `KOM_pavel_murashev` character before the parent-owned identity/rights receipt existed.

No central adapter, attestation, preflight, Join, scenario, queue, cost, pressure, map, focus layout, party, leader, portrait, flag, or generic fallback surface was changed.

## Authority and audit scope

The accepted identity and package rows are `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:51`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:51`, and `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:33`.

The accepted regional/formable context is `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:593` and `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv:13` (FORM-12 Volga-Ural Federation).

The package implementation note is `docs/events/006_independence_wave/komi_package.md`.

The offline Paradox wiki core pages and the country-creation, national-focus, character, portrait, decision, event, idea, AI, and country-creation references were opened from `paradox_wiki/` before source review.

The corresponding installed vanilla documentation was consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including effects, triggers, script concepts, and AI strategy documentation.

The inspected installed vanilla surfaces were the `KOM` tag/country, `KOM_pavel_murashev`, its portrait registration, history, states `397`, `262`, and `581`, and related Event 005 Komi focus/effect/asset surfaces.

## Country-package coverage checklist

| Surface | Status | Evidence and finding |
| --- | --- | --- |
| Candidate identity | Static pass; admission blocked | IW-050 resolves to Komi/KOM, Layer B, northern republic, compact anchor 397, and RG-397 in the accepted registry rows. `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-19` requires the active Event 006 origin and rejects Soviet Collapse origin flags. |
| Tag registration and reuse | Static pass | Installed `common/country_tags/00_countries.txt:232` maps `KOM` to `countries/Komi.txt`; no Chaos Redux duplicate KOM registration was found. The package reuses the registered tag as required by the matrix. |
| Anchor and optional territory | Source present; current MCP proof unavailable | The binding `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:51` fixes 397 with optional 262 and 581. Region-05 loader/reservation code binds IW-050 and reserves 397 before attempting 262/581 in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` and its paired region trigger registry. |
| Host survival | Source guarded; runtime receipt unavailable | Setup and runtime predicates require a former-host target whose protected state remains owned by the former host. The accepted binding protects SOV state 219; no live release transaction was run. |
| History and leader | Vanilla source present; identity gate blocked | Vanilla `history/countries/KOM - Komi Republic.txt` uses capital 397, three research slots, ordinary technologies, baseline politics, and `recruit_character = KOM_pavel_murashev`. Vanilla `common/characters/KOM.txt` defines the male Stalinist country-leader role. |
| Portrait provenance | Blocked | Vanilla `interface/_leader_portraits.gfx:5576-5579` maps `GFX_portrait_Pavel_Murashev` to generic `Portrait_Europe_Generic_3.dds`. The portrait handoffs found no attributable 1936 image and no rights-clear exact source. No replacement or generated portrait was made. |
| Flag/symbol provenance | Blocked | The mod has only Event 005-era `KOM_democratic.tga` files under `gfx/flags/`; no Event 006 neutral or route flag packet exists. The symbol handoff rejects modern and post-1936 Komi ASSR symbols for the opening. |
| Politics and parties | Source present | `common/scripted_effects/006_independence_wave_komi_package_effects.txt:146-232` initializes the democratic baseline and four guarded route governments, while `localisation/english/006_independence_wave_komi_l_english.yml:2-9` supplies route party names. Cleanup restores vanilla party names and popularity at lines 412-455. |
| Advisors and commanders | No package additions | No Komi advisor, high-command, commander, institutional portrait, random-name pool, or invented leader is added. The existing vanilla roster remains the only character consumer. |
| Shared focus tree | Source present; current MCP proof unavailable | The shared tree is `independence_wave_focus_tree` at `common/national_focus/006_independence_wave_focus.txt:38`. Five KOM callbacks are wired at the shared congress, railhead, guards, former-host, and network focus rewards, including lines 140, 193, 227, 1461, and 1732. No focus layout was edited. |
| Decisions and mission | Source present; typed pool incomplete | The current package block is consolidated in `common/decisions/006_independence_wave_siberian_decisions.txt:2513-2798`, with one 420-day founding mission and ten serialized paid projects. Category `independence_wave_komi_northern_compact_category` is in `common/decisions/categories/006_independence_wave_categories.txt:431-437`. Existing typed decision evidence is incomplete and no new decision was added. |
| Ideas and lifecycle | Source present | Seven tag-restricted ideas are in `common/ideas/006_independence_wave_ideas_registry.txt:2896-2973`, with setup/route/failure/cleanup lifecycle in the package effects. All seven ideas have package localization. |
| Localisation | Static package pass | `localisation/english/006_independence_wave_komi_l_english.yml` is BOM-encoded and covers route parties, seven ideas, category/mission, ten project names/descriptions, costs, and effect tooltips. Vanilla restoration keys remain supplied by vanilla. |
| Starting force | Source contract present; runtime proof unavailable | The accepted mapping is p50 `mountain_frontier` with five named reinforcement pathways and no navy/air inheritance. `has_prepared_independence_wave_iw_050_package_setup` requires that mapping, current generation, and all five pathways in `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:149-209`. |
| Technology and research | No package-specific surface | Vanilla Komi history supplies the normal three research slots and technology baseline; IW-050 adds no technology or doctrine. The installed package exposes no Technology Tree Viewer, so no tree-render acceptance claim is made. |
| Industry, supply, production | Source present; runtime proof unavailable | Package decisions use shared command/manpower/transport/stability and civilian-factory reservation costs; ledger effects use package constants and generic country deltas. No pre-event UI, queue, pressure, or cost was changed. |
| AI | Source present; probability evidence unavailable | Four strategy blocks are in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1562-1611` for survival, host restraint, settled republic, and emergency command. No AI values were changed. |
| Assets and manifests | Blocked at source gate | No Event 006 Komi portrait, flag, route emblem, icon, manifest, or runtime placeholder was created. Shared icons are reused only where already wired. |
| Formables | Registry source only | FORM-12 recognizes Komi among possible Volga-Ural members, but no Komi formable promotion or membership shortcut was added. Existing ownership, consent, invitation, and active-package gates remain authoritative. |
| Central admission | Intentionally absent | IW-050 is absent from the central runtime adapter, content attestation, normal preflight, scenario/SCN-008 preflight, setup/final-validation/cleanup dispatch, and deterministic Join lists. This hold is preserved. |

## File-surface checklist

| Surface | Current file and identifiers | Finding |
| --- | --- | --- |
| Package trigger | `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-220` | Package/origin/anchor/host/roster/force/AI/setup/runtime predicates are present. `has_independence_wave_komi_command_roster` at lines 91-97 requires both the parent-owned rights flag and `KOM_pavel_murashev`. |
| Package effect | `common/scripted_effects/006_independence_wave_komi_package_effects.txt:321-458` | Setup, route installers, five focus aliases, project lifecycle, validation, and cleanup are present. The roster effect was the only source line changed in this audit. |
| Roster checkpoint | `independence_wave_komi_checkpoint_vanilla_roster` at `common/scripted_effects/006_independence_wave_komi_package_effects.txt:321-327` | Before: package plus exact character could set both readiness flags. After: package, `has_country_flag = independence_wave_iw_050_identity_rights_cleared`, and exact character are all required. |
| Setup caller | `independence_wave_setup_iw_050_komi` at `common/scripted_effects/006_independence_wave_komi_package_effects.txt:329-398` | This is the only package-local caller of the checkpoint. It clears both readiness flags before retry and cannot complete setup unless the downstream rights-aware roster trigger passes. |
| Shared `.350` event | `events/006_independence_wave.txt:147-155`; `common/scripted_effects/006_independence_wave_effects.txt:3085-3246` | `.350` calls the shared roster effect, which has no KOM branch. The package-local checkpoint therefore remains the sole IW-050 roster writer. |
| Region loader | `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:429-436`; `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | IW-050 planner/load/reservation rows are present and intentionally do not establish admission. |
| Decisions/category | `common/decisions/006_independence_wave_siberian_decisions.txt:2513-2798`; `common/decisions/categories/006_independence_wave_categories.txt:431-437` | One mission plus ten projects, ordinary decision-category UI, shared icons, and package-local guards are present. No dedicated Komi scripted GUI exists. |
| Focus surface | `common/national_focus/006_independence_wave_focus.txt:38,140,193,227,1461,1732` | Shared focus tree and five guarded KOM helper calls are source-wired. |
| Ideas | `common/ideas/006_independence_wave_ideas_registry.txt:2896-2973` | Seven package ideas use existing shared idea pictures and `allowed = { original_tag = KOM }`. |
| AI | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1562-1611` | Four package strategy blocks remain unchanged. |
| Localisation | `localisation/english/006_independence_wave_komi_l_english.yml:2-70` | Package display coverage is present and the file has a UTF-8 BOM. |
| Vanilla carrier | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:232`; `common/characters/KOM.txt`; `history/countries/KOM - Komi Republic.txt` | The registered carrier and ordinary history remain untouched. |
| Central dispatch | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63,159-220,411+`; `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | No IW-050 central branch exists. No central file was edited. |
| Join | `common/scripted_effects/006_independence_wave_join_effects.txt` | No literal IW-050/KOM Join branch exists. No Join file was edited. |

## Map and state findings

Installed vanilla `history/states/397-Syktyvkar.txt` defines state 397 with SOV owner, SOV and KOM cores, Syktyvkar victory point 108, infrastructure 1, and the expected provinces.

Installed vanilla `history/states/262-Torzhok.txt` defines the optional Pechora state with SOV owner, SOV and KOM cores, oil, and infrastructure 1.

Installed vanilla `history/states/581-Northern Urals.txt` defines the optional northern interior with SOV owner, SOV and KOM cores, chromium/aluminium, and infrastructure 1.

The mod has no local state-history override for IDs 397, 262, or 581.

The package setup/runtime predicates require state 397 to be owned and controlled by KOM, capital, and linked to the protected former-host remnant before runtime validation.

The mandatory current map inspection/render route is unavailable in this runtime, so the prior map artifacts are historical context only and do not constitute a fresh engine receipt.

## Politics, leader, portrait, flag, advisor, and party findings

The four package routes are constitutional, traditional Taiga, popular-council socialist, and emergency military, with package-local party names and ideas.

The exact vanilla `KOM_pavel_murashev` character is male and is not paired with a generated name pool or opposite-gender metadata.

The generic vanilla portrait is not accepted as an attributable 1936 source, and Event 005 `GFX_portrait_KOM_mine_river_committee` at `interface/005_soviet_collapse.gfx:1959` is an institutional committee asset, not a substitute for the exact leader or an Event 006 route identity.

The portrait-worker handoffs `006_iw050_komi_portrait_source_audit_2026_08_14.md` and `006_iw050_komi_portrait_identity_research_2026_08_14.md` remain blocked with no source master, placeholder, DDS, or runtime wiring.

The symbol handoff `006_iw050_komi_symbol_research_2026_08_27.md` remains blocked; no new KOM flag or route symbol was produced.

## Focus, decision, idea, and asset findings

The shared focus route is source-wired with package guards and the five Komi callbacks named in the package note.

The decisions serialize project work through `has_independence_wave_komi_active_package_project`, require package/current-force/capital conditions, and fail closed on package loss, generation rollover, origin end, crisis failure, capital loss, or unsettled former-host conditions where applicable.

The typed mission-pool evidence remains incomplete from the prior decision audit, and no current decision-inspection MCP route is callable.

Seven ideas are localized and use existing shared pictures; no idea icon or generic fallback was added.

The ordinary category has no Komi-specific scripted GUI declaration; no GUI rewrite or render was attempted.

## Starting military, technology, industry, supply, and production findings

The package trigger enforces p50 `mountain_frontier`, five accepted reinforcement flags, current generation, and explicit absence of five forbidden reinforcement flags plus navy/air inheritance.

Vanilla history contributes the ordinary research and technology baseline only; there is no IW-050 technology-tree dependency.

Paid projects consume the existing Event 006 cost palette and reserve one civilian factory through the package-local modifier; no balance target or pre-event surface was changed.

No live force, equipment, manpower, supply, railway, stockpile, or production receipt is available because the release transaction and current map/runtime MCP route were not run.

## AI and probability findings

The four Komi strategy blocks cover survival construction, restraint against a living former host, settled-republic development, and emergency defense.

The mandatory `chaosx_ai_probability_auditor`/HOI4 probability route is unavailable in the installed runtime. `typeof` checks for `mcp__hoi4_agent_tools__hoi4_probability_inspect` and `mcp__hoi4_agent_tools__hoi4_probability_compare` returned `undefined`; earlier direct proxy attempts returned `TypeError: ... is not a function` or the unavailable-to-model MCP error.

Prior read-only evidence recorded `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces` and a named empty evaluation returning `PROBABILITY_SURFACE_EMPTY`; this is not a fresh current receipt and no quantitative AI claim is made.

## Central admission, attestation, Join, and runtime adapter findings

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains no IW-050/KOM branch in the runtime adapter OR list, content-attestation OR list, normal preflight, or scenario/SCN-008 preflight.

`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` contains no IW-050 setup, final-validation, or cleanup dispatch call.

`common/scripted_effects/006_independence_wave_join_effects.txt` contains no IW-050/KOM deterministic Join branch.

The region-05 candidate/load/reservation rows are planner evidence only and must not be treated as central authority.

The parent-owned `independence_wave_iw_050_identity_rights_cleared` flag has no package-local setter; the source/rights decision remains with the parent and portrait/symbol owners.

## Changed file and behavior

Changed file: `common/scripted_effects/006_independence_wave_komi_package_effects.txt`.

Changed identifier: `independence_wave_komi_checkpoint_vanilla_roster`.

Before: `is_independence_wave_komi_package = yes` plus `has_character = KOM_pavel_murashev` set both `independence_wave_komi_roster_checkpoint` and shared `independence_wave_command_roster_ready`.

After: the same writer also requires `has_country_flag = independence_wave_iw_050_identity_rights_cleared`.

This means an exact vanilla character cannot publish package or shared roster readiness until the parent-owned identity/source/rights receipt is present.

When the receipt and exact character are both present, the accepted setup behavior is unchanged.

No tag, state ID, leader, party, focus tree ID, focus route, decision ID, mission ID, idea ID, formable ID, cost, pressure, queue, flag asset, portrait asset, AI weight, force mapping, central registry, attestation, preflight, Join, map, or spreadsheet surface changed.

## Validation and exact limitations

The package source static check after the patch reported balanced braces `214/214`, one checkpoint definition, one rights-guard occurrence, and one package setup caller.

`python -B .tools/audit_event6_country_api.py` passed with 242 broad unique tags, 191 resolved carriers, zero missing, zero duplicates, and a passing IW-031 crosswalk.

`python -B .tools/audit_event6_allocator.py` passed with 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and IW-050 remaining outside central admission.

`python -B .tools/audit_event6_flags.py --strict` passed with 102 registered Event 006 tags and 102 complete flag families.

The fresh callable-tool registry exposes no `hoi4_agent_tools` event, focus, map, technology, or probability functions; `typeof` checks for the corresponding inspect/render/compare names returned `undefined`.

Therefore no fresh Event 006 event inspect/render, shared focus inspect/render, map inspect/render, technology viewer, or probability compare receipt is claimed.

No Hearts of Iron IV process was launched, no map write was made, no asset was generated, and no central file was edited.

## Remaining blockers and next owner

The parent/admission owner must resolve the exact Pavel Murashev source/rights packet or an explicitly accepted institution identity, then route the complete portrait workflow to `chaosx_portrait_creator`.

The parent/symbol owner must resolve whether the installed ordinary KOM ladder is identity/origin-safe after stable re-hash or approve a separately named, dated route symbol; no later 1937+ ASSR symbol may be silently used for the 1936 opening.

The parent/admission owner must reconcile current map/host-remnant proof, central adapter/attestation/normal and SCN-008 preflight, deterministic Join, and runtime adapter evidence before promotion.

The decision owner must complete the typed mission-pool receipt, and the AI owner must rerun the mandatory probability inspect/evaluate/compare workflow when the MCP route is available.

The installed package has no Technology Tree Viewer, so any technology acceptance remains an explicit unresolved limitation even though IW-050 has no package-specific technology surface.

No broad identity redesign, generic fallback, admission shortcut, balance simplification, or unapproved asset was used.

## Skills used

Applied `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui` for the bounded audit, mandatory evidence boundary, decision/focus review, and portrait/flag fail-closed policy.

No skill was created or updated.
