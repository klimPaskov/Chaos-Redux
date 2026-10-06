# Holy Mandala Animation GFX Handoff

Status: `implemented` after parent acceptance on 2026-10-06. The fourteen candidate DDS files in `candidate_dds/` were copied byte-for-byte to the runtime paths in the table. This worker did not modify `.gfx`, `.gui`, scripted localisation, or gameplay files.

## Existing consumer contract

`interface/003_holy_realm.gfx` already registers the seven static sprite names and seven `frameAnimatedSpriteType` names listed below. Each animation uses `noOfFrames = 16`, `animation_rate_fps = 8`, `looping = yes`, `play_on_show = yes`, and a 420x420 frame drawn from a 6720x420 horizontal sheet. These identifiers and settings remain unchanged.

`holy_realm_mandala_core` in the current `interface/chaosx_decisions.gui` source uses `GFX_holy_realm_mandala_dormant` as its static base sprite, at `{ x = 126 y = 12 }` with `scale = 0.52`. The parent reports that `GetHolyRealmMandalaSprite` selects the seven animated state sprites after scripted localisation evaluation. The displayed frame is 218.4 pixels wide at UI scale 1.0. The GUI worker's post-change MCP render timed out without artifacts, so that dynamic visual selection remains a separate parent evidence gate.

The source definition `common/scripted_localisation/003_holy_realm_scripted_localisation.txt:387-443` returns the seven animated sprite identifiers in this table, with `GFX_holy_realm_mandala_dormant_animated` as its final fallback. No scripted localisation change was made.

## Sprite and runtime path mapping

| State | Static sprite and runtime texture | Animated sprite and runtime texture | Candidate DDS |
| --- | --- | --- | --- |
| dormant | `GFX_holy_realm_mandala_dormant` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_dormant.dds` | `GFX_holy_realm_mandala_dormant_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds` | `candidate_dds/holy_realm_mandala_dormant.dds`, `candidate_dds/holy_realm_mandala_dormant_animated.dds` |
| teaching | `GFX_holy_realm_mandala_teaching` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_teaching.dds` | `GFX_holy_realm_mandala_teaching_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_teaching_animated.dds` | `candidate_dds/holy_realm_mandala_teaching.dds`, `candidate_dds/holy_realm_mandala_teaching_animated.dds` |
| meditation | `GFX_holy_realm_mandala_meditation` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_meditation.dds` | `GFX_holy_realm_mandala_meditation_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_meditation_animated.dds` | `candidate_dds/holy_realm_mandala_meditation.dds`, `candidate_dds/holy_realm_mandala_meditation_animated.dds` |
| awakened | `GFX_holy_realm_mandala_awakened` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_awakened.dds` | `GFX_holy_realm_mandala_awakened_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_awakened_animated.dds` | `candidate_dds/holy_realm_mandala_awakened.dds`, `candidate_dds/holy_realm_mandala_awakened_animated.dds` |
| wrathful | `GFX_holy_realm_mandala_wrathful` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_wrathful.dds` | `GFX_holy_realm_mandala_wrathful_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_wrathful_animated.dds` | `candidate_dds/holy_realm_mandala_wrathful.dds`, `candidate_dds/holy_realm_mandala_wrathful_animated.dds` |
| final_silence | `GFX_holy_realm_mandala_final_silence` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_final_silence.dds` | `GFX_holy_realm_mandala_final_silence_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_final_silence_animated.dds` | `candidate_dds/holy_realm_mandala_final_silence.dds`, `candidate_dds/holy_realm_mandala_final_silence_animated.dds` |
| empty | `GFX_holy_realm_mandala_empty` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_empty.dds` | `GFX_holy_realm_mandala_empty_animated` → `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_empty_animated.dds` | `candidate_dds/holy_realm_mandala_empty.dds`, `candidate_dds/holy_realm_mandala_empty_animated.dds` |

## Ready-to-copy existing sprite pattern

The existing declarations already match the candidate texture layout. Repeat this exact structure for each listed state only if the parent needs to restore a declaration; no wiring change is requested by this handoff.

```txt
spriteType = {
	name = "GFX_holy_realm_mandala_dormant"
	texturefile = "gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_dormant.dds"
}
frameAnimatedSpriteType = {
	name = "GFX_holy_realm_mandala_dormant_animated"
	texturefile = "gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds"
	noOfFrames = 16
	animation_rate_fps = 8
	looping = yes
	play_on_show = yes
	pause_on_loop = 0.0
	alwaystransparent = yes
}
```

## Review artifacts

The parent review index is `preview_index.md`. It links each 218px production-panel loop, 420px contact sheet, 4x contact sheet, and 218px light-gray edge check. The actual MCP background crop and its sampled `#17202A` margin color are recorded in `generation_provenance.md`.

The runtime DDS files decode as uncompressed BGRA32 and match their processed PNGs pixel-for-pixel. The full round-trip report is `notes/dds_roundtrip_report.json`; the runtime promotion report is `notes/runtime_promotion_report.json`; package digest is `F55E542C65E2604DB946F58D9FB7ACF599FB9C922058E8486525F95824677F56`.

The separate GUI worker reports that its post-change MCP render timed out without artifacts and its visual review remains unresolved; the parent owns any matched render follow-up through an available route. No GFX or GUI edit is needed for the existing sprite names and consumer behavior. This handoff does not claim in-game completion.
