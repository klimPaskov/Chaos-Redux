# 011 Secret Alliance, part 4, AI, assets, achievements, and completion design

## AI design overview

AI behavior must make the pact feel intentional. The implementation should not rely on flat weights. Countries should join, escalate, defect, and negotiate based on motive, geography, ideology, fear, and opportunity.

AI actor groups:

- hidden full signatories
- outer-ring liaisons and armed associates
- major patron
- second major candidate in Evolution III
- neutral observer countries
- player allies and faction members
- innocent suspected countries
- neighbors of the player

## Member motive types

| Motive working label, not final localisation | Who tends to have it | Behavior |
| --- | --- | --- |
| Defensive fear | weak neighbors, recent victims of player expansion | Joins for protection, defects if offered safety and evidence is high |
| Ideological hostility | opposed ideology, propagandist governments | Runs agitation, resists compromise, likely full signatory |
| Border revenge | countries with claims or lost states | Prefers border incidents and war planning |
| Patron dependency | minors dependent on a major patron | Follows patron, may defect if patron weakens |
| Opportunist | countries seeking territory or status | Joins when pact looks strong, withdraws if risk rises |
| Diplomatic idealist | nervous democracies or neutrals | Prefers inquiry and defensive language, avoids sabotage if exposed |
| Covert militarist | authoritarian army-led states | Prefers sabotage, assassinations, and secret armament |

AI should choose incidents and decisions based on motive. Defensive fear should not act like covert militarism.

## AI pact member behavior

Hidden members should:

- build pact cohesion when the player looks threatening
- invite compatible countries when cohesion and confidence are high
- avoid invitation spam when cohesion is low
- prefer deniable actions while Evidence is low
- burn evidence after player investigations succeed
- increase aggression when a major patron joins
- hold back from war if Preparedness is high and cohesion is low
- leak evidence if low stability, low confidence, or ideological mismatch exists

Public members should:

- join the faction when full signatory status is confirmed
- coordinate war entry when reveal is hard triggered
- seek separate peace or exit if cohesion collapses and their motive is defensive or opportunist
- continue war if major patron, ideological hostility, or border revenge is strong

## AI major patron behavior

A major patron should not join casually. It should join when it has reason to believe opposing the player is strategically useful.

Patron selection factors:

- player is strong or expanding near the patron's region
- player ideology opposes patron ideology
- player has high world tension contribution
- player is a rival or enemy of patron allies
- patron has enough industry and army to matter
- patron is not already overwhelmed by war
- patron can plausibly influence several minors

Patron behavior:

- funds armed associates
- hides behind minors until Evidence grows
- pushes propaganda when player isolation is high
- delays war if player Preparedness is high
- accelerates war if player is distracted by another war
- may abandon minor members if cohesion collapses before reveal
- may seize leadership once public

Second major candidate in Evolution III:

- should be rare
- should require high pact cohesion, high player isolation, or player failure to expose the first patron
- should create leadership tension if ideological alignment is weak
- should not produce incoherent alliances among sworn enemies unless the world is chaotic enough and the design makes it a fearful anti-player bargain

## Neutral and ally behavior

Neutral countries can react without joining the pact.

Neutral observers:

- can certify evidence if relations and credibility allow
- can refuse inquiry if the player is isolated
- can pressure both sides to avoid war
- can become sympathizers if player aggression is high

Player allies:

- should receive reactions when the pact becomes public
- may provide intelligence support, volunteers, or guarantees depending on faction rules
- should not automatically know hidden members unless the player exposes evidence or ally intelligence is strong

Innocent suspected countries:

- should suffer relation damage from reckless player accusations
- can become closer to the pact if humiliated
- can support the player if cleared by inquiry

## Existing focus tree interaction

Secret Alliance should not create full new focus trees for random pact members. The event selects existing countries from the campaign, and replacing their focus trees would damage compatibility and identity. Instead, pact members keep their existing trees and receive event-owned decisions, ideas, AI strategies, and faction behavior.

This event is therefore a decision, event, AI, and super-event system rather than a random-country focus tree system.

## National spirits and ideas

Use a small number of strong, readable ideas rather than many tiny modifiers.

Player-side ideas:

| Idea working label, not final localisation | Purpose | Lifecycle |
| --- | --- | --- |
| Dossier Pressure | Represents the government operating under hidden foreign pressure | Appears when dossier opens, upgrades or removes after reveal |
| Hardened Internal Lines | Represents successful defensive preparation | Built through decisions, converts into reveal-war benefit, expires after crisis |
| Diplomatic Encirclement | Represents pact propaganda and neutral doubt | Rises when isolation is high, can be reversed by evidence and inquiry |
| Surprise Mobilization Shock | Penalty only if reveal happens with low Preparedness | Temporary post-reveal weakness |

Pact-side ideas:

| Idea working label, not final localisation | Purpose | Lifecycle |
| Hidden Signatory Network | Hidden coordination among members | Active before reveal, converts into public faction idea or is removed |
| Patron Channels | Major-backed funding and planning | Appears in Evolution II, weakens if Patron exposed or defeated |
| Open Anti-Player Pact | Public war bloc identity | Appears after reveal, scaled by cohesion and readiness |
| Fractured War Table | Low-cohesion public pact penalty | Appears if player weakened the pact before reveal |

