# Event 015 advisor icon correction handoff

> Historical snapshot superseded by `asset_workflow_and_identity_regeneration_handoff_2026_07_15.md`. The active advisors use newly generated portrait masters plus separate generated frame and paper/seal overlays; processor 2.0 only performs finishing and composition. This body remains provenance for the earlier pass.

Handoff date: `2026-07-15`  
Role: `chaosx_icon_artist`  
Scope: correct all sixteen Event 015 advisor portraits to the native HOI4 advisor-icon pipeline while preserving the existing character IDs, sprite handles, and runtime texture paths

## Outcome

All sixteen Event 015 advisors now use independently cropped `65x67` advisor dossier cards produced by `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py advisor`. Every output has the dark bevelled vanilla-style card, paper overlay, and transparent outer corners required by the repository advisor pipeline. These are not square leader portraits and were not made by shrinking the existing leader-format crop.

Each source master is a distinct fictional ImageGen-created person. All sixteen sources supported a readable independent head-and-shoulders crop, so no source was blocked and no regeneration or fallback was used. Each processed PNG was reviewed at native size, at nearest-neighbour enlargement, and beside the repository references in `assets/vanilla_reference/portraits/advisors`.

The approved PNGs were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 65 --height 67`. Package and runtime DDS files are byte-identical. Existing character IDs, sprite handles, texture paths, `.gfx` definitions, and character references were preserved; this correction made no gameplay, localisation, character, or `.gfx` edits.

This handoff supersedes the former `64x64` advisor-dimension statements in the original route-identity asset handoff. The corrected package manifest, root Event 015 asset manifest, GFX handoff, prompt record, asset records, and validation records carry the current contract.

## Advisor identity, crop, and processing evidence

Every path in this section is repo-relative and written in full.

| Character ID | Stable sprite handle | Explicit source crop `[left, top, right, bottom]` | Source master | Processed `65x67` PNG | Processor metadata | Per-asset comparison |
| --- | --- | --- | --- | --- | --- | --- |
| `utopia_manifesto_interpreter` | `GFX_portrait_utopia_manifesto_interpreter_small` | `[300, 20, 990, 980]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_interpreter_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_interpreter.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_interpreter.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_interpreter_comparison.png` |
| `utopia_manifesto_general_provisioner` | `GFX_portrait_utopia_manifesto_general_provisioner_small` | `[260, 25, 1000, 1040]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_general_provisioner_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_general_provisioner.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_general_provisioner.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_general_provisioner_comparison.png` |
| `utopia_manifesto_secretary_of_callings` | `GFX_portrait_utopia_manifesto_secretary_of_callings_small` | `[300, 30, 1000, 970]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_secretary_of_callings_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_secretary_of_callings.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_secretary_of_callings.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_secretary_of_callings_comparison.png` |
| `utopia_manifesto_surveyor_of_shores` | `GFX_portrait_utopia_manifesto_surveyor_of_shores_small` | `[220, 10, 980, 1080]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_surveyor_of_shores_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_surveyor_of_shores.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_surveyor_of_shores.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_surveyor_of_shores_comparison.png` |
| `utopia_manifesto_civic_engineer` | `GFX_portrait_utopia_manifesto_civic_engineer_small` | `[190, 45, 900, 1020]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_civic_engineer_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_civic_engineer.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_civic_engineer.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_civic_engineer_comparison.png` |
| `utopia_manifesto_keeper_of_stores` | `GFX_portrait_utopia_manifesto_keeper_of_stores_small` | `[250, 30, 1000, 1040]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_keeper_of_stores_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_keeper_of_stores.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_keeper_of_stores.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_keeper_of_stores_comparison.png` |
| `utopia_manifesto_league_envoy` | `GFX_portrait_utopia_manifesto_league_envoy_small` | `[260, 40, 970, 1040]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_league_envoy_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_league_envoy.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_league_envoy.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_league_envoy_comparison.png` |
| `utopia_manifesto_advocate_of_limits` | `GFX_portrait_utopia_manifesto_advocate_of_limits_small` | `[220, 20, 940, 1000]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_advocate_of_limits_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_advocate_of_limits.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_advocate_of_limits.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_advocate_of_limits_comparison.png` |
| `utopia_manifesto_public_auditor` | `GFX_portrait_utopia_manifesto_public_auditor_small` | `[300, 20, 960, 920]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_public_auditor_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_public_auditor.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_public_auditor.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_public_auditor_comparison.png` |
| `utopia_manifesto_constitutional_jurist` | `GFX_portrait_utopia_manifesto_constitutional_jurist_small` | `[250, 20, 980, 1040]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_constitutional_jurist_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_constitutional_jurist.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_constitutional_jurist.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_constitutional_jurist_comparison.png` |
| `utopia_manifesto_council_organizer` | `GFX_portrait_utopia_manifesto_council_organizer_small` | `[200, 50, 930, 1050]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_council_organizer_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_council_organizer.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_council_organizer.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_council_organizer_comparison.png` |
| `utopia_manifesto_social_workshop_planner` | `GFX_portrait_utopia_manifesto_social_workshop_planner_small` | `[200, 10, 950, 980]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_social_workshop_planner_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_social_workshop_planner.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_social_workshop_planner.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_social_workshop_planner_comparison.png` |
| `utopia_manifesto_chief_surveyor` | `GFX_portrait_utopia_manifesto_chief_surveyor_small` | `[240, 10, 980, 1000]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_chief_surveyor_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_chief_surveyor.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_chief_surveyor.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_chief_surveyor_comparison.png` |
| `utopia_manifesto_standards_engineer` | `GFX_portrait_utopia_manifesto_standards_engineer_small` | `[300, 0, 1050, 1050]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_standards_engineer_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_standards_engineer.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_standards_engineer.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_standards_engineer_comparison.png` |
| `utopia_manifesto_steward_of_service` | `GFX_portrait_utopia_manifesto_steward_of_service_small` | `[260, 10, 950, 1080]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_steward_of_service_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_steward_of_service.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_steward_of_service.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_steward_of_service_comparison.png` |
| `utopia_manifesto_contract_broker` | `GFX_portrait_utopia_manifesto_contract_broker_small` | `[260, 20, 980, 1060]` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/advisors/advisor_utopia_manifesto_contract_broker_source.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/advisor_utopia_manifesto_contract_broker.png` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/advisor_utopia_manifesto_contract_broker.json` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/advisor_utopia_manifesto_contract_broker_comparison.png` |

