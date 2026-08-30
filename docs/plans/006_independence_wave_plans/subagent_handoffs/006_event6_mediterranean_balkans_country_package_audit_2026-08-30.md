# Event 006 Mediterranean and Balkan country-package audit

Date: 2026-08-30

Owner: `event6_country_tranche_med`
Scope: IW-013, IW-014, IW-015, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-041, IW-044, and IW-045.

## Verdict

No gameplay or package source patch is safe from this audit. Seventeen scoped packages are already source-attested and centrally admitted under the current Event 006 contract, while IW-013/NAV and IW-015/GLC are intentionally adapter-only and fail closed. Their unresolved state/identity/rights issues require an authoritative design decision, not a local wiring change.

No gameplay files, map files, assets, localisation, or registries were changed. Before and after behavior is therefore identical. The only change from this tranche is this audit handoff.

## Country-package coverage checklist

| ID | Tag | Current anchor and host | Admission | Audit result |
| --- | --- | --- | --- | --- |
| IW-013 | NAV | Installed state 792; SPR host; research/matrix baseline still says 172 with extended 806 | Adapter-only, fail-closed | State crosswalk, Basque compact-flag identity, and portrait/source-rights clearance are unresolved. Do not promote. |
| IW-014 | CAT | State 165; SPR host | Source-attested and admitted | Package source is complete at the current contract; no local defect found. |
| IW-015 | GLC | State 171; SPR host | Adapter-only, fail-closed | Castelao is independently recruited, defined as a corps commander, and created by vanilla as country leader; identity transfer or replacement is unresolved, and portrait/source rights remain caveated. Do not promote. |
| IW-017 | COR | State 1; FRA host | Source-attested and admitted | Exact state/owner/controller/capital/host gate and package lifecycle are present; no local defect found. |
| IW-018 | ARX | State 114; ITA host | Source-attested and admitted | New tag shell, package setup, council/command roster, flag, portraits, localisation, decisions, focus route, and cleanup are wired; no local defect found. |
| IW-019 | ASX | State 115; ITA host | Source-attested and admitted | New tag shell, package setup, council/command roster, flag, portraits, localisation, decisions, focus route, and cleanup are wired; no local defect found. |
| IW-023 | TRA | State 84 with optional 76; ROM host | Source-attested and admitted | Vanilla Maniu leader reference, exact package gate, force mapping, shared focus/decisions, AI, and cleanup are present; typed AI evidence remains unavailable. |
| IW-024 | AXX | State 82 with optional 764; ROM host and YUG optional | Source-attested and admitted | New tag shell, Banat presidium/Otto Roth roster, researched alternate-history flag, shared route, force mapping, and cleanup are present; typed AI evidence remains unavailable. |
| IW-026 | MAC | State 106 with optional 970; YUG host | Source-attested and admitted | Existing carrier and Vardar-presidium package surfaces are wired; no local defect found. Typed AI evidence remains unavailable. |
| IW-027 | BAX | State 184; GRE host | Source-attested and admitted | New tag shell, Thrace council/Hristo roster, researched alternate-history flag, shared route, force mapping, and cleanup are present; typed AI evidence remains unavailable. |
| IW-028 | BBX | State 185 with optional 805; GRE host and ALB optional | Source-attested and admitted | New tag shell, Epirus council/Spyros roster, researched 1914 Northern Epirus flag reconstruction, shared route, and cleanup are present; no local defect found. |
| IW-029 | BOS | State 104 with optional 804; YUG host | Source-attested and admitted | Drina-council roster, package lifecycle, shared route, decisions, AI, and cleanup are present; typed AI evidence remains unavailable. |
| IW-030 | MNT | State 105; YUG host | Source-attested and admitted | Vanilla and Event 006 Montenegro leader/portrait wiring, package lifecycle, and cleanup are present; source-placeholder disclosures remain in the existing handoff. |
| IW-031 | KOS | Current installed state 802; YUG host | Source-attested and admitted | Explicit 802 crosswalk, Ferhat Draga/Miladin Popovic/Shaban Polluzha roster, package lifecycle, and cleanup are present; crosswalk validator passes. |
| IW-038 | RUT | State 73; CZE host | Source-attested and admitted | Ruthenia package, vanilla Augustin Voloshyn reference, sourced-placeholder portrait set, decisions, shared route, and cleanup are present. |
| IW-040 | KUB | State 234; SOV host | Source-attested and admitted | Vanilla Ivanis/Vasily Nikolaevich reference, Don-Kuban package, force mapping, generated route flags, and receipt guard are present. |
| IW-041 | CRI | State 137; SOV host | Source-attested and admitted | Vanilla Ilyas Tarkhan reference, Crimean Tatar route, package lifecycle, and cleanup are present. |
| IW-044 | TAT | State 249; SOV host | Source-attested and admitted | Vanilla Alexandr Alemasov reference, Middle-Volga package, force mask, shared route, and cleanup are present. |
| IW-045 | BSK | State 651; SOV host | Source-attested and admitted | Vanilla Yakov Bykin reference, scoped portrait override with cleanup, flags, founding-mission receipt guard, shared route, and cleanup are present. |

