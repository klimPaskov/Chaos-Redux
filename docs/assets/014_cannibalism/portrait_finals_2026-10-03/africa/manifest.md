# Event 014 African Warlord Portrait Candidates

Status: the eight parent-approved Africa portraits are installed at their existing runtime DDS paths; the full 56-portrait matrix and cross-region uniqueness review remain open.

## Scope and accepted basis

This tranche covers the eight African regional variants for reusable fictional slots CBA-CBH in the accepted 56-portrait matrix.

The accepted visual requirements are recorded in `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md` and `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`.

The 2026-10-03 parent continuation report accepts the fictional native-ImageGen route for CBA-CBH and retains the full 56-final requirement; the source-polity classification is fictional because these are origin-agnostic invented slots, not real polities or offices.

The current status and authority reconciliation are recorded in `docs/plans/014_cannibalism_plans/2026-10-03_continuation_report.md` and `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_spec_receipt_reconciliation.md`.

## Source mode, provenance, and rights

Portrait source mode is `fictional_high_chaos` for all eight invented leaders, produced through native ImageGen; no Internet identity research or real-person source archive applies.

Background mode is `consumer_opaque`, matching the full-canvas leader portrait consumer.

Each portrait was generated from one unique prompt through the built-in native ImageGen tool, with one narrow same-brief retry for CBE after its first output was rejected.

No input image was attached to any generation call, and no vanilla, Europe, Asia, backdrop-library, Hannibal, actor, or other third-party raster was copied or used as an identity source.

The generated-source output paths, prompt paths and hashes, response outcomes, byte-copy checks, and CBE moderation record are in `route_log/imagegen_call_log.json`.

The exact initial prompts are in `prompts/leader_CBA_warlord_africa_prompt.txt` through `prompts/leader_CBH_warlord_africa_prompt.txt`; CBE's successful retry prompt is `prompts/leader_CBE_warlord_africa_retry01_prompt.txt`.

All eight source PNGs are opaque RGB images and remain byte-identical to the native tool outputs copied into `source_png/`.

No third-party raster rights are implicated; no separate legal license claim is made for native generated output.

## References inspected

Installed vanilla Africa leader portraits `Portrait_Africa_Generic_land_1.dds`, `Portrait_Africa_Generic_land_2.dds`, and `Portrait_Africa_Generic_land_3.dds` were decoded at their native 156x210 size before generation and informed only painted leader-bust framing and tonal treatment.

The parent-approved Europe native and 4x nearest-neighbour contact sheets in `docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/review/` informed only broad brush finish, framing, and family coherence.

The parent-approved Asia native and 4x nearest-neighbour contact sheets in `docs/assets/014_cannibalism/portrait_finals_2026-10-03/asia/review/` were inspected read-only after generation solely to check cross-region uniqueness; no Asia files were edited or attached to ImageGen calls.

The skill-local `portrait_backdrops` family was not used as artwork, an identity reference, or a generation input.

## Candidate lineage and generated actions

| Slot | Candidate ID | Exact assigned action | Native generation status |
|---|---|---|---|
| CBA | `AF-CBA-NATIVE-01` | Crushes a blood-smeared military belt buckle in a clenched fist. | First native generation succeeded. |
| CBB | `AF-CBB-NATIVE-01` | Tips a cracked enamel water cup onto a raised thumb. | First native generation succeeded. |
| CBC | `AF-CBC-NATIVE-01` | Shakes a sealed greasy ration tin beside his ear, listening with manic focus. | First native generation succeeded. |
| CBD | `AF-CBD-NATIVE-01` | Tears a salvaged leather harness seam with a jagged scrap tool. | First native generation succeeded. |
| CBE | `AF-CBE-NATIVE-R01` | Counts loose cartridge cases between trembling blood-stained fingers. | First output was rejected at output safety review; retry 01 retained the same four-case action and succeeded. |
| CBF | `AF-CBF-NATIVE-01` | Furiously wipes dried red stains from one cracked binocular lens. | First native generation succeeded. |
| CBG | `AF-CBG-NATIVE-01` | Flips a battered pay token above his open palm with an unsteady grin. | First native generation succeeded. |
| CBH | `AF-CBH-NATIVE-01` | Pulls a rusted chain taut across his chest with a rigid jaw. | First native generation succeeded. |

All generated faces are separate invented adult male identities with uncovered bald scalps, human anatomy, individual facial structure, feral bloodshot expressions, painted scars and blood, and rough invented hides/raw cloth with scavenged period military pieces.

Each candidate is a root generation with no parent candidate and no image input; the reason is its own distinct accepted Africa slot and assigned action.

