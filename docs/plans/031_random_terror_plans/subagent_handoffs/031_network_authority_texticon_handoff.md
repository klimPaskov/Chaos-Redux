# Event 31 Network Authority texticon handoff

Status: complete for the bounded static DDS production request.

The final texture is a readable 24x24 alpha-backed inline texticon derivative of the approved Event 31 network-directorate icon.

## Runtime output

| Surface | Path | Metadata |
| --- | --- | --- |
| Final DDS | `gfx/texticons/031_random_terror/random_terror_network_authority_texticon.dds` | 24x24, 2432 bytes, one-level uncompressed BGRA8 DDS |
| Processed PNG | `docs/assets/031_random_terror/processed_png/random_terror_network_authority_texticon.png` | 24x24 RGBA PNG, alpha 0..255, visible alpha bbox `(1, 1, 23, 23)` |
| Source evidence | `docs/assets/031_random_terror/source_png/random_terror_network_authority_texticon_source.png` | 64x64 RGBA copy of the approved Event 31 final icon source |
| DDS roundtrip | `docs/assets/031_random_terror/roundtrip_png/random_terror_network_authority_texticon_roundtrip.png` | 24x24 RGBA decode of the final DDS |

The parent owns the sprite name, inline token, `.gfx` registration, localisation, and gameplay wiring because no new wiring was authorized in this task.

## Reference inspection

The required Event 31 contact sheets were inspected before individual source selection: `docs/assets/031_random_terror/contact_sheets/031_idea_icons_contact_sheet.png` and `docs/assets/031_random_terror/contact_sheets/031_decision_mission_icons_contact_sheet.png`.

The canonical reference contact sheets `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/contact_sheet.png` and `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/contact_sheet.png` were inspected from the single canonical reference root.

The closest approved Event 31 source is `docs/assets/031_random_terror/processed_png/idea_random_terror_network_directorate.png` and its runtime counterpart `gfx/interface/ideas/031_random_terror/idea_random_terror_network_directorate.dds`.

This source was selected because its central radio mast and connected network nodes directly represent Network Authority without introducing sacred imagery, real extremist branding, or hostile religious symbolism.

The canonical reference root has no dedicated texticon family or texticon contact sheet.

The installed vanilla texticon registry `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/texticons.gfx` and representative vanilla `18x18` and `20x20` texticons were inspected, together with Chaos Redux `18x18` texticons in `gfx/texticons/` and the Event 014 cost-texticon handoff.

No installed 24x24 texticon precedent was found during direct enumeration, so 24x24 is used because it is the exact parent-specified target rather than an inferred family size.

## Source and processing

The source evidence copy preserves the approved Event 31 processed icon before derivative processing.

The source alpha extrema are `0..255` with source visible alpha bbox `(2, 2, 62, 62)` and transparent corner pixels.

Processing cropped to the source visible alpha bbox `(2, 2, 62, 62)`, resized the cropped 60x60 content to 22x22 with alpha-safe premultiplied-RGB Lanczos resampling, and placed it at `(1, 1)` on a transparent 24x24 canvas.

Only sub-visible alpha cleanup was applied after resampling: alpha values below `8` were set to zero and their RGB values were cleared.

No background-removal fallback was used.

The official ImageGen tool was used for one constrained transparent derivative review candidate using the approved Event 31 network-directorate icon as its sole visual reference.

That candidate was rejected from runtime because it introduced additional radial rings and laurel-like side detail instead of preserving the approved silhouette.

The rejected candidate is retained at `docs/assets/031_random_terror/notes/rejected_network_authority_texticon_imagegen_candidate.png` and its prompt record is at `docs/assets/031_random_terror/prompts/031_network_authority_texticon_prompt.md`.

The runtime output is therefore the approved Event 31 icon derivative, not an ImageGen alias, placeholder, copied texticon, or newly invented hostile/sacred emblem.

## Verification

The final DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

The DDS header has `DDS ` magic, a 124-byte header, `DDS_PIXELFORMAT` size `32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`, and `DDSCAPS_TEXTURE` `0x1000`.

The declared dimensions are `24x24`, the exact file length is `128 + 24 * 24 * 4 = 2432` bytes, alpha extrema are `0..255`, and all four corners decode to `(0, 0, 0, 0)`.

The decoded DDS roundtrip is pixel-identical to the processed PNG, including alpha.

The contact sheets used for visual review are `docs/assets/031_random_terror/contact_sheets/031_network_authority_texticon_contact.png`, `docs/assets/031_random_terror/contact_sheets/031_network_authority_texticon_contrast.png`, and `docs/assets/031_random_terror/contact_sheets/031_network_authority_texticon_scale_compare.png`.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| Source evidence PNG | `AD388A9D455CC0868513013312D367ABD275497A9BC4D7D6DACFFB43E802C62D` |
| Processed PNG | `4C50D03509A6FB42AAB3B9813A9AE122E951E1F92B1DF7429B3B3301EE2A23D3` |
| Final DDS | `A793A673D2275A68C200874F96F05CA4C03724A9592138F3893E606B187168E4` |
| DDS roundtrip PNG | `4C50D03509A6FB42AAB3B9813A9AE122E951E1F92B1DF7429B3B3301EE2A23D3` |
| Main review contact sheet | `0A4B074FED40FC4482D0ABEA89F162F24D90B4BD57AC89595530D8CC6BB3AC04` |
| Contrast review contact sheet | `71E9B9E0D8B3AF7233B3632BC108795A08C8ED65C3B302E6D9FCB97969D84C27` |

## Scope boundary

Only the final DDS and asset evidence/handoff files were created for this request.

No `interface/031_random_terror.gfx`, localisation, gameplay, or shared Event 31 manifest was edited.

No placeholder remains in the final DDS and no runtime alias was used.
