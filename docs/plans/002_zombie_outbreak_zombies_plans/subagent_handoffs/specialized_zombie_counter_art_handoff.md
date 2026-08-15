# Specialized zombie counter art handoff

## Result

Completed bespoke evidence/package artwork for exactly these seven active non-armored units:

`infected_zombies`, `rabid_zombies`, `parasitic_zombies`, `mutant_zombies`, `undead_zombies`, `necrotic_zombies`, `demonic_zombies`.

All seven have two-frame large and two-frame small DDS packages and are marked `needs_user_review` pending parent review. None is blocked. No unit uses a copied vanilla counter, a generic identical copy, a static placeholder, or an arbitrary green palette.

## Package locations

For each `<unit>`:

- Large DDS: `docs/assets/002_zombie_outbreak/models_3d/<unit>/counters/large/unit_<unit>_icon.dds`.
- Small DDS: `docs/assets/002_zombie_outbreak/models_3d/<unit>/counters/small/onmap_unit_<unit>_icon.dds`.
- Native large sheet: 152×42, two 76×42 frames.
- Native small sheet: 60×12, two 30×12 frames.
- Source, alpha, processed, round-trip, contact sheet, metrics, validation, manifest, and SHA-256 files are in that unit's `counters/` folder.

The package-level overview is `docs/assets/002_zombie_outbreak/models_3d/gfx_handoff.md`.

## Installed vanilla and canonical-reference evidence

Installed vanilla inspection was read-only and covered:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

The matching canonical contact sheets were inspected first from the one allowed root:

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`

Specifically, `units/land/counters_large/contact_sheet.png` and `units/land/map_counters/contact_sheet.png` were reviewed before the individual infantry references. Those references established the two-frame order, 152×42 and 60×12 canvases, alpha behavior, silhouette scale, border/shading conventions, and state contrast.

The inspected installed normal large state contains the exact vanilla green `#496a49` (`RGB 73,106,73`). Final processed opaque pixels were palette-mapped to the corresponding installed vanilla infantry frame; the alternate state uses the installed pale schematic palette and the small normal state uses the installed on-map infantry palette. The generated art therefore does not use a guessed green.

The existing matching model inputs and weaponized portraits were inspected and captured in `counter_evidence/matching_refs/`. Existing mod counter files were captured in `counter_evidence/current_mod/`; their generic repeated silhouettes were not reused.

## Consumers and runtime boundary

The existing consumer names and expected runtime paths are:

| Surface | Consumer sprite | Runtime path | Frames |
| --- | --- | --- | ---: |
| Large | `GFX_unit_<unit>_icon_medium` | `gfx/interface/counters/divisions_large/unit_<unit>_icon.dds` | 2 |
| Small | `GFX_unit_<unit>_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_<unit>_icon.dds` | 2 |

Frame 0 is the unit-specific normal silhouette. Frame 1 is the unit-specific pale sparse alternate schematic. The parent owns any runtime promotion and final in-game consumer review.

## Generation and processing

The official native ImageGen workflow generated original source PNGs with the matching model and portrait references as subject guidance. The exact prompts, unit motifs, source attachments, chroma-key instruction, and the regenerated wide undead source are recorded in `counter_evidence/generation_prompts.md`.

The sources used a solid `#ff00ff` key only for alpha extraction. `remove_chroma_key.py` was used with automatic border keying, soft matte, despill, and a transparent threshold. The processed frames were cropped to silhouette, smoothly reduced to the exact native frame sizes, and mapped to the installed vanilla state palettes. DDS conversion used `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` at 152×42 and 60×12.

## Validation

The regenerated validation evidence reports:

- 7 units and 14 final DDS files checked.
- Every large DDS is exactly 152×42.
- Every small DDS is exactly 60×12.
- Every DDS round-trips pixel-identically against its processed PNG sheet.
- Every processed opaque frame palette is a subset of the corresponding installed vanilla infantry state palette.
- Every sheet contains two frames in the inspected vanilla order.

Evidence is in `counter_evidence/validation_summary.json`, with per-unit detail in each `counters/validation.json`. Per-file hashes are in each unit's `counters/sha256sums_artifacts.txt` and duplicated in `counters/manifest.md`.

Shared evidence hashes are in `counter_evidence/shared_evidence_sha256sums.txt`, and the exhaustive generated-package inventory is in `counter_evidence/counter_package_file_inventory.txt`.

## Changed files and exclusions

This subagent added or updated only evidence/package outputs under `docs/assets/002_zombie_outbreak/models_3d/` plus this handoff under `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/`.

It did not edit `common/units`, runtime `.gfx`, runtime `.asset`, sounds, base counters, armored counters, or any existing runtime DDS. No Meshy call, paid call, or unrelated repository edit was made by this work.

## Parent review state

Parent review should compare the shared and per-unit contact sheets, verify the exact runtime sprite consumers, and decide whether to promote any package DDS into runtime. The package is complete as an art handoff but is not a claim of runtime wiring or live-game validation.
