# Event 014 Super-Event Action Art Finalization Handoff

Date: 2026-07-12

## Outcome

The accepted four-image Event 014 super-event action-art package is asset-complete and verified. No validation defect was found, and no artwork or runtime DDS required replacement.

- Four accepted source PNGs are present.
- Four accepted `457x328` processed PNG crops are present.
- Four runtime DDS files are present at the stable Event 014 paths.
- Every DDS is uncompressed 32-bit BGRA8 with one base image level and no additional mip surfaces.
- Every raw-decoded DDS is pixel-identical to its processed PNG.
- The decoded-DDS contact sheet contains the exact runtime pixels.
- OpenAI image-generation lineage and the two retained moderated reveal attempts are documented without inventing missing model metadata.

## Files created or finalized

- `docs/assets/014_cannibalism/static_event_art_imagegen/super_events_manifest.md`
- `docs/assets/014_cannibalism/static_event_art_imagegen/contact_sheets/super_events_final_dds_contact_sheet.png`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_super_event_action_regen_2026-07-12.md`

The contact sheet already contained the four decoded runtime images when this finalization began. Its cells were independently checked against raw BGRA-decoded DDS payloads and required no pixel change.

The following accepted artwork and runtime files were verified but not modified:

- `docs/assets/014_cannibalism/static_event_art_imagegen/source_png/super_events/`
- `docs/assets/014_cannibalism/static_event_art_imagegen/processed_png/super_events/`
- `gfx/super_events/014_cannibalism/`

No gameplay, localisation, `.gfx`, GUI, audio, specification, report/news artwork, or other asset family was touched.

## Accepted action scenes

| Stem | Accepted action at the actual crop |
| --- | --- |
| `super_event_cannibalism_reveal` | Fictional bald commander points from a period truck while attackers converge through a ruined railway square and adult civilians flee. |
| `super_event_cannibalism_world_end_ordinary` | Fictional commander directs a massed assault from a moving vehicle as a burning capital is overrun and adults flee through rubble. |
| `super_event_cannibalism_global_defeat` | Coalition soldiers break into a burning prison-fortress while prisoners escape opened cages and the remaining defense collapses. |
| `super_event_cannibalism_world_end_wendigo` | Fictional frost-transformed pack leader lunges through a blizzard breach while transformed attackers pursue fleeing adults. |

All people and commanders are fictional. No real actor or celebrity likeness is claimed. The `wendigo` stem is an internal route identifier only; no folklore, Indigenous, tribal, ceremonial, religious, or sacred motif is claimed or used as provenance.

## Exact validation proof

| Stem | Source SHA-256 | Processed PNG SHA-256 | Runtime DDS SHA-256 | Decoded RGBA pixel SHA-256 | PNG/DDS pixels |
| --- | --- | --- | --- | --- | --- |
| `super_event_cannibalism_reveal` | `d7c5cf9b89b2f8edf6f6262aba4f34817159effb973c0b26bf03ae437278a3b2` | `656b04a40b599bfec6cb495366d0bbbfb4f4dc9e58aaa7d255841f14b8b6fb20` | `b73a9e9274b411c1a637d01641a27c9aab69b05fdc25340106f3371aca760014` | `fe53d12f773022654f59c497003f437ad97a68292d5d170f0207ea8dce4bb7e0` | exact |
| `super_event_cannibalism_world_end_ordinary` | `a9e077905a0d326db90bb870f72235f382cf3897647d9af95f8d770e060a7ced` | `7891e6aea037570add6b5615e62042439e8e615bc4fdfe68a8c976fd898850f1` | `2e6ab8e3af541a75d143885f12fbefd8d3c784a9bb998d69e77c2e10d132d512` | `ee921645c4ec3470a9e871a23f575b9723743f50e64f5e7614053dce47f30498` | exact |
| `super_event_cannibalism_global_defeat` | `640584c223219e491f76e3378990c914638f7d74974c21c570001930d85352ce` | `40a3d7e4ad11c5bdbcbf608438e051c3b371e5af4e81639be4e0ff005218a746` | `61cf83f3c533b219f56345abe8f550725925dad5ca5ab92fdb0ab88f244eacd9` | `aa0ed292b86b9cefe70c38f9fc735506aa68b8d23c9d37a0073cc76742223f34` | exact |
| `super_event_cannibalism_world_end_wendigo` | `777589a73c4c9661b82511ac155ce9a4ff5d122c3d964f41e5e239a4bcefe508` | `442604cfc652eeb316114d5d4919a8ac1ec203e5d7cc66b743d5e02483e44351` | `a7f5288912ef82c1539d5ee8c83a1125afb4943bb3a31691311333f9c76214fd` | `2aba531739ed133124963d5bcb6f2fac263780cccaadc81cf01dc468a92c66d1` | exact |

Source dimensions are `1536x1024`, `1477x1065`, `1478x1064`, and `1536x1024` respectively. Every processed PNG and DDS is exactly `457x328`.

Every DDS has:

- `DDS ` magic and a 124-byte DDS header
- `457x328` dimensions
- `1828`-byte pitch
- `32` bits per pixel
- `0x00ff0000`, `0x0000ff00`, `0x000000ff`, `0xff000000` RGBA masks, giving BGRA byte order
- exactly `599584` pixel bytes and `599712` total bytes
- no DX10 extension
- no mipmap flag or extra mip payload; `dwMipMapCount = 0`, the repository converter's single-base-level representation for `MIP_LEVELS = "1"`

The processing pipeline was also replayed in memory. The documented crop centering and tonal operations reproduced all four processed PNGs pixel-for-pixel.

## Decoded-DDS contact sheet proof

- Path: `docs/assets/014_cannibalism/static_event_art_imagegen/contact_sheets/super_events_final_dds_contact_sheet.png`
- Dimensions: `986x796 RGB`
- SHA-256: `bd46c5cfe8855ee09decdc5ac6fda133ec48381466ae6671a45e46133f33f3a2`
- All four displayed image cells match the corresponding raw BGRA-decoded DDS pixels exactly.

## OpenAI provenance and moderated attempts

Accepted final output ids:

- Reveal action composition: `exec-e3615ba5-5bd4-4e3c-ac1f-20507e4d3719`
- Reveal final identity/detail edit: `exec-66301a11-cc96-433d-96c0-8f325b7de429`
- Ordinary world-end: `exec-1fe56a70-198e-4e5e-95ae-11f660406c74`
- Global defeat: `exec-e7769588-95a1-468d-a873-b1be811b8e68`
- Transformed world-end: `exec-bedf57af-30fa-42df-8d74-e3a25e16f11b`

Two reveal attempts were rejected by OpenAI output moderation in the `violence` category and produced no image:

- `exec-3074414e-4ff5-4b46-a8ae-0ca7103553db`
- `exec-fdf7e638-e661-47bc-8935-08475eff868f`

The accepted prompt retained the action composition while removing explicit anatomical-injury instructions. No retained evidence records a rejected or moderated attempt for the other three accepted assets.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Asset omissions: none.
- Fallbacks: none.
- Runtime validation defects: none.
- Evidence limitation: the retained OpenAI records do not expose an exact image-model or model-version identifier, so no model-specific claim is possible. Tool/session/call lineage and immutable output hashes are present.
- Wiring validation: intentionally outside scope. Gameplay, `.gfx`, localisation, GUI, and audio were not opened or changed for integration work.
- Commit: not created because the accepted source, processed, and runtime dependency files are part of the parent's larger uncommitted Event 014 tranche; a documentation-only subagent commit would not contain the full package it describes.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-super-events`

No skill was created or updated.
