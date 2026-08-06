# Event 006 IW-024 Banat / AXX — Otto Roth portrait source-placeholder handoff

Date: 2026-08-06.

Owner: `chaosx_portrait_creator`.

## Handoff result

The grounded male portrait candidate is **Otto Roth** (`otto_roth`), a Temesvár/Timișoara lawyer, journalist, trade unionist, and Social Democratic regional politician who served as Commissioner-in-Chief of the Banat Republic from 31 October 1918 to 17 January 1919. He lived through the 1936 setting and is historically connected to Banat without inventing a modern officeholder. The selected portrait mode is `source_placeholder`; no ImageGen, ComfyUI, RunPod, repaint, or styled final was used or requested.

Stable runtime portrait basename: `portrait_AXX_independence_wave_otto_roth`.

Stable runtime sprite: `GFX_portrait_AXX_independence_wave_otto_roth`.

Final runtime path: `gfx/leaders/006_independence_wave/portrait_AXX_independence_wave_otto_roth.dds`.

Portrait-specific GFX: `interface/006_independence_wave_iw024_banat_portraits.gfx`.

The AXX package contract is now admitted conditionally through the central Event 006 dispatcher. The parent-owned character definition, localisation, setup, focus, decision, idea, party, AI, and country surfaces are wired in the AXX package files; this handoff remains the source-placeholder evidence for the portrait only.

## Source and rights evidence

The unchanged master is archived at `docs/assets/portraits/006_independence_wave/iw024_banat_otto_roth_source_placeholder_2026_08_06/portrait_AXX_independence_wave_otto_roth_source.jpg`.

Source page: [Wikimedia Commons — Dr. Otto Roth.jpg](https://commons.wikimedia.org/wiki/File:Dr._Otto_Roth.jpg).

Original binary: `https://upload.wikimedia.org/wikipedia/commons/f/f2/Dr._Otto_Roth.jpg`.

Commons describes the image as a circa-1930 portrait of Dr. Otto Roth, former Commissioner of the Banat Republic, as a Romanian lawyer, credits an Adevărul Timișoara article, identifies the author as unknown, and applies `PD-RO-photo` plus `PD-1996`. Commons labels the file `Public domain` and reports no attribution requirement. The source is RGB `627x1026`, 89,883 bytes, SHA-256 `c9ab09e6d7f13d002de703818b47dd5ea91ccdba4526ea23d5bb31c7698448b3`.

Role/date corroboration is recorded in `source_provenance.json` and the [Otto Roth biography](https://en.wikipedia.org/wiki/Otto_Roth); Wikipedia is not the image-rights authority.

## Crop and processing evidence

The immutable crop was made with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` at decoded coordinates `[18, 5, 609, 800]` (left, top, right, bottom). The crop is RGB `591x795`, SHA-256 `05f9c7e3f46381ebc3763704f07a4ecacb94a507f72810bfc4ab1655712bf6a1`, and its JSON equality evidence is `portrait_AXX_independence_wave_otto_roth_source_crop.json` with `status: exact_source_crop_verified` and master/crop RGBA SHA-256 `bf7d9c46e3395ec9370f1f380eebb21adc6211c32a9b309e560cd12a2d83a81d`.

The deterministic candidate `portrait_AXX_independence_wave_otto_roth.png` is RGB `156x210`, 42,882 bytes, SHA-256 `2269029043683f617b9dce9e604bf2139303c3a52c1686db3278b4565b672647`. It was made by converting the immutable crop to RGB and resizing once with Pillow `11.1.0` `Image.Resampling.LANCZOS`; no other pixel operation was applied. The 4x nearest-neighbour review enlargement is `portrait_AXX_independence_wave_otto_roth_4x_nearest.png` (`624x840`, SHA-256 `c6dfe98ded686f0d320578818ee22553a19eaa16757f28c63efc6582aa83abed`).

## DDS and runtime evidence

The candidate was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 156 --height 210` to `gfx/leaders/006_independence_wave/portrait_AXX_independence_wave_otto_roth.dds`.

- Dimensions: `156x210`.
- Length: `131168` bytes (`128 + 156*210*4`).
- SHA-256: `82e616bda81fee899f3d9a7fdfcc7557f2b487452e8591dba77319492c48f046`.
- Header: `DDS ` magic; header size `124`; pixel-format size `32`; flags `65`; fourCC `0`; bit count `32`; BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`; texture caps `0x1000`; no mipmaps.
- Alpha range: `255..255`.
- DDS decode: pixel-identical RGBA bytes to processed PNG (`c4fed05fe409c0f68c461e05e814f192e381f92455607b375b18363e95a7c237`).

## Review, gate, and blockers

Producer review passed for male identity, attribution, public-domain record, circa-1930 era fit, head-and-shoulders framing, caption exclusion, full leader canvas, and preservation of visible face, hairline, expression, collar, tie, shoulders, and source tonal structure. Canonical installed-vanilla country-leader references were inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the eight native `156x210` references. Independent parent source-placeholder admission review also passed at native and 4x nearest-neighbour scale.

AXX package admission is **source-attested and conditionally selectable**. The package has a central dispatch adapter, content attestation, identity-specific setup/final/cleanup path, character roster, AI profile, state-82 anchor, and flat alternate-history flag handoff. The runtime portrait remains an unchanged source placeholder under the current historical-portrait policy, not a styled final.

Skipped by scope: no advisor/dossier/small portrait, no female portrait, no styled-final request, no RunPod operation, no ImageGen, no gameplay or localisation edits, and no live-game validation. The source-placeholder candidate is ready for parent review and future package wiring at the stable runtime path.
