# Event 019 Golem Regional Full-Flag Raw Source Handoff

> **Raw-tranche status (2026-07-18):** This handoff remains valid as source
> evidence for its 28-row raw tranche, but its raw-only boundary is historical.
> The later 7/18 postprocess adds the 91-row spot-master, native PNG, and
> runtime-TGA chain. Visual/runtime rows pass, and the independent remediation
> re-audit handoff
> `019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md` is PASS,
> clearing the regional asset gate for parent-owned package promotion. The
> machine JSON retains its immutable literal
> `candidate_requires_independent_visual_review` processor-state value. Parent
> workbook/catalog reconciliation and export are complete, Event 19 and SCN-013
> now read `Fully Functional`, and package inventory and final completion audit
> are PASS-complete. No closure gate remains. Current package status is owned by
> the manifest and final audit handoff.

Date: 2026-07-18

## Scope and disposition

This handoff covers only the Event 019 Golem regional full-flag raw-source batch: four identity contracts (GOLEM_BASE, GOLEM_CLAIMANT, GOLEM_COLLECTIVE, GOLEM_SPECIES) crossed with seven regions (EUROPE, MIDDLE_EAST, AFRICA, ASIA, AUSTRALIA, NORTH_AMERICA, SOUTH_AMERICA). Exactly 28 separate built-in ImageGen calls were made, one per runtime tag. Every generated result was copied unmodified and retained in the owned raw folder. The Event 019 user-approved deterministic spot-colour flattening/normalisation exception remains available for a later processing tranche; no final processed flag, runtime TGA, or DDS is claimed here.

## Changed files

- `docs/assets/019_infantry_spawn/source_png/flags/regional_full_flag_raw/golem/`: **28** unmodified ImageGen raw PNGs, named `INFANTRY_SPAWN_GOLEM_<IDENTITY>_<REGION>_imagegen_raw.png`.
- `docs/assets/019_infantry_spawn/prompts/regional_full_flag_golem_prompts_2026_07_18.md`: shared production brief, identity/region contracts, and all **28** full prompt sections.
- `docs/assets/019_infantry_spawn/notes/regional_full_flag_golem_provenance_2026_07_18.md`: **28** provenance sections with exact owned path, built-in result handle/path, prompt reference, SHA-256, dimensions/mode, disposition, and visual survival notes.
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_full_flag_golem_raw_contact_sheet.png`: review-only contact sheet for all **28** raw sources.
- This handoff file.

No gameplay, localisation, GFX, GUI, spreadsheet, registry, processed flag, runtime TGA, or DDS files were edited.

## Validation evidence

- Raw count: **28/28** expected Cartesian-product rows present; no duplicate legacy filenames remain.
- Filename contract: all rows use the `INFANTRY_SPAWN_GOLEM_<IDENTITY>_<REGION>_imagegen_raw.png` form.
- Source dimensions/mode: all **28** decode as **1586x992 RGB** ImageGen outputs; bytes were copied without local resizing, compositing, or recolouring.
- SHA-256: every raw file is recorded in the provenance note and can be recomputed from the owned path.
- Built-in provenance: all **28** handles point to the retained originals under `C:/Users/klimp/.codex/generated_images/019f7430-d891-75c2-a496-8e8bc3242228/`.
- Contact-sheet review: all identity and regional motifs are visually distinct and central silhouettes remain readable when reduced for flag-size review.

## Remaining risks and next owner actions

- Raw ImageGen results retain some tonal falloff/dimensional variation. Under the explicit Event 019 exception, a separate deterministic spot-colour flattening/normalisation pass must produce processed masters while retaining these raw sources and recording exact arguments/hashes.
- These raw PNGs are not final runtime flags and are not self-approved. A separate reviewer must inspect the processed 82x52, 41x26, and 10x7 ladder before runtime conversion.
- The main asset owner should wire only independently reviewed processed outputs into the existing flag pipeline; this subtask intentionally did not edit processed variants, runtime TGAs, or registries.
