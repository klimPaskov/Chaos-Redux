# Asset Prompt: Event 24 Video Game in Sweden

Create the complete visual asset package required by the Event 24 specifications under:

`docs/specs/024_video_game_in_sweden_specs/`

Read and follow `AGENTS.md`, `chaos-redux-event-assets`, and `chaos-redux-subagents`. Produce the complete authorized static asset inventory below.

Use `fork_context=false` for every project asset subagent. Pass every constraint from this file explicitly.

## Event identity

- Event ID: 24
- Event slug: `video_game_in_sweden`
- Setting: Sweden during the 1936 to 1945 visual period
- Subject: An alternate-history electromechanical grand-strategy war game used by officers and later by the public
- Source rule: Generated fictional and alternate-history art through ImageGen
- Asset inventory rule: The asset rows in this prompt are exhaustive

The technology is deliberately anachronistic. Clothing, room design, photography, furniture, maps, paper, machinery, and military details must remain period-authentic.

## Required reference inspection

Before production, inspect the exact canonical reference family and its contact sheet for each asset type:

- Report art: `assets/vanilla_reference/event_art/report/`
- Decision category picture: `assets/vanilla_reference/icons/decision_categories/pictures/`
- Ideas: `assets/vanilla_reference/icons/ideas/`
- Decisions: `assets/vanilla_reference/icons/decisions/`
- Commander traits: `assets/vanilla_reference/icons/commander_traits/`
- Achievements: `assets/vanilla_reference/icons/achievements/`

For the decision category picture family, require:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference\icons\decision_categories\pictures`

If `contact_sheet.png` is missing, create it from the reference images, label filenames and native dimensions, and update the reference README and catalog before production. Reference assets are review material and must not be shipped, recolored, traced, or wired.

Follow each reference path to its installed-vanilla consumer when the active canvas or sprite behavior is uncertain.

## Temporary workspace

Use:

`docs/assets/024_video_game_in_sweden/`

Required active-work structure:

```text
docs/assets/024_video_game_in_sweden/
  manifest.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  notes/
  gfx_handoff.md