Idea effects should matter. Avoid tiny modifiers as the main effect. Each idea should alter sabotage defense, diplomacy, war readiness, intelligence, supply, mobilisation, faction cohesion, or war behavior in visible ways.

## Asset plan overview

The asset package should focus on the dossier, the super-event reveal, decision icons, national spirits, and achievements. There are no fixed new country flags because members are random existing countries and keep their own flags. The public faction may need an emblem or super-event iconography, but not a country flag.

Static assets:

- decision category icon for the dossier category
- decision icons for investigation, counter-sabotage, diplomacy, border watch, exposure, and war preparation
- idea icons for player pressure, hardened internal lines, diplomatic encirclement, hidden signatory network, patron channels, open pact, and fractured war table
- super-event image for public reveal
- faction emblem or seal for the Anti-[player country] Pact if the implementation supports faction emblem display
- achievement icons for all achievements

Animated assets:

- dossier seal with closed, active, urgent, public, and compromised states
- warning pulse for imminent reveal or high War Clock
- suspect card highlight for confirmed member, if custom GUI is used
- static fallback for each animated asset

Generated assets are appropriate because the event is fictional and symbolic. If the implementation uses real historical photographs for the super-event image, the asset source researcher must document source and license. Otherwise, generated period-authentic documentary or symbolic art is preferred.

## Super-event package overview

The super-event belongs to public reveal. The implementation must not use unresearched final title, button text, quote, cultural remark, or audio.

Super-event package needs:

- title direction from the super-event prompt
- description direction from the spec
- verified quote through super-event text research
- verified cultural remark or button direction through super-event text research
- unique licensed or public domain audio through super-event audio research
- super-event image through event asset workflow
- settings-aware playback wiring
- event docs and catalog alignment after implementation

## Achievements

Achievements are included because the event has a deep playable system, rare evolutions, a reveal super-event, and several mastery routes. They should not unlock just because the event fired.

| Achievement id working key | Visibility | Difficulty | Route |
| --- | --- | --- | --- |
| chaosx_secret_alliance_read_the_room | visible | medium | Identify at least two full signatories before public reveal without triggering premature exposure |
| chaosx_secret_alliance_every_door_locked | visible | hard | Reach public reveal with high Preparedness and prevent any severe sabotage from succeeding |
| chaosx_secret_alliance_the_empty_chair | hidden | hard | Force the Convener or a major patron to withdraw before reveal through evidence and negotiation |
| chaosx_secret_alliance_pact_against_me | visible | medium | Survive the reveal war until the first pact member capitulates or exits |
| chaosx_secret_alliance_no_shadow_left | visible | very hard | Collapse the pact after reveal while keeping strong evidence and preventing outer-ring members from joining the war |
| chaosx_secret_alliance_bad_guess | hidden | challenge | Accuse an innocent country, recover diplomatic credibility, and still expose the real pact before war |
| chaosx_secret_alliance_three_knives_one_table | hidden | hard | Reveal all original three full signatories before Evolution II adds a major patron |
| chaosx_secret_alliance_public_enemy_number_one | hidden | very hard | Trigger Evolution III with two majors in the pact, then defeat or force exit from the full public faction |
| chaosx_secret_alliance_quietly_undone | hidden | very hard | Dissolve the hidden pact before public faction formation through exits, evidence, and cohesion collapse |

Achievement text should be written during implementation from direction only. Icon directions appear in the achievement prompt.

## Localisation handoff

The implementation should write final localisation from these directions:

- event name should retain Secret Alliance as the catalog identity
- early report titles should focus on observed incidents rather than naming the pact
- options should sound like government reactions, not generic `OK` buttons
- the decision category should use dossier, investigation, security, or cabinet language depending on final style
- super-event title and button text require research gate and should not use working labels
- Event Details should describe the situation and premise without listing exact effects
- evolution text should describe new pact behavior without revealing hidden future stages
- decision tooltips should clearly show concrete costs and blocked requirements
- achievement descriptions should describe route goals without spoiling hidden member selection too early

## Acceptance principles

The implementation should be considered incomplete if:

- the pact does not remember hidden-phase Evidence and Preparedness after reveal
- decisions are mostly political power purchases
- hidden members can be selected while at war with the player at creation
- reveal does not form a public faction when a pact country goes to war with the player
- the super-event lacks researched quote, remark, image, audio, and wiring
- AI pact behavior is flat or nonsensical
- the decision category shows a wall of targets without phase control
- sabotage continues in hidden form after the pact is public
- achievements are automatic or trivial
- assets are missing, unwired, or undocumented

## Anti-bloat note

This event should not become a full country-package or focus-tree generator. Its strength is that it can wrap around the existing world and make random countries feel like they are secretly coordinating. Adding full bespoke focus trees for every possible member would weaken compatibility and delay the main mechanic. The implementation should keep the event deep through decisions, values, AI, diplomacy, reveal memory, and super-event presentation.
