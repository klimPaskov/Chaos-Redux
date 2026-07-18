# Event 019 Regional Full-Flag Postprocess Remediation Re-Audit

Date: 2026-07-18  
Scope: Event 019 regional full-flag candidate only (91 identity/region rows)  
Mode: independent read-only re-audit after the documentation reconciliation  
Verdict: **PASS — remediation gate cleared**

This is a separate re-audit of the corrected documentation and the unchanged
7/18 asset rows. The original FAIL handoff,
`019_regional_full_flag_postprocess_independent_audit_2026_07_18.md`, was left
untouched. This PASS authorizes promotion of the 91-row regional candidate to
the parent-owned package workflow. It does not claim workbook export, package
inventory reconciliation, DDS/TGA wiring review, or final whole-event
completion; those remain later parent-owned gates.

## Scope and source-of-truth review

Re-read and cross-checked the current regional sections in:

- `docs/assets/019_infantry_spawn/manifest.md`
- `docs/assets/019_infantry_spawn/gfx_handoff.md`
- `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_18.json`
- `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_18.sha256`
- `docs/events/019_infantry_spawn.md`
- `docs/systems/triggerable_scenarios.md`
- `docs/systems/019_infantry_spawn_triggerable_scenario.md`
- `docs/specs/019_infantry_spawn_specs/README.md`
- `docs/specs/019_infantry_spawn_specs/review/blockers_and_uncertainty.md`
- `docs/plans/019_infantry_spawn_plans/source_of_truth_map.md`
- `docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`
- `docs/plans/019_infantry_spawn_plans/019_mandatory_improvement_loop_closure_handoff.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_documentation_reconciliation_2026_07_18.md`

The current chain is consistently documented as 91 unmodified built-in
ImageGen full-flag raws -> 91 deterministic 820x520 spot-colour masters ->
native 82x52, 41x26, and 10x7 PNGs -> 273 bottom-left-origin runtime TGAs.
The manifest status is correctly in progress with the validator status
`candidate_requires_independent_visual_review`, rather than a package-complete
claim. The old `regional_variants/` and 7/16 motif/composite records are
explicitly labelled archival/superseded in the current surfaces. The GFX
handoff names the regional processor, exact executable command, current
validation/checksum evidence, and current processor hash.

Searches for stale owner-choice, current-source, and obsolete-processor
wording found only explicitly negated or archival statements (for example,
“no longer describe ... awaiting owner choice”, “superseded/rejected as
current source”, and historical 7/16 handoff sections). No active source-of-
truth surface retains the former owner-choice blocker or points the regional
candidate at `process_event_019_generated_art.py`. The generic processor entry
in the manifest is separately accompanied by the current regional processor
entry and is not the regional validation owner.

## Exact GHOST_BASE prompt/archive recovery

The seven retained GHOST_BASE rows were checked against the archived JSONL at:

`C:/Users/klimp/.codex/sessions/2026/07/16/rollout-2026-07-16T22-47-22-019f6c78-240c-7202-afe2-5bba7e6e6dd1.jsonl`

The shared custom task is zero-based record 599, call ID
`call_C1UW7Dpr74vvHbUwksvojQU4`. For every row, the submitted prompt in the
current prompt record exactly matches the expanded line-599 task template and
the revised prompt exactly matches the archived `image_generation_end` prompt.
The archived result was decoded independently; its SHA-256 equals both the
retained raw source and the saved built-in result file. The current records
also preserve a forward-slash reference-image path, the archive timestamp,
result record, call ID, saved path, and raw/result digest.

| Region | Result record (zero-based) | Archive timestamp | `image_generation_end` call ID | Raw/result SHA-256 |
|---|---:|---|---|---|
| EUROPE | 660 | 2026-07-16T20:41:13.866Z | `exec-2fa201c7-ad5f-4c41-ad95-991ec717a209` | `0796537b4745852c72b9f25188bfd44b16aa85265b87131c8ae5cd6241246fb6` |
| MIDDLE_EAST | 665 | 2026-07-16T20:41:52.816Z | `exec-cf299094-3b37-43c3-9f99-b62499901e9c` | `ffca1492a7c9785d53243030bc2b4cd8d74dcb430afdab44eb8f3673688897d1` |
| AFRICA | 670 | 2026-07-16T20:42:35.131Z | `exec-cbcb9a98-a0ed-46f8-a0a7-666e295f25dd` | `92f812d86e523e3b2818597c7d90517456767b93ca020bb5337f72cab0231d10` |
| ASIA | 675 | 2026-07-16T20:43:19.128Z | `exec-9e61a730-e741-45c0-9b44-08e6ff8d6be3` | `39e87de52456f93e5da4b4ae8e56092d7df833b41b44d68f5b26b40d871689e7` |
| AUSTRALIA | 678 | 2026-07-16T20:43:58.207Z | `exec-e9b015c0-0d4d-4490-b0bf-a9d2e5813bc2` | `6c7a3cd6b17d3f79b1e498a9490339797b04ba9df65ab3399e14096699e8dfef` |
| NORTH_AMERICA | 681 | 2026-07-16T20:44:37.733Z | `exec-3eb5804b-75d1-44d9-acea-5380eaad49cd` | `4ea3d41e262a90265790d22b51597db8900952fdda0fe67f7521186e4e2db37a` |
| SOUTH_AMERICA | 686 | 2026-07-16T20:45:16.042Z | `exec-3c49f1c5-d49b-4121-918c-a570348df24a` | `bcc2fc0eb5d5670629cfed0229cad1d4b753db2650688b1aafc717aeebdecdcc` |

