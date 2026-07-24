# Event 012 priority-member focus icon handoff

## Scope

Produced the eight missing national focus icon assets registered in `interface/012_africa_priority_member_assets.gfx` and consumed by `common/national_focus/012_africa_priority_member_focus.txt`.

The work stayed within the bounded icon family and did not touch portrait work, gameplay, localisation, `.gfx`, GUI, spreadsheets, or other documentation surfaces.

## Files created

- `docs/assets/012_africa_priority_focus_icons/manifest.md`
- `docs/assets/012_africa_priority_focus_icons/crosswalk.md`
- `docs/assets/012_africa_priority_focus_icons/gfx_handoff.md`
- `docs/assets/012_africa_priority_focus_icons/prompts/prompts.md`
- `docs/assets/012_africa_priority_focus_icons/contact_sheets/focus_icons_contact_sheet.png`
- Eight ImageGen source PNGs under `docs/assets/012_africa_priority_focus_icons/source_png/`.
- Eight chroma-key-removed evidence PNGs with `_alpha` suffix under `docs/assets/012_africa_priority_focus_icons/processed_png/`.
- Eight exact-size processed PNG previews under `docs/assets/012_africa_priority_focus_icons/processed_png/`.
- Eight final DDS files under `gfx/interface/goals/012_africa/priority_members/`.

## Sprite and consumer crosswalk

| Focus id | Sprite | Runtime DDS |
| --- | --- | --- |
| `africa_priority_define_compact_country` | `GFX_goal_012_africa_priority_compact_country` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_compact_country.dds` |
| `africa_priority_ratify_political_settlement` | `GFX_goal_012_africa_priority_political_settlement` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_political_settlement.dds` |
| `africa_priority_build_distinct_institution` | `GFX_goal_012_africa_priority_distinct_institution` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_distinct_institution.dds` |
| `africa_priority_secure_economic_function` | `GFX_goal_012_africa_priority_economic_function` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_economic_function.dds` |
| `africa_priority_negotiate_league_role` | `GFX_goal_012_africa_priority_league_role` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_league_role.dds` |
| `africa_priority_resolve_overlap_question` | `GFX_goal_012_africa_priority_overlap_question` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_overlap_question.dds` |
| `africa_priority_field_national_force` | `GFX_goal_012_africa_priority_national_force` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_national_force.dds` |
| `africa_priority_write_post_settlement_programme` | `GFX_goal_012_africa_priority_post_settlement` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_post_settlement.dds` |

Each registered `_shine` sprite reuses its corresponding base DDS through the existing `gfx/FX/buttonstate.lua` definition.

## Generation evidence

All eight icons were generated independently with the official built-in ImageGen tool after inspecting the canonical contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png`.

ImageGen output paths and full prompts are recorded in `docs/assets/012_africa_priority_focus_icons/prompts/prompts.md`.

The source mode is `$imagegen` with a flat `#00ff00` chroma-key background, and the source PNGs remain retained as immutable generation evidence.

The compositions are intentionally distinct by route role: three-shield civic compact, treaty and scales, civic hall institution, granary and trade gear, League medallion, force shield and standard, congress overlap seal, and post-settlement ledger tree.

## Processing and conversion

The installed `remove_chroma_key.py` helper produced real alpha PNGs from each generated source.

Mechanical normalization cropped transparent margins, preserved the generated silhouette, and fitted each icon inside a transparent 94x86 RGBA canvas.

Final DDS files were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 94 --height 86`.

## Meaningful QA

The review contact sheet shows all eight final PNGs over a checkerboard at target size and confirms distinct silhouettes, central alignment, transparent corners, and no visible white matte, opaque square, or sticker rim.

Every processed PNG is exactly 94x86 RGBA with alpha range 0-255 and alpha-zero corners.

Every DDS is exactly 94x86, 32,464 bytes, has the legacy 128-byte header plus 94x86x4 payload, has pixel format size 32 and flags 65, has BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`, has `DDSCAPS_TEXTURE`, and retains transparent corners.

No `.gfx` edits were made because all eight sprite names and texture paths were already registered by the parent.

## Blockers and review state

All eight requested icons are complete and handed off.

No blockers, fallback art, reused icon masters, recoloured variants, or needs-user-review items remain in this bounded family.

The parent agent still owns final runtime review and any unrelated `.gfx`, focus, localisation, portrait, or documentation integration.
