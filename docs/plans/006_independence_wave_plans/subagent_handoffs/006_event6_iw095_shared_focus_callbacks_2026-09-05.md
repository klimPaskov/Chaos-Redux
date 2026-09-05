# Event 006 IW-095 shared-focus callback tranche handoff (2026-09-05)

## Scope and disposition

This tranche wires the existing IW-095 Dahomey package-local callbacks into the shared Event 006 focus tree and gates the three government-settlement decisions behind the matching map-exposure receipt.

Disposition: **implemented for the package-local focus callback surface; central admission remains blocked**. No identity, flag, portrait, formable, adapter, Join, roster, or live-runtime claim is made.

## Changed files and identifiers

- `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt` adds the idempotent `independence_wave_iw095_focus_expose_government_settlements` callback and clears `independence_wave_dah_government_settlements_exposed` during both setup reset and cleanup.
- `common/scripted_triggers/006_independence_wave_first_footprint_package_triggers.txt` adds `has_independence_wave_dahomey_government_settlements_exposed`, which requires the IW-095 package gate and the exposure flag.
- `common/national_focus/006_independence_wave_focus.txt` calls the IW-095 callbacks from the existing shared nodes `independence_wave_prepare_capital_administration`, `independence_wave_restore_regional_communications`, `independence_wave_map_internal_power_centers`, `independence_wave_establish_emergency_revenue`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states`.
- `common/decisions/006_independence_wave_decisions.txt` requires `has_independence_wave_dahomey_government_settlements_exposed = yes` for visibility and availability of `iw095_ratify_civic_compact`, `iw095_restore_council_authority`, and `iw095_authorize_emergency_directorate`.

All callbacks remain origin-gated through the existing `is_independence_wave_dahomey_package` helper and are idempotent where they introduce a receipt flag.

## Intentionally deferred surfaces

The shared `independence_wave_survey_regional_ambition` focus was not given a DAH formable callback because FORM-24 identity and membership evidence is not accepted. No DAH central adapter, publisher, attestation, Join path, portrait, flag, emblem, leader, or formable family was introduced.

## Validation evidence

- `audit_event6_allocator.py --strict` passed with 149 publishers, 126 automatic/high-chaos selectable rows, 138 SCN-ranked rows, 40 runtime adapters, 32 centrally attested rows, 29 compatible reservation groups, and the exact 3/4/5/7/10 automatic ladder with World Collapse at 10.
- `audit_event6_flags.py --strict` passed with 102 registered tags and 102 complete flag families.
- `audit_event6_country_api.py` passed with 242 broad unique tags, 191 resolved tags, zero missing tags, zero duplicates, and the IW-031 crosswalk passing.
- `audit_event6_scenario_matrix.py`, `audit_event6_form16.py`, and `audit_event6_gui_matrix.py` passed their focused checks.
- Post-change `hoi4_focus_inspect` returned `FOCUS_INSPECTED` with 184 focuses, 195 connectors, zero crossings, zero node intersections, zero long connectors, and layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1a0e179ca81b4929b254cf24f93833adf770ef138c262ffbb3ffa8eb4aa2059/79f806c153ae857cef171e993924e3183f495f5789d38d2a77a167d78e2a62d8/focus-inspect.bb7415fdf4d60df7.json`.
- Post-change `hoi4_focus_render` returned `FOCUS_RENDERED` with HTML, SVG, JSON, source-map, and plan artifacts, all tied to layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/afb6d0c839d67acea925bf299868107c6bb301e40395058cbb6eb40ed029dad6/f551db2e68b960da0ba46203749337bf667c7ab048b0e11ca6908d9bac505055/independence_wave_focus_tree.focus.html`.
- The only focus diagnostic was the pre-existing vanilla `continuous_restrict_freedom_desc` localisation warning; the focus validation reported no blocking diagnostics.

## Remaining risks and next owner

IW-095 remains a package-local, fail-closed implementation because central identity and rights, opening flag/emblem, grounded portrait, FORM-24, adapter and Join receipts, Event 012 origin separation, typed probability evidence, and live engine receipts are still open. The parent integration owner must resolve those inputs before central admission or any live completion claim.

No live game, save-load, release, absent-country materialisation, state-transfer, host-survival, or rollback evidence was produced in this tranche.

## Simplifications, omissions, and blockers

No fallback or simplification was introduced. The FORM-24 survey callback and all central admission surfaces remain intentionally omitted pending accepted identity, rights, asset, probability, and engine evidence.