## Runtime and package paths

| Character ID | Runtime DDS | Package-mirror DDS | Decoded verification PNG |
| --- | --- | --- | --- |
| `utopia_manifesto_interpreter` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_interpreter.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_interpreter.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_interpreter.png` |
| `utopia_manifesto_general_provisioner` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_general_provisioner.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_general_provisioner.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_general_provisioner.png` |
| `utopia_manifesto_secretary_of_callings` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_secretary_of_callings.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_secretary_of_callings.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_secretary_of_callings.png` |
| `utopia_manifesto_surveyor_of_shores` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_surveyor_of_shores.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_surveyor_of_shores.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_surveyor_of_shores.png` |
| `utopia_manifesto_civic_engineer` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_civic_engineer.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_civic_engineer.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_civic_engineer.png` |
| `utopia_manifesto_keeper_of_stores` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_keeper_of_stores.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_keeper_of_stores.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_keeper_of_stores.png` |
| `utopia_manifesto_league_envoy` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_league_envoy.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_league_envoy.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_league_envoy.png` |
| `utopia_manifesto_advocate_of_limits` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_advocate_of_limits.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_advocate_of_limits.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_advocate_of_limits.png` |
| `utopia_manifesto_public_auditor` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_public_auditor.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_public_auditor.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_public_auditor.png` |
| `utopia_manifesto_constitutional_jurist` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_constitutional_jurist.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_constitutional_jurist.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_constitutional_jurist.png` |
| `utopia_manifesto_council_organizer` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_council_organizer.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_council_organizer.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_council_organizer.png` |
| `utopia_manifesto_social_workshop_planner` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_social_workshop_planner.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_social_workshop_planner.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_social_workshop_planner.png` |
| `utopia_manifesto_chief_surveyor` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_chief_surveyor.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_chief_surveyor.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_chief_surveyor.png` |
| `utopia_manifesto_standards_engineer` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_standards_engineer.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_standards_engineer.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_standards_engineer.png` |
| `utopia_manifesto_steward_of_service` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_steward_of_service.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_steward_of_service.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_steward_of_service.png` |
| `utopia_manifesto_contract_broker` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_contract_broker.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/advisor_utopia_manifesto_contract_broker.dds` | `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/advisor_utopia_manifesto_contract_broker.png` |

## Comparison and visual-review findings

