# Event 016 base portrait source handoff

Date: 2026-07-14

## Scope

This handoff completes the bounded source and static-output tranche for Doctor Warren Kruger stage 0. It preserves the exact user-required tracked face, creates the verified large scientist or leader asset and small advisor asset, and leaves all GFX, character, gameplay, GUI, localisation, event, spreadsheet, and later-stage art wiring to the parent.

No generated or alternate face was used. No placeholder or fallback was introduced.

## Authoritative source

| Field | Evidence |
| --- | --- |
| Tracked source | `gfx/leaders/scientists/generic_scientists/portrait_generic_biowarfare_europe_male_01.dds` |
| Git provenance | Added by Klim Pashkov in commit `6aa363c64195eb9dbb4faed174e8493287666715` on 2025-08-08, `Biowarfare facilities scientists and historical starting locations` |
| Git tracking | Tracked mode `100644`, current blob `fbf51955d868bae649fdc60f526aa5edf65721b3` |
| Source SHA-256 | `5D0CF3F973B6099DB895C96A6FED9544F30873076985DDF885032793C5183075` |
| Decoded-pixel SHA-256 | `CF69E37EDF7A52470CE80492549C7EA60CE571397F3BA4F703932E49EDA7B9A0` |
| Source format | Legacy DDS, uncompressed 32-bit BGRA, `156x210`, pitch `624`, eight mip levels, alpha `255..255` |
| Mip dimensions | `156x210`, `78x105`, `39x52`, `19x26`, `9x13`, `4x6`, `2x3`, `1x1` |
| Immutable Event 016 copy | `docs/assets/016_brilliant_scientist/source_dds/originals/portrait_generic_biowarfare_europe_male_01.dds` |
| Decoded reference PNG | `docs/assets/016_brilliant_scientist/source_png/portraits/portrait_generic_biowarfare_europe_male_01_decoded.png` |
| License status | Repository-tracked and explicitly approved by the user for Event 016. No separate license or public-domain declaration accompanies the file. Do not describe it as public domain or externally cleared. |

The approved asset is distinct from vanilla `gfx/leaders/scientists/generic_scientists/portrait_generic_europe_male_01.dds`: both its file hash and decoded-pixel hash differ. The immutable Event 016 copy and large runtime copy are byte-identical to the tracked Chaos Redux source.

## Why there are exactly two runtime files

Official and vanilla evidence supports one large and one small portrait, not three independent stage-0 DDS files:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/_documentation.md` defines the scientist role on the same character object.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` documents `add_scientist_role`, `generate_scientist_character`, and `set_portraits`.
- Vanilla scientist entries such as `GER_heisenberg` and `USA_robert_oppenheimer` use `portraits = { army = { large = ... small = ... } }` on the scientist character.
- Vanilla `_scientists_portraits.gfx` points scientist `large` sprites to `156x210` DDS files under `gfx/leaders/scientists/`.
- Vanilla advisor or theorist `small` sprites such as `idea_heisenberg.dds`, `idea_robert_oppenheimer.dds`, and `idea_von_braun.dds` are `65x67`.
- The offline `Portrait modding`, `Graphical asset modding`, and `Interface modding` references confirm portrait pools, sprite registration, and `spriteType` use.

The `156x210` stage-0 file is therefore the shared scientist `large` portrait and later leader portrait. A second byte-identical `scientist_doctor_warren_kruger_stage_0.dds` would add no engine surface and was deliberately not created. The advisor asset is `65x67`, following the actual vanilla character-small precedent rather than the generic `64x64` idea-icon guideline.

## Output inventory

