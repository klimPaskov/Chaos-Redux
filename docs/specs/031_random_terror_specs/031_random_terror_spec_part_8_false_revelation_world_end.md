# Event 31 Random Terror specification

## Part 8: The False Revelation world-end branch

## Implementation status

Implemented: the initial gate (Chaos `1000+`, Evolution V, public toggle, readiness, unity, territory, crisis states, strategic victories), the delayed transition with an acceleration decision, the entity as a gated final leader with five research slots, the three objective-based strengths as dynamic modifiers recomputed from world state (R38), the opening uprising wave limited to governments with real pressure and an active state, the Terminal Counteroffensive (D12), the reveal and defeat super-events with researched text, art and audio, and the world-threat source (R47).

Open, from the completion audit:

- C01 terminal access: the government response category is hidden once `world_end` is set, so the counteroffensive and the emergency missions cannot be used after the transition. See World-end transition below.
- C02 player control is implemented: a human dominant actor is asked (`chaosx.nr31.12`) to accept, contest or keep an independent command before any promotion or merger, and an unanswered choice falls back to accepting after 30 days. Contesting makes the actor a rival claimant that goes to war with the final command when the revelation commits, independence keeps it outside the command without a war, and when every viable actor declined, a free carrier is split off the declining actor with half of its territory outside the capital and a share of its forces. AI jihadist actors choose between subordination, rivalry, merger into the final command and collapse into cells (the last two only when weak); non-jihadist actors are never subordinated automatically. Two-player transition evidence is still missing.
- C03 commit revalidation: the delayed commit does not recheck the full gate. See Delayed transition.
- C04 strategic victory and unity: the victory counter increments even when a takeover fails, does not distinguish major victories, and unity counts every actor. See Major strategic victory.
- C10 campaign beats and aftermath: see the two sections below, both revised by the 2026-10-10 audit.
- The entity animation is shown in the Evolution V detail before the revelation. It must stay static until the terminal state exists.

## Terminal role

The False Revelation is Event 31's public world-end branch.

It marks the transition from a global extremist war to a terminal campaign led by an ambiguous supernatural or impossible entity.

The branch must feel larger than a strong Evolution V offensive.

It changes leadership, unifies or subordinates existing actors, synchronizes uprisings, activates terminal abilities, freezes ordinary random-event progression, and gives the world a final counter-campaign.

The branch is public in Event Details and has its own persistent enable toggle.

Disabling the branch does not disable Event 31, the jihadist route, or the Final Jihad.

## Ambiguity rule

The entity appears before the extremist leadership and is proclaimed divine by the movement.

The game never confirms that the entity is Allah.

The entity can be interpreted as:

- a demon
- an alien intelligence
- a temporal anomaly
- a psychic or technological projection
- a mass hallucination
- a constructed fraud with impossible effects
- another supernatural force

The event must preserve uncertainty.

No hidden tooltip, leader biography, Event Details text, achievement, asset manifest, or final localisation should reveal a canonical answer.

The entity is an impossible fictional leader and may use native ImageGen.

Its followers' claim is part of their ideology, not a statement by the game.

## Religious representation

The world-end branch must make Muslim opposition visible and consequential.

Fictional Muslim religious authorities, communities, soldiers, scholars, and governments can reject the claim, protect civilians, organize resistance, encourage defections, and join the final coalition.

The branch must not depict Allah.

It must not use Quranic calligraphy, Quran recitation, the call to prayer, sacred chant, or another Islamic sacred practice as hostile branding or enemy audio.

It must not use real extremist symbols or reproduce real propaganda.

The entity's art should focus on ambiguous physical presence, altered light, followers, damaged architecture, or impossible atmospheric effects.

It should avoid a direct sacred iconography claim.

## Eligibility

The branch becomes eligible only when all public and hidden requirements are satisfied.

### Public requirements

- global Chaos is at least `1000`
- Evolution V, The Final Jihad, is enabled and recorded
- no world-end state already exists
- The False Revelation public branch toggle is enabled
- at least one viable jihadist territorial actor exists
- substantial extremist territorial success exists
- widespread active terror crises exist
- International Unity is high enough to support a common claim
- the movement has achieved at least one major strategic victory

### Major strategic victory

A qualifying victory can include:

- capture of an original national capital of a major or regional power
- destruction of a major counterterror coalition command
- successful unification of several territorial actors
- control of a broad connected regional bloc
- survival of a coordinated global offensive through a major campaign phase

A minor isolated state does not satisfy the requirement by itself.

A victory is counted only after the state transfer, capital capture or merger actually succeeds, and each qualifying victory is counted once.
International Unity for this gate counts only members of the Jihadist International and keeps the losses from rivalry and community rejection between refreshes.

### Hidden requirement

Apocalyptic Readiness must reach its threshold.

