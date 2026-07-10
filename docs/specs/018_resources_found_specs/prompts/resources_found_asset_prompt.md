# Asset Production Prompt for Event 018 Resources Found

Produce the complete visual asset package for Chaos Redux Event 018, Resources Found. This is a generated fictional and alternate-history package. Use the narrow project asset workers by asset type. Use `chaosx_generated_event_art` for non-icon scenes, fictional portraits, flags, emblems, and super-event images. Use `chaosx_icon_artist` for focus, idea, decision, decision-category, achievement, warning, and mechanic icons. Use `chaos-redux-frame-animation` for every animated element.

All working labels in this prompt are internal design handles, not final localisation.

## Required reading and boundaries

Read the relevant sections of:

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md` for animated work
- this asset prompt
- the Event 018 source specs
- the named reference folders for each asset type

Do not edit gameplay, localisation, GUI, GFX, focus, idea, decision, event, country, history, or spreadsheet files. Produce source art, processed PNGs, final DDS or TGA files, manifests, contact sheets, and `gfx_handoff.md` only.

Do not use generated text, labels, watermarks, modern clothing, modern machinery, modern roads, modern safety gear, cinematic color grading, meme imagery, fake checkerboards, white halos, or opaque square backgrounds on transparent icons.

No asset may remain a placeholder. If an asset cannot be completed, mark it `blocked` or `needs_user_review`.

## Package paths

Working package root:

```text
docs/assets/018_resources_found/
```

Required working structure:

```text
docs/assets/018_resources_found/
  manifest.md
  gfx_handoff.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  animations/
  notes/
