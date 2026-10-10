# Event 006 regional formable federation flags

Status: three original flags generated, processed, installed and decoded back for exact equality on 2026-10-10. Native formation and actual in-game display of the cosmetic flags are user-owned and unverified.

The three tags are registered in `common/countries/cosmetic.txt` (`LKX`, `HLX`, `IOX`, palette comments FORM-27, FORM-29, FORM-31); their names are set in localisation by the parent. This package changes no script, localisation, `.gfx`, GUI, or country file.

These are original fictional alternate-history symbols for negotiated federation proposals. None claims historical attestation, and no real national, royal or religious glyph was copied; no historical flag design was used as an input.

The method mirrors `docs/assets/006_independence_wave/ready_formable_flags_20261006/` exactly: image generation for each distinct design, direct Lanczos resize of the accepted master to the three native canvases, mechanical encoding to the vanilla-convention TGA, and byte-identical ideology aliases.

## Design table

| Tag | Name | Field (specified, generated) | Emblem | Palette accents |
| --- | --- | --- | --- | --- |
| `LKX` | Great Lakes Federation (Buganda, Rwanda, Burundi) | green rgb 58 112 58, about 63 113 61 | Three layered ivory lake-ripple arcs, each a bold band with angular squared tips, resting beneath one small angular ochre hill. | ivory about 238 230 203, ochre about 232 196 96 |
| `HLX` | Horn League State (Harar, Afar state, Somaliland, Tigray) | terracotta rgb 142 64 40, about 135 65 42 | Three-tier stepped ivory plateau over one curved sand coastline arc over a row of five sand well-dots. No cross, crescent, star, lion, religious glyph or lettering. | ivory, sand about 232 198 120 |
| `IOX` | Indian Ocean League State (Madagascar, Mauritius) | turquoise-blue rgb 18 98 126, about 13 100 130 | One large and one small faceted ivory island joined by a gold sea-lane arc above two ivory wave bands. No sun disc or star. | ivory, gold about 235 188 92 |

Distinctness: LKX is a radial fan on a mid green and is separate from the dark-green three-prong MSX; HLX is a rectilinear stepped block on terracotta, the only warm field in the set; IOX is a pair of masses with an arch on turquoise and carries no sun, unlike the navy sun-over-islands MRX. NCX (mountains and sun on slate blue) and IDX (bridge and braids on teal) share no emblem structure with any of the three. See `contact_sheets/4x_contact.png` and `contact_sheets/normal_3x_all.png`.

## Source mode and lineage

Source mode is the gptimage MCP image-generation route (`mcp__gptimage__generate_image`, quality `high`, requested size `1600x1008`, delivered 1575x999), no reference image, one call per candidate, prompts in `prompts/<TAG>.md`. The tool reports no model version, so none is asserted.

Candidate 1 of each flag was rejected and candidate 2 accepted, so each flag used 2 of the 3 permitted iterations:

| Tag | Candidate 1 (rejected) | Candidate 2 (accepted) |
| --- | --- | --- |
| `LKX` | `source_png/LKX_rejected_v1_transparent.png`: RGBA, field transparent, emblem only. | `source_png/LKX_imagegen_master.png` |
| `HLX` | `source_png/HLX_rejected_v1_transparent.png`: RGBA, transparent field with a ragged brown halo and dark fringe. | `source_png/HLX_imagegen_master.png` |
| `IOX` | `source_png/IOX_rejected_v1_transparent.png`: RGBA, transparent field, pale emblem with ragged island edges and an arc detached from both islands. | `source_png/IOX_imagegen_master.png` |

The rejected candidates were not composited onto a drawn field, repaired, or used as inputs. Candidate 2 added an explicit opaque-canvas instruction and produced an opaque RGB flat field in each case. Accepted master hashes:

| Tag | Master | Size | SHA-256 |
| --- | --- | --- | --- |
| `LKX` | `source_png/LKX_imagegen_master.png` | 1575x999 | `43E2A089F0C84DC9495D8368FD8CF79FF508373FDD6D3800DA2647F0A453C113` |
| `HLX` | `source_png/HLX_imagegen_master.png` | 1575x999 | `C6DEE7DE2D2CF45CD326478250698A54DAE6DB8B3C6405C575B98EDD827688C8` |
| `IOX` | `source_png/IOX_imagegen_master.png` | 1575x999 | `457A1DD686DB9414EE126DB8BF3940ADF04A6D4BD0ECB7FDBA182124DDE33719` |

## Processing

Every accepted master is opaque RGB and was resized directly, without cropping, to 82x52, 41x26 and 10x7 with Lanczos resampling (the masters are 1.577:1 against the 1.577:1 canvas, so no visible stretch). Nothing was drawn, traced, recoloured, palette-quantised, background-removed or simplified. Pixels were encoded mechanically to TGA.

TGA schema, read from `gfx/flags/NCX.tga`, `gfx/flags/medium/NCX.tga` and `gfx/flags/small/NCX.tga`: uncompressed 32-bit true colour (type 2), BGRA pixel order, bottom-left origin rows, alpha 255 throughout. Normal and medium: image descriptor `0x08` and the 26-byte TGA 2.0 footer (`TRUEVISION-XFILE.`). Small: descriptor `0x00`, no footer. The 18-byte headers (all three sizes) and the 26-byte footers (normal and medium) of the new base files are byte-identical to NCX's; file sizes are 17100, 4308 and 298 bytes, equal to the sibling flags. `file` reports `Targa image data - RGBA 82 x 52 x 32 - 8-bit alpha`, `RGBA 41 x 26 x 32 - 8-bit alpha` and `RGB 10 x 7 x 32` for each tag, and no file reports `- top`.

