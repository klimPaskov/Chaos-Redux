# IW-030 Montenegro country-package audit v85 (2026-08-01)

## Scope and disposition

This audit covers only the Event 006 IW-030 Montenegro carrier package (`MNT`, state `105`, reservation group `RG-105`). Event 012 and Fallout surfaces are outside scope.

Disposition: **HOLD / fail-closed; no gameplay patch made**.

The package is a bounded runtime adapter around the registered vanilla `MNT` carrier, not a new country. Its package-local setup, route, decision, lifecycle, AI, force, cleanup, and synchronous roster surfaces are present, but content admission remains intentionally closed. The generic vanilla Kristo Popović portrait is not a grounded real-person asset, the Jovanović and Đukanović source candidates still need rights review and final runtime promotion, and the shared Event 006 focus tree still has blocking geometry diagnostics. A v87 source-research handoff identifies Mitar Martinović as a role-correct replacement lead, but it is evidence-only and cannot be silently assigned to the Popović character. The exact IW-030 dispatch/preflight wrappers are also intentionally absent until those gates clear.

## Evidence snapshot

- `hoi4_map_inspect` on state `105` returned `MAP_INSPECTED`, all bounded map validations true, and no map blockers. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39fe58052c963b634367aa8c68aac9185d01ad2dad3947e56add74a419e1315b/38a297b770587e8aa19a16a43caf17591189ddaf5a67e32e98945380b5987a3a/map-inspect.5821bdb2a798ef97.json`.
- `hoi4_focus_inspect` on `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned `FOCUS_INSPECTED` with `passed: false`, 184 focuses, 223 connectors, 45 crossings, 7 node intersections, 28 long connectors, and 14 blocking diagnostics among 130 diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01272b03475419d8ad051443db071a15438e42da9e3f4125e76173a803c4eaab/98c82b6425b635479a946f526a133b1e4c5056484de2086e779c31c82130ff87/focus-inspect.8b417681564969c4.json`.
- `hoi4_event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics for the bounded query, but workspace analysis was deferred and 2,096 non-blocking issues were reported. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e63ce02e3bffab23ceb6b5a77473816a226201b8b8ad517d6815b357ab5a1e61/7b26dc63912987ac83b94d43cc9ba16c72548b2eb4e8a7b1db0aaeb3275dbfe4/event-lint-3e25e616c431.json`.
- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, and 13 compatible reservation groups. IW-030 remains outside the 14-package attestation set.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` passed with zero external country-definition collisions and zero external identity-surface collisions.
- The installed `hoi4-agent-tools` package exposes no Technology Tree Viewer. A technology render remains unresolved and no technology admission claim is made.
- The concurrent portrait-source handoff `006_iw030_mnt_portrait_source_research_v87_2026_08_01.md` adds an evidence-only Mitar Martinović 1912 source/crop candidate with exact-pixel proof; it does not authorize character identity changes, repainting, DDS/GFX promotion, or runtime wiring.

## Country-package coverage checklist

