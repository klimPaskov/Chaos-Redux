# Event 010 Zol world-end portrait DDS repair

This record covers a lossless DDS container repair for the inherited static and animated Zol world-end portraits. The existing artwork was not regenerated, repainted, cropped, resized, recolored, or otherwise edited.

## Provenance and source mode

Source evidence is the byte-for-byte copy of each inherited runtime DDS under `source/`; each archived hash matched the runtime file before conversion. Provenance status: `inherited DDS; original master provenance unresolved`. No original master, attributed Internet source, rights record, ImageGen prompt, or ImageGen output was available, and no such evidence is claimed. The portrait source-mode gate and any prior replacement state were not reclassified by this container repair.

## Asset records

| Asset and use | Runtime sprite and consumer | Archived original SHA-256 | Original format and dimensions | Repaired runtime SHA-256 | Output format and dimensions | Equality evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Static leader portrait for Event 010 Zol world-end | `GFX_portrait_DTH_zol_world_end`; `common/scripted_effects/010_death_effects.txt` calls `set_country_leader_portrait` | `E308A6A8C802BF75FAA52EB04AD42285ADEEDE259027AC671894E60CAC4F2060` | 156×210, uncompressed RGB24, alpha absent and decoded as opaque | `4E53B401005BDA473EB2EB40CB4D7570DAE11A6449533229DEBD9F07069FE184` | 156×210, uncompressed BGRA32, one base level | 32,760 of 32,760 pixels equal; effective alpha equal for every pixel; output alpha is 255 throughout |
| Animated leader portrait for the same world-end state | `GFX_portrait_DTH_zol_world_end_animated`; `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` selects this sprite | `8495895AA0B437FD2601623C35CFA95639DAF35A6FB938E1B21C8AF94C756973` | 1248×210, DXT1, alpha decoded as opaque | `274A6863BB36E3D4B93A9C300E661BB7E9588E5D3B22AED9AFBB46593490EA1F` | 1248×210, uncompressed BGRA32, one base level | 262,080 of 262,080 pixels equal; alpha equal for every pixel; each of the 8 frames equals its corresponding decoded source frame pixel-for-pixel, and output alpha is 255 throughout |

The animated sheet remains eight horizontal 156×210 frames. The existing definition in `interface/chaosx_characters.gfx` retains `noOfFrames = 8`, `animation_rate_fps = 4`, `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0`, and `alwaystransparent = yes`. Its static fallback remains `GFX_portrait_DTH_zol_world_end`.

## Conversion and review

The conversion used Pillow 11.1.0 to decode each archived DDS and `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py::write_bgra_dds` to write the uncompressed BGRA32 container. The decoder output was compared against the repaired DDS output at every pixel and alpha value before replacing the runtime file. No resizing, frame extraction, or PNG intermediate was used.

The exact vanilla leader portrait reference inspected was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds` (156×210), registered as `GFX_portrait_ETH_haile_selassie` in `interface/_leader_portraits.gfx`. It was used only to confirm the installed leader-portrait canvas and role. The vanilla animated-strip precedent inspected was `GFX_active_operative_mission_anim` in `interface/operativeleader.gfx`; its installed texture is a horizontal frame strip. Neither reference was used as an identity or art source.

The source and repaired portraits were visually inspected at native size; the animated review contact sheets were 624×420, below the 1200-pixel preview limit. Exact decoded-pixel equality confirms the visuals and frame content were preserved. No art-quality, likeness, rights, or ImageGen review is claimed because no original master/source package exists.

## Durable lossless PNG previews

| Preview | Dimensions | SHA-256 | Verification |
| --- | --- | --- | --- |
| `processed/portrait_DTH_zol_world_end.png` | 156×210 | `227699B17C00689A9BA2E21FB345E5264FF0C7DD98684538D8D4609CC109D167` | RGBA pixels equal the repaired static DDS exactly |
| `processed/portrait_DTH_zol_world_end_animated.png` | 1248×210 | `59304D04D23A2D8A890D6974A10CFF284A2FE6A83A5ABFC8DB930E8D99931500` | Full eight-frame horizontal strip; RGBA pixels equal the repaired animated DDS exactly |
| `processed/portrait_DTH_zol_world_end_contact_sheet.png` | 468×702 | `17FC8FE391749744303F6B008C493B8D089024F83CB2D8788BAE95808AB56589` | Labeled static portrait and frames 01–08; every native-size panel equals its corresponding repaired DDS pixels; longest side is 702 px |

The animated PNG retains the original 1248×210 canvas and eight-frame horizontal layout. The contact sheet rearranges only review panels into three columns of native 156×210 images and adds labels above them; it does not alter or replace either runtime portrait.

## Wiring, replacement, and scope

Runtime basenames, stable paths, sprite names, character references, frame count, animation timing, and animation behavior were not changed. `gfx/leaders/010_death/portrait_DTH_zol.dds` was not changed; its SHA-256 remains `A1A55F8FDA949DC8F0487796FD3FD37D20FFC4B521B8D49916E6B1681F2DA4A3`.

No replacement art was supplied or created. The inherited portrait art remains the same; the source-mode/replacement state remains whatever the existing package recorded, with original-master provenance unresolved. HOI4 was not launched, so this records container and decoded-pixel evidence rather than live-engine acceptance.

## Archived originals

- `source/portrait_DTH_zol_world_end.dds` — archived unchanged; SHA-256 `E308A6A8C802BF75FAA52EB04AD42285ADEEDE259027AC671894E60CAC4F2060`.
- `source/portrait_DTH_zol_world_end_animated.dds` — archived unchanged; SHA-256 `8495895AA0B437FD2601623C35CFA95639DAF35A6FB938E1B21C8AF94C756973`.
