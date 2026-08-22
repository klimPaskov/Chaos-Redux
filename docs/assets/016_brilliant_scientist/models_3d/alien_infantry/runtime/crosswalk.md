# Alien infantry requirement-to-runtime crosswalk

| Requirement | Proposed runtime consumer | Evidence | Status |
|---|---|---|---|
| Reusable generic alien identity | `alien_infantry_entity` | `refs/original/meshy_input.png`; `refs/original/input_manifest.json` | Source approved; provider candidate rejected |
| Bald green head, large black eyes, harness, boots | `alien_infantry_mesh` | Seven candidate previews and contact sheet | Present in candidate, but not exportable while candidate is rejected |
| Readable retro-futurist laser rifle | `alien_infantry_mesh` | `validation/generation_rejection.json` | Blocked: component completely absent |
| Vanilla-calibrated scale | `alien_infantry_entity`, scale `0.8` | `blender/reports/alien_infantry_candidate_prepare.json` | Calibration passed; final model remains pending |
| Idle | entity state `idle` -> `alien_infantry_idle` | No accepted action | Blocked |
| Move | entity state `move` -> `alien_infantry_move` | No accepted action | Blocked |
| Laser attack | entity state `attack` -> `alien_infantry_laser_attack` | No accepted rifle/action | Blocked |
| Defend | entity state `defend` -> `alien_infantry_defend` | No accepted action | Blocked |
| Support attack | entity state `support_attack` -> `alien_infantry_support_attack` | No accepted rifle/action | Blocked |
| Retreat | entity state `retreat` -> `alien_infantry_retreat` | No accepted action | Blocked |
| Death | entity state `death` -> `alien_infantry_death` | No accepted action | Blocked |
| Laser, movement, idle, death sound | entity-state sound events | `evidence/audio/provenance/audio_sources.json` | Sources and PCM candidates complete; exact frames and definitions blocked |
| Selection/acknowledgement voice | country/original-tag `TAG_infantry_*` | `runtime/sound_handoff.md` | Intentionally blocked to protect ordinary infantry voices |
| Large division counter | `GFX_unit_alien_infantry_icon_medium` | `runtime/counter_handoff.md` | Icon-artist production pending |
| Small on-map counter | `GFX_unit_alien_infantry_icon_medium_white` | `runtime/counter_handoff.md` | Icon-artist production pending |
| PDX mesh and animation exports | model/animation definitions | No accepted source | Blocked; no files emitted |
| Runtime registration and live validation | subunit sprite `alien_infantry` -> `alien_infantry_entity` | Unit owner confirmed exact token | Parent/user owned; not performed |

No requested action has been substituted with a static asset or a weaker semantic action.
