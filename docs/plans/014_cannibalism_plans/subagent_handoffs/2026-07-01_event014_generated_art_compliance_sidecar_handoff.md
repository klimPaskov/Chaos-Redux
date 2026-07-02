# Event 014 Generated Art Compliance Sidecar Handoff

Scope: replaced/augmented the current procedural Event 014 non-icon art package with fictional `$imagegen` source art, processed PNG previews, final DDS/TGA files, a contact sheet, and provenance notes. No gameplay, localisation, event, decision, focus, spreadsheet, GUI, or `.gfx` files were edited.

## Reference And Source Mode

- Read `docs/specs/014_cannibalism_specs/prompts/014_cannibalism_asset_prompt.md`.
- Read `docs/specs/014_cannibalism_specs/prompts/014_cannibalism_super_event_prompt.md`.
- Read `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_4_world_end_super_events_assets.md`.
- Read the Chaos Redux event asset skill and `$imagegen` skill.
- Inspected reference folders:
  - `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
  - `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
  - `.agents/skills/chaos-redux-event-assets/assets/flags`
- Source mode for all new art: `$imagegen` generated fictional alternate-history war horror.
- Generation is appropriate because the requested assets are fictional, staged-documentary, symbolic, and CBL identity art requiring invented gore/horror without real gore photos or real extremist symbols.

## Created Or Updated Files

Source PNGs:

- `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/news_cannibalism_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_ritual_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_islands_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/super_event_cannibalism_network_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/report_event_cannibalism_hannibal_hook_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/leader_CBL_warlord_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/CBL_table_council_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/flag_CBL_generated_emblem_source.png`
- `docs/assets/014_cannibalism/generated_art_sources/generated_art_manifest.md`

Processed PNG previews:

- `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism.png`
- `docs/assets/014_cannibalism/generated_art_processed/news_cannibalism.png`
- `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_ritual.png`
- `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_islands.png`
- `docs/assets/014_cannibalism/generated_art_processed/super_event_cannibalism_network.png`
- `docs/assets/014_cannibalism/generated_art_processed/report_event_cannibalism_hannibal_hook.png`
- `docs/assets/014_cannibalism/generated_art_processed/leader_CBL_warlord.png`
- `docs/assets/014_cannibalism/generated_art_processed/CBL_table_council.png`
- `docs/assets/014_cannibalism/generated_art_processed/flag_CBL_82x52.png`
- `docs/assets/014_cannibalism/generated_art_processed/flag_CBL_41x26.png`
- `docs/assets/014_cannibalism/generated_art_processed/flag_CBL_10x7.png`

Final DDS/TGA files:

- `gfx/event_pictures/014_cannibalism/report_event_cannibalism.dds`
- `gfx/event_pictures/014_cannibalism/news_cannibalism.dds`
- `gfx/event_pictures/014_cannibalism/report_event_cannibalism_ritual.dds`
- `gfx/event_pictures/014_cannibalism/report_event_cannibalism_islands.dds`
- `gfx/super_events/014_cannibalism/super_event_cannibalism_network.dds`
- `gfx/event_pictures/014_cannibalism/report_event_cannibalism_hannibal_hook.dds`
- `gfx/leaders/014_cannibalism/leader_CBL_warlord.dds`
- `gfx/leaders/014_cannibalism/CBL_table_council.dds`
- `gfx/flags/CBL.tga`
- `gfx/flags/medium/CBL.tga`
- `gfx/flags/small/CBL.tga`

Contact sheet:

- `docs/assets/014_cannibalism/generated_art_contact_sheets/event014_generated_non_icon_contact_sheet.png`

## Processing Notes

- Report images: generated source photos were locally processed into the report-event house style at 210x176 with black-and-white sepia treatment, paper border, slight tilt, transparent corners, and drop shadow.
- News image: generated source was cropped to 397x153, converted to black-and-white, contrast-adjusted, sharpened, and lightly grained.
- Super-event image: generated source was cropped to 457x328 with subdued color, contrast, sharpening, and a mild vignette for readability.
- Leader portraits: generated sources were cropped to 156x210 and processed with subdued HOI4-style portrait contrast and a narrow dark border.
- Flag: generated source emblem was processed into 82x52, 41x26, and 10x7 TGA files for CBL base flag lookup.

## Sprite And Wiring Handoff

Existing `interface/014_cannibalism.gfx` currently points Event 014 art at older paths such as `gfx/event_pictures/014_cannibalism/...`, `gfx/super_events/014_cannibalism/...`, and `gfx/leaders/014_cannibalism/...`. This sidecar did not edit `.gfx` and stayed inside the owned write scope, so the final DDS files preserve basenames but live in the new owned paths.

Suggested parent wiring in `interface/014_cannibalism.gfx`:

- Keep `GFX_report_event_cannibalism`; change texturefile to `gfx/event_pictures/014_cannibalism/report_event_cannibalism.dds`.
- Keep `GFX_news_cannibalism`; change texturefile to `gfx/event_pictures/014_cannibalism/news_cannibalism.dds`.
- Keep `GFX_report_event_cannibalism_ritual`; change texturefile to `gfx/event_pictures/014_cannibalism/report_event_cannibalism_ritual.dds`.
- Keep `GFX_report_event_cannibalism_islands`; change texturefile to `gfx/event_pictures/014_cannibalism/report_event_cannibalism_islands.dds`.
- Keep `GFX_super_event_cannibalism_network`; set texturefile to `gfx/super_events/014_cannibalism/super_event_cannibalism_network.dds`.
- Add or wire proposed `GFX_report_event_cannibalism_hannibal_hook` to `gfx/event_pictures/014_cannibalism/report_event_cannibalism_hannibal_hook.dds` if the Hannibal/unifier hook receives a visible event surface.
- Add or wire proposed `GFX_portrait_CBL_warlord` to `gfx/leaders/014_cannibalism/leader_CBL_warlord.dds` if CBL uses the one-person fictional leader portrait. This portrait is male-presenting; gameplay should use male leader metadata and a male small random name pool, not a generic office title and not female metadata.
- Keep `GFX_portrait_CBL_table_council`; use `gfx/leaders/014_cannibalism/CBL_table_council.dds` if the institutional council remains the active CBL portrait. This is a collective institutional portrait, so gameplay should use an institutional name rather than a personal random-name pool.
- CBL base flag files were updated at `gfx/flags/CBL.tga`, `gfx/flags/medium/CBL.tga`, and `gfx/flags/small/CBL.tga`. Ideology variants and `CBL_LAST_TABLE` flags were not changed by this sidecar.

## Uncertain Fit And Parent Follow-Up

- The parent asset-organization pass placed the generated super-event DDS under `gfx/super_events/014_cannibalism/` and wired `GFX_super_event_cannibalism_network` to that path.
- The source prompt for the Hannibal/unifier hook avoids a final Hannibal likeness and uses a back-turned unknown commander. This matches the current blocker that Hannibal-specific identity is not finalized.
- Only the CBL base flag was regenerated into final TGA files. CBL ideology variants and Last Table cosmetic flags remain outside this sidecar unless the parent grants or requests that specific asset pass.

## Validation Notes

- Processed report PNGs are 210x176 RGBA with transparent corners.
- News PNG and DDS are 397x153.
- Super-event PNG and DDS are 457x328.
- Leader DDS files are 156x210.
- CBL flag TGAs are 82x52, 41x26, and 10x7.
- Contact sheet exists and shows the generated non-icon set.
