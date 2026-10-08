# Event 006 ready-formable federation flags

Status: asset processing complete; parent visual review accepted all four motifs and all twelve native-size base files on 2026-10-06, recorded in ready_formable_flags_20261006.md and commit aeea04afc1d2838e53e25d30c2f48e2831a3c714.
Native formation and actual cosmetic-flag display remain unverified consumer behavior.

The four IDs were checked in the producer's palette table before generation, and their English names were checked in `localisation/english/006_independence_wave_ready_formable_contracts_l_english.yml`.
The engine-loaded palette definitions are in `common/countries/cosmetic.txt`; the producer table is archived at `docs/plans/006_independence_wave_plans/evidence_20261006/ready_cosmetic_palette_source.txt` and is not a second engine definition.

The parent uses the common fictional federation identity across democratic, communist, fascist and neutral governments rather than claiming four historically distinct political flags.
Forty-eight ideology aliases at the three native sizes are exact byte copies of these accepted twelve base outputs, preserving the charter symbol while preventing a base-country ideology flag from taking precedence over it.
The resulting sixty runtime paths and alias hashes are recorded in `docs/plans/006_independence_wave_plans/evidence_20261006/ready_cosmetic_flag_variants.json`, and installed by source commit 9e2837f8edc1633cd8e96415366821ca5dc16886.
This reuse records the parent choice within the human-authorized fictional-symbol scope and does not promote native display or historical-attestation claims.

These are original fictional alternate-history symbols for negotiated federation proposals; none claims historical attestation, and no real national or religious glyph was copied.

| Tag | Federation identity | Flag composition | Generation fit |
| --- | --- | --- | --- |
| `NCX` | North Caucasian Federation | Deep slate-blue field; three pale snow peaks linked by a warm amber defensive ridge; off-white starless sun above the central pass. | A distinct mountain-and-valley civic emblem with full-field flag framing. |
| `IDX` | Indus Federation | Teal river-blue field; golden geometric braid crosses a narrow abstract bridge, integrating parallel land and water strokes. | A transport-and-water emblem without chakra, religious, or national cues. |
| `MRX` | Maritime Federation | Dark navy field; warm-gold sun above exactly three islands and one connecting sail-or-wave arc. | A simple, balanced maritime emblem with three separate island masses. |
| `MSX` | Mainland Southeast Asian Federation | Jade and forest-green field; three stepped river-and-terrace bands meet at an open angular transport junction in muted gold and ivory. | A three-route civic emblem without a star, circle, disk, medallion, or roundel. |

## Processing and source mode

Source mode is native built-in ImageGen; prompt files are under `prompts/`, unchanged source masters are under `source_png/`, and provider lineage is recorded in `provider_lineage.md`.

Every master is opaque RGB and was resized directly, without cropping, to the canonical 82x52, 41x26, and 10x7 canvases using Lanczos resampling.

Processing did not draw, trace, recolor, quantize, normalize the field, remove a background, or simplify the generated emblem; final TGA pixel order and orientation were mechanically encoded to match the inspected vanilla flag schema.

Processed RGB PNG previews are under `processed_png/`; installed game files are opaque 32-bit TGA outputs under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

No DDS is included because this flag consumer uses native TGA flag paths.

## Native consumer and review evidence

The inspected canonical family is `.agents/skills/chaos-redux-event-assets/assets/gfx_references/flags/contact_sheet.png`, with source dimensions documented in that root's `CATALOG.md`.

The installed vanilla reference `gfx/flags/ICE.tga` uses 82x52, uncompressed 32-bit TGA, bottom origin, and an 8-bit alpha descriptor; its medium file uses the same convention at 41x26.

The installed vanilla `gfx/flags/small/ICE.tga` is 10x7, uncompressed 32-bit TGA, bottom origin, descriptor 0, and no TGA 2.0 footer; the small outputs follow that size-specific convention.

The normal and medium outputs use the matching 26-byte TGA 2.0 footer observed in the vanilla references.

`native_tga/decoded_pixel_proof.json` records the dimensions, hashes, headers, and exact decoded RGB equality between each of the twelve TGAs and its matching processed PNG; all twelve comparisons passed.

`contact_sheets/native_contact.png` presents the required outputs as unscaled native-pixel tiles; `contact_sheets/4x_contact.png` shows the source master preview plus all three flag sizes at 4x nearest-neighbour; `contact_sheets/light_dark_map_preview.png` shows opaque flags against light, dark, and muted-map surrounds without baking those surrounds into the flags.

The installed files were checked with `file`; none reports a top-origin flag.

## Installed file hashes

