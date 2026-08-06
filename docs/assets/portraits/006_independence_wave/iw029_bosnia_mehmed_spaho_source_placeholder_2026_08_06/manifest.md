# IW-029 Bosnia — Mehmed Spaho source-placeholder portrait manifest

Date: 2026-08-06.

Asset owner: `chaosx_portrait_creator`.

Scope: grounded male historical country-leader portrait source package for Event 006 IW-029 Bosnia (`BOS`). This package contains one archival source master, one immutable head-and-shoulders crop, one deterministic `156x210` candidate, one nearest-neighbour review enlargement, and one runtime DDS. It does not contain an advisor, dossier, commander-small, mini, generated, or alternate runtime portrait.

## Identity and source-mode gate

- Subject: Mehmed Spaho (13 March 1883–29 June 1939), male Bosniak/Yugoslav politician and leader of the Yugoslav Muslim Organization.
- Event role: sourced real male Bosnia/Bosnia-and-Herzegovina officeholder for the 1936 Independence Wave period; the role is historically plausible because Spaho remained active in Yugoslav politics until his death in 1939.
- Classification: `grounded_identity`.
- Selected mode: `source_placeholder`.
- Generation policy: no ImageGen, ComfyUI, RunPod, repaint, face reconstruction, recolouring, enhancement, or identity substitution was used.
- Replacement state: `source_placeholder`; no styled final was requested, so `replacement_pending` does not apply.

## Attributed archival source

