# Event 006 IW-023 Transylvania Regional Focus Callback Audit

**Disposition:** `implemented` for the scoped IW-023 callback audit; the full REG-03 regional overlay remains `partial`.

**Acceptance basis:** The user explicitly approved the accepted Event 006 specification and implementation scope on 2026-09-25. This audit applies that decision to the IW-023 adapter and REG-03 coverage boundary only.

**Scope:** Read-only review of the IW-023 Transylvania callback on the existing shared overlay, its package and carrier gates, its current settlement lifecycle refresh, the accepted REG-03 criteria, and the supplied final MCP layout evidence. No gameplay, focus, localisation, AI, or other source was changed.

## Coverage result

| Coverage slice | Result | Evidence |
| --- | --- | --- |
| IW-023 / TRA adapter criterion | **Met.** The existing `independence_wave_overlay_address_former_host` focus has an exact IW-023-gated completion callback. | `common/national_focus/006_independence_wave_focus.txt:3488-3512`; callback `independence_wave_tra_focus_arbitrate_danube_border` in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt:2779-2789`. |
| REG-03 full regional overlay | **Partial.** The callback supplies a package-gated reward adapter, not the country-specific focus group and wider overlay content specified for highlighted packages. | Part 4 requires regional overlay differences including one or more country-specific focus groups (`006_independence_wave_spec_part_4_focus_tree_architecture.md:649-665`); Part 5 defines the additional country-specific focus group for Level 2 packages (`006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:52-61`). The baseline audit defines an adapter as coverage evidence but still classifies REG-03 as partial (`006_event6_regional_overlay_coverage_audit_2026-09-25.md:5,31`). |

The callback therefore clears the narrow IW-023 adapter criterion. It does not establish completion of the REG-03 overlay or of Event 006.

## Source findings

`is_independence_wave_tra_package` requires `original_tag = TRA`, active Event 006 package content, and package id `IW-023` (`common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:1197-1202`). The shared focus invokes the TRA reward only under that trigger, and the callback repeats the same gate (`common/national_focus/006_independence_wave_focus.txt:3501-3512`; `common/scripted_effects/006_independence_wave_balkan_package_effects.txt:2782-2788`). Other packages cannot enter the callback through this call site.

The adapter is limited to the reviewed additive carrier route. IW-023 setup selects `additive_overlay` when `austro_hungarian_releasable_focus` is loaded and keeps the existing full-framework fallback otherwise (`common/scripted_effects/006_independence_wave_balkan_package_effects.txt:3002-3011`). The assignment helper sets additive-overlay ownership only after `can_attach_independence_wave_additive_focus_carrier` succeeds; that predicate requires active package content, the registered carrier, the IW-023 lifecycle receipt, and the current Austro-Hungarian tree (`common/scripted_effects/006_independence_wave_focus_effects.txt:63-75`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:70-81`). The carrier retains its existing focus tree and imports the shared overlay (`common/national_focus/austro_hungarian_releasable_shared.txt:29-38`). The shared focus itself requires `can_use_independence_wave_additive_focus_overlay` (`common/national_focus/006_independence_wave_focus.txt:3497-3499`), so the full-framework fallback does not expose this additive-overlay node.

The prepared IW-023 setup check now accepts the selected assignment through `has_independence_wave_generic_focus_contract` (`common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt:1302-1323`). Its full-framework branch verifies the Event 006 tree and assignment flags; its additive branch verifies the overlay flags and reviewed carrier predicate (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-67`). Thus the prepared-package gate is consistent with both the retained full-framework fallback and the valid additive-carrier route.

The value and idea refresh sequence is consistent with the established TRA lifecycle. Setup initializes both ledgers and refreshes their ideas before setting `independence_wave_iw_023_lifecycle_initialized`, then assigns the carrier (`common/scripted_effects/006_independence_wave_balkan_package_effects.txt:2994-3011`). The callback applies the same centralized `standard_gain` to frontier cohesion and federal legitimacy. `independence_wave_change_tra_settlement_values` adds those deltas, clamps both ledgers to the shared minimum and maximum, and invokes the lifecycle refresh (`common/scripted_effects/006_independence_wave_balkan_package_effects.txt:2742-2788`). The refresh removes both mutually exclusive settlement ideas, re-adds the stable or divided state from the current settlement trigger, and updates the stabilization flag (`common/scripted_effects/006_independence_wave_balkan_package_effects.txt:2742-2756`). No source defect was found in this bounded path.

The package-specific completion tooltip reports the same centralized gain for both named ledgers (`independence_wave_tra_overlay_address_former_host_tt`, `localisation/english/006_independence_wave_focus_l_english.yml:418-421`). The focus reuses its existing `GFX_goal_independence_wave_former_host_settlement` icon, defined in `interface/006_independence_wave.gfx:21`; no icon or AI weight change is part of this adapter. No reward/localisation mismatch or icon-reference defect was found within scope.

`docs/events/006_independence_wave/transylvania_package.md:5-11` describes the additive carrier, full-framework fallback, callback, and limits consistently with source. The callback performs no territorial transfer, claim, or maximal-border action.

## Remaining coverage defect

The accepted regional design calls for more than this single reward adapter: Part 4 specifies the regional overlay themes and package-specific focus group coverage for highlighted packages, while Part 5 defines the additional country-specific focus group for Level 2 packages. The present IW-023 reward advances the arbitration/frontier ledgers through one common shared focus; it is not that country-specific group. Keep REG-03 classified as `partial` until the wider accepted coverage is implemented and audited. This finding does not reassess the other REG-03 packages.

## MCP evidence and validation limits

The supplied parent evidence for final source revision `1de285d388acf794b8b10842e22db2d8c0bfc81f4b154691dd9c9e2d30e41242` records `FOCUS_INSPECTED` and `FOCUS_RENDERED`, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, 184 focuses, 196 connectors, zero crossings/intersections, and one existing ten-column connector warning. The supplied notes identify the vanilla continuous-focus localisation warning and inline inventory truncation as unrelated. I used this supplied final-revision evidence and did not rerun MCP; no artifact URI was included in the supplied evidence.

No AI probability audit was run because this bounded callback adds no weight or probability-bearing modifier and the focus weights were out of scope. No live-game validation was performed. The source review and supplied layout result do not prove runtime focus visibility or reward execution in a live campaign.

## Files reviewed

- `common/national_focus/006_independence_wave_focus.txt` — `independence_wave_overlay_address_former_host`.
- `common/scripted_effects/006_independence_wave_balkan_package_effects.txt` — `independence_wave_tra_focus_arbitrate_danube_border`, `independence_wave_change_tra_settlement_values`, `independence_wave_refresh_tra_settlement_lifecycle`, and `independence_wave_setup_iw_023_transylvania`.
- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt` — `is_independence_wave_tra_package` and `has_prepared_independence_wave_iw_023_package_setup`.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt` — `has_independence_wave_generic_focus_contract` and `can_attach_independence_wave_additive_focus_carrier`.
- `localisation/english/006_independence_wave_focus_l_english.yml` — `independence_wave_tra_overlay_address_former_host_tt`.
- `docs/events/006_independence_wave/transylvania_package.md`.
- Accepted design: Part 4 focus architecture, Part 5 package/regional overlay contract, REG-03 matrix row, and IW-023 package research row.
- Prior evidence: `006_event6_regional_overlay_coverage_audit_2026-09-25.md` and `006_event6_transylvania_focus_carrier_preservation_2026-09-25.md`.

No implementation or documentation follow-up beyond the remaining REG-03 coverage gap is identified by this bounded audit.
