# Event 066 Abundance Asset Prompt

Create the final visual asset package for Event 66 Abundance under the rules in `chaos-redux-event-assets`.
Use the project subagents with `fork_context=false` and bounded prompts.
Use `chaosx_generated_event_art` for the report image and `chaosx_icon_artist` for achievement icons.
The required visual scope is one report image and three achievement icon families.

## Required source reading

Read:

- `docs/specs/066_abundance_specs/specs/066_abundance_spec_part_8_achievements_assets.md`
- `docs/specs/066_abundance_specs/prompts/066_abundance_achievement_prompt.md`
- `AGENTS.md`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

Inspect the exact installed game and Chaos Redux consumer before final processing.
Inspect these canonical reference families first:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/`

Review each folder's contact sheet and provenance catalog.
Create the required contact sheet and update the skill-local reference documentation only when the canonical sheet is genuinely missing.
Do not wire reference images into runtime files.

## Asset 1: Event report image

- Asset type: report event image
- Source mode: generated fictional documentary scene
- Target size: `210x176`
- Suggested source basename: `abundance_report_source.png`
- Processed preview: `abundance_report_210x176.png`
- Final path: `gfx/event_pictures/066_abundance/abundance_report.dds`
- Suggested sprite: `GFX_report_event_066_abundance`

Create a late 1930s or early 1940s documentary-style scene inside an administrative warehouse or rail depot.
Several kinds of surplus should overwhelm the same space, including crates, fuel drums, sacks, files, coins, military supplies, and industrial parts.
Workers and clerks should provide human scale and show that normal measurement has failed.
The image must represent broad excess without making one resource the definitive identity of Event 66.

Use period clothing, period architecture, period containers, documentary composition, restrained monochrome or sepia treatment, and the current report-event border and crop pattern.
Avoid readable text, modern equipment, modern uniforms, digital devices, glossy cinematic grading, a map as the main subject, conference-table staging, fantasy creatures, a giant literal cornucopia, or a primitive locally assembled collage.

## Assets 2 through 4: Achievement completed icons

Create separate 64x64 completed artwork for:

### `chaosx_066_poisoned_plenty`

An overflowing period vessel or cornucopia releases a dark harmful substance while a hand or tool closes the source.
Keep the composition readable and avoid gore, modern hazard signs, text, and medical-cross shorthand.

### `chaosx_066_full_ledger`

A period ledger bursts with a small number of clear category symbols, such as fuel, industry, grain, military command, and an abstract gauge.
Use one strong silhouette and avoid tiny clutter.

### `chaosx_066_threefold_surplus`

Three distinct overflowing vessels or containers surround one central ring.
Use visibly different material cues, such as liquid, documents, and mechanical parts.

Each icon needs its own source artwork and composition.
Do not resize or crop the report image.
Do not derive one achievement icon from another.

Follow the current root-only achievement filename convention:

- `gfx/achievements/chaosx_066_poisoned_plenty.dds`
- `gfx/achievements/chaosx_066_full_ledger.dds`
- `gfx/achievements/chaosx_066_threefold_surplus.dds`

Create grey and not-eligible variants only through the verified current achievement pattern and exact full achievement IDs.
Preserve the required overlay, alpha, frame, and naming behavior found in the current consumer.

## Temporary workspace and manifest

Use `docs/assets/066_abundance/` as the temporary source and evidence workspace while production is active.
Keep generated source PNGs, prompts, processed previews, comparison sheets, contact sheets, DDS files, checksums, reference notes, and `gfx_handoff.md` there.
Move final runtime files to the engine folders listed above.

The manifest must record:

- asset identity and type
- source mode and exact prompt
- reference family inspected
- native and final dimensions
- crop and processing notes
- final runtime path
- suggested sprite identity where applicable
- source and final checksums
- reviewer status
- achievement state coverage
- any fallback background handling
- blocked or review-needed items

Before event completion, promote durable provenance and handoff facts into permanent Event 66 documentation, verify that no runtime path points into `docs/assets/`, then delete the complete temporary Event 66 workspace.

## Acceptance

Reject generated text, modern props, wrong era, opaque square icon mistakes, weak small-size readability, primitive local drawings, asset-type reuse, missing achievement states, incorrect root paths, and undocumented processing.
Return a handoff under `docs/plans/066_abundance_plans/subagent_handoffs/` with files, paths, checksums, reference evidence, review results, and remaining blockers.
