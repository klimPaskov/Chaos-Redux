# IW-006 Wallonia (AFX) Level-2 unique visual package

## Scope and ownership

This package supplies only the eleven AFX visual requirements assigned on 2026-07-16:

- eight original `94x86` national-focus icons
- three original `210x176` report-event scenes

The asset producer created source masters, processed PNGs, runtime DDS files, prompts, contact sheets, hashes, and validation evidence. The main agent owns sprite registration and final consumer wiring. No gameplay, focus, localisation, registry, readiness, event-reference, spreadsheet, or interface file was edited by this asset pass.

## Source and processing method

- Source mode: official built-in `$imagegen`, one separate generation call per asset.
- Focus rationale: each focus needed original compact painterly symbolism rather than a resized or recoloured shared icon.
- Report rationale: the alternate-history incidents needed unique period-coherent scenes that do not exist as real archival events.
- Focus generation: original master on a flat `#00ff00` key, retained unchanged under `source_png/focus/`.
- Alpha extraction: official ImageGen chroma-key helper with border sampling, soft matte, thresholds `12/220`, and despill.
- Focus finishing: alpha-bound crop, premultiplied Lanczos reduction, restrained dark outline, and one-pixel soft shadow on a transparent `94x86` canvas.
- Report finishing: canonical `process_report_event_image.py` treatment (cover crop, monochrome/sepia, grain, paper edge, subtle deterministic tilt, transparent corners, and soft shadow).
- DDS conversion: repository `convert_to_dds.py`, legacy one-level uncompressed 32-bit BGRA.
- Fallbacks or substitutions: none.

Exact generation prompts are retained as one text file per source master under `prompts/focus/` and `prompts/report/`.

## Asset inventory

All paths are relative to the mod root. Status `handed_off` means the runtime art is final and the main agent owns retention/review of the existing sprite registration.

| Asset | Type and use | Prompt | Source master | Processed PNG | Runtime DDS | Sprite | Consumer | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `goal_independence_wave_afx_sambre_meuse_authority` | Focus icon; Sambre–Meuse public authority | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_sambre_meuse_authority.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_sambre_meuse_authority.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_sambre_meuse_authority.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_sambre_meuse_authority.dds` | `GFX_goal_independence_wave_afx_sambre_meuse_authority` + `_shine` | `independence_wave_afx_charter_sambre_meuse_authority_focus` | `handed_off` |
| `goal_independence_wave_afx_mines_rails_furnaces` | Focus icon; linked coal, rail, and steel economy | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_mines_rails_furnaces.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_mines_rails_furnaces.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_mines_rails_furnaces.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_mines_rails_furnaces.dds` | `GFX_goal_independence_wave_afx_mines_rails_furnaces` + `_shine` | `independence_wave_afx_bind_mines_rails_furnaces_focus` | `handed_off` |
| `goal_independence_wave_afx_basin_government` | Focus icon; regional basin government | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_basin_government.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_basin_government.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_basin_government.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_basin_government.dds` | `GFX_goal_independence_wave_afx_basin_government` + `_shine` | `independence_wave_afx_codify_basin_government_focus` | `handed_off` |
| `goal_independence_wave_afx_industrial_reserve` | Focus icon; protected industrial capacity | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_industrial_reserve.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_industrial_reserve.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_industrial_reserve.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_industrial_reserve.dds` | `GFX_goal_independence_wave_afx_industrial_reserve` + `_shine` | `independence_wave_afx_integrate_industrial_reserve_focus` | `handed_off` |
| `goal_independence_wave_afx_industrial_succession` | Focus icon; orderly institutional succession | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_industrial_succession.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_industrial_succession.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_industrial_succession.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_industrial_succession.dds` | `GFX_goal_independence_wave_afx_industrial_succession` + `_shine` | `independence_wave_afx_settle_industrial_succession_focus` | `handed_off` |
| `goal_independence_wave_afx_meuse_network_office` | Focus icon; river-network administration | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_meuse_network_office.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_meuse_network_office.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_meuse_network_office.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_meuse_network_office.dds` | `GFX_goal_independence_wave_afx_meuse_network_office` + `_shine` | `independence_wave_afx_open_meuse_network_office_focus` | `handed_off` |
| `goal_independence_wave_afx_meuse_conference` | Focus icon; Meuse conference | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_meuse_conference.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_meuse_conference.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_meuse_conference.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_meuse_conference.dds` | `GFX_goal_independence_wave_afx_meuse_conference` + `_shine` | `independence_wave_afx_mandate_meuse_conference_focus` | `handed_off` |
| `goal_independence_wave_afx_low_countries_delegation` | Focus icon; Low Countries delegation | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_afx_low_countries_delegation.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_afx_low_countries_delegation.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_afx_low_countries_delegation.png` | `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_low_countries_delegation.dds` | `GFX_goal_independence_wave_afx_low_countries_delegation` + `_shine` | `independence_wave_afx_prepare_low_countries_dossier_focus` | `handed_off` |
| `report_event_006_afx_industrial_authority` | Report scene; civic/industrial authority formed in a rail-and-furnace yard | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/report/report_event_006_afx_industrial_authority.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/report/report_event_006_afx_industrial_authority.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/report/report_event_006_afx_industrial_authority.png` | `gfx/event_pictures/006_independence_wave/afx/report_event_006_afx_industrial_authority.dds` | `GFX_report_event_006_afx_industrial_authority` | `chaosx.nr6.18` | `handed_off` |
| `report_event_006_afx_basin_government` | Report scene; basin assembly in an austere civic hall | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/report/report_event_006_afx_basin_government.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/report/report_event_006_afx_basin_government.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/report/report_event_006_afx_basin_government.png` | `gfx/event_pictures/006_independence_wave/afx/report_event_006_afx_basin_government.dds` | `GFX_report_event_006_afx_basin_government` | `chaosx.nr6.19` | `handed_off` |
| `report_event_006_afx_meuse_ambition` | Report scene; river, bridge, barges, rail quay, and survey party | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/prompts/report/report_event_006_afx_meuse_ambition.txt` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/source_png/report/report_event_006_afx_meuse_ambition.png` | `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/processed_png/report/report_event_006_afx_meuse_ambition.png` | `gfx/event_pictures/006_independence_wave/afx/report_event_006_afx_meuse_ambition.dds` | `GFX_report_event_006_afx_meuse_ambition` | `chaosx.nr6.20` | `handed_off` |

