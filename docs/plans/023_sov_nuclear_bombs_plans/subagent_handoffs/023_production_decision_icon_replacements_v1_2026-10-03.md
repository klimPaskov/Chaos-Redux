# Event 023 decision-icon replacement production handoff

Date: 2026-10-03.

## Result

Produced six original, separately prompted 33x32 RGBA decision-icon candidates under docs/assets/023_sov_nuclear_bombs/decision_icon_replacements_v1/. Each has a source lineage record, processed PNG, candidate DDS, decoded RGBA round trip, native neutral-background preview, 4x nearest-neighbour preview, 4x smooth preview, and a contact-sheet row. All six remain needs_user_review; no runtime asset or GFX registration was changed.

The parent explicitly authorized new icon generation and replacement for these exact six decision ids and locked their basenames, sprites, consumer, paths, and canvas. No old generation prompts were reconstructed.

## Exact consumer and reference findings

The active consumer is interface/023_sov_nuclear_bombs.gfx. Existing sprite registrations are GFX_decision_sov_nuclear_decision_accounting, GFX_decision_sov_nuclear_decision_storage_hardening, GFX_decision_sov_nuclear_decision_reactor_construction, GFX_decision_sov_nuclear_decision_device_assembly, GFX_decision_sov_nuclear_decision_delivery_preparation, and GFX_decision_sov_nuclear_decision_command_exercise. They retain the locked runtime folder gfx/interface/decisions/023_sov_nuclear_bombs/ and exact basenames.

The canonical decision contact sheet was inspected before the individual Vanilla HOI4 reference. CATALOG.md records decision_generic_intelligence_operation.png as a 33x32 Vanilla HOI4 source. The installed vanilla GFX definition and DDS were inspected; the DDS decodes to 33x32 legacy BGRA32 and is pixel-identical to the canonical reference PNG. The decision-category background template was not applicable to ordinary decision icons, and no visual component was used.

## File inventory

The package manifest at docs/assets/023_sov_nuclear_bombs/decision_icon_replacements_v1/manifest.md records the per-file hashes, prompts, candidate lineage, crop bounds, scale, alpha bounds, DDS strict-header evidence, visual review, consumers, and status.

The new source PNGs are source_png/sov_nuclear_decision_accounting.png, source_png/sov_nuclear_decision_storage_hardening.png, source_png/sov_nuclear_decision_storage_hardening_v2.png, source_png/sov_nuclear_decision_storage_hardening_v3.png, source_png/sov_nuclear_decision_storage_hardening_v4.png, source_png/sov_nuclear_decision_reactor_construction.png, source_png/sov_nuclear_decision_device_assembly.png, source_png/sov_nuclear_decision_delivery_preparation.png, and source_png/sov_nuclear_decision_command_exercise.png.

The processed PNGs and candidate DDS files use the six exact locked basenames in processed_png/ and dds/.

The prompt files are prompts/sov_nuclear_decision_accounting.md, prompts/sov_nuclear_decision_storage_hardening.md, prompts/sov_nuclear_decision_storage_hardening_v2_edit.md, prompts/sov_nuclear_decision_storage_hardening_v3_edit.md, prompts/sov_nuclear_decision_storage_hardening_v4_edit.md, prompts/sov_nuclear_decision_reactor_construction.md, prompts/sov_nuclear_decision_device_assembly.md, prompts/sov_nuclear_decision_delivery_preparation.md, prompts/sov_nuclear_decision_command_exercise.md, and prompts/generation_trace.md.

Review evidence is in review/contact_sheet.png, review/storage_hardening_edge_lineage_4x.png, the six *_dds_roundtrip.png files, the six *_dds_neutral_1x.png files, the six *_dds_neutral_4x_nearest.png files, the six *_dds_neutral_4x_smooth.png files, and per-icon processed 1x/4x inspection previews. The initial incorrectly sized edge-lineage-sheet attempt is preserved as review/storage_hardening_edge_lineage_layout_failed_v1.png and is not the selected review sheet.

The sprite/path handoff is docs/assets/023_sov_nuclear_bombs/decision_icon_replacements_v1/gfx_handoff.md. This parent handoff is docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_production_decision_icon_replacements_v1_2026-10-03.md.

## Visual findings

At native 33x32 and 4x nearest-neighbour, accounting reads as a closed ledger with a small red seal; reactor construction reads as an industrial vessel and pipe assembly; device assembly reads as a heavy cylindrical casing on a cradle with a wrench cue; delivery preparation reads as a period propeller bomber with one subordinate bomb cue; and command exercise reads as a field telephone with a key cue.

Storage hardening v1 has RGBA (255,0,0,1) at source pixel (320,24). The v2 native ImageGen edit changes that same sample to fully transparent RGBA (0,0,0,0), and the parent reports that the remaining upper-edge antialiasing is mostly alpha 2-3. V2 is the source used for the current processed PNG and DDS candidate; the final edge acceptance remains the parent's decision from the retained RGBA source and native/4x review. V3 and v4 were additional native ImageGen edit outputs created before the latest parent direction; both remain preserved but unselected and were not used for processing.

No background-removal fallback, manual color painting, recoloring, or local primitive drawing was used.

## Task-specific validation

The installed vanilla DDS header was parsed and its decoded pixels compared to the canonical reference PNG; dimensions were 33x32 and pixel equality was exact.

All six candidate DDS files were converted with .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py and verified as 4352-byte, 33x32, one-level legacy BGRA32 with the expected masks, no mipmaps, alpha range 0-255, and zero-alpha corners. Every decoded DDS RGBA pixel exactly matches its processed PNG.

All six decoded DDS images were opened individually at native 1x and on neutral grey, and at nearest-neighbour 4x on neutral grey. The full contact sheet and the storage v1-v4 upper-edge comparison were also opened. Original RGBA round trips remain separate from their neutral-background review composites.

## Ownership, skipped work, and parent follow-up

No GFX, runtime DDS, gameplay, decision, localisation, achievement, workbook, shared manifest, skill, or Git file was changed. The seven achievement triplets and every non-selected Event 23 asset family were untouched.

No test suite was added or run. No game was launched. The parent owns the final visual review, exact DDS promotion to the locked runtime paths, and any consumer wiring. In particular, the parent must accept or reject the storage v2 upper-edge pixels using the actual RGBA source and decoded DDS evidence before promotion.

The six candidate DDS files are not runtime-complete assets until parent acceptance and promotion. Event 23 and its full asset package remain outside this bounded handoff.
