# Produce the Fuel Crisis visual package

Read Part 4 in full, then the other specification parts, implementation handoff, achievement prompt, and final review record under `docs/specs/109_fuel_crisis_specs/`. Follow current `AGENTS.md`, event-assets, subagents, and the assigned non-portrait role profile. This is a future production handoff. Planning created directions, not finished images.

The parent owns final non-portrait GFX registration and shared consumer wiring. Spawn `chaosx_generated_event_art` for the scene and `chaosx_icon_artist` for the achievement, each with `fork_turns="none"`, current profile settings, exact allowed paths, and explicit consumer and evidence requirements. Source research, if needed to ground period equipment, does not change the selected generated source mode.

## Lock the consumers before production

Inspect the current owner `assets/gfx_references/` README, CATALOG, matching contact sheets, and individual report, news, and achievement references. Verify the actual source consumers, GFX definitions, lookup keys, dimensions, and alpha behavior. These reference assets are for review and must not become runtime output.

| Required row | Final consumer and canvas | Proposed final path |
| --- | --- | --- |
| News scene | One native news announcement, 397x153 | `gfx/event_pictures/109_fuel_crisis/news_event_109_fuel_crisis.dds` |
| Shared report scene | Verified existing shared-log report slot, 210x176 RGBA | `gfx/event_pictures/109_fuel_crisis/report_event_109_fuel_crisis.dds` |
| Achievement completed | Existing achievement UI, 64x64 | `gfx/achievements/109_fuel_crisis_running_on_empty.dds` |
| Achievement grey | Same achievement, 64x64 | `gfx/achievements/109_fuel_crisis_running_on_empty_grey.dds` |
| Achievement not eligible | Same achievement, 64x64 | `gfx/achievements/109_fuel_crisis_running_on_empty_not_eligible.dds` |

The parent must lock actual runtime names after inspecting the consumers. Preserve an existing required basename or alias. If the report slot does not exist or is incompatible, report that accepted row as blocked. Do not invent another popup or unrelated GUI surface to consume it.

## Generate one coherent period scene

Create a fictional 1936 to 1945 documentary-style photograph of an intact fuel depot with empty gauges, an idle pump or period tanker, and personnel checking the stores. The visible situation is a missing reserve inside undamaged infrastructure. Keep the cause unexplained.

Use a strong central subject with enough lateral context for the news crop and a meaningful narrower report crop. Period clothing, equipment, and vehicles should support the scene. Exclude fire, wreckage, broken refineries, sabotage clues, conspicuous national symbols, identifiable real people, modern equipment, readable generated text, fake UI, and cinematic color grading.

Use the available native image-generation route, with no invented backend selector. Preserve the actual request and any input reference roles. Clearly identify the scene as generated rather than an archival record. Retain the unmodified returned source, dimensions, hashes, candidate lineage, selected result, and rejection reasons for rejected candidates where relevant.

Generate the scene itself first. Do not ask the image model to render the final tilted report card, its paper border, or shadow.

## Process and verify both scene outputs

Use the current `process_report_event_image.py` workflow for the 210x176 report card. Apply the owner-required documentary treatment, subtle sepia, tilt, paper edge, transparent margin, and soft shadow locally. Keep the complete image edge inside the canvas. Reject opaque corners, black padding, clipped photo edges, or a heavy artificial frame.

Create a separate panoramic black-and-white 397x153 news crop. Preserve the evidence of empty stores at native size. Do not use the report texture as the news texture or the reverse. Record crop coordinates and source-to-output mapping for each.

Convert the scene outputs through the current owner `convert_to_dds.py` route using its required strict 2D BGRA8888 output. Decode the final DDS files and inspect exact dimensions, content, alpha where relevant, and native-size legibility. Review both crops together and inside their actual rendered consumers. A good source master or a successful converter exit does not establish consumer acceptance.

## Produce the achievement triplet

The proposed achievement key is `109_fuel_crisis_running_on_empty`. Running on Empty is a working label, not final localisation. The icon subject is an original compact empty period fuel can with a restored supply hose, using a readable silhouette and subdued industrial materials. It must work at 64x64 without text, a scene thumbnail, a fake gauge UI, or a copied icon.

Inspect `assets/gfx_references/icons/achievements/contact_sheet.png`, relevant examples, the owning UI, and immutable template inputs in `assets/gfx_references/icons/achievements/template/`. Verify the owner-recorded hashes for `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png`. Do not modify those inputs.

Generate one original transparent color subject without a square background, achievement frame, red cross, lettering, or fake checkerboard. Prepare the centered native-size subject. Derive its grey variant deterministically with identical position, canvas, and alpha. Apply the unchanged overlay to that grey source at the specified alignment for the not-eligible source.

Pass the complete color, grey, and not-eligible source triplet through the current `process_achievement_icons.py` workflow. Preserve the exact supplied completed and grey background composition. Do not independently run a generic single-image converter on these final states. Do not generate three unrelated paintings.

Keep root-only runtime placement under `gfx/achievements/`. Retain the original generated subject, request, processed sources, immutable-template checks, composite PNGs, decoded final DDS states, native-size contact sheet, exact hashes, and consumer mapping.

## Return an accepted asset handoff

While work is active, use `docs/assets/109_fuel_crisis/` for sources, prompts, processing evidence, previews, manifests, and the GFX handoff. Preserve the owner cleanup and permanent-provenance rules at full event completion. Blocked work keeps its evidence.

Return one requirement-to-runtime crosswalk covering each of the five required outputs, accepted design basis, source family, final path, actual registry or sprite, actual consumer, final dimensions and hashes, decoded previews, parent review, and disposition. Count inventory, aliases, consumption, and accepted coverage separately.

Do not claim complete visual delivery from PNGs, unreviewed DDS files, missing achievement states, guessed consumers, or an unverified report slot. The parent reviews the source and actual consumer evidence and integrates the final assets. The achievement's gameplay condition is a separate acceptance dependency.
