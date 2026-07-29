# Asset production prompt: Event 011 Secret Alliance

Status: fulfilled historical implementation prompt. The final 57-DDS package, animation frames, static fallback, and six achievement triplets are validated and wired. Do not rerun this prompt as open work.

Create the complete visual asset package for Chaos Redux Event 011 Secret Alliance. Treat the supplied spec pack and `matrices/011_secret_alliance_asset_register.md` as the source design. Follow `chaos-redux-event-assets` for every static asset and `chaos-redux-frame-animation` for the one animated warning family.

## Required ownership split

Route the work by asset type.

- Use the generated event-art role for fictional report images, the news image, the super-event image, and the mechanic panel art.
- Use the icon artist role for decision icons, decision category icons, idea icons, status icons, faction emblem, achievement icons, and the animated warning asset.
- Do not use the archival source researcher unless a real historical source becomes necessary. This event is procedural and should not be tied to one photographed alliance.

Do not edit gameplay, localisation, GUI, GFX, event, decision, idea, achievement, or spreadsheet files. Produce final files, manifests, contact sheets, and wiring handoffs for the main implementation agent.

## Required reference inspection

Before generation or processing, inspect the matching repository reference folders:

- report images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report`
- news images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/news`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event`
- decisions and category icons: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions`
- ideas: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements`

Record the references inspected in the manifest and GFX handoff.

## Working folder

Use:

```text
docs/assets/011_secret_alliance/
  manifest.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  animations/coalition_closure_warning/
  gfx_handoff.md
```

Final DDS files must be placed in the event-scoped gameplay folders from the asset register.

## Event pictures

Create seven generated period-documentary report images at source resolution, then process each through `tools/process_report_event_image.py` to 210x176 and convert to DDS:

1. `report_event_first_pattern`
2. `report_event_missing_courier`
3. `report_event_machine_sabotage`
4. `report_event_safehouse_raid`
5. `report_event_border_survey`
6. `report_event_political_attack`
7. `report_event_turned_channel`

Each scene must use 1936 to 1945 clothing, vehicles, architecture, photographic technology, and press composition. Avoid readable documents, modern technology, modern streets, cinematic color grading, fake dust damage, and generic maps as the central subject.

Create one generated period-news image at 397x153 and black and white:

- `news_event_public_coalition`

Show several visibly different delegations entering a public common front. Keep the shared emblem unlettered. Do not include fixed country flags or readable signage.

Create one generated super-event image at 457x328:

- `super_event_public_reveal`

Show several period delegations and military representatives converging around one formal commitment. The human coalition must be the central subject. A broken seal, folded target map, or shared emblem may appear as a secondary prop. Avoid a globe, a title card, a pile of dossiers, or arrows drawn over a map.

## UI and icon package

Create the decision category icons, panel art, meter frames and fills, suspect card states, status icons, decision icons, idea icons, faction emblem, and achievement icons exactly as listed in `matrices/011_secret_alliance_asset_register.md`.

Important rules:

- Every icon type needs its own source artwork.
- Do not resize a focus-style source into an idea or decision icon.
- Decision icons are 32x32 and require simple silhouettes.
- Idea icons are 64x64 and require compact spirit-style compositions.
- Achievement icons are 64x64 full-canvas art with completed, grey, and not-eligible variants.
- Transparent assets need real transparency, no white rim, no fake checkerboard, no opaque square, and no sticker outline.
- The faction emblem must remain procedural and must not copy a real political or extremist symbol.
- UI art must contain no generated text.

The counter-network panel should leave clear functional space for two meters, three suspect cards, recent-operation status, and buttons. Generated art must not decide exact interactive layout.

## Animated warning family

Create `coalition_closure_warning` as an eight-frame real-source animation.

- First approve the static fallback.
- Write `brief.md` and `frame_plan.md` before generation.
- Create eight separate source frames showing several cords, shadows, or metal arms closing around a broken seal and easing back slightly.
- Keep the same camera, subject, palette, scale, and anchor across all frames.
- Do not create motion through translation, scaling, rotation, recoloring, opacity, blur, or glow filters on one still.
- Recommended playback is 6 to 8 fps, continuous slow loop.
- Build a horizontal sheet and verify width equals frame width multiplied by eight.
- Provide source frames, processed frames, sheet PNG, sheet DDS, static PNG and DDS, preview GIF, contact sheet, manifest entry, and ready-to-copy GFX handoff.

Proposed sprites:

- `GFX_011_secret_alliance_coalition_closure_warning`
- `GFX_011_secret_alliance_coalition_closure_warning_animated`

The animation represents Evolution III with an active offensive countdown. It should be noticeable without flashing or obscuring text.

## Naming and final paths

Preserve every path and proposed sprite name in the asset register unless the implementation agent has already registered a different stable name. If a name must change, record the old and proposed name in `gfx_handoff.md` rather than changing it silently.

## Manifest requirements

For every asset, record:

- asset key
- asset type
- intended use
- source mode
- generation prompt
- source PNG
- processed PNG
- final DDS
- target size
- proposed sprite
- proposed GFX file
- related event, decision, idea, achievement, GUI state, or super-event
- status
- uncertainty or user-review need

For the animation, also record frame count, timing, loop behavior, anchor, sheet size, frame source note, static fallback, and wiring precedent.

## Acceptance gates

Do not mark the package complete unless:

- all requested source PNGs exist
- all processed previews exist at exact dimensions
- all final DDS files exist at exact dimensions
- transparent icons pass checker-background review
- report images have transparent card corners and house treatment
- the news image is black and white
- the super-event image is legible in a UI preview
- the animation has eight real source frames and a valid horizontal sheet
- achievement triplets use the final achievement IDs
- the manifest covers every asset
- `gfx_handoff.md` lets the main agent wire every sprite without guessing

Report blocked assets and the precise reason. Do not substitute placeholders or reuse unrelated assets.
