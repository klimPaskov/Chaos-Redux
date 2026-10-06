# Shared ChaosX super-event asset manifest

Source mode: native ImageGen edits of existing fictional/staged art. Both consumers require opaque `457x328` full-canvas super-event scenes.

| Asset | Prompt | Native source | Processed preview | Final DDS | Sprite and target `.gfx` | Status |
|---|---|---|---|---|---|---|
| AZL text-free poster illustration | `prompts/super_event_azl_v1.md` | `source_generated/super_event_azl_candidate_v1_source.png` | `processed/super_event_azl_candidate_v1.png` | `gfx/super_events/002_zombie_outbreak/super_event_azl.dds` | `GFX_super_event_azl`, `interface/chaosx_super_events.gfx` | Parent-approved, converted, pixel-roundtrip verified |
| Final Silence terminal decay scene | `prompts/super_event_final_silence_terminal_v1.md` | `source_generated/super_event_the_final_silence_terminal_candidate_v1_source.png` | `processed/super_event_the_final_silence_terminal_candidate_v1.png` | `gfx/super_events/003_holy_realm/super_event_the_final_silence_terminal.dds` | `GFX_super_event_final_silence_terminal`, `interface/chaosx_super_events.gfx` | Parent-approved, converted, pixel-roundtrip verified and wired |

The original AZL and main Final Silence DDS bytes are preserved in `source_runtime/`. The original main-stage Final Silence DDS remains the active main-stage texture.
