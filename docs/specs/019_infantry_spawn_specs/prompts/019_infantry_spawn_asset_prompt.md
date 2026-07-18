# Asset Production Prompt for Event 19 Infantry Spawn

## Task

Produce the complete visual asset package for Chaos Redux Event ID `19`, Infantry Spawn, from the accepted specification in `docs/specs/019_infantry_spawn_specs/`.

Read the event asset skill, frame animation skill, and the bounded source files named below. Do not inspect unrelated gameplay files. Preserve final filenames and sprite names if the implementation agent has already registered them. Values in this prompt are proposed identifiers until registration.

## Required source files

- all eight event specification parts
- `matrices/019_asset_inventory.md`
- `matrices/019_possessed_general_matrix.md`
- `matrices/019_country_package_matrix.md`
- `matrices/019_achievement_matrix.md`
- final implementation GFX handoff identifiers, when provided

## Routing

Split production by asset type.

- Use `chaosx_generated_event_art` for fictional report and news scenes, the 20 claimant army/muster identity scenes delivered through fixed portrait slots, six derivative massed-host identity scenes, fictional flags, and GUI background art.
- Use `chaosx_icon_artist` for decision, decision-category, idea, national-spirit, focus, achievement, warning, meter, seal, and small animated UI assets.
- Do not use generated art for a real historical person or attested historical flag. This source design does not require either. Mark any later real-person or historical-symbol addition for `chaosx_asset_source_researcher`.
- Animated work must follow `chaos-redux-frame-animation` with real separate source frames.

## Working package paths

Use:

```text
docs/assets/019_infantry_spawn/
  manifest.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  animations/
  notes/
  gfx_handoff.md
```

Final game assets must go under event-scoped folders such as:

```text
gfx/event_pictures/019_infantry_spawn/
gfx/interface/decisions/019_infantry_spawn/
gfx/interface/ideas/019_infantry_spawn/
gfx/interface/goals/019_infantry_spawn/
gfx/interface/019_infantry_spawn/
gfx/leaders/019_infantry_spawn/
```

Flags remain in the normal HOI4 flag roots with the final cosmetic or dynamic identity filenames. Achievement DDS files remain directly under `gfx/achievements/` and match final achievement IDs.

## Reference inspection

Before creating each asset type, inspect the matching project reference folder:

- report event images
- news event images
- decisions
- ideas
- focuses
- achievements
- flags

Record the inspected references in the manifest. Do not copy them.

## Report and news images

Create generated fictional 1936 to 1945 documentary-style source scenes. No readable text, modern equipment, modern streets, cinematic color grading, fake UI, or comedy framing.

Required report scenes at 210 by 176 after processing:

1. initial manifestation across a rail siding, schoolyard, depot, or town square, with recruits, horses, trucks, and guns visibly mismatched
2. organized muster with coherent columns and an unexplained parallel staff
3. arsenal lottery with serious incompatible vehicles and infantry occupying one logistics site
4. claimant emergence shown through a mixed formation realigning around an impossible command order, with no individual commander as the focal subject
5. anomalous muster showing bounded ordinary, zombie, ghost, and golem visual cues without copying parent-event imagery
6. zombie derivative release and defeat
7. ghost derivative release and defeat
8. golem derivative release and defeat

Use the repository report-event processing script and house style. Preserve source PNGs, processed PNGs, and final DDS files.

Use 397 by 153 black-and-white news images only when implementation confirms that derivative release or regional dominance receives a news event. Do not create unused news assets blindly.

## Twenty claimant army/muster identity scenes

Create all 20 fictional army/muster scenes in `matrices/019_possessed_general_matrix.md`. Preserve the fixed technical portrait filenames and sprite identifiers.

Requirements:

- final 156 by 210
- HOI4-style vertical army/muster identity composition
- period-appropriate regional troops, logistics, terrain, transport, guns, animals, craft, or field infrastructure
- a distinct formation geometry and operational posture for every slot
- severe, uncanny, or possessed collective identity with subtle supernatural disturbance
- no gore-centered caricature
- no text or watermark
- no individual focal human/person, readable face, bust, officer, or commander
- no real national/state/party emblem or copied historical identity
- strong massed-army silhouette at runtime size
- retain all 20 male gameplay claimant profiles and matching regional male name-pool requirements as metadata, without depicting the named person
- record the region/profile binding and scene identity in every manifest entry

These fixed portrait-slot scenes are static. Do not create animated versions.

The no-focal-person rule is scoped to the 27 fixed identity slots and any Event 19 UI, scenario, or authority display that reuses them. Independent report, focus, decision, and achievement illustrations remain governed by their own briefs and never serve as claimant, commander, council, or derivative identity art.

