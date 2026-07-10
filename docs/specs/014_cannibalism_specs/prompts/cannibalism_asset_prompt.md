# Event 014 Cannibalism Asset Production Prompt

Use this prompt after extracting the full package to `docs/specs/014_cannibalism_specs/`.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- the full Event 014 spec pack
- `matrices/asset_inventory_matrix.md`
- `specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md`

All custom subagents must be spawned with `fork_context=false`. Pass this prompt, the event ID, event slug, exact output paths, and every relevant spec path directly.

## Routing

Do not use one broad worker for the mixed package.

- Use `chaosx_generated_event_art` for report images, news images, super-event images, fictional flags, generic warlord portraits, Hannibal portraits, Wendigo Hannibal portraits, GUI background art, faction emblems, and non-icon fictional presentation art.
- Use `chaosx_icon_artist` for focus icons, idea icons, national spirit icons, decision icons, category icons, achievement icons, unit or technology icons, route seals, warning frames, and small animated sprites.
- Use `chaosx_asset_source_researcher` only if a final asset genuinely needs real archival material. The default core event art is generated. Do not use real atrocity photographs as final fictional event art.

## Hard visual requirements

- Gore is mandatory.
- Important assets must be unsettling.
- Warlord portraits depict bloody, bald men in invented rough hides, raw cloth, bone ornaments, and scavenged 1930s to 1940s military gear.
- Do not copy real Indigenous, African, Pacific, or religious ceremonial clothing.
- Do not expose Hannibal's face, silhouette, symbol, or transformed identity before the reveal state.
- Do not use historical Carthaginian imagery for Hannibal.
- The Wendigo Hannibal package must reuse existing Chaos Redux Wendigo visual language and add no borrowed living cultural regalia.
- Generated period scenes must use period clothing, weapons, buildings, vehicles, and photographic technology.
- No readable generated text, watermarks, modern UI, modern objects, film stills, or reenactment visuals.

## Required generated event art

### Report images, 210 by 176 after processing

Produce at least these ten final report images:

1. Initial field discovery.
2. Missing burial party evidence.
3. Ration store and military kitchen investigation.
4. Compromised field hospital.
5. Prison or detention-site evidence.
6. Silent island landing.
7. Empty village under commune control.
8. Captured warlord camp.
9. Liberated feeding state and identification teams.
10. Broken Wendigo transformation anchor.

Use `tools/process_report_event_image.py` for final card treatment. Preserve source PNG, processed PNG, and final DDS.

### News images, 397 by 153, black and white

Produce six distinct images:

1. Public exposure of military cannibalism.
2. Confirmed island or commune.
3. First warlord country.
4. Coordinated multi-warlord offensives.
5. Hannibal reveal news fallback.
6. Global defeat.

### Super-event images, 457 by 328

Produce four distinct final scenes:

1. Hannibal reveal among warlords.
2. Ordinary Hannibal world-end.
3. Wendigo Hannibal world-end.
4. Global defeat aftermath.

These must be separate compositions, not recolors or crop variants.

## Portrait package

### Generic warlords

Produce 8 to 12 male-presenting portraits at 156 by 210:

- two Island Host leaders
- two Siege Commune leaders
- two March Host leaders
- two Prison Host leaders
- optional regional alternatives

Record apparent gender presentation and require matching male regional name pools. Each portrait must remain distinct and must not resemble Hannibal.

### Hannibal

Produce:

- static ordinary portrait
- 12 separate ordinary source frames
- 12 processed 156 by 210 frames
- 1872 by 210 sheet PNG and DDS
- static fallback DDS
- GIF preview
- contact sheet

### Wendigo Hannibal

Produce:

- static transformed portrait
- 16 separate transformed source frames
- 16 processed 156 by 210 frames
- 2496 by 210 sheet PNG and DDS
- static fallback DDS
- GIF preview
- contact sheet

Do not create motion through translation, scaling, rotation, blur, recolor, opacity, glow filters, or other one-still transforms. Every meaningful frame state needs real source art.

## Flags

Produce normal, medium, and small TGA files for:

- eight warlord slot identities
- approved route or cosmetic variants
- unified Hannibal base
- central, confederated, and ritual-state variants
- Wendigo Hannibal transformation

Keep existing Wendigo base flags unchanged unless the transformation uses an explicit cosmetic tag. Validate dimensions and TGA orientation.

## Icon package

Produce focus-specific art for the final implemented trees:

- 60 to 72 local warlord focuses
- 96 to 120 unified Hannibal focuses
- 24 to 32 Wendigo overlay focuses

Produce separate source art for at least 20 idea and national spirit icons, at least 24 decision icons, all required category and scripted GUI icons, all 18 achievement icon triplets, and any unit or technology icons required by the final implementation.

Focus, idea, decision, and achievement icons are different asset types. Do not satisfy one type by resizing another.

## Animated UI package

Create true frame packages for:

- early warning seal, 8 frames at 64 by 64
- Cult Cohesion emblem, 8 frames at 64 by 64
- network threads, 12 frames at final UI size
- island alert, 8 frames at 64 by 64
- selected target overlay, 6 frames
- critical Larder glow, 8 frames at 64 by 64
- Frenzy border, 8 frames
- warlord route emblem, 8 frames at 94 by 86
- unification seal, 12 frames at 94 by 86
- ordinary terminal frame, 12 frames
- Wendigo anchor pulse, 12 frames at 64 by 64
- Wendigo terminal frame, 12 frames

Every animated asset needs a static fallback, source frames, processed frames, sheet PNG, sheet DDS, preview GIF, contact sheet, manifest entry, and `gfx_handoff.md` entry.

## Final placement

Use event-scoped folders:

- `gfx/event_pictures/014_cannibalism/`
- `gfx/super_events/014_cannibalism/`
- `gfx/interface/ideas/014_cannibalism/`
- `gfx/interface/goals/014_cannibalism/`
- `gfx/interface/decisions/014_cannibalism/`
- `gfx/leaders/014_cannibalism/`
- `gfx/interface/014_cannibalism/`

Flags and achievements follow engine root conventions.

## Documentation

Create or update:

- `docs/assets/014_cannibalism/manifest.md`
- `docs/assets/014_cannibalism/gfx_handoff.md`
- animation briefs and frame plans
- contact sheets
- prompt records

Every requested asset must be complete, blocked, or marked `needs_user_review`. Do not substitute a placeholder or weak fallback.