The value can rise through:

- controlled states and population
- captured capitals
- number and strength of member actors
- high-pressure foreign countries
- regional spread
- major victories
- successful leadership unification
- extremist control of strategic corridors
- prolonged Final Jihad activity

It can fall through:

- member defeat
- leadership rivalry
- loss of capitals
- falling International Unity
- destruction of safe havens
- successful defections
- religious and civic rejection
- restoration of high-pressure countries

The exact formula remains hidden.

Player-facing text can show broad signs that the movement is approaching final unification without exposing the threshold.

## Delayed transition

Eligibility does not trigger the branch instantly.

The branch uses its own delayed event with mean time to happen influenced by readiness, unity, territorial success, and leadership stability.

This gives the world a final chance to reduce readiness.

When the delay ends, the commit rechecks the complete public and hidden gate, that the host still exists, that no other world end began, and that the branch and Evolution V are still enabled.
A failed recheck cancels the pending transition without any partial change, and readiness must be rebuilt before a new delay starts.

A dominant actor can also attempt to accelerate the transition through a visible high-risk route, but it cannot bypass the `1000+` Chaos gate or public enable state.

## Dominant actor selection

The transition chooses one existing jihadist actor as the host or creates a safe final carrier from the shared registry when transformation of the existing actor would be invalid.

The dominant actor score considers:

- Network Authority
- International Unity contribution
- controlled territory and population
- captured capitals
- military strength
- surviving foreign cells
- external supply
- faction leadership
- recent victories
- internal rival support

A player-controlled actor should not be silently deleted.

When several player-controlled members exist, the transition should preserve control through faction subordination, a consent choice, or a clear player takeover rule defined for multiplayer.

## Revelation incident

The transition begins with an event at the selected command location.

The public sees:

- the entity's appearance
- extremist leaders accepting or contesting the claim
- synchronized movement orders
- fear, defections, and resistance
- a new final country identity
- the first global uprising wave

The event should describe observable reactions and uncertainty.

It should not state what the entity truly is.

Rival leaders can reject the claim and begin a final internal war.

That rejection should not cancel the world end after the terminal flag is set. It becomes part of the final campaign.

## World-end transition

The transition must:

- guard against an existing world end
- set the shared world-end state
- set a scenario-specific False Revelation flag
- activate the dedicated super-event
- stop ordinary random-event firing
- preserve Event 31 terminal missions and campaign logic, including a usable government response category with the Terminal Counteroffensive, Stop the Coordinated Uprising, Prevent Capital Seizure and Retake the Lost State
- transform or create the final state
- assign the entity as visible leader
- reconcile faction membership and actor mergers
- trigger uprisings in valid high-pressure countries
- set final values and objectives
- block incompatible future branches

The transition is one transaction.

A failed validation must not set the world-end flag or partially merge countries.

## Actor unification

Existing jihadist actors can enter one of four outcomes.

### Direct merger

Compatible AI actors or consenting player actors are absorbed into the final state.

Territory, units, stockpiles, technologies, characters, wars, and subjects are reconciled once.

### Subordinate command

An actor remains a country and joins the final faction under a terminal command relationship.

This is preferred when direct merger would break player control, geography, subjects, or wars.

### Rival claimant

An actor rejects the entity and fights the final state.

It loses access to the shared Final Jihad command but can cooperate with governments against the entity.

### Fragmentation

A weak actor collapses into cells, local enclaves, or defectors during the transition.

The unification system must not duplicate units, equipment, territory, technology, or leaders.

## Final state identity

The final state receives:

- a unique fictional country name and adjective
- a unique flat flag and faction emblem
- the ambiguous entity as leader
- a terminal politics identity
- five research slots
- a replacement focus route
- terminal decisions and missions
- extreme but staged national abilities
- a distinct world-threat source
- player-facing rules that explain its campaign objectives

The human population remains human.

The state is a special Chaos country and not an actual nonhuman country.

## Final state ideas

The final package should use a small number of powerful staged ideas.

### Presence of the Entity

Represents command cohesion, fear, recovery, and resistance to ordinary leadership disruption.

Its strength depends on command capitals, International Unity, and successful uprisings.

### World in Revolt

Represents synchronized cells and uprisings behind enemy lines.

Its strength depends on high-pressure countries and surviving networks.

### Supply Through Ruin

Represents captured depots, coerced transport, corridors, and extreme logistical adaptation.

Its strength depends on real controlled infrastructure, ports, supply hubs, and territory.

These ideas should change as the final campaign advances or loses key objectives.

They should not give unlimited power at full strength regardless of world state.

They are implemented as three scaling modifiers, each with a 0 to 100 score, a floor the coalition cannot remove, and a cap.

### Terminal presentation budget

