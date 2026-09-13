# Event 029 Riches Found achievement icon audit handoff

Date: 2026-09-01

Worker scope: audit and repair the seven registered Event 029 achievement triplets as evidence/package files only.

Runtime wiring and in-game validation remain parent-owned. This worker did not edit `common/`, `interface/`, `localisation/`, `events/`, `decisions/`, gameplay files, GFX files, or the existing runtime `gfx/achievements/` DDS files.

## Outcome

All seven registered achievement IDs have retained native 64x64 source triplets, processed source-layer copies, repaired composited evidence previews, repaired evidence DDS triplets, recovered full prompt files, and per-state QA records.

| Achievement id | Source triplet | Evidence DDS triplet | Prompt record | Evidence status | Runtime status |
|---|---|---|---|---|---|
| `029_public_fortune` | `docs/assets/029_riches_found/source_triplets/achievement_029_public_fortune/` | `docs/assets/029_riches_found/final_dds/achievements/029_public_fortune.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_public_fortune_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_public_fortune_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_public_fortune_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |
| `029_claim_jumper` | `docs/assets/029_riches_found/source_triplets/achievement_029_claim_jumper/` | `docs/assets/029_riches_found/final_dds/achievements/029_claim_jumper.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_claim_jumper_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_claim_jumper_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_claim_jumper_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |
| `029_the_pay_train_runs` | `docs/assets/029_riches_found/source_triplets/achievement_029_the_pay_train_runs/` | `docs/assets/029_riches_found/final_dds/achievements/029_the_pay_train_runs.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_the_pay_train_runs_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_the_pay_train_runs_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_the_pay_train_runs_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |
| `029_all_that_glitters` | `docs/assets/029_riches_found/source_triplets/achievement_029_all_that_glitters/` | `docs/assets/029_riches_found/final_dds/achievements/029_all_that_glitters.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_all_that_glitters_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_all_that_glitters_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_all_that_glitters_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |
| `029_no_man_owns_the_mountain` | `docs/assets/029_riches_found/source_triplets/achievement_029_no_man_owns_the_mountain/` | `docs/assets/029_riches_found/final_dds/achievements/029_no_man_owns_the_mountain.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_no_man_owns_the_mountain_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_no_man_owns_the_mountain_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_no_man_owns_the_mountain_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |
| `029_close_the_account` | `docs/assets/029_riches_found/source_triplets/achievement_029_close_the_account/` | `docs/assets/029_riches_found/final_dds/achievements/029_close_the_account.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_close_the_account_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_close_the_account_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_close_the_account_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |
| `029_the_last_shift` | `docs/assets/029_riches_found/source_triplets/achievement_029_the_last_shift/` | `docs/assets/029_riches_found/final_dds/achievements/029_the_last_shift.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_the_last_shift_grey.dds`; `docs/assets/029_riches_found/final_dds/achievements/029_the_last_shift_not_eligible.dds` | `docs/assets/029_riches_found/prompts/achievements/029_the_last_shift_prompt.md` | Complete; strict audit pass | Synchronized; runtime byte-equal |

Each source directory contains exactly `<id>.png`, `<id>_grey.png`, and `<id>_not_eligible.png`.

## Repair and evidence disposition

Retained assets: the seven existing native-transparent source triplets and their seven recovered full prompt files were retained because they passed the source and visual checks.

Repaired assets: all 21 evidence DDS files were rebuilt with the strict achievement processor, and all 21 composited evidence previews plus all 21 decoded DDS review PNGs were refreshed.

Missing evidence: the inherited workspace does not retain ImageGen request or response identifiers for these seven generations, so no such identifier is claimed or fabricated. The specifically named `common/achievements/029_riches_found_achievements.txt` file is also absent; the actual definitions were found in `common/achievements/chaos_redux_achievements.txt`.

Needs user review: parent-owned synchronization of the 21 repaired evidence DDS files to `gfx/achievements/` and live consumer validation remain outstanding.

## Consumer and path evidence

The specifically named `common/achievements/029_riches_found_achievements.txt` file is not present in this workspace; the seven exact achievement definitions are registered in `common/achievements/chaos_redux_achievements.txt` at lines 4378, 4388, 4398, 4408, 4413, 4424, and 4435 respectively.

