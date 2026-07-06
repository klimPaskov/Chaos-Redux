# Event 011 Secret Alliance Spec Part 4: AI, Balance, Assets, And Acceptance

## Pact AI

Pact members are the event's engine. Their AI should not be decorative.

Member AI weights should consider:

- role
- commitment
- ideology relative to player and organizer
- border adjacency
- player strength
- current wars
- stability
- equipment and manpower
- exposure level
- pact cohesion
- world tension and chaos pressure

Organizer AI should:

- maintain cohesion
- recruit only valid candidates
- avoid reveal until the pact can survive, unless war forces it
- seek a major sponsor at Evolution II when eligible
- choose sabotage, recruitment, or provocation based on pressure and exposure
- replace itself if invalid only through approved validity rules

Major sponsor AI should:

- prefer proxy pressure before reveal
- join only when not at war with the player
- weigh player dominance, ideology, distance, faction obligations, and war risk
- avoid suicidal immediate reveal unless the event's crisis state demands it

Revealed faction AI should:

- call members into the player war
- prioritize front defense for border members
- use naval, expeditionary, or support pressure for remote members
- keep reluctant members less aggressive but still obligated unless split or delayed

## Player-Side AI

If the target player country is AI in observer or automated tests, it should use simplified equivalents:

- investigate when pressure is high and stability is safe
- prepare when known border risk exists
- expose when evidence is high and readiness is adequate
- negotiate with low-commitment members
- avoid border incidents during equipment or manpower collapse

AI must use the same scripted effects and validity triggers as human decisions. It should not depend on a human selected-target flag.

## Balance Goals

The event should be dangerous but not arbitrary.

Baseline:

- low impact
- clear unease
- no heavy damage

Evolution I:

- more reports
- mild pressure
- more members

Evolution II:

- active damage and counterplay
- major sponsor possibility
- strong but manageable costs

Evolution III:

- public crisis
- likely war
- high payoff for earlier readiness, evidence, and split-member work

Reveal war:

- serious coalition threat
- prepared players should feel the difference
- unprepared players should understand why the situation escalated

## Exploit Guards

High severity guards:

- reveal should process once per war cascade
- border wars should have no state transfer by default
- border war farming needs target and state-pair cooldowns
- exposure rewards need evidence costs and cooldowns
- negotiation cannot remove the whole pact cheaply
- members invalidated by annexation, capitulation, subject conversion, or player faction membership must be pruned
- reveal must not drag unrelated third-party factions into war through unsafe hidden membership

Medium severity guards:

- dynamic cost triggers and completion effects must remove the same resources
- active mission cap must apply to all activation paths
- selected target state must clear when target becomes invalid
- repeated sabotage needs state and packet cooldowns
- public awareness without evidence needs leak containment options

Low severity guards:

- replace early investigation decisions with public crisis decisions in Evolution III to reduce clutter
- AI should not spend scarce trains, convoys, or fuel during unrelated disaster wars
- reports should not spam every hidden pulse

## Assets

Use `chaos-redux-event-assets` for final asset production.

Static asset families:

| Asset | Use | Source mode | Notes |
| --- | --- | --- | --- |
| report image: secret meetings | opening and baseline reports | generated | clandestine delegates, sealed files, no readable generated text |
| report image: courier network | Evolution I reports | generated | rail, port, or embassy routes |
| report image: sabotage aftermath | Evolution II sabotage reports | generated | damaged rail/factory/port, period tone |
| report image: public compact | Evolution III reports | generated | public delegation or flags emerging from secrecy |
| super-event image | reveal | generated unless final research changes it | 457x328 final target |
| decision category icon | countermeasures category | generated icon | dossier, seal, or cipher-board symbol |
| decision icons | investigate, prepare, expose, negotiate, counter-sabotage, border war | generated icons | 32x32 decision family coverage |
| idea icons | suspicion, preparation, sabotage, pact pressure | generated icons | 64x64 |
| faction emblem | public pact faction | generated emblem | must be registered before final art naming is locked |
| achievement icons | Event 011 achievements | generated icons | 64x64 |

