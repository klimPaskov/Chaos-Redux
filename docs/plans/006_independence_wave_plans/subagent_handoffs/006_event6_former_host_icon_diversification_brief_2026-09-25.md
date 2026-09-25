# Former-host route focus icon package — production brief

## Acceptance and scope

**Disposition: implemented.** The user approved the full Event 006 work, and Part 4 of the accepted focus-tree specification requires coordinated route icons that are not all identical. The 2026-09-03 focus-gap inventory found the generic former-host settlement icon repeated across core focus nodes and package overlays. This package gives the twelve former-host route choices distinct art while retaining the shared policy root on its existing icon; the implementation and post-integration MCP evidence are recorded in `006_event6_focus_audit_remediation_2026-09-25.md`.

Produce twelve original, static national-focus icons in the established Event 006 visual family. Keep all gameplay rewards, prerequisites, AI weights, localization, and focus geometry unchanged. The parent owns sprite registration, focus references, runtime integration, final validation, and commit.

## Visual and file contract

- Match the ornate, painterly, compact heraldic treatment visible in `docs/assets/006_independence_wave/contact_sheets/006_icon_focuses_contact_sheet.png` and the installed vanilla national-focus icon contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png`.
- Build each icon for the 94x86 in-game focus canvas, with a transparent unused canvas. Request native transparency in the initial ImageGen call and preserve the alpha channel through processing and DDS conversion.
- Use legible central silhouettes, strong separation at 94x86, period-appropriate materials, and a shared restrained slate, aged-gold, parchment, and muted-red palette. Do not include readable text, letters, numbers, or a background plate that fills the transparent canvas.
- Make all twelve compositions visibly distinct. Do not make a set of recolors or reuse one central silhouette with small prop swaps.
- Keep the source/native output, processed PNGs, final DDS files, prompt notes, contact sheets, and verification notes inside this package directory. Runtime DDS files belong under `gfx/interface/goals/006_independence_wave/former_host_route/`.
- Supply one normal sprite and its exact `_shine` sibling for every row below. The `.gfx` pair will reference the same final DDS; the shine definition follows the existing Event 006 `effectFile = gfx/FX/buttonstate.lua` pattern.

## Accepted focus-to-art mapping

| Focus | Localized title | Sprite | Runtime file | Distinct visual subject |
| --- | --- | --- | --- | --- |
| `independence_wave_open_separation_talks` | Open Separation Talks | `GFX_goal_independence_wave_host_separation_talks` | `goal_independence_wave_host_separation_talks.dds` | Two delegations meet across a treaty table, with an opened sealed agreement between them. |
| `independence_wave_settle_property_and_citizenship` | Settle Property and Citizenship | `GFX_goal_independence_wave_host_property_citizenship` | `goal_independence_wave_host_property_citizenship.dds` | A household key and civic registry ledger, with a family silhouette reflected in a signet. |
| `independence_wave_recognize_the_frontier` | Recognize the Frontier | `GFX_goal_independence_wave_host_frontier_recognition` | `goal_independence_wave_host_frontier_recognition.dds` | Survey hands place a boundary marker on a folded map beneath two joined seals. |
| `independence_wave_fortify_former_host_frontier` | Fortify the Former-Host Frontier | `GFX_goal_independence_wave_host_frontier_fortification` | `goal_independence_wave_host_frontier_fortification.dds` | A concrete border blockhouse and watch post command an open frontier. |
| `independence_wave_establish_armed_coexistence` | Establish Armed Coexistence | `GFX_goal_independence_wave_host_armed_coexistence` | `goal_independence_wave_host_armed_coexistence.dds` | Lowered rifles stand behind a guarded gate, with a controlled signal lantern between the sides. |
| `independence_wave_convene_association_conference` | Convene an Association Conference | `GFX_goal_independence_wave_host_association_conference` | `goal_independence_wave_host_association_conference.dds` | Delegates gather around a circular conference table beneath linked, unmarked banners. |
| `independence_wave_submit_union_question` | Submit the Union Question | `GFX_goal_independence_wave_host_union_question` | `goal_independence_wave_host_union_question.dds` | A ballot drops into a voting urn beside a folded constitutional charter. |
| `independence_wave_document_unsettled_claims` | Document Unsettled Claims | `GFX_goal_independence_wave_host_unsettled_claims` | `goal_independence_wave_host_unsettled_claims.dds` | An archival survey map is weighed by a compass, petition bundle, and evidence seal. |
| `independence_wave_prepare_reclamation_command` | Prepare the Reclamation Command | `GFX_goal_independence_wave_host_reclamation_command` | `goal_independence_wave_host_reclamation_command.dds` | A command baton and field map sit beneath a compact operational pennant. |
| `independence_wave_demand_recognition_or_conflict` | Demand Recognition or Conflict | `GFX_goal_independence_wave_host_recognition_ultimatum` | `goal_independence_wave_host_recognition_ultimatum.dds` | A sealed ultimatum rests across a drawn sword and a sharply divided frontier map. |
| `independence_wave_inherit_successor_ledger` | Inherit the Successor Ledger | `GFX_goal_independence_wave_host_successor_ledger` | `goal_independence_wave_host_successor_ledger.dds` | An abandoned archive shelf holds neglected ledgers beneath a broken former-government seal. |
| `independence_wave_settle_empty_claim` | Settle the Empty Claim | `GFX_goal_independence_wave_host_empty_claim_settlement` | `goal_independence_wave_host_empty_claim_settlement.dds` | A living state's seal closes the final inherited claim ledger beside an empty counterpart chair. |

## Wiring and acceptance checks

The parent registered each base and `_shine` sprite in `interface/006_independence_wave.gfx` and updated only the twelve matching `icon =` lines in `common/national_focus/006_independence_wave_focus.txt`. The root focus `independence_wave_define_former_host_policy` and every package overlay keep their existing references. All twelve runtime DDS files passed exact processed-PNG decode comparison and unique-payload checks; the parent completed the shared-tree inspect, render, and raster review recorded in `006_event6_focus_audit_remediation_2026-09-25.md`, while package-overlay geometry remains unresolved.

The artist handoff must list each source/native-alpha image, processed image, runtime DDS, prompt record, contact sheet, exact dimensions, alpha-channel evidence, DDS decode/round-trip result, and visual uniqueness review. The parent will verify all twelve output files, inspect the contact sheet, confirm every registered texture resolves, and run the mandatory Event 006 focus inspect/render/raster review after wiring. No gameplay or weighted-logic change is part of this icon package.
