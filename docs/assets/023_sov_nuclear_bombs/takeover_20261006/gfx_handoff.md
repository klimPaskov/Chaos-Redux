# GFX handoff: Event 023 icon defects, 2026-10-06

## Result

The three reviewed Event 023 icon defects are repaired and the approved candidate DDS files are promoted to their existing runtime paths. The existing sprite aliases and `.gfx` texture paths remain unchanged.

| Asset | Final runtime path | Canvas | Status |
| --- | --- | ---: | --- |
| Delivery preparation bomber | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_delivery_preparation.dds` | 33x32 | Complete; three-quarter bomber, one visible bomb, warm bronze highlights. |
| Device disablement | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_disablement.dds` | 33x32 | Complete; retained bomb/device source enlarged to 28x22 with safe margins. |
| Broken-chain national spirit | `gfx/interface/ideas/023_sov_nuclear_bombs/sov_nuclear_spirit_broken_chain.dds` | 60x68 | Complete; original red-and-black medal badge with upright warhead and broken chain. |

All source generations, selected background-only edits, prior sources, processed PNGs, candidate DDS files, exact previous runtime DDS files, prompts, and audit evidence are retained under this `takeover_20261006/` directory.

## Source and review paths

The generated delivery-preparation source and its prompt record are `source_png/imagegen_initial/sov_nuclear_decision_delivery_preparation_initial.png`, `source_png/transparent_edit/sov_nuclear_decision_delivery_preparation_background_edit.png`, and `prompts/sov_nuclear_decision_delivery_preparation.md`.

The generated broken-chain source and its prompt record are `source_png/imagegen_initial/sov_nuclear_spirit_broken_chain_initial.png`, `source_png/transparent_edit/sov_nuclear_spirit_broken_chain_background_edit.png`, and `prompts/sov_nuclear_spirit_broken_chain.md`.

The device-disablement source and recrop record are `source_png/preexisting/sov_nuclear_decision_device_disablement_original_source.png` and `prompts/sov_nuclear_decision_device_disablement.md`.

The accepted native-size processed previews are `processed_png/sov_nuclear_decision_delivery_preparation_33x32.png`, `processed_png/sov_nuclear_decision_device_disablement_33x32.png`, and `processed_png/sov_nuclear_spirit_broken_chain_60x68.png`.

The parent-reviewed before/after contact sheets are `contact_sheets/icon_replacements_native_20261006.png` and `contact_sheets/icon_replacements_4x_20261006.png`. They display prior runtime DDS and candidate DDS art over checkerboard, white, and navy surfaces, with a separate alpha view.

The selected runtime achievement triplets are shown in `contact_sheets/achievement_runtime_grey_x_native_20261006.png` and `contact_sheets/achievement_runtime_grey_x_4x_20261006.png`.

The optional non-erosive defringe comparison is `contact_sheets/defringe_probe_comparison_4x_20261006.png`.

## Validation evidence

The `.tools/gfx/gfx.py dds` path converted all three processed previews through the canonical `convert_to_dds.py` writer and strictly decoded them; 3/3 passed with no findings in `evidence/candidate_dds_report.json`.

The final runtime `.tools/gfx` alpha report passes 3/3 with no findings, alpha extrema 0–255, subject alpha means 203.35, 226.859, and 239.208, and zero magenta/green chroma-edge pixels; see `evidence/final_runtime_alpha.json`.

The final runtime size reports pass 2/2 decision icons at 33x32 and 1/1 idea icon at 60x68, with safe margins and no undersized-span findings; see `evidence/final_runtime_decision_size.json` and `evidence/final_runtime_idea_size.json`.

Each promoted runtime DDS SHA-256 equals its parent-approved candidate DDS SHA-256 byte-for-byte. The exact hashes and processed alpha bounds are recorded in `evidence/processed_icon_metrics.json`.

The initial generated bomber and medal sources were opaque checkerboards despite the native-transparency prompts. Each was preserved unchanged and passed through a background-only built-in ImageGen edit with `transparent_background=true`. The edited sources were confirmed to contain transparent unused canvas and complete subject bounds; no opaque checkerboard was promoted.

The `.tools/gfx` alpha checks found no chroma-edge contamination, and the non-erosive defringe probe showed no visible fringe defect on white or navy. The approved candidate previews and DDS were retained without applying the probe's edge RGB changes.

The selected v1/v2 achievement source triplets pass the canonical processor audit against all seven exact runtime IDs. Source verification confirms 7/7 grey layers are exact color-source grayscale derivations and 7/7 not-eligible layers are exact grey-plus-unchanged-overlay composites. The immutable canonical templates and overlay retain their recorded hashes, and all 21 runtime achievement DDS files match their selected source composites and selected candidate DDS byte-for-byte; see `evidence/achievement_processor_audit.txt` and `evidence/achievement_grey_x_runtime_audit.json`.

## Parent and live review

The parent reviewed both native and 4x candidate sheets and approved all three replacements before promotion. This is static asset review; live in-game rendering remains `needs_user_review` for the user.

No `.gfx`, `.gui`, gameplay, event, decision, idea, localisation, history, or spreadsheet files were edited. No commit or staging operation was performed.

The exact changed-path inventory is `evidence/changed_paths.txt`.
