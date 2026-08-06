# IW-024 Banat — Otto Roth source-placeholder portrait manifest

Date: 2026-08-06.

Asset owner: `chaosx_portrait_creator`.

Scope: grounded male historical country-leader portrait source package for Event 006 IW-024 Banat (`AXX`). This package contains one attributed archival source master, one immutable head-and-shoulders crop, one deterministic `156x210` candidate, one nearest-neighbour review enlargement, one runtime DDS, and one portrait-specific `.gfx` definition. It does not contain an advisor, dossier, commander-small, mini, generated, or alternate runtime portrait.

## Identity and source-mode gate

- Subject: Otto Roth (6 December 1884–22 April 1956), Temesvár/Timișoara lawyer, journalist, trade unionist, and Social Democratic politician.
- Event role: historically connected male Banat regional leader candidate for an alternate 1936 AXX package. Roth was Commissioner-in-Chief of the Banat Republic from 31 October 1918 to 17 January 1919 and had been a Temesvár municipal councillor and regional Social Democratic leader.
- Classification: `grounded_identity`.
- Selected mode: `source_placeholder`.
- Final character key for parent admission: `otto_roth`.
- Generation policy: no ImageGen, ComfyUI, RunPod, repaint, face reconstruction, recolouring, enhancement, or identity substitution was used.
- Replacement state: `source_placeholder`; no styled final was requested, so `replacement_pending` does not apply.

## Attributed archival source and rights