| Surface | Status | Evidence and identifiers |
|---|---|---|
| Tag registration and identity | Covered for reuse | Vanilla `common/country_tags/00_countries.txt:99` registers `MNT = "countries/Montenegro.txt"`. `common/script_constants/006_independence_wave_country_registry_constants.txt` includes `MNT` in the registered-reuse, selectable-bound, and Balkans/Danube lists. `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:8` requires `original_tag = MNT` and package id `iw_030`. |
| Planner and reservation binding | Registered, not executable | `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:61` binds IW-030 to `RG-105`, MNT, and state 105, but line 66 still calls the legacy `MNT = { is_independence_wave_candidate_tag_available = yes }` dormant-tag flag path. `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt:84` loads MNT, state 105, `balkans_danube`, `mountain_or_frontier`, and `RG-105`. |
| Runtime adapter | Covered locally | `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt:279` sets up IW-030; lines 319, 326, 333, and 378 provide dispatch setup, final validation, and cleanup adapters. |
| Admission/preflight | Intentionally withheld | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10` lists IW-030 only as an adapter. The content attestation at line 72 has no IW-030 branch; runtime preflight at line 94 has no MNT identity branch; scenario preflight at line 196 has no IW-030 branch. `common/scripted_triggers/006_independence_wave_package_triggers.txt` has no `is_independence_wave_exact_package_iw_030_tag_available` wrapper. |
| Country definition and history | Safe vanilla reuse | Vanilla `common/countries/Montenegro.txt` and `history/countries/MNT - Montenegro.txt` remain untouched. Vanilla history supplies capital 105, three research slots, native 1936 technologies, baseline democratic politics, and the three MNT characters. |
| State and map anchor | Covered and validated | Vanilla `history/states/105-Montenegro.txt:3` defines state 105 with chromium 20, aluminium 70, victory points at provinces 9809 and 9821, YUG owner, MNT core, naval bases, and local supplies 3.0. The bounded map inspection passed with no state or network blockers. |
| Politics, parties, and laws | Covered in adapter | `independence_wave_ensure_mnt_baseline_laws` and `independence_wave_initialize_mnt_politics` in `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt` establish the civilian economy, export focus, volunteer-only baseline, four route-compatible party names, popularity, and provisional politics. |
| Leaders and roster | Recruitment wired; provenance incomplete | `events/006_independence_wave.txt:198-223` synchronously recruits `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic` through `chaosx.nr6.350`. `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:32` checks all three characters and Jovanović/Đukanović corps-commander roles. |
| Portraits and gender metadata | Blocking visual gap | Vanilla `common/characters/MNT.txt:9` gives Kristo Popović the generic `GFX_portrait_europe_generic_land_19`; the texture is not an accepted grounded portrait. `interface/_leader_portraits.gfx:8156` maps `GFX_portrait_Blazo_Jovanovic` to `Portrait_Europe_Generic_land_5.dds`, so the named key is also generic. `interface/_leader_portraits.gfx:8501` maps `GFX_portrait_MNT_blazo_dukanovic` to the named Italian DDS. The Jovanović and Đukanović source/crop candidates recorded in `006_iw030_mnt_portrait_source_v68_2026_08_01.md` pass visual/source-linkage checks but remain `needs_user_review` for rights and have no final DDS/GFX promotion. Popović remains source-blocked. The concurrent v87 handoff records Mitar Martinović as a role-correct, pre-1936 candidate with exact source/crop proof, but it requires an explicit character/localisation identity amendment and the full portrait pipeline before it can replace any roster role. No opposite-gender pairing was introduced. |
| Flags and cosmetic identity | Base reuse covered; route variants absent by design | Vanilla MNT base and ideology flags are present and can remain carrier assets. No mod-side flag replacement or cosmetic-tag change is used. No route-specific flag is claimed, so source review is still required before any route identity expansion. |
| Advisors and high command | Intentionally absent | No MNT-specific advisor, high-command portrait, advisor icon, or advisor sprite is referenced by the package. This is a deliberate no-art surface, not an untracked omission. |
| Focus tree | Adapter wired; shared blocker | MNT setup sets `independence_wave_focus_assignment_input = full_framework` at `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt:292`; `common/scripted_effects/006_independence_wave_focus_effects.txt:48-50` calls `load_focus_tree` for `independence_wave_focus_tree`. Vanilla MNT has no dedicated meaningful tree, so no local tree copy is justified. The shared focus diagnostics remain a global admission blocker. |
| Decisions and mission | Covered | `common/decisions/006_independence_wave_montenegro_decisions.txt:10` defines the Montenegrin Mountain Compact category, a 420-day founding mission, and ten costed projects for depots, guards, offices, host ledgers, four governments, durable sovereignty, and the Balkan corridor. The sovereignty decision is an instant one-shot completion effect and lacks the capital-control/active-project guards used by timed projects; this is a review note, not a safe local patch while IW-030 is closed. |
| Ideas and lifecycle | Covered | `common/ideas/006_independence_wave_montenegro_ideas.txt` defines `mnt_divided_mountain_authority`, `mnt_mountain_state_compact`, and four route ideas. Setup, route changes, project failure, and cleanup are linked through the MNT effect and trigger contracts. |
| Formable and ambition hooks | Shared registry only | MNT setup registers the shared ambition family and league route. `independence_wave_mnt_focus_open_balkan_corridor` sets `independence_wave_unlock_formable_discovery` and rewards shared network/ambition values, while `has_prepared_independence_wave_iw_030_package_setup` explicitly requires that `independence_wave_formable_family_registered` remain unset. No MNT-specific formable tag or automatic family registration exists, matching the compact negotiated-expansion contract. |
| Host and diplomacy | Covered in adapter | MNT setup enables negotiation, guarded-frontier, association, and reclamation host routes. The former-host ledger decision requires a living non-war host and capital control, and the package checks the protected former-host state and host relation arrays before setup. |
| Starting force and command | Dynamic contract covered; runtime-dependent | IW-030 loads force mapping p30 and profile `mountain_frontier`, requires five reinforcement pathways, and applies the shared dynamic starting force only after the three-character roster is present. `common/scripted_effects/006_independence_wave_force_effects.txt:554-578` defines the mountain-frontier template and lines 718-734 create divisions at the anchor. No separate MNT OOB file is copied. |
| Technology, industry, supply, and production | Vanilla baseline plus dynamic force | Vanilla MNT history has three research slots and native support/engineers/mountaineers/infantry technologies with DLC-gated early air/armor/naval entries. State 105 provides the recorded resources, infrastructure, factory, naval bases, and local supplies. The adapter does not invent production lines or unsupported technology. Because vanilla `history/countries/MNT - Montenegro.txt:3` references `MNT_1936` but `history/units/MNT_1936.txt` is absent, runtime safety depends on the dynamic-force gate and must remain fail-closed if force materialization fails. |
| AI and playability | Covered in package; admission pending | `common/ai_strategy/006_independence_wave_montenegro.txt:9`, `:25`, `:37`, and `:48` provide mountain survival, host restraint, settled frontier, and emergency guard plans using centralized constants. The package requires the AI profile, force package, lifecycle, route, and focus gates before completion. Live playability cannot be claimed while closed admission gates remain. |
| Localisation and assets | Localisation complete; portrait manifest open | `localisation/english/006_independence_wave_montenegro_l_english.yml` contains the package party, idea, decision, and tooltip keys with UTF-8 BOM. A bounded source-reference scan found no missing package-local keys. No MNT-specific portrait/flag/advisor asset manifest exists because the carrier assets are vanilla reuse or blocked source-review evidence. |
| Cleanup and release safety | Covered locally; not executable through admission | `independence_wave_cleanup_iw_030_montenegro` removes the mission, ten decisions, package ideas, variables, and flags. The adapter final-validation trigger at `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:142` requires setup, force generation, lifecycle, arrays, and network membership. |

## File-surface checklist

Package-owned surfaces present and reviewed:

- `common/script_constants/006_independence_wave_montenegro_constants.txt`
- `common/ideas/006_independence_wave_montenegro_ideas.txt`
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt`
- `common/decisions/006_independence_wave_montenegro_decisions.txt`
- `common/ai_strategy/006_independence_wave_montenegro.txt`
- `events/006_independence_wave.txt` branch `chaosx.nr6.350`
- `localisation/english/006_independence_wave_montenegro_l_english.yml`
- `docs/events/006_independence_wave/montenegro_package.md`

