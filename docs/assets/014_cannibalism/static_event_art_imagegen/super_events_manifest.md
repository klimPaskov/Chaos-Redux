# Event 014 Cannibalism Super-Event Action Art Manifest

Date: 2026-07-12

## Scope and authority

This manifest is authoritative only for these four accepted Event 014 super-event assets:

- `super_event_cannibalism_reveal`
- `super_event_cannibalism_world_end_ordinary`
- `super_event_cannibalism_global_defeat`
- `super_event_cannibalism_world_end_wendigo`

The parent visually accepted the actual `457x328` processed crops before this finalization pass. No source artwork, crop, tonal processing, or runtime DDS was regenerated or altered during finalization.

The super-event entries in `prompts/final_source_prompts.md` describe the superseded 2026-07-11 images and hashes. They are not provenance for the accepted 2026-07-12 action replacements. This scoped manifest supersedes those four entries only; the report and news entries remain outside this manifest.

## Source mode and provenance boundary

- Source mode: OpenAI image generation through the Codex built-in `$imagegen` / `image_gen.imagegen` tool.
- Generation session: `019f55fd-99b2-7a50-b6db-756c091e40d6`.
- Accepted generation date: 2026-07-12.
- The final packaged source files are byte-identical copies of the retained OpenAI image-generation outputs listed below.
- The retained `image_generation_end` records contain call ids, revised prompts, status, output paths, and result data. They do not contain an exact image-model or model-version identifier, so none is claimed here.
- All depicted people and commanders are fictional. No real actor, celebrity, archival person, or real victim is claimed as a source or likeness.
- `wendigo` is an internal route and filename identifier only. No Wendigo folklore iconography, Indigenous or tribal motif, ceremonial regalia, religious symbol, or sacred motif is claimed as source material. The accepted prompt explicitly excluded those elements.

## Processing record

The accepted source files were cover-cropped with Pillow `ImageOps.fit` using Lanczos resampling, then processed with `autocontrast(cutoff=1)`, contrast `1.04`, brightness `0.98`, and sharpness `1.04`.

- Reveal centering: `(0.50, 0.50)`
- Ordinary world-end centering: `(0.50, 0.50)`
- Global defeat centering: `(0.58, 0.50)`
- Transformed world-end centering: `(0.50, 0.50)`

An in-memory replay of that pipeline reproduced every processed PNG pixel exactly.

Runtime DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, whose contract is `BGRA` / `B8G8R8A8_UNORM` with `MIP_LEVELS = "1"`.

## Accepted assets

### `super_event_cannibalism_reveal`

- Action scene: a fictional bald commander points from the running board of a period truck while distinct attackers converge through a shattered railway square and adult civilians flee across blood-stained cobbles.
- OpenAI lineage:
  - accepted action composition: `C:/Users/klimp/.codex/generated_images/019f55fd-99b2-7a50-b6db-756c091e40d6/exec-e3615ba5-5bd4-4e3c-ac1f-20507e4d3719.png`
  - accepted final identity/detail edit: `C:/Users/klimp/.codex/generated_images/019f55fd-99b2-7a50-b6db-756c091e40d6/exec-66301a11-cc96-433d-96c0-8f325b7de429.png`
  - final call completed: `2026-07-12T11:38:09.175Z`
- Source PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/source_png/super_events/super_event_cannibalism_reveal_source.png`
  - dimensions and mode: `1536x1024 RGB`
  - SHA-256: `d7c5cf9b89b2f8edf6f6262aba4f34817159effb973c0b26bf03ae437278a3b2`
- Processed PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/processed_png/super_events/super_event_cannibalism_reveal.png`
  - dimensions and mode: `457x328 RGB`
  - SHA-256: `656b04a40b599bfec6cb495366d0bbbfb4f4dc9e58aaa7d255841f14b8b6fb20`
- Runtime DDS: `gfx/super_events/014_cannibalism/super_event_cannibalism_reveal.dds`
  - dimensions and format: `457x328 BGRA8`, one base image level, `599712` bytes
  - SHA-256: `b73a9e9274b411c1a637d01641a27c9aab69b05fdc25340106f3371aca760014`
  - decoded RGBA pixel SHA-256: `fe53d12f773022654f59c497003f437ad97a68292d5d170f0207ea8dce4bb7e0`
  - decoded pixels equal processed PNG: `yes`