The current central contract is consistent with this result: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains adapters for the scoped IDs, but content attestation and deterministic Join contain the seventeen admitted IDs and intentionally omit NAV and GLC.

## File-surface checklist

The following surfaces were inspected and are present for the admitted packages unless noted in the blocker section.

- Tag registration and new country shells are in `common/country_tags/006_independence_wave_countries.txt` and `common/countries/006_independence_wave_ARX.txt`, `006_independence_wave_ASX.txt`, `006_independence_wave_AXX.txt`, `006_independence_wave_BAX.txt`, and `006_independence_wave_BBX.txt`; reused vanilla carriers are not re-registered.
- State and host bindings are in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` and `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`, with vanilla histories providing the carrier capitals and starting ownership.
- Package effects and triggers are split across `common/scripted_effects/006_independence_wave_*_package_effects.txt` and `common/scripted_triggers/006_independence_wave_*_package_triggers.txt`, with central dispatch in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`, `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- Join, preflight, cleanup, roster checkpoint, and lifecycle dispatch are present in `common/scripted_effects/006_independence_wave_join_effects.txt` and `common/scripted_effects/006_independence_wave_effects.txt`.
- Regional decisions are present in `common/decisions/006_independence_wave_iberian_decisions.txt`, `006_independence_wave_mediterranean_decisions.txt`, `006_independence_wave_balkan_decisions.txt`, `006_independence_wave_frontier_decisions.txt`, `006_independence_wave_siberian_decisions.txt`, `006_independence_wave_karelia_crimea_decisions.txt`, and `006_independence_wave_bashkiria_mari_decisions.txt`.
- The shared focus route is in `common/national_focus/006_independence_wave_focus.txt`; the inspected tree is assigned through the package/runtime path and no package-specific tree is missing from this tranche.
- Shared ideas and AI strategy registration are in `common/ideas/006_independence_wave_ideas_registry.txt` and `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`.
- Character and recruitment wiring is in `common/characters/006_independence_wave_characters_registry.txt` and `history/general/006_independence_wave_character_recruitment_registry.txt`.
- Localisation is split across the regional `localisation/english/006_independence_wave_*_l_english.yml` files, including the Mediterranean, Balkan, Kosovo, Ruthenia, Frontier, Karelia/Crimea, Tatarstan, and Bashkiria/Mari files.
- Flag registration is in `interface/006_independence_wave.gfx`; portrait registration is in `interface/006_independence_wave_portraits_registry.gfx`; runtime flag and portrait files are present for the inspected custom packages, with vanilla portrait reuse for KUB, CRI, and TAT.

## Missing, stale, or blocked surfaces

### Map and state setup

The nineteen selected state IDs have map definitions, province geometry, state/region membership, adjacency, supply, railway, coast, port, resource, and building records sufficient for read-only inspection. No map rewrite is justified.

NAV is the only concrete scoped map-binding discrepancy: the current installed runtime and binding use state 792, while the public research/matrix row still uses state 172 and mentions 806 as an extension. This must be reconciled in the source-of-truth design/binding documents before any gameplay change.

KOS is correctly bound to current installed state 802 in `006_current_installed_map_package_bindings.csv`; the crosswalk validator passes. No state 802 replacement or map edit is needed.

### Politics, leaders, portraits, flags, advisors, and parties

Shared package setup supplies the scoped party, ideology, law, popularity, stability, war-support, leader, command, and cleanup surfaces, and no missing party or advisor identifier was found for the admitted packages.

GLC has a blocking duplicate real-person identity: `history/general/006_independence_wave_character_recruitment_registry.txt` recruits `GLC_independence_wave_alfonso_daniel_castelao`, `common/characters/006_independence_wave_characters_registry.txt` defines that same person as a corps commander, and vanilla `history/countries/GLC - Galicia.txt` creates Castelao as the country leader. An approved transfer/replacement decision is required before admission.

NAV and GLC custom portraits are wired and runtime files are present, but both carry unresolved source-rights or identity clearance in their existing handoffs. They cannot be treated as cleared final assets for admission. Admitted packages retain their existing sourced-placeholder or researched-flag disclosures; no unapproved fallback was added.

No opposite-gender portrait/name pairing or institutional-body personal-name misuse was found in the inspected Event 006 roster. No new portrait or flag production was authorized by this audit.

### Focus, decisions, ideas, and assets

The admitted packages use the shared `independence_wave_focus_tree`, regional decisions, shared ideas, central event icons, and package-specific flag/portrait wiring. Source inspection found no missing package-local focus assignment, decision identifier, idea identifier, localisation key, flag family, or portrait registration that can be safely fixed locally.

The focus MCP inspection found 184 focuses, 195 connectors, zero crossings, zero node intersections, and zero long connectors. It reported 213 spacing warnings caused by existing dense fixed/relative placement and one unrelated vanilla `continuous_restrict_freedom_desc` localisation warning; neither is a scoped country-package defect.

### Starting military, technology, industry, supply, and production

The force-package mapping, package setup effects, starting roster checkpoint, state bindings, and cleanup paths are present for all seventeen admitted IDs and do not show a scoped source mismatch. This audit did not alter armies, templates, equipment, production, manpower, industry, supply, ports, or resources.

No custom Event 006 technology or doctrine is introduced by these country packages. The installed Technology Tree Viewer route is unavailable: both narrow technology inspections and the summary render returned `SCAN_BYTE_LIMIT`. Technology coverage and balance are therefore not claimed.

### AI and playability

Package AI strategy references and shared focus/decision behavior are wired for the admitted packages. The direct probability source-discovery pass reported `discoveryReason=no_weighted_surfaces` for `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, with zero discovered candidates.