Shared surfaces that remain authoritative and unadmitted:

- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` planner/reservation binding.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt` IW-030 load/weight/reservation effects.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` setup, final-validation, and cleanup dispatch.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` adapter, content-attestation, runtime-preflight, and scenario-preflight gates.
- `common/scripted_triggers/006_independence_wave_package_triggers.txt` exact package wrappers.
- `common/scripted_effects/006_independence_wave_focus_effects.txt` shared full-framework loader.
- `common/scripted_effects/006_independence_wave_force_effects.txt` shared p30 dynamic force implementation.
- `common/script_constants/006_independence_wave_country_registry_constants.txt` registered MNT identity and region membership.

Vanilla reference surfaces intentionally not copied:

- `common/countries/Montenegro.txt`
- `history/countries/MNT - Montenegro.txt`
- `history/states/105-Montenegro.txt`
- `common/characters/MNT.txt`
- `common/national_focus/generic.txt`
- `common/national_focus/yugoslavia.txt`
- vanilla MNT flags and portrait interface definitions.

## Missing or stale admission surfaces

1. Add an exact origin-safe `is_independence_wave_exact_package_iw_030_tag_available` wrapper only after the portrait and shared-focus gates clear; do not grant the dormant candidate flag in the planner as a substitute.
2. Add IW-030 to `has_independence_wave_runtime_package_content_attestation_for_execution_id`, then add the exact MNT identity branch to `is_independence_wave_runtime_package_preflight_ready` and the exact IW-030 branch to `is_independence_wave_scenario_package_preflight_ready` in the parent-owned dispatch file.
3. Replace or supersede the legacy `MNT = { is_independence_wave_candidate_tag_available = yes }` planner gate with the accepted exact wrapper during the same parent-owned admission change.
4. Complete the MNT real-male portrait package: resolve Popović with a defensible source or explicitly decide whether the v87 Mitar Martinović lead warrants a stable character/localisation identity amendment; finish rights review for the Jovanović and Đukanović source candidates; promote final 156x210/DDS/GFX assets only after independent provenance and pixel-identity review. Do not silently place Martinović's face under `MNT_kristo_popovic`.
5. Resolve the shared `independence_wave_focus_tree` geometry diagnostics before claiming IW-030 admission; no local MNT focus patch can safely mask global crossing/intersection/long-connector blockers.
6. Re-run the package, allocator, tag, focus, event, and post-wire visual audits after the above changes, then update the source-of-truth map and event overview before attestation.

