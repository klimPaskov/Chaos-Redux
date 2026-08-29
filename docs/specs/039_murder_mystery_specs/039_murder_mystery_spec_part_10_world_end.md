# Murder Mystery Specification Part 10: World of Anarchy

## Terminal role

World of Anarchy is Event 39's public world-end branch. It begins only when the Assassin movement deliberately starts a worldwide campaign to dismantle ordinary state leadership. It is a terminal war and government-replacement system, not a strong modifier or one global declaration event.

The branch remains separately enabled by default in Event Details. Disabling World of Anarchy removes it from automatic terminal readiness without disabling Event 39, the Assassin State, or Evolution V content.

## Activation requirements

World of Anarchy may activate only when:

- global Chaos is at least 1000
- no shared `world_end` state is active
- Event 39 reached Evolution V
- the central Assassin State or valid movement heir exists
- the central country controls a viable capital or active campaign command
- Brotherhood Cohesion meets the route-specific minimum
- terminal command settlement is complete
- the public branch toggle is enabled for automatic access
- required terminal assets, super-event, audio, text, and country replacement systems are ready
- no incompatible event-owned country transaction or world-end setup is in progress

Manual scenario intensity does not bypass these requirements unless a future dedicated terminal scenario is separately specified.

## Activation transaction

1. Recheck every hard requirement.
2. Set the shared world-end state and Event 39 terminal flag.
3. Freeze normal automatic event firing through the shared world-end contract.
4. Lock incompatible Event 39 evolution and country creation paths.
5. Initialize the terminal eligible-government registry.
6. Initialize campaign sectors and victory counters.
7. Apply route-specific terminal command structure.
8. Reveal the World Without Leaders decision category.
9. Set the matching super-event visibility and unique audio ID.
10. Play the settings-aware super-event audio.
11. Fire the World of Anarchy super-event after setup succeeds.
12. Begin the first campaign sector after player or AI selection.

If setup fails, the transaction must not leave `world_end`, terminal presentation, frozen event selection, or partial registries active.

## Eligible ordinary government classifier

A country is an ordinary terminal target when it:

- exists as an independent or relevant government actor
- uses normal civilian systems
- is not a special Chaos country
- is not an actual nonhuman country
- is not the central Assassin State, a valid Assassin derivative, or a protected Event 39 administration
- is not already dismantled, annexed, or registered as terminally resolved
- has territory, government, or exile structure that the terminal system can process safely
- has a safe country and character disposition for government dismantling

Special Chaos countries remain exempt from ordinary leadership extermination. They can fight, ally, remain neutral, or interact through their own logic. Their leaders, populations, and government structures must not be processed through human office assumptions.

## Registry and performance model

The terminal system builds a bounded registry at activation from valid countries, then updates it through country creation, capitulation, annexation, liberation, and terminal administration hooks. It does not perform a daily whole-world scan.

The registry tracks target status, sector, current war relation, cell presence, government protection, administration outcome, protected-character disposition, and victory contribution. Dead or transformed entries are retired immediately.

Periodic terminal work iterates only the registry or active sector. A full rebuild is allowed only at activation, explicit debug repair, or a rare bounded reconciliation event.

## Campaign sectors

The world is divided into strategic sectors using existing regional or continent groupings and live country state. The player normally campaigns in one to three active sectors. The system does not declare simultaneous war on every government in one day.

A sector can become active through:

- direct selection by the Assassin player
- AI strategy based on borders, cells, subjects, logistics, and enemy strength
- a mature network wave
- a government coalition attack on the movement
- completion of the previous sector mandate

Sector activation can declare wars, awaken cells, assign subjects, and create objectives in a bounded wave. Countries already at war with the movement join the active sector state without duplicate declarations.

## Global war model

World of Anarchy creates a worldwide conflict through phased fanout. The movement's enemies can form coalitions, join existing factions, guarantee threatened governments, or fight separately according to campaign state.

