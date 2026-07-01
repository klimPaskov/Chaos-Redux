# Event 015 Cosmetic Flag Asset Handoff

Date: 2026-07-01
Subagent scope: `chaosx_generated_event_art`, `fork_context=false`
Source mode: `$imagegen` built-in image generation
Asset type: fictional HOI4 cosmetic flags

## Process Notes

- Inspected the Chaos Redux flag reference folder: `.agents/skills/chaos-redux-event-assets/assets/flags/`.
- Used `$imagegen` to create one source artwork per fictional late Event 015 identity.
- Copied generated outputs from `C:/Users/klimp/.codex/generated_images/019f1d1f-a88a-7ef3-b448-c9c645fdf4d5/` into the Event 015 source PNG folder with stable filenames.
- Processed each source into an opaque 82x52 preview PNG, then exported HOI4 flag TGAs at normal, medium, and small sizes.
- Did not edit gameplay files, localisation, interface `.gfx`, achievement files, focus/decision/idea/icon assets, or the existing Event 015 asset manifest.
- Manifest-style entries are included in this handoff because the existing `docs/assets/015_utopia_manifesto/manifest.md` was intentionally left untouched.

## Created Files

### Source PNGs

- `docs/assets/015_utopia_manifesto/source_png/flag_utopia_new_utopia_source.png`
- `docs/assets/015_utopia_manifesto/source_png/flag_utopia_necessary_commonwealth_source.png`
- `docs/assets/015_utopia_manifesto/source_png/flag_utopia_league_of_need_source.png`
- `docs/assets/015_utopia_manifesto/source_png/flag_utopia_marked_bounds_state_source.png`

### Processed Preview PNGs

- `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_new_utopia_processed.png`
- `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_necessary_commonwealth_processed.png`
- `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_league_of_need_processed.png`
- `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_marked_bounds_state_processed.png`

### Final TGA Flags

- `gfx/flags/utopia_new_utopia.tga`
- `gfx/flags/medium/utopia_new_utopia.tga`
- `gfx/flags/small/utopia_new_utopia.tga`
- `gfx/flags/utopia_necessary_commonwealth.tga`
- `gfx/flags/medium/utopia_necessary_commonwealth.tga`
- `gfx/flags/small/utopia_necessary_commonwealth.tga`
- `gfx/flags/utopia_league_of_need.tga`
- `gfx/flags/medium/utopia_league_of_need.tga`
- `gfx/flags/small/utopia_league_of_need.tga`
- `gfx/flags/utopia_marked_bounds_state.tga`
- `gfx/flags/medium/utopia_marked_bounds_state.tga`
- `gfx/flags/small/utopia_marked_bounds_state.tga`

### Contact Sheet

- `docs/assets/015_utopia_manifesto/contact_sheets/utopia_cosmetic_flags_imagegen_contact.png`

## Asset Entries

### `utopia_new_utopia`

- Related event: Event 015, Utopian Manifesto
- Asset type: fictional cosmetic flag
- Intended in-game use: late Event 015 New Utopia identity/cosmetic tag flag
- Source mode: `$imagegen`
- Why generation is appropriate: fictional alternate-history civic-state identity with no real historical flag source
- Visual identity: civic ledger and rising storehouse/granary, green-red civic field, centered emblem
- Source PNG: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_new_utopia_source.png`
- Processed PNG: `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_new_utopia_processed.png`
- Final paths: `gfx/flags/utopia_new_utopia.tga`, `gfx/flags/medium/utopia_new_utopia.tga`, `gfx/flags/small/utopia_new_utopia.tga`
- Target sizes: 82x52, 41x26, 10x7
- Sprite name / `.gfx`: not needed; HOI4 flags are engine-facing files under `gfx/flags/`
- Status: complete

Prompt summary: fictional 1930s/40s civic-state flag, centered ledger fused with a rising granary/storehouse, textile banner art, readable at HOI4 flag sizes, no text, no real-world coats of arms, no white-background icon look.

### `utopia_necessary_commonwealth`

- Related event: Event 015, Utopian Manifesto
- Asset type: fictional cosmetic flag
- Intended in-game use: late Event 015 Necessary Commonwealth identity/cosmetic tag flag
- Source mode: `$imagegen`
- Why generation is appropriate: fictional alternate-history guarded-commonwealth identity with no real historical flag source
- Visual identity: guarded common store, fortified ledger, lock-shield, heavy red-blue-gold field
- Source PNG: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_necessary_commonwealth_source.png`
- Processed PNG: `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_necessary_commonwealth_processed.png`
- Final paths: `gfx/flags/utopia_necessary_commonwealth.tga`, `gfx/flags/medium/utopia_necessary_commonwealth.tga`, `gfx/flags/small/utopia_necessary_commonwealth.tga`
- Target sizes: 82x52, 41x26, 10x7
- Sprite name / `.gfx`: not needed; HOI4 flags are engine-facing files under `gfx/flags/`
- Status: complete

