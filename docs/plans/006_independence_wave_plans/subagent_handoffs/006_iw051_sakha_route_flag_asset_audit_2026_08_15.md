# IW-051 YAK route-flag asset audit — 2026-08-15

## Disposition

`NEEDS_USER_REVIEW / BLOCKED FOR ADMISSION — asset package exists, but the current ladders must not be promoted as the accepted route flags.`

This audit inspected the existing package at `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/` without overwriting any source, processed PNG, TGA, DDS, contact sheet, manifest, or handoff. The package contains four native ImageGen source PNGs, 12 processed PNG previews, 12 package TGA copies, 12 package DDS files, 12 installed route-specific TGAs, a contact sheet, metadata, a manifest, and a GFX handoff.

The vanilla `YAK`, `YAK_democratic`, `YAK_communism`, `YAK_fascism`, and `YAK_neutrality` ladders were not modified by this audit. No `.gfx`, gameplay, central attestation, deterministic Join, localisation, character, history, or spreadsheet surface was changed.

## Independent evidence

- The four source masters are `1536x1024` and contain a red-field majority: measured red-pixel fractions are approximately `0.777` Civic, `0.775` Arctic, `0.753` Socialist, and `0.724` Emergency under a conservative red-field threshold.
- The existing `flag_validation.json` crop boxes end at the blue-canton boundary: Civic `(0,0,768,394)`, Arctic `(0,0,692,512)`, Socialist `(0,0,688,592)`, and Emergency `(0,0,768,576)`.
- Every existing processed normal PNG has `red_frac = 0.0`, and the contact sheet shows only the light-blue canton and emblem with no red field.
- All 12 package and runtime TGAs independently decode as type-2, 32-bit, bottom-origin files with the expected dimensions: normal `82x52`, medium `41x26`, and small `10x7`; normal/medium descriptors are `8`, small descriptors are `0`; package and runtime TGA bytes match per ladder.
- All 12 package DDS files have the expected `DDS ` magic, `124`-byte header, `82x52`/`41x26`/`10x7` dimensions, uncompressed BGRA masks, texture caps, exact payload lengths, and metadata-reported PNG round-trip equality.
- The current package DDS files were produced by the package-local `build_flags.py` writer rather than the repository-standard `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` converter. For the Civic normal sample, the standard converter produced the same dimensions and BGRA masks but a different header (`flags 0x100f`, row pitch `328`) from the package DDS (`flags 0x2100f`, linear-size field `17056`); this is a provenance/workflow mismatch even though the current custom files are structurally decodable.
- The package-local build script performs fixed-palette quantization before export. The event-assets flag workflow forbids aggressive palette quantization that reduces generated heraldic detail, so this processing route requires parent review before acceptance.

## Remaining blockers

1. The crop boxes are not safe. They remove the generated red field and turn the route flags into canton-only designs, contradicting the requested red-field/light-blue-hoist motif family and the manifest's route identity claims.
2. The package does not retain the native ImageGen prompt text. `manifest.md`, `gfx_handoff.md`, and `generation_evidence.json` correctly record this as `prompt_archive: not present`; the missing prompt archive remains a provenance gap and must stay `needs_user_review`.
3. The DDS evidence must be regenerated with the repository-standard converter, or the parent must explicitly approve the custom writer after confirming its header convention against the current converter. The existing DDS files were not replaced during this audit.
4. The fixed-palette processing in `build_flags.py` should not be treated as accepted final processing until the parent reviews the detail loss visible in the medium and small contact-sheet columns.
5. Final admission remains separately blocked by the unresolved IW-051 identity/rights and parent-owned central admission gates documented in `006_iw051_sakha_flag_symbol_provenance_2026_08_15.md` and `006_iw051_yak_authority_reconciliation_2026_08_15.md`.

## Safe next action

The asset owner should regenerate a review candidate from each full source master using a crop that retains the complete red field and blue hoist canton, then create normal/medium/small PNGs and TGAs without aggressive palette quantization. The DDS files should be produced by `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, with fresh header and decoded-pixel evidence. The corrected contact sheet must include each full source master, selected crop, normal, medium, and small output.

Until that correction and review occur, retain the existing package and route-specific TGAs as provisional evidence only, keep all four routes marked `needs_user_review`, and do not widen central Event 006 admission or Join wiring from this package.

## Files reviewed

- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/manifest.md`
- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/gfx_handoff.md`
- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/build_flags.py`
- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/metadata/flag_validation.json`
- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/metadata/dds_validation.json`
- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/metadata/generation_evidence.json`
- `docs/assets/006_independence_wave/iw051_sakha_flags_2026_08_15/contact_sheets/iw051_sakha_flag_ladders_contact_sheet.png`
- Four source masters, 12 processed PNGs, 12 package TGAs, 12 package DDS files, and 12 installed route-specific TGAs under the package and `gfx/flags/{,medium,small}/`.

No runtime or gameplay files were edited by this audit.