- Status: `complete`

### `super_event_cannibalism_world_end_ordinary`

- Action scene: a fictional commander directs a massed attack from a moving period vehicle as attackers overrun a burning capital boulevard and defenders and adult civilians flee through rubble.
- OpenAI output: `C:/Users/klimp/.codex/generated_images/019f55fd-99b2-7a50-b6db-756c091e40d6/exec-1fe56a70-198e-4e5e-95ae-11f660406c74.png`
- Generation completed: `2026-07-12T11:29:14.335Z`
- Source PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/source_png/super_events/super_event_cannibalism_world_end_ordinary_source.png`
  - dimensions and mode: `1477x1065 RGB`
  - SHA-256: `a9e077905a0d326db90bb870f72235f382cf3897647d9af95f8d770e060a7ced`
- Processed PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/processed_png/super_events/super_event_cannibalism_world_end_ordinary.png`
  - dimensions and mode: `457x328 RGB`
  - SHA-256: `7891e6aea037570add6b5615e62042439e8e615bc4fdfe68a8c976fd898850f1`
- Runtime DDS: `gfx/super_events/014_cannibalism/super_event_cannibalism_world_end_ordinary.dds`
  - dimensions and format: `457x328 BGRA8`, one base image level, `599712` bytes
  - SHA-256: `2e6ab8e3af541a75d143885f12fbefd8d3c784a9bb998d69e77c2e10d132d512`
  - decoded RGBA pixel SHA-256: `ee921645c4ec3470a9e871a23f575b9723743f50e64f5e7614053dce47f30498`
  - decoded pixels equal processed PNG: `yes`
- Status: `complete`

### `super_event_cannibalism_global_defeat`

- Action scene: symbol-free coalition soldiers break into a burning prison-fortress while adult prisoners run from opened cages and the remaining defenders collapse under the breakthrough.
- OpenAI output: `C:/Users/klimp/.codex/generated_images/019f55fd-99b2-7a50-b6db-756c091e40d6/exec-e7769588-95a1-468d-a873-b1be811b8e68.png`
- Generation completed: `2026-07-12T11:36:30.487Z`
- Source PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/source_png/super_events/super_event_cannibalism_global_defeat_source.png`
  - dimensions and mode: `1478x1064 RGB`
  - SHA-256: `640584c223219e491f76e3378990c914638f7d74974c21c570001930d85352ce`
- Processed PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/processed_png/super_events/super_event_cannibalism_global_defeat.png`
  - dimensions and mode: `457x328 RGB`
  - SHA-256: `40a3d7e4ad11c5bdbcbf608438e051c3b371e5af4e81639be4e0ff005218a746`
- Runtime DDS: `gfx/super_events/014_cannibalism/super_event_cannibalism_global_defeat.dds`
  - dimensions and format: `457x328 BGRA8`, one base image level, `599712` bytes
  - SHA-256: `61cf83f3c533b219f56345abe8f550725925dad5ca5ab92fdb0ab88f244eacd9`
  - decoded RGBA pixel SHA-256: `aa0ed292b86b9cefe70c38f9fc735506aa68b8d23c9d37a0073cc76742223f34`
  - decoded pixels equal processed PNG: `yes`
- Status: `complete`

### `super_event_cannibalism_world_end_wendigo`

