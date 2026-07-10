# Animation production prompt for Event 016 Brilliant Scientist

Use this prompt with `chaosx_generated_event_art` for portraits and `chaosx_icon_artist` for small UI animation. Spawn with `fork_context=false` and require the `chaos-redux-frame-animation` skill.

## Source design

Read:

- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_9_assets_animation_and_localisation.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`

## Required portrait packages

Create separate animation packages for the implemented Stage IV identities:

- Clone Kruger.
- Machine-linked Kruger.
- Temporal Continuum Kruger.
- Xenobiological or alien Kruger.
- Synthesis Kruger.

Do not create a route package that implementation has not accepted. Each package must preserve Doctor Warren Kruger's identity, camera, framing, period style, palette, and bottom-center anchor.

Leader portrait frame size is 156x210. Use at least 8 real source frames for subtle motion unless the brief justifies a different count. Temporal and synthesis variants may need 10 to 16 frames. Suggested playback is 3 to 6 FPS depending on motion.

Every visual state must be intentionally drawn or generated as its own source frame. Do not create final motion through translation, scaling, rotation, blur, recolor, brightness, glow, opacity, warping, or scripted particles over one still.

## Portrait motion direction

Clone Kruger:

- Distinct bodies or reflected versions move independently while remaining recognizably the same person.
- Avoid simple duplicate-opacity effects.

Machine-linked Kruger:

- Real mechanical or interface movement, changes in eye focus, and designed interaction with the machine environment.
- Avoid a static portrait with blinking lights pasted over it.

Temporal Continuum Kruger:

- Intentionally generated changes in age, posture, position, or simultaneous versions.
- The loop should return cleanly without a transform-only shimmer.

Xenobiological or alien Kruger:

- Controlled anatomical or living-equipment movement drawn per frame.
- Keep the face readable.

Synthesis Kruger:

- Combine accepted route features without visual clutter.
- Motion must communicate integration rather than random mutation.

## UI animation packages

Create only the state-driven animations approved by implementation:

- Government-control critical warning frame.
- Active project marker.
- Sovereignty crisis border.
- Singularity armed indicator.

Keep ordinary lists, text panels, costs, and static project stages unanimated.

## Required deliverables per package

- `brief.md` with in-game use, target surface, frame size, frame count, calculated sheet size, FPS, loop, `play_on_show`, anchor, source mode, target GFX, target GUI or character surface, and static fallback.
- `frame_plan.md` with one row per frame.
- One source PNG per frame.
- One processed PNG per frame at exact size.
- Horizontal sheet PNG.
- Final horizontal sheet DDS.
- Static fallback PNG and DDS.
- GIF preview for review only.
- Contact sheet.
- Manifest entry.
- `gfx_handoff.md` with proposed `GFX_` static and animated sprite names, frame count, timing, trigger, and target files.

Before wiring handoff, inspect the required offline wiki pages, vanilla files, and existing Chaos Redux examples for the target surface. Record the precedent. If the exact surface has no verified animated support, mark wiring `blocked` or `needs_user_review` while still preserving the static fallback.

Do not edit gameplay, GFX, GUI, characters, localisation, or spreadsheets.
