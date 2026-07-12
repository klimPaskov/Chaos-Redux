# Event 014 Europe/Asia/Africa Warlord Portrait Handoff

Owner: `/root/event014_feral_warlord_portraits`

Status: complete for the assigned Europe, Asia, and Africa tranche

## Delivered scope

- 24 distinct built-in-imagegen source portraits: CBA-CBH for Europe, Asia, and
  Africa.
- 24 processed `156x210 RGBA` PNGs.
- 24 installed uncompressed one-image-level BGRA DDS runtime textures.
- Per-region source, processed, and decoded-DDS review sheets.
- Three-region source, processed, actual-size, and decoded-DDS review sheets.
- Exact 82-attempt generation audit with all revised prompts, imagegen call IDs,
  42 moderation request IDs, saved outputs, and rejection/intermediate/final
  dispositions.
- Prompt ledger, crop ledger, hash ledger, validation report, tranche manifest,
  and GFX handoff.

## Runtime identifiers

- Europe textures: `gfx/leaders/014_cannibalism/leader_CBA_warlord.dds` through
  `leader_CBH_warlord.dds`
- Asia textures: `gfx/leaders/014_cannibalism/leader_CBA_warlord_asia.dds`
  through `leader_CBH_warlord_asia.dds`
- Africa textures: `gfx/leaders/014_cannibalism/leader_CBA_warlord_africa.dds`
  through `leader_CBH_warlord_africa.dds`
- Existing sprites: `GFX_portrait_<TAG>_warlord`,
  `GFX_portrait_<TAG>_warlord_europe`,
  `GFX_portrait_<TAG>_warlord_asia`, and
  `GFX_portrait_<TAG>_warlord_africa`

## Principal package files

- `docs/assets/014_cannibalism/warlord_portraits_imagegen/europe_asia_africa_manifest.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/gfx_handoff_europe_asia_africa.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/europe_asia_africa_hashes.sha256`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/prompts/europe_asia_africa_prompt_ledger.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/europe_asia_africa_generation_attempts.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/europe_asia_africa_generation_attempts.json`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/europe_asia_africa_crop_ledger.csv`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/europe_asia_africa_processing.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/europe_asia_africa_validation.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/europe_asia_africa_validation.json`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/build_europe_asia_africa_tranche.py`

## Validation evidence

- All `24` source, processed, and runtime SHA-256 hashes are unique.
- Every processed PNG is `156x210 RGBA`.
- Every DDS decodes to `156x210 RGBA` and is pixel-identical to its processed
  PNG.
- Every DDS has a `124`-byte header, `624`-byte row pitch, uncompressed 32-bit
  BGRA masks, texture caps, one stored base image, and size `131168` bytes.
- Whole-image 64-bit dHash distance spans `17-43`; the closest pair was manually
  reviewed and remains visually distinct in face, pose, prop, clothing, light,
  and setting.
- The source, processed, actual-size, and decoded-runtime contact sheets were
  directly inspected after final conversion.

## Parent merge actions

1. Preserve the 24 runtime paths and their existing Event 014 registrations.
2. Merge this tranche's manifest, prompt/attempt evidence, and review sheets into
   the parent-owned all-region manifest and all-set contact sheet.
3. Do not promote any intermediate or rejected output listed in the attempt
   ledger.
4. Include these 24 paths in the parent commit without staging unrelated shared
   worktree changes.

## Simplifications, omissions, and blockers

None within the assigned Europe, Asia, and Africa scope. Middle East, North
America, South America, Oceania, `.gfx` edits, gameplay, localisation, and the
combined all-region package were explicitly outside this subagent's ownership.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- `imagegen`

No skill was created or updated; this tranche did not reveal a reusable workflow
gap beyond the existing asset and subagent guidance.
