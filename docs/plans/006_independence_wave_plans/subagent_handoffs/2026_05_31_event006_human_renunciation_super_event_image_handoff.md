# Event 006 Human Renunciation Super-Event Image Handoff

Scope: generated super-event image asset package only. No gameplay, localisation, `.gfx`, GUI, event, focus, decision, or script files were edited.

## Files created

- `docs/assets/006_independence_wave/super_events/human_renunciation/prompts/super_event_independence_wave_human_renunciation.txt`
- `docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation.png`
- `docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_a.png`
- `docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_b.png`
- `docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_c.png`
- `docs/assets/006_independence_wave/super_events/human_renunciation/processed_png/super_event_independence_wave_human_renunciation.png`
- `docs/assets/006_independence_wave/super_events/human_renunciation/contact_sheets/human_renunciation_super_event_source_contact_sheet.png`
- `docs/assets/006_independence_wave/super_events/human_renunciation/manifest.md`
- `docs/assets/006_independence_wave/super_events/human_renunciation/gfx_handoff.md`
- `gfx/super_events/super_event_independence_wave_human_renunciation.dds`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_human_renunciation_super_event_image_handoff.md`

## Reference inspection completed

- Existing Event006 package:
  - `docs/assets/006_independence_wave/super_events/first_league/manifest.md`
  - `docs/assets/006_independence_wave/super_events/first_league/gfx_handoff.md`
  - `docs/assets/006_independence_wave/super_events/first_league/processed_png/super_event_independence_wave_first_league.png`
  - `docs/assets/006_independence_wave/super_events/first_league/contact_sheets/first_league_super_event_crop_candidates.png`
- Super-event reference folder:
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_angel_directorate.png`
  - `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_divine_sovereignty.png`

## Asset decision

- Chosen direction: empty parliamentary registry chamber with erased citizenship ledgers, stacked sealed records, and a central state seal over blank papers.
- Source mode: generated with `$imagegen`.
- Why generated is appropriate: this is a symbolic alternate-history event image about official erasure and bureaucratic absence, not a real attested historical scene.
- Final chosen source: `source_a`, copied to the canonical source PNG path.
- Alternate sources preserved: `source_b` and `source_c`.

## Validation

- `identify` on canonical source PNG: `1479x1063`
- `identify` on processed PNG: `457x328`
- `identify` on final DDS: `457x328`
- `file` on final DDS: `Microsoft DirectDraw Surface (DDS): 457 x 328, 24-bit color, RGB888`

## Commands run

```bash
mkdir -p docs/assets/006_independence_wave/super_events/human_renunciation/{source_png,processed_png,contact_sheets,prompts}
identify docs/assets/006_independence_wave/super_events/human_renunciation/source_png/*.png
convert docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_a.png -colorspace Gray -sigmoidal-contrast 3,50% -unsharp 0x0.6+0.5+0 -resize 457x328^ -gravity center -extent 457x328 docs/assets/006_independence_wave/super_events/human_renunciation/processed_png/super_event_independence_wave_human_renunciation.png
convert docs/assets/006_independence_wave/super_events/human_renunciation/processed_png/super_event_independence_wave_human_renunciation.png -define dds:compression=none gfx/super_events/super_event_independence_wave_human_renunciation.dds
montage docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_a.png docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_b.png docs/assets/006_independence_wave/super_events/human_renunciation/source_png/super_event_independence_wave_human_renunciation_source_c.png -thumbnail 320x230 -tile 3x1 -geometry +12+12 docs/assets/006_independence_wave/super_events/human_renunciation/contact_sheets/human_renunciation_super_event_source_contact_sheet.png
identify docs/assets/006_independence_wave/super_events/human_renunciation/processed_png/super_event_independence_wave_human_renunciation.png gfx/super_events/super_event_independence_wave_human_renunciation.dds
file gfx/super_events/super_event_independence_wave_human_renunciation.dds
```

## Notes for parent wiring

- Final DDS path is fixed by task constraint: `gfx/super_events/super_event_independence_wave_human_renunciation.dds`.
- Proposed sprite name: `GFX_super_event_independence_wave_human_renunciation`.
- Suggested `.gfx` target remains the repo's existing super-event sprite file.
- No `.gfx` edit was made here.
