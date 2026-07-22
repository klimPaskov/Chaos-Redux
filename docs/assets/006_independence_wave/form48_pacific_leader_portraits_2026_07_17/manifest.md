# Event 006 FORM-48 Pacific individual-leader portrait manifest

> **Superseded source mode (2026-07-22):** California and Micronesia are
> grounded polities. Their generated officeholders remain provenance and
> consumer evidence only; sourced real male replacements are required before
> IW-184 or IW-179 can regain visual readiness.

## Production contract

- Asset family: `ASSET-045`, country-leader portraits.
- Country-package requirements: `IW-184` California and `IW-179` Micronesia.
- Scope: exactly two fictional adult-male, individual, large country-leader
  portraits at `156x210`; no group/council scene and no adviser asset.
- Source mode: official built-in ImageGen with canonical vanilla large-leader
  style references.
- Status: final, installed, validated, independently approved, and handed off.

| Requirement | Character | Stable sprite | Runtime DDS | Status |
|---|---|---|---|---|
| `IW-184` | Daniel Mercer, fictional adult male California Civic Convention chair | `GFX_portrait_HBX_independence_wave_civic_convention` | `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds` | final and live |
| `IW-179` | Elias Kihleng, fictional adult male Pohnpeian Inter-Island Congress chair | `GFX_portrait_FSM_independence_wave_inter_island_congress_chair` | `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds` | final and live |

## Artifact crosswalk and hashes

| Subject | ImageGen source SHA-256 | Approved PNG SHA-256 | Runtime/retained DDS SHA-256 |
|---|---|---|---|
| Daniel Mercer | `b15b5dff29a9ac5a746183be8f05a7f6a6841f48f6fe6ded6c58cb66e53ca4b1` | `40fc48f166fdccb3b2777ecbcf402ed487d043366d80e5ff55382f78cd0c0242` | `7cd86794c10c9621f90340490e2d57b72edd01b6c785240db943fe9253af145e` |
| Elias Kihleng | `9bb42598ddca666a9f5bdedf5ccafcf5bb1d6a12c9a0f93bf894bf7188e7d52c` | `0ab2385c51562af1557bf3839dbe3fedcf9f5bc19a1a76564709fe997cc68310` | `64db23c13f8f3f488079ea24ca4d8ef9326bbb3fd9abbc94ee9b9251b004ae29` |

For each row, `source_png/` retains the official ImageGen master,
`processed_png/` retains the approved `156x210` PNG, `final_dds/` retains the
handoff DDS, and `dds_decoded_png/` contains a decode of the actual retained DDS.
The runtime copy is byte-identical to the retained DDS.

## Processing and conversion

The canonical portrait processor
`.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
version `5.0` (render version `2.0`, SHA-256
`e248979f21784c016e69c5458b9925c32177d6af29f2cca1a82bfaaffbe1f23c`)
ran in `leader` mode under Python `3.9.12` and Pillow `11.1.0`.

- Daniel crop: `(0, 0, 1081, 1455)`.
- Elias crop: `(0, 1, 1080, 1455)`.
- Composition contract: crop, grade, and export only; no programmatically drawn
  person, emblem, or scene.

The canonical `convert_to_dds.py` (SHA-256
`d8aa0ba6a16ba8b6b698ccd6cf599b90e81db6f6c6132009f07115c728f6b8a0`)
used its built-in FFmpeg BGRA writer backend. Both results are one-level,
uncompressed legacy 32-bit BGRA DDS files, exactly `131168` bytes, with a
`124`-byte DDS header, `156x210` dimensions, `32` bits per pixel, and the exact
BGRA/alpha masks recorded in `notes/validation.json`. Decoding each DDS produces
pixels identical to its approved PNG. This backend choice did not substitute or
simplify the art; the file-header and decoded-pixel contracts are exact.

## Independent approval authority

The separate approval record is `notes/visual_review.md`. Parent reviewer
`/root` approved the exact processed PNG and review-sheet hashes on 2026-07-17
after native-size and enlarged reference-family comparison. The approved review
sheet hashes are:

- Daniel: `4dc693f5291b439510ab287d75628e248e356a382a7d72726d9d4c7583703f50`;
- Elias: `d3f81fe9b994a78d25cfb9d79d417544dfab06e096864851b83ed13d611e5560`.

The approval confirms two single adult men, native-size face readability,
distinct identities, HOI4 large-leader framing and tonal treatment, and the
absence of women, additional people, group/council imagery, text, adviser
framing, or modern props.

## Protected portrait guards

This package did not edit the user-approved historical portraits. The evidence
builder verifies them on every run:

| Protected runtime file | Expected and actual SHA-256 |
|---|---|
| `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b` |
| `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2` |

## Provenance and rights

The exact prompts are retained in `prompts/imagegen_prompts.md`. Reference
provenance, installed vanilla source mappings, hashes, and the internal-review-
only rights boundary are in `notes/reference_provenance.md`. The generated
masters depict original fictional people and contain no copied or reconstructed
historical identity. Canonical vanilla review images remain internal style
references and are not runtime assets.

## Wiring boundary

`gfx_handoff.md` records the exact sprite and consumer contract. The parent-owned
`interface/006_independence_wave_pacific_portraits.gfx` and
`common/characters/006_independence_wave_pacific_characters.txt` already use the
stable identifiers. This asset lane did not edit gameplay, localisation, or
interface files.

No `65x67` adviser card, small portrait, adviser role, adviser sprite, or adviser
runtime texture was created. The two earlier group/council concepts were rejected
after the individual-male requirement was clarified and are absent from the
package and runtime.

## Evidence inventory

- `notes/validation.json`: structured header, byte-identity, decode, pixel-equality,
  independent-approval, and protected-file validation.
- `contact_sheets/006_form48_pacific_individual_leader_portraits.png`: source crop
  and approved native pixel comparison.
- `review_sheets/`: processor-native reference-family review sheets.
- `metadata/`: normalized processor records and artifact integrity.
- `hashes.sha256`: SHA-256 inventory for every retained package file except the
  inventory itself.

## Simplifications, omissions, and blockers

None within the requested two-portrait asset scope. Both exact leaders are
generated, processed, independently approved, converted, installed, registered,
consumed, documented, and validated. No fallback person, group image, emblem,
advisor asset, placeholder, or protected-portrait overwrite was used.
