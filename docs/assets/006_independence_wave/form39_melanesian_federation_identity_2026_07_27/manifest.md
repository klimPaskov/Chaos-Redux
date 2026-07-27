# FORM-39 Melanesian Federation identity flag manifest

Status: `needs_user_review`.

The visual package is complete and the FIJ/PNG/WPG consent-led FORM-39 adapter is source-implemented, but runtime admission remains intentionally fail-closed pending the six named research, reservation, flat-flag, and identity-review inputs plus collision tests. `MFX` is a proposed/reserved route tag candidate only and remains `needs_user_review`; it is not an approved gameplay identity. The parent agent must not treat this asset as proof that the formable is runtime-ready.

## Requirement-to-runtime crosswalk

| Requirement | Evidence | Runtime path | State |
| --- | --- | --- | --- |
| ImageGen source master | `source_png/FORM39_melanesian_federation_imagegen_source.png` | Evidence only | Complete |
| Normal flag | `processed_png/FORM39_melanesian_federation_normal.png`, `dds/MFX.dds` | `gfx/flags/MFX.tga` | Needs user review for final X-tag admission |
| Medium flag | `processed_png/FORM39_melanesian_federation_medium.png`, `dds/MFX_medium.dds` | `gfx/flags/medium/MFX.tga` | Needs user review for final X-tag admission |
| Small flag | `processed_png/FORM39_melanesian_federation_small.png`, `dds/MFX_small.dds` | `gfx/flags/small/MFX.tga` | Needs user review for final X-tag admission |
| Visual comparison | `review/FORM39_flag_contact_sheet.png` | Review only | Complete |
| Prompt/provenance | `prompt_record.md` | Review only | Complete |
| Sprite/wiring handoff | `gfx_handoff.md` | Parent-owned `.gfx` wiring | Pending adapter/tag approval |

## Identity and source mode

- Formable: `FORM-39`, Melanesian Federation.
- Classification: fictional alternate-history negotiated federation.
- Source mode: official built-in ImageGen, generated from scratch. No historical flag is asserted and no real national flag is reconstructed.
- Accepted design direction: negotiated federation of Fiji, Papua, West Papua, and specifically researched island packages; island anchors and member consent; strong cultural autonomy and maritime logistics.
- Symbol rationale: ocean blue represents shared maritime space; the gold route band represents the federation's maritime logistics and civic compact; the ivory three-lobed mark is an invented, non-sacred federation emblem with three internal divisions for the three named member packages; dark teal gives a clear heraldic outline at reduced sizes.
- Palette: ocean blue `#123B5A`, gold `#E6B94A`, ivory `#F2E8D5`, dark teal `#0C2B36`.
- Geometry: flat horizontal field, centered gold band, centered symmetrical three-lobed emblem; no fabric, folds, pole, perspective, scene, lighting, gradients, text, or watermark.

## Dimensions and hashes

All runtime TGAs are uncompressed 32-bit truecolor, bottom-left origin (`descriptor 0x08`), with exact legacy sizes 82x52, 41x26, and 10x7. DDS files are one-level uncompressed BGRA with the repository converter's 128-byte legacy header and exact lengths.

| File | Dimensions | SHA-256 |
| --- | ---: | --- |
| `source_png/FORM39_melanesian_federation_imagegen_source.png` | 1619x971 | `a397e54382e0296282f63b3cd63b9d641ffdf90d1704809ba23ad46002fab839` |
| `processed_png/FORM39_melanesian_federation_normal.png` | 82x52 | `101dc4ee64e563a4cef55197338b58d2a8f132dd08f54efcc57e8fedadb4cd71` |
| `processed_png/FORM39_melanesian_federation_medium.png` | 41x26 | `46b4b891417eaa79fb77ead7e663cde2c4c300d2549455567f9110862ee70478` |
| `processed_png/FORM39_melanesian_federation_small.png` | 10x7 | `cccf5a299df70c6fc37cfffb65026769a84d648bfb2c72e971cdb8159232d6fb` |
| `dds/MFX.dds` | 82x52 | `bdde7f6de5eb1abfcf80017f833c4d2aa1746e89149861434c1405f1eb489560` |
| `dds/MFX_medium.dds` | 41x26 | `85186268d6919e40613d5cef822182778bbcc01755dc8d74bd447144ac0d54da` |
| `dds/MFX_small.dds` | 10x7 | `24e005b884e026c3dd3c28a48f86ba2567ae102a5964db57fc1d8e6486df435e` |
| `runtime_tga/MFX_normal.tga` | 82x52 | `63cc5ce467ba982abb901003371cfdec13f4a280ad11e4435cc315d5ed66e851` |
| `runtime_tga/MFX_medium.tga` | 41x26 | `441060d6bdaf3c81fe283227f2016e709ee9aede8158c9951a490b3e07b92859` |
| `runtime_tga/MFX_small.tga` | 10x7 | `5b2f9e9bc87054c8157bce7329a2ef5decc2fd7890d462378dab29d91e701db2` |
| `review/FORM39_flag_contact_sheet.png` | 1568x768 | `ea68c547ade570589fc261bd5fa06c393037333193a45a95f578787a429521d5` |

The runtime copies under `gfx/flags/` are byte-identical to the package TGAs: normal `63cc5ce467ba982abb901003371cfdec13f4a280ad11e4435cc315d5ed66e851`, medium `441060d6bdaf3c81fe283227f2016e709ee9aede8158c9951a490b3e07b92859`, small `5b2f9e9bc87054c8157bce7329a2ef5decc2fd7890d462378dab29d91e701db2`.

## Review notes

The source and ladder are flat orthographic graphics. The normal and medium exports retain the three-lobed silhouette and central band. At 10x7 the emblem collapses to a compact three-lobed light mark over the gold band; it is intentionally reviewed enlarged with nearest-neighbour in the contact sheet. If the parent or an independent reviewer judges the small silhouette insufficient, request a new ImageGen design rather than redrawing or replacing the emblem locally.
