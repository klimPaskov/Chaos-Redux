# New Zealand Lifeboat State Fallout visual-asset manifest

Package for the dormant New Zealand Lifeboat State Fallout pilot. Every final image in this package is a fictional ImageGen source, retained alongside its processed review PNG. No gameplay, localisation, or `.gfx` files are edited here. The selected report, leader, dairy-advisor, and storm-advisor assets are final-source art. The radio advisor master remains explicitly blocked by the frozen advisor processor and is not a substitute.

## Requirement-to-runtime crosswalk

| Requested surface | Runtime asset(s) | Status | Notes |
|---|---|---|---|
| Lifeboat State flat flag | `gfx/flags/NZL_FALLOUT_LIFEBOAT_STATE.tga`, `medium/`, `small/` | complete | Three exact ladder sizes: 82x52, 41x26, 10x7. |
| Pacific Relief Republic flat flag | `gfx/flags/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga`, `medium/`, `small/` | complete | Independent red/green/blue design; no protected emblem or copied New Zealand ensign. |
| Southern Refuge flat flag | `gfx/flags/NZL_FALLOUT_SOUTHERN_REFUGE.tga`, `medium/`, `small/` | complete | Independent navy/silver/red design; no copied official symbol. |
| Lifeboat Parliament leader | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_lifeboat_parliament.dds` | complete | 156x210 processed portrait. Council image is people-rich but uses an institutional council name. |
| Relief Speaker leader | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_relief_speaker.dds` | complete | 156x210 processed portrait; female-presenting source requires a female regional name pool. |
| Harbor Constable leader | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_harbor_constable.dds` | complete | 156x210 processed portrait; male-presenting source requires a male regional name pool. |
| Dairy Relief Commissioner advisor | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_dairy_relief_commissioner.dds` | approved and converted | 65x67 candidate independently approved by `/root`; exact candidate hash is pinned below. |
| Storm Port Engineer advisor | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_storm_port_engineer.dds` | approved and converted | Fresh v9 candidate and review were independently approved by `/root`; exact approval is recorded in `_approval.json`. |
| Radio Service Coordinator advisor | no runtime DDS | blocked / needs_user_review | v10–v13 remained blocked; authorized v14 added a visible radio control panel, tuning dials, ledger, cables, and desk edge but still failed unchanged v5 at `paper_mean` (`198.848766`) and `bottom_area_variation` (`15.683616`), minimum margin `-0.020252`. No fallback portrait. |
| Four report-event images | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_*.dds` | complete | Processed to 210x176 sepia documentary cards; parent owns the `.gfx` registration. |

## Flags

Source masters are 1774x887 RGB ImageGen flat designs. They are intentionally separate designs and were resized mechanically with Pillow to the three requested runtime ladders. TGA output is RGBA with the repository's bottom-left origin convention.

| Sprite proposal | Source master | Normal / medium / small | Source SHA-256 |
|---|---|---|---|
| `GFX_flag_NZL_FALLOUT_LIFEBOAT_STATE` | `source_masters/flags/NZL_FALLOUT_LIFEBOAT_STATE_source.png` | `gfx/flags/NZL_FALLOUT_LIFEBOAT_STATE.tga` / `gfx/flags/medium/NZL_FALLOUT_LIFEBOAT_STATE.tga` / `gfx/flags/small/NZL_FALLOUT_LIFEBOAT_STATE.tga` | `f38c165101728d915fe1c27de94ec0f4363479075b48d1b3018cc38cc483f082` |
| `GFX_flag_NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC` | `source_masters/flags/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC_source.png` | `gfx/flags/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga` / `gfx/flags/medium/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga` / `gfx/flags/small/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga` | `595a977f8a3e04ea494cd8b48c8b081cb84397cf1e03d5229abd8e57252a2d1d` |
| `GFX_flag_NZL_FALLOUT_SOUTHERN_REFUGE` | `source_masters/flags/NZL_FALLOUT_SOUTHERN_REFUGE_source.png` | `gfx/flags/NZL_FALLOUT_SOUTHERN_REFUGE.tga` / `gfx/flags/medium/NZL_FALLOUT_SOUTHERN_REFUGE.tga` / `gfx/flags/small/NZL_FALLOUT_SOUTHERN_REFUGE.tga` | `984ca2c9ead2b98d80032892b35d70b50cdbd69d99df9ae8981d31cdd722ac4d` |

## Leader portraits

All three sources are fictional ImageGen portrait masters, processed with the repository leader processor to exact 156x210 PNGs and converted with `convert_to_dds.py`.

