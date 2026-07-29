# 016 Brilliant Scientist spec, part 9: assets, animation, and localisation

## Binding reconciliation, 2026-07-14

The severe portrait inventory has exactly five animation package families: clone, machine, temporal, xenobiological or alien, and synthesis. The combined xenobiological-or-alien family contains mutually exclusive evidence-gated subvariants and depicts the campaign conclusion actually proven. Transformation alone cannot imply extraterrestrial provenance. The super-event inventory is exactly six, and the achievement inventory is exactly seventeen three-state icon sets.

Stage 0 is complete from the exact approved `portrait_generic_biowarfare_europe_male_01` base. Its runtime leader or scientist DDS and manually composed `65x67` advisor DDS are registered as `GFX_portrait_KRG_doctor_warren_kruger_stage_0` and `GFX_idea_doctor_warren_kruger_stage_0`. The advisor composition uses `.tools/create_advisor_icon.py` with the canonical advisor frame and paper sources in bottom-to-top frame, resized/rotated portrait, and paper order, plus a slight portrait-only sepia blend. Stage I through IV sprite contracts are pre-registered, but their source art, runtime files, static fallbacks, animation sheets, previews, contact sheets, and state wiring remain missing. All other visual families in this part remain unproduced and unwired.

## Visual identity purpose

Kruger's appearance is part of the mechanic. His portrait should communicate the stage and dominant project route before the player opens a long tooltip. The event also needs distinct visual families for projects, facilities, host governance, the Kruger State, super-events, decisions, focuses, ideas, achievements, and custom UI states.

Every final asset needs source art, a processed PNG preview, a final DDS or required flag format, manifest documentation, and a GFX handoff. Animated assets additionally need real source frames, processed frames, a horizontal frame sheet, a static fallback, a GIF preview for review only, and target-surface wiring notes.

## Base Doctor Warren Kruger portrait

### Required source

The user explicitly requires the base portrait to use `portrait_generic_biowarfare_europe_male_01` as its visual base.

Asset workflow:

1. Locate the approved source portrait in the current game or mod files.
2. Copy it into the Event 16 source package.
3. Rename the event-scoped asset to a stable Kruger filename.
4. Preserve the original source without altering or redistributing font or unrelated game assets.
5. Process the copy into the required advisor, scientist, leader, and UI sizes without treating resized outputs as separate artistic designs when the surface needs its own composition.
6. Record the source as an approved in-game visual base in the manifest.

Working filename direction:

- `leader_doctor_warren_kruger_stage_0.dds`
- `scientist_doctor_warren_kruger_stage_0.dds`
- `idea_doctor_warren_kruger_stage_0.dds`

Final names should follow the repository's current sprite registration pattern.

### Base presentation

- European male scientist.
- Period-appropriate protective or laboratory clothing.
- Controlled expression.
- No obvious alien anatomy.
- Slightly clinical and detached.
- Clear face at leader portrait size.
- No generated text or modern equipment.

The baseline portrait can contain one subtle detail that later becomes meaningful, such as unusual eye reflection, skin tone, instrument design, or posture. It should not confirm the twist.

## Portrait progression

### Stage 0: appointment

Visual state:

- Human and credible.
- Calm, precise, difficult to read.
- Original base portrait remains recognizable.

Surfaces:

- Advisor.
- Scientist.
- Custom UI.
- Event picture crop when needed.

### Stage I: national institution

Visual state:

- More severe grooming and clothing.
- National laboratory insignia or controlled institutional details.
- Small physiological or optical anomaly.
- More confident and less deferential.

Source mode:

Generated fictional portrait variant based on the approved Kruger identity. Keep the same face, camera, framing, and period style.

### Stage II: international target

Visual state:

- Hardened security environment.
- Fatigue or altered vitality.
- Subtle evidence of self-experimentation, unusual eyes, skin, or equipment.
- Project-route hint appears for the first time.

The image should still plausibly be interpreted as illness, stress, injury, protective equipment, or strange lighting.

### Stage III: forbidden science

Visual state:

- Clearly unsettling.
- Dominant project route affects anatomy or equipment.
- Clone route can show repeated features or a second blurred figure.
- Machine route can show interfaces, prosthetics, or network light.
- Temporal route can show overlapping posture or inconsistent age.
- Xenobiological route can show altered anatomy.
- Alien route can show a stronger nonhuman reveal.

This stage can remain static if the animation package is not yet active, but it requires route-specific source art and cannot be created by simple recoloring.

### Stage IV: sovereign route animation

Severe route identities use animated portraits.

