# Asset prompt for Event 014 Cannibalism

Use this prompt with the Chaos Redux event asset workflow. Split work across asset subagents by type.

## Required source files to read

- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_1_core.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_2_evolutions_decisions.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_3_country_packages_focus_tree.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_4_world_end_super_events_assets.md
- chaos-redux-event-assets skill
- chaos-redux-frame-animation skill for animated pieces

## Nonnegotiable art direction

Gore is required for Event 014 assets. Use generated fictional gore, stylized gore, or symbolic gore. Do not use real photographs of identifiable victims or real atrocity gore as final assets. Sourced research material can guide period atmosphere, documents, locations, and military framing. Generated art should carry the explicit gore.

All World War II-era event images should look period-authentic. Avoid modern uniforms, modern streets, modern weapons, generated readable text, UI artifacts, and cinematic modern color grading.

## Subagent routing

Use chaosx_generated_event_art for:

- fictional report images
- fictional news images
- super-event images
- fictional leader and council portraits
- fictional flags and faction emblems
- UI panels and progression-state art

Use chaosx_icon_artist for:

- idea icons
- national spirit icons
- decision icons
- decision category icon
- focus icons
- achievement icons
- small animated icons or button sprites

Use chaosx_asset_source_researcher only for:

- non-gore real archival reference images if a sourced report or news asset is explicitly selected
- historical research references
- any real historical symbol if implementation later adds one

## Reference folders to inspect

- ideas: .agents/skills/chaos-redux-event-assets/assets/ideas
- decisions: .agents/skills/chaos-redux-event-assets/assets/decisions
- focuses: .agents/skills/chaos-redux-event-assets/assets/focuses
- achievements: .agents/skills/chaos-redux-event-assets/assets/achievements
- report event images: .agents/skills/chaos-redux-event-assets/assets/report_event_images
- news event images: .agents/skills/chaos-redux-event-assets/assets/news_event_images
- super-event images: .agents/skills/chaos-redux-event-assets/assets/super_event_images
- flags: .agents/skills/chaos-redux-event-assets/assets/flags

## Report event images, 210 by 176

Every generated report image must receive the report-event card treatment and final DDS conversion.

Required assets:

1. first field report, soldiers and field kitchen records, gore present but partially obscured
2. field hospital audit, evidence table and military doctors, gore present and fictional
3. prison kitchen seizure, prison corridor and seized tools, gore required
4. island inspection, ruined dock and silent garrison signs, gore required
5. empty village aftermath, military patrol and missing persons evidence, gore required
6. contained aftermath, sealed archive and cleaned field kitchen, restrained gore trace

## News event images, 397 by 153, black and white

Required assets:

1. public leak, military police and newspaper office, gore implied and fictional
2. cannibal country declaration, armed commune and captured flag, gore visible
3. global network reveal, intelligence boards and matching symbols, gore visible

## Super-event images, 457 by 328

Required assets:

1. cannibal islands reveal, generated island horror with ruined dock and explicit fictional gore
2. Hannibal network reveal, generated cult command scene, no final Hannibal likeness unless Hannibal asset exists
3. world-end terminal scenario, generated global threat composition with explicit fictional gore
4. defeat aftermath, generated tribunal, island memorial, or archive recovery with aftermath gore

## Idea and national spirit icons, 64 by 64

Required icons:

- cannibalism in the ranks
- sealed kitchens
- military tribunal pressure
- ritual hunger
- no common rations
- hunted by the living
- eating ledger
- Hannibal discipline
- contained aftermath
- exploitation stain

## Decision icons, 32 by 32

Required icons:

- secure field kitchens
- rotate compromised units
- ration convoy
- hospital audit
- prison transfer freeze
- island inspection
- evacuation
- break ritual cell
- exploit terror
- dismantle terror units

## Decision category icon

- frontline hunger office, target size according to existing category pattern

## Focus icons, 94 by 86

Create a coordinated focus icon family for the shared cannibal country tree. Required motifs:

- opening survival
- command hierarchy
- council route
- warlord route
- Hannibal route, blocked until Hannibal exists
- supply and economy
- depot raids
- prisoner ledger
- hunting-ground administration
- restrained consumption
- runaway consumption
- hunger columns
- butcher packs
- scavenger parties
- prison processions
- island chain raids
- port seizure
- prison road route
- mainland hunting corridors
- cannibal pact
- solitary rampage
- Last Table formable
- world-end preparation

## Country identity assets

Generate fictional flags and portraits.

- CBL base flag in normal, medium, and small sizes
- CBL ideology variants if implementation uses ideology flags
- Last Table cosmetic flag if formable is implemented
- Hannibal dominion flag only after Hannibal spec confirms design
- cannibal leader portrait, 156 by 210, generated fictional person or council
- cannibal council portrait, 156 by 210, generated collective body
- cannibal pact faction emblem

For one-person generated portraits, record apparent gender presentation and require matching name pool and metadata. Council portraits should use institutional names.

## Animated assets

Use chaos-redux-frame-animation. Each animation needs real source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF for review only, manifest entry, and gfx handoff.

Planned animated assets:

- decision category seal, 64 by 64 or category pattern size, 8 frames, slow gore pulse
- cult pressure warning frame, 8 frames, visible only after Evolution I
- island silence signal card, 8 to 12 frames, radio flicker and bloodied paper
- Hannibal resonance seal, 8 to 12 frames, hidden until Hannibal exists
- cannibal council portrait overlay, 156 by 210 or overlay size, 8 frames
- world-end progress border, UI panel size, 12 frames

## Achievement icons, 64 by 64

Create completed icons for each achievement in matrices/014_cannibalism_achievement_matrix.md. Grey and not-eligible variants may be generated after completed icons if the implementation requires them.

## Manifest and handoff

Create or update:

- docs/assets/014_cannibalism/manifest.md
- docs/assets/014_cannibalism/gfx_handoff.md

Every asset entry must include source mode, source PNG, processed PNG, final DDS, target size, sprite name, related gameplay id, status, and uncertainty.