- All sixteen source masters are byte-distinct and visibly depict different fictional people.
- Every crop is an explicit head-and-shoulders crop selected from the high-resolution source master; none reuses a leader-format crop.
- All sixteen native-size icons retain a readable face and silhouette at `65x67`.
- The nearest-neighbour enlargement review found no clipped eyes, displaced faces, unreadable silhouettes, frame breaks, or paper-overlay failures.
- Per-asset comparison sheets show the same visual grammar as `assets/vanilla_reference/portraits/advisors`: dark bevelled dossier card, aged paper inset, and transparent outer corners.
- All sixteen candidates were approved. No source was rejected, regenerated, substituted, or treated as a fallback.
- The mandated portrait processor's soft frame shadow produces corner alpha `[0, 0, 4, 0]` in corner order top-left, top-right, bottom-left, bottom-right. The lower-left value is about `1.6%` opacity at the extreme pixel and remains visually transparent; it is consistent across all sixteen processor outputs and was retained rather than hand-altered after processing.

Review surfaces:

- Source overview: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_sources_contact_sheet.png`
- Native-size overview: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_native_contact_sheet.png`
- Nearest-neighbour enlarged overview: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`
- Decoded-DDS overview: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- Sixteen reference comparisons: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/`
- Focused machine-readable proof: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_validation_2026_07_15.json`

## DDS and package validation

All sixteen runtime DDS files and all sixteen package mirrors meet the same exact contract:

- dimensions: `65x67`
- file length: `17,548` bytes, equal to the `128`-byte DDS header plus `65 * 67 * 4` pixel bytes
- DDS magic: `DDS `
- header size: `124`
- pitch: `260`
- pixel format: uncompressed `32`-bit RGB with alpha, flags `65`, no FourCC
- channel masks: red `0x00FF0000`, green `0x0000FF00`, blue `0x000000FF`, alpha `0xFF000000`
- caps: `0x00001000`
- mipmaps: none
- alpha range: `0..255`
- package/runtime relationship: byte-identical for every advisor
- decoded relationship: every DDS decodes pixel-identically to its approved processed PNG
- distinctness: all sixteen processed PNG hashes are unique and all sixteen source hashes are unique

`asset_records.json`, `validation.json`, and `advisor_validation_2026_07_15.json` carry per-advisor hashes and validation values. The character file contains exactly the sixteen expected stable `small` handles, and `interface/015_utopia_manifesto.gfx` contains the sixteen expected stable sprite definitions and texture paths. Those source files were inspected read-only and were not edited by this correction.

## Changed files

Runtime and package assets:

- `gfx/leaders/015_utopia_manifesto/advisors/*.dds` - sixteen corrected runtime DDS files
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/advisors/*.png` - sixteen corrected `65x67` processor outputs
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_dds/advisors/*.dds` - sixteen corrected DDS package mirrors
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/advisors/*.png` - sixteen refreshed decode-verification mirrors
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/metadata/advisors/*.json` - sixteen processor metadata and review records
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_reviews/*.png` - sixteen processor comparison sheets
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_sources_contact_sheet.png`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_native_contact_sheet.png`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_decoded_contact_sheet.png`

Records and documentation:

- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_validation_2026_07_15.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/asset_records.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/validation.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/manifest.md`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/gfx_handoff.md`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/prompts/route_identity_prompts.md`
- `docs/assets/015_utopia_manifesto/manifest.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_icon_correction_handoff.md`

No source master was modified by this correction. Concurrent Event 015 flag and institutional-portrait work exists in the shared worktree and is outside this handoff.

## Parent integration status

No asset wiring edit is required. The stable handles and texture paths already resolve to the replaced runtime DDS files. The parent should retain the existing `.gfx` definitions and character `small` references unchanged, and include this handoff and corrected package evidence when reconciling the final Event 015 documentation and commit.

## Skills and references used

- `chaos-redux-event-assets` - advisor source review, separate cropping, processor metadata, reference comparison, DDS conversion, manifest, contact sheet, and asset handoff requirements
- `chaos-redux-subagents` - bounded asset ownership, parent-owned integration, and evidence-rich handoff requirements

The required offline Paradox wiki core pages, Interface Modding, and Scripted GUI Modding were consulted. Vanilla effects documentation, character portrait precedents, and advisor sprite definitions were inspected. No skill was created or updated; the existing asset and subagent skills already captured the reusable workflow.

## Simplifications, omissions, blockers, and residual risks

- Simplifications: none.
- Fallbacks: none.
- Missing advisors: none.
- Blocked or inadequate sources: none.
- Gameplay, localisation, character, or `.gfx` edits: none.
- Residual asset risks: none identified after native, enlarged, reference-comparison, header, byte-equality, and decode-equality review.
- Commit: not created; the parent owns the integrated Event 015 commit and concurrent Event 015 work is present in the shared tree.
