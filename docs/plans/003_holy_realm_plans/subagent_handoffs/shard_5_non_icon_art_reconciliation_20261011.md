# Shard 5 non-icon art reconciliation ? 2026-10-11

Disposition: `needs_user_review` for the eleven inventory-only Holy Realm UI texture names; no production batch was authorized by the accepted asset requirements and current consumers. Existing report, news, super-event, and flag outputs were preserved.

## Scope and evidence

This reconciliation covers non-icon, non-portrait art for Events 003, 007, and 011. The inputs were `.tmp/assets_shard_5_20261011/inventory_rows.json` and `docs/assets/asset_inventory_from_specs_2026-10-11.md`; the accepted owner references were `docs/specs/003_holy_realm_specs/003_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_asset_animation_spec.md`, `docs/plans/003_holy_realm_plans/subagent_handoffs/ui_sweep_2026-10-11.md`, Event 007's spec and follow-up plan, and Event 011's five-part spec and accepted resolution/decision records. Exact inventory receipt evidence for all existing event-picture, super-event, and flag outputs is `.tmp/assets_orchestrator_20261011/restart_03/inventory/numeric_001_040/reviewed_rows.jsonl`.

## Runtime crosswalk and counts

| Owner | Required family | Rows | Inventory/runtime status | Action |
| --- | --- | ---: | --- | --- |
| 003 | report images | 8 | All DDS paths exist in the mod; inventory rows have reviewed-row evidence. Five are marked `present_needs_review`, three `exists_fine`. | Preserve; no regeneration. |
| 003 | super-event images | 9 | All DDS paths exist in the mod; inventory rows have reviewed-row evidence. Seven are marked `present_needs_review`, two `exists_fine`. | Preserve; no regeneration. |
| 003 | flag family | 6 | Great Mandala and Silent Mandala normal/medium/small TGA paths exist in the mod; inventory rows have reviewed-row evidence. | Preserve; no regeneration. |
| 007 | report images | 4 | Three Fury paths and the shared `gfx/event_pictures/004_random_war/report_event_random_war.dds` path exist in the mod; all have reviewed-row evidence. | Preserve; no regeneration. |
| 007 | super-event images | 2 | Both DDS paths exist in the mod and have reviewed-row evidence. | Preserve; no regeneration. |
| 011 | report images | 7 | All DDS paths exist in the mod and have reviewed-row evidence. | Preserve; no regeneration. |
| 011 | news image | 1 | DDS path exists in the mod and has reviewed-row evidence. | Preserve; no regeneration. |
| 011 | super-event image | 1 | DDS path exists in the mod and has reviewed-row evidence. | Preserve; no regeneration. |

Existing visuals marked `present_needs_review` are not candidates for regeneration because this task forbids replacing existing finals and the inventory provides no diagnosed visual defect. The requirement-to-runtime crosswalk therefore contains 38 existing scene/flag rows and zero missing authorized scene/flag rows.

## Inventory-only Holy Realm UI names

The inventory marks these eleven textures missing. They are not a viable art batch: the accepted Holy Realm asset spec describes GUI-dependent panel support assets generically, while the current accepted Event 003 UI sweep says the panel-background options remain unselected and unintegrated. Exact-name search across the accepted Event 003 package and current runtime interface/GFX/scripted-GUI source found no live consumer or registry entry for these names. Their dimensions, composition, sprite names, and consuming surface are consequently unspecified. No template placeholder or substitute art was generated.

- `gfx/interface/003_holy_realm/ledger/holy_realm_ledger_background_a.dds`
- `gfx/interface/003_holy_realm/ledger/holy_realm_ledger_background_b.dds`
- `gfx/interface/003_holy_realm/ledger/holy_realm_ledger_background_c.dds`
- `gfx/interface/decisions/003_holy_realm/bodhi_progress_frame.dds`
- `gfx/interface/decisions/003_holy_realm/final_silence_locked_overlay.dds`
- `gfx/interface/decisions/003_holy_realm/high_defilements_warning_overlay.dds`
- `gfx/interface/decisions/003_holy_realm/mandala_button_hover.dds`
- `gfx/interface/decisions/003_holy_realm/mandala_button_selected.dds`
- `gfx/interface/decisions/003_holy_realm/meditation_charge_progress_frame.dds`
- `gfx/interface/decisions/003_holy_realm/unmet_power_locked_overlay.dds`
- `gfx/interface/decisions/003_holy_realm/wrathful_protection_warning_overlay.dds`

Other missing inventory rows in this owner set are icon or faction-emblem work owned elsewhere and were not included in this art pass. Event 011 has no missing report/news/super-event scene rows; its missing decision-category icons are out of scope. Event 007 has no missing non-icon scene or flag rows.

## Production and receipt status

No image-generation call or final promotion was made because no missing non-icon row had both accepted design authorization and a confirmed live consumer with dimensions/path contract. No art candidates or receipts were created by this worker. The existing inventory receipt is evidence of row review, not evidence that this worker generated or independently approved those existing images. The only uncommitted path produced by this worker is this reconciliation handoff.

Skills used: `chaos-redux-event-assets` and `chaos-redux-frame-animation`. No GFX, GUI, gameplay, localisation, or spreadsheet files were changed, and no commit was created.