| Tag | Size | Processed PNG SHA-256 | Installed TGA | TGA SHA-256 | Bytes |
| --- | --- | --- | --- | --- | ---: |
| `NCX` | 82x52 | `60DF24849FDD2EFEAF6674BF4AECD69F11FC3A7C557810C9D80F3887BA227241` | `gfx/flags/NCX.tga` | `EF930D934E79116AC35DD4531FD69913CE94A2277660D7F7BA1C4F56FA2751BF` | 17100 |
| `NCX` | 41x26 | `BC81F69CBF616973FC037257F4A11B2E6F9E5A1295BF5B13F3BAB7B8FCB80A49` | `gfx/flags/medium/NCX.tga` | `C235EF89E7CD78CD7BC2D913FE3006F57F6E10F1D30D461B629C8E00B4B4BCCD` | 4308 |
| `NCX` | 10x7 | `28D10166C99DCBDD17AB7588EF5EC52FEFFF1B107B71F35FD03C9025E67640C8` | `gfx/flags/small/NCX.tga` | `B66E8383D52E34A95A1A01B814F20ED33CDB77DDD2131CB123A4DB161BB2BF96` | 298 |
| `IDX` | 82x52 | `F5CD27340592F5D1DBE56FB8A28F49FF16105846B308D69EDD7F0BF6EB2417E7` | `gfx/flags/IDX.tga` | `F118B162B7AFDED389A506A6327F5F59FBB9A8A001C29D193D1556FF45B23F5C` | 17100 |
| `IDX` | 41x26 | `02DA46900922AFE9358F63958BF3D91CAA625FEC84723BB7C0EF7686FB5E3DB8` | `gfx/flags/medium/IDX.tga` | `AE91EFE826638E495AF168FDBDA845679BF8F9674CB2306BAE145A350C4712AD` | 4308 |
| `IDX` | 10x7 | `8007335518C211E96BD40E10D158A9376E0E8A3866C6CEBA758C9CD080681E7F` | `gfx/flags/small/IDX.tga` | `5C6BB86EC11AA6C7DBF8460BC3626177F0241CF63FFF4D34F62985CF1A152177` | 298 |
| `MRX` | 82x52 | `87B8A45CC27BE096A81CD68FEA2359946B42E86854E005F033B77E4DD05CE5A2` | `gfx/flags/MRX.tga` | `5D1000EF90D5CFE18AF14839574FBC2480907EC804D6068AD3E134AE45CCE0DA` | 17100 |
| `MRX` | 41x26 | `8D2F090DFA104C7507817440C1F7EB7230E0381D6553E73D21E20351FD5A199A` | `gfx/flags/medium/MRX.tga` | `C27DD03C18556C123C4FF547B2D54AA3D0C43B3ADA40407296415CE405FCD391` | 4308 |
| `MRX` | 10x7 | `BC6DE9A2634AAE947F6CA47947E06B4EA42A079A60252B7DDFE11D40909F9694` | `gfx/flags/small/MRX.tga` | `18BA3749994560BFFA247D0D473907F05E6CB4C46BC33735A5E6FCBB2AB5F284` | 298 |
| `MSX` | 82x52 | `99C43D4364CE01AE33240D219F15467CC5D4C391F11A7895909A9EF5937F0816` | `gfx/flags/MSX.tga` | `052273DC244FA6CEC3BAED0D93FD5791987BD7D849EA7FA82EE3CB3A6339449C` | 17100 |
| `MSX` | 41x26 | `2C89F53FB1C8FF490D2351B514855E87A35B5F3DD504CA39CC3751C084E159CE` | `gfx/flags/medium/MSX.tga` | `F459B3704577FC85F2D40BAF2AD1A2F7C1A8AB643EE1A176FFC3D321DE42284D` | 4308 |
| `MSX` | 10x7 | `FF35E5533CEA3815E08D8A384FE6A12CB43B0B473D734945BA00CD0064B57FB5` | `gfx/flags/small/MSX.tga` | `1688CA967C196DA559567D8C677255302053AD828F242930729B6A9FC3B14350` | 298 |

## Remaining integration boundary

The route IDs and names exist, but this package does not change their gameplay triggers, country setup, event outcomes, or cosmetic-tag application.

No `.gfx`, country, gameplay, localisation, or character file was edited, and no in-game flag display is claimed.

## Parent review

The parent inspected all four native and nearest-neighbor four-times ladders.
The IDX source clearly depicts a railway bridge over the braided river; its tiny rendition is an abstract transport mark rather than an asserted religious symbol.
The MRX normal and medium sizes clearly depict a sun over three islands, and the tiny symbol remains a distinct gold light above a linked island band.
All four motifs, opaque fields and native framings are accepted as original fictional federation flags.
No palette swap, text, historical attribution or replacement emblem was introduced during review.
