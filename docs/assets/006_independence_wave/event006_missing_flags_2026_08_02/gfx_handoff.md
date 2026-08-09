# Event 006 missing base flags handoff

Flags use HOI4's engine filename lookup and do not require `.gfx` sprite definitions. The main agent should keep the existing country tag and ideology lookup unchanged; these files supply the missing democratic/base ladder.

## Runtime ladder

Each accepted tag below has all three exact runtime files:

```text
gfx/flags/<TAG>.tga          # 82x52 normal
gfx/flags/medium/<TAG>.tga   # 41x26 medium
gfx/flags/small/<TAG>.tga    # 10x7 small
```

Runtime ladders currently present in this tranche: `AKX ATX AXX BAX BBX BFX BHX BJX BKX BWX CIX CJX CKX CLX`; AXX is handed off as a parent-accepted alternate-history civic synthesis, while BBX uses the historically attested 1914 Northern Epirus geometry.

## AXX review state

`AXX` has a replacement flat candidate in the runtime ladder. Banat has no cited attested flag geometry for this synthesis, so the parent accepted it only as an explicitly alternate-history civic design; it must not be described as a historical Banat flag. The rejected illustrated-shield source remains at `source_png/AXX_banat_imagegen_raw.png` for comparison, and the replacement evidence is `contact_sheets/AXX_banat_replacement_contact_sheet.png`.

### AXX replacement details

- Source mode: native ImageGen flat graphic, using the Banat regional reference [Banat](https://en.wikipedia.org/wiki/Banat) for the documented red/white/blue palette and lion/river motif only.
- Classification: alternate-history civic synthesis; no attested Banat flag adoption or exact historical geometry is claimed.
- Replacement source: `source_png/AXX_banat_imagegen_flat_raw.png` (SHA-256 `59bbcc5851e7435a37e0e107f5ffc8057a88f84721a4bbff3567cf97810d4de6`).
- Rejected source retained: `source_png/AXX_banat_imagegen_raw.png` (SHA-256 `f71260b9ed1f0710afe213f2f6a47898bde1a990d70b64fb68ccafb1d59cc75c`), rejected for its illustrated shield and detailed castle/lion artwork.
- Prompt: `prompts/AXX_flag_imagegen_prompt.txt` (SHA-256 `ed2fb6a28ac777f6f8d051e38373d6fc4c1ba010b4f955772a2992923300d533`).
- Processed master: `processed_png/AXX_flat_master_820x520.png` (SHA-256 `3b6606ff1c4fb9993fb5f37ffca9fe040d96520e8a47d7c88ee9f2841697139a`).
- Runtime ladder: `gfx/flags/AXX.tga` (82x52, SHA-256 `55b1dbc417cf1a5d14f45a6f1537c56baa3e6c192ce586e6c9b392db2b4e02cb`), `gfx/flags/medium/AXX.tga` (41x26, SHA-256 `58ea23655f8d5a14ebe85d700aab3d7e1a02658ab2b09282eb14e9f41ded2c1a`), and `gfx/flags/small/AXX.tga` (10x7, SHA-256 `aaf2541128fe25dce539875795100a4384d5c805562332f02df4be5891fffde8`). Package copies are in `final_tga/` with matching hashes.
- QA: all three TGAs are uncompressed 32-bit type-2 bottom-left-origin (`descriptor = 8`), exact lengths 17074/4282/298 bytes, and decode pixel-identical to their processed PNGs; the replacement contact sheet shows old rejected source, new source, master, and all three exports.
- Main-agent wiring: no `.gfx` sprite is required; keep normal HOI4 tag lookup filenames. AXX is accepted for the IW-024 alternate-history route with the historical-geometry limitation above.

## BBX review state

`BBX` uses a flat ImageGen reconstruction of the public-domain 1914 Northern Epirus flag rather than the former blue-eagle synthesis. Its archived references are a surviving flag photograph, a period stamp, and a clean public-domain reconstruction. The generated source was flattened to exactly three design colours before export; it contains no fabric, lighting, gradient, border, lettering, or painterly flag artwork. The base and all four ideology lookup variants use the same historical design.

- ImageGen source: `source_png/BBX_epirus_historical_imagegen_raw.png` (SHA-256 `6e277fdd5d2d69a11b4eb5c73e2e8dd40beefce5686b714dd0f635c93cfe6f2a`).
- Processed flat master: `processed_png/BBX_flat_master_820x520.png` (SHA-256 `ab9cdadf08267f7f93d4bf6601b2a0850fc8a264eca93a8822a6fa387fb4df8f`).
- Runtime ladder: normal SHA-256 `c7dc18e5804be779a84526ad98e44a32ee567662c0ed4f98793a0f09ef75b8f1`, medium SHA-256 `abd3433d7281567179cdb1b1dd9e36b852bd8d9564b1f9814679994c8195f3e4`, and small SHA-256 `255ad2a4cdf4e7b9d50a47b19c78cbb283a38c49ea26c3bb6fbe1967eb82afa3`.
- QA: the runtime files are uncompressed 32-bit type-2 bottom-left-origin TGAs at 82x52, 41x26, and 10x7. The package copies under `final_tga/` match the runtime hashes.

The package manifest and machine-readable validation record are at:

- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md`
- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/metadata/flag_validation.json`
- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/metadata/hashes.sha256`

All 14 ladders are bottom-origin, uncompressed 32-bit TGA files (`descriptor = 8`) and were decoded back against their processed PNGs. The source masters, design references, prompts, and comparison sheets remain in the package for review.

## Deliberately blocked reservations

The 17 reservation tags are documented in `blockers.md`; no runtime files were created for them. Do not fill those paths until the parent accepts a concrete polity identity and defensible flag design.
