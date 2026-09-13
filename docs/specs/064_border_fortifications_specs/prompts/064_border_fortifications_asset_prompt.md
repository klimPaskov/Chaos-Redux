# Asset Prompt: Event 064 Border Fortifications

Create and deliver the complete static visual asset package for Chaos Redux Event 064, Border Fortifications.

Read the full source package under `docs/specs/064_border_fortifications_specs/` before producing art. Follow `AGENTS.md`, `chaos-redux-event-assets`, the generated-event-art and icon-artist subagent definitions, current repository asset conventions, and the exact active consumer files. Use `fork_context=false` for any spawned specialist.

Do not implement gameplay script. Produce final asset files, source files, previews, manifests, and a precise `.gfx` handoff. Do not stop at prompts or mockups.

## Event visual identity

Event 064 causes finished defensive works to appear along every valid current foreign land frontier during one synchronized global incident. Later evolutions create selected strategic anchors, secondary positions, integrated Fortress States, and internal redoubts. The visual identity should communicate completed concrete defenses, period military engineering, transport support, observation, and layered geography.

The event has no confirmed national origin. Avoid flags, readable signs, named emblems, or country-specific uniforms that imply one state created the phenomenon.

Use a 1930s or 1940s material language:

- reinforced concrete bunkers and blockhouses
- firing ports and observation cups
- anti-tank obstacles
- wire and access trenches
- rail or road support
- field telephones, signal posts, crates, and inspection parties where readable
- period trucks or engineering equipment only when scale permits

Do not use modern ballistic armor, modern radar dishes, contemporary concrete barriers, digital screens, night-vision equipment, or postwar tactical gear.

## Source mode and provenance

Use generated non-portrait art for final report, category, posture, decision, and achievement images. Historical photographs can guide composition only after source and rights inspection. Do not distribute an unverified archival photograph as the final asset.

For every source or reference, record:

- source mode
- creator or model where applicable
- generation prompt and settings where applicable
- reference path or URL where project rules require it
- rights or license note
- transformations
- final consumer
- uncertainty

Generated art must be original and must not closely reproduce a distinctive protected photograph.

## Existing Event 064 audit

Inspect these current repository surfaces before generating replacements:

- `events/064_border_forts.txt`
- `localisation/english/064_border_forts_l_english.yml`
- `interface/chaosx_pictures.gfx`
- current sprite `GFX_report_event_border_fortifications`
- current texture family `gfx/event_pictures/064_border_forts/`
- current `report_event_border_fortifications.dds`
- canonical report-event image references from recently accepted Chaos Redux events
- canonical decision category pictures and icons
- canonical idea or timed-modifier icons
- canonical achievement completed, grey, and not-eligible triplets

Document whether the existing report image is retained, replaced in place, or migrated. Preserve the current sprite identity unless a documented migration is safer. Remove no shared sprite without a reference audit.

## Deliverable 1: Report event image

### Consumer

Event 064 local report.

### Identity

Preferred sprite:

`GFX_report_event_border_fortifications`

Preferred final family:

`gfx/event_pictures/064_border_forts/`

### Format

- final processed DDS
- final processed PNG preview
- source image at sufficient resolution for clean processing
- final report-event composition `210x176`
- black and white with restrained sepia treatment
- standard Chaos Redux report-card framing and transparent corners
- correct alpha and compression for the active event consumer

### Composition

Create one clear foreground defensive emplacement with a visible firing port or observation feature. Extend obstacles, trenches, and other positions through the middle distance. Include a road, railway, settlement, mountain pass, river approach, or other strategic route in the scene so the line has a reason to exist.

Show a few soldiers or engineers inspecting, mapping, or occupying completed works. Do not show an ordinary long construction site as the main action. The event should look as if the line already exists and has just been discovered or taken over.

Use atmospheric depth to imply global scale. Do not use a literal world map, repeated tiny flags, glowing magical effects, or a collage of national monuments.

### Negative constraints

- no readable text
- no flags
- no modern objects
- no tanks or aircraft dominating the frame
- no gore
- no painted user interface
- no duplicated or malformed people
- no impossible bunker geometry
- no cropped firing port that reads as an abstract black rectangle
- no flat row of identical bunkers with no strategic landscape

### Native-size review

Review at `210x176` inside the actual report window. The foreground fort, line direction, and strategic route must remain readable. Check transparent corners and edge bleed.

## Deliverable 2: Decision category picture

### Consumer

The temporary Event 064 response category.

### Size

Use the current canonical reference family and inspect the exact active consumer before locking output dimensions. The planning reference canvas is `114x101`. The live consumer is authoritative.

### Composition

Show a compact fortified sector with a transport line feeding it. Include one observation or signal position and one distant strategic objective such as a town, port, pass, or supply route.

The scene should support all three postures:

- defense through the visible line
- logistics through road or rail
- offense through a visible gap, obstacle, or surveyed approach

Keep important shapes away from interface overlays. Do not paint labels, buttons, meters, frames, or fake map markers into the image.

### Output

- source file
- processed PNG preview
- final DDS
- exact verified dimensions
- proposed sprite name
- target `.gfx` owner

## Deliverable 3: Decision category icon

Create one transparent `32x32` icon.

Working identity:

`GFX_decision_category_064_border_fortifications`

Visual direction:

- simple concrete bunker silhouette
- one clear frontier line or obstacle element
- strong outer contour
- low internal detail
- no text

Review at native size on the actual category background.

## Deliverable 4: Posture icons

Create three coordinated transparent `64x64` idea or timed-modifier icons. Do not resize the category icon.

### Integrate the Line

