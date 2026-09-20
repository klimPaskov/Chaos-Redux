# Shared systems, clusters, and Chaos accounting

Event 069 owns the Boxer crisis and its political and military relationships.
It should use the project's existing shared systems for effects they already represent.
The implementation must bind the contracts below to actual current helpers after reading their source.
The contract names in this document describe responsibilities and are not claims that a function with that exact name already exists.

## One event in two clusters

The catalog membership is Domestic Unrest with Severe severity and Diplomacy with Medium severity.
Both memberships refer to the same event ID and the same fire-once state.
They do not create two copies of the event or two independent chances to grant its opening effects in the same selection beat.

The Domestic Unrest role concerns the movement's challenge to internal authority.
The Diplomacy role concerns foreign interests, ultimatums, intervention, and settlement.
A firing can begin with a strong domestic role and develop a larger diplomatic role later.
Its catalog identity remains Minor Fire-Once.

Use the existing cluster selection and burst contract.
A cluster firing counts as one pacing beat, and each member must remain independently valid.
Deduplicate Event 069 across the two membership paths before dispatch.
A failed target search must not consume the fire-once state or leave half of the opening initialized.

## Event-system integration

Preserve the existing entry namespace `chaosx.nr69.1` and use `069` for new event-scoped filenames.
The rework must replace the old assumptions of a CHI-only recipient, a fixed fascist civil war, and the unconditional five-million-manpower loss.
No compatibility wrapper may keep those effects active behind the new opening.

Wire the event's classification, registration, target preparation, name mapping, history actor, Event Details, evolution previews, settings behavior, and documentation together.
When an actor is needed for the generic history row, prepare it before the shared fired-event handler records the row.
Do not invent a default Chinese actor when the actual controller or movement actor has not been resolved.

The event remains in the unreworked default-disabled state until implementation and its required completion evidence are actually ready.
This planning package does not change the catalog status or the runtime allowlist.

## Shared-system contracts

| System | Information Event 069 supplies | Information it consumes | Integration rule |
| --- | --- | --- | --- |
| Country and carrier registry | Event origin, package identity, required anchor, activation and cleanup | Living and reserved carriers, origin guards, existing content ownership | Never load another event's package merely because a carrier is listed |
| Deaths and casualties | Incident identity, location, victim group, responsible actor when known, actual count | Existing recorded losses and attribution rules | Count once, distinguish recruitment and migration from death |
| Famine and relief | Siege or blockade cause, affected sites, route restrictions, relief commitments | Current civilian needs and supported relief actions | No separate Boxer food or relief meter |
| Migration | Real evacuation or displacement cause, source, destination, and affected group | Population movement and capacity rules | Evacuated people cannot also be killed or recruited by another receipt |
| Condemnation | Confirmed conduct and responsible actors | Existing norms and reactions | Do not award condemnation for mere possession of weapons or an unverified rumor |
| Contamination and outbreaks | A relevant actual attack, exposed location, and protection context | Current contamination, outbreak, and protective-equipment behavior | Rituals do not bypass normal exposure or create a second contamination pool |
| Crisis budget | Actual affected country and active crisis phase | Current eligibility and concurrency policy | No private bypass of the shared cap |
| Event log | Parent ID, real actor, milestone, evolution context, outcome | Shared history and detail views | One factual record per milestone, not a popup-driven duplicate |
| Triggerable scenarios | Type, intensity, resolved participants, explicit launch context | Existing confirmation and scenario registry | Manual setup is separate from natural eligibility and pacing |
| CXT testing extension | One idempotent package setup and its ownership token when required | Existing dynamic registration and synchronization contract | No duplicate test country system or unbounded world hook |

The mechanics document and country registry were read for this planning pass.
The complete implementation bodies for all the shared systems above were not read.
Their exact helper bindings and engine behavior remain part of the source-review gap recorded in `research/source_review.md`.

## Named event connections

### Chemical and Biological Weapons Convention

The convention can affect which intervention methods a government considers acceptable and how violations are judged.
Read the actual ratification, prohibition, condemnation, and AI interfaces before connecting them.
Do not infer a ban from a country's ideology or from the mere fact that a foreign coalition exists.

A chemical or biological attack in the theater is handled by the existing warfare and civilian systems.
It can damage a government's credibility, strengthen a local grievance, or divide the intervention coalition.
Any resulting casualties and contamination remain under their shared accounting.
A Boxer ritual does not grant immunity in place of masks, equipment, medicine, or the supported protection mechanic.

### The Offensive

The Offensive can make relevant AI plans more aggressive through its actual shared behavior.
Event 069 still applies validity, supply, access, and resource checks.
The connection changes AI willingness and planning.
It does not force a human player to attack or make an impossible operation available.

### Independence Wave