```

Proposed final game folders:

```text
gfx/event_pictures/018_resources_found/
gfx/event_pictures/news/018_resources_found/
gfx/super_events/018_resources_found/
gfx/interface/ideas/018_resources_found/
gfx/interface/goals/018_resources_found/
gfx/interface/decisions/018_resources_found/
gfx/interface/018_resources_found/
gfx/leaders/018_resources_found/
```

Flags remain in the root flag folders with the final country tag filenames:

```text
gfx/flags/
gfx/flags/medium/
gfx/flags/small/
```

Achievements remain directly under `gfx/achievements/` and use exact final achievement IDs.

## Visual identity

The event begins as a practical 1936 to 1945 industrial discovery. Its early art should show survey stakes, drills, shafts, derricks, ore carts, rail spurs, field camps, processing yards, workers, geologists, and local authorities. Later art introduces corrosion, missing crews, armored subterranean creatures, public evacuation, and organized nonhuman armies.

The cave species must have one coherent identity across leader portrait, flags, super-events, icons, and report images:

- intelligent nonhuman anatomy
- mineral or stone-like armor grown as part of the body
- heavy, low, deliberate movement
- visual connection to resource-bearing rock without becoming a pile of gemstones
- no resemblance to a real ethnic or religious group
- no borrowed kobold, goblin, or Tommyknocker design
- no comedy fantasy styling
- organized military presence at Evolution IV
- strong readability in HOI4 presentation

## Reference folders

Inspect before production:

```text
.agents/skills/chaos-redux-event-assets/assets/report_event_images
.agents/skills/chaos-redux-event-assets/assets/news_event_images
.agents/skills/chaos-redux-event-assets/assets/super_event_images
.agents/skills/chaos-redux-event-assets/assets/ideas
.agents/skills/chaos-redux-event-assets/assets/focuses
.agents/skills/chaos-redux-event-assets/assets/decisions
.agents/skills/chaos-redux-event-assets/assets/achievements
.agents/skills/chaos-redux-event-assets/assets/flags
```

Record which references were inspected in the manifest.

## Report event images

All report images are generated fictional period-documentary scenes. Generate the underlying 1936 to 1945 photograph first. Then use `tools/process_report_event_image.py` to create the required 210 by 176 sepia report-card treatment with transparent corners and soft shadow.

### 1. Baseline discovery survey

Proposed filename:

```text
report_event_018_resource_discovery.dds
```

Proposed sprite:

```text
GFX_report_event_018_resource_discovery
```

Scene direction:

A mixed team of period geologists, surveyors, drilling workers, and local officials examining unexpectedly rich samples beside a new shaft, test well, or drill rig. Include period instruments, crates, sample trays, and practical excitement. The scene should be location-neutral enough for a random state. Avoid readable signs and avoid making a map the central subject.

### 2. Compound field development

```text
report_event_018_compound_field.dds
GFX_report_event_018_compound_field
```

Scene direction:

A large extraction zone with several kinds of workings, rail wagons, processing sheds, and crowded labor activity. The image should communicate that one state has become a vast multi-resource complex.

### 3. Sick lower workings

```text
report_event_018_sick_workings.dds
GFX_report_event_018_sick_workings
```

Scene direction:

Period miners and medical staff in a dim lower work. One worker is visibly exhausted or ill, supports show strange corrosion, and equipment has failed. Keep the cause ambiguous. No visible monster.

### 4. Missing crew evidence

```text
report_event_018_missing_shift.dds
GFX_report_event_018_missing_shift
```

Scene direction:

An abandoned underground work station with lamps, helmets, tools, and a damaged ore cart. A rescue team examines a passage that should have been sealed. No gore and no readable text.

### 5. First physical evidence

```text
report_event_018_first_evidence.dds
GFX_report_event_018_first_evidence
```

Scene direction:

A guarded period field laboratory or mine office examining a fragment of mineral armor or an injured nonhuman limb recovered underground. Show uncertainty and military interest without fully revealing the species.

### 6. Perimeter breach

```text
report_event_018_perimeter_breach.dds
GFX_report_event_018_perimeter_breach
```

Scene direction:

Field guards, workers, and engineers retreating from a shattered mine entrance as one or two heavily armored cave creatures emerge. The creatures are physically real but not yet an organized army.

### 7. Evacuation corridor

```text
report_event_018_evacuation.dds
GFX_report_event_018_evacuation
```

Scene direction:

Period trucks and a train evacuating workers and families from an industrial settlement. Soldiers and engineers guard the route. Show urgency and organized movement, not cinematic fireballs.

### 8. Monster hunt

```text
report_event_018_monster_hunt.dds
GFX_report_event_018_monster_hunt
```

Scene direction:

A period combined-arms security force with anti-tank guns, heavy rifles, and engineers preparing to clear a tunnel or ruined industrial district. One armored creature is visible at distance. The image should explain why hard attack matters.

### 9. Full sealing project

```text
report_event_018_full_seal.dds
GFX_report_event_018_full_seal
```

Scene direction:

Engineers placing heavy demolition charges, pumps, concrete, rails, and support equipment around a vast mine entrance while soldiers hold the perimeter. The visual center is the physical sacrifice of an enormous field.

### 10. Liberated anchor cleanup

```text
report_event_018_anchor_cleanup.dds
GFX_report_event_018_anchor_cleanup
```

Scene direction:

Post-battle engineers and soldiers clearing mineral growth, collapsed tunnels, and damaged resource infrastructure in a liberated state. Reflect exhaustion and reconstruction.

## News event images

All news images are generated fictional period press images, processed to black and white at 397 by 153.

### 1. International compound field

```text
news_event_018_global_resource_field.dds
GFX_news_event_018_global_resource_field
```

A wide period press photograph of an enormous extraction complex, rail yards, derricks, headframes, and foreign delegations. No readable banners.

### 2. Border crisis

```text
news_event_018_border_crisis.dds
GFX_news_event_018_border_crisis
```

Period border guards, survey posts, roadblocks, and a resource camp in contested terrain. Avoid generic officers around a map table.

### 3. Public creature attack

```text
news_event_018_public_attack.dds
GFX_news_event_018_public_attack
```

A black-and-white press scene of civilians and soldiers fleeing an industrial street while armored cave creatures enter from a broken tunnel or collapsed road.

### 4. Cave-country emergence

```text
news_event_018_cave_country_emergence.dds
GFX_news_event_018_cave_country_emergence
```

Organized rows of mineral-armored nonhuman soldiers leaving the ruined field under one coherent emblem or command presence. The image must read as a country and army reveal.

### 5. Regional containment

```text
news_event_018_regional_containment.dds
GFX_news_event_018_regional_containment
```

Battle-worn soldiers and engineers sealing the final cave stronghold after a regional victory. Avoid triumphal parade tone.

### 6. Global defeat aftermath

```text
news_event_018_global_defeat.dds
GFX_news_event_018_global_defeat
```

A multinational reconstruction and tunnel-sealing scene after a truly global cave war. Produce only if the defeat aftermath is implemented.

## Super-event images

All super-event images are generated fictional art at 457 by 328. Use strong central composition, high contrast, period fit, and no text.

### Cave-country emergence super-event

```text
gfx/super_events/018_resources_found/super_event_018_cave_emergence.dds
GFX_super_event_018_cave_emergence
```

Direction:

A colossal excavated breach dominates the scene. Organized mineral-armored broods march from it through ruined field infrastructure. Human defenders withdraw at the edges. The composition communicates the birth of a nonhuman state, not a random monster attack. Use a period documentary-painting or staged press-photo realism appropriate to the existing super-event style.

### Cave world-end super-event

```text
gfx/super_events/018_resources_found/super_event_018_world_end.dds
GFX_super_event_018_world_end
```

Direction:

A mature cave host emerging through a shattered resource center on another continent, with distant evidence of simultaneous ruptures. The central subject is the organized host and its mineral-armored leader or command form. Do not use a flat world map as the main visual.

### Global defeat super-event

```text
gfx/super_events/018_resources_found/super_event_018_global_defeat.dds
GFX_super_event_018_global_defeat
```

Direction:

A final sealed chasm surrounded by damaged industrial ruins, multinational engineering teams, abandoned anti-armor weapons, and signs of immense loss. Reflect survival and cost rather than uncomplicated victory. Produce only if the global defeat super-event is implemented.

## Cave leader portrait

### Static portrait

```text
gfx/leaders/018_resources_found/leader_018_cave_sovereign.dds
GFX_portrait_018_cave_sovereign
```

Target: 156 by 210.

Direction:

One intelligent nonhuman cave leader in HOI4 upper-torso framing. The subject has a recognizable face or sensory structure, mineral carapace, weight, and command presence. Use subdued painterly treatment and a dark cavern or command-chamber background. No crown copied from a human monarchy. No text. Record the subject as nonhuman and use an authored original name, not a human gendered name pool.

### Animated portrait

Proposed sprites:

```text
GFX_portrait_018_cave_sovereign
GFX_portrait_018_cave_sovereign_animated
```

Target frame size: 156 by 210.

Frame count target: 8 to 12 real source frames.

FPS: 4 to 6.

Loop: yes.

Play on show: yes when supported.

Motion plan:

- rest pose
- slow chest or throat expansion
- sensory organs narrow or shift
- mineral plates flex slightly
- dust falls from one shoulder
- low chamber light changes across the face
- return to rest without a visible pop

Generate or edit every frame as a real source frame. Do not create final motion through translation, scaling, opacity, glow filters, or color shifts.

Required output:

- source frames
- normalized processed frames
- horizontal sheet PNG and DDS
- static fallback PNG and DDS
- preview GIF
- contact sheet
- manifest entry
- GFX and GUI handoff with the verified target surface

### Optional route portraits

Produce only after final focus and leader-change design confirms use:

```text
leader_018_cave_collective.dds
leader_018_cave_world_end.dds
```

The collective portrait should show a readable council or governing body and use an institutional leader name. The world-end portrait should be a distinct evolved form with its own animation package if wired.

## Cave flags

The final country tag is not yet assigned. Use placeholder asset names in the manifest, then rename to the final tag before wiring.

### Base flag direction

An original high-contrast flag using one central cavern or mineral-vein symbol. It must read at 10 by 7 pixels. Avoid a detailed creature illustration, human heraldry, readable runes, or simple recolor variants.

Required final files after tag assignment:

```text
gfx/flags/<TAG>.tga
gfx/flags/medium/<TAG>.tga
gfx/flags/small/<TAG>.tga
```

### World-end cosmetic flag

Produce only if the country uses a world-end cosmetic tag. Use a distinct composition that suggests a connected continental vein network or several ruptures. Do not recolor the base flag.

Validate TGA dimensions and origin. `file` output must not end with `- top`.

## Field scripted-GUI visual family

### Baseline seal

Proposed static and animated sprites:

```text
GFX_018_resource_field_seal
GFX_018_resource_field_seal_animated
```

Target size: determine from the final scripted GUI brief, recommended 96 by 96 or 128 by 128.

Direction:

A resource-authority seal combining a period industrial headframe or derrick with geological strata. No text.

Animation target: 8 frames at 4 FPS. Real source-frame changes show slow machinery motion, survey light, or moving sample indicator. Static fallback required.

### Unsafe warning overlay

```text
GFX_018_resource_field_unsafe
GFX_018_resource_field_unsafe_animated
```

Transparent warning overlay with damaged supports, corroded metal, or a subtle shaking indicator. Use 6 to 8 real frames. It should communicate unsafe conditions without revealing creatures.

### Disturbance state

```text
GFX_018_resource_field_disturbance
GFX_018_resource_field_disturbance_animated
```

The seal gains unnatural fractures, displaced tools, or a vibration pattern. Avoid magical glow. Use physical movement and dust.

### Breach critical state

```text
GFX_018_resource_field_breach
GFX_018_resource_field_breach_animated
```

A severe state with broken stone, an opening shaft, moving shadows, and visible pressure. Use real source frames. The animation should be noticeable but not obscure values.

### Suspended state

```text
GFX_018_resource_field_suspended
```

Static sealed gate, idle machinery, and guarded works.

### Sealing state

```text
GFX_018_resource_field_sealing
GFX_018_resource_field_sealing_animated
```

Real-frame sequence showing concrete, supports, pumping, or demolition preparation progressing subtly.

### Closed state

```text
GFX_018_resource_field_closed
```

Permanent sealed works with removed extraction symbols. Static asset.

## Decision category and mechanic icons

Inspect the decision reference folder. Produce separate 32 by 32 transparent icons for each action family. Do not derive these by shrinking focus icons.

Proposed list:

```text
decision_category_018_resource_field.dds
decision_018_geological_appraisal.dds
decision_018_deeper_test.dds
decision_018_primary_works.dds
decision_018_transport_corridor.dds
decision_018_heavy_machinery.dds
decision_018_local_processing.dds
decision_018_worker_settlement.dds
decision_018_safety_rotation.dds
decision_018_shaft_reinforcement.dds
decision_018_field_hospital.dds
decision_018_field_guards.dds
decision_018_smuggling_crackdown.dds
decision_018_export_contract.dds
decision_018_foreign_concession.dds
decision_018_nationalization.dds
decision_018_commission.dds
decision_018_demilitarization.dds
decision_018_suspension.dds
decision_018_partial_closure.dds
decision_018_full_seal.dds
decision_018_monster_hunt.dds
decision_018_evacuation.dds
decision_018_anti_armor_aid.dds
decision_018_resource_anchor.dds
decision_018_spawn_queue.dds
decision_018_tunnel_link.dds
decision_018_anchor_guard.dds
decision_018_resource_denial.dds
```

Each icon needs one clear subject, strong silhouette, transparent unused pixels, dark outline, subtle shadow, no text, and readability at 32 by 32.

## Idea and national spirit icons

Target: 64 by 64 transparent compact spirit art.

Proposed list:

```text
idea_018_resource_authority.dds
idea_018_commercial_charter.dds
idea_018_foreign_concession.dds
idea_018_international_commission.dds
idea_018_strategic_reserve.dds
idea_018_compound_field.dds
idea_018_sick_workings.dds
idea_018_open_breach.dds
idea_018_mineral_carapaces.dds
idea_018_slow_blood.dds
idea_018_resource_born_broods.dds
idea_018_surface_starvation.dds
idea_018_untranslatable_command.dds
idea_018_unfed_broods.dds
idea_018_continental_network.dds
idea_018_world_end_host.dds
```

The ordinary field ideas should use period industrial motifs. Cave ideas should use the coherent species identity.

## Focus icon family

Target: 94 by 86. Produce each as a focus-specific generated asset, not as a resized idea or decision icon.

Proposed focus group icons:

```text
goal_018_first_breach.dds
goal_018_origin_chamber.dds
goal_018_first_war_broods.dds
goal_018_surface_veins.dds
goal_018_one_maw.dds
goal_018_central_resonance.dds
goal_018_origin_above_all.dds
goal_018_singular_hunger.dds
goal_018_many_chambers.dds
goal_018_local_brood_memory.dds
goal_018_distributed_command.dds
goal_018_second_deep_capital.dds
goal_018_host_without_a_head.dds
goal_018_hoard_the_veins.dds
goal_018_mineral_tithe.dds
goal_018_guard_feeding_chambers.dds
goal_018_vaults_beneath_continent.dds
goal_018_survey_surface_seams.dds
goal_018_activate_anchors.dds
goal_018_brood_queues.dds
goal_018_consume_industry.dds
goal_018_link_chambers.dds
goal_018_continental_network.dds
goal_018_stone_phalanx.dds
goal_018_interlocking_carapaces.dds
goal_018_moving_mountain.dds
goal_018_burrow_war.dds
goal_018_hidden_approach.dds
goal_018_front_has_a_floor.dds
goal_018_scree_tide.dds
goal_018_lighter_plates.dds
goal_018_hills_begin_to_move.dds
goal_018_study_broken_weapons.dds
goal_018_dense_plates.dds
goal_018_surface_senses.dds
goal_018_final_adaptation.dds
goal_018_mark_richest_route.dds
goal_018_break_first_ring.dds
goal_018_consume_industrial_belt.dds
goal_018_seal_coast.dds
goal_018_break_coalitions.dds
goal_018_last_resistance.dds
goal_018_continent_consumed.dds
goal_018_continental_heart.dds
goal_018_distant_shores.dds
goal_018_first_rupture.dds
goal_018_world_opens_below.dds
```

The final implementation may add focus nodes. Every final focus still needs icon coverage. Use coordinated motifs, but do not reuse one icon across unrelated capstones.

## Achievement icons

Target: 64 by 64. Use the exact final achievement IDs as filenames directly under `gfx/achievements/`. Produce completed, grey, and not-eligible variants according to the achievement workflow.

Working concepts and icon direction:

- One Vein to Rule the Market: one immense ore or oil vein dominating trade machinery
- The Whole Periodic Table, Figuratively: six distinct resource symbols converging on one field
- Seal It While We Still Can: a massive sealed shaft with pressure behind it
- Thirty From Below: thirty organized silhouettes emerging from one breach, simplified for readability
- Contract of the Century: period contract seal over rail and resource imagery, no readable text
- No Claims Left Unsettled: border markers joined by a neutral resource seal
- Ten From One State: one rich state anchor producing ten brood marks
- The Last Shaft Closed: final cave entrance sealed after battle
- Continental Appetite: underground vein network crossing a continent silhouette
- Every Worker Came Home: helmets and lamps arranged around a safely closed shaft

Do not generate text or numbers inside icons. The thirty and ten concepts should use composition rather than readable numerals.

## Cave unit and commander assets

Produce only if required by the final implementation surface:

- one base cave division emblem
- one Stone Phalanx emblem
- one Burrow War emblem
- one Scree Tide emblem
- one anchor guard emblem
- a small set of commander portraits with original nonhuman identities

These are fictional generated assets. Record every commander’s apparent nonhuman identity and final authored name requirement.

## Animation validation

Every animated package must include:

- written brief
- frame plan
- one source PNG per frame
- one processed PNG per frame
- exact shared frame dimensions
- horizontal sheet PNG
- horizontal sheet DDS
- static fallback PNG and DDS
- preview GIF for review only
- contact sheet
- frame count
- FPS
- loop and play-on-show behavior
- target GFX file
- target GUI or portrait surface
- source mode for every frame
- validation that the motion is not transform-only

A GIF is never the final HOI4 asset.

## Manifest requirements

For every asset record:

- asset name
- Event 018 association
- asset type
- intended use
- source mode as generated
- generation prompt
- reference folder inspected
- source PNG path
- processed PNG path
- final DDS or TGA path
- exact dimensions
- sprite name
- target GFX file
- related event, focus, idea, decision, country, achievement, or super-event
- animation metadata where relevant
- status
- uncertainty or blocker

## GFX handoff requirements

`gfx_handoff.md` must list:

- final path
- exact proposed sprite name
- target GFX file
- target GUI or gameplay reference
- size
- frame count and FPS for animations
- static fallback
- ready-to-copy sprite snippets where useful
- any naming that remains blocked by the final country tag or focus ID

Do not wire GFX or gameplay files. The main implementation agent owns final wiring and must preserve the final registered names.

## Completion standard

Every requested asset is either complete, blocked, or marked needs user review. A complete static asset has source PNG, processed PNG, final game file, verified dimensions, manifest entry, and GFX handoff. A complete animated asset also has real source frames, sheet, fallback, preview, contact sheet, timing, and target-surface handoff. No placeholder, generic reused image, resized cross-type icon, or undocumented asset counts as complete.