The final command's category shows exactly the three strength scores, the state of the command capital, and one line naming what lowers each strength.
Raw International Unity, External Supply, readiness and counts stay out of the header.
Government players see the same three scores in the Terminal Counteroffensive tooltip, because those scores are what the coalition is trying to lower.

## Extreme abilities

The user brief requires intentionally extreme recruitment, organization, recovery, supply, resistance, uprising, expansion, and combat abilities.

The branch should deliver that power through staged systems.

### Recruitment

The final state can draw from controlled population, absorbed actors, foreign fighters, defecting units, and high-pressure uprisings.

It receives very strong recruitable-population and mobilization support.

It still needs population and equipment.

### Organization and recovery

The final state receives high organization recovery and reduced disruption while the entity holds command centers and unity remains high.

Loss of command capitals or rival rejection weakens the effect.

### Supply

The state receives strong supply grace, captured-supply use, reduced out-of-supply penalties, and emergency corridor decisions.

It does not receive unlimited supply in an isolated empty state.

Ports, railways, hubs, convoys, fuel, and territory remain strategic targets.

### Resistance and occupation

The state can create Event 31 uprisings and resistance support in high-pressure countries.

Occupied states can face forced rule and atrocities that generate Deaths, Condemnation, and resistance.

High Response Legitimacy and successful local opposition reduce conversion.

### Expansion

The final state receives rapid war planning, coordinated war goals, and terminal objectives against coalition command regions.

It should prioritize connected fronts and strategic capitals.

### Combat

The state receives strong attack, defense, breakthrough, planning, reinforcement, and recovery bonuses while it holds its command capital and keeps its strengths high.

These bonuses scale down when the entity loses command sites, International Unity collapses, or the final network is severed.

## Uprising system

The transition triggers uprisings only in countries with real Event 31 groundwork.

Uprising strength uses:

- Terror Pressure
- active state stage
- local captured equipment
- military defection
- Network Reach
- connected territorial actors
- government Response Legitimacy
- capital security
- current war and occupation

A country with zero pressure and no active cell cannot receive a full rebel army from the branch.

A high-pressure country can receive:

- sabotage and state modifiers
- temporary control loss
- defecting units
- a civil war actor
- state transfer to the final state when contiguous and valid
- a capital seizure mission

The setup should choose the outcome that fits geography and carrier capacity.

## Terminal campaign beats

The terminal campaign has no separate phase counter.
Its stages are readouts of the objectives the coalition and the final command fight over, so every beat is caused by something on the map.

- Revelation: the transition commits, the opening uprising wave rises where pressure is real, and governments receive Stop the Coordinated Uprising where their emergency slot is free.
- Offensive: while the command capital is held and the strengths stay high, the final command pushes connected fronts and the coalition targets command capitals, corridors and pressured countries.
- Forced rule: conquered states can suffer forced administration, expulsions and mass killing. These add Deaths, Condemnation and deportations through migration, and they raise resistance and defections, which lower the strengths over time.
- Resolution: the campaign ends in one of four outcomes.

The four outcomes are:

- the final command conquers or subordinates every meaningful opposition center
- the coalition destroys the final command and its surviving commands
- the entity disappears when all three strengths sit at their floors and the command capital is lost, leaving fragmented actors that fall back to ordinary Event 31 rules
- a rival claimant destroys the final unity, and the remaining commands fight each other as ordinary Event 31 actors

## Global counterplay

The world needs clear objectives beyond winning every front conventionally.

### Recapture command capitals

Each major command capital strengthens Presence of the Entity.

Recapturing and holding it weakens final bonuses and can free local resistance.

### Sever strategic corridors

Destroying or controlling named ports, rail links, border states, and supply hubs reduces Supply Through Ruin and prevents reinforcement of distant fronts.

### Restore high-pressure countries

Governments can lower Terror Pressure, protect capitals, support victims, and defeat uprisings.

Each restored country lowers World in Revolt.

### Support defectors and rival claimants

The coalition can encourage members, commanders, and communities to reject the entity.

This lowers International Unity and can create internal fronts.

### Protect religious and civic opposition

Fictional Muslim religious authorities and other threatened institutions can undermine the movement's claim, protect civilians, and support defections.

Their survival affects recruitment and legitimacy.

### Expose atrocities and coercion

Public evidence increases Condemnation, coalition participation, sanctions, resistance, and sponsor withdrawal.

### Destroy the central command

The final state should have one or more clear command sites whose loss changes its abilities.

The entity cannot become immune to every conventional objective.

## Coalition behavior

Existing factions can cooperate through a terminal coalition system without requiring every country to leave its faction.

The coalition can coordinate:

- intelligence
- command-capital targets
- relief corridors
- lend-lease
- volunteers and expeditionary support
- naval blockade
- air defense
- resistance support
- reconstruction after liberation

Membership and contribution depend on access, threat, ideology, relations, war state, and capacity.