Ideology aliases follow the sibling pattern, confirmed against the existing `gfx/flags/NCX_*.tga` set (all four aliases byte-identical to the base file at all three sizes): for each tag and size, `<TAG>_communism.tga`, `<TAG>_democratic.tga`, `<TAG>_fascism.tga` and `<TAG>_neutrality.tga` are exact byte copies of the base file. That is 9 base files plus 36 aliases, 45 TGAs. The shared design is deliberate, as in the sibling package: the fictional federation identity is the same under every government.

## Verification run

- Each of the nine base TGAs was decoded by a purpose-written reader (header, BGRA, bottom-up rows) and compared with its processed PNG: exact RGB equality, 9 of 9. An independent decode through Pillow's TGA reader also matched all nine.
- Every one of the 36 alias files was read back and compared to its base file byte for byte.
- Re-running the pipeline reproduced all nine base TGAs with identical SHA-256 values.
- `contact_sheets/native_contact.png` shows NCX, IDX, MRX, MSX, LKX, HLX, IOX at unscaled native sizes; `contact_sheets/4x_contact.png` shows the same set at 4x nearest-neighbour; `contact_sheets/normal_3x_all.png` shows the seven normal flags side by side. All seven were viewed: the three new emblems are readable at 82x52 and 41x26, and at 10x7 each keeps a distinct colour-and-mass read.
- `native_tga/decoded_pixel_proof.json` (local evidence, not committed) records source, PNG and TGA hashes, descriptor, footer, and alias paths.
- Not verified: display in the engine, orientation inside the game window, and cosmetic-tag application. The orientation matches the vanilla-derived NCX header and row order, but no game was launched.

## Installed file hashes

Processed PNG previews are local evidence under `processed_png/` and are not committed. Alias files share the SHA-256 of their base file.

| Tag | Size | Processed PNG SHA-256 | Installed TGA | TGA SHA-256 | Bytes |
| --- | --- | --- | --- | --- | ---: |
| `LKX` | 82x52 | `9A572C00400B0B63C7E39A5C097266B2F3F5C4216478EFAEAF2C0C792D997072` | `gfx/flags/LKX.tga` | `E817145F2B7C7F56D37BC648147DB59E9016321D73A7AB459F2E35A934F85065` | 17100 |
| `LKX` | 41x26 | `E5300D1BA0A3A26AE9C051734964AC008B487A2335A0843E331E89D71D500E5C` | `gfx/flags/medium/LKX.tga` | `D6F7116FECD89122B57C4841E9C93CD559E1EE72DDB691C914DEAD064C038818` | 4308 |
| `LKX` | 10x7 | `2C7A12B5A5D9B754FCF9927638278B6176C7F7C04750AD7345C4BFBF071F54EA` | `gfx/flags/small/LKX.tga` | `7D049EAD32E62D2E958E633B42481CDAFC127C0116ABBED93DD7142D0B6B079F` | 298 |
| `HLX` | 82x52 | `5F92E556D4E8634F6652BA4240F62D7962C81F46F78B934D58090EEF4681E429` | `gfx/flags/HLX.tga` | `9193EC86C91081E2537B50A8B5D587C90EDFB5904D16302860C7172CE00F74CC` | 17100 |
| `HLX` | 41x26 | `18ED60EA671629006F4A94E1110A94516AC64DF757B21E1DD7634001B1C968C7` | `gfx/flags/medium/HLX.tga` | `92FAC456B4C9C84439E14F88F1C87009D66EEED4AC1FF100DEB3FDA9DEC9D476` | 4308 |
| `HLX` | 10x7 | `383B4800DB2A26DC48E35833B94C0172467E372B614B2C31D4DB0A63A5A3FF64` | `gfx/flags/small/HLX.tga` | `B0B3318E23BB277CC1931C990CD68E251587917C48243831A452DD63C795E6C9` | 298 |
| `IOX` | 82x52 | `9DE7DC6720B936A7954426D085FE89CC471473EB5EA0EA9BB040EBC844A8FA8B` | `gfx/flags/IOX.tga` | `3CFF14308D3A48012FA4388C8BF77579A57E6AEEAEA3CE48791E3FB027833247` | 17100 |
| `IOX` | 41x26 | `3DB03E8CE85881FE7755E9355294777F9DDB6A9AB4641CA681C5C5FA6A5BC431` | `gfx/flags/medium/IOX.tga` | `B8C50BD414A254A3BFDB9BFA39200FF98B66B235CF8FB2132FB4234123409692` | 4308 |
| `IOX` | 10x7 | `0DDE81AF6925B5B99BAC06CF8D7D13AD7D588D6771AAFA5970DE66EE24C415B3` | `gfx/flags/small/IOX.tga` | `CA475B8560DCEEC1C416C2506CCF6E2ED7B92AB69120E620BF6958DE0E4EC2E1` | 298 |

## Remaining integration boundary

No gameplay trigger, cosmetic-tag application, localisation or `.gfx` was edited here. Use `gfx_handoff.md` for the paths. Whether each formable route selects the intended tag and the engine displays all three sizes is the parent's integration and the user's live check.