## Validation and skipped checks

Meaningful checks run:

- Bounded state-105 map inspection passed with no map blockers.
- Shared focus inspection ran and recorded the 14 blocking geometry diagnostics.
- Bounded `chaosx.nr6.350` event lint returned no blocking diagnostics for the selected query, but it was partial and not a workspace-wide pass.
- Event 006 allocator audit passed and confirmed IW-030 remains outside the attested set.
- Chaos Redux country-tag surface audit passed with zero collisions.
- Package-local localisation key scan found no missing package-local keys; the file begins with UTF-8 BOM bytes `239,187,191`.
- Vanilla references were checked for country registration, history, state 105, characters, portraits, flags, focus-tree availability, and OOB presence.

Skipped or unresolved checks:

- No in-game launch, save, or live gameplay test was run, per repository policy.
- No Technology Tree Viewer render was run because the installed MCP package exposes none.
- No portrait runtime promotion or final rights decision was made because the evidence handoff remains `needs_user_review` or blocked.
- No map write or focus rewrite was attempted because the MNT surface is not the source of the map/focus blockers.

## Patch record and remaining risk

Gameplay files were not patched. This handoff is the only new file from this audit.

No fallback portrait, invented leader, copied history/OOB, new tag, route-specific flag, advisor icon, or MNT-specific formable was added. The missing vanilla `MNT_1936` OOB is an accepted runtime dependency only because the package requires the shared dynamic force to materialize before final validation; admitting the package without that force proof would be unsafe.

The narrowest safe admission path is therefore source/rights closure for the complete non-generic male roster, an explicit decision on the v87 Martinović identity lead if Popović remains blocked, accepted resolution of the shared focus geometry diagnostics, and one parent-owned dispatch/preflight change that adds exact IW-030 wrappers and attestation without reintroducing the dormant-tag flag gate.
