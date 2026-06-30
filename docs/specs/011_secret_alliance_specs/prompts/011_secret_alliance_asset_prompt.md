# Asset prompt for Event 011 Secret Alliance

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation` for this asset package. Use the provided event spec files as the source design. Do not edit gameplay, localisation, GUI, GFX, or spreadsheet files. Produce source PNGs, processed PNGs, final DDS files, contact sheets when useful, manifest entries, and `gfx_handoff.md` entries.

## Required reference folders

Inspect these before creating assets:

- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`

## Asset package folder

Use:

`docs/assets/011_secret_alliance/`

Suggested final game folders should follow existing Chaos Redux patterns. Do not invent a new folder when an existing event, decision, idea, news, report, super-event, or UI asset folder fits.

## Static icons

Create the decision category icon, decision icons, idea icons, pact emblem, Dossier Board badges, and achievement icons listed in `matrices/011_secret_alliance_asset_matrix.md`.

Icon rules:

- Decision icons are 32x32.
- Idea and national spirit icons are 64x64.
- Achievement icons are 64x64.
- Focus icons are not required by this package unless implementation adds focus hooks later.
- Do not derive decision icons from idea icons or idea icons from decision icons.
- Use transparent canvas where the target asset type requires it.
- No text, readable letters, fake UI, watermarks, or modern props.

## Event images

Create generated documentary-style images for:

- Founding meeting report, 210x176 final report card treatment.
- Courier captured report, 210x176 final report card treatment.
- Sabotage aftermath report, 210x176 final report card treatment.
- Public reveal news image, 397x153 black and white.
- Reveal super-event image, 457x328.

These are fictional and dynamic. Use generated period-authentic 1936 to 1945 documentary style. Do not use real leaders, readable country names, readable treaty text, or modern uniforms. Do not make maps the central subject unless the scene still reads as people and institutions conspiring.

## Dossier Board UI assets

Create the UI assets listed in the asset matrix:

- Board background.
- Unknown member card.
- Known member card.
- Founder marker.
- Patron marker.
- Wavering marker.
- Evidence meter frame and fill variants.
- Pressure meter frame and fill variants.
- Preparedness meter frame and fill variants.

These should be functional UI art, not a generated exact layout. The implementation agent owns final GUI layout and button wiring.

## Animated assets

Use `chaos-redux-frame-animation`. Every final animation must use real source frames, a horizontal frame sheet DDS, a static fallback DDS, a GIF preview for review only, contact sheet, manifest entry, and GFX handoff.

Create animation briefs and frame plans for:

| Asset | Target size | Frames | FPS | Loop | Use |
| --- | ---: | ---: | ---: | --- | --- |
| Radio pulse | 64x64 or matching GUI slot | 8 | 8 | yes | Investigation available |
| Red thread glow | Board overlay size chosen by GUI | 8 | 8 | yes | Pact pressure rising |
| Seal crack | 96x96 or matching GUI slot | 10 | 8 | yes | Reveal near |
| Border warning frame | Member card overlay | 8 | 8 | yes | Neighbor member operation available |

Use static fallbacks named as in the asset matrix. Do not make the final animation by shifting, scaling, recoloring, or glow-filtering one still image.

## Manifest requirements

For every asset, record:

- Asset name.
- Related event ID 011.
- Asset type.
- In-game use.
- Source mode.
- Prompt if generated.
- Source PNG path.
- Processed PNG path.
- Final DDS path.
- Target size.
- Sprite name.
- Suggested GFX file.
- Related decision, idea, event, UI element, achievement, or super-event.
- Status.
- Any uncertainty.

## Handoff requirements

Create `docs/assets/011_secret_alliance/gfx_handoff.md` with ready-to-copy sprite definitions or precise wiring notes for the main implementation agent. Do not edit `.gfx` files yourself unless the parent explicitly grants that scope.
