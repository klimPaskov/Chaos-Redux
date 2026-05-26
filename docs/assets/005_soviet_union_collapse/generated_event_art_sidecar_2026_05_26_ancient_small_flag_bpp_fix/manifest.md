# Event 005 Ancient Restoration Small Flag BPP Fix

Date: 2026-05-26

Scope: asset sidecar correction for `KZR`, `SOG`, `KHW`, and `ALN` small flags only. The current normal-size flag artwork was treated as the approved source art, then re-exported to `10x7` 32 bpp bottom-origin TGA outputs for the base flag and four ideology variants.

No gameplay, `.gfx`, localisation, GUI, focus, decision, event, script, history, country, spreadsheet, normal flag, medium flag, or leader portrait files were edited. No default flags for vanilla-supported existing countries were created or changed.

Source mode: existing generated/historical-restoration Event 005 flag artwork. No new `$imagegen` prompt was issued because the issue was export format, not missing artwork.

Reference folders inspected:

- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `docs/assets/005_soviet_union_collapse/contact_sheets/`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_small_flag_export_fix/`

Outputs:

- Source PNGs: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/source_png/`
- Processed PNG previews: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/processed_png/`
- Sidecar final TGA copies: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/final_tga/small/`
- Promoted final TGAs: `gfx/flags/small/<TAG>[_<ideology>].tga`
- Contact sheet: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/contact_sheets/ancient_small_flag_bpp_fix_contact.png`
- Header audit: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/notes/tga_header_audit.tsv`
- Touched file list: `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/notes/touched_small_flags.txt`

## Asset Records

| Family | Variants | Source PNG pattern | Processed PNG pattern | Sidecar TGA pattern | Final small TGA pattern | Target size | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `KZR` | base, `communism`, `democratic`, `fascism`, `neutrality` | `source_png/KZR*_source_from_normal.png` | `processed_png/KZR*_small.png` | `final_tga/small/KZR*.tga` | `gfx/flags/small/KZR*.tga` | 10x7, 32 bpp | converted |
| `SOG` | base, `communism`, `democratic`, `fascism`, `neutrality` | `source_png/SOG*_source_from_normal.png` | `processed_png/SOG*_small.png` | `final_tga/small/SOG*.tga` | `gfx/flags/small/SOG*.tga` | 10x7, 32 bpp | converted |
| `KHW` | base, `communism`, `democratic`, `fascism`, `neutrality` | `source_png/KHW*_source_from_normal.png` | `processed_png/KHW*_small.png` | `final_tga/small/KHW*.tga` | `gfx/flags/small/KHW*.tga` | 10x7, 32 bpp | converted |
| `ALN` | base, `communism`, `democratic`, `fascism`, `neutrality` | `source_png/ALN*_source_from_normal.png` | `processed_png/ALN*_small.png` | `final_tga/small/ALN*.tga` | `gfx/flags/small/ALN*.tga` | 10x7, 32 bpp | converted |

## Validation

- Before the fix, the direct TGA header audit found the 20 scoped small flags were `10x7` but 8 bpp.
- After the fix, all 20 promoted final TGAs are `10x7`, 32 bpp, bottom-origin, descriptor `0x08`.
- Direct leader audit found `47` Event 005 leader DDS files, all `156x210`, with zero duplicate SHA-256 groups and zero vanilla leader DDS hash matches.
- Direct custom/cosmetic flag audit found zero missing files and zero base/ideology duplicate hash groups for the checked Event 005 custom/cosmetic families.
- Direct existing-country flag audit found zero default `gfx/flags/<existing_TAG>*.tga` overrides for the vanilla-supported ordinary/internal tags listed in the Event 005 asset handoff.

## Blockers And Uncertainty

No safe generated asset batch remains in this scoped surface after the small-flag export correction. The remaining non-sidecar asset concerns in the main manifest, such as duplicate focus icon assignments, are outside this generated/council portrait and fictional/route flag sidecar scope.