Muslim-majority governments should be strong likely participants when targeted, without receiving magical bonuses based on identity.

## Player control

A player controlling the dominant actor can accept the entity, contest it, or attempt to preserve independent command during the transition.

Accepting the entity gives control of the final state or preserves player control through the safest supported route.

Contesting the claim creates a rival actor or internal war and places the player against the terminal state.

A player controlling a victim government receives immediate objectives and coalition choices.

In multiplayer, no player country should disappear without an explicit handoff, consent path, or documented terminal takeover rule.

A human dominant actor makes the accept, contest or independence choice before any promotion or merger.
Contesting must start a real war against the new final command or create a rival claimant, and non-jihadist actors are never subordinated automatically.

## Super-event presentation

The reveal and defeat super-events are implemented with researched titles, quotes, remarks, images and licensed audio.
Their research records live under `docs/super_events/031_random_terror/`.
Any revision keeps these rules:

- preserve uncertainty about the entity and show it only indirectly
- no depiction of Allah, sacred calligraphy, real extremist emblems, modern equipment, or a generic fantasy demon
- no Quranic verse as villain presentation, no sacred Islamic phrase as a button, and no invented or misattributed quote
- no Quran recitation, call to prayer, Islamic sacred chant, generated audio, drones, test tones, or unlicensed music
- every quote and audio cue keeps its source and rights evidence

## Entity portrait and animation

The entity is an impossible fictional subject and can use native ImageGen through the portrait worker.

The static portrait must work at `156x210`.

One animated portrait or transparent portrait overlay is justified because the visual state marks a terminal identity transformation.

A possible loop can show subtle impossible light, shifting shadow, or a presence that does not remain optically stable.

Every frame must be separately generated or edited under the frame-animation rules.

Transform-only motion, glow filters, or a GIF made from one shifted still cannot be the final asset.

The animation needs a static fallback and verified GUI consumer before implementation.

The animated portrait belongs to the terminal state.
Before the revelation, including the Evolution V entry in Event Details, the static portrait is shown.

## Defeat aftermath

Defeating the final command qualifies for a major aftermath because the threat was global, prolonged, and destructive.
The world does not return to normal at once, but the aftermath is kept to a few consequential choices.

- The reflective defeat super-event and news report announce the outcome.
- Liberated states keep their damage and become recovering states, so the ordinary Support Victims, Restore Services and Restore Civil Authority actions carry the reconstruction.
- Each government that held liberated territory receives one accounting event about prisoners and defectors. Tribunals raise Response Legitimacy and lower recurrence but cost stability. Broad amnesty ends the remaining cells faster but lowers legitimacy and leaves Dormant traces. Summary punishment ends the crisis quickest, adds Condemnation and disqualifies the No Collective Punishment achievement.
- Surviving splinter cells remain as Dormant traces under ordinary Event 31 rules.
- Chaos falls through the reversal rows of the Part 10 Chaos impact map. Deaths and Condemnation history stay.

The earlier plan items for a counterterror compact, a debate over the entity's nature and recurring vigilance events are folded into the accounting event text and the defeat news, and do not become separate systems.

## Event Details public branch

The False Revelation receives one stable public scenario registry row owned by Event 31.

The row includes:

- branch title
- premise
- terminal-state summary
- current enabled state
- current broad availability state when useful
- persistent independent toggle

It must not show:

- Apocalyptic Readiness
- exact territorial score
- exact capital count
- hidden MTTH
- entity identity
- secret transition branches

Disabling the row skips automatic selection and leaves Event 31 active.

## World-threat interaction

The final state activates the strongest Event 31 world-threat source.

Defeat, collapse, or terminal replacement clears or updates the source through the shared aggregate.

The world-threat flag must reflect real surviving qualifying actors and not remain active after total cleanup.

## Acceptance cases

The world-end branch is complete only when:

1. It cannot fire below `1000` Chaos.
2. It cannot fire before Evolution V is enabled and recorded.
3. It cannot fire when its public toggle is disabled.
4. It requires substantial territory, widespread crises, unity, and a major strategic victory.
5. Eligibility starts a delay instead of an immediate transition.
6. A failed transaction does not set `world_end`.
7. Existing actors merge, subordinate, reject, or fragment without duplication.
8. Player-controlled actors retain a clear control path.
9. Uprisings require actual prior pressure or cells.
10. Final abilities remain extreme and respond to command, territory, supply, unity, and counterplay.
11. Muslim religious and governmental opposition is visible and mechanically meaningful.
12. The game never confirms that the entity is Allah.
13. No sacred Islamic audio or real extremist visual is used.
14. Ordinary random events freeze while terminal content continues.
15. The final state is special Chaos but not actual nonhuman.
16. Defeat creates a structured aftermath and a separate researched super-event.
