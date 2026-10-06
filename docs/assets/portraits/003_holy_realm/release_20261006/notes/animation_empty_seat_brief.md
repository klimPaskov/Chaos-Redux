# Empty Seat animated portrait brief

The asset `portrait_THR_empty_seat_animated` presents the deliberately absent leader in Event003's event-log presentation when the Empty Seat stage is selected. The existing scripted localization selects `GFX_portrait_THR_empty_seat_animated` for that presentation, while `GFX_portrait_THR_empty_seat` remains the static leader portrait and fallback.

| Property | Specification |
| --- | --- |
| Subject | A genuinely unoccupied ceremonial throne; no person, face, statue, shadow figure, or reflection. |
| Source mode | Native ImageGen edits of the original Empty Seat scene seed. The connected image tool exposes no model selector; record only the actual native ImageGen route. |
| Consumer | Existing `frameAnimatedSpriteType` in `interface/chaosx_characters.gfx`; event-log scripted localization in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. |
| Static fallback | `GFX_portrait_THR_empty_seat`, texture `gfx/leaders/003_holy_realm/portrait_THR_empty_seat.dds`. |
| Animated sprite | `GFX_portrait_THR_empty_seat_animated`, texture `gfx/leaders/003_holy_realm/portrait_THR_empty_seat_animated.dds`. |
| Target frame and sheet | 156x210 opaque frames; 16 columns produce a 2496x210 horizontal sheet. |
| Playback | Existing 4 frames per second, looping, play-on-show behavior. Eight distinct authored scene states run forward and return in reverse (`000` through `007`, then `007` through `000`); duplicated endpoints make the ping-pong loop seamless. |
| Motion | Incense drift, lamp flame, a small draft in the curtain or scarf fringe, and slow window light. The throne remains still and visibly empty. |
| Anchor | Centered throne back and seat; keep armrests, cushion, folded saffron cloth, and window composition stable. |
| Background | `consumer_opaque`, matching the inspected full-canvas portrait and existing sheet. |
| Source frames | `source_png/animation/portrait_THR_empty_seat/portrait_THR_empty_seat_000_source.png` through `_007_source.png`. |
| Processed frames and sheet | `processed_png/animation/portrait_THR_empty_seat/`; final PNG is `portrait_THR_empty_seat_animated_sheet.png`. |
| Preview and contacts | `previews/portrait_THR_empty_seat_animated_preview.gif` and both native and 4x contacts under `contact_sheets/`. |

The parent-authorized eight-pose mirrored loop fits the existing 16-frame sheet and 156x210 display size; each unique scene state still needs its own ImageGen source output. Processing may crop, resize, and assemble the accepted frames, but may not create motion.
