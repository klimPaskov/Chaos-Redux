# Asset production handoff for Event 096

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

When separately authorized, produce the complete non-text visual package specified in `096_divisions_lock_part_6_presentation_achievements.md`.
Read that file, Parts 1 and 3, the achievement prompt, and [the current authority and workflow notes](README.md#authority-and-current-workflow).
Use the current [asset owner skill](../../../.claude/skills/chaos-redux-event-assets/SKILL.md) and [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md).
Parent acceptance within the authorized production scope controls the assignment; the original receipt is historical.
Do not inherit a superseded provisional batch or UI design from an earlier handoff.

Use `chaosx_generated_event_art` for the two original report images and `chaosx_icon_artist` for the category, actions, and achievement subjects.
Pass self-contained assignments with exact paths, consumers, modes, dimensions, references, transparency, and handoff requirements.
Use a source researcher only if the selected final art actually depends on a real documentary source.
The parent owns gameplay, shared UI, sprite integration, and final review.

## Required outputs and consumers

| Asset | Proposed sprite or consumer | Proposed runtime output |
| --- | --- | --- |
| Lock report card | `GFX_chaosx_096_report_lock` | `gfx/event_pictures/096_divisions_lock/096_report_lock.dds` |
| Release report card | `GFX_chaosx_096_report_release` | `gfx/event_pictures/096_divisions_lock/096_report_release.dds` |
| Inspection category icon | Ordinary decision category | `gfx/interface/decisions/096_divisions_lock/096_category_inspection.dds` |
| Single-removal icon | `division_inspection_disband_one` | `gfx/interface/decisions/096_divisions_lock/096_action_single.dds` |
| Batch-removal icon | `division_inspection_disband_batch` | `gfx/interface/decisions/096_divisions_lock/096_action_batch.dds` |
| Industrial-growth achievement | `chaosx_096_grow_into_army` | Completed, grey, and not-eligible files directly in `gfx/achievements/` |
| Voluntary-demobilization achievement | `chaosx_096_orderly_stand_down` | Same exact three-state naming pattern |
| Rolling-compliance achievement | `chaosx_096_inspection_proof` | Same exact three-state naming pattern |

Check these proposed paths and sprite IDs for repository collisions and the actual native naming convention.
Resolve a necessary path correction in one parent-reviewed manifest before writing consumers.
Do not silently create duplicate aliases or leave an old sprite referenced.

The planned runtime image count is fourteen: two report cards, three ordinary category/action icons, and nine achievement states.
There are eight original image subjects, since each achievement derives its other two states from one original subject.

## Reference and visual direction

Inspect the actual consuming interface and the applicable canonical reference families under `.claude/skills/chaos-redux-event-assets/assets/gfx_references/`.
The semantic reference catalog and rules are `assets/gfx_references/CATALOG.md` and `assets/gfx_references/README.md`.
The separate reusable-component catalog is `assets/visual_components/CATALOG.md`, directly beneath `assets`, not inside `gfx_references`.

The original [research receipt](096_divisions_lock_research_evidence.md) records an incorrect-path probe and later correct-path 404 results in the earlier environment.
Discover and read current skill-local references and inspect the actual consumers before production; neither those historical failures nor the prose directions establish current resource availability or visual approval.

The report source should evoke a period military office, formation files, physical inspection controls, and staff continuing to work while establishment records remain frozen.
The release scene returns to that setting with the records reopened.
Keep the subject readable at 210 by 176, without generated text, final borders, UI labels, modern objects, or a collage of multiple panels.

Generate the underlying period image first with an opaque image background.
Apply the required black-and-white and restrained sepia treatment, card tilt, shadow, and transparent corners through the canonical local processing workflow.
Preserve native card geometry and alpha.
Do not generate a fake premade screenshot of the final event UI.

Generate category and action subjects separately for their 32 by 32 icon consumers.
Single and batch actions must remain distinguishable at native size through one record versus several records, with strong silhouettes.
Do not resize a focus icon, existing achievement, or report image into a decision icon.
Request a real transparent background in the initial image-generation call (the gptimage route described in the asset skill) wherever the inspected family uses transparent unused canvas, and preserve alpha through processing.
Background removal is fallback-only under the current asset skill, with original output and edge-review evidence.

This event has an ordinary category with two actions and a compact text summary.
A category background picture is not part of the accepted output list.
If a production review proposes one, apply the canonical picture eligibility gate, explain its benefit, and update the parent-approved design and manifest.
Do not add a dedicated scripted window or animation as an asset-only choice.

## Achievement production

Apply the current [achievement production and processing contract](../../../.claude/skills/chaos-redux-event-assets/references/icon-and-ui-families.md#achievement-icons), including exact supplied template paths and hashes, unchanged overlay, deterministic state derivation, complete source triplets, canonical processor, decoded-pixel checks and required reviews.
Those mutable workflow rules are owned by that skill rather than copied here.
For each of the three exact Part 6 achievement IDs, produce one original centered transparent subject with no frame, background square, lettering, red cross or fake checkerboard.
Preserve the image-generation source and prompt, use the selected 64 by 64 consumer, and deliver all nine completed, grey and not-eligible DDS files directly in `gfx/achievements/` with exact ID and suffix names.
The parent owns shared registry, sprite, localisation and runtime integration.

## Production evidence and acceptance

Preserve original provider output, exact prompts, reference images inspected, any documentary source URL and license, source checksums, processed PNGs, processing commands, final DDS files, sprite definitions, and native-size previews.
Report the actual returned generation metadata rather than claiming a model selection the tool did not expose, and verify alpha in each saved PNG because the tool has no alpha parameter.

Verify report alpha and card corners, native icon legibility, each real consumer, every referenced path, and achievement three-state consistency.
For achievement DDS outputs, perform the skill's strict one-level 64 by 64 legacy BGRA and decoded-pixel checks against the exact background-and-subject composite.
Keep the complete source triplets, composited review PNGs, contact sheet, and processor audit output.

Parent integration must update the event GFX consumer, category/action references, `interface/chaosx_achievements.gfx`, registry definitions, and documentation together.
An asset is not complete just because a DDS exists at a proposed path.
Show its actual consumer and obtain the required native view or render evidence in the implementation environment.

Write a bounded handoff under `docs/plans/096_divisions_lock_plans/subagent_handoffs/` listing every original and final path, sprite, state, source mode, reference, processing result, parent-owned integration item, and unresolved blocker.
Do not supply final localisation, alter gameplay, or claim missing references and renders passed.
