# Event 006 League War Super-Event Image Handoff

Scope: generated super-event image asset package only. No gameplay, localisation, `.gfx`, GUI, event, focus, decision, or script files were edited.

## Files created

- `docs/assets/006_independence_wave/super_events/league_war/prompts/super_event_independence_wave_league_war.txt`
- `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war.png`
- `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_a.png`
- `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_b.png`
- `docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_c.png`
- `docs/assets/006_independence_wave/super_events/league_war/processed_png/super_event_independence_wave_league_war.png`
- `docs/assets/006_independence_wave/super_events/league_war/contact_sheets/league_war_super_event_source_contact_sheet.png`
- `docs/assets/006_independence_wave/super_events/league_war/manifest.md`
- `docs/assets/006_independence_wave/super_events/league_war/gfx_handoff.md`
- `gfx/super_events/super_event_independence_wave_league_war.dds`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_league_war_super_event_image_handoff.md`

## Reference inspection completed

- Existing Event 006 package:
  - `docs/assets/006_independence_wave/super_events/first_league/manifest.md`
  - `docs/assets/006_independence_wave/super_events/first_league/gfx_handoff.md`
  - `docs/assets/006_independence_wave/super_events/human_renunciation/manifest.md`
- Super-event reference folder:
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_angel_directorate.png`
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_divine_sovereignty.png`

## Asset decision

- Chosen direction: small-state defensive mobilization staged inside a rail-hall war office, with volunteer queues beside a long planning table and a steam locomotive visible through the station windows.
- Source mode: generated with `$imagegen`.
- Why generated is appropriate: the League War scene is fictional, alternate-history, and composition-specific; generated documentary-style art fits the brief better than any real archive photograph.
- Final chosen source: `source_a`, copied to the canonical source PNG path.
- Alternate sources preserved: `source_b` and `source_c`.

## Validation

- `identify` on canonical source PNG: `1479x1064`
- `identify` on processed PNG: `457x328`
- `identify` on final DDS: `457x328`
- `file` on final DDS: `Microsoft DirectDraw Surface (DDS): 457 x 328, 24-bit color, RGB888`

## Commands run

```bash
mkdir -p docs/assets/006_independence_wave/super_events/league_war/{source_png,processed_png,contact_sheets,prompts}
cp /home/klim/.codex/generated_images/019e7f5c-9361-7de0-8b34-21828f276031/ig_070be2a6fc036800016a1c826316cc81919956da1caf01061a.png docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_a.png
cp /home/klim/.codex/generated_images/019e7f5c-9361-7de0-8b34-21828f276031/ig_070be2a6fc036800016a1c833634c08191b474d5df364b4a78.png docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_b.png
cp /home/klim/.codex/generated_images/019e7f5c-9361-7de0-8b34-21828f276031/ig_070be2a6fc036800016a1c829cf1308191bb64a69d00c3dd12.png docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_c.png
cp docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_a.png docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war.png
convert docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_a.png -colorspace Gray -sigmoidal-contrast 3,50% -unsharp 0x0.6+0.5+0 -resize 457x328^ -gravity center -extent 457x328 docs/assets/006_independence_wave/super_events/league_war/processed_png/super_event_independence_wave_league_war.png
convert docs/assets/006_independence_wave/super_events/league_war/processed_png/super_event_independence_wave_league_war.png -define dds:compression=none gfx/super_events/super_event_independence_wave_league_war.dds
montage docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_a.png docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_b.png docs/assets/006_independence_wave/super_events/league_war/source_png/super_event_independence_wave_league_war_source_c.png -thumbnail 320x230 -tile 3x1 -geometry +12+12 docs/assets/006_independence_wave/super_events/league_war/contact_sheets/league_war_super_event_source_contact_sheet.png
identify docs/assets/006_independence_wave/super_events/league_war/processed_png/super_event_independence_wave_league_war.png gfx/super_events/super_event_independence_wave_league_war.dds
file gfx/super_events/super_event_independence_wave_league_war.dds
```

## Notes for parent wiring

- Final DDS path is fixed by task constraint: `gfx/super_events/super_event_independence_wave_league_war.dds`.
- Proposed sprite name: `GFX_super_event_independence_wave_league_war`.
- Suggested `.gfx` target remains the repo's existing super-event sprite file.
- No `.gfx` edit was made here.