## Derivative host and council-as-massed-entities scenes

Produce a bounded reusable set after implementation confirms the final leader model.

Minimum plan:

- one massed zombie army wall for the commander-labelled slot
- one zombie council expressed as exactly three undead legion masses
- one massed spectral spearhead for the ghost commander-labelled slot
- one ghost council expressed as exactly three genderless spectral formations
- one collective quarry builder-host for the golem master-builder-labelled slot
- one golem council expressed as exactly three geological cohorts

All six slots depict hosts, never individual leaders, councillors, people, faces, busts, or anthropomorphic close-ups. Commander/master-builder labels are gameplay and technical identifiers. Council slots use institutional names and exactly three massed formations/cohorts.

## Flags

Create distinct fictional flag families for zombie, ghost, and golem derivatives.

Each final identity needs:

- 82 by 52 normal TGA
- 41 by 26 medium TGA
- 10 by 7 small TGA
- verified vanilla-compatible TGA origin
- contact sheet showing orientation and readability

Each family needs a stable base motif and only the route variants that implementation actually uses for claimant, collective, or species-command identities. Route variants must be distinct designs, not recolors.

Do not copy parent Zombie, Death, or golem flags.

## Decision and idea icons

Create separate source art for every icon type. Never resize a focus icon to satisfy a decision or idea icon.

Decision category and decision families:

- audit and census
- equipment ledger
- territorial assignment
- standardization
- emergency integration
- rail corridor
- muster depot
- relocation
- demobilization and disarmament
- five ordinary request modes
- anomalous request
- formal command
- counter-command
- arrest, retirement, and takeover
- cantonment, liaison, restriction, sustainment, and breach sealing
- base zombie training
- ghost manifestation
- golem binding

Core idea or UI value icons:

- Muster Control
- Army Congestion
- Claimant Influence
- Anomalous Saturation
- supply strain
- command confusion
- training saturation
- equipment debt

Decision icons are 32 by 32. Idea and national-spirit icons are 64 by 64. Decision-category size must follow the verified existing project pattern.

## Muster Board UI art

Create only the artwork required by the final layout:

- background panel
- overview header
- formation lot card states
- quality and coherence markers
- command army/muster identity-scene frame states
- registry family card states
- cost, warning, cooldown, and invalid-target markers

The implementation agent owns exact layout and interactive slicing. Generated art must not determine button geometry.

## Animated UI packages

Create three final frame-sheet packages.

### Muster seal pulse

- 8 real source frames
- target size from final category or GUI layout
- 6 to 8 frames per second
- looping
- indicates unresolved lots

### Critical command border

- 8 real source frames
- target fits the claimant army/muster identity-scene panel while retaining the fixed portrait-slot dimensions
- 5 to 7 frames per second
- looping while revolt risk is critical

### Anomalous registry emblem

- 10 real source frames
- target from final registry tab layout
- 4 to 6 frames per second
- slow loop while a family is active or saturation is rising

For each animation provide:

- brief and frame plan
- separate source frame PNGs
- processed frames
- horizontal sheet PNG and DDS
- static fallback PNG and DDS
- GIF preview for review only
- contact sheet
- frame count, FPS, anchor, loop, and `play_on_show` note
- ready-to-copy GFX handoff after local precedent verification

Do not create motion from one transformed or filtered still.

## Derivative focus icons

After implementation fixes the final focus list, produce one 94 by 86 icon per focus. Plan coordinated families for:

- opening survival
- claimant hierarchy
- collective hierarchy
- species command
- sustainment and economy
- military and reinforcement
- former-parent war
- regional expansion
- integration
- zombie transformation
- ghost transformation
- golem transformation
- regional predator capstone

Every focus needs an icon. Reuse is allowed only where the final focus meaning genuinely matches.

## Achievement icons

Produce completed, grey, and not-eligible variants for every final achievement in `matrices/019_achievement_matrix.md`.

- final size 64 by 64
- completed icon first
- grey variant by black-and-white conversion
- not-eligible variant by applying the project overlay to the grey version
- exact filenames match registered achievement IDs

## Manifest and handoff

Every asset entry must record:

- asset name and type
- related event, focus, decision, idea, leader, country identity, or achievement
- source mode
- generation prompt
- reference folder inspected
- source PNG
- processed PNG
- final DDS or TGA
- target size
- sprite name
- target GFX file
- status
- region/profile and male gameplay name-pool note for claimant identity scenes
- frame data for animations
- uncertainty or blocker

Do not mark the package complete while any requested visible asset is missing, placeholder, incorrectly sized, undocumented, or unwired in the GFX handoff.