| Sprite proposal | Source master | Processed PNG | Runtime DDS |
|---|---|---|---|
| `GFX_portrait_NZL_fallout_lifeboat_parliament` | `source_masters/portraits/NZL_fallout_lifeboat_parliament_source.png` | `processed/portraits/NZL_fallout_lifeboat_parliament.png` | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_lifeboat_parliament.dds` |
| `GFX_portrait_NZL_fallout_relief_speaker` | `source_masters/portraits/NZL_fallout_relief_speaker_source.png` | `processed/portraits/NZL_fallout_relief_speaker.png` | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_relief_speaker.dds` |
| `GFX_portrait_NZL_fallout_harbor_constable` | `source_masters/portraits/NZL_fallout_harbor_constable_source.png` | `processed/portraits/NZL_fallout_harbor_constable.png` | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_harbor_constable.dds` |

## Advisor dossier portraits

Advisor processing used the pinned schema-1 portrait provenance manifest, the schema-4 overlay manifest, Python 3.9.12/Pillow 11.1.0, processor SHA `e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`, and render hash `e9f8d54d1ea7fc8845bf22675c09686acc7196556a56f96f5a1b46268b134637`. The processor's mechanical result is not itself visual approval.

| Sprite proposal | Source / candidate | Review metadata | Runtime DDS | Status |
|---|---|---|---|---|
| `GFX_portrait_NZL_fallout_dairy_relief_commissioner_small` | `source_masters/portraits/NZL_fallout_dairy_relief_commissioner_source_v2.png` / `processed/advisors/NZL_fallout_dairy_relief_commissioner.png` | `reviews/advisors/NZL_fallout_dairy_relief_commissioner_review.png`, `.json`, and independent `_approval.json` | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_dairy_relief_commissioner.dds` | approved by `/root`; candidate SHA `6712fdb638c4ef5c3daab2cff6920d9b011a037a6bb75361af5608031d7e1657`; DDS SHA `edb5a86c6578d01aa0ca21cba0e8d1b2cd1627b829844f46af60cd50af12f1fb` |
| `GFX_portrait_NZL_fallout_storm_port_engineer_small` | `source_masters/portraits/NZL_fallout_storm_port_engineer_source_v9.png` / `processed/advisors/NZL_fallout_storm_port_engineer.png` | `reviews/advisors/NZL_fallout_storm_port_engineer_review.png`, `.json`, and `_approval.json` | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_storm_port_engineer.dds` | independently approved by `/root`; candidate SHA `ec53d400dbdbb58d8aacda9fe5555fd77f480deab2efd39637a095ed241cc0d9`; review SHA `f8e0e82e72af3cdab14482e28929e143c6139cb7a64b86d0af69ea14514a5cbb`; DDS SHA `65b51bc3af39c5dc2865d722d3167d78c0180361837fc105e3ceba39cb109a13`; native minimum margin `0.031294`; source SHA `de19a5cfee608ea9ae3e160efc2e8f05e5420ee4b66d5c8ec688315c0120d8ac`; ImageGen handle `exec-05deef3b-f158-4554-971e-8503df61d83e` |
| `GFX_portrait_NZL_fallout_radio_service_coordinator_small` | `source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v14.png` / no candidate PNG | no review sheet produced because processor rejected all candidates | none | blocked / needs_user_review; v14 source SHA `a1085e9c2839f740b6f34deab8f587ffc8333bf6f787507f299294d42014a342`; closest v14 failure was `paper_mean` `198.848766` and `bottom_area_variation` `15.683616`, minimum margin `-0.020252`; exact handles and rejection counts are in `reviews/advisors/NZL_fallout_radio_service_coordinator_blocker.md` |

The historical v7 radio comparison remains retained for provenance in the contact sheet. v10 through v14 sources are available in the source folder for independent inspection. No DDS is created for the blocked radio advisor.

## Report-event images

Each generated 1536-ish source is retained under `source_masters/reports/`, then passed through `process_report_event_image.py` to a 210x176 RGBA sepia documentary card and converted with the repository `convert_to_dds.py` converter. Parent has registered the four report sprites in `interface/fallout_world_end.gfx`.

| Sprite | Source master | Processed PNG | Runtime DDS |
|---|---|---|---|
| `GFX_report_event_fallout_nzl_opening` | `source_masters/reports/report_event_fallout_nzl_opening_source.png` | `processed/reports/report_event_fallout_nzl_opening.png` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_opening.dds` |
| `GFX_report_event_fallout_nzl_domestic` | `source_masters/reports/report_event_fallout_nzl_domestic_source.png` | `processed/reports/report_event_fallout_nzl_domestic.png` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_domestic.dds` |
| `GFX_report_event_fallout_nzl_external` | `source_masters/reports/report_event_fallout_nzl_external_source.png` | `processed/reports/report_event_fallout_nzl_external.png` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_external.dds` |
| `GFX_report_event_fallout_nzl_late` | `source_masters/reports/report_event_fallout_nzl_late_source.png` | `processed/reports/report_event_fallout_nzl_late.png` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_late.dds` |

## Dedicated decision icons — dormant NZL Lifeboat State Fallout pilot

Six independent decision icons were generated specifically for the dormant pilot's exact stored-partner and stored-aggressor actions. They use the canonical decision-icon surface at `32x32`, with strong silhouettes and real alpha; none is a resized, recoloured, or relabelled copy of the existing twelve NZL decision icons. The parent agent owns the final `.gfx` registration in `interface/fallout_world_end.gfx`.

| Decision id | Sprite proposal | Source master | Processed PNG | Runtime DDS | Review |
|---|---|---|---|---|---|
| `fallout_nzl_mobilize_home_guard_state` | `GFX_decision_fallout_nzl_mobilize_home_guard_state` | `source_masters/decisions/decision_fallout_nzl_mobilize_home_guard_state_source.png` | `processed/decisions/decision_fallout_nzl_mobilize_home_guard_state_key.png` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_mobilize_home_guard_state.dds` | complete; shield/watchtower/rifle silhouette checked at 32px and 8x contact sheet |
| `fallout_nzl_dispatch_dairy_relief_convoy` | `GFX_decision_fallout_nzl_dispatch_dairy_relief_convoy` | `source_masters/decisions/decision_fallout_nzl_dispatch_dairy_relief_convoy_source.png` | `processed/decisions/decision_fallout_nzl_dispatch_dairy_relief_convoy_key.png` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_dispatch_dairy_relief_convoy.dds` | complete; cargo launch/milk-can relief read at 32px and 8x contact sheet |
| `fallout_nzl_rebuild_partner_relief_port` | `GFX_decision_fallout_nzl_rebuild_partner_relief_port` | `source_masters/decisions/decision_fallout_nzl_rebuild_partner_relief_port_source.png` | `processed/decisions/decision_fallout_nzl_rebuild_partner_relief_port_key.png` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_rebuild_partner_relief_port.dds` | complete; crane/pier/relief crate silhouette checked at 32px and 8x contact sheet |
| `fallout_nzl_guarantee_relief_partner` | `GFX_decision_fallout_nzl_guarantee_relief_partner` | `source_masters/decisions/decision_fallout_nzl_guarantee_relief_partner_source.png` | `processed/decisions/decision_fallout_nzl_guarantee_relief_partner_key.png` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_guarantee_relief_partner.dds` | complete; shield/lifeboat/interlocking rings read at 32px and 8x contact sheet |
| `fallout_nzl_revoke_raider_access` | `GFX_decision_fallout_nzl_revoke_raider_access` | `source_masters/decisions/decision_fallout_nzl_revoke_raider_access_source.png` | `processed/decisions/decision_fallout_nzl_revoke_raider_access_key.png` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_revoke_raider_access.dds` | complete; snapped chain/barred gate/grapnel cancellation read at 32px and 8x contact sheet |
| `fallout_nzl_quiet_seas_patrol` | `GFX_decision_fallout_nzl_quiet_seas_patrol` | `source_masters/decisions/decision_fallout_nzl_quiet_seas_patrol_source.png` | `processed/decisions/decision_fallout_nzl_quiet_seas_patrol_key.png` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_quiet_seas_patrol.dds` | complete; patrol cutter/searchlight/hostile wake read at 32px and 8x contact sheet |

Review sheet: `contact_sheets/decision_icons_fallout_nzl_lifeboat_state_32x32.png` (960x794; each icon shown 8x over a checkerboard). The six DDS files were header-checked and decoded back to exact RGBA equality with their processed PNGs.

## Review material and provenance

- `prompts/imagegen_prompts.md` records the generation prompts; its pinned SHA-256 is `6d4ebf3d4c202851fe09c0730a55bd95eb6fcd29974dcdb1e2d4632078a37e64`.
- `portrait_provenance_manifest.json` pins the selected advisor source bytes, dimensions, crops, face boxes, and ImageGen handles.
- `contact_sheets/flags_contact_sheet.png`, `portraits_contact_sheet.png`, `reports_contact_sheet.png`, and `decision_icons_fallout_nzl_lifeboat_state_32x32.png` are the review sheets.
- `reviews/portraits/` contains leader processor reviews; `reviews/advisors/` contains the dairy candidate review/approval, metadata, and the exact storm/radio blocker records.

## Blockers and non-fallback policy

The storm candidate has independent approval and a final DDS. The radio fresh source remains blocked after the exact processor. Do not substitute a resized leader/primitive-drawn/paperless portrait. Dairy and storm are the approved advisor runtime DDS assets in this package.