Prompt summary: fictional 1930s/40s state flag, central lock-shield over granary vault and public account book, fortress-like framing, readable at small sizes, no text or real-world heraldry.

### `utopia_league_of_need`

- Related event: Event 015, Utopian Manifesto
- Asset type: fictional cosmetic flag
- Intended in-game use: late Event 015 League of Need identity/cosmetic tag flag
- Source mode: `$imagegen`
- Why generation is appropriate: fictional alternate-history aid-league identity with no real historical flag source
- Visual identity: aid corridors, bridge, paired storehouses, teal-ochre-red route field
- Source PNG: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_league_of_need_source.png`
- Processed PNG: `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_league_of_need_processed.png`
- Final paths: `gfx/flags/utopia_league_of_need.tga`, `gfx/flags/medium/utopia_league_of_need.tga`, `gfx/flags/small/utopia_league_of_need.tga`
- Target sizes: 82x52, 41x26, 10x7
- Sprite name / `.gfx`: not needed; HOI4 flags are engine-facing files under `gfx/flags/`
- Status: complete

Prompt summary: fictional 1930s/40s state flag, central arched bridge connecting two granary warehouses with aid-corridor route bands, readable at tiny flag size, no text or modern logos.

### `utopia_marked_bounds_state`

- Related event: Event 015, Utopian Manifesto
- Asset type: fictional cosmetic flag
- Intended in-game use: late Event 015 Marked Bounds State identity/cosmetic tag flag
- Source mode: `$imagegen`
- Why generation is appropriate: fictional alternate-history survey/boundary-state identity with no real historical flag source
- Visual identity: severe survey marker, crossed measuring rods, boundary stakes, black-green tan field
- Source PNG: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_marked_bounds_state_source.png`
- Processed PNG: `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_marked_bounds_state_processed.png`
- Final paths: `gfx/flags/utopia_marked_bounds_state.tga`, `gfx/flags/medium/utopia_marked_bounds_state.tga`, `gfx/flags/small/utopia_marked_bounds_state.tga`
- Target sizes: 82x52, 41x26, 10x7
- Sprite name / `.gfx`: not needed; HOI4 flags are engine-facing files under `gfx/flags/`
- Status: complete

Prompt summary: fictional 1930s/40s severe administrative state flag, central survey marker and measuring rods with boundary-post perimeter motifs, readable at tiny flag size, no text or real-world heraldry.

## Validation

- Source PNG dimensions:
  - `utopia_new_utopia`: 1577x997 RGB
  - `utopia_necessary_commonwealth`: 1577x997 RGB
  - `utopia_league_of_need`: 1536x1024 RGB
  - `utopia_marked_bounds_state`: 1536x1024 RGB
- Processed previews are 82x52 RGBA with fully opaque alpha.
- Final normal flags are 82x52, medium flags are 41x26, and small flags are 10x7.
- Final TGAs use uncompressed 32-bit TGA headers matching `gfx/flags/THR.tga`: image type 2, 32-bit pixels, descriptor 8, bottom-origin, 8 alpha bits.
- Alpha is fully opaque in all final TGA files, which is appropriate for HOI4 flags.
- Contact sheet inspection: all four full-size flags are centered; 10x7 previews retain distinct color/value identities. At 10x7, the New Utopia and Necessary Commonwealth emblems reduce to small central gold marks, while League of Need and Marked Bounds State retain stronger route/boundary silhouettes.

## Parent Follow-up

- Added ideology-specific runtime copies for each generated cosmetic tag under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Covered ideology suffixes: `_democratic`, `_communism`, `_fascism`, and `_neutrality`.
- These copies intentionally derive from the generated base flag art for each cosmetic identity so the late-route flag identity is stable when Event 015 applies a cosmetic tag to arbitrary existing countries.

## Risks

- The two ledger-state flags intentionally share civic ledger/storehouse motifs, so their smallest previews depend more on palette distinction than emblem detail.
- No `.gfx` handoff is needed for these flags unless the main agent later introduces custom UI display sprites outside HOI4's normal flag lookup.