```

Keep source prompts and generated source files. Final runtime DDS files must move to engine-facing folders. Before the event is fully complete, promote durable provenance, prompt, review, coverage, and wiring facts into permanent event or plan documentation, confirm no runtime reference points into `docs/assets/`, then delete the temporary event workspace.

## Visual language

Core motifs:

- Wall-sized projected or illuminated strategy maps
- Relay cabinets and switchboards
- Punched cards and printed scenario sheets
- Teleprinters, telephone lines, plotting tools, and mechanical counters
- Swedish officers, civilian engineers, referees, teachers, and club members
- Brass, dark wood, painted steel, paper maps, and restrained period lighting

Avoid:

- Modern monitors, laptops, plastic keyboards, game controllers, LED lighting, neon arcades, headsets, or modern server racks
- Modern uniforms, weapons, furniture, streets, or office design
- Readable generated text
- UI overlays or fake in-game interfaces
- Waving flags, modern Swedish logos, or invented insignia
- Modern esports imagery
- Comic or meme treatment
- A map-only image with no active human or mechanical subject

## Asset A1: Main report image

Working filename:

`024_video_game_in_sweden_report_release.dds`

Proposed runtime folder:

`gfx/event_pictures/024_video_game_in_sweden/`

Target canvas:

- `210x176`, subject to verification against the exact report-event consumer

Source mode:

- Generated period-documentary image

Scene:

A Swedish military room during the late 1930s or early 1940s. Officers and civilian engineers gather around a large projected strategy map and mechanical plotting table. Relay cabinets, punched cards, teleprinters, wooden counters, cables, and printed charts show how the machine works. The group is attentive and professionally curious. The scene should look like a contemporary press photograph, with realistic monochrome or restrained period photographic treatment.

The image should communicate invention, practical military interest, and the possibility of institutional fascination.

Suggested sprite:

`GFX_report_event_024_video_game_in_sweden_release`

## Asset A2: Static decision category picture

Working filename:

`024_video_game_in_sweden_category.dds`

Proposed runtime folder:

`gfx/interface/decisions/024_video_game_in_sweden/`

Reference canvas:

- The canonical family currently uses `114x101` examples, but verify the active consumer before final output

Source mode:

- Generated static category picture

Composition:

A close view of the operating apparatus. Show a map projection, relay or switchboard hardware, punched cards, printed scenario sheets, and plotting counters. Include human hands or partial operators so the scene feels active. Keep the composition readable behind normal decision-category text.

Do not paint buttons, meters, values, frames, or fake controls into the picture.

Suggested sprite:

`GFX_decision_category_picture_024_video_game_in_sweden`

## Idea icon family

Create each idea icon as separate source artwork designed for the `64x64` idea surface. Coordinate the motifs while changing the subject and silhouette for each stage.

### A3: Experimental War Game

Filename:

`024_video_game_in_sweden_idea_experimental.dds`

Direction:

A compact relay box, folded military map, and one plotting counter. The icon should feel exploratory and controlled.

Suggested sprite:

`GFX_idea_024_video_game_in_sweden_experimental`

### A4: Gamified Staff Culture

Filename:

`024_video_game_in_sweden_idea_staff_culture.dds`

Direction:

Officer cap, score or ranking markers without readable text, and competing map arrows. The icon should show professional competition.

Suggested sprite:

`GFX_idea_024_video_game_in_sweden_staff_culture`

### A5: National Strategy Craze

Filename:

`024_video_game_in_sweden_idea_national_craze.dds`

Direction:

Several civilian hands around a map board, club tokens, and a simplified relay display. The icon should show broad participation and crowding.

Suggested sprite:

`GFX_idea_024_video_game_in_sweden_national_craze`

### A6: Simulation Orthodoxy

Filename:

`024_video_game_in_sweden_idea_orthodoxy.dds`

Direction:

A rigid illuminated map grid or plotting table dominating a small officer silhouette. The icon should convey authority and inflexibility without supernatural imagery.

Suggested sprite:

`GFX_idea_024_video_game_in_sweden_orthodoxy`

### A7: Validated Wargaming Methods

Filename:

`024_video_game_in_sweden_idea_validated.dds`

Direction:

A field compass, muddy boot print or terrain profile, and a smaller map board. Real evidence should visibly correct abstraction.

Suggested sprite:

`GFX_idea_024_video_game_in_sweden_validated`

## Priority decision icon family

Each priority decision icon needs its own source artwork designed for `32x32`. Use strong silhouettes and minimal interior detail. Do not resize an idea icon.

### A8: Controlled staff exercise

Filename:

`024_video_game_in_sweden_decision_controlled_exercise.dds`

Motif:

Two opposing counters and a referee pointer over a map.

### A9: Logistics module

Filename:

`024_video_game_in_sweden_decision_logistics_module.dds`

Motif:

Rail line, truck or train symbol, and punch card.

### A10: Field validation

Filename:

`024_video_game_in_sweden_decision_field_validation.dds`

Motif:

Boot, compass, and map grid.

### A11: Independent red team

Filename:

`024_video_game_in_sweden_decision_red_team.dds`

Motif:

Opposing arrow or counter breaking the preferred plan. Do not use a modern red-team hacker image.

### A12: Rules revision

Filename:

`024_video_game_in_sweden_decision_rules_revision.dds`

Motif:

Printed rule sheet, mechanical gear, and corrected map symbol. No readable text.

### A13: National league season

Filename:

`024_video_game_in_sweden_decision_national_league.dds`

Motif:

Public hall, map board, and several competing tokens.

### A14: Reality Audit

Filename:

`024_video_game_in_sweden_decision_reality_audit.dds`

Motif:

Map projection compared against terrain, rail, or field compass evidence.

### A15: Trust the Model

Filename:

`024_video_game_in_sweden_decision_trust_model.dds`

Motif:

A dominant illuminated map board with rigid arrows and a small warning fracture or broken rail underneath.

Suggested sprites use this pattern:

`GFX_decision_024_video_game_in_sweden_<asset_slug>`

## Conditional decision icons

Inspect installed vanilla and existing Chaos Redux icons for these actions:

- Foreign licensing
- Dual-track staff system
- Official restriction
- Protect essential shifts
- Preparedness clubs

Reuse is allowed only when an existing icon is an exact semantic and visual match. Record the inspected source and final choice in the manifest. A generic placeholder, renamed unrelated icon, or resized Event 24 icon is unacceptable. If no exact match exists, create a separate ImageGen source and final `32x32` DDS before completion.

## Commander trait icons

Inspect the exact active commander-trait canvas and consumer. Do not assume a generic `64x64` size.

### A16: Rulebook Commander

Filename:

`024_video_game_in_sweden_trait_rulebook_commander.dds`

Direction:

Officer profile, rigid planning arrows, and a rule or scoring element without readable text. Show detailed preparation and low flexibility.

Suggested sprite:

`GFX_trait_024_video_game_in_sweden_rulebook_commander`

### A17: Retired trait icon

The user's explicit 2026-09-20 instruction removes Field-Validated Planner. The former A17 icon request is superseded; no replacement commander-trait art should be produced for field validation.

## Achievement icon triplets

Create each completed achievement icon at `64x64` and the matching grey and not-eligible variants according to the current achievement workflow. Achievement files remain directly under `gfx/achievements/` and use full achievement ids.

### A18: Reality Check

Achievement id:

`024_video_game_in_sweden_reality_check`

Completed direction:

A projected strategy map crossed by a muddy boot print, field compass, or survey notebook. Evidence corrects the clean model.

Required files:

- `024_video_game_in_sweden_reality_check.dds`
- `024_video_game_in_sweden_reality_check_grey.dds`
- `024_video_game_in_sweden_reality_check_not_eligible.dds`

### A19: According to Plan

Achievement id:

`024_video_game_in_sweden_according_to_plan`

Completed direction:

A brass plotting table with a Swedish-colored marker reaching an objective while broken rail, weather, or terrain symbols show real friction around it. Do not use readable text or a literal modern achievement badge.

Required files:

- `024_video_game_in_sweden_according_to_plan.dds`
- `024_video_game_in_sweden_according_to_plan_grey.dds`
- `024_video_game_in_sweden_according_to_plan_not_eligible.dds`

## ImageGen and processing requirements

- Save every original ImageGen source and exact prompt.
- Use real transparent backgrounds for transparent icon families.
- Remove fake checkerboards, white halos, white outlines, opaque square backgrounds, and stray pixels.
- Give small icons a restrained dark outline and subtle shadow when the matching reference family uses them.
- Keep one clear centered subject at final size.
- Preserve separate source art for each icon type.
- Convert through the repository DDS workflow and validate decoded dimensions, format, alpha, and appearance.
- Review icons at native size and enlarged nearest-neighbor scale.
- Create contact sheets for report art, category art, idea icons, decision icons, trait icons, and achievement variants.
- Do not mark an asset complete from a prompt or preview alone.

## Manifest requirements

Each entry records:

- Asset id and working name
- Event id and slug
- Asset type
- Intended consumer
- Source mode
- Exact ImageGen prompt
- Reference family and inspected examples
- Original source path and checksum
- Processed PNG path and checksum
- Final DDS path and checksum
- Native dimensions and alpha behavior
- Proposed sprite name
- Review status
- Any reuse decision and exact precedent
- Any blocker or uncertainty

## Handoff requirements

Write `gfx_handoff.md` with:

- Final DDS paths
- Proposed stable sprite names
- Target `.gfx` file or owning surface
- Canvas and frame count, always one frame here
- Transparency and format notes
- Conditional reuse findings
- Contact sheet paths
- Remaining parent-owned wiring

Asset subagents must not edit event, decision, idea, trait, achievement, GUI, localisation, scripted localisation, spreadsheet, or broad `.gfx` files unless the parent grants a narrow exception. The parent owns final non-portrait wiring and completion.

## Completion status

The asset package is complete only when every required final DDS exists, every conditional icon has an exact reuse or a newly created final asset, contact sheets and manifest evidence pass review, and no placeholder remains. Missing ImageGen access, missing reference files, failed DDS conversion, or uncertain conditional reuse must be reported as blocked and never replaced.