The mandatory `chaosx_ai_probability_auditor` route was not available in the installed tool inventory, so no evaluate, sweep, sequence, seeded simulation, or before/after probability comparison was possible. No quantitative AI, MTTH, score, or survival claim is made. Typed AI evidence remains a follow-up requirement for the packages called out in existing handoffs.

## Read-only MCP evidence

- Event scan/render of `events/006_independence_wave.txt` completed with status `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` at revision `903a0ec1e1c79d4d289cdfc3a91862032b64986b4a47ff563fda9057305390cb`. The event graph reported helper/lifecycle analysis deferred and eight global blocking diagnostics, but no explicit scoped Event 006 blocker. Useful render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52456ba58b6764124d2a3cf9e24084746efc734420738dfe5c3a7c78bdcf5fb8/0ae0dae2e51b0d54ebf81805b0838c22689826d68383a6894af6cd58cf8e01e2/event-overview-903a0ec1e1c7-manifest.json`.
- Focus inspection/render completed for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, with no blocking diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f8c036172bfdf2bf0a6a0740ce745cf0fe530f02291661687a11f272a1fe81e/3ab1256ad9b8770ec51eea5ae820b6f0197f50cbd1a395d1d0dafd7ba2e6414e/focus-inspect.00e7dc1995105549.json`.
- Map inspection covered states 1, 73, 82, 84, 104, 105, 106, 114, 115, 137, 165, 171, 184, 185, 234, 249, 651, 792, and 802. State geometry and network checks passed; the global package report retained unrelated invalid building/port position diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5a7c75a08f3d3a6ca9ba303fa458c36b2cc649181efcbe7418f7589ec49d4f5/f03eaddf2744519f817ebc3eb2986563f69fcccbef67403e88ca93dc7601e0a8/map-inspect.9f06d224130002c1.json`.
- Map state render with coastlines, ports, victory points, resources, state buildings, supply nodes, and railways completed in offline representation with no render validation failure: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11da464a58a00f392d20160c03b0af4a5e89f3dc88629a12e57291b26e12dba/7a9e82b6d7270d7c6c58e3cc133b326b6bbbd4b515e6450b7725e6ef14f1436b/map-state.png`.
- The shared `independence_wave_status_window` GUI completed read-only inspection and render across normal, warning, long-text, and missing-localisation states at 1920x1080 and 1280x720. Validation passed with nonblocking overlap, clipping, and animated-static-fallback warnings. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16261efe627c05f365d7b70a6d492ad10cac782c734e1173814ffa36793ef92a/775bbfefa68231802818996ac7e714b4b94d06e5dd4621c702e14e87a56fc4ab/gui-inspect.c6a1b8d8ac3c974f.json`.
- Probability source discovery completed for `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` with no weighted surfaces: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f49820b5848f94844783da35973bc6e87531f55fcafa8d8ae13fe24cdd2a9e2/dfdcf5cf9c6cd0142c4cee19ae593cd80090d225999aca6abf9e9024a6c0b734/probability-inspect-c9a81863c89a.json`.

