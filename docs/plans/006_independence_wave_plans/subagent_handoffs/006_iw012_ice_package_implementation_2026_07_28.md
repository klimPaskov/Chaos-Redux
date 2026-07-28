# IW-012 Iceland package implementation handoff

Date: 2026-07-28

## Scope and disposition

This handoff records the parent-owned IW-012 implementation tranche for Event 006, Independence Wave. IW-012 reuses the registered vanilla `ICE` tag and remains an additive Event 006 package; no new country tag, country history file, state file, flag, portrait, advisor icon, or OOB was added. The whole Event 006 goal remains **HOLD / PARTIAL** because live allocator, save/load, synchronized release, force materialization, AI probability, scenario transaction, GUI, achievement, and super-event evidence remain open.

## Changed gameplay surfaces

- `common/script_constants/006_independence_wave_ice_constants.txt` centralizes the five ICE ledgers, project costs, thresholds, durations, route politics, and documented integer AI strategy weights. The harbour deadline is 1,440 days; the six serialized project path totals 1,230 project-days, leaving a 210-day margin.
- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt` proves the exact ICE origin, state-100 anchor, living former host, vanilla command roster, additive carrier, p12 force mapping, route hooks, visible ledgers, ideas, cleanup, and FORM-02 readiness. The active-project helper intentionally checks only the six serialized projects, so the survival mission does not deadlock project starts.
- `common/scripted_effects/006_independence_wave_ice_package_effects.txt` owns setup, visible-ledger changes, project failure, host settlement, route politics, route locks, p12 force setup, AI flags, final validation, and cleanup. Existing vanilla Sveinn Björnsson and Björn Sveinsson Björnsson are promoted; no dynamic character recruitment is used.
- `common/decisions/006_independence_wave_ice_decisions.txt` and `common/decisions/categories/006_independence_wave_ice_categories.txt` provide the harbour mission and six concrete-cost projects for shipping registers, municipal government, coastwatch, compact negotiation, former-host settlement, and armed neutrality. No political-power store, passive checklist, free-unit loop, or reward dust was introduced.
- `common/ideas/006_independence_wave_ice_ideas.txt` supplies five lifecycle and route ideas using existing Event 006 icon art.
- `common/ai_strategy/006_independence_wave_ice.txt` adds supported vanilla AI strategy types with integer weights and a fixed Danish former-host target where the engine requires a target token; vanilla ICE plans remain authoritative.
- `common/national_focus/iceland.txt` is an exact vanilla `iceland_tree` snapshot with only explicit additive `shared_focus` imports. The normalized body comparison against the installed vanilla file is `BODY_CONTENT_MATCH=True`; the only raw difference is one final LF at EOF. It imports the complete eight-focus Event 006 overlay and four ICE route consumers without altering vanilla focus blocks, history, characters, flag, or Nordic shared focus.
- `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, and the Event 006 package dispatch/registry triggers and effects now carry IW-012 through setup, final validation, cleanup, automatic readiness, scenario preflight, and content attestation.
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt` rejects vanilla Nordic identity flags before Event 006 FORM-02 membership, preserving vanilla Nordic League precedence.

## Documentation and asset evidence

- `docs/events/006_independence_wave_iw012_ice_package.md` is the package source-of-truth document and records preservation, ledgers, projects, host/league/formable behavior, force mapping, focus carrier, asset reuse, and remaining live evidence.
- `docs/assets/006_independence_wave/iw012_ice_package_2026_07_28/manifest.md` records that IW-012 reuses approved vanilla ICE historical assets and creates no Event 006 advisor icons. The original-size portrait shelf remains flat at `docs/assets/006_independence_wave/portraits_generated_png`; it contains 54 source-derived masters directly in one directory, no nested folders, and no normalized 156×210 PNGs.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` now list IW-012 in the current eleven-package compile-time attestation set and retain the whole-event HOLD / PARTIAL disposition.

## Audit evidence

- `python .tools/audit_event6_allocator.py` passes with 149 publishers, 126 automatic/high-chaos selectable rows, 138 SCN-ranked rows, eleven attested packages across ten compatible groups, the RG-RHINE-SAAR pair capacity of two, automatic wave counts 3/4/5/7/10, World Collapse count 10, all scenario intensities and types, and Event 005-first joint ordering.
- The country-package retry audit is a static **PASS** for IW-012 admission and confirms the exact package wrapper, dispatch/readiness links, supported integer AI profile, exact vanilla focus snapshot with twelve shared imports, Nordic precedence guard, zero tag collisions, and no advisor/portrait additions. Live release, focus visibility in the engine, AI activation, force materialization, and rollback remain pending.
- The decision/mission audit is a static **PASS** after the project-only serialization guard, 1,440-day survival deadline, 1,230-day project path, four route-focus imports, and FORM-02 Nordic guards. No remaining ICE cost, threshold, cancellation, or cleanup blocker was found.
- The final focus retry audit is a bounded **PASS** for the exact vanilla carrier, all twelve imports, route prerequisites/exclusions, maturity route-lock, localization, and icon coverage, with a separate **HOLD** for live shared-focus rendering, route-aware AI probabilities, and dynamic former-host AI targeting. `hoi4.focus_inspect` and `hoi4.focus_render` still ignore `shared_focus` nodes in their metrics and report vanilla-source sprite diagnostics; those tool limitations and baseline diagnostics are not claimed as a clean focus validation.
- Scoped Clausewitz brace/depth, constants-reference, AI-type, localization-BOM/key, and exact-vanilla-snapshot checks pass. No Event 006 advisor icon reference was added. Installed-tag collision evidence remains zero collisions.

## Remaining blockers

No fallback was used for IW-012. The package is compile-time admitted, but the parent must still obtain live allocator and synchronized host-survival evidence, save/load cleanup proof, scenario intensity/type transaction proof, force materialization proof, AI probability/balance evidence, Event Details/GUI evidence, achievement evidence, and whole-event completion-audit reconciliation before claiming Event 006 complete.
