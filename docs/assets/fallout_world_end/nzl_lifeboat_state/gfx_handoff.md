# New Zealand Lifeboat State Fallout GFX handoff

This handoff is asset-only. The generated-art producer did not edit `.gfx`, event, country, localisation, or GUI files. Use the proposed sprite names and paths below when wiring the parent event/country package.

## Suggested sprite registration

Suggested target file for leader, advisor, and report registrations: `interface/fallout_world_end.gfx` (the parent has already registered the four report sprites there). Flags use the engine's conventional `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small` ladders and normally do not need an explicit custom sprite block.

### Report-event sprites: ready

| Sprite name | DDS path | Dimensions | Use note |
|---|---|---:|---|
| `GFX_report_event_fallout_nzl_opening` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_opening.dds` | 210x176 | Opening: berth ledger, evacuees, and harbor officials. |
| `GFX_report_event_fallout_nzl_domestic` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_domestic.dds` | 210x176 | Domestic ration/dairy warehouse dispute. |
| `GFX_report_event_fallout_nzl_external` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_external.dds` | 210x176 | Linked radio rooms and Pacific storm contact. |
| `GFX_report_event_fallout_nzl_late` | `gfx/event_pictures/fallout_world_end/nzl_lifeboat_state/report_event_fallout_nzl_late.dds` | 210x176 | Repaired harbor, stores, patrol craft, and civic assembly. |

### Leader portraits: ready

| Sprite name | DDS path | Dimensions | Assignment note |
|---|---|---:|---|
| `GFX_portrait_NZL_fallout_lifeboat_parliament` | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_lifeboat_parliament.dds` | 156x210 | Institutional council composition. Keep a council or institutional leader name rather than a single generic office title. |
| `GFX_portrait_NZL_fallout_relief_speaker` | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_relief_speaker.dds` | 156x210 | Female-presenting. Use an actual-ish female regional name pool. |
| `GFX_portrait_NZL_fallout_harbor_constable` | `gfx/leaders/fallout_world_end/nzl_lifeboat_state/NZL_fallout_harbor_constable.dds` | 156x210 | Male-presenting. Use an actual-ish male regional name pool. |

### Advisor dossier portraits

| Sprite name | DDS path | Dimensions | Status / use note |
|---|---|---:|---|
| `GFX_portrait_NZL_fallout_dairy_relief_commissioner_small` | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_dairy_relief_commissioner.dds` | 65x67 | Approved by `/root` as a separate reviewer. Candidate SHA `6712fdb638c4ef5c3daab2cff6920d9b011a037a6bb75361af5608031d7e1657`. DDS SHA `edb5a86c6578d01aa0ca21cba0e8d1b2cd1627b829844f46af60cd50af12f1fb`. |
| `GFX_portrait_NZL_fallout_storm_port_engineer_small` | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/NZL_fallout_storm_port_engineer.dds` | 65x67 | **Approved and converted.** Source v9 SHA `de19a5cfee608ea9ae3e160efc2e8f05e5420ee4b66d5c8ec688315c0120d8ac`. Candidate SHA `ec53d400dbdbb58d8aacda9fe5555fd77f480deab2efd39637a095ed241cc0d9`. Review SHA `f8e0e82e72af3cdab14482e28929e143c6139cb7a64b86d0af69ea14514a5cbb`. DDS SHA `65b51bc3af39c5dc2865d722d3167d78c0180361837fc105e3ceba39cb109a13`. Independent reviewer `/root`. Approval file `reviews/advisors/NZL_fallout_storm_port_engineer_approval.json`. |
| `GFX_portrait_NZL_fallout_radio_service_coordinator_small` | no runtime DDS because frozen processor produced no candidate | 65x67 target | **BLOCKED / needs_user_review.** Final source `docs/assets/fallout_world_end/nzl_lifeboat_state/source_masters/portraits/NZL_fallout_radio_service_coordinator_source_v10.png` has SHA `1bf30d1994696037ceb994e9b5ba41249faaaec1df01739cb2190b2393531362` and ImageGen handle `exec-8103dbe6-42b9-4070-b953-faa106b01080`. Frozen v5 rejected 96 final candidates. Rejections: `portrait_top_left_native_bands` 680, `portrait_background_identity` 505, `portrait_palette` 42, `paper_identity_or_palette` 18, `native_band_paper_mean` 78, `native_band_paper_std` 63, and `native_band_bottom_area_variation` 96. No review sheet, candidate PNG, DDS, or sprite wiring exists. |

The storm candidate and dairy review/approval files are included in `source_masters/portraits/` and `reviews/advisors/`. `contact_sheets/portraits_contact_sheet.png` retains the approved portrait set beside the historical v7 radio source. It does not show the final v10 source, which must be inspected directly in `source_masters/portraits/`. The storm DDS is present only after the separate `/root` approval record.

## Flag ladders: ready

Use the cosmetic tag names from the parent country package with these files:

| Cosmetic tag | Normal | Medium | Small |
|---|---|---|---|
| `NZL_FALLOUT_LIFEBOAT_STATE` | `gfx/flags/NZL_FALLOUT_LIFEBOAT_STATE.tga` (82x52) | `gfx/flags/medium/NZL_FALLOUT_LIFEBOAT_STATE.tga` (41x26) | `gfx/flags/small/NZL_FALLOUT_LIFEBOAT_STATE.tga` (10x7) |
| `NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC` | `gfx/flags/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga` (82x52) | `gfx/flags/medium/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga` (41x26) | `gfx/flags/small/NZL_FALLOUT_PACIFIC_RELIEF_REPUBLIC.tga` (10x7) |
| `NZL_FALLOUT_SOUTHERN_REFUGE` | `gfx/flags/NZL_FALLOUT_SOUTHERN_REFUGE.tga` (82x52) | `gfx/flags/medium/NZL_FALLOUT_SOUTHERN_REFUGE.tga` (41x26) | `gfx/flags/small/NZL_FALLOUT_SOUTHERN_REFUGE.tga` (10x7) |

The flags are intentional flat ImageGen designs, not waving fabric or locally drawn recolors. `contact_sheets/flags_contact_sheet.png` shows the master and all three runtime sizes.

## Processing and review references

- Source prompts: `prompts/imagegen_prompts.md` (SHA-256 `6d4ebf3d4c202851fe09c0730a55bd95eb6fcd29974dcdb1e2d4632078a37e64`).
- Advisor provenance: `portrait_provenance_manifest.json`.
- Advisor overlay contract: `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_dossier_overlay_manifest.json`.
- Report processor: `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.
- DDS converter: `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

No `.gfx` changes are included in this handoff. The parent implementation agent owns final sprite registration and any event/country references.

## Dedicated dormant-pilot decision sprites: proposed

The six sprites below are proposed for the parent agent's `interface/fallout_world_end.gfx` registration. Each texture is a dedicated Fallout-owned `32x32` transparent decision icon. No `.gfx` file was edited by this asset package.

| SpriteType name | Texture path | Dimensions | Related decision |
|---|---|---:|---|
| `GFX_decision_fallout_nzl_mobilize_home_guard_state` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_mobilize_home_guard_state.dds` | 32x32 | `fallout_nzl_mobilize_home_guard_state`: controlled-state home guard mobilization, infantry equipment/manpower, defensive identity |
| `GFX_decision_fallout_nzl_dispatch_dairy_relief_convoy` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_dispatch_dairy_relief_convoy.dds` | 32x32 | `fallout_nzl_dispatch_dairy_relief_convoy`: one-shot domestic dairy-relief conversion, with no exact-partner convoy requirement |
| `GFX_decision_fallout_nzl_rebuild_partner_relief_port` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_rebuild_partner_relief_port.dds` | 32x32 | `fallout_nzl_rebuild_partner_relief_port`: exact-partner coastal relief port rebuilding and humanitarian logistics |
| `GFX_decision_fallout_nzl_guarantee_relief_partner` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_guarantee_relief_partner.dds` | 32x32 | `fallout_nzl_guarantee_relief_partner`: New Zealand guarantee for an exact relief partner |
| `GFX_decision_fallout_nzl_revoke_raider_access` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_revoke_raider_access.dds` | 32x32 | `fallout_nzl_revoke_raider_access`: revoke access against the exact stored pirate aggressor |
| `GFX_decision_fallout_nzl_quiet_seas_patrol` | `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_quiet_seas_patrol.dds` | 32x32 | `fallout_nzl_quiet_seas_patrol`: bounded anti-piracy patrol against the exact stored aggressor |

Ready-to-copy SpriteType pattern (repeat once per row with the matching name/path):

```text
SpriteType = {
    name = GFX_decision_fallout_nzl_mobilize_home_guard_state
    texturefile = "gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_mobilize_home_guard_state.dds"
}
```

Review sheet: `contact_sheets/decision_icons_fallout_nzl_lifeboat_state_32x32.png` (all six shown at 8x nearest-neighbour over a checkerboard). The six processed PNGs have transparent corners, and the DDS payloads decode to exact RGBA equality. No asset is blocked or pending review.
