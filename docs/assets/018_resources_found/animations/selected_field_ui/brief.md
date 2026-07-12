# Event 018 selected-field UI animation brief

## Scope

This package supplies the art already registered by `interface/018_resources_found.gfx` for the selected resource-field header. It does not change GFX, GUI, gameplay, localisation, focus, idea, decision, category, or achievement files.

## Shared visual system

- Subject: a compact 1930s industrial and geological authority medallion over physical rock strata.
- Frame size: 128 by 128 pixels for every state image.
- Placement fit: the live icon origin is x 290, y 4 inside the 438 by 172 selection area, so a 128 by 128 frame occupies x 290 through 417 and y 4 through 131.
- Anchor: center, with the lower edge of the medallion and strata base held stable.
- Source mode: generated fictional art through the built-in image-generation workflow. Each atlas panel is separately illustrated from the written frame plan, then preserved as an individual source-frame PNG.
- Transparency: flat chroma-green source background removed locally, with transparent unused pixels retained in processed PNG and DDS outputs.
- Style: period industrial illustration, engraved and painterly HOI4-scale finish, dark steel, tarnished brass, coal black, slate grey, concrete grey, rust brown, and limited safety red.
- No baked text, labels, numerals, logos, watermarks, modern PPE, modern machinery, magical glow, generic horror faces, or creatures before the breach state.

## Runtime animations

| State | In-game use | Frames | FPS | Sheet size | Loop | Play on show | Static fallback | Sprites |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| Seal | Safe active field and productive development | 10 | 8 | 1280 by 128 | Yes | Yes | Frame 000 | `GFX_018_resource_field_seal`, `GFX_018_resource_field_seal_animated` |
| Unsafe | Low workforce-safety field without revealed disturbance | 10 | 8 | 1280 by 128 | Yes | Yes | Frame 000 | `GFX_018_resource_field_unsafe`, `GFX_018_resource_field_unsafe_animated` |
| Disturbance | Revealed physical subsurface disturbance before public breach | 12 | 9 | 1536 by 128 | Yes | Yes | Frame 000 | `GFX_018_resource_field_disturbance`, `GFX_018_resource_field_disturbance_animated` |
| Breach | Public open-breach crisis | 12 | 10 | 1536 by 128 | Yes | Yes | Frame 000 | `GFX_018_resource_field_breach`, `GFX_018_resource_field_breach_animated` |
| Sealing | Active full-seal works | 12 | 8 | 1536 by 128 | Yes | Yes | Frame 000 | `GFX_018_resource_field_sealing`, `GFX_018_resource_field_sealing_animated` |

## Static state art

| State | In-game use | Size | Sprite |
| --- | --- | ---: | --- |
| Suspended | Guarded reserve with idle machinery and a locked work gate | 128 by 128 | `GFX_018_resource_field_suspended` |
| Closed | Permanent concrete-and-steel seal with extraction symbols removed | 128 by 128 | `GFX_018_resource_field_closed` |

## Panel

- Runtime size: 470 by 304 pixels.
- Sprite: `GFX_018_resource_field_panel`.
- Function: compact dark industrial parchment and steel frame behind the title, state name, values, medallion, and five bottom controls.
- Layout protection: quiet readable field on the left and center, a recessed medallion zone on the right around x 306 to 434 and y 86 to 214, and an uncluttered bottom control strip from y 258 downward.
- No text is baked into the panel.

## Reference basis

- Offline wiki: Interface modding, Scripted GUI modding, and Graphical asset modding.
- Official vanilla documentation: `common/scripted_guis/_documentation.md`.
- Vanilla animation precedent: `interface/countryintelligenceagencyview.gfx` and `interface/countryintelligenceagencyview.gui`, where the 11-frame `GFX_agency_upgrade_anim` sheet is displayed through an `iconType`.
- Chaos Redux visual precedents inspected: the camp-repression ledger window background, Event 017 pressure-seal source atlas, and Event 014 animated warning and signal-card contact sheets.

## Output paths

- Source and processed frames: `docs/assets/018_resources_found/animations/selected_field_ui/`.
- Panel and static-state sources: `docs/assets/018_resources_found/source_png/gui/`.
- Panel and static-state processed PNGs: `docs/assets/018_resources_found/processed_png/gui/`.
- Runtime panel/static DDS: `gfx/interface/018_resources_found/`.
- Runtime sheets and fallbacks: `gfx/interface/animated/018_resources_found/`.
- Review GIFs and contact sheets: within this package's `previews/` and `contact_sheets/` folders.
