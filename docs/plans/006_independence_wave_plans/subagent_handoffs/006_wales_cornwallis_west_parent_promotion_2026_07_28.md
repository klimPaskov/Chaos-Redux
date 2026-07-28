# IW-002 Wales Cornwallis-West parent promotion

Date: 2026-07-28.

Parent-owned integration after the independent visual/provenance audit in `006_wales_two_role_retry04_visual_audit_2026_07_28.md`.

## Promoted surface

Major George Frederick Myddleton Cornwallis-West is the approved real male source for the existing WLS mountain-commandant character and sprite. The audit passes likeness, HOI4 commander style, source/crop provenance, role fit, and artifact checks. The source remains a Welsh-born Scots Guards officer; this package does not claim specialist Welsh mountain service.

| Surface | Path / identifier | Evidence |
| --- | --- | --- |
| Original-size shelf master | `docs/assets/006_independence_wave/portraits_generated_png/WLS_george_cornwallis_west_identity_preserve_retry_04.png` | Byte-identical to package raw ImageGen output; RGB `1122x1402`; SHA-256 `23f39f714510df4707d81677ed549420e1d9687a70270c946396e1e6b45bf9c0`. The shelf is flat and contains no normalized PNG. |
| Processed candidate | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wales_two_role_retry_04/processed_png/WLS_george_cornwallis_west_identity_preserve_retry_04_156x210.png` | RGBA `156x210`; SHA-256 `9b58faa2262f3182f0e89ac3d8985effd1f76864eb63b25edb498ed7f8a6d04d`; processor v5.0, commander role family. |
| Sprite | `GFX_portrait_WLS_independence_wave_mountain_commandant` | Existing definition in `interface/006_independence_wave_region_01_portraits.gfx`; unchanged identifier and path. |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | Legacy one-level BGRA, `156x210`, 131,168 bytes, opaque alpha, SHA-256 `63e974a6d95117e3c37efca01884a3bdfec1da190b25617164ad177934c0cd94`; header and pixel-format checks pass. |
| Player-facing name | `WLS_independence_wave_mountain_commandant` | Localised as `Major George Frederick Myddleton Cornwallis-West`; descriptor records Welsh-born Scots Guards service and the emergency mountain-directorate role. |

## Explicit non-promotion

David Rhys Grenfell retry 04 and retry 05 remain `NEEDS_REVIEW` for likeness. Their original-size raw masters are retained in the flat shelf as user-requested evidence copies, but neither candidate is converted, wired, or used to replace the current WLS national-council portrait. No advisor icon, dossier card, high-command derivative, or `_small` asset was created for this Event 006 tranche.

## Validation

- Independent audit compared archival master, exact crop, raw repaint, processed candidate, and commander references at native and enlarged scale.
- The flat shelf now has 54 root-level PNG masters, zero child directories, and zero normalized `156x210` PNGs.
- DDS header checks confirm `DDS ` magic, 124-byte header, 32-bit BGRA masks, texture caps, exact length, declared `156x210` dimensions, and alpha range `255..255`.
- No country tag, state, history, character token, or sprite identifier was added or renamed.

The Commons PD-Art jurisdiction caution for the Barnett source remains recorded in the independent audit and package provenance; this promotion does not broaden the rights claim.
