# Event 006 IW-029 Bosnia — Mehmed Spaho portrait source-placeholder handoff

Date: 2026-08-06.

Owner: `chaosx_portrait_creator`.

Scope: grounded historical male portrait source, exact crop, deterministic leader candidate, DDS conversion, portrait-specific `.gfx`, provenance manifest, and handoff only. Bosnia gameplay, history, localisation, character definitions, event dispatch, country setup, and central package attestation were not edited.

## Result

Mehmed Spaho has a defensible attributed archival source and is suitable for a source-only placeholder. The selected source is Wikimedia Commons [File:Mehmed Spaho.jpg](https://commons.wikimedia.org/wiki/File:Mehmed_Spaho.jpg), a 1920s scan credited to Josip Horvat's *Politička povijest Hrvatske* (1989), with the underlying photograph marked Public domain under the Bosnia and Herzegovina/Yugoslav photograph-duration rationale. The source image visibly captions “Dr. Mehmed Spaho,” and Commons identifies him as a Yugoslav Muslim politician. A separate 1937 National Digital Archive of Poland photograph [record](https://commons.wikimedia.org/wiki/File:MehmedSpahoIgnacyMosciskiJuliuszYlrych19051937.jpg) identifies him as Yugoslav Minister of Communications, confirming an active 1936-period political role; that corroborating image is not used as the runtime master.

Source mode is `grounded_identity` + `source_placeholder`. No generated or fictional portrait, generic face, female source, advisor icon, commander-small portrait, mini portrait, dossier card, repaint, or RunPod operation was used. `replacement_pending` is not applicable because the user did not request a styled final.

## Changed files

- `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/portrait_BOS_independence_wave_mehmed_spaho_source.jpg` — unchanged 902x1424 grayscale archival source master, SHA-256 `748f9c2848eb4d936ed0290c4d54f6b712ab15c1d5cc9114a4229723d9e149d0`.
- `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/portrait_BOS_independence_wave_mehmed_spaho_source_crop.png` — exact 700x945 grayscale crop from `(101,10)-(801,955)`, SHA-256 `0e87ed968bf0ce19c8f991b5f3862817fff221390ee5b13bf89eb0dd0fb10405`.
- `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/portrait_BOS_independence_wave_mehmed_spaho_source_crop.json` — `exact_source_crop_verified` Pillow equality evidence and normalized command.
- `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/portrait_BOS_independence_wave_mehmed_spaho.png` — deterministic 156x210 RGB candidate, SHA-256 `deada51c3ed2049365c43464bf1f1d6373e97305520722d30561c5b30edd4aa8`.
- `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/portrait_BOS_independence_wave_mehmed_spaho_4x_nearest.png` — 624x840 nearest-neighbour review enlargement, SHA-256 `23f990219b44cba8b98e178c5d80f9f987cdd0cf0be10bdecc7459fa09a511b2`; review-only.
- `docs/assets/portraits/006_independence_wave/iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06/manifest.md` — complete source, rights, identity, crop, processing, DDS, wiring, ownership, and review record.
- `gfx/leaders/006_independence_wave/portrait_BOS_independence_wave_mehmed_spaho.dds` — one-level 156x210 BGRA runtime texture, 131,168 bytes, SHA-256 `160e85c619ae982a1ca5a5fdf8aff48a8c0ea40247f6c90675fecfdaf048d581`.
- `interface/006_independence_wave_iw029_bosnia_portraits.gfx` — portrait-specific sprite registration for `GFX_portrait_BOS_independence_wave_mehmed_spaho`.

## Processing evidence

1. The source master was downloaded unchanged from the direct Wikimedia binary and archived before processing.
2. `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` created the explicit crop with `left=101, top=10, right=801, bottom=955`; the JSON proves decoded RGBA pixel equality and preserves the source/crop hashes.
3. The crop was converted to RGB and resized once to `156x210` with Pillow `11.1.0` and `Image.Resampling.LANCZOS`; no enhancement, recolouring, retouching, or filtering was applied.
4. `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 156 --height 210` produced the runtime DDS.
5. DDS validation passed the legacy one-level BGRA contract: `DDS ` magic, 124-byte header, 156x210 dimensions, 32-bit BGRA masks, texture caps, no mipmaps, exact 131,168-byte length, opaque alpha, and pixel-identical BGRA decode against the candidate PNG.

## Portrait-specific wiring

The runtime texture path is `gfx/leaders/006_independence_wave/portrait_BOS_independence_wave_mehmed_spaho.dds`.

The sprite is `GFX_portrait_BOS_independence_wave_mehmed_spaho`.

The sprite is registered only in `interface/006_independence_wave_iw029_bosnia_portraits.gfx` and points to the runtime DDS. No central dispatcher, shared GFX file, character definition, localisation, history, or gameplay file was touched.

Copy-ready definition:

```text
spriteTypes = {
	spriteType = {
		name = "GFX_portrait_BOS_independence_wave_mehmed_spaho"
		texturefile = "gfx/leaders/006_independence_wave/portrait_BOS_independence_wave_mehmed_spaho.dds"
	}
}
```

## Ownership search

The terms `Mehmed Spaho`, `Mehmet Spaho`, `Muhamed Spaho`, `Spaho Mehmed`, `Mehmed_Spaho`, and `MehmedSpaho` were searched across project and installed-vanilla `common`, `history`, `interface`, `gfx`, `localisation`, and `events` roots on 2026-08-06. No existing character, portrait, leader, commander, operative, officeholder, or localisation consumer was found. The no-match result is recorded in the manifest; the parent remains responsible for any future BOS character ownership guard when Bosnia gameplay is implemented.

## Review state and blockers

Producer visual review: PASS. The crop is a centered male head-and-shoulders frame with the original facial geometry, moustache, age, expression, hairline, collar, tie, grayscale lighting, and visible asymmetry preserved. The source caption is excluded from the runtime crop, and there are no extra people or invented insignia.

Independent identity/framing/provenance audit: **PASS, parent review 2026-08-06**. I compared the source master, exact crop, 156x210 candidate, DDS decode, and 4x nearest-neighbour review image. The crop removes the printed caption and background margin while retaining the same male face, moustache, hairline, collar, tie, expression, and grayscale tonal structure. The decoded DDS matches the processed candidate byte-for-byte under the documented BGRA contract. The result is a valid source-placeholder portrait consumer. It remains a source placeholder rather than a styled HOI4 final, and it does not by itself admit the BOS gameplay package.

Current asset state: `handed_off`, portrait state `source_placeholder`.

No simplification, fallback, or unapproved substitute was used. The missing BOS gameplay/character consumer and central package admission remain parent scope and are intentionally not blockers to this portrait-source handoff, but they prevent any claim that IW-029 Bosnia is gameplay-complete.
