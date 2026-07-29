# Event 012 Africa Focus Icon Asset Handoff

## Handoff status

Asset production is complete for all 13 unique focus-family sprite IDs currently referenced by `common/national_focus/012_africa_continental_focus_tree.txt` and undefined at the start of this tranche.

The deliverable includes 13 unchanged generated source masters, 13 alpha intermediates, 13 processed PNGs, 13 final HOI4 DDS textures, three contact sheets, a validation ledger, a prompt/provenance record, a matrix crosswalk, a reproducible processing script, and a ready-to-copy `.gfx` registration block.

## Exact delivered sprite IDs

| Sprite ID | Current tree uses | Matrix disposition |
| --- | ---: | --- |
| `GFX_goal_africa_focus_family_host_proclamation` | 12 | direct match: `focus_family_host_proclamation` |
| `GFX_goal_africa_focus_family_host_legitimacy` | 34 | direct match: `focus_family_host_legitimacy` |
| `GFX_goal_africa_focus_family_charter_law` | 25 | direct match: `focus_family_charter_law` |
| `GFX_goal_africa_focus_family_continental_representation` | 36 | direct match: `focus_family_continental_representation` |
| `GFX_goal_africa_focus_family_protection_guarantee` | 32 | direct match: `focus_family_protection_guarantee` |
| `GFX_goal_africa_focus_family_volunteer_intervention` | 1 | direct match: `focus_family_volunteer_intervention` |
| `GFX_goal_africa_focus_family_aid_and_relief` | 23 | direct match: `focus_family_aid_and_relief` |
| `GFX_goal_africa_focus_family_regional_congress` | 33 | direct match: `focus_family_regional_congress` |
| `GFX_goal_africa_focus_family_road_corridor` | 1 | direct match: `focus_family_road_corridor` |
| `GFX_goal_africa_focus_family_rail_corridor` | 32 | direct match: `focus_family_rail_corridor` |
| `GFX_goal_africa_focus_family_army_common_reserve` | 23 | direct match: `focus_family_army_common_reserve` |
| `GFX_goal_africa_focus_family_resource_sovereignty` | 23 | direct match: `focus_family_resource_sovereignty` |
| `GFX_goal_africa_focus_family_rival_bloc` | 1 | direct match: `focus_family_rival_bloc` |
| **Total references** | **276** | **13 direct; 0 derived; 0 unmatched** |

## Delivered paths

- Final DDS textures: `gfx/interface/goals/012_africa/`
- Complete asset package: `docs/assets/012_africa/focus_icons_imagegen/`
- Manifest: `docs/assets/012_africa/focus_icons_imagegen/manifest.md`
- Requirement/runtime crosswalk: `docs/assets/012_africa/focus_icons_imagegen/coverage_crosswalk.md`
- Prompt and source record: `docs/assets/012_africa/focus_icons_imagegen/prompts/focus_icon_prompts.md`
- Ready-to-copy regular and `_shine` definitions: `docs/assets/012_africa/focus_icons_imagegen/gfx_handoff.md`
- Processed visual review sheet: `docs/assets/012_africa/focus_icons_imagegen/contact_sheets/focus_icon_processed_checker_contact_sheet.png`
- Decoded-DDS visual review sheet: `docs/assets/012_africa/focus_icons_imagegen/contact_sheets/focus_icon_dds_decoded_contact_sheet.png`
- Technical/hash ledger: `docs/assets/012_africa/focus_icons_imagegen/validation/focus_icon_validation.tsv`
- Rebuild script: `docs/assets/012_africa/focus_icons_imagegen/process_focus_icons.py`

## Technical and visual evidence

- Every final texture is 94 x 86, legacy uncompressed 32-bit BGRA DDS with real alpha and no mipmaps.
- Each DDS decodes pixel-for-pixel identically to its processed PNG.
- All four corner pixels are fully transparent for every icon.
- No visible `#ff00ff` key-color pixel remains.
- All 13 normalized RGBA hashes are unique.
- Visual review confirmed legible, distinct silhouettes and dignified institutional, relief, infrastructure, and military symbolism without readable text, real insignia, colonial symbols, tribal-mask shorthand, animalization, safari imagery, or protected medical emblems.

## Provenance and licensing

All 13 source masters are independent original generations made through the built-in OpenAI image-generation tool on 2026-07-17. The unchanged returned PNGs are retained under `source_png/`. No external image, third-party mod asset, vanilla texture, real emblem, or licensed source was incorporated into the deliverables. Vanilla references were inspected only for small-icon composition and technical precedent.

## Parent integration action

Add the ready-to-copy sprite block from `gfx_handoff.md` to `interface/012_africa.gfx` or the canonical Event 012 sprite file created by the parent. It registers 13 regular IDs and the required 13 `_shine` IDs while reusing each final DDS for its shine state.

No gameplay, `.gfx`, `.gui`, localisation, spreadsheet, specification, or existing Event 012 source file was edited by this asset tranche.

## Scope boundary and simplifications

No simplifications or omissions were made within the assigned family-level asset scope: all 13 requested live IDs have complete source-to-DDS packages and direct matrix reconciliation.

The source matrix separately calls for one distinct icon per final focus through `<focus_slug>` variants. The current focus tree consumes shared family-level sprite IDs, so that broader per-focus expansion remains a planned Event 012 design task and is not represented as complete here. Runtime registration is complete for the thirteen current family consumers; the broader per-focus expansion remains deferred.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`

## Release-candidate correction (2026-07-29)

The runtime-registration note above is historical. `interface/012_africa.gfx` now registers all thirteen regular focus-family sprites and their thirteen shine sprites, and the thirteen final DDS textures are present under `gfx/interface/goals/012_africa/`. The final focus re-audit and registration scan report no active blocker for these consumers. The broader matrix request for one distinct icon per final focus remains deferred.
