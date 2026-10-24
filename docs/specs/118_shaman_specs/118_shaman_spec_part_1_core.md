# Shaman, Part 1: The visit and its place in the campaign

## Design identity

| Field | Specification |
| --- | --- |
| Requested event identity | 118, Shaman |
| Original catalog identity | 129 |
| Proposed runtime namespace | `chaosx.nr118` |
| Type | Minor Fire-Once, one opening across the campaign |
| Chaos level | 1, the existing Calm World entry tier |
| Proposed catalog status | To Be Reworked only after an accepted migration and corresponding root exist |
| Import snapshot catalog status | Unavailable, per parent-provided 2026-10-24 catalog evidence |
| Cluster | None |
| Evolution | True Sight, Chaos 400 or above |
| Principal actor | The major country directly controlling the selected home state at entry |
| Geographic scale | One culturally defined home region, with at most three states under an active rite |

This is an imported proposed design.
Parent-provided pre-migration catalog snapshot for 2026-10-24 places Shaman at 129 and Plague of locust at 118; both rows were Unavailable. The user has since approved adopting ID 118 and migrating the catalog, which the parent owns.
This curator did not independently inspect the workbook or runtime registry.
The requested design identity is retained here.
The implementation handoff preserves both legacy concepts and requires an explicit catalog migration entry.
This document does not claim that the event has been implemented or that a workbook row has changed.

All labels for choices, phases, outcomes, achievements and assets in this package are working design labels.
They specify purpose and structure.
They are not final localisation.

## The experience

A regional religious practitioner seeks an audience with the government that controls their home.
Local intermediaries establish where the visitor comes from, what community recognizes the role, and why an audience is possible.
The government is offered help with a problem close to that home.
It can accept a land blessing, ask for military guidance, or end the visit peacefully.
It can also persecute the visitor, risking a local political consequence.

The best initial use is concrete.
A state with food shortages can receive substantial relief.
A damaged district can recover sooner.
A threatened frontier can benefit from local supply, movement and preparation.
A calm state can gain a useful seasonal reserve.
The government pays for the material work surrounding a rite and accepts uncertainty about its extraordinary result.

The supernatural question remains unresolved.
A successful harvest could reflect local expertise, favorable conditions or a miracle.
A military setback could reflect deception, poor judgment or something more disturbing.
The player receives an honest account of observed effects without an omniscient identification of the visitor.

At Chaos 400 or above, an accepted relationship can develop into True Sight.
Visions name a state, a concrete threat and a time window.
They support preparation decisions, some of which prove useful and some of which waste scarce capacity.
The first rite remains a single opportunity.
The evolved relationship can produce up to three separate visions over time.

## What makes decisions consequential

The player decides where a scarce benefit belongs.
Choosing a calm region for a harvest reserve leaves an existing crisis untreated.
Choosing military guidance only helps a frontier near the visitor's home.
Waiting for a careful rite can miss an approaching attack.
Rushing can deliver help sooner while increasing the chance of a poor result.

The government also decides how to treat local authority.
Cooperation makes work easier.
Occupation and strained relations make access more difficult, without changing the community's underlying likelihood of producing an honest person or a supernatural one.
Persecution is a political act with local consequences.
It does not reveal the hidden identity or create a replacement visitor.

True Sight asks a further question.
How much present capacity should be committed to an uncertain future?
Existing official disaster information remains accessible.
A vision can focus attention on a particular consequence or a queued follow-up, and its accompanying preparation can add protection.
The player can compare it with official information instead of being required to trust it blindly.

## Opening eligibility

The ordinary event pool may consider Shaman only when the event is enabled, its global opening has not been consumed, and at least one valid host and regional profile exist.
A host must be an existing, non-capitulated major country using the normal civilian systems.
Its capital and government must exist.
Its selected home state must have an existing owner and controller that both qualify for those systems, and its current controller must be the host itself.

Direct control is essential.
An overlord cannot receive a visitor merely because a subject controls suitable territory.
A major occupying suitable territory can receive the event.
The visitor's community remains that of the territory.
A change of flag does not convert a Korean practitioner into a Japanese one or an Alaskan practitioner into a generic national archetype.

Home states come from the reviewed regional profile manifest in Part 4.
State IDs are resolved against the implementation checkout and installed map before activation.
Culture is never inferred from the controller's tag, an entire continent, climate alone, or the nearest existing character portrait.
A profile without a verified map binding is unavailable.
Other validated profiles remain usable.

A host needs a valid land-rite target in the home region.
A crisis is preferred but is not required.
A calm inhabited state can receive the seasonal form of the land blessing.
Military guidance is offered only when its separate operational conditions are met.
An empty or invalid pool leaves the opening unconsumed and provides the shared event list with a specific unavailable reason.