A newly released country can alter the local government, foreign interest, and occupation relationships inside the theater.
Refresh the affected records and preserve the releasing event's origin and country-content ownership.
Do not grant Event 006 equipment, ideas, or a focus tree again simply because the new country joins the Boxer crisis.

The registry's current active collections and dormant reservation rules are established project interfaces.
Event 069 still needs its own identity and map proof when reusing a carrier.

### Subjects Break Free

A subject's independence can change whether its territory counts as foreign-controlled, whether it can choose its own stance, and which government is responsible for an existing commitment.
Use the actual new autonomy and ownership state.
Do not automatically dissolve the Boxer movement or transfer every foreign claim when the subject becomes independent.

### The Black Market

The market can provide a real supply path to societies, Chinese governments, or collaborators when the existing market system and a valid transaction are available.
Every purchase must have a payer, delivered allocation, route, and recipient.
A delivery failure must not still create the equipment in the recipient's stockpile.

The baseline event remains playable without the Black Market.
Ordinary donations, captured allocations, and domestic production supply the movement through their own real accounting.
Do not invent a parallel market currency for Event 069.

### Random Civil War

A civil war can split authorities, change controllers, move equipment, or create a rival Chinese government.
Refresh the affected local records and commitments.
Support follows actual governments and ownership, not a permanent assumption that CHI represents every Chinese state.

An existing civil war does not automatically become part of every foreign participant's war.
The intervention and Chinese pact logic must inspect the real war graph before changing diplomacy.

These named connections are required design integrations where their corresponding runtime systems exist.
The current bodies of all six event packages were not exhaustively inspected in this run.
The implementation must report an absent or incompatible connection rather than claiming it is already wired.

## Chaos impact ledger

Boxer Strength and Intervention Pressure are not direct conversions into the global Chaos Meter.
A high local value does not continuously add Chaos every day.

| Development | Chaos treatment | Anti-duplication rule |
| --- | --- | --- |
| Natural source firing | The shared catalog pipeline applies the normal Chaos-level-1 behavior | No second manual opening increment inside the event |
| A stance change, conference, mandate, or country classification flag | No automatic additional Chaos | Political bookkeeping is not itself a separate disaster |
| Evolution I, II, or III activates or is logged | Zero Chaos | No concealed award in the unlock, log helper, focus grant, or scenario wrapper |
| A real war, peace, annexation, liberation, subject change, or faction change | Use the established shared contribution for the actual consequence | Do not add a second generic war or territorial-change reward |
| Recorded deaths, contamination, or world-tension effects | Use the existing shared accounting | Do not add an Event 069 copy of the same contribution |
| First coordinated collapse of several major theater transport sites for 30 days | Proposed event-owned +5 when it is a distinct recorded infrastructure crisis | Once per natural crisis generation, and only when no shared system already owns the same consequence |
| Durable restoration of that recorded transport breakdown | Proposed event-owned -5 | Requires its original receipt and a completed restoration, once only |
| Completion of ordinary recruitment, training, repair, or a payment | No automatic additional Chaos | These actions do not become repeatable global Chaos controls |
| A major new anomalous consequence | Define its concrete effect first and check shared ownership | No Chaos merely for revealing or using an evolution |

The proposed transport contribution is a design addition requiring review against the current shared impact rules.
If the shared system already represents it, use that owner and remove the duplicate event-owned contribution.
This is an accounting reconciliation, not permission to delete the underlying infrastructure crisis.

## Runtime ownership and scheduling

The crisis has a stable generation identity, registered participants, registered states and sites, current commitments, outcome receipts, and a bounded scheduler.
Ownership changes repair only the affected records and their dependent targets.
The periodic repair pass iterates the event's bounded theater and participant lists.
It must not introduce a new whole-world daily or weekly scan.

A coordinator country is an execution host, not the owner of the entire crisis's meaning.
If that country disappears, the persistent registry and outstanding commitments must allow a valid surviving host to continue the event.
The replacement process cannot restart the opening or lose all foreign objectives.

Repeated hooks coalesce into one pending refresh.
The implementation must distinguish scheduled delivery from pending work so that an immediate update and a queued event do not both apply the same change.
Cleanup validates every remaining reference before returning allocated assets or closing tasks.

## Human population and special countries

The Boxer government is a human country even when its religious route develops a genuine anomaly.
It continues to use ordinary civilian systems.
Do not classify it as nonhuman to avoid migration, famine, disease, or other difficult integration work.

A nonhuman occupier or a country whose own package forbids ordinary diplomacy must not receive invented consulates, normal civilian missions, or a standard reparation conference.
Use the actual supported role of that actor.
A human protection or anti-occupation objective can remain valid without pretending that the occupier has ordinary diplomatic institutions.