No portrait contains a known face, actor likeness, Hannibal likeness, supernatural anatomy, animal anatomy, sacred or living ceremonial regalia, a cultural stereotype, detention imagery, text, branding, or a watermark.

## Source, crop, and processed PNG inventory

Each lossless `*_source_crop.png` retains the complete generated frame because every ImageGen output already has a portrait aspect ratio close to 156x210; `route_log/processing_audit.json` records each full-frame crop box and exact-pixel equality.

Processing performs only a deterministic resize to 156x210 with LANCZOS; it does not recolor, repaint, filter, composite, remove the opaque background, or change alpha.

| Slot | Native source PNG dimensions; SHA-256 | Processed PNG dimensions; SHA-256 |
|---|---|---|
| CBA | 1080x1456; `573F91EC729D1E0B9C0223681348ABB9A181BA11ADE01A14DE54855EB005DB0C` | 156x210; `E365F00E7877AFF9C3EB5E1D383F0705A978A96E7158E988A99F82C45327B790` |
| CBB | 1081x1455; `5B6AA4F215CBC97AFC6D3329BE68CC2D10EB26F2007D39C13FD9E20C897AFDCE` | 156x210; `63975BF781BFE62DA7ACBB3A2809F0E20571C5B76FA7ACD41C920C114B58E507` |
| CBC | 1082x1454; `3D6115896097ABA54FF0C73B66B69FC1EF84548EE1B3EF543CB7AB098DE1428E` | 156x210; `14A3614A0BA45B079CD71FCA93F43136D542AF2029A9BA5A36CEC3DCF6914604` |
| CBD | 1082x1454; `C3C3545E2AD99238FA89E53228A44A08DF7F9B6284B1FB2CD8433F9348309959` | 156x210; `240A8E305FE96D9E1203F8A752E914EA4F91478F87E255B09E8F22F9A1181706` |
| CBE | 1081x1455; `5CAFD2F277E9A94502B0CFD3947AAE86BA09CD910067970DB40F739904658A3E` | 156x210; `36E814DAAD8606AD56DC21545B9EF60119059CE7C5055F76D5EF4418CE0D9EC3` |
| CBF | 1080x1456; `BBCAE28E94A5EC1D5EC12F3A436CB47BDE6DD63D8C0A2A4F32D33FF38A2CA1BD` | 156x210; `0B96D7990431F201316FAA5CEFBCCDA9131A8B7D1B8E55F909C16EB9BD445E16` |
| CBG | 1081x1455; `EF567FB4A97ACC8BCECF7E8B031DA4CAD01F67BE1D13F4EC8E1DE00AFF69E289` | 156x210; `58B749A15BDC73DE9BF38C603095C35A7FCBF38CFF182C2E6D214AE9C3216C7E` |
| CBH | 1081x1455; `4C8B2092C81EB81222A22400C9566C3B6F7011B54478D2545BBEDF7BFDE97914` | 156x210; `83DF9714D156BF8FD64941B66F28B0E8B86820B94327442DB1EDA3A91788C4B0` |

The two producer-reviewed source/processed contact sheets are `review/africa_native_4x2_contact_sheet.png` and `review/africa_nearest4_4x2_contact_sheet.png`; their row-major slot order is in `review/contact_sheet_order.txt`.

## Isolated DDS candidates

The eight DDS files in `candidate_dds/` were created only through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

The converter used its FFmpeg BGRA fallback because `texconv` was not available on PATH; this is the converter's own documented backend, not a separate conversion route.

All eight outputs are 156x210, 131168 bytes, uncompressed BGRA32 with one image level and opaque alpha; every decoded DDS pixel buffer exactly matches its processed PNG and all eight decoded-pixel hashes are unique.

Full DDS hashes, header fields, decoded-pixel hashes, exact-round-trip checks, and decoded review-sheet paths are in `route_log/dds_roundtrip_audit.json`.

The decoded native and 4x nearest-neighbour contact sheets are `review/africa_dds_decoded_native_4x2_contact_sheet.png` and `review/africa_dds_decoded_nearest4_4x2_contact_sheet.png`.

## Existing portrait registrations and runtime state

The stable existing Africa sprite names and DDS paths in `interface/014_cannibalism.gfx` are verified in `route_log/runtime_preservation_audit.json`.

