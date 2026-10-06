# shared_chaosx_buildings GFX fix report

Disposition: implemented and parent-reviewed building graphics; live consumer review remains user-owned.

Source plan: `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` lines 1139-1147.
Raw issue source: `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_issues.json` rows 641-643.
The group has three findings: one severity 2 and two severity 3.
The machine manifest is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/manifest.json`.
The asset handoff is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/gfx_handoff.md`.

## Finding dispositions

- Severity 2, `GFX_building_gulag_labor_camp_network`: implemented as a distinct 27x23 orange-on-transparent timber barracks, watchtower and logging spur icon, plus original ImageGen frame 36 art on a 46x46 dark plate; parent visual review passed, runtime promotion awaits parent wiring.
- Severity 3, `GFX_building_biowarfare_facility`: the optional alias replacement is the exact existing dark-plate frame 32 extracted from the frozen building strip; parent may repoint the unused alias to that 46x46 DDS or retire the alias.
- Severity 3, `GFX_building_cw_facility`: the optional alias replacement is the exact existing dark-plate frame 33 extracted from the frozen building strip; parent may repoint the unused alias to that 46x46 DDS or retire the alias.

## Sources and reference evidence

The canonical contact sheet was inspected first at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/buildings/contact_sheet.png` (SHA-256 `d480b9161608ff3f0093a72c2c2d533125dd957a4fd278e24de048fa12dc4bbd`).
Individual references inspected from the same canonical family were `fort.png` (27x23, SHA-256 `560f14a3112783d4273536ccfcfc555d6ff7f3bd8cd4c1a86ac52a04330cd675`) and `building_railway_gun.png` (46x46, SHA-256 `a3e9e58907313b252ada53acd6037b9cce2284affaf8118a46b1bfce599740d9`).
The installed vanilla `interface/countrystateview.gfx` registers `GFX_buildings_strip` with 31 frames and `GFX_building_fort_icon` at lines 191-205.
The installed vanilla `gfx/interface/buildings/building_icon_strip.dds` is 1426x46 with SHA-256 `973d29d4aacf12ca1659619422a4953f240c0def18bbed29a8c828dfd2a97f0f`; the vanilla `building_fort_icon.dds` is 27x23 with SHA-256 `a9c2b1d5354eb33d9237f5dde94c5335554d108ae1e243d1ea5e84180ca51c47`.
The current Chaos Redux strip was frozen at `gfx/interface/buildings/building_icon_strip.dds` with SHA-256 `c010949226860dd9820746c4ddb36cc89d2464ea9696d75682dae4520a1e175b`, 1610x46 and 35 frames.
Frames 32 and 33 in that frozen strip are the existing biowarfare and CW dark-plate glyphs; frames 34 and 35 are the camp icons.

## Generated sources and processed candidates

The standalone Gulag source is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/source_pngs/building_gulag_labor_camp_network.png` (SHA-256 `0f15452cf77e97c8495cc373fef21ae0346d1a75bd508b87cf5fc5d59edc35de`); its full prompt is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/prompts/building_gulag_labor_camp_network.md`.
The generated frame 36 source is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/source_pngs/building_gulag_labor_camp_network_strip_frame36.png` (SHA-256 `0d2414461f5952ee6eea21de0e6732e8ffbcd96aa1fb060a0785f45fc07daf83`); its full prompt is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/prompts/building_gulag_labor_camp_network_strip_frame36.md`.
Both calls used built-in ImageGen with `transparent_background=true`; unused canvas is transparent in the source and processed PNGs.
The standalone preview is `processed_pngs/building_gulag_labor_camp_network.png` at 27x23, and the plate cell is `processed_pngs/building_gulag_labor_camp_network_strip_frame36.png` at 46x46.
The strip assembly is `processed_pngs/building_icon_strip.png` at 1656x46 with 36 frames.
The first 35 cells compare pixel-for-pixel with the frozen source strip.
A selective orange-luminance lift was applied only to warm orange pixels of the generated icon layers; its exact channel mask and factors are recorded in `evidence/building_processing_report.json`; alpha was unchanged.
The optional biowarfare and CW alias PNGs are exact extractions of frames 32 and 33, with their extraction notes in `prompts/building_biowarfare_facility_frame32_extraction.md` and `prompts/building_cw_facility_frame33_extraction.md`.
All five DDS candidates passed strict canonical BGRA decoding and pixel equality against their processed PNGs.
The full strip DDS candidate is `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/dds_candidates/gfx/interface/buildings/building_icon_strip.dds` (1656x46, SHA-256 `580e4ccb2de2b44d3a20cb7041dd46a7907dc563caf871d7daf9225f7c25cc48`).
Its first 35 decoded frames are pixel-identical to the frozen strip.

## Exact parent wiring

- Repoint `GFX_building_gulag_labor_camp_network` in `interface/chaosx_buildings.gfx` to `gfx/interface/buildings/building_gulag_labor_camp_network.dds`.
- Set `GFX_buildings_strip` to 36 frames in the parent-owned narrow late GFX registration and set `@GULAG_NETWORK_ICON_FRAME = 36` in `common/buildings/chaosx_buildings.txt`.
- If the unused `GFX_building_biowarfare_facility` alias is retained, repoint it to `gfx/interface/buildings/building_biowarfare_facility.dds`, the extracted dark-plate frame 32.
- If the unused `GFX_building_cw_facility` alias is retained, repoint it to `gfx/interface/buildings/building_cw_facility.dds`, the extracted dark-plate frame 33.
- Keep the existing `GFX_buildings_strip` runtime path `gfx/interface/buildings/building_icon_strip.dds`; the candidate strip replaces that texture after parent review.

No GFX, GUI, common/buildings or other gameplay files were edited by this worker.
Costs, gameplay effects and localization were not changed.
The remaining live checks are that the state view shows the Gulag network in frame 36 beside distinct concentration/extermination camp icons, and any retained biowarfare/CW aliases show their dark-plate building frames at native UI size.


## Parent integration and references

The parent installed the standalone Gulag icon, the 36-frame strip, and both 46x46 dark-plate alias textures, and applied the three exact existing-sprite texture-path repoints.
`@GULAG_NETWORK_ICON_FRAME` selects 36 in the existing building definition; `interface/zz_chaosx_building_strip.gfx` supplies one late 36-frame registration without editing the shared `countrystateview.gfx` override.
The first 35 decoded cells remain pixel-identical; no building effects, costs, levels or gameplay setup changed.
The offline Building modding Icon section, lines 135-152, documents matching `icon_frame`, strip art and `noOfFrames`; Character modding Sprite, lines 631-654, documents later ASCII-filename sprite precedence.
Both local sections were read directly after `hoi4.reference_read` failed with `Transport closed`; exact source files are `paradox_wiki/Building modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`.
Installed `common/buildings/00_buildings.txt`, lines 1-66, supplies the native building schema/comments and `icon_frame` precedents; no dedicated installed graphics/icon-frame documentation section was found.
`hoi4.script_validate` for `common/buildings/chaosx_buildings.txt` also failed with `Transport closed`; no engine validation is claimed.
The linked current group sheet is retained at `docs/assets/gfx_fix_2026-10/shared_chaosx_buildings/evidence/current_linked_sheet/`.