The system should avoid forcing every ordinary country into one faction. Existing diplomacy, ideology, factions, rivalries, and wars should continue to matter. The common threat can produce cooperation without erasing the map's political history.

The Assassin side includes the central state, foreign derivatives, eligible subjects, and selected uprisings. Ordinary puppets of Assassin administrations follow their owner only when their package and protected status are valid.

## Leadership pressure during war

World of Anarchy increases assassination and office-disruption capability, but safe character rules remain absolute.

The movement can target:

- ordinary national leadership with verified succession or terminal replacement
- command staff and advisors with explicit Event 39 dispositions
- generic ministries, courts, intelligence offices, and local administration
- campaign headquarters and communication nodes

The system must preserve protected characters owned by unrelated special systems. It must never delete every commander or leave an ordinary country without a valid acting government before the conquest transaction resolves.

Leadership attacks should create military and political consequences, not automatic capitulation. They can lower planning, delay focus or decision action, damage Cohesion of a coalition, expose a capital, or change target protection.

## Government dismantling transaction

When an ordinary target capitulates, accepts terminal surrender, or is fully conquered, the event performs one country-specific dismantling transaction.

### Preflight

- identify the defeated government and all relevant states
- validate war, capitulation, peace, faction, subject, exile, and protected-country state
- resolve every eligible leader and office through the safe disposition registry
- select a valid administration outcome
- reserve the required dynamic carrier or subject identity
- validate capital, territory, economy, supply, and population
- preserve unrelated event ownership and protected characters

### Character handling

The transaction removes or retires only safe eligible leaders and offices. Protected characters move, remain in exile, transfer through owner callbacks, or become unavailable according to their system. Generic office casualties represent unregistered administration loss.

A conquered country's terminal record stores the offices dismantled, protected exceptions, successor administration, and date. It prevents duplicate death and replacement processing.

### Administration outcomes

#### Central subject administration

Creates a subordinate Assassin administration with a viable capital, local forces, staged control, and central obligations. Favored by The Hidden Hand.

#### Autonomous cell territory

Creates a decentralized local territory that joins the movement but retains wide autonomy. Favored by Cells Without Masters.

#### Temporary campaign council

Creates a revocable administration with a defined mandate. Authority can expire or be renewed. Used by the decentralized terminal command settlement.

#### Staged integration

The central state directly controls strategic territory while local decisions integrate the rest. Favored by The Necessary Mask when it returns to the terminal route.

#### Existing derivative elevation

If a valid local Assassin derivative already exists, it can receive the conquered territory through staged integration instead of creating another tag.

No outcome grants instant universal cores. Resistance, compliance, supply, local population, protected systems, and postwar decisions remain relevant.

## Treatment of civilians

World of Anarchy targets organized leadership and government institutions. It is not a license for an unbounded civilian extermination mechanic. Civilian deaths can occur through war, occupation, failed administration, reprisals, and specific mapped actions, all through the shared deaths system.

Route choices affect population treatment:

- centralized rule may impose strict security and forced transfers
- decentralized rule may create local disorder and uneven protection
- pragmatic administration may preserve services at a Cohesion cost

The player should face consequences for destructive administration. Deaths, migration, famine, condemnation, resistance, and Chaos integrate through their shared systems where relevant.

## Network and uprising integration

Active cells in a sector can:

- provide reconnaissance and target information
- sabotage rail, supply, or communications through bounded actions
- protect landing or uprising points
- create local revolt candidates when map safety passes
- lower the cost of a subject administration
- help identify safe character and office targets

A cell cannot create a derivative after its country has already been dismantled or assigned to another Event 39 administration. The transaction chooses one owner.

## Terminal command contradiction

The Assassin side must maintain playable coordination while claiming that leadership should disappear.

### Hidden Hand outcome

A concealed central command survives behind nominally leaderless administrations. High military efficiency comes with severe ideological hypocrisy, succession risk, and subject resentment.

### Cells Without Masters outcome

Campaign councils receive limited authority for one sector or mandate. Military coordination is weaker, but local administrations are more autonomous and survive central collapse better.

