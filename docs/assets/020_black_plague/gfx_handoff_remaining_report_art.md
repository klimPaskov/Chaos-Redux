# Event 020 remaining report art GFX handoff

Parent-owned wiring target: `interface/020_black_plague_event_pictures.gfx`.

Add one `spriteType` for each final DDS below, preserving these stable names and event-scoped texture paths.

```text
spriteType = { name = "GFX_report_event_020_black_plague_severe" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_black_plague_severe.dds" }
spriteType = { name = "GFX_report_event_020_rat_king_crisis" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_rat_king_crisis.dds" }
spriteType = { name = "GFX_report_event_020_crown_strike" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_crown_strike.dds" }
spriteType = { name = "GFX_report_event_020_rat_king_aftermath" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_rat_king_aftermath.dds" }
spriteType = { name = "GFX_report_event_020_doctor_wu" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_doctor_wu.dds" }
```

## Consumer crosswalk

| Accepted consumer | Exact sprite name | Final texture |
| --- | --- | --- |
| `chaosx.nr20.6`, `.8`, `.56` | `GFX_report_event_020_black_plague_severe` | `gfx/event_pictures/020_black_plague/report_event_020_black_plague_severe.dds` |
| `chaosx.nr20.53`, `.57`, `.58`, `.59` | `GFX_report_event_020_rat_king_crisis` | `gfx/event_pictures/020_black_plague/report_event_020_rat_king_crisis.dds` |
| `chaosx.nr20.54`, `.55`, `.64`, `.65` | `GFX_report_event_020_crown_strike` | `gfx/event_pictures/020_black_plague/report_event_020_crown_strike.dds` |
| `chaosx.nr20.73`, `.74`, `.75` | `GFX_report_event_020_rat_king_aftermath` | `gfx/event_pictures/020_black_plague/report_event_020_rat_king_aftermath.dds` |
| Existing Event 163 Doctor Wu Black Plague bridge | `GFX_report_event_020_doctor_wu` | `gfx/event_pictures/020_black_plague/report_event_020_doctor_wu.dds` |

All five textures are native `210x176` report cards. Sources, processed previews, prompt text, manifest, and contact sheet remain under `docs/assets/020_black_plague/` as active evidence and are not runtime references.