Working sprite:

`GFX_idea_064_integrate_the_line`

Direction:

- bunker cross-section or two linked firing positions
- contained command or coordination arrows
- stable defensive silhouette

### Keep the Roads Open

Working sprite:

`GFX_idea_064_keep_the_roads_open`

Direction:

- road or railway entering a fortified position
- small supply crate, wheel, or transport marker
- clear connection motif

### Study the Breach

Working sprite:

`GFX_idea_064_study_the_breach`

Direction:

- cracked fort plan or bunker face
- engineer wedge, tool, or concentrated arrow
- offensive study without gore

### Family rules

- shared rendering style
- distinct silhouette for each posture
- correct transparent edges
- no tiny text or flags
- no recolored duplicate base icon
- clear native-size comparison sheet

## Deliverable 5: Decision icons

Create five transparent `32x32` icons.

### Reinforce a Priority Sector

Working sprite:

`GFX_decision_064_reinforce_priority_sector`

Direction: bunker with a clear reinforcing layer, added concrete band, or sandbag section.

### Connect the New Line

Working sprite:

`GFX_decision_064_connect_new_line`

Direction: rail or road joining a fortified point. Connection must read before vehicle detail.

### Conduct Breach Exercises

Working sprite:

`GFX_decision_064_conduct_breach_exercises`

Direction: cracked fort target with engineer wedge, obstacle-clearing tool, or concentrated assault marker.

### Harden the Air and Coastal Flank

Working sprite:

`GFX_decision_064_harden_flank`

Direction: one readable fortified-flank warning symbol. Try a simplified anti-air barrel with radar arc above a coastal emplacement. If that fails at native size, use a general warning arc over a bunker and let localisation distinguish air and coastal target branches.

### Prepare a National Redoubt

Working sprite:

`GFX_decision_064_prepare_national_redoubt`

Direction: central capital citadel or star within an inner defensive ring.

### Decision icon rules

- one concept per icon
- no resized event art
- no photographic crops
- transparent background
- crisp native-size silhouette
- adequate interior contrast
- consistent family border and lighting
- no country-specific symbols

## Deliverable 6: Achievement art

Create four original completed `64x64` achievement icons, then process each through the current Chaos Redux achievement pipeline to create completed, grey, and not-eligible variants.

Inspect current achievement naming, folder, sprite, and processor conventions before naming final files.

### Continent of Concrete

Working key:

`chaosx_achievement_064_continent_of_concrete`

Direction:

- broad land or frontier arc
- linked bunker ring
- several outward threat arrows stopped at the line
- dense but readable composition

### The Line Held

Working key:

`chaosx_achievement_064_the_line_held`

Direction:

- intact short fort line
- broken assault arrows
- small protected capital or national center behind it

### Breach the Unbreachable

Working key:

`chaosx_achievement_064_breach_the_unbreachable`

Direction:

- cracked bunker
- engineer wedge or focused assault arrow through the crack
- route continuing toward a small capital symbol

### Last Redoubt

Working key:

`chaosx_achievement_064_last_redoubt`

Direction:

- central capital citadel
- linked supply node
- broken encirclement ring
- small outward recovery cue

### Achievement rules

- each completed icon has a distinct composition
- do not use one base icon with four labels or recolors
- no readable text
- no flag unless the achievement system adds a generic frame outside the art
- preserve standard achievement frame treatment
- validate all three states in the actual achievement interface

## Asset authorization boundary

Create only the accepted report, category, posture, decision, and achievement asset families named in this prompt. Any additional asset family requires an accepted specification amendment. Do not create placeholders or substitute assets.

## Processing rules

- Use the report-event processor for report art.
- Use exact native-size icon workflows for `32x32` and `64x64` consumers.
- Preserve transparency for icon families.
- Do not resize one asset type into another.
- Review crops and edge bleed.
- Review icons on light and dark game backgrounds where relevant.
- Keep final files in runtime asset folders.
- Keep source and preview files in the accepted documentation asset workspace.
- Remove temporary generation files from runtime folders.
- Do not use a fallback image as final completion.

## Required package structure

Follow the current asset skill and repository convention. At minimum deliver:

- source images
- processed PNG previews
- final DDS files
- contact sheets at native size
- `manifest.json` or the current accepted asset manifest format
- `gfx_handoff.md`
- provenance and source notes
- review screenshots or evidence paths when the active tools support them

The manifest must include for every asset:

- asset id
- working and final name
- consumer
- source mode
- source path
- preview path
- final runtime path
- width and height
- alpha status
- DDS format
- sprite proposal
- target `.gfx` file
- SHA-256
- completion status
- known uncertainty

## `.gfx` handoff

The asset worker proposes exact sprite blocks and ownership, but the main implementation agent performs final runtime wiring unless explicitly assigned otherwise.

The handoff must state:

- whether `GFX_report_event_border_fortifications` remains unchanged
- every new sprite name
- every final texture path
- exact consumer
- target `.gfx` owner
- any load-order or duplicate-name risk
- any obsolete current reference that must be removed

## Visual acceptance

Do not call the asset package complete until:

- report image reads at `210x176`
- report corners and alpha are correct
- decision category picture fits its verified consumer
- category icon reads at `32x32`
- three posture icons read and differ at `64x64`
- five decision icons read and differ at `32x32`
- four achievement families include all required states
- no icon has clipping, halos, unintended background, or edge bleed
- no asset uses unverified rights
- no asset contains readable generated text
- no runtime path points to documentation or temporary output
- manifest and hashes match final files
- `.gfx` handoff is complete
- any remaining blocker is reported directly
