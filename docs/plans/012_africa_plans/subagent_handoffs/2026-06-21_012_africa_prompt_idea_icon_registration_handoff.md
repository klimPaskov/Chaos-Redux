# 012 Africa Prompt Idea Icon Registration Handoff

Date: 2026-06-21

## Scope

Register the prompt-listed Event 012 Africa idea icon DDS files that already existed in the live asset folder but did not have matching `GFX_idea_*` entries in `interface/012_africa.gfx`.

## Files changed

- `interface/012_africa.gfx`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`

## Registered sprites

- `GFX_idea_africa_paper_cores`
- `GFX_idea_africa_proclamation_without_machinery`
- `GFX_idea_africa_regional_trust`
- `GFX_idea_africa_colonial_alarm`
- `GFX_idea_africa_liberation_momentum`
- `GFX_idea_africa_congress_legitimacy`
- `GFX_idea_africa_continental_general_staff`
- `GFX_idea_africa_green_covenant`
- `GFX_idea_africa_diaspora_return_cadres`
- `GFX_idea_africa_scramble_pressure`

## Evidence

The image package `docs/assets/012_africa/icon_regen_prompt_idea_icons_2026_06_21/` already contains generated source PNGs, processed PNGs, DDS copies, live DDS files, and validation sheets for the 12 prompt-listed idea ids. Its validation summary records transparent corners, no transparent white pixels, no opaque square background, and distinct idea-vs-goal compositions.

The live DDS audit run during this patch found:

- all 13 goal icons decode at `94x86` with `white_opaque = 0`;
- all 20 live idea DDS files decode at `64x64`;
- the 10 newly registered prompt-listed idea DDS files have `white_opaque = 0`;
- no registered prompt-listed sprite path points to a missing DDS file.

## Remaining risk

This is a registration/documentation patch only. It does not regenerate additional artwork and does not close live in-game UI render proof for the broader Continental Congress panel.