### Necessary Mask outcome

A formal temporary state directs the war and promises dissolution after victory. It gains strong logistics and diplomacy but faces hard-line rebellion if the promise is delayed or broken.

Brotherhood Cohesion changes after every sector, major conquest, command appointment, leader loss, and administration choice.

## Victory condition

World of Anarchy reaches terminal victory when no eligible ordinary independent government remains outside one of these states:

- dismantled and replaced by a valid Event 39 administration
- integrated into the central movement through an accepted terminal outcome
- protected special Chaos or nonhuman exemption
- no longer a country through unrelated valid campaign resolution that the terminal registry reconciles

The victory check uses the terminal registry and update hooks. It does not scan every country daily.

## Victory presentation and post-victory play

Victory triggers a terminal resolution event and a final super-event stage or ending presentation when the implementation framework supports it. The player then resolves the movement's command promise.

Possible post-victory outcomes:

- secret central command remains and the world is administered through subjects
- campaign councils dissolve into autonomous cell territories
- the temporary state refuses to dissolve and creates an internal legitimacy crisis
- a mixed settlement preserves strategic coordination while devolving local rule

The campaign remains playable. The player receives continuing administration, Cohesion, local conflict, supply, reconstruction, and subject-management content. Normal random event firing remains frozen by the world-end state unless the shared terminal framework permits a post-end event set.

## Assassin defeat

The terminal movement can be defeated through destruction of the central country and every viable heir, collapse of Cohesion, subject defection, loss of campaign command, and dismantling of mature cells.

A defeat transaction:

- ends Event 39 terminal readiness
- preserves the shared world-end resolution rules
- releases or restores countries only through valid existing or event-owned packages
- resolves protected characters and exile governments
- removes terminal decisions and sectors
- retires cells or places them in bounded hunted-remnant cleanup
- applies movement defeat Chaos reversal once
- triggers defeat aftermath presentation when the campaign was sufficiently large and costly

A short failed terminal activation does not automatically justify a global treaty. A long war with several dismantled governments, high deaths, and broad coalition participation can justify a defeat super-event and postwar compact.

## Defeat aftermath

When the movement reached Evolution IV or V, held several countries, operated for a substantial duration, and caused a major global war, ordinary victors may create a postwar protection and reconstruction compact.

Aftermath content can include:

- restoration or successor government decisions
- memorial and investigation records
- international counterintelligence cooperation
- limits on clandestine military networks
- rehabilitation of compromised institutions
- management of former Assassin administrations and subjects
- continuing low-level cell remnants with no evolution path

The aftermath should not become a generic new world order after a small local defeat.

## Super-event package

World of Anarchy requires its own unique super-event slot, image, title, description, button reaction, verified quote, licensed musical WAV, settings-aware playback, scripted localisation, docs, and catalog row. It cannot reuse the Evolution III reveal package.

The image should communicate organized leadership being removed across several ordinary governments while the movement's own hidden command remains. It should avoid graphic bodies, real political figures, religious imagery, and generic ninja art.

## Event Details contract

World of Anarchy appears as one public terminal row under Event 39. The row has independent persistent enable state, title and premise direction, terminal state direction, availability status, and a detail panel. The public text must not reveal protected-character registries, exact sector weights, or internal administration callbacks.

## Manual and debug access

Normal manual Event 39 fire respects event level and host eligibility. Force mode may bypass event selection gates but not impossible country, character, or map transactions. The Assassin Network scenario can prepare Evolution IV state at Maximum, but World of Anarchy still requires its own terminal gate.

Any debug launch must reuse the terminal setup effect and clear debug flags. No separate simplified world-end implementation is allowed.

## Acceptance standard

World of Anarchy is accepted only when activation is transactional, the public toggle works independently, eligible governments and exemptions are correct, global war fanout is bounded, leadership handling is safe, conquest creates viable administrations, victory and defeat are reachable, post-victory play functions, shared deaths and Chaos do not double count, performance avoids world scans, and the complete super-event package is final.
