# Event 018 Resources Found consolidated asset manifest

## Status

The Event 018 visual and audio package is complete and wired. Every live Event 018 asset reference has a runtime file and registration. Source art, processed intermediates, runtime exports, contact sheets, provenance, animation previews, and specialist handoffs remain under `docs/assets/018_resources_found/`.

No placeholder, generic replacement, cross-type resize, transform-only animation, reused final super-event image, generated music cue, or unresolved live mapping remains. Static animation images are the explicitly required accessibility fallbacks paired with real multi-frame artwork.

## Runtime inventory

| Family | Runtime delivery | Registration or consumer | Detailed manifest |
| --- | --- | --- | --- |
| Report events | 10 DDS files at 210 by 176 | `interface/018_resources_found.gfx` | `generated_event_art_manifest.md` |
| News events | 6 grayscale DDS files at 397 by 153 | `interface/018_resources_found.gfx` | `generated_event_art_manifest.md` |
| Super events | 3 DDS files at 457 by 328 | `interface/chaosx_super_events.gfx` and shared super-event selectors | `generated_event_art_manifest.md` |
| Oth-Kesh portraits | 4 large DDS, 3 small DDS, and one eight-frame animated DDS | `interface/chaosx_characters.gfx` and Event Details portrait mapping | `generated_event_art_manifest.md` |
| Oth-Kesh flags | 6 original identities in normal, medium, and small sizes, 18 TGA files total | Country tag, ideology variants, and `DHO_WORLD_BELOW` cosmetic identity | `generated_event_art_manifest.md` |
| Focus icons | 65 dedicated DDS files | `interface/018_resources_found.gfx` | `gfx_handoff.md` and `icon_generation_provenance_ledger.md` |
| Idea and state icons | 36 unique dedicated DDS files covering 37 live picture tokens | `interface/018_resources_found.gfx` | `gfx_handoff.md` and `icon_generation_provenance_ledger.md` |
| Decision families | 39 dedicated DDS files covering 125 visible decisions and missions | `interface/018_resources_found.gfx` | `gfx_handoff.md` and `icon_generation_provenance_ledger.md` |
| Decision categories | 5 icons and 5 category pictures | `interface/018_resources_found.gfx` | `gfx_handoff.md` and `icon_generation_provenance_ledger.md` |
| Achievements | 15 original identities with completed, grey, and not-eligible states, 45 DDS files total | `interface/chaosx_achievements.gfx` | `achievement_icons_imagegen/manifest.md` |
| Selected-field UI | 1 panel, 5 animated sheets, 5 static fallbacks, Suspended, and Closed, 13 DDS files total | `interface/018_resources_found.gfx` and `interface/018_resources_found.gui` | `animations/selected_field_ui/manifest.md` |
| Super-event audio | 3 final OGG cues and 3 WAV mirrors | `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset` | `audio_manifest.md` |

The Closed selected-field sprite is registered, inspected, and consumed by the live `resources_found_gui_closed_selection` history container. Exact closure removes the field from the active registry, stores its reversed ledger under `resources_found_last_closed_field`, and switches the panel to that presentation-only record. The parent field-management category accepts the history trigger and remains visible after the country's last active field closes. The History control never assigns the closed state to `resources_found_selected_field`, so the sprite is visible without reopening discovery or project eligibility.

## Animation proof

- Vhorruk uses eight separately generated source frames, a static fallback, a horizontal runtime sheet, and a GIF preview.
- The selected-field families use exact frame counts of 10, 10, 12, 12, and 12 for Unsafe, Seal, Disturbance, Breach, and Sealing.
- The selected-field package contains 56 separate animated source frames plus separate Suspended and Closed artwork, five runtime sheets, five static fallbacks, five GIF previews, and seven contact sheets.
- Frame construction, pixel identity, DDS format, dimensions, and static-fallback parity are recorded in `animations/selected_field_ui/validation.md` and `animations/selected_field_ui/hash_inventory.md`.

## Audio provenance and licensing

- Emergence uses Mussorgsky's *Bydło*, sourced from a Musopen public-domain recording with VRTS confirmation.
- World end uses Brahms's Symphony No. 1 in C minor, movement I, performed by the Czech National Symphony Orchestra and published as the Musopen Symphony Orchestra recording. The preserved recording is CC0 1.0 Universal and supplies worldwide redistribution and adaptation rights.
- Eligible global defeat uses Chopin's Prelude in E minor, Op. 28 No. 4, performed by Ivan Ilić under CC BY 3.0 with the required attribution and edit notice.

Source links, performers, retained intervals, licences, exact 115/110/109-second durations, hashes, processing, loudness, and required attribution are recorded in `audio_manifest.md`, the detailed audio research, and the combined `docs/super_events/018_resources_found_super_event_research.md`. Frozen source-page and licence snapshots are indexed under `source/audio/license_evidence/README.md`.

## Review evidence

The generated-event-art contact sheets cover report, news, super-event, portrait, animation, and flag outputs. Icon contact sheets cover focus, idea/state, decision, and category families. Achievement contact sheets cover source, processed, and decoded DDS outputs. Selected-field contact sheets cover every frame family and the live panel position. Root review inspected these sheets and rejected generations documented in the specialist manifests before runtime export.

Registration parity is documented by:

- `generated_event_art_gfx_handoff.md`
- `gfx_handoff.md`
- `achievement_icons_imagegen/manifest.md`
- `animations/selected_field_ui/manifest.md`
- `audio_manifest.md`

## Simplifications, omissions, fallbacks, and blockers

No asset simplification, omission, placeholder, or unresolved mapping remains. The five selected-field static textures and Vhorruk's static portrait are required accessibility fallbacks backed by complete real-frame animations. The jurisdiction-limited Debussy candidate is preserved only as rejected research history; the live ID 55 cue is the worldwide CC0 Brahms recording documented above.