All seven prompt records use the expected forward-slash references under
`source_png/flags/regional_reference_inputs/INFANTRY_SPAWN_GHOST_BASE_<REGION>_source.png`.
All seven archive result payloads have status `completed`, the saved paths
exist, and their decoded result bytes match the current raw files byte-for-
byte.

## Independent 7/18 contract recomputation

The machine-readable evidence was re-read and every recorded file contract was
recomputed independently with Python 3.9.12/Pillow 11.1.0:

- Validation date `2026-07-18`, matrix 13 identities x 7 regions = 91 rows;
  recorded status remains `candidate_requires_independent_visual_review`.
- Regional processor SHA-256 is
  `d87e879184d5a28a52736b80af4bc0ce70abd9744de47210b1f6a7c3db15ece6`, matching
  the file at `docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py`.
- All 91 raw paths exist, have their recorded dimensions/mode, match the
  recorded built-in ImageGen result path and digest byte-for-byte, and are
  mutually byte-distinct.
- All 91 820x520 RGB spot masters match their recorded SHA-256 values, use only
  their recorded exact palette representatives, and are mutually byte-
  distinct.
- All 273 processed PNGs match their recorded hashes and dimensions (82x52,
  41x26, or 10x7), are RGBA with fully opaque alpha, and use only their row's
  recorded spot palette.
- All 273 runtime TGAs match their recorded hashes and checksum file entries;
  every header is uncompressed type 2, 32-bit RGBA, x/y origin 0, descriptor 8
  bottom-left, and the exact expected byte length. Every TGA decodes to the
  same RGBA pixels as its processed PNG.
- Recomputed totals were 91 unique tags, 91 unique raw hashes, 91 unique spot
  hashes, 273 processed PNGs, 273 runtime TGAs, 273 checksum records, and zero
  contract mismatches.

## Visual re-audit

The current raw/spot, three-size runtime, 10x7 readability, and GHOST_BASE raw
contact sheets were inspected again. The current hashes are unchanged from the
prior independent PASS row review:

- `event_019_regional_full_flag_claimant_zombie_raw_contact_sheet.png` —
  `e2d731418d9269080ba5e669bbffa80da87d2fce383f33ec930ec819820b2df9`
- `event_019_regional_full_flag_ghost_raw_contact_sheet.png` —
  `9a85fde7dbd0f4b088c991b0c72c142dda01211f7b35ca5ca54e73be19a6bff1`
- `event_019_regional_full_flag_golem_raw_contact_sheet.png` —
  `0fe26cd80a61a9f247c2ac44e6e5bb0ebaaad767ab19de33371f8369b21c2a5d`
- `event_019_regional_full_flag_raw_spot_contact_sheet.png` —
  `f0945b9e508e493372405b52a58806cc41ca950df1e654d054885382d89c6aa1`
- `event_019_regional_flag_contact_sheet.png` —
  `e83e0b59c946828dd7d9ce46250d8218a93f8996f2db74bcea2cec367ce65837`
- `event_019_regional_flag_small_readability_contact_sheet.png` —
  `c65c163dbe1a558589dbb9c51cc7fadffd52d58942d982e37d463e58ef6b1d64`

All 91 rows remain visually readable at normal/medium/small sizes. Identity
and region contracts remain distinct with no row swaps. No readable text,
watermark, people, fabric, pole, scenery, perspective, modern prop, or
processing artifact was observed. The deterministic spot pass preserves the
flat orthographic flag presentation and the regional/identity motifs at the
runtime sizes.

## Final disposition

**PASS.** The original documentation/provenance blockers are remediated and
the unchanged 91-row regional candidate is independently reproducible,
archive-backed, and visually unchanged. The parent may promote the 91-row
regional asset candidate using the current raw/spot/native PNG/runtime TGA
chain and current manifest/GFX handoff.

Remaining package gates are intentionally not folded into this verdict:
workbook/catalog export and reconciliation, package inventory reconciliation,
and the final whole-Event 019 completion audit. No fallback, regenerated
substitute, or simplification was used.

Files changed by this re-audit: this handoff only. No asset, manifest, GFX,
gameplay, localisation, workbook, or prior FAIL handoff was edited.
