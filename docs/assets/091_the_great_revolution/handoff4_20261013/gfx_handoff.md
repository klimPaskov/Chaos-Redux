# Event 091 SE01 source-placeholder handoff

- Logical role: SE01 Worldwide Opening, reserved presentation slot 121.
- Proposed unique runtime basename: `super_event_091_the_great_revolution_worldwide_opening_source_placeholder.dds`.
- Proposed runtime path: `gfx/event_pictures/091_the_great_revolution/super_event_091_the_great_revolution_worldwide_opening_source_placeholder.dds`.
- Proposed unique sprite: `GFX_super_event_091_the_great_revolution_worldwide_opening_source_placeholder`.
- Suggested registry: parent-owned `interface/chaosx_super_events.gfx`, consistent with the existing Event 091 scene handoff. No registry or consumer was edited here.
- Source: `source/lenin_goldstein_after_speech_1920.jpg`, SHA-256 `CCE1B67B766D82C12EE4D484A0D14B97579DB6D2E2C703311141514900B274DE`.
- Processed preview: `processed_png/super_event_091_the_great_revolution_worldwide_opening_source_placeholder.png`, SHA-256 `B740D315A581FD77494EE49C7022579C8F502DBF3FE463363D0A9EDCC0946436`.
- Final DDS candidate: SHA-256 `11BE8FAF77BEDD633C0447312B2893D3C4637057464223EF75C0D6A0EF49B0FC`; exact round-trip match to processed PNG.
- Current consumer evidence: `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:261` maps `super_event_visible` value 91 to the existing `GFX_super_event_016_kruger_state_formation`; that sprite is defined in `interface/016_brilliant_scientist_super_events.gfx:8-9`. The shared GUI resolves the image through `[GetSuperEventImage]` in `common/scripted_guis/chaosx_scripted_gui_super_events.txt:32`. The accepted Event 091 prompt reserves presentation slot 121, and no current `super_event_visible` image mapping for value 121 was found. Parent owns resolving the slot and final image binding.
- Parent visual sample review: PASS on 2026-10-13 for readable Lenin/crowd context and no introduced artifacts.
- Status: `needs_user_review`, unbound. The source is a real 1920 Red Army speech, not the fictional worldwide event, and slot 121 still has no image case; see the composition and rights limitations in [source_research.md](source_research.md).
