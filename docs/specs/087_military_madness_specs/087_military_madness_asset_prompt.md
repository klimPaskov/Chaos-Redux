# Military Madness Asset Production

Produce the bounded 2D asset package for Chaos Redux Event 087, Military Madness. Read `AGENTS.md`, the event-assets and subagents skills, specification Parts 1, 5, and 6, and the achievement prompt. This assignment produces assets and handoffs. It does not change the military lottery, generate units, create portraits, or redesign shared interfaces.

## Source and ownership

Every requested scene is fictional period documentary art. Every requested icon is original symbolic art. No real person's likeness or historical photograph is requested.

Use `chaosx_generated_event_art` for the four report scenes. Use `chaosx_icon_artist` for the national spirit and the three achievement subjects and state triplets. Spawn with self-contained prompts and `fork_turns="none"` when the actual tool is available.

Use native ImageGen through the required image-generation route. Do not replace it with manually drawn final raster art. Native transparency is the initial route for icon subjects. Do not fabricate transparent checkerboards, routine chroma backgrounds, or clipped alpha edges.

Use the one canonical reference root:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\gfx_references`

Read its README, catalog, and matching contact sheets before production. Inspect `icons/ideas/`, `icons/achievements/`, and the exact report family specified by the catalog. These reference assets were not supplied to or visually reviewed by the planning chat. Missing references remain a blocker.

## Four report images

Generate full-canvas fictional period photographs first. Do not ask ImageGen to paint the finished tilted paper card, transparent corners, or a UI frame.

1. `report_event_military_madness`: a close military test scene with an analog measuring instrument pushed beyond its expected range and a field exercise behind it. Keep the subject clear at small size and generate no readable digits or labels.
2. `report_event_military_insanity`: an implausibly successful combined field exercise, with one dominant main action and a few supporting period details. Do not create a collage of icons or an unreadable mass of equipment.
3. `report_event_impossible_warfare`: a period force moving with extraordinary ease through visibly severe terrain or weather. The picture represents potential situational advantages, not a guaranteed local roll.
4. `report_event_gods_of_war`: overwhelming coordinated military movement across a vast period battlefield, with confidence and scale that exceed ordinary expectations. No literal gods, modern electronics, fantasy armor, or newly invented unit family.

Use a 1936–1945 material world. Clothing, vehicles, tools, architecture, and photographic composition must fit that boundary. Use no readable text, watermarks, UI fragments, modern optics, meme styling, or recognizable public figure.

Apply `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` to the approved scene. Deliver the established 210x176 black-and-white sepia RGBA card with slight tilt, real transparent edge space, and its documented soft shadow.

Convert through the required repository DDS route and verify the decoded output. Final paths:

- `gfx/event_pictures/087_military_madness/report_event_military_madness.dds`
- `gfx/event_pictures/087_military_madness/report_event_military_insanity.dds`
- `gfx/event_pictures/087_military_madness/report_event_impossible_warfare.dds`
- `gfx/event_pictures/087_military_madness/report_event_gods_of_war.dds`

Proposed sprites follow the same basenames with the `GFX_` prefix. The parent verifies and performs final event/GFX wiring.

## One national-spirit icon

Produce `idea_military_madness` at 64x64. Use a damaged military chronometer or an overdriven mechanical gauge with a compact martial silhouette. A restrained baton or similar period military element may support the main object.

The icon must read as a temporary impossible military advantage, not as a technology unlock. Use aged material, strong value contrast, a clear silhouette, native alpha, and no text, focus-frame medallion, giant border, modern digital display, or tiny illegible detail.

Final path:

`gfx/interface/ideas/087_military_madness/idea_military_madness.dds`

Proposed sprite:

`GFX_idea_military_madness`

There is one spirit icon for the combined effect. Do not create one icon for each possible roll, duplicate, package, or tier.

## Three achievement subjects

Read the exact objectives in Part 6 before composition. Produce one original transparent subject for each exact proposed registry ID:

- `087_military_madness_minor_major_offensive`: a small standard overcoming a much larger fortress or military symbol.
- `087_military_madness_core_recovery`: a damaged homeland shield restored around a firmly planted standard.
- `087_military_madness_hold_after_expiry`: a stopped chronometer beside a still-held standard and intact position.

Inspect the achievement contact sheet and matching references. Request no frame, square background, red cross, writing, or checkerboard in the generated subject.

Follow the current [achievement creation and processing contract](../../../.agents/skills/chaos-redux-event-assets/SKILL.md#achievement-icons) for the original transparent subject, immutable templates, complete three-state source set, canonical processor and native-size review.
Keep source layers separate from outputs and retain the same subject and alignment in all three states.

Final files belong directly under `gfx/achievements/` as `<exact_id>.dds`, `<exact_id>_grey.dds`, and `<exact_id>_not_eligible.dds`. These are the engine-facing root lookup exception. There is no event subfolder here.

## Evidence and acceptance

Use an event-owned working asset folder at `docs/assets/087_military_madness/` during production. Preserve approved source PNGs, exact prompts, selected candidate lineage, processed PNGs, hashes, runtime derivatives, native-size contact sheets, and the source-to-consumer manifest.

Require the documented strict legacy BGRA DDS format and exact decoded-pixel round-trip equality. Report images must retain their correct 210x176 card and alpha treatment. Spirit and achievement outputs must remain exactly 64x64.

For achievement states, prove template and overlay integrity and exact alpha-compositing equality. Review all three states together at native size.

Return a `gfx_handoff.md` with each final path, proposed sprite or exact achievement lookup ID, dimensions, source mode, hashes, status, and parent-owned wiring requirement. Place the agent handoff under `docs/plans/087_military_madness_plans/subagent_handoffs/`.

All fourteen runtime textures require their own coverage row. A preview, plausible filename, or generated source does not establish a finished runtime asset.

No portrait, flag, focus icon, custom unit counter, animation, 3D model, new audio, or super-event asset is authorized by this brief. The dedicated read-only ledger uses verified native interface elements. Any genuine missing visual requirement must be reported, not replaced by invented final art.

Mark each requested asset complete, blocked, or needs_user_review with evidence. Do not claim in-game completion. The parent owns integration and the user provides live consumer validation.
