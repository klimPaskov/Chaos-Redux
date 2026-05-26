# Event 005 Generated Event Art Sidecar Handoff

Date: 2026-05-26

Scope: asset sidecar only for generated/council/high-chaos portraits and fictional or alternate-history flag status. No gameplay, `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files were edited.

## Evidence Reviewed

- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`

## Files Changed

- `gfx/flags/small/KZR.tga`
- `gfx/flags/small/KZR_communism.tga`
- `gfx/flags/small/KZR_democratic.tga`
- `gfx/flags/small/KZR_fascism.tga`
- `gfx/flags/small/KZR_neutrality.tga`
- `gfx/flags/small/SOG.tga`
- `gfx/flags/small/SOG_communism.tga`
- `gfx/flags/small/SOG_democratic.tga`
- `gfx/flags/small/SOG_fascism.tga`
- `gfx/flags/small/SOG_neutrality.tga`
- `gfx/flags/small/KHW.tga`
- `gfx/flags/small/KHW_communism.tga`
- `gfx/flags/small/KHW_democratic.tga`
- `gfx/flags/small/KHW_fascism.tga`
- `gfx/flags/small/KHW_neutrality.tga`
- `gfx/flags/small/ALN.tga`
- `gfx/flags/small/ALN_communism.tga`
- `gfx/flags/small/ALN_democratic.tga`
- `gfx/flags/small/ALN_fascism.tga`
- `gfx/flags/small/ALN_neutrality.tga`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/`

## Exact Surface Changed

Only the small flag TGA export format for the ancient-restoration custom Event 005 tags `KZR`, `SOG`, `KHW`, and `ALN` changed. Each base plus `_communism`, `_democratic`, `_fascism`, and `_neutrality` small flag was rebuilt from the current normal-size flag art and promoted back to `gfx/flags/small/`.

Normal and medium flags were used only as source evidence and were not edited. No default base flags were created for vanilla-supported existing countries.

## Before And After

Before: the 20 scoped small flags existed and were `10x7`, but direct TGA header checks showed they were 8 bpp.

After: all 20 scoped small flags are `10x7`, 32 bpp, bottom-origin TGAs with descriptor `0x08`.

## Portrait Status

No new portrait batch was created. Direct audit of `gfx/leaders/005_soviet_collapse/` found `47` Event 005 leader DDS files, all `156x210`, with zero duplicate SHA-256 groups and zero vanilla leader DDS hash matches. The 2026-05-26 release council sidecar for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` remains valid.

## Flag Status

Direct audit checked 33 custom/cosmetic Event 005 flag families, including `UKR_BLACK_BANNER`, across base plus four ideology variants and normal, medium, and small outputs.

Result after this fix:

- missing custom/cosmetic flag files: `0`
- malformed checked TGA headers: `0`
- base/ideology duplicate hash groups within checked normal-size tag families: `0`
- default flag overrides for vanilla-supported ordinary/internal tags: `0`

## Validation Run

- DDS leader header and hash audit: passed.
- Vanilla leader hash comparison against `~/projects/Hearts of Iron IV/gfx/leaders/`: passed.
- TGA flag presence, dimension, bpp, origin, and descriptor audit: passed after this fix.
- Existing-country default flag override audit: passed.

Audit artifacts:

- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/notes/tga_header_audit.tsv`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/notes/touched_small_flags.txt`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_26_ancient_small_flag_bpp_fix/contact_sheets/ancient_small_flag_bpp_fix_contact.png`

## Remaining Issues

No safe generated portrait or fictional/route flag batch remains in this scoped sidecar surface. The duplicate focus-icon assignment concern recorded in the main asset manifest is outside this generated leader portrait and flag sidecar scope.
