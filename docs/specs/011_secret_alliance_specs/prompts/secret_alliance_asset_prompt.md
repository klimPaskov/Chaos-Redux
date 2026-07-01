# Asset Prompt for Event 011 Secret Alliance

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation` where animation is requested.

Event ID: 011
Event slug: secret_alliance
Output package path suggestion: `docs/assets/011_secret_alliance/`

## Required static assets

Create complete source PNG, processed PNG, final DDS, manifest, contact sheet where useful, and `gfx_handoff.md` entries for:

- reveal super-event image, generated non-icon event art, 457x328
- suspicious meeting report image, generated or sourced period-documentary image, 210x176 with report-card treatment
- sabotage aftermath report image, generated or sourced period-documentary image, 210x176 with report-card treatment
- exposed protocol report image, generated fictional period-documentary image, 210x176 with report-card treatment
- decision category icon for Counter-Conspiracy Dossier, generated icon, inspect decision references
- decision icons for courier tracing, rail guard, exposure, backchannel, border watch, factory shielding, false leak, and strike first, all 32x32
- idea icons for Dossier Pressure, Counter-Conspiracy Network, Secret Protocol Discipline, Patron Liaison Offices, Publicly Exposed Signatory, and Pact War Coordination, all 64x64
- faction emblem or UI seal for Anti-[target country] Pact, generated emblem, no text
- Dossier Board background and UI decorative pieces, generated UI art with manual slicing expected
- achievement completed icons for all eight planned achievements, 64x64, with grey and not-eligible variants if the achievement system requires triplets

## Animated assets

Create real source frames, static fallback, horizontal sheet PNG, final sheet DDS, preview GIF for review only, and handoff for:

- evidence seal pulse, state-driven when exposure decision is available
- pact readiness warning frame, state-driven near war threshold
- exposed member card glow, state-driven when a country is confirmed
- war countdown ticker, state-driven during public pact crisis
- hidden protocol overlay, state-driven during public reveal or super-event support

Do not create final animation by shifting, scaling, recoloring, blurring, or pulsing one still image. Use real generated source frames for every meaningful state.

## Visual direction

The visual identity should feel like hidden diplomacy becoming a military mechanism. Use sealed folders, courier bags, shadowed delegations, neutral corridors, radio cables, guard posts, torn treaty ribbon, border lamps, and wax seals. Avoid readable text, modern props, real leader likenesses, and map-only compositions.

## Source mode rules

Use generated art for fictional symbolic images and icons. Use sourced images only if a real archival scene is intentionally chosen for a report image. Do not replace existing country flags or generate real leader portraits.

Inspect relevant reference folders before work:

- `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`

## Handoff requirements

For every asset, list final DDS path, sprite name, target size, source mode, prompt or source URL, status, and uncertainty. For animated assets, include frame count, frame size, sheet size, fps, loop behavior, static fallback sprite, animated sprite, and target `.gfx` or `.gui` surface.
