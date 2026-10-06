# Buddha Mandate animated portrait brief

The asset `portrait_THR_buddha_mandate_animated` presents the fictional leader in Event003's event-log presentation when the Buddha Mandate stage is selected. The existing scripted localization selects `GFX_portrait_THR_buddha_mandate_animated` for that presentation, while `GFX_portrait_THR_buddha_mandate` remains the static leader portrait and fallback.

| Property | Specification |
| --- | --- |
| Subject | One unnamed fictional supernatural Bodhisattva incarnation; same invented identity as the accepted Godly Figure and Buddha Mandate portraits. |
| Source mode | Native ImageGen edits of the approved fictional Buddha Mandate seed. The connected image tool exposes no model selector; record only the actual native ImageGen route. |
| Consumer | Existing `frameAnimatedSpriteType` in `interface/chaosx_characters.gfx`; event-log scripted localization in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. |
| Static fallback | `GFX_portrait_THR_buddha_mandate`, texture `gfx/leaders/003_holy_realm/portrait_THR_buddha_mandate.dds`. |
| Animated sprite | `GFX_portrait_THR_buddha_mandate_animated`, texture `gfx/leaders/003_holy_realm/portrait_THR_buddha_mandate_animated.dds`. |
| Target frame and sheet | 156x210 opaque frames; 16 columns produce a 2496x210 horizontal sheet. |
| Playback | Existing 4 frames per second, looping, play-on-show behavior. Eight distinct authored states run forward and return in reverse (`000` through `007`, then `007` through `000`); duplicated endpoints make the approved ping-pong loop seamless. |
| Motion | A restrained breath, natural blink, cloth settling, and distant cloud movement. No speaking, transformation, or implied historical behavior. |
| Anchor | Centered head and chest; face, hand, ceremonial cloth, and camera stay fixed. |
| Background | `consumer_opaque`, matching the inspected full-canvas portrait and existing sheet. |
| Source frames | `source_png/animation/portrait_THR_buddha_mandate/portrait_THR_buddha_mandate_000_source.png` through `_007_source.png`. |
| Processed frames and sheet | `processed_png/animation/portrait_THR_buddha_mandate/`; final PNG is `portrait_THR_buddha_mandate_animated_sheet.png`. |
| Preview and contacts | `previews/portrait_THR_buddha_mandate_animated_preview.gif` and both native and 4x contacts under `contact_sheets/`. |

The parent-authorized eight-pose mirrored loop fits the existing 16-frame sheet and 156x210 display size; each unique pose still needs its own ImageGen source output. Processing may crop, resize, and assemble the accepted frames, but may not create motion.
