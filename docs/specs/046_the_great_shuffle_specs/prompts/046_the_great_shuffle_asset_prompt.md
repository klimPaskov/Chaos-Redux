# Event 046 asset production prompt

Create the complete authorized visual asset package for Chaos Redux Event 046, **The Great Shuffle**.

Read `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and the Event 046 specification pack before producing files.

Use the narrow asset subagents with context-complete prompts and no inherited conversation context.

Use `chaosx_generated_event_art` for the report image and `chaosx_icon_artist` for achievement icons.

Do not route character work to either agent because Event 46 has no portraits.

## Authorized asset inventory

### Report-event image

Create one full-canvas report-event image.

Proposed source basename: `046_the_great_shuffle_report`.

Proposed runtime folder: `gfx/event_pictures/046_the_great_shuffle/`.

Proposed sprite identity: `GFX_chaosx_046_the_great_shuffle_report`.

Inspect the canonical report-event reference family and the live Event 46 report consumer before locking the final canvas, crop, DDS format, sprite path, and `.gfx` handoff.

The expected family is the ordinary HOI4 report-event image, but installed vanilla and current Chaos Redux precedent are authoritative.

Source mode is generated.

The image should look like period documentary photography from the late 1930s or early 1940s.

Show a familiar civic or industrial scene made impossible through mismatched population, factories, transport, military stores, and public space.

Keep one readable central subject.

Use period clothing, vehicles, machinery, buildings, photographic exposure, grain, contrast, and framing.

Avoid modern equipment, modern streets, readable generated text, clean maps, flags arranged as a collage, game UI, ledgers, staff tables, card-game art, cinematic color grading, and generic officers studying a map.

This is a deliberate full-canvas scene.

Do not request transparency.

Preserve the generated source PNG, prompt, processed preview, final DDS, contact sheet, manifest row, and GFX handoff.

### Achievement icon packages

Create a separate achievement icon package for each exact working achievement ID:

- `chaosx_046_shuffle_veteran`
- `chaosx_046_from_empty_depots`
- `chaosx_046_impossible_geography`
- `chaosx_046_government_rebuilt`
- `chaosx_046_world_redealt`
- `chaosx_046_three_reversals`

Achievement files belong directly under `gfx/achievements/` and must match the full achievement IDs and the current root-only engine convention.

Inspect the installed vanilla achievement definitions, textures, canonical achievement reference family, frame treatment, final native size, variant suffixes, and background or alpha behavior before production.

Create every state required by the current achievement system, normally the completed icon, grey icon, and not-eligible icon.

Use these exact visual directions:

1. `chaosx_046_shuffle_veteran` shows a battered globe or national seal assembled from five misaligned layers.
2. `chaosx_046_from_empty_depots` shows an empty warehouse opening onto restored crates, fuel drums, and rail supply.
3. `chaosx_046_impossible_geography` contrasts a crowded city with an empty industrial skyline across a broken survey line.
4. `chaosx_046_government_rebuilt` shows a cracked parliament or cabinet chamber restored through mismatched symbols.
5. `chaosx_046_world_redealt` combines a globe, factory, soldier, and government seal in one forceful circular rearrangement.
6. `chaosx_046_three_reversals` shows one national silhouette moving through high, low, and high positions across three shuffled layers.

Every achievement icon needs its own source artwork.

Do not resize the report image, reuse one icon under another name, recolor a single master into six identities, or assemble final art from primitive local shapes.

Generated icons must retain visible ImageGen source evidence, prompt notes, exact asset type, source mode, contact sheet, final alignment review, and variant-generation evidence.

Use native transparency only when the inspected achievement reference family uses transparent unused canvas.

Do not assume that icons follow the transparency rules of decision or idea icons.

## Working and final folders

Use `docs/assets/046_the_great_shuffle/` as the temporary source, prompt, preview, contact-sheet, manifest, and handoff workspace.

Keep final runtime DDS files in the engine-facing paths.

No runtime reference may point into `docs/assets/`.

Before the overall event can be complete, promote durable provenance, prompt, coverage, review, and sprite-handoff facts into permanent Event 046 documentation, then delete the complete temporary Event 046 asset workspace.

Retain it while the event remains blocked, awaiting review, or incomplete.

## Manifest and QA

Record for every asset:

- exact asset type
- source mode
- prompt and source evidence
- reference folder and installed vanilla precedent inspected
- source PNG checksum
- processed PNG checksum
- final DDS checksum
- native and final dimensions
- background or alpha mode
- runtime path
- proposed sprite or achievement consumer
- review state
- blocked or pending reason

Create a labeled contact sheet showing final size, alignment, framing, and all achievement variants.

Check the report art at its actual event size and every icon at its actual achievement size.

Reject unreadable silhouettes, white matte, fake transparency, halos, opaque squares where the reference is transparent, text artifacts, wrong era objects, drifted variants, and weak icon separation.

## Scope boundary

Do not create a super-event image, audio, portrait, flag, decision icon, focus icon, idea icon, category image, cluster icon, animation, 3D model, counter, or unit sound.

A cluster icon can be added only after the parent proves that the current cluster UI has a real per-cluster icon consumer and explicitly expands this brief.

Do not edit gameplay, event, cluster, achievement, localisation, GUI, or workbook files.

Write the asset manifest and `gfx_handoff.md` under the Event 046 temporary workspace and provide the parent with exact final paths, checksums, proposed sprite definitions, and any blocker.
