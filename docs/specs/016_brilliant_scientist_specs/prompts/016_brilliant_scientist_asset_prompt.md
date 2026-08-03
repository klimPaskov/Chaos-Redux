# Asset production prompt for Event 016 Brilliant Scientist

> Superseded continuation note (2026-08-03): the production inventory below is a historical planning prompt. The current asset manifest records the produced and registered 2D packages, including the complete 21-icon KRG country-idea extension. Do not rerun broad asset production from this prompt. Use `docs/assets/016_brilliant_scientist/manifest.md` and `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` for current status. External Stage-0 portrait rights, targeted or live acceptance, and the no-model boundary remain open.

The binding inventory is six super-event images, seventeen achievement icon triplets, and five severe portrait animation package families. All remain required. Stage 0 alone is complete and registered. Every super-event image, achievement icon, later portrait source and runtime file, severe animation package, flag, project icon, UI asset, report image, and news image remains unproduced and unwired.

Use this prompt with the correct narrow Chaos Redux asset subagents. Spawn every project subagent with `fork_context=false`.

## Source design

Read:

- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_9_assets_animation_and_localisation.md`
- `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_3_project_portfolio.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_5_kruger_state_country_package.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_6_kruger_state_focus_tree.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_8_super_events_world_end_and_aftermath.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md` for animated work

## Routing

Use `chaosx_generated_event_art` for fictional Kruger portraits, fictional report and news scenes, super-event art, Kruger State flags, faction emblems, and UI thematic art.

Use `chaosx_icon_artist` for focus, idea, national spirit, decision, decision category, achievement, tech, special-project, focus-filter, and animated small UI icons.

Use `chaosx_asset_source_researcher` only when an asset must depict real historical material or when locating the approved base portrait source. Doctor Warren Kruger is fictional and must not be presented as a real historical person.

## Base Kruger portrait

Do not recreate Stage 0. The approved `portrait_generic_biowarfare_europe_male_01` source, immutable Event 016 copy, processed leader and advisor PNGs, runtime leader and advisor DDS files, and sprite registrations are complete. Preserve the established face and use the registered identifiers `GFX_portrait_KRG_doctor_warren_kruger_stage_0` and `GFX_idea_doctor_warren_kruger_stage_0` as the identity baseline.

The external redistribution rights of the copied base remain unresolved because the tracked source has no standalone licence metadata. Internal Event 016 use is explicitly user-authorized. Do not describe the base as public domain or externally cleared.

Create synchronized portrait states for:

- Stage 0 appointment, already complete and used as the identity reference.
- Stage I national figure.
- Stage II international target.
- Stage III forbidden science, with route hints.
- Stage IV clone, machine, temporal, xenobiological or alien, and synthesis variants.

Leader portrait target is 156x210. Advisor and scientist surfaces must be composed for their verified UI sizes rather than blindly resizing the leader portrait.

Stage I through IV static and animated sprite contracts are pre-registered in `interface/016_brilliant_scientist.gfx`. Registration is a filename contract, not evidence that those assets exist. Produce the exact missing files named by the live contracts and do not rename the sprites without parent approval.

## Required visual families

Produce the complete inventory in `matrices/016_asset_inventory.md`.

At minimum:

- Kruger portrait and advisor or scientist progression.
- 15 project-family icon sets.
- Host management, foreign contest, sovereignty, recovery, Kruger State, project-army, submission, and singularity category art.
- Focus icon families for the 85 to 115 focus tree.
- Idea and spirit icons for every staged institution.
- Decision icons for facilities, projects, security, foreign actions, confrontation, armies, integration, and singularity.
- All 17 achievement icon triplets, for 51 final DDS files.
- Base and implemented route flags at 82x52, 41x26, and 10x7.
- Kruger faction emblem.
- Report scenes at 210x176 with the repository sepia report-card treatment.
- News scenes at 397x153 in black and white.
- Super-event images at 457x328.
- Directorate interface background, panels, project cards, facility cards, meters, state frames, and warning surfaces.

## Source and style rules

Inspect the matching reference folders under `.agents/skills/chaos-redux-event-assets/assets/` before creating each asset type.

Keep World War II visual technology, clothing, vehicles, architecture, laboratories, and press composition. No modern props, readable generated text, watermarks, fake UI, film stills, reenactments, or generic cinematic color grading.

Focus, idea, decision, achievement, tech, and category icons require separate source art designed for their target sizes. Do not satisfy one icon type by resizing another.

Flags must remain readable at 10x7. Create only actual route variants. Validate TGA orientation and vanilla header convention.

## Output package

Use `docs/assets/016_brilliant_scientist/` for source, prompt, processed, contact-sheet, manifest, and handoff material. Put final game assets in event-scoped gameplay folders following the asset skill.

Every asset entry must include:

- Asset name and related script ID or working role.
- Asset type and target size.
- Source mode.
- Prompt or source URL.
- Source author, archive, date, and license when sourced.
- Source PNG.
- Processed PNG.
- Final DDS or TGA.
- Proposed sprite name.
- Suggested GFX file.
- Related event, project, focus, idea, decision, achievement, country identity, or UI state.
- Status and uncertainty.

Create contact sheets for each large family. Create `gfx_handoff.md` with ready-to-review paths and sprite names. Do not edit gameplay, GFX, GUI, localisation, focus, decision, country, event, or spreadsheet files.

Mark every requested asset `complete`, `blocked`, or `needs_user_review`. Do not substitute placeholders.
