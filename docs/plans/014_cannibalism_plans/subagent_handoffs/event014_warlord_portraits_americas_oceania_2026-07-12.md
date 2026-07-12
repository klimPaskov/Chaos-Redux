# Event 014 Warlord Portraits Americas Handoff

Date: 2026-07-12

Subagent task path: `/root/event014_warlord_portraits_americas_oceania`

## Outcome

Completed all 16 parent-owned North America and South America CBA-CBH warlord portraits. Each selected portrait has an independent built-in `image_gen` source PNG, manually reviewed 156x210 RGBA processed PNG, and uncompressed one-mip BGRA DDS at the already-registered runtime path.

The parent reviewed and accepted the final source board after rejecting ordinary-looking early attempts. The final actions, faces, asymmetry, expressions, props, crops, clothing constructions, and backgrounds are visibly distinct within the Americas set and do not repeat the accepted Europe CBA skull-licking or CBB ration-biscuit actions.

## Ownership revision

The initial assignment also named Oceania. During production the parent reassigned all eight Oceania portraits to `/root/event014_warlord_middle_east_oceania` before this tranche created any Oceania source, processed PNG, or DDS. This handoff claims only North America and South America. The stable ledger filename still includes `americas_oceania`, but its title and content explicitly release Oceania.

## Created files

### Final accepted artwork

- 16 source PNGs: `docs/assets/014_cannibalism/warlord_portraits_imagegen/source_png/leader_CB[A-H]_warlord_{north_america,south_america}_source.png`
- 16 processed PNGs: `docs/assets/014_cannibalism/warlord_portraits_imagegen/processed_png/leader_CB[A-H]_warlord_{north_america,south_america}.png`
- 16 runtime DDS files: `gfx/leaders/014_cannibalism/leader_CB[A-H]_warlord_{north_america,south_america}.dds`

Exact per-asset paths, registered sprite ids, origins, and actions are in `docs/assets/014_cannibalism/warlord_portraits_imagegen/americas_tranche_manifest_2026-07-12.md`.

### Rejected-attempt evidence

Nine generated but rejected sources are preserved under `docs/assets/014_cannibalism/warlord_portraits_imagegen/source_png/rejected_attempts/`. Their filenames state the rejection reason: too jovial, too ordinary, cropped hook, or too passive. None was processed or converted into a final DDS.

### Tranche documentation and proof

- Behavior reservation: `docs/assets/014_cannibalism/warlord_portraits_imagegen/prompts/americas_oceania_behavior_ledger.md`
- Prompt and attempt ledger: `docs/assets/014_cannibalism/warlord_portraits_imagegen/prompts/americas_prompt_attempt_ledger_2026-07-12.md`
- Tranche manifest: `docs/assets/014_cannibalism/warlord_portraits_imagegen/americas_tranche_manifest_2026-07-12.md`
- Crop and conversion ledger: `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/americas_processing_2026-07-12.md`
- Validation and decoded-pixel proof: `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/americas_validation_2026-07-12.md`
- SHA-256 ledger: `docs/assets/014_cannibalism/warlord_portraits_imagegen/hashes_americas_2026-07-12.sha256`
- Source contact: `docs/assets/014_cannibalism/warlord_portraits_imagegen/contact_sheets/warlord_americas_source_contact_2026-07-12.png`
- Processed contact: `docs/assets/014_cannibalism/warlord_portraits_imagegen/contact_sheets/warlord_americas_processed_contact_2026-07-12.png`
- DDS-decoded contact: `docs/assets/014_cannibalism/warlord_portraits_imagegen/contact_sheets/warlord_americas_dds_decoded_contact_2026-07-12.png`

## Runtime identifiers

The live `interface/014_cannibalism.gfx` registrations already point to these exact files as `GFX_portrait_<SLOT>_warlord_north_america` and `GFX_portrait_<SLOT>_warlord_south_america`. No `.gfx`, gameplay, localisation, character, flag, spreadsheet, other regional portrait, or other asset-family file was edited by this tranche.

All 16 portraits are adult male-presenting and require their matching male regional name pools and male metadata. Do not pair them with `female = yes` or a female name pool.

## Meaningful validation evidence

- Parent visual review accepted all 16 final source compositions at grouped board scale.
- Every processed PNG is exactly 156x210 RGBA with alpha extrema `(255,255)`.
- Every DDS is 131,168 bytes, 156x210, 32-bit BGRA with the expected masks, 624-byte pitch, and one stored base image level.
- FFmpeg decoded every DDS successfully; every decoded RGBA byte stream is exactly equal to its processed PNG byte stream.
- Source, processed, and DDS SHA-256 values are unique across all 16 accepted assets.
- Full-image dHash pairwise distance ranges from 21 to 43 bits. Manual review separates the closest pairs by face geometry, action, prop, silhouette, clothing, lighting, and setting.

## Moderation blocks and rejected outputs

Five built-in output-stage moderation blocks occurred:

- North America CBA attempt 1: `db4d6127-6b94-451b-bf5a-e947af037c0d`
- North America CBC attempt 2: `88e78698-b76d-4b88-babb-613086fcaa0c`
- North America CBC attempt 3: `d8fbb000-84be-4b2c-b6db-28c9877ae380`
- South America CBH attempt 1: `0e555c1f-0b82-4cc1-aaac-c7ec781748d0`
- South America CBH attempt 2: `31425a8c-bd15-4679-a33e-66689c6a1631`

No blocked call produced a file. The complete generated-rejection ledger is in the tranche prompt/attempt ledger.

## Simplifications, omissions, and blockers

- No simplification, fallback, placeholder, locally fabricated artwork, missing asset, or unresolved file exists inside the final 16-portrait North/South America scope.
- Oceania is not an omission from this completed tranche; the parent explicitly reassigned it before production, and a separate live agent owns it.
- No Git commit was created by this subagent because the parent owns final integration and the shared worktree contains concurrent Event 014 tranches. The parent should review and include these files in the plan-level commit.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`

No skill was created or updated.