All three report sources are generated fictional documentary scenes, not depictions of a real photographed incident or real person. Their clothing, civil architecture, industrial plant, rail equipment, barges, cranes, office objects, and photographic treatment are directed to the 1936–1942 period. No flags, portraits, readable generated text, or modern logos appear in the selected results.

## Requirement-to-runtime coverage crosswalk

Accepted design source for every row: the parent assignment for exact package `IW-006 Wallonia (AFX)` dated 2026-07-16. The current repository already contains matching definitions in `interface/006_independence_wave_wallonia_frisia_assets.gfx`; this asset pass did not edit that file.

| Requirement | Source-package entry | Runtime registration | Live consumer | Evidence | Row status |
| --- | --- | --- | --- | --- | --- |
| `AFX-L2-F01` | Sambre–Meuse Authority row above | focus DDS + base/shine sprite | `independence_wave_afx_charter_sambre_meuse_authority_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F02` | Mines, Rails, Furnaces row above | focus DDS + base/shine sprite | `independence_wave_afx_bind_mines_rails_furnaces_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F03` | Basin Government row above | focus DDS + base/shine sprite | `independence_wave_afx_codify_basin_government_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F04` | Industrial Reserve row above | focus DDS + base/shine sprite | `independence_wave_afx_integrate_industrial_reserve_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F05` | Industrial Succession row above | focus DDS + base/shine sprite | `independence_wave_afx_settle_industrial_succession_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F06` | Meuse Network Office row above | focus DDS + base/shine sprite | `independence_wave_afx_open_meuse_network_office_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F07` | Meuse Conference row above | focus DDS + base/shine sprite | `independence_wave_afx_mandate_meuse_conference_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-F08` | Low Countries Delegation row above | focus DDS + base/shine sprite | `independence_wave_afx_prepare_low_countries_dossier_focus` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-R01` | Industrial Authority report row above | report DDS + report sprite | `chaosx.nr6.18` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-R02` | Basin Government report row above | report DDS + report sprite | `chaosx.nr6.19` | `validation/asset_validation.json` | asset complete; handed off |
| `AFX-L2-R03` | Meuse Ambition report row above | report DDS + report sprite | `chaosx.nr6.20` | `validation/asset_validation.json` | asset complete; handed off |

## Review and validation evidence

- Focus contact sheet: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/contact_sheets/focus_icons_contact_sheet.png`
- Report contact sheet: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/contact_sheets/report_scenes_contact_sheet.png`
- Visual review record: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/validation/visual_review.md`
- Machine-readable validation: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/validation/asset_validation.json`
- SHA-256 inventory: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/validation/sha256_inventory.txt`
- Mechanical provenance tool: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/tools/asset_pipeline.py`

The machine report verifies exact `11/11/11` source/processed/runtime counts, dimensions, focus transparency, legacy DDS magic/header/pixel-format/masks/caps/file length, unique hashes, distinct perceptual hashes, and exact decoded RGBA equivalence between every processed PNG and runtime DDS.

## Simplifications, omissions, and blockers

None. All eleven assigned assets use separate original source compositions, and no fallback art, reused composition, placeholder, flag, portrait, or weaker substitute was used.
