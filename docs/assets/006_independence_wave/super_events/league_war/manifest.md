# Event 006 League War Super-Event Image Manifest

Package scope: bounded generated super-event image package for `independence_wave_league_war` only.

Reference inspection completed:
- `docs/assets/006_independence_wave/super_events/first_league/manifest.md`
- `docs/assets/006_independence_wave/super_events/first_league/gfx_handoff.md`
- `docs/assets/006_independence_wave/super_events/human_renunciation/manifest.md`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_angel_directorate.png`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_divine_sovereignty.png`
- Existing Chaos Redux `gfx/super_events/*.dds` size pattern verified as `457x328` for active super-event image assets.

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Resulting files validate locally at `457x328`.
- `file` reports the final DDS as `Microsoft DirectDraw Surface (DDS): 457 x 328, 24-bit color, RGB888`.

## Asset

### `super_event_independence_wave_league_war`
- Asset type: super-event image
- Intended in-game use: Event 006 Independence Wave super-event `independence_wave_league_war`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: generated with `$imagegen`
- Generation rationale: the brief calls for a fictional small-state mobilization scene for an alternate-history league war, so staged documentary-style generated art fits better than trying to force a real archive image into a non-attested event
- Prompt file: `docs/assets/006_independence_wave/super_events/league_war/prompts/super_event_independence_wave_league_war.txt`
- Primary source PNG: `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war.png`
- Alternate source PNGs:
  - `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_a.png`
  - `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_b.png`
  - `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_c.png`
- Processed PNG: `docs/assets/006_independence_wave/super_events/league_war/processed_png/super_event_independence_wave_league_war.png`
- Final DDS: `gfx/super_events/super_event_independence_wave_league_war.dds`
- Target size: `457x328`
- Proposed sprite name: `GFX_super_event_independence_wave_league_war`
- Suggested `.gfx` file: existing Chaos Redux super-event sprite definition file
- Related super-event key: `independence_wave_league_war`
- Visual fit note: the chosen composition combines volunteer queues, a rail-hall mustering point, a war-planning table, and abstract banners, which reads as defensive coalition mobilization without relying on any specific national insignia
- Processing note: selected source A for the clearest wide composition and strongest balance between mobilized civilians, staff officers, maps, and locomotive context; converted to grayscale, lightly contrast-shaped, sharpened, center-cropped, and resized to the established super-event target
- Asset status: `converted`
- Uncertainty: the scene is intentionally fictional and documentary-staged rather than archival, so it should be treated as final generated source art for this super-event rather than as a real photographed historical moment

## Review files

- Source contact sheet: `docs/assets/006_independence_wave/super_events/league_war/contact_sheets/league_war_super_event_source_contact_sheet.png`