Avoid real historical meeting photos unless the final text explicitly names the historical source context. This pact is fictional and campaign-dynamic.

## Animation

Use `chaos-redux-frame-animation` only if implementation adds animated UI or animated sprite surfaces.

Candidate animated assets:

- sealed dossier pulse for high exposure
- cipher-line warning for high threat pressure
- border warning frame for neighboring pact member crisis
- broken seal reveal asset for public reveal

Final animated assets must be frame sheets with real source frames, static fallbacks, manifests, and `.gfx` or `.gui` handoff notes. Do not use transform-only or GIF-only animations as final in-game assets.

If the final implementation uses ordinary decisions only, keep animation optional and compact. Do not add a large scripted GUI merely to display animation.

## Super-Event Direction

Use `chaos-redux-super-events` for final super-event implementation.

Trigger role:

- first public reveal of the anti-player pact
- faction formation
- collective war commitment

Working title direction:

- `The Hidden Front`

Working quote direction:

- Luke 8:17 KJV, source-verified in the research handoff

Working button or remark direction:

- `In battalions.`, Shakespeare allusion from `Hamlet`

Image direction:

- period-authentic fictional documentary mood
- clandestine council becoming public
- sealed documents, radio cables, shadowed delegates, and an anti-player map
- no readable generated text
- avoid generic map-only art and modern intelligence walls

Audio direction:

- restrained, conspiratorial, martial
- public-domain or clearly licensed
- do not reuse another super-event track without approval and documentation

## Achievement Hooks

Working achievement hooks:

| Working id | Challenge |
| --- | --- |
| `secret_alliance_all_lamps_lit` | reveal every current member before Evolution III public reveal |
| `secret_alliance_clean_break` | split a founding member without entering war with any pact member first |
| `secret_alliance_no_first_shot` | defeat the revealed pact war without escalating a border clash into formal war |
| `secret_alliance_iron_curtain_raiser` | win the defensive pact war after reaching readiness and industrial security thresholds |
| `secret_alliance_border_sentinel` | win multiple pact border clashes without losing one and without formal war during those clashes |
| `secret_alliance_smoke_without_fire` | expose the pact through observers and proof while keeping public awareness below panic |

Achievement text and icons need a later implementation pass. Decision text must not mention achievements.

## Localisation Direction

Final localisation should:

- use in-world language
- describe current state and choices, not implementation history
- avoid saying the event was reworked or newly added
- avoid exposing hidden future reveal logic
- keep early text uncertain and investigative
- make Evolution III public and concrete
- show costs and blocked requirements with short icon-first text and custom tooltips
- use scripted localisation for dynamic state, counts, target names, and state or border names where supported

No final localisation strings are provided in this spec.

## Required Implementation Acceptance Criteria

A future Event 011 implementation is complete only when:

- `chaosx.nr11.1` initializes a hidden anti-player pact with three valid founders or fails cleanly before visible effects
- the pact target, organizer, founders, members, roles, values, arrays, and event targets are saved and cleaned correctly
- no visible faction exists before public reveal or Evolution III public bloc state
- Evolution I adds minors and stronger reports
- Evolution II unlocks countermeasures, active sabotage, provocations, and one major sponsor path
- Evolution III can create a public bloc and near-war state without forcing instant war unless reveal conditions fire
- any pact member entering war with the player reveals the pact, creates the faction, triggers the super-event, and calls valid members into the intended war
- decisions and missions have concrete costs beyond political power and meaningful success, failure, partial success, AI, and cleanup
- border wars use no state transfer by default and have cooldowns and cleanup
- AI exists for members, organizer, major sponsor, player target, and revealed faction behavior
- constants and MTTH entries own timing, caps, costs, weights, and thresholds
- event logs, event details, event name mappings, super-event integration, localisation, icons, docs, and spreadsheet/catalog alignment are updated
- no recurring daily, weekly, or monthly world iteration is introduced without explicit user approval

No simplifications are approved by this source package.

