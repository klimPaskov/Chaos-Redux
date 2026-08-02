# Ashline Firebreak implementation proof

## Source ownership

- Events: `events/fallout_world_end_events.txt`, ids `chaosx.fallout.554` through `chaosx.fallout.564`
- Constants: `common/script_constants/fallout_consolidated_constants.txt`
- Triggers: `common/scripted_triggers/fallout_consolidated_triggers.txt`
- Effects: `common/scripted_effects/fallout_consolidated_effects.txt`
- Modifiers: `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`
- Candidate producer: `common/scripted_effects/fallout_consolidated_effects.txt`
- Event Log: `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`
- Localisation: `localisation/english/fallout_consolidated_l_english.yml`
- Asset: `gfx/event_pictures/fallout/report_event_fallout_ashline_firebreak.dds`, `interface/fallout_consolidated.gfx`, and the dedicated workspace under `docs/assets/air_cleanliness_fallout/fallout_ashline_firebreak/`

## Static checks

- Event ids `554` through `564` each occur once.
- The inserted event block is brace-balanced and owns eleven defined event blocks.
- Dedicated constants, triggers, effects, modifiers, scripted localisation, and localisation contain no unsupported comparison forms or em dash punctuation.
- Localisation begins with a UTF-8 BOM.
- The runtime DDS is one-level uncompressed BGRA with length `147968`, header `124`, width `210`, height `176`, and pitch `840`.
- The candidate producer selects an owned state through `fallout_event_554_state_is_current`, writes candidate `554`, transaction `710052`, and route `7152`, and does not set a scheduler activation flag.
- The Deaths path supplies an explicit request, reason, target country, log flag, and minimum remaining population for both result and callback failure.
- The natural-disaster aftermath source helper remains outside this chain. The chain does not add a second contamination receipt.

## Runtime boundary

No HOI4 runtime was launched. Popup order, delayed state delivery, Event Log secondary actor rendering, host authority, scheduler activation, save recovery, and multiplayer behavior are not claimed.

## Asset-processing note

The repository DDS converter used its available BGRA ffmpeg path because no DirectXTex executable was present in the configured workspace. The final DDS dimensions and header were inspected. This is a documented asset-processing simplification.
