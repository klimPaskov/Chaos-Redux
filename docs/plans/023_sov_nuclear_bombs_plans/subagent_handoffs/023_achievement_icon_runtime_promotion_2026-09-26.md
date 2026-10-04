# Event 023 achievement icon runtime promotion, 2026-09-26

Disposition: selected replacement art was promoted to the existing Event 023 achievement DDS destinations after parent visual review. Live HOI4 consumer presentation remains `needs_user_review`; no game was launched.

## Acceptance and prompt provenance

The user explicitly authorized new icon generation and replacement after the original `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md` was confirmed absent from the checkout and Git history. No original prompt was reconstructed or claimed. The exact v1 and v2 replacement prompts remain at `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set_replacement_2026-09-26.md` and `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set_replacement_2026-09-26_v2.md`.

The parent reviewed the native 64x64, 4x nearest-neighbour, alpha/round-trip, and lineage sheets. V2 was selected for the three v1 mismatches (a star on the storage door, a bomb inside the supposedly empty cradle, and an unreadable reflected cloud). The remaining four v1 candidates were selected after review. All v1 and v2 source/edit lineage is retained; no candidate source or template was overwritten.

## Selected runtime set

| Achievement ID | Selected lineage | Parent visual disposition |
| --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | v2 `GEN-08` | Unmarked storage cabinet; sealed casings remain readable at 64x64. |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | v2 `GEN-09` | Locked cradle is visibly empty; keys and dismantlement tools are distinct; no munition appears. |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | v1 `GEN-03` | Sealed unused device, separate keys, and blank document read as restraint without detonation. |
| `023_sov_nuclear_bombs_scattered_arsenal` | v1 `EDIT-04A` | Closed depot, converging rails, distinct crates, and guard form a readable compact symbol. |
| `023_sov_nuclear_bombs_firebreak` | v1 `EDIT-05A` | Rejoined field-telephone splice is inside the frame and readable. |
| `023_sov_nuclear_bombs_first_and_last` | v2 `GEN-10` | Empty rack and tools remain distinct; one pale cloud is visibly confined to the wrench reflection. |
| `023_sov_nuclear_bombs_the_last_telephone` | v1 `GEN-07` | Period telephone and sealed key capsule remain distinct at icon scale. |

Each selected source triplet was produced by the canonical achievement processor. The v1 audit passed seven triplets and the v2 audit passed three triplets; all 30 eligible/grey/not-eligible candidate DDS files across the selected and retained branches passed strict 64x64 BGRA validation and source-layer/template equality. The canonical templates remained byte-identical. No background-removal fallback was used.

The 21 selected candidate DDS files were copied into the stable runtime targets `gfx/achievements/<achievement_id>{,_grey,_not_eligible}.dds`, using the full achievement IDs in the table above. A post-copy SHA-256 check matched every runtime file byte-for-byte to its selected candidate (21/21). No achievement ID, alias, `.gfx` registration, definition, localization, or gameplay code changed in this asset tranche.

## Files and remaining validation

- Runtime: the 21 existing `gfx/achievements/023_sov_nuclear_bombs_*.dds` files, with stable destinations and aliases.
- Source/provenance: v1 and v2 prompts, generated masters, focused-edit branches, deterministic triplets, candidate DDS, review PNGs, contact sheets, processor logs, manifest, and replacement crosswalks under `docs/assets/023_sov_nuclear_bombs/`.
- Existing GFX and achievement registry wiring: unchanged; the stable aliases in `interface/chaosx_achievements.gfx` still resolve to the same 21 runtime filenames.

The `docs/assets/` tree is ignored by Git in this repository. The new versioned replacement lineage and updated manifest/crosswalk require explicit path-scoped force-add when committing the asset tranche; unrelated ignored assets must not be staged.

The selected art has parent static review. It is not represented as a live native-game visual acceptance result. No runtime test, GUI change, or user-owned in-game validation was performed.

## Current runtime recheck, 2026-10-03

The canonical processor was run with `--audit --input <selected-version>/source_triplets --achievement-id <id> --output-dir gfx/achievements` for each of the seven selected IDs.
All seven current runtime triplets returned `AUDIT OK`, proving strict 64x64 BGRA decoding and exact equality with the selected source layers composited over the canonical templates.
This recheck read the final runtime destination files and wrote no output assets.
