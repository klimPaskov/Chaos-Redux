# Event 31 Random Terror specification

## Part 11: Assets, presentation, and localisation direction

## Presentation strategy

Event 31 needs strong visual identity across four scales.

- national crisis response
- named fictional organizations
- territorial extremist countries
- terminal False Revelation campaign

The presentation should help the player distinguish state activity, organization profile, country route, and evolution.

It must not use real extremist imagery, sacred calligraphy, modern tactical aesthetics, or generic map diagrams as the main art.

## Decision-category presentation

### Government response category

Presentation layer: ordinary decision category with one static category picture.

The picture should show a period emergency response involving damaged transport, guarded civilians, relief workers, and security personnel.

The scene should communicate protection, uncertainty, and material disruption.

It should avoid:

- a modern command center
- a tactical map covered in arrows
- visible real flags or organization symbols
- a staged propaganda poster
- fake UI controls
- unreadable generated text

### Territorial actor category

Presentation layer: ordinary decision category with one static category picture.

The picture should show an improvised command center inside captured civic or industrial space, with damaged infrastructure and mixed militia or defecting regulars.

It must remain fictional and period-authentic.

### Final state category

Presentation layer: ordinary terminal decision category with a distinct static picture.

A full custom GUI remains unnecessary.

The image should show the altered command environment and worldwide uprising state without depicting a deity.

## State and map presentation

The event needs an event-owned state map mode or map highlight family.

Required states:

- dormant activity
- active cell
- entrenched network
- armed insurgency
- lost local control
- current government operation target
- current corridor or safe-haven connection

Color and icon treatment must include non-color cues such as borders, symbols, patterns, or tooltips.

The map mode should name the state, activity stage, organization, current mission, and broad next risk.

It should not expose hidden incident probability or Apocalyptic Readiness.

## Report and event art inventory

The event should use a curated report-art family.

Recommended generated period-documentary scenes:

1. damaged railway and civilian evacuation
2. guarded station and emergency transport
3. hostage or public-building crisis shown indirectly
4. burned depot and captured equipment aftermath
5. intelligence raid aftermath with recovered documents
6. relief workers and victims after an attack
7. border corridor under military protection
8. armed enclave in a captured town
9. defecting soldiers or police joining an insurgency
10. government capital under emergency guard
11. rival extremist groups fighting in an urban or border setting
12. local religious and civic leaders rejecting the fictional jihadist movement
13. territorial actor proclamation inside a captured public building
14. jihadist international gathering using wholly fictional emblems
15. synchronized uprising during the Final Jihad
16. defeat, liberation, and reconstruction aftermath

These images can be generated because the incidents and organizations are fictional and need unique compositions.

They should use 1936 to 1945 photographic technology, clothing, vehicles, architecture, and documentary framing.

Readable generated text, modern weapons, modern body armor, cinematic color grading, and real organization imagery are forbidden.

## News-art inventory

Major public milestones need wider news treatment.

Recommended news images:

1. first large coordinated international attack wave
2. first durable territorial extremist country
3. creation of the Jihadist International
4. activation of the Final Jihad
5. defeat of a major territorial network
6. defeat aftermath of The False Revelation

The False Revelation reveal itself uses dedicated super-event art.

## Leader portrait pool

The event can create many simultaneous fictional countries.

It needs a prebuilt portrait pool large enough to avoid obvious duplicate leaders in one campaign.

Recommended minimum full leader pool:

- `6` fictional military-command leaders
- `6` fictional clandestine or council delegates
- `6` fictional revolutionary or ideological leaders
- `6` fictional criminal-political leaders
- `6` fictional millenarian or cult leaders
- `8` fictional jihadist-route leaders
- `6` fictional institutional council portraits
- `1` False Revelation entity portrait

Total recommended leader and council masters: `45`.

The final count can rise after live carrier and simultaneous-actor limits are verified.

Every one-person portrait uses the `fictional_high_chaos` route through `chaosx_portrait_creator`.

Each portrait should have:

- `156x210` framing
- period photographic treatment
- role-specific clothing
- a memorable fictional motif
- varied age, gender, appearance, pose, and regional context without stereotype
- no real-person target
- no real extremist symbol
- no modern equipment
- no readable text
- matching name and gender metadata

Council portraits are fictional institutional assets and require explicit group or symbolic composition briefs.

The pool should be manually reviewed for accidental resemblance, repeated faces, stereotype, drift, and route mismatch.

## Advisor and commander portrait authorization