### Selection

Choose the host before the opening history entry is recorded.
Eligible majors have equal base weight.
Multiply a host's weight by 1.5 if at least one eligible regional state has an active civilian crisis, and by 1.5 if an eligible regional state is on an active hostile land frontier.
These multipliers cap at 2.0 combined.
Having more cultural profiles or more controlled states does not multiply the host's tickets.

Within the chosen host, select a valid profile with weight 1, doubled if it contains the selected civilian or frontier urgency.
Select its home state uniformly from the reviewed community anchors that pass current control and safety gates.
A country cannot reroll profiles by reopening the audience.
Persist the chosen host, home state, profile and encounter generation before dispatch.

The three distinct pools are host, profile and home state.
Their actual campaign probabilities depend on all eligible candidates.
The package's balance calculations concern the stated weights and named fixtures, not a claim about every possible campaign.

## The regional boundary

Each profile contains a finite set of reviewed states representing a specific community's home and plausible neighboring working area.
The selected home state anchors the visit.
The active region is the subset currently directly controlled by the host and eligible for civilian or military work.

A land rite chooses one state from this subset.
Military guidance chooses one operational focus state and up to two directly adjacent, eligible states from the same profile.
Adjacency alone never extends the effect beyond the cultural region.
A province across a remote sea, an allied state, a subject state or a newly conquered distant state does not join the region.

The player sees the home state and all selected targets by their current proper map names.
A target selector offers at most three ranked candidate rows at a time.
Ranking is actual crisis severity, then immediate local military exposure, then population and relevant damage.
A next-page control may browse the remaining finite manifest.
Selecting a target reveals the effect, cost, duration and current conditions before commitment.

The home identity is immutable.
Target selection can change before payment.
Once a rite or prophecy response is committed, its state and receipt are fixed.

## Arrival and audience

The opening report establishes the regional identity, the intermediary who makes the audience credible, current local circumstances and the government's practical choices.
It avoids claims that a real community uniformly supports the visitor.
The visible evidence can be a delegation, a local official's report or an attributed community relationship, as appropriate to the profile.

The audience has three outcomes.

| Choice function | Immediate result | Later consequence |
| --- | --- | --- |
| Peaceful refusal | The visitor leaves, no payment and no punishment | Opening consumed, contact closed, no unrest from refusal |
| Welcome | Open the one-rite offer and establish a regional contact | The government may choose a rite within 90 days and may later qualify for True Sight |
| Persecution | Close the contact and cancel the offer | Resolve the bounded local reaction described below |

Peaceful refusal is the harmless first option.
Closing or timing out the audience after 30 days follows it.
The available options must be revalidated when clicked.
An old popup cannot charge, persecute or welcome a successor generation.

Welcome is free.
It creates no national spirit or perpetual payment.
It adds 10 Local Cooperation points and gives the government 90 days to select one rite.
Expiry of that selection window closes the original offer peacefully.
The contact remains eligible for True Sight while its home and host remain valid.
The government can explicitly end the relationship at any later idle point.

## Local Cooperation

One persistent public value supports the relationship: Local Cooperation, from 0 to 100.
It represents willingness to assist this government's work.
It does not measure the worth, credulity, religion or supernatural ability of a community.

| Starting political context | Before welcome | After welcome |
| --- | ---: | ---: |
| Host core state, no active occupation conflict | 60 | 70 |
| Peaceful non-core administration | 45 | 55 |
| Host controls the home state during an active war against its owner | 30 | 40 |

Use the third row before the second.
These are gameplay relationship assumptions, not historical measurements.
All profiles use the same rules.
Cooperation bands are strained at 0 to 34, workable at 35 to 64, and strong at 65 to 100.
The header shows the value, band and most recent cause.

Effective rites add 10, exceptional rites add 15, inconclusive rites subtract 5, and adverse rites subtract 15.
Completed practical aftercare adds 10 once.
A supported warning with useful completed preparation adds 10.
A visibly false alarm after a paid response subtracts 10.
A void warning makes no change.
Every change clamps to the range and records its cause.

Cooperation changes rite outcome weights in Part 2.
It never changes the hidden identity distribution.
It also affects the cost of reconciliation after a public false alarm or an adverse rite.
It is not a currency and cannot be bought through a repeatable improve-relations button.

## Persecution and local reaction

The opening records whether the visitor has visible local backing.
Backing is a narrative context flag drawn independently of hidden identity: 70 percent established backing, 30 percent limited backing.
The report makes that distinction clear.
It can never be inferred from ethnicity, religion or occupation status.