The exact project aliases and runtime texture paths are registered in `interface/029_riches_found.gfx`: `029_public_fortune` lines 347-356, `029_claim_jumper` lines 359-368, `029_the_pay_train_runs` lines 371-380, `029_all_that_glitters` lines 383-392, `029_no_man_owns_the_mountain` lines 395-404, `029_close_the_account` lines 407-416, and `029_the_last_shift` lines 419-428.

The exact vanilla consumer is root `gfx/achievements/`. For every ID the engine filenames are `gfx/achievements/<id>.dds`, `gfx/achievements/<id>_grey.dds`, and `gfx/achievements/<id>_not_eligible.dds`; the offline Achievement modding reference and vanilla `common/achievements.txt` were inspected, and no per-achievement `spriteType` is required.

The machine audit lists every concrete source, processed, evidence DDS, decoded DDS, runtime path, sprite alias, and consumer line in `docs/assets/029_riches_found/notes/achievement_icon_audit.json`.

## Canonical reference and template evidence

The canonical reference family was inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/`, beginning with `contact_sheet.png` and then the individual vanilla color, grey, and not-eligible references.

The exact immutable template inputs were inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/template/`.

| Template input | SHA-256 | Dimensions |
|---|---|---:|
| `achievement_template.png` | `248db006611eb3942550c43df83802aa6fb24761035fc928b5d34586c0c4c5ba` | 64x64 |
| `achievement_template_grey.png` | `70e073694c1a7d9fe40c63b1eb2e987a8a45b3ffd15ccf789eeaa5b843b90022` | 64x64 |
| `overlay.png` | `89bc80c6ac975bf6f1ff000ff3070b20c337bfb8b8ae966ae35a5540c004d6dd` | 64x64 |

The supplied templates and overlay remain unchanged. The final evidence DDS files use the canonical completed background under the completed state and the canonical grey background under both grey and not-eligible states.

## Processing and QA evidence

Each ID was processed with the strict achievement processor using the retained source triplet as input:

```text
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --input docs/assets/029_riches_found/source_triplets/achievement_<id> --achievement-id <id> --output-dir docs/assets/029_riches_found/final_dds/achievements --write-png --force
```

The processor writes the evidence DDS through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and emitted the repaired composited review PNGs under `docs/assets/029_riches_found/final_dds/achievements/review/`.

The 21 retained source states were individually checked at exactly 64x64 with native alpha, and the 21 repaired evidence DDS files were individually decoded and inspected at exactly 64x64.

All seven grey source states equal deterministic grayscale derivatives of their completed source states with the canvas and alpha preserved.

All seven not-eligible source states equal their grey source state composited with the unchanged canonical overlay at exact 64x64 alignment.

All 21 repaired evidence states pass strict uncompressed BGRA header, dimensions, file-length, alpha, and pixel-exact decoded round-trip checks.

The native-size contact sheet `docs/assets/029_riches_found/contact_sheets/achievements_contact_sheet.png` shows, for every ID, completed/grey/not-eligible source layers, processed composited layers, and decoded DDS layers.

No background-removal fallback was used. No opaque or chroma background was introduced into the source subjects. No placeholder, fallback art, cross-family substitute, resized unrelated icon, portrait, flag, animation, audio, unit, 3D art, readable text, treasure chest, giant fantasy crystal, horned generic demon, or copied living religious symbol was used.

## Provenance

The full prompts are retained in `docs/assets/029_riches_found/prompts/achievements/029_<id>_prompt.md`, indexed by `docs/assets/029_riches_found/prompts/achievements/generation_records.md`, and linked from every per-state record in the machine audit.

The inherited workspace retained complete prompt text and source subject PNGs but did not retain ImageGen request or response identifiers for these seven generations. No missing identifier was fabricated. The source subjects passed audit, so no regeneration was performed during this repair.

## Runtime handoff and blockers

All 21 root runtime DDS files under `gfx/achievements/` were inspected individually and the parent synchronized the repaired evidence triplets to the exact registered paths.

The current machine audit records byte equality against the repaired evidence for all 21 runtime files, along with native-size consumer evidence.

Live in-game rendering remains user-owned; no source, runtime, wiring, or asset-production blocker remains in this handoff.
