# Asset production prompt: Event 027 Doctrine Research

Create the complete static visual asset package required by the accepted Event 027 specification.

Read first:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/specs/027_doctrine_research_specs/027_doctrine_research_spec_part_4_presentation_assets_achievements.md`
- the current event implementation and registered asset identities supplied by the parent

Use the correct project subagent for each asset family. Spawn all project subagents with `fork_context=false` and pass every path and constraint explicitly.

## Asset family 1: Doctrine Research report image

Route this family to `chaosx_generated_event_art`.

### Required asset

- stable asset slug: `027_doctrine_research_report`
- asset type: report-event image
- source mode: generated period-authentic documentary scene
- recommended runtime path: `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`
- recommended sprite: `GFX_report_event_027_doctrine_research`
- target canvas: inspect the active Chaos Redux report-event consumer and canonical report reference before production. Use `210x176` only when the current local precedent confirms it
- target GFX file: parent must supply the current event-picture GFX owner after repository inspection

### Scene brief

Show a 1936 to 1945 joint-service field exercise or military-school demonstration. Use one clear instructor, officer, or observer as the focal subject. Show practical doctrine work through coordinated infantry, artillery, armored, air, and command activity. A distant naval or harbor cue may appear when it fits naturally.

Use period uniforms, weapons, radios, maps, vehicles, aircraft, buildings, photographic technology, and composition. The image should resemble documentary material from the period. Keep the event internationally neutral. Avoid a flag, insignia, or recognizable leader that makes the scene belong to one country.

Use maps, manuals, range boards, observation equipment, field telephones, or staff notes as secondary props. Do not make a command table the whole subject.

### Reject

- readable generated text
- modern uniforms, vehicles, screens, radios, weapons, or architecture
- cinematic color grading
- futuristic or holographic doctrine imagery
- collage or split-panel composition
- doctrine user-interface screenshots
- national ownership cues
- generic scientists in a laboratory
- battle carnage as the focal subject
- malformed hands, weapons, vehicles, or aircraft
- a loose generated image with no processed and runtime outputs

### Required outputs

During active production, use the event-scoped temporary workspace required by the asset skill. Produce:

- generation prompt and source-mode note
- original generated source PNG
- processed PNG at the verified report-event canvas
- final DDS through the repository converter
- native-size and enlarged review views
- manifest entry
- contact sheet when alternatives are generated
- `gfx_handoff.md` with final path, sprite identity, target GFX file, dimensions, source mode, checksum, and consumer notes

Do not edit gameplay, localization, event, GUI, GFX, spreadsheet, or doctrine files unless the parent grants that scope.

## Asset family 2: Achievement icon triplets

Route this family to `chaosx_icon_artist`.

Inspect the canonical achievement reference folder and contact sheet before generation. Follow the root achievement filename rule and the current achievement state-triplet convention.

### Achievement A

- working achievement key: `027_first_lesson`
- recommended basename: `027_doctrine_research_first_lesson`
- motif: a closed field manual opened to its first marked practical lesson, paired with a small staff-college insignia, pointer, or pencil
- meaning: a country establishes a Grand Doctrine and begins mastery in the same batch
- visual priority: the first lesson marker must remain clear at 64x64

### Achievement B

- working achievement key: `027_single_school`
- recommended basename: `027_doctrine_research_single_school`
- motif: five doctrine tabs, lesson markers, or curriculum bands converging on one military-school crest
- meaning: all five Evolution IV choices develop one branch
- visual priority: communicate five concentrated steps without tiny numerals or text
- distinction: do not imitate the official all-subdoctrine achievement icon

### Achievement C

- working achievement key: `027_joint_curriculum`
- recommended basename: `027_doctrine_research_joint_curriculum`
- motif: four service or track symbols arranged around one central curriculum binder, compass, or staff-college crest
- meaning: one evolved batch advances four distinct tracks
- visual priority: the four-part structure should remain readable and balanced

### Required states for every achievement

- completed
- grey or locked
- not eligible

Use the repository achievement overlay and state-production workflow. Do not satisfy one achievement by recoloring or resizing another. Each achievement needs its own source art, prompt, crop, manifest entry, and final triplet.

### Required outputs for every achievement

- original generated source PNG
- processed completed-state PNG
- grey-state PNG
- not-eligible-state PNG
- final DDS triplet in `gfx/achievements/`
- filename alignment with the final root achievement ID
- transparency and frame review according to the current achievement precedent
- contact sheet showing all three achievements and all states at native size and enlarged review size
- manifest entries
- `gfx_handoff.md` with final IDs, paths, checksums, dimensions, and target registry

## Existing doctrine icons

Do not generate new Army, Navy, Air, Special Forces, Chaos Warfare, Grand Doctrine, track, or subdoctrine icons for Event 027.

The parent implementation agent must inspect and reuse the verified owning doctrine sprites. Report any missing or ambiguous sprite as a blocker. Do not substitute a focus, idea, decision, or unrelated technology icon.

## Scope boundary

The accepted asset set is one report image and three achievement triplets. Keep production within this set. Static assets are sufficient for the event's presentation.

## Completion report

Return:

- files created
- final runtime paths
- proposed and confirmed sprite or achievement IDs
- dimensions
- source mode and prompts
- reference folders inspected
- checksums
- manifest paths
- handoff path
- review status for every asset
- blockers and unresolved parent-owned wiring

An asset is complete only when its source, processed PNG, final DDS, manifest, and handoff exist. Missing image-generation access, missing reference assets, uncertain target dimensions, failed conversion, or unresolved achievement identity is a blocker. Do not use a placeholder or unrelated asset.
