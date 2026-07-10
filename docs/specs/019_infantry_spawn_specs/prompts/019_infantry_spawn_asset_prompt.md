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

- Use `chaosx_generated_event_art` for fictional report and news scenes, the 20 fictional claimant portraits, derivative leader or council portraits, fictional flags, and GUI background art.
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
4. claimant emergence with a frightening fictional commander inspecting a mixed formation
5. anomalous muster showing bounded ordinary, zombie, ghost, and golem visual cues without copying parent-event imagery
6. zombie derivative release and defeat
7. ghost derivative release and defeat
8. golem derivative release and defeat

Use the repository report-event processing script and house style. Preserve source PNGs, processed PNGs, and final DDS files.

Use 397 by 153 black-and-white news images only when implementation confirms that derivative release or regional dominance receives a news event. Do not create unused news assets blindly.

## Twenty claimant portraits

Create all 20 fictional portraits in `matrices/019_possessed_general_matrix.md`.

Requirements:

- final 156 by 210
- HOI4-style bust or upper torso
- period-appropriate regional military or improvised command clothing
- severe, uncanny, or possessed identity
- subtle supernatural disturbance
- no gore-centered caricature
- no text or watermark
- strong face readability
- 10 male-presenting and 10 female-presenting
- record presentation and matching regional name-pool requirement in every manifest entry

These portraits are static. Do not create animated versions.

## Derivative leaders and councils

Produce a bounded reusable set after implementation confirms the final leader model.

Minimum plan:

- one zombie claimant-independent fictional leader
- one zombie collective or symbolic council portrait
- one ghost claimant-independent fictional or spectral leader
- one ghost collective or symbolic council portrait
- one golem claimant-independent fictional master-builder or construct leader
- one golem collective or symbolic council portrait

One-person portraits need gender presentation and matching name-pool notes. Collective portraits use institutional names.

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
- command portrait frame states
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
- target fits the claimant portrait panel
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
- presentation and name-pool note for one-person portraits
- frame data for animations
- uncertainty or blocker

Do not mark the package complete while any requested visible asset is missing, placeholder, incorrectly sized, undocumented, or unwired in the GFX handoff.
