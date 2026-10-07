# Event 085 — Visual Asset Production Prompt

Produce the complete visual package for Ten Plagues of Egypt from `docs/specs/085_ten_plagues_of_egypt_specs/`.
Read the README and all specification parts before producing assets, with particular attention to Parts 7, 16, 17, and 18.
This is a major global event with one event-specific public value, Divine Wrath, and ten distinct ordered plagues.
The current package contains art directions, not finished approved art.

Follow `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and the frame-animation skill wherever motion is actually mapped.
Read the canonical skill-local `assets/vanilla_reference/README.md`, `CATALOG.md`, matching category contact sheets, and owning native consumer definitions.
Resolve those reference paths relative to `.agents/skills/chaos-redux-event-assets/`.
Do not use a project-root imitation of that reference library or ship its review PNGs.

## Scope and source mode

Use original generated fictional period scenes for the 16 report pictures, six news pictures, four super-event pictures, and twelve triggered category pictures.
Use separately designed native-transparent symbolic artwork for the three national spirits, sixteen decision families, and twelve achievement subjects.
Sources must match a plausible interwar/wartime setting and the current event context.

Preserve the report suffixes and scene identities in Part 16.
The reports cover global Blood, the additional Nile scene, Frogs, Lice and Gnats, Flies, Livestock, Boils, Hail and Fire, Locusts, Darkness, Passover, Firstborn, Exodus, Mourning, returning Blood, and the broken cycle.
A different crop or tint of one generated image does not count as a separately composed plague scene.

The six news subjects and four super-event subjects have their own aspect-ratio compositions.
The twelve category pictures cover the ten phases, mourning, and reconstruction.
Use a mutually exclusive state-to-picture mapping.
Do not create a custom category command GUI merely to display the inventory.

## Final sizes and consumers

Reports: 210 × 176, with the skill's required local report-card processing.
News: 397 × 153, black-and-white.
Super-events: 457 × 328.
Ideas: 64 × 64.
Decision icons: 32 × 32.
Achievements: 64 × 64 for every state.
Category pictures: 114 × 101 is only the planning reference; inspect the actual consumer and lock its correct canvas before production.

The known planned static inventory is 93 final outputs.
Do not call this complete merely because 93 files exist.
Every declared asset must have the right consumer, state, shape, source quality, and final review.
The separate global Darkness presentation remains mandatory and its supported runtime provider must be resolved by the parent and relevant specialist.

No new flags, country portraits, focus icons, formable puzzles, 3D animals, or skeletal animations are in the accepted event scope.
Do not manufacture them to broaden the assignment.
Real named characters use existing identity-preserving sources; no newly invented image of a historical firstborn victim is authorized.

## Achievement triplets

For each of the twelve achievement subjects in Part 18, generate one original subject on genuine transparency, without text, frame, square background, red cross, or fake checkerboard.
Create the centered color subject at 64 × 64.
Derive a deterministic grey subject with the same alignment and alpha.
Create the not-eligible source by placing the unchanged supplied overlay on that grey source.

Verify the three supplied immutable template files and their skill-defined hashes.
Supply the complete color, grey, and not-eligible source triplet to `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`.
One source file is not valid processor input.
Keep inputs and final outputs separate.
Do not regenerate three unrelated images, redraw the cross, or run final achievement states through the ordinary converter instead.

Achievement runtime files stay directly under `gfx/achievements/`.
Their filenames must equal the final achievement IDs plus the required suffixes.
The semantic `tp85_*` keys in the design are mapped to collision-checked full event-prefixed IDs by the parent; do not invent or overwrite global IDs.

## Ordinary processing and placement

For ordinary outputs use `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
The obsolete `.tools/convert_to_dds.py` path must not be restored.
Verify the required legacy BGRA DDS format, dimensions, alpha behavior, and decoded result.

Use event-scoped folders directly under the appropriate category, such as `gfx/event_pictures/085_ten_plagues_of_egypt/`, `gfx/super_events/085_ten_plagues_of_egypt/`, `gfx/interface/ideas/085_ten_plagues_of_egypt/`, and `gfx/interface/decisions/085_ten_plagues_of_egypt/`.
Do not add another `chaos_redux/` namespace directory.
The parent resolves exact category-picture and news destinations against their existing consumers.

Keep source PNGs, generation prompts, intermediate processed files, and review contact sheets in the event's `docs/assets/085_ten_plagues_of_egypt/` workspace.
Reference images are review material, not distributed final textures.

## Delegation and review

Use the named `chaosx_generated_event_art`, `chaosx_icon_artist`, and `chaosx_asset_source_researcher` roles as appropriate.
Every Codex `collaboration.spawn_agent` call uses `fork_turns="none"` and a self-contained assignment with exact source paths, output paths, sizes, semantic IDs, constraints, and handoff path.
Do not substitute built-in general agents for named specialists.

Asset workers do not edit `.gfx` by default.
Return the manifest and `gfx_handoff.md` with exact intended sprite names, textures, consumer state conditions, and unresolved questions.
The parent performs final wiring and reviews each visual family at native size.

If the Darkness implementation introduces an explicitly event-owned GUI layer, give the UI worker its exact accepted ownership, layout reference, input behavior, resolution states, assets, and MCP comparison requirements.
Do not route shared settings, event logs, or super-event framework work to that worker.

Return all created sources and outputs, their hashes and processing details, a consumer coverage matrix, independent review evidence where required, and an honest list of unresolved items.
No placeholder art, fabricated provenance, fake animation, or good-enough size-only completion is accepted.
