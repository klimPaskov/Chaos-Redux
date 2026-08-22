# Event 006 Transcaucasus country-package handoff

Date: 2026-08-22

Scope: IW070 Armenia (`ARM`), IW071 Georgia (`GEO`), and IW072 Azerbaijan (`AZR`) only.

Accepted design: `docs/plans/006_independence_wave_plans/006_iw070_iw072_transcaucasus_source_complete_tranche_addendum_2026_08_05.md` and the accepted Event 006 specifications under `docs/specs/006_independence_wave_specs/`.

## Disposition

Status: **SOURCE-COMPLETE / NO SAFE GAMEPLAY PATCH**.

The three requested packages are complete for the static source admission contract and are registered in the central Event 006 adapter, content-attestation, exact-tag, allocator, dispatch, and cleanup paths. No scoped gameplay source file was changed in this audit. The remaining qualification is runtime evidence: the installed focus, map, and event MCP routes timed out, the project probability-auditor route is not exposed in the installed tool list, and the technology inspection returned a partial/deferred report. Those limitations block stronger engine/runtime claims but do not identify a concrete local source defect to patch.

The user-mentioned `BFX`, `BHX`, and `BJX` tags are not Transcaucasus carriers. They are the separate IW-032 Slavonia, IW-034 Ingria, and IW-036 Courland carriers in `common/country_tags/006_independence_wave_countries.txt`; they were collision-checked and intentionally left untouched.

## Country-package coverage checklist