| Output | Dimensions | SHA-256 | Notes |
| --- | ---: | --- | --- |
| `docs/assets/016_brilliant_scientist/source_dds/originals/portrait_generic_biowarfare_europe_male_01.dds` | `156x210`, eight mips | `5D0CF3F973B6099DB895C96A6FED9544F30873076985DDF885032793C5183075` | Immutable source copy |
| `docs/assets/016_brilliant_scientist/source_png/portraits/portrait_generic_biowarfare_europe_male_01_decoded.png` | `156x210` | `13BE2B86DB91C89A2C3588DC7B2A22D64563DB9B8632AB82DCC334272114318D` | Main-mip RGBA inspection and generation reference |
| `docs/assets/016_brilliant_scientist/processed_png/portraits/leader_doctor_warren_kruger_stage_0.png` | `156x210` | `13BE2B86DB91C89A2C3588DC7B2A22D64563DB9B8632AB82DCC334272114318D` | Pixel-identical processed preview for the shared large portrait |
| `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_0.dds` | `156x210`, eight mips | `5D0CF3F973B6099DB895C96A6FED9544F30873076985DDF885032793C5183075` | Byte-identical stage-0 runtime copy |
| `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png` | `65x67` | `2725A4E73BBBB230E80254C9E3D23A55C06245173509DCD6332C6AAB863C9980` | Face-preserving advisor composition |
| `gfx/interface/ideas/016_brilliant_scientist/idea_doctor_warren_kruger_stage_0.dds` | `65x67`, one level | `487F5D52167543FAFB998A103C1576321AC1DE67FFFDCF804F3B3AAF55122503` | Standard converter output, legacy uncompressed BGRA |

## Processing record

The source DDS was decoded with Pillow 11.1.0. The large PNG and runtime DDS retain the source composition and pixels without crop, recolour, repaint, retouching, generation, or facial alteration.

The advisor PNG uses only a deterministic crop and resize of the approved source. Crop box `(3, 0, 153, 155)` retains the full hair silhouette, face, shoulders, laboratory clothing, and original blue background. The crop was resized to `65x67` with Lanczos resampling. No frame, text, filter, colour change, generated content, or replacement detail was added. `.tools/convert_to_dds.py` converted this PNG to a one-level legacy BGRA DDS through its installed FFmpeg fallback.

## Proposed stable GFX names

Target file: `interface/016_brilliant_scientist.gfx`

```text
spriteTypes = {
	spriteType = {
		name = "GFX_portrait_KRG_doctor_warren_kruger_stage_0"
		texturefile = "gfx/leaders/KRG/leader_doctor_warren_kruger_stage_0.dds"
	}

	spriteType = {
		name = "GFX_idea_doctor_warren_kruger_stage_0"
		texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_doctor_warren_kruger_stage_0.dds"
	}
}
```

Suggested portrait assignment for the single persistent Kruger character:

```text
portraits = {
	army = {
		large = GFX_portrait_KRG_doctor_warren_kruger_stage_0
		small = GFX_idea_doctor_warren_kruger_stage_0
	}
}
```

The main agent must confirm the final portrait scope while implementing the character and must keep both identifiers stable once wired. The same large sprite should be used for Kruger's scientist role and any later country-leader role unless a staged replacement sprite is active.

## Validation evidence

- The tracked source, immutable source copy, and large runtime DDS are byte-identical.
- The decoded reference and large processed PNG are pixel-identical to the source DDS main mip.
- The large DDS header declares legacy uncompressed 32-bit BGRA with the expected masks and complete eight-level mip chain. Its exact length is `174608` bytes, matching the summed mip payload plus the 128-byte header.
- The advisor DDS header declares legacy one-level uncompressed 32-bit BGRA with `DDSCAPS_TEXTURE`, correct masks, and exact length `17548` bytes.
- Decoded advisor DDS pixels are pixel-identical to the processed advisor PNG.
- Both final assets were visually inspected at original resolution. The face and stage-0 composition remain recognizable and unchanged apart from the documented small-surface crop.

## Remaining parent work and risks

- Add the two sprite definitions to `interface/016_brilliant_scientist.gfx` and wire the character portrait block. This subagent did not edit either surface.
- The source's external redistribution rights are unresolved because no standalone licence metadata exists. This does not block the user-authorized in-repository Event 016 use, but it must remain explicit in any external asset ledger.
- Stages I through IV, severe animations, custom UI crops, event-picture crops, and all other Event 016 art remain outside this bounded tranche.
- No simplification or fallback was used within the assigned stage-0 source package.