| Variant | Motion direction | State meaning |
| --- | --- | --- |
| Clone Kruger | Different Kruger bodies enter alignment, breathe independently, or exchange focus | Personal continuity through replication |
| Machine-linked Kruger | Real source frames show interface lights, mechanical movement, eye focus, and machine response | Authority distributed into the network |
| Temporal Continuum Kruger | Real source frames show age, position, or duplicate-state changes designed per frame | Several temporal versions share authority |
| Xenobiological or alien Kruger | Real source frames show controlled anatomical changes or a stable unfamiliar state selected from the locked campaign conclusion | Engineered transformation or evidence-proven extraterrestrial provenance; transformation alone never implies alien origin |
| Synthesis Kruger | Real source frames combine selected project features without visual clutter | Several systems integrated under one identity |

Animation rules:

- Create or approve the static fallback first.
- Use at least 8 real source frames for subtle portrait motion unless a different count is justified by the target surface.
- Keep a shared bottom-center anchor and consistent camera.
- Do not create final motion by shifting, scaling, rotating, blurring, recoloring, changing opacity, or adding a scripted glow to one still.
- Build a horizontal frame sheet and verify exact dimensions.
- Use a static fallback wherever animation is unavailable or disabled.
- Record the character key and route trigger for every variant.

## Advisor and scientist icon evolution

The user requires advisor icons to evolve alongside the portrait.

Required states:

- Stage 0 human appointment.
- Stage I national figure.
- Stage II secured international asset.
- Stage III dangerous experimental scientist.
- Stage IV route-specific sovereign identity.

The advisor and scientist images can share identity and visual motifs. They must still be composed for their actual UI surfaces. A leader portrait crop should not be used blindly as a small icon if the face and project motif become unreadable.

## Report-event image family

Target size:

- 210x176.
- Black and white with sepia.
- Finished report-card treatment with transparent corners and soft shadow.

Required report scenes:

1. Kruger's first demonstration.
2. Universities competing for access.
3. Construction of the first laboratory.
4. Security expansion around the facility.
5. First impossible Prototype.
6. Foreign extraction or sabotage aftermath.
7. Project-specific accident scenes.
8. Government confrontation at a laboratory perimeter.
9. Archive recovery after defection or defeat.
10. Remnant scenes after a major crisis.

Source mode:

Generated period-documentary scenes because Kruger and the incidents are fictional. Use 1936 to 1945 photographic technology, clothing, architecture, instruments, vehicles, and press composition.

Every generated report image still receives the repository report-card processing.

## News-event image family

Target size:

- 397x153.
- Black and white.

Required news scenes:

- Public appointment.
- International recognition.
- Major public breakthrough.
- Kruger State formation.
- First project-army deployment.
- Global containment coalition.
- Singularity prototype discovery.
- Regional or global defeat.

Generated text must not appear in newspapers, banners, equipment labels, or laboratory signs.

## Super-event images

Target size:

- 457x328.

Required packages:

- International recognition, conditional.
- Kruger State formation.
- Global Kruger threat.
- Laboratory World terminal.
- Strategic Singularity terminal.
- Defeat aftermath, conditional.

Each image must follow the role and dominant project route described in part 8. Do not use a map with arrows as the central composition. The subject should be Kruger, the project force, a laboratory city, a scientific crowd, a machine or biological army, or the terminal device.

## Kruger State flags

### Source mode

Generated fictional flag art.

### Required sizes

- 82x52 normal.
- 41x26 medium.
- 10x7 small.

### Design rules

- Strong central symbol.
- Readable at 10x7.
- No generated text.
- Avoid a generic atom icon as the only motif.
- Avoid complex laboratory diagrams.
- Use route-specific symbols that remain flags rather than poster art.
- Validate TGA orientation against vanilla convention.

### Flag families

Base Kruger State:

- Scientific sovereignty.
- Precision and personal authority.
- Symbol can combine a divided lens, asymmetric star, impossible geometry, or a distinct Kruger monogram-like mark without readable lettering.

Human technocracy:

- Public institution and structured science.

Replicated sovereignty:

- Repetition, branching life, mirrored forms, or a controlled cellular motif.

Machine ascendancy:

- Network, mechanical symmetry, command node, or ordered circuit-like motif simplified for flag use.

Temporal Continuum:

- Phase, loop, offset star, or layered time motif.

Xenobiological ascendancy:

- Living geometry, engineered organism, or unfamiliar symmetry.

Synthesis:

- Deliberately combined emblem that remains simple.

Do not create ideology suffix variants that will never appear in play. Create route or cosmetic-tag flags for actual visible identities.

## Faction emblem

