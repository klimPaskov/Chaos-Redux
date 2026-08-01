# Candidate 684: The First Red Line asset manifest

This package owns the dedicated fictional Quarantine report-event image for candidate 684.

## Requirement-to-runtime coverage

| Requirement | Intended use | Source package | Runtime registration | Consumer | Status |
| --- | --- | --- | --- | --- | --- |
| `684.first_red_line.report_event` | Fever clinic, ash road, and Quarantine ward policy | generated source PNG to processed PNG | `gfx/event_pictures/fallout_first_red_line/report_event_fallout_first_red_line.dds`, sprite `GFX_report_event_fallout_first_red_line` | Events 684, 686, and 688 | wired static runtime |

## Asset entry

- Asset name: `report_event_fallout_first_red_line`
- Related event ids: `684` through `690`
- Related event slug: `first_red_line`
- Asset type: fictional generated report-event picture
- Intended in-game use: `210x176` Fallout report-event card for The First Red Line
- Source mode: OpenAI built-in image generation workflow
- Source note: generated from a dedicated prompt. No repository image, internet image, real person, real flag, or attested symbol was reused.
- Canonical reference inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`
- Source PNG: `docs/assets/684_first_red_line/source_png/report_event_fallout_first_red_line_source.png`
- Source PNG SHA-256: `9955be36f74748c65737093dc3a72552368e144b8d4bd2f09e8ee8061bbb7d94`
- Source dimensions: `1536x1024` RGB PNG
- Processed PNG: `docs/assets/684_first_red_line/processed_png/report_event_fallout_first_red_line.png`
- Processed PNG SHA-256: `d75916aee0acb6334b67ea165754016420bea60b54dea3cd9896852f2112c570`
- Processed dimensions: `210x176` RGBA PNG with report-card transparency
- Final DDS: `gfx/event_pictures/fallout_first_red_line/report_event_fallout_first_red_line.dds`
- Final DDS SHA-256: `5d8cb9749c02d255ff44e126c9d13bafc6a088f2e70702ac4520ed130bd513d4`
- DDS format: legacy one-level uncompressed BGRA, 32-bit, `210x176`, 128-byte header, exact length `147968` bytes
- Sprite name: `GFX_report_event_fallout_first_red_line`
- `.gfx` target: `interface/fallout_world_end.gfx`
- Related localisation key: `chaosx.fallout.684.t`
- Prompt record: `docs/assets/684_first_red_line/prompts/first_red_line_report_prompt.md`
- GFX handoff: `docs/assets/684_first_red_line/gfx_handoff.md`
- Asset status: `wired_static_runtime_unproven`

The report image is dedicated to the First Red Line chain. It is not shared with zombie content, Final Silence, or another Fallout chain.

## Validation evidence

The processed PNG is `210x176` RGBA. The DDS header declares `210x176`, uses uncompressed BGRA channels, and has exact length `128 + 210*176*4 = 147968` bytes. The sprite path and texture path match the event source. Hearts of Iron IV was not launched, so player-visible presentation remains unproven.
