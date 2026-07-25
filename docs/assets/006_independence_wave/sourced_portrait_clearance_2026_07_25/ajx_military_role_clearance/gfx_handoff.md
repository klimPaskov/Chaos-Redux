# AJX military-role source-only GFX handoff

This handoff contains no `.gfx` edit, DDS, runtime texture, or localisation change.

## Source-ready candidate

Consumer: `AJX_karl_becker`.

Grounded identity: Friedrich von Rabenau (1884–1945), German Army Generalleutnant.

Use the exact crop at `source_crops/friedrich_von_rabenau_1937_c05190_head_shoulders.png` only after the parent accepts the broader German military-role fit and completes the required source-locked identity-preserving portrait pipeline and independent audit.

The existing stable sprite token is `GFX_portrait_AJX_karl_becker`; this package authorizes no new token and does not alter the existing declaration in `interface/006_independence_wave_region_01_portraits.gfx`.

Suggested eventual texture destination, subject to parent approval and the existing runtime path, is `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`. Do not create or overwrite that DDS from this source-only package.

Source: [Bundesarchiv Bild 183-C05190, Friedrich v. Rabenau](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-C05190,_Friedrich_v._Rabenau.jpg).

Required attribution: `Bundesarchiv, Bild 183-C05190 / Foto: Dorneth / CC BY-SA 3.0 DE`.

## Alternate (review only)

`source_masters/friedrich_von_rabenau_1937_dorneth_c05192.jpg` is an attributed April 1937 uniform photograph of the same subject. It is not the primary crop because the visor obscures the hairline and deepens the eye shadow. Compare both masters in `contact_sheets/ajx_friedrich_von_rabenau_source_candidates.png`.

## Parent decision boundary

The candidate is a broad German Army identity, not a Saarbrücken-specific commander. If that identity boundary is not accepted for `AJX_karl_becker`, mark the consumer blocked and do not substitute a generated face, generic German officer, postwar courtroom image, or unattributed uniform photograph.

The full provenance, era-fit, ownership, crop coordinates, hashes, and uncertainty record is `manifest.md` and `manifest.json`.
