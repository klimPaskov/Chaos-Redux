# Event 006 First League Super-Event Image Manifest

Package scope: bounded sourced super-event image package for `independence_wave_first_league` only.

Reference inspection completed:
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md`
- `docs/events/006_independence_wave.md`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_angel_directorate.png`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_divine_sovereignty.png`
- Existing Chaos Redux `gfx/super_events/*.dds` size pattern verified as `457x328` for active super-event image assets.

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Resulting files validate locally at `457x328`.

## Asset

### `super_event_independence_wave_first_league`
- Asset type: super-event image
- Intended in-game use: Event 006 Independence Wave super-event `independence_wave_first_league`
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: internet source image
- Source title: `Bruce presiding over the League of Nations Council`
- Source page URL: `https://commons.wikimedia.org/wiki/File:Bruce_presiding_over_the_League_of_Nations_Council.png`
- Source file URL: `https://upload.wikimedia.org/wikipedia/commons/c/ce/Bruce_presiding_over_the_League_of_Nations_Council.png`
- Source author or archive: `Commonwealth of Australia`, scanned from the Bruce Collection, `National Archives of Australia`
- Source date: `1936`
- License or public-domain status: Wikimedia Commons marks the image public domain in Australia and public domain in the United States via URAA restoration rules
- Era-fit note: authentic interwar diplomatic council photograph from 1936; chamber, delegates, papers, and conference-table composition fit the First League brief without flag-forward framing
- Event 006 fit note: reads as a tense formal congress of states at one table, which matches the faction-formation and world-order signal role better than military or collapse imagery
- Source PNG: `docs/assets/006_independence_wave/super_events/first_league/source_png/bruce_presiding_over_league_of_nations_council_1936.png`
- Processed PNG: `docs/assets/006_independence_wave/super_events/first_league/processed_png/super_event_independence_wave_first_league.png`
- Final DDS: `gfx/super_events/super_event_independence_wave_first_league.dds`
- Target size: `457x328`
- Sprite name: `GFX_super_event_independence_wave_first_league`
- `.gfx` file: `interface/chaosx_super_events.gfx` suggested by naming pattern only; parent agent should place it in the existing super-event sprite file actually used by the mod
- Related super-event key: `independence_wave_first_league`
- Notes: processed from a tighter crop variant that emphasizes the curved treaty table and listening delegates while keeping the chamber context readable at super-event scale
- Asset status: `converted`
- Uncertainty: source scene is a real League of Nations Council session, not a literal small-state league congress; the match is tonal and compositional rather than event-specific. The uncropped source includes major-power diplomatic context, including the Commons note that Ribbentrop is present, but that identity is not foregrounded in the selected crop.

## Review files

- Crop candidate contact sheet: `docs/assets/006_independence_wave/super_events/first_league/contact_sheets/first_league_super_event_crop_candidates.png`