Separate advisor dossier portraits are not authorized as a blanket family.

The final country-package implementation should first determine which advisors or commanders add meaningful gameplay.

For the accepted minimum package, authorize up to `12` route-critical fictional characters across the shared actor framework.

Possible roles:

- field commander
- quartermaster
- civil administrator
- foreign liaison
- intelligence chief
- ideological organizer

A character used in both leader and advisor roles needs separate role-specific outputs and wiring.

Do not infer or generate a broad advisor roster from every focus or idea.

## False Revelation portrait animation

One animated entity portrait or transparent portrait overlay is authorized.

The animation should show subtle impossible change, such as unstable shadow, shifting reflected light, or a presence that appears optically inconsistent.

Requirements:

- separately generated or edited source frames
- stable identity, camera, framing, and anchor
- static `156x210` fallback
- horizontal frame-sheet PNG and DDS
- preview GIF for review only
- verified `.gfx` and GUI consumer
- no transform-only motion
- no simple filter pulse
- no fake sacred imagery

The animation should be reserved for the terminal state and removed when that leader is no longer active.

## Flag pool

The event needs enough flat fictional flags for simultaneous territorial actors.

Recommended minimum:

- `24` ordinary Event 31 base flag designs
- `8` jihadist-route flag designs
- `4` merger or transnational-command flag designs
- `1` final False Revelation flag design

Every design needs normal, medium, and small HOI4 variants.

All final flags use ImageGen and follow the flat flag workflow.

Required design qualities:

- strong geometry
- clear contrast
- readable small size
- no text
- no real organization symbol
- no sacred calligraphy
- no fabric folds
- no perspective
- no gradients or lighting
- no invented claim that resembles a real community symbol without review

The ordinary pool should cover military, clandestine, revolutionary, criminal-political, and millenarian profiles.

Jihadist flags should use wholly fictional geometric symbols and colors with no copied real emblem.

## Faction emblems

Required emblem families:

- regional Event 31 coordination structure
- transnational network confederation
- Jihadist International
- Final Jihad command
- possible anti-Event 31 terminal coalition only if the existing faction UI requires a dedicated emblem

Each emblem is a separate asset designed for the faction surface.

It cannot be a resized country flag.

## Focus icons

The shared focus framework needs a broad coordinated icon set.

Recommended minimum by branch:

- opening survival: `6`
- Shadow Council: `10`
- War Directorate: `10`
- Ideological Secretariat: `10`
- Captured Economy: `12`
- Armed Movement: `12`
- Network and Diplomacy: `12`
- Expansion and State Capture: `12`
- Crisis and Failure: `8`
- Jihadist International: `12`
- Final Jihad and terminal route: `10`

Recommended total: about `114` focus icons before exact tree count.

The implementation agent should finalize the count after the actual focus tree is built.

Each icon must be designed for `94x86` focus presentation.

Focus icons cannot be resized idea or decision icons.

## Idea and national-spirit icons

Required lifecycle families:

- Improvised Command and route upgrades
- Captured Economy and route upgrades
- Contested Legitimacy and route upgrades
- Presence of the Entity
- World in Revolt
- Supply Through Ruin
- government recovery and response-capacity ideas when implementation confirms they are persistent

Recommended planned total: `18` to `24` idea icons.

Each lifecycle stage needs a distinct compact `64x64` composition when the visible idea identity changes.

A minor numerical upgrade can reuse the same icon when the institution remains visibly the same.

## Decision and mission icons

Required government action families:

- response cell
- transport protection
- victim support
- intelligence sweep
- security surge
- targeted raid
- finance and corridor disruption
- allied intelligence
- defection channel
- movement restriction
- community-site protection
- sponsor exposure
- military reinforcement
- capital security
- enclave isolation
- relief corridor
- retake operation
- surrender negotiation
- foreign intervention
- reconstruction

Required actor action families:

- militia recruitment
- unit integration
- depot capture and repair
- external supply
- sponsor agreement
- foreign cell support
- actor merger
- faction leadership
- state offensive
- territorial administration
- jihadist unity
- coordinated uprising
- terminal command objective

Decision icons should use simple strong silhouettes designed for their actual final size.

Mission icons remain a separate family when the UI surface requires them.

## State-modifier icons

Required activity icons:

- dormant
- active
- entrenched
- armed insurgency
- lost local control
- recovery or restored authority

Additional state icons can cover:

- damaged transport
- relief corridor
- safe haven
- foreign corridor
- capital infiltration
- forced rule