| Gate | Result | Evidence |
| --- | --- | --- |
| Identity and tag registration | PASS | `common/country_tags/006_independence_wave_countries.txt`; ARM/GEO/AZR are the exact IW070/IW071/IW072 carriers. BFX/BHX/BJX remain separate carriers. |
| Package identity predicates | PASS | `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:9-40` validates original tag, package ID, carrier flag, active origin, and excludes the Soviet-origin collision. |
| History and territory | PASS, static | Vanilla histories use capitals/anchors 230 Armenia, 231 Georgia, and 229 Baku; the accepted map binding records those states as fixed-anchor compact bindings. Runtime map MCP evidence is unavailable because inspect/render timed out. |
| Host and allocator registration | PASS | `common/scripted_effects/006_independence_wave_packages_region_06_effects.txt:129-153,213-215` loads IW070/IW071/IW072 and reserves 230/231/229. Reservation groups are RG-230/RG-231/RG-229. |
| Central adapter and attestation | PASS | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-36,159-190,372-381` registers the three execution IDs, content attestation, and exact ARM/GEO/AZR tag pairs. Dispatch setup/final-validation/cleanup calls the Transcaucasus package at `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:30,62,108`. |
| Leaders and portraits | PASS, vanilla reuse | ARM history supplies Drastamat Kanayan, Hovhannes Kajaznuni, and Grigor Harutyunyan with vanilla portrait GFX; AZR supplies Mir Jafar Baghirov, Mammad Amin Rasulzade, and Gara Garabeyov; GEO's accepted command roster uses its installed vanilla characters including Giorgi Kvinitadze, Noe Zhordania, and George Bagration. No custom character or fallback portrait was invented. |
| Politics and parties | PASS, shared route | Vanilla ARM/GEO/AZR history supplies initial politics/popularity and leaders. The package deliberately uses the shared Event 006 route contract for government changes; no unplanned `set_politics` patch was made. |
| Forces and starting setup | PASS, static contract | `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:147-213` checks each command roster, force mapping/application receipts, four reinforcement pathways, and package-specific regional/naval/air profiles. Force levels are p70=4, p71=4, p72=3 in `common/script_constants/006_independence_wave_force_package_constants.txt:147-149`; the shared force effects provide OOB-derived setup, equipment, manpower, technology, slots, and approved naval/air inheritance. |
| Ideas and ledgers | PASS | `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:11-89` refreshes package ideas and ARM/GEO/AZR ledgers; `common/ideas/006_independence_wave_transcaucasus_ideas.txt` defines crisis, settled, and FORM-16 ideas. |
| Focus loading | PASS, source contract | `common/national_focus/006_independence_wave_focus.txt` supplies `independence_wave_focus_tree`; the package focus contract checks full framework assignment, generic AI, constitutional/popular/emergency/patron route availability, and the ARM/GEO traditional or AZR radical route flags in `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:215-256`. Focus inspect/render MCP calls timed out before returning an artifact. |
| Decisions and missions | PASS, source contract | `common/decisions/006_independence_wave_transcaucasus_decisions.txt` contains one founding mission and four package projects for each carrier, including the exact ARM/GEO/AZR IDs in the source audit. Category visibility is in `common/decisions/categories/006_independence_wave_transcaucasus_categories.txt:8-10`. No decision/mission MCP inspection route is exposed. |
| AI | PASS, source inventory only | `common/ai_strategy/006_independence_wave_transcaucasus.txt:18-141` adds ARM/GEO/AZR survival, reconstruction, settled, and FORM-16 strategy blocks. Probability inspect found no weighted surfaces in this source, so no quantitative balance claim is made. The named `chaosx_ai_probability_auditor` route is not present in the installed tool list. |
| Localisation | PASS, static reference scan | `localisation/english/006_independence_wave_transcaucasus_l_english.yml` and the associated cost localisation cover package categories, missions, decisions, ideas, FORM-16 text, and tooltips. Existing country localisation covers ARM/GEO/AZR and the unrelated BFX/BHX/BJX carriers. |
| Flags and visual assets | PASS, installed family audit | `python .tools/audit_event6_flags.py --strict` reported 102 registered Event 006 tags, 102 complete flag families, and 0 incomplete families. The accepted design reuses installed vanilla ARM/GEO/AZR flags and portraits; no new asset or placeholder was added. |
| Formable and identity collision | PASS, fail-closed | `common/scripted_triggers/006_independence_wave_form16_triggers.txt` enforces exact ARM/GEO/AZR members, anchors, peace, identity clearance, receipts, and route compatibility. `common/scripted_effects/006_independence_wave_form16_effects.txt:114-153,174-245` applies the existing `transcaucasia_unified` identity, member state transfer/cores, postformation setup, rollback, and cleanup. |
| Cleanup | PASS | `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:502-584` clears package flags, force/route/lifecycle receipts, missions, ledgers, and project flags; the shared FORM-16 cleanup removes postformation decisions and rolls back incomplete transactions. |

## File-surface checklist

The audited source surface is:

- `common/country_tags/006_independence_wave_countries.txt` and the ARM/GEO/AZR country shells.
- `common/scripted_effects/006_independence_wave_packages_region_06_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_06_triggers.txt` for allocator loading, weights, reservations, and exact anchors.
- `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt` and `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt` for setup, force, focus, ledgers, decisions, AI receipts, and cleanup.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for central runtime registration and final validation.
- `common/script_constants/006_independence_wave_package_constants.txt`, `common/script_constants/006_independence_wave_force_package_constants.txt`, and `common/script_constants/006_independence_wave_transcaucasus_constants.txt` for package IDs, reservation groups, force levels, profiles, costs, and ledger thresholds.
- `common/scripted_effects/006_independence_wave_force_effects.txt` and the shared force mapping/trigger files for starting units, stockpiles, technology, research slots, and reinforcement pathways.
- `common/national_focus/006_independence_wave_focus.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt` for the shared full focus framework.
- `common/decisions/006_independence_wave_transcaucasus_decisions.txt` and `common/decisions/categories/006_independence_wave_transcaucasus_categories.txt` for missions, projects, and category visibility.
- `common/ideas/006_independence_wave_transcaucasus_ideas.txt`, `common/ai_strategy/006_independence_wave_transcaucasus.txt`, and `localisation/english/006_independence_wave_transcaucasus_l_english.yml` for ideas, AI, and player-facing strings.
- `common/scripted_effects/006_independence_wave_form16_effects.txt` and `common/scripted_triggers/006_independence_wave_form16_triggers.txt` for the accepted Transcaucasian formable and its fail-closed cleanup.

No files in the gameplay surface above were changed by this audit.

## Map, state, host, and collision findings

The accepted static map bindings are ARM/IW070 to state 230 (Armenia), GEO/IW071 to state 231 (Georgia), and AZR/IW072 to state 229 (Baku), all with Soviet former-host state 219 retained as the protected host remnant. The current package binding CSV records these as `ready_if_tag_not_living` fixed-anchor compact bindings and records the exact host remnant condition.

The installed identity-surface audit found no external country-definition or identity collision. BFX/IW032 has no authoritative unique Slavonia state and remains disabled for automatic selection; BHX/IW034 is a route-only Ingria binding on state 195; BJX/IW036 is the separate Kurzeme binding on state 190. None is an ARM/GEO/AZR alias or package reference.

No map rewrite was attempted. `hoi4.map_inspect` and `hoi4.map_render` were invoked for states 229, 230, and 231 with state/railway/port/resource/supply overlays, but both timed out after 180 seconds without an artifact. This is recorded as an engine-evidence limitation, not a source pass for fresh rendered geometry.

## Politics, leaders, portraits, flags, and parties

The vanilla histories were read directly from the installed game directory. ARM uses capital 230 and OOB `AZR_1936` with three research slots and the accepted leader portraits; GEO uses capital 231 and OOB `GEO_1936` with its installed character roster; AZR uses capital 229 and OOB `AZR_1936` with the accepted three-leader roster. The accepted design explicitly reuses these installed vanilla identities and portrait assets, so no fictional leader name, opposite-gender portrait pairing, or source-placeholder substitution is present in this tranche.

## Focus, decision, idea, and asset findings

The package uses the accepted shared focus tree rather than creating a bespoke tree. The ARM/GEO/AZR founding mission and project IDs are all present with decision icons, visibility/availability/cost wrappers, effects, cancellation/timeouts, and AI blocks. Ideas and ledger lifecycle are wired through the package effects. The strict Event 006 flag audit and static localisation scan found no missing required asset family or referenced package text.

The installed Technology inspection route returned `TECH_INSPECTED_PARTIAL` for workspace `mod_chaos_redux_ea3b2d67c2c0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48cb05a824bf5a819fd8672a159d451a9dfedc760578182ce03e4e0eb0bbaf29/baa98180751a4943da28cfa4a88170dcd125bcd35bd81444d47a1057584e90c5/technology-scan-517708b76c53.json`. Its large-workspace helper projections were deferred; the installed package exposes no usable Technology Tree Viewer for a complete tech-tree claim. This tranche does not add a bespoke technology tree.

## AI and probability evidence

The required source-first probability inspection was run against `common/ai_strategy/006_independence_wave_transcaucasus.txt` with the source-only and `ai_strategy_factor` adapter requests. Both returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason: no_weighted_surfaces`, zero candidates, zero unresolved items, and passed source validation. The source-only artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/274cb0c8f3551728fde07e368a1f8e26e5591334405c76f0042eb20b87871eaa/e0f24f9a7f75eaf49d77f2006ac9c1058286b2c85ddbc102913773d5766afd5c/probability-inspect-16dcc44e817b.json`.

There was no weighted-surface patch, so no probability compare was applicable. The named `chaosx_ai_probability_auditor` custom route was not available in the installed tool inventory. Decision AI and focus-selection quantitative scenarios therefore remain unclaimed beyond source inventory.

## Validation performed

The following bounded, read-only validators all exited 0:

- `python .tools/audit_event6_allocator.py` — allocator/adapter/attestation inventory passed.
- `python .tools/audit_event6_form16.py` — ARM/GEO/AZR exact FORM-16 member, consent, mutation, readiness, rollback, and cleanup contract passed.
- `python .tools/audit_event6_country_api.py` — broad/resolved tag API reported missing 0 and duplicates 0.
- `python .tools/audit_event6_flags.py --strict` — 102 registered Event 006 tags, 102 complete flag families, 0 incomplete.
- `python .tools/audit_chaosx_country_tags.py --surface-scan` — protected Event 006/Soviet tags 136, external country-definition collisions 0, external identity-surface collisions 0.

Source review also covered the required offline Paradox wiki pages and installed vanilla documentation for country creation, history, characters, portraits, focuses, decisions, ideas, AI, map/state behavior, localisation, triggers, effects, and cleanup. No live HOI4 launch or save/load test was performed, per repository policy.

## Changed files and remaining blockers

Changed files: only this handoff document. No gameplay, map, shared focus/decision, character, portrait, flag, or allocator file was modified.

No safe source patch exists within the bounded scope. The static source contracts are already present, and patching politics, identities, fallback portraits, map states, focus layout, or fail-closed checks would exceed the accepted design or weaken safety gates.

Remaining evidence limitations are the 180-second timeouts from valid focus inspect/render, map inspect/render, and event inspect/render calls; no exposed decision/mission inspection route; no exposed `chaosx_ai_probability_auditor` route; partial/deferred technology inspection; and no live-game visual or save/load validation. These should be carried into the parent completion report as runtime-evidence blockers rather than silently treated as passes.

Simplifications or omissions made by this subagent: none. No fallback identity, generated portrait, new country, map rewrite, shared-system change, or balance change was introduced.
