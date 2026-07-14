# Validation record

Asset: `bio_designate_strategic_raid_staging_state`

## PNG validation

| File | Dimensions | Mode | Alpha min/max | Transparent | Partial | Opaque |
|---|---:|---|---:|---:|---:|---:|
| `source_png/bio_designate_strategic_raid_staging_state_source.png` | `1254x1254` | RGB (opaque source; inspected as RGBA) | `255/255` | `0` | `0` | `1572516` |
| `source_png/bio_designate_strategic_raid_staging_state_cutout.png` | `1254x1254` | RGBA | `0/255` | `802221` | `10205` | `760090` |
| `processed_png/bio_designate_strategic_raid_staging_state.png` | `32x32` | RGBA | `0/255` | `262` | `421` | `341` |

The alpha-check preview was inspected over a checkerboard. The processed icon has transparent corners and no visible green chroma fringe, white halo, or opaque square background.

## DDS validation

File: `gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds`

- Magic: `DDS `
- Header size: `124`
- Declared dimensions: `32x32`
- Pitch: `128`
- Pixel format size: `32`
- Pixel-format flags: `65` (`RGB | ALPHAPIXELS`)
- FourCC: `0`
- Bit count: `32`
- Masks: `R=0x00FF0000`, `G=0x0000FF00`, `B=0x000000FF`, `A=0xFF000000`
- Caps: `0x1000` (`DDSCAPS_TEXTURE`)
- Mipmap count: `0` / one base level with no mip payload
- Pixel payload: `4096` bytes; expected `32 * 32 * 4 = 4096`
- Total file length: `4224` bytes; expected `128 + 4096 = 4224`
- DDS alpha min/max: `0/255`
- DDS transparent/partial/opaque pixels: `262 / 421 / 341`
- Header and payload validation: `PASS`

## SHA-256

| File | SHA-256 |
|---|---|
| `source_png/bio_designate_strategic_raid_staging_state_source.png` | `ecf92b5153c1e89a3c0b72db637f8e457e48c1d5370cf282443610c865eead87` |
| `source_png/bio_designate_strategic_raid_staging_state_cutout.png` | `3195717d4e2d8ebbb0ee9d8bb69f757ed51f600e77c58a5da0c0680553066591` |
| `processed_png/bio_designate_strategic_raid_staging_state.png` | `644780ba905b7b8afc06c60ee95a0d1db62edded9534da18f2878253164557d4` |
| `gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds` | `8f2bae43b1b818046dd4eac319d1c1baff67b33bee0c0c31118aac0bb948497f` |

## Scope validation

- No gameplay files edited.
- No localisation files edited.
- No interface `.gfx` or `.gui` files edited.
- No specs or shared docs edited.
- Sprite wiring remains intentionally outstanding for the main agent.