These icons should remain readable beside state modifiers and map tooltips.

## Achievement icons

Part 12 defines `12` achievements.

Every achievement needs:

- completed `64x64` icon direction
- grey state
- not-eligible state
- stable achievement filename triplet
- event-specific symbolism

Achievement art must not reuse a focus or decision icon through resizing.

## Super-event images

Required super-event images:

1. The False Revelation reveal
2. Defeat of The False Revelation

Possible later major milestones can use normal news events unless implementation proves a separate super-event is justified.

The reveal image should be generated, period-authentic, ambiguous, and focused on the entity's appearance and human reaction.

The defeat image should show liberation, ruins, survivors, and the uncertain absence of the entity.

Neither image should depict Allah, sacred calligraphy, real extremist symbols, modern equipment, or fantasy concept-art framing.

## Super-event audio

Each super-event requires a unique licensed or public-domain musical recording.

The audio researcher must verify composition and recording rights separately.

The final cue should normally last one to two minutes and be converted to the established game-ready WAV format.

Generated audio, test tones, drones, sound-effect beds, Quran recitation, the call to prayer, Islamic sacred chant, unlicensed commercial recordings, and undocumented repository audio are forbidden.

The reveal and defeat need different tracks.

## Super-event text research

The final title, button text, quote, and cultural reference remain research-gated.

The text researcher should compare several candidates and record exact sources and confidence.

Preferred quote themes:

- false prophecy
- coercive belief
- deception
- idolatry
- judgment
- resistance to false authority
- survival after fanatic rule

The final quote should be concise enough for the UI and should avoid using Islamic scripture as hostile branding.

## Localisation direction

### Event titles and reports

Use specific incident and state context.

Mention the affected state, government, organization, corridor, sponsor, or territorial actor when known.

Avoid generic crisis language, dramatic filler, and map-summary prose.

### Organization names

Use fictional names that fit the profile and region without copying real organizations.

Do not place an ordinary ethnic, religious, or national group name beside a generic terror label.

### Government decisions

Describe the action, exact target, resource commitment, public risk, and visible consequence.

Costs remain concise and icon-first.

### Extremist-country focuses

Each route needs a distinct voice.

- Shadow Council uses controlled secrecy and internal discipline
- War Directorate uses military command and territorial necessity
- Ideological Secretariat uses doctrinal authority and state-building
- criminal-political variants use patronage, extraction, and coercive bargains
- jihadist variants use fictional absolutist religious claims while preserving clear opposition by Muslim actors
- terminal text focuses on the entity's command, uprisings, coercion, and uncertainty

Do not copy real propaganda or sacred text.

### Muslim opposition

Describe local leaders, scholars, soldiers, communities, and governments rejecting the movement's claim, protecting civilians, preserving worship and public life, and supporting resistance.

Do not reduce the content to a disclaimer.

The opposition should appear in events, decisions, focus effects, and AI behavior.

### Victims and civilians

Describe human consequences, emergency services, missing people, damaged transport, displacement, and reconstruction.

Avoid turning every death report into spectacle.

### Event Details

Describe the premise and public progression.

Do not expose hidden readiness, exact probability, future surprises, or the identity of the entity.

### Spreadsheet wording

Event details, evolution details, scenario details, and world-end details should match the final in-game wording.

The authoritative workbook remains the only editable catalog source.

## Source and manifest rules

Every asset package needs:

- source mode
- exact asset type
- stable filename
- target size
- final DDS path
- sprite proposal
- prompt or source record
- generated source PNG or archived source
- processed preview
- contact sheet
- status
- reviewer notes
- final runtime hash after wiring

Temporary work belongs under the event-scoped asset workspace while implementation is active or blocked.

Before full completion, durable provenance and handoff facts move into permanent event or plan documentation, runtime files move to engine folders, no runtime reference points into `docs/assets/`, and the temporary event workspace is deleted.

The durable portrait archive remains separate and is not deleted.

## Asset review gates

The asset package is complete only when:

- every accepted asset row has a runtime consumer
- no required asset remains a placeholder
- flags are flat and distinct
- portraits are fictional, varied, and free of real-person targeting or stereotype
- icons remain readable at final size
- transparent assets have real transparency
- no focus, idea, decision, mission, achievement, or faction family is satisfied by resizing another family
- super-event image, text, quote, and audio agree
- entity animation has real source frames and a static fallback
- no real extremist symbol or sacred hostile branding appears
- all final DDS files, manifests, and wiring handoffs exist