A Kruger-led submission or scientific bloc needs an emblem distinct from the national flag.

Direction:

- Network of connected laboratories or an imposed scientific seal.
- Clear at small UI size.
- Route-neutral enough for several Kruger political paths.
- Can receive route-specific variants only when the faction identity changes mechanically.

## Project icon families

### Tech and special-project icons

Required family motifs:

- Computational mathematics.
- Electronics and guidance.
- Advanced materials.
- Rocketry and propulsion.
- High-energy physics.
- Biomedical acceleration.
- Teleportation.
- Cloning.
- Robotics and AI.
- Paleogenetics.
- Xenobiological monsters.
- Biological weapons.
- Alien arms.
- Temporal mechanics.
- Strategic singularity.

Each family should have a coordinated progression from Theory to Prototype to Deployment to Weaponization or Autonomy. Progression can share motifs, but every final icon must remain readable at its required size and cannot be a simple recolor of one base icon.

### Idea and national-spirit icons

Required concepts:

- Kruger's Appointment.
- The Kruger Method.
- National Scientific Dependence.
- Public Scientific Renaissance.
- Controlled Secret Compact.
- Unrestricted Laboratory State.
- Scientific Vacuum.
- Improvised Laboratory State.
- Inherited Project Portfolio.
- Fragmented Command.
- Experimental Supply Chain.
- Scientific Exodus.
- World-threat project state.

Target size:

- 64x64.

Each icon needs its own spirit-style composition and source art. Do not resize focus icons.

### Decision-category icons

Required categories:

- Host Kruger management.
- Project portfolio.
- Foreign scientific contest.
- Sovereignty crisis.
- Former-host recovery.
- Kruger State administration.
- Kruger project armies.
- Global submission and containment.
- Strategic singularity.

Category icon size should follow the verified existing pattern. Do not guess.

### Decision icons

Target size:

- 32x32.

Create simplified symbols for:

- Facility construction and hardening.
- Staff recruitment.
- Publication.
- Compartmentalization.
- Security assignment.
- Relocation.
- Foreign invitation, theft, sabotage, extraction, and protection.
- Project approval and suspension.
- Replication mission.
- Charter, confinement, assassination, and military seizure.
- Project-unit growth.
- Archive recovery.
- Singularity components and disarmament.

### Focus icons

Target size:

- 94x86.

The focus tree needs icon families rather than one icon repeated across many focuses.

Families:

- State survival.
- Government and citizenship.
- Human technocracy.
- Clone sovereignty.
- Machine ascendancy.
- Temporal Continuum.
- Synthesis.
- Laboratory economy.
- Conventional military.
- Robot corps.
- Clone corps.
- Bestiary.
- Portal and temporal operations.
- Exotic energy.
- Diplomacy and intelligence.
- Expansion and integration.
- World conquest.
- Singularity.

Every important capstone needs a unique icon.

## Achievement icons

Target size:

- 64x64.

Every achievement in part 10 needs:

- Completed icon.
- Grey variant.
- Not-eligible variant using the approved overlay workflow.
- Exact achievement-ID filenames in the root achievement folder.

The icon direction should communicate the actual challenge, not merely show Kruger's face for every achievement.

## Custom interface assets

### Panel family

Required visual pieces:

- Main directorate background.
- Profile frame.
- Value meter frames.
- Project cards.
- Facility cards.
- Security-contact cards.
- Sovereignty warning panel.
- Tab buttons.
- Close and open controls.
- Locked, available, selected, completed, damaged, compromised, and critical states.

Generated art should supply thematic background and decorative elements. Exact layout, slicing, button hitboxes, and meter fills remain UI implementation work.

### State-driven animation candidates

#### Kruger status seal

States:

- Stable.
- Active breakthrough.
- Under foreign threat.
- Government control contested.
- Sovereignty crisis.

Motion:

Real frame variations in light, mechanism, or biological state. Static fallback required.

#### Security warning border

States:

- Moderate threat.
- Active infiltration.
- Immediate attack.

Motion should be restrained and readable. Do not animate every border at once.

#### Project activation marker

Shows one active project card. Use subtle mechanical or laboratory motion with real frames.

#### Singularity arming indicator

Late route only. It should become visually severe as components are completed. Static versions are required for every public arming state.

### Static presentation choice

Facility list rows, long project descriptions, cost text, and ordinary decision icons should remain static. Animation belongs to identity, danger, activation, and terminal progress, not every decorative surface.

## Animation brief requirements

Every animated asset handoff must record:

- Asset name.
- In-game surface.
- Target frame size.
- Frame count.
- Calculated sheet size.
- FPS.
- Loop behavior.
- `play_on_show` expectation.
- Anchor.
- Static fallback sprite.
- Animated sprite.
- State trigger.
- Source mode for every frame.
- Target GFX and GUI or character file.
- Local vanilla or Chaos Redux precedent used during implementation.

## Localisation direction

### Character voice

Doctor Warren Kruger should sound:

- Precise.
- Patient only when explaining science.
- Impatient with institutions.
- Dry rather than theatrical.
- Increasingly possessive about staff, facilities, and results.
- Capable of sincere curiosity and protection as well as cruelty.
- Certain that ordinary schedules and political limits are irrational.

He should not sound like:

- A generic cackling mad scientist.
- A modern internet character.
- A constant alien joke.
- An exposition machine explaining hidden mechanics.
- A villain who announces rebellion years in advance.

### Early uncertainty

The opening must keep several explanations possible.

Possible observed details:

- Unverifiable academic history.
- Notation from no known school.
- Instruments built from ordinary parts in unfamiliar arrangements.
- Knowledge of classified work.
- Physical details that could be injury, illness, or unusual anatomy.
- Predictions that are too accurate.

Do not state that he is an alien until a route produces strong public evidence. Even then, final wording can preserve uncertainty if the campaign has not proven it.

### Country-specific flavor

Dynamic text can mention:

- Universities.
- Academies.
- Military research offices.
- Industrial firms.
- Private workshops.
- Exile scholars.
- Colonial institutes.
- Rural test ranges.
- Naval or aviation laboratories.

The system should select a flavor frame that fits the host. It should not invent a major university in a state where none makes sense.

### Event text surfaces

#### Appointment event

Viewpoint:

Government receiving an extraordinary offer.

Visible information:

Demonstration, request, biography gaps, immediate utility.

Hidden information:

Origin, future projects, rebellion capacity, terminal branches.

Tone:

Curious, uneasy, opportunistic, or urgent based on host context.

#### University and policy events

Viewpoint:

Researchers, ministers, firms, and institutions competing for access.

Tone:

Specific institutional rivalry, prestige, resource pressure, and genuine scientific excitement.

#### Foreign events

Viewpoint:

Diplomats, intelligence services, scientists, or security staff.

Tone:

Strategic and personal. Avoid generic diplomatic-note language when a concrete invitation, disappearance, theft, or attack can be described.

#### Project events

Viewpoint:

People who observe an actual test, accident, specimen, machine, signal, or impossible result.

Tone:

Concrete and sensory. Do not label the event as a warning. Show what happened and what people fear or cannot explain.

#### Sovereignty events

Viewpoint:

Government and laboratory power centers.

Tone:

Political and material. Use guards, procurement, territory, archives, and project units. Do not reduce the crisis to abstract constitutional phrases.

#### Kruger State events

Viewpoint:

A new state trying to govern laboratories, unusual populations, and a hostile border.

Tone:

Route-specific. Human, clone, machine, bestiary, temporal, and synthesis routes need distinct vocabulary and public concerns.

### Option direction

Important options should communicate stance and visible consequence.

- Public appointment can sound confident or proudly academic.
- Secret appointment can sound urgent and controlled.
- Rejection can sound suspicious, cautious, or darkly practical.
- Project approval can sound ambitious, desperate, or morally compromised.
- Safety refusal can sound principled or fearful.
- Charter can sound like negotiated surrender of sovereignty.
- Confinement can sound decisive while acknowledging uncertainty.
- Assassination can sound grim and irreversible.
- World-end options must be restrained and severe.

Do not provide bland `OK`, `We must act`, or `This is terrible` buttons.

Cultural references, slogans, quotations, and song fragments require research. Do not invent them during implementation.

### Event Details and catalog

Event Details text describes:

- A scientist appearing.
- His impossible breadth.
- The transformation of national institutions.
- Foreign interest and uncertainty.

It does not list modifiers, projects, armies, hidden paths, or achievements.

### Dynamic placeholders

Final localisation should use dynamic names for:

- Host country.
- Recipient country after transfer.
- Primary laboratory state.
- Foreign actor.
- Selected project family.
- Current public governance model.
- Current dominant Kruger route.
- Former host.
- Kruger State cosmetic identity.
- Visible project or singularity stage.

### Writing prohibitions

- No em dash.
- No semicolons in sentences.
- No staccato chains.
- No thesis-antithesis-synthesis formulas.
- No staged official-denial contrast formulas.
- No generic apocalypse filler.
- No implementation-history language.
- No effect lists in Event Details.
- No hidden-route spoilers.