The selected master is the unchanged Wikimedia Commons file [Mehmed Spaho.jpg](https://commons.wikimedia.org/wiki/File:Mehmed_Spaho.jpg), downloaded from [the original Wikimedia binary](https://upload.wikimedia.org/wikipedia/commons/2/22/Mehmed_Spaho.jpg) on 2026-08-06 with a descriptive research user agent.

Commons records the image as a 1920s photograph of “Yugoslav Muslim politician Mehmed Spaho,” credits the scan to Josip Horvat's book *Politička povijest Hrvatske* (1989), and lists the photographer as unknown. The source page marks the underlying photograph `Public domain` under its Bosnia and Herzegovina public-domain rationale for anonymous or pre-1977 photographs under the Yugoslav Copyright Act framework; attribution is not required by the listed rights template, but the archive and scan credit are retained here.

The exact source page carries the visible caption “Dr. Mehmed Spaho,” which anchors the identity without relying on a name-only or generated likeness. A period-role corroboration is [MehmedSpahoIgnacyMosciskiJuliuszYlrych19051937.jpg](https://commons.wikimedia.org/wiki/File:MehmedSpahoIgnacyMosciskiJuliuszYlrych19051937.jpg), credited to Poland's National Digital Archive and dated 1937; its description identifies Spaho as Yugoslav Minister of Communications. The 1937 record is role/date evidence only and was not used as the runtime identity master.

The source is grayscale (`L`), 902x1424 pixels, 594,556 bytes, and SHA-256 `748f9c2848eb4d936ed0290c4d54f6b712ab15c1d5cc9114a4229723d9e149d0`.

## Immutable crop evidence

The exact source crop was created before any resize with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` and the decoded half-open rectangle `left=101, top=10, right=801, bottom=955`. The crop is 700x945 pixels, preserves the source grayscale mode, excludes the source's bottom caption, and retains the face, collar, tie, and shoulders needed for a leader portrait.

The crop JSON records `exact_source_crop_verified`, Pillow RGBA equality, the normalized command, tool version and tool hash. The master-crop and output RGBA equality hash is `e6491ca238afc57851aa8c958f33f03409e80febb0c8ae9e2096251addaa3224`, and the crop PNG SHA-256 is `0e87ed968bf0ce19c8f991b5f3862817fff221390ee5b13bf89eb0dd0fb10405`.

## Deterministic processing

The candidate was made by converting the immutable crop to RGB and resizing exactly once to `156x210` with Pillow `11.1.0` and `Image.Resampling.LANCZOS`; no other pixel operation was applied. The reproducible processing expression was `Image.open(source_crop).convert("RGB").resize((156, 210), Image.Resampling.LANCZOS).save(candidate_png, format="PNG", optimize=False)`.

The candidate PNG is `portrait_BOS_independence_wave_mehmed_spaho.png`, RGB `156x210`, 37,561 bytes, SHA-256 `deada51c3ed2049365c43464bf1f1d6373e97305520722d30561c5b30edd4aa8`.

The retained nearest-neighbour review enlargement is `portrait_BOS_independence_wave_mehmed_spaho_4x_nearest.png`, RGB `624x840`, SHA-256 `23f990219b44cba8b98e178c5d80f9f987cdd0cf0be10bdecc7459fa09a511b2`. It is review evidence only and is not a runtime consumer.

## DDS conversion and runtime wiring

The approved candidate was converted with the repository tool `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using `--width 156 --height 210`.

| Surface | Stable identifier or path | Evidence |
| --- | --- | --- |
| Source master | `portrait_BOS_independence_wave_mehmed_spaho_source.jpg` | 902x1424 `L`, SHA-256 `748f9c2848eb4d936ed0290c4d54f6b712ab15c1d5cc9114a4229723d9e149d0` |
| Immutable source crop | `portrait_BOS_independence_wave_mehmed_spaho_source_crop.png` | 700x945 `L`, exact crop JSON PASS, SHA-256 `0e87ed968bf0ce19c8f991b5f3862817fff221390ee5b13bf89eb0dd0fb10405` |
| Processed candidate | `portrait_BOS_independence_wave_mehmed_spaho.png` | 156x210 RGB, SHA-256 `deada51c3ed2049365c43464bf1f1d6373e97305520722d30561c5b30edd4aa8` |
| Runtime texture | `gfx/leaders/006_independence_wave/portrait_BOS_independence_wave_mehmed_spaho.dds` | 131,168-byte one-level BGRA DDS, SHA-256 `160e85c619ae982a1ca5a5fdf8aff48a8c0ea40247f6c90675fecfdaf048d581` |
| Runtime sprite | `GFX_portrait_BOS_independence_wave_mehmed_spaho` | `interface/006_independence_wave_iw029_bosnia_portraits.gfx` |

DDS header validation passed: magic `DDS `, header size `124`, declared dimensions `156x210`, pixel-format size `32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`, no mipmaps, exact length `128 + 156*210*4 = 131168`, and alpha range `255..255`. Decoding the BGRA payload back to RGBA is pixel-identical to the processed RGB candidate with opaque alpha.

No runtime reference points into this durable `docs/assets/portraits/` archive.

## Ownership and collision gate

The exact and variant terms `Mehmed Spaho`, `Mehmet Spaho`, `Muhamed Spaho`, `Spaho Mehmed`, `Mehmed_Spaho`, and `MehmedSpaho` were searched in the project and installed vanilla `common`, `history`, `interface`, `gfx`, `localisation`, and `events` roots on 2026-08-06. No existing Chaos Redux or vanilla character, country history, portrait, `.gfx`, leader, commander, operative, officeholder, or localisation consumer was found. The source-only package therefore introduces no cloned live roster owner; Bosnia gameplay and character creation remain outside this portrait scope.

## Review and status

Producer review: PASS for male identity, source attribution, source-era plausibility, head-and-shoulders framing, caption exclusion from the crop, `156x210` leader canvas, no extra figures, and preservation of visible facial geometry, age, expression, hairline, moustache, collar, tie, and source lighting. Canonical installed-vanilla leader references were inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the eight native `156x210` leader references.

Independent review: `PENDING_PARENT_INDEPENDENT_REVIEW`. The producer cannot self-approve the non-compensable identity/provenance gate; the parent must compare the unchanged master, exact crop, processed candidate, DDS decode, and leader reference family at native size and at least 4x nearest-neighbour scale before treating the BOS package as admitted. This pending review does not alter the produced `source_placeholder` state and does not authorize a styled final.

Asset status: `handed_off` / `source_placeholder` pending the parent-owned independent review and future BOS gameplay consumer. No simplification or fallback was used.
