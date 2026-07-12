# Event 018 Generated Event Art Handoff

## Result

The complete reserved raster tranche is delivered: 10 report images, 6 news images, 3 super-event images, literal Vhorruk and all three implemented Oth-Kesh commanders, an 8-frame Vhorruk animation package, five DHO political flag identities, and the implemented `DHO_WORLD_BELOW` cosmetic flag. No `.gfx`, `.gui`, gameplay, localisation, or spreadsheet file was edited by this worker.

## Runtime files

- Reports: `gfx/event_pictures/018_resources_found/` — 10 DDS files, each `210x176`.
- News: `gfx/event_pictures/news/018_resources_found/` — 6 DDS files, each `397x153`, from true-grayscale PNGs.
- Super events: `gfx/super_events/018_resources_found/` — 3 DDS files, each `457x328`.
- Leaders: `gfx/leaders/018_resources_found/` — Vhorruk, Thessik, Orrukesh, and Khalvek large portraits at `156x210`; three commander-small portraits at `50x67`; Vhorruk animation at `1248x210`.
- Flags: `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` — `DHO`, `DHO_democratic`, `DHO_fascism`, `DHO_communism`, `DHO_neutrality`, and `DHO_WORLD_BELOW` at `82x52`, `41x26`, and `10x7`.

Every DDS is one-mip 32-bit BGRA. Every TGA is uncompressed 32-bit with bottom-left origin and 8 alpha bits.

## Stable identifiers

Reports:

- `GFX_report_event_018_resource_discovery`
- `GFX_report_event_018_compound_field`
- `GFX_report_event_018_sick_workings`
- `GFX_report_event_018_missing_shift`
- `GFX_report_event_018_first_evidence`
- `GFX_report_event_018_perimeter_breach`
- `GFX_report_event_018_evacuation`
- `GFX_report_event_018_monster_hunt`
- `GFX_report_event_018_full_seal`
- `GFX_report_event_018_anchor_cleanup`

News:

- `GFX_news_event_018_global_resource_field`
- `GFX_news_event_018_border_crisis`
- `GFX_news_event_018_public_attack`
- `GFX_news_event_018_cave_country_emergence`
- `GFX_news_event_018_regional_containment`
- `GFX_news_event_018_global_defeat`

Super events:

- `GFX_super_event_018_cave_emergence`
- `GFX_super_event_018_world_end`
- `GFX_super_event_018_global_defeat`

Characters:

- `GFX_portrait_DHO_vhorruk`
- `GFX_portrait_DHO_vhorruk_animated`
- `GFX_portrait_DHO_thessik` and `GFX_portrait_DHO_thessik_small`
- `GFX_portrait_DHO_orrukesh` and `GFX_portrait_DHO_orrukesh_small`
- `GFX_portrait_DHO_khalvek` and `GFX_portrait_DHO_khalvek_small`

## Vhorruk animation

- Eight distinct generated/edit source frames, not transform-only animation.
- Normalized frame size: `156x210`.
- Horizontal sheet: `1248x210`.
- Runtime DDS: `gfx/leaders/018_resources_found/portrait_DHO_vhorruk_animated.dds`.
- Static country-leader presentation: `gfx/leaders/018_resources_found/portrait_DHO_vhorruk.dds`.
- Recommended declaration: `frameAnimatedSpriteType`, `noOfFrames = 8`, `animation_rate_fps = 4`, `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0`, `alwaystransparent = yes`.
- Preview: `docs/assets/018_resources_found/animations/portrait_dho_vhorruk/previews/portrait_DHO_vhorruk_preview.gif`.

Keep the character definition's large portrait static. For the animated event-log surface, change only the Event 018 branch of `GetEventsLogSelectedEvolutionPortrait` from `GFX_portrait_DHO_vhorruk` to `GFX_portrait_DHO_vhorruk_animated` after registering the animated sprite.

## Parent wiring

- Put report and news registrations in `interface/018_resources_found.gfx`.
- Put the three super-event registrations in `interface/chaosx_super_events.gfx`; scripted localisation already maps display values 82/83/84.
- Put portrait registrations in `interface/chaosx_characters.gfx`.
- Make the event-log animated-key switch in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.
- Flags require no GFX declarations. Preserve exact cosmetic token `DHO_WORLD_BELOW`.

Copy-ready declaration blocks and exact texture paths are in `docs/assets/018_resources_found/generated_event_art_gfx_handoff.md`.

## Review surfaces

The exhaustive manifest is `docs/assets/018_resources_found/generated_event_art_manifest.md`. Source, processed, final-size flag, animation, and super-event UI-mask contact sheets are all under `docs/assets/018_resources_found/contact_sheets/`.

## Meaningful validation

`docs/assets/018_resources_found/_tooling/process_event_018_raster_assets.py` completed successfully with the verified report processor SHA-256 `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9`. It proved DDS pixel identity and format, report corner transparency, news grayscale mode, TGA dimensions/origin/pixel identity, distinct flag identities, distinct Vhorruk source and processed frames, an 8-frame GIF, and a static fallback identical to frame 1.

Visual review found and corrected two generations before final export: a first-evidence image with recognizable insignia and a communism flag with a saltire-like composition. Both rejected sources are retained under `docs/assets/018_resources_found/notes/` and are not used by runtime files.

## Simplifications, omissions, and blockers

None inside the assigned raster scope. Optional collective/world-end route portraits were not mapped by the final implementation and were therefore correctly not produced. The only remaining work is the parent-owned registration described above; there is no unresolved asset-production risk.

## Git

No commit was created, as requested.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-subagents`
- `imagegen`