Persecution causes a reaction with base chance 60 percent for established backing or 25 percent for limited backing.
Add 15 percentage points during hostile occupation.
Cap at 75 percent.
The reaction draw occurs once when the order is committed.
The absence of a reaction never proves that the visitor was a fraud.

In an occupied non-core home state, the reaction adds 10 percentage points of resistance target for 90 days through the applicable state owner contract.
It does not set a state's absolute resistance or manufacture a revolt country.
In a core home state, and in non-core states without an applicable resistance system, it causes a 15 percent local production and construction disruption for 90 days through a state-scoped modifier.
Only the home state is affected.
The exact applicable modifier binding is an implementation verification gate.

The government may repair relations once with an acknowledgement and practical relief package.
It costs 50 political power and 100 support equipment, scaled only by shared cost rules, and starts 30 days of work during which no second coercive action by this event may occur.
The offer opens immediately after the reaction and can be accepted for 30 days.
The quiet-period requirement is checked at completion, not before entry.
It shortens the remaining event-owned disruption by half, rounded up, and does not erase unrelated resistance or damage.
The visitor does not return, and the rite remains unavailable.
No benefit is awarded merely for creating unrest and then settling it.

An initial persecution choice is an authored state action without an automatic execution or civilian death.
If later integration adds physical injury, it must be based on a separately approved concrete consequence and the shared measured-loss owner.
The present design's consequence is local disruption.

## Relationship duration and endings

After the original rite or its selection window ends, the visitor returns home and remains a contact.
This idle state carries no maintenance cost and no recurring passive bonus.
It produces no further work until the True Sight gate can operate.
The government may end contact peacefully while no response confirmation is pending.
Ending contact during an active job cancels that job under its payment and expiry rules.

The relationship closes after peaceful dismissal, persecution, host annexation, invalid civilian classification, loss of the home state's direct control, or completion of the third evolved vision.
A fall from major status after a valid opening does not itself break an existing relationship.
The original government remains the actor while it exists.
A civil-war successor or conquering government does not automatically inherit the visitor.

Loss of a supporting military state cancels only work or benefits on that state.
Loss of the chosen military focus state cancels the entire guidance package.
A land target that is not the home state can be lost without ending the contact, but its action and undelivered benefits retire.
It does not transfer the bargain.
Loss of the home state closes the relationship.
Control loss is processed immediately through the exact affected-state hook, with due-work validation as a second guard.
Recovering the state does not create a second opening or restore a canceled random draw.

Physical relief already delivered, real repairs already completed and conventional fortification built during a preparation window remain physical history.
Unused reservations are released.
Temporary benefits bound to this government expire or are removed according to their receipts.
Ending contact never reverses actual deaths or recreates spent equipment.

## Evolution entry

True Sight requires a welcomed, still-valid contact, the shared evolution enable setting, and Chaos at least 400.
If Shaman first opens at 400 or above, use an evolved opening variation.
Welcome activates the evolution immediately, after the audience choice is accepted.
Peaceful refusal and persecution do not activate it.

For a contact welcomed below 400, an eligible waiting process begins when the threshold is reached.
Its baseline median waiting time is 90 eligible days.
An exceptional initial rite multiplies that time by 0.75.
A currently actionable regional threat multiplies it by 0.75.
Chaos at least 600 multiplies it by 0.75.
Clamp the resulting median to 30 through 180 days.
Shared evolution timing should reproduce those design medians without adding another polling framework.

Days below 400 do not advance eligibility.
An activation check that finds the contact invalid does nothing.
Once activated, True Sight remains part of the encounter even if Chaos later falls.
Activation writes one evolution history entry with the host as actor and adds zero Chaos.
The first vision waits for a valid candidate.
It never starts a disaster in order to populate the offer.

## Campaign examples

An early American opening in an eligible Alaskan community can offer civilian recovery during peace.
Military guidance is unavailable if the government is fighting only in Europe.
The same region can support guidance if a later war produces an active local frontier and eligible troops before the original offer expires.

A Soviet-controlled Baikal profile can assist a genuine local shortage or a nearby defensive operation.
The visitor's cultural identity comes from the chosen home community.
Soviet control does not select a generic Russian ritual costume.

A Japanese government controlling an eligible Korean home state receives a Korean regional visitor with a colonial relationship context.
The state's non-core status affects cooperation and the political consequences of persecution.
It does not change the hidden chances of fraud or supernatural power.

These are gameplay illustrations subject to Part 4's actual source and state-binding qualifications.
They are not claims that any historical practitioner offered wartime supernatural assistance to those governments.