| Slot | Existing sprite | Existing GFX line | Existing runtime path | Candidate DDS |
|---|---|---:|---|---|
| CBA | `GFX_portrait_CBA_warlord_africa` | 171 | `gfx/leaders/014_cannibalism/leader_CBA_warlord_africa.dds` | `candidate_dds/leader_CBA_warlord_africa.dds` |
| CBB | `GFX_portrait_CBB_warlord_africa` | 179 | `gfx/leaders/014_cannibalism/leader_CBB_warlord_africa.dds` | `candidate_dds/leader_CBB_warlord_africa.dds` |
| CBC | `GFX_portrait_CBC_warlord_africa` | 187 | `gfx/leaders/014_cannibalism/leader_CBC_warlord_africa.dds` | `candidate_dds/leader_CBC_warlord_africa.dds` |
| CBD | `GFX_portrait_CBD_warlord_africa` | 195 | `gfx/leaders/014_cannibalism/leader_CBD_warlord_africa.dds` | `candidate_dds/leader_CBD_warlord_africa.dds` |
| CBE | `GFX_portrait_CBE_warlord_africa` | 203 | `gfx/leaders/014_cannibalism/leader_CBE_warlord_africa.dds` | `candidate_dds/leader_CBE_warlord_africa.dds` |
| CBF | `GFX_portrait_CBF_warlord_africa` | 211 | `gfx/leaders/014_cannibalism/leader_CBF_warlord_africa.dds` | `candidate_dds/leader_CBF_warlord_africa.dds` |
| CBG | `GFX_portrait_CBG_warlord_africa` | 219 | `gfx/leaders/014_cannibalism/leader_CBG_warlord_africa.dds` | `candidate_dds/leader_CBG_warlord_africa.dds` |
| CBH | `GFX_portrait_CBH_warlord_africa` | 227 | `gfx/leaders/014_cannibalism/leader_CBH_warlord_africa.dds` | `candidate_dds/leader_CBH_warlord_africa.dds` |

No `.gfx`, character, gameplay, localisation, event, focus, decision, country, or spreadsheet file was written in this portrait install.

Parent approval is recorded in `docs/plans/014_cannibalism_plans/evidence/2026-10-03_africa_portrait_parent_review.json`; the eight approved candidate DDS files are copied byte-for-byte to their exact existing Africa runtime paths.

Only those eight Africa runtime DDS files were backed up and replaced; their original bytes are in `evidence/runtime_before/`, and their pre-install and post-install hashes are in `evidence/runtime_install_receipt.json`.

The Africa install receipt snapshots all 60 current Event 014 leader DDS files plus the portrait GFX and Event 014 character definition before and immediately after this installation; at that point, the other 52 DDS files and both definitions match the current pre-install snapshot.

The Middle East owner subsequently installed its eight parent-approved disjoint DDS files; their current bytes match `docs/assets/014_cannibalism/portrait_finals_2026-10-03/middle_east/evidence/runtime_install_receipt.json` and are attributed in `route_log/runtime_install_final_audit.json` without rollback.

That final audit snapshots the current 60 DDS files after both regional installs and verifies the remaining 44 DDS files, portrait GFX, Event 014 character definition, and Africa eight against their respective saved state or approvals.

The four protected canonical Hannibal DDS files (two static portraits and two animated sheets) remain byte-identical to the current pre-install snapshot, as recorded in `evidence/runtime_install_receipt.json`.

## Review state and event-wide remainder

The producer reviewed all eight source masters, the 156x210 and 4x nearest-neighbour sheets, the DDS-decoded sheets, and a read-only cross-region comparison with the accepted Europe and Asia sheets.

The parent approved all eight native sources and decoded DDS candidates for their bald human male faces, assigned actions, props, gestures, crops, and backgrounds within this bounded set; the approval does not complete cross-region uniqueness across all 56 slots.

Each listed candidate is the parent-approved final for its Africa slot and is installed at the existing runtime path through the unchanged sprite registration.

Each Africa asset status is `wired` through its existing GFX sprite and runtime path.

The earlier Africa/Middle East checkpoint recorded 32 installed regional portraits. The current parent inventory verifies all 56 regional installations; global art and live acceptance remain parent-owned.

Their current final-art and acceptance states were not audited in this bounded Africa install.

No full 56-portrait completion, cross-region uniqueness, legal license, or in-game acceptance claim is made by this bounded Africa package.

## Current parent matrix checkpoint

The parent selected-art inventory is `docs/plans/014_cannibalism_plans/evidence/2026-10-03_global_portrait_review/candidate_inventory.json`.
It records 56 installed candidate matches and four protected Hannibal files, independently of this package's timestamped installation snapshots.
The global visual audit accepts all 56 distinct faces/compositions, and the parent-reviewed Asia CBD paper-only correction is installed. Live acceptance remains open.
