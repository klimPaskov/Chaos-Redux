# Asset prompt: Event 074

Produce the visual package for Event 074, Japan Lands in USA, from `docs/specs/074_japan_lands_in_usa_specs/`.
Read the README, design Part 7, Part 8, the army and geography parts, and the source register first.
Follow the current `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and the achievement-image rules.
Use `docs/assets/074_japan_lands_in_usa/` as the evidence workspace.
Write specialist handoffs under `docs/plans/074_japan_lands_in_usa_plans/`.
The plan contains no completed images and no permission to call a future manifest an asset delivery.

## Reference gate

Read `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, the matching family contact sheets, and the exact vanilla or accepted repository consumer for every requested family.
The absolute Windows reference path in the supplied source identifies the original library location and may need resolution in the active checkout.
Read report, news, ideas, decisions, category icons, category pictures and achievement references.
For category pictures, inspect `icons/decision_categories/pictures/contact_sheet.png`.
If that required contact sheet is absent, build it from the actual reference assets with filenames and native dimensions, and update its indexes before generating category pictures.
Do not create a guessed consumer or guessed final size to bypass missing references.

## Required production inventory

Plan seven country-report and news scenes, consisting of three 210 × 176 sepia reports and four 397 × 153 black-and-white news images.
The report subjects are Japanese landing command, American mainland warning, and campaign aftermath.
The news subjects are initial landing, a wider western front, inland advance, and coastal recovery.
Use region-neutral framing where one asset must support a legal Oregon or Washington fallback.
California-only landmarks may appear only in a consumer that is actually California-specific.

Produce one 457 × 328 super-event scene showing a substantial multi-region mainland invasion, coordinated with the super-event team.
Produce four Japanese and five American 32 × 32 decision icons, five mission icons at the verified native size, two category icons and two category pictures after consumer verification, and up to two 64 × 64 event-owned spirit icons if those visible spirits are actually used.
The full planned table and conditional spirit rule are in Part 7.

Produce five distinct achievement subjects and all fifteen finished 64 × 64 state tiles.
Use the IDs and concepts in Part 8 and the achievement prompt.
Do not invent achievement titles or alter tracking rules as part of the visual task.

These requirements yield 43 planned runtime images when every family is used.
Maintain an actual asset manifest that records any accepted removal of an unused consumer.
No country flag, portrait, focus-tree icon, new unit counter, model, equipment family or animation is requested.
Do not create those files as unsolicited additions.
If real-character portrait work is separately approved, route it through `chaosx_portrait_creator` with sourced identity preservation and the proper role outputs.
If a flag is separately approved, follow the flat reference-constrained image-generation rule and cited historical design review.

## Source and art direction

Use image generation for symbolic icons and the fictional invasion scenes.
The invasion is alternate-history content, so never label its generated scene as a historical photograph.
Archival photographs can serve as sourced uniform, shipyard, transport and geography references after provenance and rights checks.
The source register's limited NPS research does not constitute a completed reference pack for every scene.
Use `chaosx_asset_source_researcher` for missing grounded references and `chaosx_generated_event_art` and `chaosx_icon_artist` for production within their allowed scopes.
Spawn specialists with `fork_turns="none"` and pass complete task context.

At native size, use a few clear subjects and avoid dense collages, embedded captions, tiny maps or generic modern equipment.
Reports follow the prescribed sepia and alpha/card treatment.
News follow the black-and-white period treatment.
Do not ask the image model to draw finished localisation or UI text inside a picture.
Static artwork is the approved presentation choice.
Do not fabricate animation by moving a flat image to claim skeletal or frame-animation work.

## Achievement-specific pipeline

Create one transparent color subject per achievement, then use `process_achievement_icons.py` with the unchanged `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png`.
Derive the gray state consistently from the accepted subject.
Do not generate three independent drawings and do not replace the templates with homemade tile backgrounds.
Final paths are directly under `gfx/achievements/` using the exact validated achievement ID, plus `_grey` and `_not_eligible` suffixes.

## Export and handoff

Use the prescribed ordinary DDS conversion pipeline for nonachievement images, including `convert_to_dds.py` and strict BGRA payload validation where the skill requires it.
Verify the actual header, dimensions, alpha, decoded appearance and consumer.
The ordinary uncompressed layout check is 128 header bytes plus four bytes per pixel when that is the prescribed output format.
An extension change is not conversion.

Deliver accepted runtime files, source/generation records, family contact sheets at native scale, proposed sprite mappings, and a manifest of completed and blocked consumers.
Final `.gfx` wiring belongs to the parent implementation agent unless it explicitly delegates that write scope.
Keep unfinished or blocked source evidence in the workspace.
Promote durable provenance and remove disposable intermediates only through the asset skill's closure rules.
Do not claim completion while required subjects, references, consumers, masks or byte checks are missing.
