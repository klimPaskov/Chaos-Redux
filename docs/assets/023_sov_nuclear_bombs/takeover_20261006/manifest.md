# Event 023 icon defect takeover manifest

Date: 2026-10-06.

Scope: repair the three Event 023 icon findings in the external GFX review plan while preserving their registered sprite names and runtime paths.

Disposition: the three static icon assets are produced, parent-reviewed, and promoted; live HOI4 consumer review remains `needs_user_review`.

## Requirement-to-runtime crosswalk

| Finding | Sprite alias | Runtime DDS | Canvas | Result |
| --- | --- | --- | ---: | --- |
| Delivery preparation bomber framing | `GFX_decision_sov_nuclear_decision_delivery_preparation` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_delivery_preparation.dds` | 33x32 | Complete; compact nose-forward three-quarter bomber with one under-fuselage bomb, visible bronze highlights, and transparent padding. |
| Device disablement undersized device | `GFX_decision_sov_nuclear_decision_device_disablement` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_disablement.dds` | 33x32 | Complete; retained source recrop enlarged to 28x22 subject bounds with 2px horizontal and 5px vertical margin. |
| Broken-chain spirit style | `GFX_idea_sov_nuclear_spirit_broken_chain` | `gfx/interface/ideas/023_sov_nuclear_bombs/sov_nuclear_spirit_broken_chain.dds` | 60x68 | Complete; framed red-and-black Soviet medal badge with upright warhead and broken chain, sized to 51x61 subject bounds. |

## Reference inspection

The canonical contact sheets inspected first were `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions/contact_sheet.png`, `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/ideas/contact_sheet.png`, and `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/contact_sheet.png`.

Canonical decision examples then inspected individually were `icons/decisions/decision_generic_guerilla_base_2.png` and the 33x32 reference family recorded in the canonical `CATALOG.md`.

Canonical idea examples then inspected individually were `icons/ideas/idea_generic_deal_with_the_devil.png` and `icons/ideas/home_of_the_revolution.png`.

The Event 023 sibling source sheet and relevant sibling sources included `sov_nuclear_decision_device_assembly`, `sov_nuclear_spirit_coercive_arsenal`, and `sov_nuclear_spirit_unrestrained_release`.

The exact Event 023 sprites and consumer paths were read from `interface/023_sov_nuclear_bombs.gfx`; all three aliases and paths remain unchanged.

## Sources and lineage

The delivery-preparation source is `source_png/transparent_edit/sov_nuclear_decision_delivery_preparation_background_edit.png`, produced by a targeted background-only built-in ImageGen edit. The opaque checkerboard ImageGen input is preserved at `source_png/imagegen_initial/sov_nuclear_decision_delivery_preparation_initial.png`, and its exact prompt and generation paths are recorded in `prompts/sov_nuclear_decision_delivery_preparation.md`.

The broken-chain source is `source_png/transparent_edit/sov_nuclear_spirit_broken_chain_background_edit.png`, produced by a targeted background-only built-in ImageGen edit. The opaque checkerboard ImageGen input is preserved at `source_png/imagegen_initial/sov_nuclear_spirit_broken_chain_initial.png`, and its exact prompt and generation paths are recorded in `prompts/sov_nuclear_spirit_broken_chain.md`.

The device-disablement icon reuses the retained, native-alpha artwork copied byte-for-byte to `source_png/preexisting/sov_nuclear_decision_device_disablement_original_source.png` from `docs/assets/023_sov_nuclear_bombs/source_png/decisions/sov_nuclear_decision_device_disablement_source.png`. Its recrop procedure and source reference are recorded in `prompts/sov_nuclear_decision_device_disablement.md`.

The prior sources, previews, and exact previous runtime DDS files are preserved under `source_png/preexisting/`, `previous/processed_png/`, and `previous/runtime_dds/`.

## Transparency and processing

The initial bomber and medal ImageGen results were opaque checkerboard images with alpha fixed at 255. They were not used as final art. Following the asset skill fallback order, each was sent through a focused built-in ImageGen edit that changed only the background to real transparency and retained the depicted subject. The untouched opaque outputs remain archived.

The selected edited PNGs contain zero-alpha unused canvas and intact painted subjects. The device-disablement source already has native transparency. Processed PNGs use premultiplied-alpha Lanczos resizing and retain the exact runtime canvas; the transparent outer canvas remains zero-alpha.

The delivery-preparation preview is framed to 28x23 subject pixels at `(2,4)` on 33x32; low-level exterior residue below alpha 8 was cleared, and pixels with alpha at least 128 were set to 255 so the small painted silhouette remains solid. Its final subject alpha mean is 203.35.

The device-disablement preview uses the complete source bounds at alpha 16, resized with aspect preserved to 28x22 and centered at `(2,5)` on 33x32. Its final subject alpha mean is 226.859.

The broken-chain preview uses the complete edited-source bounds at alpha 8, resized with aspect preserved to 51x61 and centered at `(4,3)` on 60x68. Its final subject alpha mean is 239.208.

The accepted processed previews are in `processed_png/`; the canonical DDS writer outputs are staged in `candidate_dds/processed_png/` and copied byte-for-byte to their exact runtime destinations.

## Alpha and defringe review

The `.tools/gfx` alpha report found genuine zero-alpha canvas in all three processed previews, alpha maximum 255, subject alpha means of 203.35, 226.859, and 239.208, and zero detected chroma-edge pixels.

A non-erosive `.tools/gfx` `defringe --erosion 0` probe was made and reviewed against white and navy composites. It preserved alpha but made no visible improvement; no edge contamination or halo was visible, so the probe outputs were not promoted. The approved DDS files preserve their reviewed source RGB and alpha instead of shrinking their small silhouettes.

The native and 4x nearest-neighbour pre-promotion sheets are `contact_sheets/icon_replacements_native_20261006.png` and `contact_sheets/icon_replacements_4x_20261006.png`. They compare prior runtime DDS files to candidate DDS files over checkerboard, white, and navy grounds and include alpha masks.

The 4x defringe probe comparison is `contact_sheets/defringe_probe_comparison_4x_20261006.png`.

## Achievement grey and red-X cross-cutting audit

The seven current selected achievement triplets were audited from the selected v1/v2 replacement source folders named in `docs/assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md`.

All seven selected grey source layers are exact grayscale derivations of their selected color source; all seven selected not-eligible layers equal the grey source composited with the unchanged canonical red-X overlay. The unchanged achievement backgrounds and overlay match their canonical SHA-256 hashes.

The canonical `process_achievement_icons.py --audit` passed all seven selected triplets directly against `gfx/achievements/`; strict decoded pixels and bytes match the selected candidate DDS files for all 21 runtime states. All 21 stable GFX aliases still resolve to the exact achievement IDs and filenames.

The runtime triplet sheets are `contact_sheets/achievement_runtime_grey_x_native_20261006.png` and `contact_sheets/achievement_runtime_grey_x_4x_20261006.png`. No achievement runtime DDS was modified in this takeover because the selected grey/X states pass.

Detailed alpha, size, processor, selected-source, runtime hash, and achievement-state audit records are under `evidence/`.

## Review and limits

The parent reviewed both native and 4x candidate sheets and approved all three icon replacements. The parent described the bomber as clearer with warm highlights, the disablement symbol as enlarged with a safe margin, and the broken-chain badge as family-matched with clean edges on white and navy.

This records static asset review and exact DDS promotion only. No game was launched, and live HOI4 consumer rendering remains pending user review.

The parent owns any later GFX or gameplay wiring changes; no `.gfx`, `.gui`, gameplay, or localisation source was edited in this takeover.