The selected unchanged master is the Wikimedia Commons file [Dr. Otto Roth.jpg](https://commons.wikimedia.org/wiki/File:Dr._Otto_Roth.jpg), downloaded from [the original Wikimedia binary](https://upload.wikimedia.org/wikipedia/commons/f/f2/Dr._Otto_Roth.jpg) on 2026-08-06. Commons describes it as a circa-1930 portrait of Dr. Otto Roth, former Commissioner of the Banat Republic, as a Romanian lawyer, and records the source credit to an [Adevărul Timișoara article](https://adevarul.ro/locale/timisoara/povestea-republicii-banatene-forma-statala-supravietuit-patru-luni-fost-proclamata-avocat-evreu-sfarsitul-primului-razboi-mondial-1_5a1735a85ab6550cb876a032/index.html) with an unknown author.

The Commons record applies `PD-RO-photo` and `PD-1996`, labels the file `Public domain`, and reports no attribution requirement. The unchanged source is retained locally for provenance; the rights determination is the Commons record, not the Wikipedia biography. The source image is RGB `627x1026`, 89,883 bytes, and SHA-256 `c9ab09e6d7f13d002de703818b47dd5ea91ccdba4526ea23d5bb31c7698448b3`.

The source visibly includes the printed caption `AVOCAT / DR. OTTO ROTH / TIMIȘOARA`. That caption remains in the archived master as identity evidence and is excluded from the runtime crop. A role/date corroboration reference is [Otto Roth](https://en.wikipedia.org/wiki/Otto_Roth), used only to verify identity, Temesvár activity, dates, and the 1918–1919 Banat Republic office.

## Immutable crop evidence

The explicit source crop was created before any resize with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` using the decoded half-open rectangle `left=18, top=5, right=609, bottom=800`. The crop is RGB `591x795`, excludes the printed caption, and retains Roth's face, hairline, expression, collar, tie, and shoulders for the full leader canvas.

The retained crop metadata is `portrait_AXX_independence_wave_otto_roth_source_crop.json`. It records Pillow `11.1.0`, the crop-tool version/hash, normalized command, master/output hashes and dimensions, and exact decoded-pixel equality. The crop PNG is 344,504 bytes with SHA-256 `05f9c7e3f46381ebc3763704f07a4ecacb94a507f72810bfc4ab1655712bf6a1`; the master/crop RGBA equality SHA-256 is `bf7d9c46e3395ec9370f1f380eebb21adc6211c32a9b309e560cd12a2d83a81d`.

## Deterministic processing

The candidate was produced by converting the immutable crop to RGB and resizing exactly once to `156x210` with Pillow `11.1.0` and `Image.Resampling.LANCZOS`; no other pixel operation was applied. The reproducible expression was `Image.open(source_crop).convert("RGB").resize((156, 210), Image.Resampling.LANCZOS).save(candidate_png, format="PNG", optimize=False)`.

The candidate `portrait_AXX_independence_wave_otto_roth.png` is RGB `156x210`, 42,882 bytes, and SHA-256 `2269029043683f617b9dce9e604bf2139303c3a52c1686db3278b4565b672647`. The retained nearest-neighbour review enlargement `portrait_AXX_independence_wave_otto_roth_4x_nearest.png` is RGB `624x840`, 64,980 bytes, and SHA-256 `c6dfe98ded686f0d320578818ee22553a19eaa16757f28c63efc6582aa83abed`. The enlargement is review evidence only.

## DDS conversion and runtime wiring

The candidate was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using `--width 156 --height 210`.

| Surface | Stable identifier or path | Evidence |
| --- | --- | --- |
| Source master | `portrait_AXX_independence_wave_otto_roth_source.jpg` | RGB `627x1026`, 89,883 bytes, SHA-256 `c9ab09e6d7f13d002de703818b47dd5ea91ccdba4526ea23d5bb31c7698448b3` |
| Immutable source crop | `portrait_AXX_independence_wave_otto_roth_source_crop.png` | RGB `591x795`, exact crop JSON PASS, SHA-256 `05f9c7e3f46381ebc3763704f07a4ecacb94a507f72810bfc4ab1655712bf6a1` |
| Processed candidate | `portrait_AXX_independence_wave_otto_roth.png` | RGB `156x210`, SHA-256 `2269029043683f617b9dce9e604bf2139303c3a52c1686db3278b4565b672647` |
| Runtime texture | `gfx/leaders/006_independence_wave/portrait_AXX_independence_wave_otto_roth.dds` | 131,168-byte one-level BGRA DDS, SHA-256 `82e616bda81fee899f3d9a7fdfcc7557f2b487452e8591dba77319492c48f046` |
| Runtime sprite | `GFX_portrait_AXX_independence_wave_otto_roth` | `interface/006_independence_wave_iw024_banat_portraits.gfx` |

DDS header validation passed: magic `DDS `, header size `124`, declared dimensions `156x210`, pixel-format size `32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`, no mipmaps, exact length `128 + 156*210*4 = 131168`, and alpha range `255..255`. Decoding the BGRA payload back to RGBA is pixel-identical to the processed RGB candidate with opaque alpha (`c4fed05fe409c0f68c461e05e814f192e381f92455607b375b18363e95a7c237` for both decoded RGBA byte streams).

No runtime reference points into `docs/assets/portraits/`; the durable archive is evidence only.

## Review and package admission state

Producer review: PASS for male identity, attributed source, public-domain record, circa-1930 era fit, head-and-shoulders framing, caption exclusion, `156x210` country-leader canvas, no extra figures, and preservation of visible facial geometry, age, expression, hairline, collar, tie, shoulders, and source tonal structure. Canonical installed-vanilla leader references were inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the eight native `156x210` leader references.

Independent review: PASS for the unchanged master, exact crop, processed candidate, DDS decode, and canonical leader reference family at native size and at least 4x nearest-neighbour scale. This source-placeholder package does not authorize a styled final; the historical-source policy permits the unchanged source placeholder until a later user-supplied HOI4-style replacement.

Package admission: `source_attested_conditional_selectable_AXX`. The AXX package now has a central dispatch adapter, content attestation, identity-specific setup/final/cleanup path, country-owned character roster, AI profile, state-82 anchor, and flat alternate-history flag handoff. The runtime remains a source placeholder rather than a styled final, and this asset handoff does not add any advisor, dossier, small-portrait, or alternate portrait surface.

No advisor, dossier, small portrait, female portrait, ImageGen fallback, or map anchor was created. No simplification or fallback was used within the portrait scope.
