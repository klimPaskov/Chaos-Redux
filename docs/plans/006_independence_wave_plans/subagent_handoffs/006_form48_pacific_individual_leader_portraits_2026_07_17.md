# Event 006 FORM-48 Pacific individual-leader portrait handoff

## Outcome

The ASSET-045 portrait lane is complete for IW-184 California and IW-179
Micronesia. Exactly two distinct fictional adult-male country-leader portraits
were generated with official ImageGen, processed at the canonical `156x210`
large-leader size, independently approved, converted to legacy BGRA DDS,
installed at their stable runtime paths, and matched to the live parent-owned
sprite and character consumers. No adviser asset was made.

Producer: `/root/form48_leader_portraits`  
Independent reviewer/approver: `/root`  
Approval date: 2026-07-17

## Delivered assets and exact hashes

| Requirement | Character | Source PNG SHA-256 | Approved processed PNG SHA-256 | Runtime DDS SHA-256 |
|---|---|---|---|---|
| `IW-184` | Daniel Mercer, adult male California Civic Convention chair | `b15b5dff29a9ac5a746183be8f05a7f6a6841f48f6fe6ded6c58cb66e53ca4b1` | `40fc48f166fdccb3b2777ecbcf402ed487d043366d80e5ff55382f78cd0c0242` | `7cd86794c10c9621f90340490e2d57b72edd01b6c785240db943fe9253af145e` |
| `IW-179` | Elias Kihleng, adult male Pohnpeian Inter-Island Congress chair | `9bb42598ddca666a9f5bdedf5ccafcf5bb1d6a12c9a0f93bf894bf7188e7d52c` | `0ab2385c51562af1557bf3839dbe3fedcf9f5bc19a1a76564709fe997cc68310` | `64db23c13f8f3f488079ea24ca4d8ef9326bbb3fd9abbc94ee9b9251b004ae29` |

Runtime paths:

- `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds`;
- `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds`.

Both are exactly `131168` bytes and are byte-identical to their retained package
copies.

## Independent review and approval

This is the approval authority for conversion and handoff. Reviewer `/root`
reviewed the exact processed candidates against the skill-local canonical
eight-leader reference family.

| Candidate | Approved PNG SHA-256 | Review-sheet SHA-256 | Native-size verdict | Enlarged/style verdict |
|---|---|---|---|---|
| Daniel Mercer | `40fc48f166fdccb3b2777ecbcf402ed487d043366d80e5ff55382f78cd0c0242` | `4dc693f5291b439510ab287d75628e248e356a382a7d72726d9d4c7583703f50` | face, shoulders, grey-streaked hair, narrow moustache, and tired civic-lawyer expression remain distinct and readable at `156x210` | at processor review scale and the package's `1.5x` nearest view, value range, facial edges, subdued civilian clothing, and quiet painted interior fit the vanilla large-leader family |
| Elias Kihleng | `0ab2385c51562af1557bf3839dbe3fedcf9f5bc19a1a76564709fe997cc68310` | `d3f81fe9b994a78d25cfb9d79d417544dfab06e096864851b83ed13d611e5560` | adult Micronesian identity, face, shoulders, composed expression, and tropical civilian clothing remain distinct and readable at `156x210` | at processor review scale and the package's `1.5x` nearest view, value range, facial edges, subdued civilian clothing, and quiet painted interior fit the vanilla large-leader family without reading as a generic European reuse |

The reviewer found exactly one adult man in each image and no women, additional
people, group/council imagery, text, advisor framing, modern props, or identity
reuse. The full verbatim review and hash-locked authority are in
`docs/assets/006_independence_wave/form48_pacific_leader_portraits_2026_07_17/notes/visual_review.md`.

## Protected portrait guards

The evidence builder verified the protected runtime portraits before closeout:

- BAY Rupprecht:
  `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`;
- RHI Josef Friedrich Matthes:
  `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`.

Expected and actual hashes match. Neither file was edited or overwritten.

## Wiring confirmation

- `interface/006_independence_wave_pacific_portraits.gfx` already registers the
  two exact stable sprites.
- `common/characters/006_independence_wave_pacific_characters.txt` already uses
  them as the `civilian.large` portraits and declares both characters male.
- Localisation already names the characters Daniel Mercer and Elias Kihleng.
- This subagent made no gameplay, localisation, interface, or registry edit.

No adviser assets or sprites were created: no adviser role, `65x67` dossier,
small portrait, advisor `spriteType`, or advisor DDS exists in this deliverable.

## Evidence and validation

Authoritative package:
`docs/assets/006_independence_wave/form48_pacific_leader_portraits_2026_07_17/`.

- `manifest.md`: complete crosswalk, provenance, tooling, hashes, and scope.
- `prompts/imagegen_prompts.md`: exact official ImageGen prompts.
- `notes/visual_review.md`: separate parent approval record.
- `notes/reference_provenance.md`: vanilla reference mapping and rights boundary.
- `notes/validation.json`: DDS header, retained/runtime byte identity, decoded
  pixel equality, approval hashes, and protected-file guards.
- `hashes.sha256`: full retained-package checksum inventory.
- `gfx_handoff.md`: exact sprite/texture/character contract.

The final evidence run decoded the actual DDS files and found each pixel-equal to
its approved PNG. It also confirmed the required legacy BGRA header, exact
dimensions, and one-level file size.

## Simplifications, omissions, blockers, and risks

None within the requested portrait scope. Earlier group/council concepts were
rejected after the requirement was clarified and never entered the repository or
runtime. The delivered assets are the required individual male leaders, not
fallback figures or institutional substitutes.