The Event and map MCP reports also retained unrelated global diagnostics, including 2,655 invalid building/port position errors and an unrelated BOM error in `localisation/english/025_alien_technology_in_antarctica_l_english.yml`. These were not changed because they are outside this tranche.

## Focused validators

All commands exited 0 on 2026-08-30.

```text
python -B .tools/audit_event6_allocator.py
  passed: 40 runtime adapters, 32 content-attested packages, 29 reservation groups, 161 unattested selectable rows, and adapter-only fail-closed IW-013/IW-015/IW-043/IW-058/IW-093/IW-098/IW-177/IW-179.
python -B .tools/audit_event6_country_api.py
  passed: 242 unique tags, 191 resolved carriers, 0 missing, 0 duplicates, and IW-031 state crosswalk pass.
python -B .tools/audit_event6_flags.py --strict
  passed: 102 registered Event 006 tags and 102 complete flag families.
python -B .tools/audit_event6_scenario_matrix.py
  passed: all 32 SCN-008 cells and 8 edge cases.
python -B .tools/audit_event6_form16.py
  passed: ARM/GEO/AZR exact member, consent, refusal, mutation, rollback, cleanup, and readiness cases.
python -B .tools/audit_event6_gui_matrix.py
  passed: five tabs, recognition/dependency/league/formable frame coverage, cleanup, and matrix semantics.
```

No map write was attempted, so there is no map rollback or post-apply receipt to report. Live game setup, save/load, and in-game playability remain user-owned validation surfaces.

## Simplifications, omissions, and blockers

No simplification or unapproved fallback was made. In particular, this audit did not promote NAV or GLC, invent a leader or flag, replace a duplicate historical identity, generate a portrait, alter the shared focus tree, change map ownership, or make an unsupported AI/balance claim.

Parent follow-up is to reconcile the authoritative NAV state (172 versus installed 792, with 806 extension), clear NAV Basque flag/portrait rights, resolve GLC Castelao identity ownership and portrait rights, preserve the current seventeen-package admission set, and obtain the unavailable typed probability-auditor and technology-viewer evidence before claiming a stronger package completion state.

Skills and references used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui`; required offline Paradox wiki pages, vanilla HOI4 documentation, vanilla country/history/character/focus/flag/AI files, current Event 006 specs/matrices/research, and existing package handoffs were reviewed before this audit.
