# Asset production prompt: Event 42 Equipment from Heavens

Create the complete static visual asset package for Chaos Redux Event 42, Equipment from Heavens. Follow `AGENTS.md`, `chaos-redux-event-assets`, the official ImageGen workflow, and the Event 42 source specifications in this package.

## Event identity

The event shows enormous military stockpiles appearing across ordinary countries without a sender or believable delivery route. The main visual subject is the physical skyfall and recovery scene. Do not make maps, command tables, diplomatic meetings, cargo manifests, or abstract symbols the main composition.

## Source mode

Use generated period-documentary artwork because the scenes are fictional and physically impossible. Create each base scene as a coherent 1936 to 1945 documentary photograph with period clothing, vehicles, buildings, cameras, roads, airfields, military equipment, and recovery methods. Avoid modern cargo aircraft, modern uniforms, digital displays, container ports, contemporary forklifts, readable generated text, cinematic color grading, and science-fiction interfaces.

Inspect these reference families before production:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/`

## Report-event image requirements

Create six distinct report-event scenes.

### 1. Crate fields

A rural field, village road, or depot approach is covered with military crates, artillery pieces, ammunition pallets, and parachute cloth. Soldiers and civilians stand among the cargo. The scene should communicate impossible quantity and blocked movement.

Suggested runtime basename: `equipment_from_heavens_crate_fields`

Suggested final path: `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_crate_fields.dds`

Suggested sprite: `GFX_report_event_equipment_from_heavens_crate_fields`

### 2. Vehicles under parachutes

Tanks, trucks, or armored vehicles descend or have just landed under immense parachutes. The vehicle scale must remain believable. Show torn fields, recovery crews, and parachute fabric without showing a sender aircraft.

Suggested runtime basename: `equipment_from_heavens_vehicle_descent`

Suggested final path: `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_vehicle_descent.dds`

Suggested sprite: `GFX_report_event_equipment_from_heavens_vehicle_descent`

### 3. Aircraft landing ground

Intact military aircraft have appeared across an improvised field or small airstrip. Ground crews inspect them. The aircraft may come from several recognizable conventional roles, but the scene must not become a modern air show or futuristic concept-art image.

Suggested runtime basename: `equipment_from_heavens_aircraft_field`

Suggested final path: `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_aircraft_field.dds`

Suggested sprite: `GFX_report_event_equipment_from_heavens_aircraft_field`

### 4. Overwhelmed depot

A railway yard, village square, or military depot is filled beyond capacity with artillery, trucks, trains, and crates. Emphasize human scale, congestion, improvised inventory work, and inaccessible roads.

Suggested runtime basename: `equipment_from_heavens_overwhelmed_depot`

Suggested final path: `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_overwhelmed_depot.dds`

Suggested sprite: `GFX_report_event_equipment_from_heavens_overwhelmed_depot`

### 5. Sealed atomic cache

A restrained military recovery scene around sealed heavy weapon containers, guarded underground storage, or a newly discovered custody site. The image should imply atomic weapons through period handling equipment and strict cordons without modern nuclear symbols, glowing objects, or spectacle.

Suggested runtime basename: `equipment_from_heavens_atomic_cache`

Suggested final path: `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_atomic_cache.dds`

Suggested sprite: `GFX_report_event_equipment_from_heavens_atomic_cache`

### 6. Sealed Chaos cargo

Unidentified sealed containers and strange military equipment are being quarantined by period soldiers. Keep the contents visually ambiguous so the image does not claim an unverified robot, plague, clone, alien, or other exact family. Use unusual proportions, unknown materials, power cables, frost, condensation, or disturbed guards as subtle cues.

Suggested runtime basename: `equipment_from_heavens_chaos_cargo`

Suggested final path: `gfx/event_pictures/042_equipment_from_heavens/equipment_from_heavens_chaos_cargo.dds`

Suggested sprite: `GFX_report_event_equipment_from_heavens_chaos_cargo`

## Report image processing

For each report image:

- preserve the full-resolution generated source PNG
- create a processed documentary scene
- convert the scene to black and white with sepia treatment
- place it on the standard 210 by 176 RGBA report-event card
- apply the established slight tilt, transparent corner space, and soft drop shadow locally
- preserve real transparency in the card corners
- produce final DDS output in the event-scoped runtime folder
- include a native-size contact sheet and a larger review sheet
- validate subject clarity at 210 by 176

Do not ask ImageGen to paint the tilted card or fake transparent corners. Generate the photograph first and apply the card treatment through the deterministic asset workflow.

## Achievement icons

Create one completed 64 by 64 icon for each working achievement route, then derive the grey and not-eligible states through the approved achievement workflow.

### Tiny Arsenal State

Show a very small country silhouette or tiny military standard dwarfed by an immense mountain of rifles, tanks, and crates. The icon must remain readable at 64 by 64. Avoid maps with unreadable borders and avoid text.

Suggested achievement ID and basename: `042_equipment_from_heavens_tiny_arsenal_state`

### Nuclear Lottery

Show a sealed atomic weapon crate or bomb silhouette descending under a parachute toward a small military depot. Use a strong central silhouette and period military framing. Avoid modern warning labels and readable text.

Suggested achievement ID and basename: `042_equipment_from_heavens_nuclear_lottery`

### Borrowed Nightmare

Show an ordinary soldier opening a military crate whose interior contains an unknown unnatural weapon glow or silhouette. Keep the exact special family ambiguous. The subject should read as captured or unearned dangerous equipment, not occult treasure.

Suggested achievement ID and basename: `042_equipment_from_heavens_borrowed_nightmare`

Achievement files remain directly under `gfx/achievements/` with exact full achievement IDs:

- `<achievement_id>.dds`
- `<achievement_id>_grey.dds`
- `<achievement_id>_not_eligible.dds`

## Asset families not authorized

Do not create portraits, flags, focus icons, decision icons, national-spirit icons, unit counters, animated sprites, 3D models, super-event images, or news-event images for this package. Event 42 introduces no new character, country, unit family, focus tree, decision category, mechanic window, or super-event.

## Temporary workspace and handoff

Use `docs/assets/042_equipment_from_heavens/` as the temporary evidence workspace while production is active. Include source PNGs, processed previews, prompts, contact sheets, manifest, provenance, DDS conversion notes, and `gfx_handoff.md`.

The handoff must list every final runtime file, sprite name, source prompt, dimensions, alpha status, processing steps, review result, and remaining blocker. Do not edit gameplay, localisation, event, GFX, GUI, achievement script, or spreadsheet files unless the parent explicitly expands scope.

Before the event is finally complete, promote durable prompt, provenance, review, and sprite-crosswalk facts into permanent event or plan documentation, verify that no runtime reference points into `docs/assets/`, and delete the temporary event workspace.