- Action scene: a fictional frost-transformed pack leader lunges through a shattered barricade in a blizzard while other transformed attackers vault wrecked vehicles and pursue fleeing adults.
- OpenAI output: `C:/Users/klimp/.codex/generated_images/019f55fd-99b2-7a50-b6db-756c091e40d6/exec-bedf57af-30fa-42df-8d74-e3a25e16f11b.png`
- Generation completed: `2026-07-12T11:41:12.901Z`
- Source PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/source_png/super_events/super_event_cannibalism_world_end_wendigo_source.png`
  - dimensions and mode: `1536x1024 RGB`
  - SHA-256: `777589a73c4c9661b82511ac155ce9a4ff5d122c3d964f41e5e239a4bcefe508`
- Processed PNG: `docs/assets/014_cannibalism/static_event_art_imagegen/processed_png/super_events/super_event_cannibalism_world_end_wendigo.png`
  - dimensions and mode: `457x328 RGB`
  - SHA-256: `442604cfc652eeb316114d5d4919a8ac1ec203e5d7cc66b743d5e02483e44351`
- Runtime DDS: `gfx/super_events/014_cannibalism/super_event_cannibalism_world_end_wendigo.dds`
  - dimensions and format: `457x328 BGRA8`, one base image level, `599712` bytes
  - SHA-256: `a7f5288912ef82c1539d5ee8c83a1125afb4943bb3a31691311333f9c76214fd`
  - decoded RGBA pixel SHA-256: `2aba531739ed133124963d5bcb6f2fac263780cccaadc81cf01dc468a92c66d1`
  - decoded pixels equal processed PNG: `yes`
- Status: `complete`

## DDS contract proof

All four runtime files have the same structural contract:

- DDS magic: `DDS `
- DDS header size: `124`
- dimensions: `457x328`
- pitch: `1828` bytes
- pixel-format flags: `0x41` (`RGB | ALPHAPIXELS`)
- FourCC: `0` (uncompressed, no DX10 extension)
- bit count: `32`
- red mask: `0x00ff0000`
- green mask: `0x0000ff00`
- blue mask: `0x000000ff`
- alpha mask: `0xff000000`
- caps: `0x1000` (`DDSCAPS_TEXTURE`)
- base-level pixel payload: exactly `457 * 328 * 4 = 599584` bytes
- total file size: exactly `128 + 599584 = 599712` bytes
- no mipmap-count flag, no additional mip payload, and `dwMipMapCount = 0`; this is the repository converter's one-level/base-surface representation for `MIP_LEVELS = "1"`

Raw DDS payloads were decoded by applying the declared BGRA masks and compared byte-for-byte with the processed PNGs converted to RGBA. All four comparisons are exact.

## Decoded-DDS contact sheet

- File: `docs/assets/014_cannibalism/static_event_art_imagegen/contact_sheets/super_events_final_dds_contact_sheet.png`
- Dimensions and mode: `986x796 RGB`
- SHA-256: `bd46c5cfe8855ee09decdc5ac6fda133ec48381466ae6671a45e46133f33f3a2`
- Each displayed `457x328` cell was compared with the raw BGRA-decoded runtime DDS and matched pixel-for-pixel.
- This sheet is a review artifact only and is not used by the game.

## Rejected and moderated attempt record

Two retained reveal-generation attempts produced no image:

1. `exec-3074414e-4ff5-4b46-a8ae-0ca7103553db` ended `2026-07-12T11:14:30.980Z` with `moderation_blocked` at the output stage in the `violence` category. The prompt contained explicit dismemberment instructions.
2. `exec-fdf7e638-e661-47bc-8935-08475eff868f` ended `2026-07-12T11:20:16.638Z` with `moderation_blocked` at the output stage in the `violence` category. It was still rejected after the explicit anatomical wording was narrowed.

The subsequent reveal prompt retained the chase, breach, fleeing adults, converging attackers, blood-stained setting, and command gesture while removing graphic injury close-ups. It produced the accepted action composition, followed by the accepted precise identity/detail edit.

No retained `image_generation_end` evidence records a rejected or moderated attempt for the accepted ordinary world-end, global-defeat, or transformed world-end outputs. No additional attempt history is inferred.

## Evidence limitations

- Exact OpenAI image-model and model-version identifiers are not present in the retained generation records. This prevents a model-specific provenance claim but does not affect the source hashes, output-path lineage, crop replay, DDS structure, or pixel-equality proof.
- Generator output paths are local Codex cache paths rather than repository paths. The repository-owned source PNGs preserve the accepted pixels, and their hashes match those cached outputs exactly.

## Scope exclusions

No gameplay, localisation, `.gfx`, GUI, audio, specification, report/news artwork, or other asset family was edited as part of this finalization.
